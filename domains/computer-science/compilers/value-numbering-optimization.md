---
id: value-numbering-optimization
title: Value Numbering and Redundancy Elimination
domain: computer-science
course: compilers
prerequisites:
- id: code-optimization
  type: hard
- id: dataflow-analysis
  type: soft
tags:
- optimization
- redundancy
- CSE
stage: advanced
status: draft
---

# Value Numbering and Redundancy Elimination

## Core Idea
Value numbering assigns numbers to expressions based on their semantic value; identical expressions receive the same number. Redundant computations are then replaced with the first computation's result, achieving both common subexpression elimination and constant folding in a single, efficient pass.

## Questions

```yaml
- question: "A basic block contains: `t1 = a + b`, then `a = 5`, then `t2 = a + b`. Will local value numbering mark t2 as redundant and replace it with a copy of t1?"
  type: multiple-choice
  options:
    - "Yes — t2 and t1 both compute a + b, so they receive the same value number and t2 is eliminated."
    - "No — the assignment `a = 5` gives `a` a new value number, so the (operator, VN(a), VN(b)) key for t2 differs from t1's key, and t2 is not redundant."
    - "Yes — but only after a dataflow analysis pass confirms that `a` holds the same value at both points."
    - "No — value numbering only works for multiplications and divisions, not additions."
  answer: 1
  explanation: "This scenario is the canonical test of value numbering understanding. When `a = 5` is processed, `a` receives a new value number representing the constant 5 — different from the value number it held when t1 was computed. So when the algorithm reaches t2 = a + b, it forms the key (ADD, new-VN-of-a, VN-of-b), which is a different key from t1's (ADD, old-VN-of-a, VN-of-b). The table lookup fails to find a match, and t2 is correctly not eliminated. A common mistake is thinking value numbering tracks variable names syntactically; it actually tracks semantic values, and any reassignment creates a fresh value number."

- question: "Which of the following optimizations is performed automatically by value numbering without requiring a separate analysis pass?"
  type: multiple-choice
  options:
    - "Loop unrolling — value numbering detects loop bounds and duplicates loop bodies."
    - "Dead code elimination — value numbering marks unreachable instructions as unused."
    - "Constant folding — expressions like `3 + 4` receive the value number for the constant 7, and future uses are replaced by 7."
    - "Register allocation — value numbering assigns registers based on value lifetimes."
  answer: 2
  explanation: "Constants receive value numbers just like computed expressions. When the algorithm encounters `3 + 4`, it looks up value numbers for the operands (constants 3 and 4), forms the key (ADD, VN(3), VN(4)), and evaluates the result: the value number is simply assigned to represent the constant 7. Any later expression that computes 3 + 4 gets the same value number and is replaced with 7. Constant folding thus falls out as a free byproduct of the value numbering machinery, with no additional analysis needed."

- question: "Local value numbering can detect that `t3 = a + b` is redundant — even though it uses different variable names from an earlier `t1 = a + b` — as long as `a` and `b` have not been reassigned in between."
  type: true-false
  answer: true
  explanation: "This is the fundamental advantage of value numbering over purely syntactic methods. Value numbering tracks the abstract value computed by each expression, not the textual identity of variable names. If `a` and `b` have not been reassigned between t1 and t3, they hold the same values (same value numbers), so the same key (ADD, VN(a), VN(b)) appears in the hash table twice, and the second computation is correctly identified as redundant. The algorithm replaces t3 with a copy of t1 without needing to know or care that both instructions 'look like' the same text."

- question: "Value numbering identifies redundant computations by comparing the text of instructions — two computations with different variable names but equal results are never detected as equivalent."
  type: true-false
  answer: false
  explanation: "Value numbering explicitly avoids textual comparison. It maps each variable to an abstract value number based on what computation produced it, not what the variable is named. Two variables with the same value number represent the same computed value, regardless of their names. This is what makes value numbering more powerful than naive syntactic redundancy elimination: it can detect that `t3 = x + y` is the same as `t1 = a + b` if x and a hold the same value number and y and b hold the same value number — which happens when they were both assigned the same prior computations."

- question: "Explain how value numbering's hash table approach lets a compiler detect that an expression is redundant in a single forward pass, without re-examining prior instructions."
  type: short-answer
  answer: "The hash table maps (operator, value-number-of-left-operand, value-number-of-right-operand) to value numbers. As the algorithm processes each instruction, it looks up the operands' current value numbers, forms this triple as a key, and checks the table. If the key is present, the expression was computed before — it's redundant and can be replaced with a copy. If the key is absent, a fresh value number is assigned and stored. The table accumulates all previously seen value computations, so each new instruction only requires a single O(1) lookup to determine if it's redundant. No backward scanning is needed because the hash table is the accumulated memory of all prior computations."
  explanation: "The power of the hash table is that it provides constant-time lookup regardless of how many prior instructions exist. Instead of scanning backward through the instruction stream to find a matching computation, the algorithm simply hashes the current expression's semantics and checks if that hash key already exists. The key insight is that the value number of each operand already encodes everything relevant about what that variable holds — so looking up (operator, VN(op1), VN(op2)) is equivalent to asking 'has this exact computation been done before with these exact input values?' The answer is available in O(1) from the table."
```

## Explainer

Consider a basic block containing `t1 = a + b` followed later by `t2 = a + b`, where `a` and `b` have not been reassigned. A human reader immediately sees that `t2` is redundant — it computes the same thing `t1` already holds. **Value numbering** is the compiler's systematic way of recognizing this. It assigns each computed value a unique number, and when it encounters an expression whose operands have the same value numbers as a previously computed expression with the same operator, it reuses the earlier result instead of recomputing.

The algorithm maintains a hash table mapping (operator, value-number-of-left-operand, value-number-of-right-operand) to value numbers. As it processes each instruction in order, it looks up the operands' value numbers, forms the hash key, and checks the table. If the key is already present, the expression is redundant — the compiler replaces it with a copy from the variable that already holds that value. If the key is absent, a new value number is assigned and recorded. Constants receive value numbers too, which means constant folding falls out naturally: `3 + 4` hashes to the same entry as any other expression producing 7.

**Local value numbering** (LVN) operates within a single basic block and is simple to implement — a single forward pass suffices. From your knowledge of code optimization and dataflow analysis, you can appreciate why extending this across basic blocks is harder. **Global value numbering** (GVN) must reason about values that flow through multiple paths in the control flow graph. If `a + b` is computed in two predecessor blocks but with different assignments to `a`, the value numbers may differ along different paths. GVN typically uses a dominator-based approach: a computation in a dominating block is available to all blocks it dominates, so redundancies within a dominator tree can be eliminated safely.

Value numbering is particularly effective because it subsumes several optimizations at once. It eliminates common subexpressions, folds constants, and can even detect algebraic identities (like `x + 0` or `x * 1`) if extended with simple rewrite rules. It is also efficient — local value numbering is linear in the number of instructions, making it one of the best cost-to-benefit optimizations a compiler can perform.
