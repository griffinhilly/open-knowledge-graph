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

## Explainer

Consider a basic block containing `t1 = a + b` followed later by `t2 = a + b`, where `a` and `b` have not been reassigned. A human reader immediately sees that `t2` is redundant — it computes the same thing `t1` already holds. **Value numbering** is the compiler's systematic way of recognizing this. It assigns each computed value a unique number, and when it encounters an expression whose operands have the same value numbers as a previously computed expression with the same operator, it reuses the earlier result instead of recomputing.

The algorithm maintains a hash table mapping (operator, value-number-of-left-operand, value-number-of-right-operand) to value numbers. As it processes each instruction in order, it looks up the operands' value numbers, forms the hash key, and checks the table. If the key is already present, the expression is redundant — the compiler replaces it with a copy from the variable that already holds that value. If the key is absent, a new value number is assigned and recorded. Constants receive value numbers too, which means constant folding falls out naturally: `3 + 4` hashes to the same entry as any other expression producing 7.

**Local value numbering** (LVN) operates within a single basic block and is simple to implement — a single forward pass suffices. From your knowledge of code optimization and dataflow analysis, you can appreciate why extending this across basic blocks is harder. **Global value numbering** (GVN) must reason about values that flow through multiple paths in the control flow graph. If `a + b` is computed in two predecessor blocks but with different assignments to `a`, the value numbers may differ along different paths. GVN typically uses a dominator-based approach: a computation in a dominating block is available to all blocks it dominates, so redundancies within a dominator tree can be eliminated safely.

Value numbering is particularly effective because it subsumes several optimizations at once. It eliminates common subexpressions, folds constants, and can even detect algebraic identities (like `x + 0` or `x * 1`) if extended with simple rewrite rules. It is also efficient — local value numbering is linear in the number of instructions, making it one of the best cost-to-benefit optimizations a compiler can perform.
