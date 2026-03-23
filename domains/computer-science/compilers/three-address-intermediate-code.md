---
id: three-address-intermediate-code
title: Three-Address Intermediate Code
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: ast-node-representation
  type: hard
builds-toward:
- quadruple-intermediate-representation
- basic-block-analysis
tags:
- ir
- intermediate-representation
- code-generation
stage: advanced
status: validated
---

# Three-Address Intermediate Code

## Core Idea
Three-address code is a popular intermediate representation where each instruction has at most three operands and one operation. 3AC is linear (easy to optimize sequentially), easy to generate from ASTs, and straightforward to translate to machine code.

## How It's Best Learned
Write a code generator producing 3AC from an AST. Manually optimize 3AC to understand what compilers must do.

## Common Misconceptions
Three-address code is the only intermediate representation (SSA, bytecode, and tree-based IRs exist). All 3AC is equally easy to optimize (SSA form has special properties).

## Questions

```yaml
- question: "A compiler processing `x = (a + b) * (a + b)` generates 3AC. Which property of three-address code most directly enables the compiler to compute `a + b` only once?"
  type: multiple-choice
  options:
    - "Each 3AC instruction maps to exactly one machine instruction"
    - "Complex sub-expressions are broken into primitive operations assigned to named temporaries, making repeated computations visibly identical"
    - "Three-address code uses quadruple encoding for all instructions"
    - "Control flow is expressed as labeled jumps rather than nested structures"
  answer: 1
  explanation: "When `a + b` is computed the first time, it is assigned to a temporary: `t1 = a + b`. The second occurrence also generates `t1 = a + b`. Because each sub-expression has an explicit named result, a common subexpression elimination (CSE) pass can trivially detect that these are identical computations and replace the second with a reuse of `t1`. This would be far harder in the AST, where the addition is buried in two separate subtrees with no shared name. The explicit naming of temporaries is what makes redundancy visible."

- question: "A compiler uses triple encoding for 3AC, where the result of instruction i is implicitly named by index i (no explicit result field). An optimizer wants to move instruction 5 ahead of instruction 3. What problem does this create?"
  type: multiple-choice
  options:
    - "Triples require more memory than quadruples, so reordering would cause overflow"
    - "Subsequent instructions that reference '(5)' as an operand now refer to the wrong instruction after reordering"
    - "Optimization passes cannot operate on triple-encoded instructions at all"
    - "Triples only support arithmetic operations, not control flow instructions"
  answer: 1
  explanation: "In triple encoding, an instruction refers to earlier results by their numeric index: `(3) = b * c` means 'the result of instruction 3.' If you move instruction 5 before instruction 3, all the index references shift — what was instruction 3 is now instruction 4, and any instruction that referenced '(3)' now points to the wrong operation. This is the key disadvantage of triples versus quadruples: quadruples give each result an explicit name (a temporary variable), so instructions can be reordered without invalidating references. Indirect triples add a pointer table to recover reordering flexibility."

- question: "Three-address code makes common subexpression elimination (CSE) easier than performing the same optimization on an AST, because the same sub-expression appears as identical instruction sequences with named results."
  type: true-false
  answer: true
  explanation: "In an AST, the subexpression `b * c` might appear in two subtrees with no explicit shared name — recognizing them as identical requires a tree-matching pass. In 3AC, both instances generate `t = b * c` (or identical operand sequences), so a simple linear scan can detect the match. The flattening of the tree into a sequence of named, primitive operations is precisely what exposes redundancy at a granularity where pattern matching is tractable."

- question: "Three-address code is the only widely used intermediate representation in production compilers."
  type: true-false
  answer: false
  explanation: "Multiple IR forms are used in production compilers. Static Single Assignment (SSA) form — a variant of 3AC where each variable is defined exactly once — is used in LLVM, GCC, and most modern compilers because it simplifies many optimization passes. Java and Python use bytecode (stack-based IR). The JVM's HotSpot compiler works with a sea-of-nodes IR. Tree-based IRs appear in early pipeline stages. 3AC (particularly in quadruple or SSA form) is the most common for the optimization middle-end, but claiming it is the only option conflates one popular design with the entire field."

- question: "Explain why decomposing `a + b * c` into two 3AC instructions (`t1 = b * c` followed by `t2 = a + t1`) is not merely a formatting constraint but qualitatively changes what the compiler can do."
  type: short-answer
  answer: "The decomposition gives every intermediate value an explicit name (a temporary). Once named, sub-results can be individually tracked, referenced by later instructions, and checked for redundancy across the entire instruction stream. An optimization pass can see that `t1 = b * c` is the same computation wherever it appears, enabling common subexpression elimination, constant propagation, and dead code elimination on each primitive step. The AST cannot support this directly because intermediate values inside a complex expression are unnamed and only exist as tree structure."
  explanation: "This is the central justification for using a linear IR rather than operating on the AST for optimization. Named temporaries create an explicit data-flow graph — you can trace exactly where each value is produced and consumed. Optimization algorithms (liveness analysis, reaching definitions, available expressions) are all defined over this named-value data flow. Without decomposition and naming, these algorithms would need to re-traverse the tree for every analysis, and the concept of a 'value used in multiple places' would have no direct representation."
```

## Explainer

You already know that a compiler translates the high-level AST into some intermediate representation before producing machine code, and that different IR designs make different tradeoffs between expressiveness and analyzability. **Three-address code (3AC)** is the most widely used linear IR, and its defining constraint is simple: every instruction contains at most one operator and at most three operands — two sources and one destination. The expression `a + b * c` cannot be a single 3AC instruction; instead, it becomes two: `t1 = b * c` followed by `t2 = a + t1`, where `t1` and `t2` are compiler-generated **temporaries**.

This decomposition is not bureaucratic overhead — it is the whole point. By breaking complex expressions into a sequence of primitive operations, 3AC makes the compiler's job tractable. Each instruction maps almost directly to a machine instruction (an add, a multiply, a load, a store), so code generation becomes a straightforward walk through the instruction list. Optimization passes — common subexpression elimination, constant propagation, dead code elimination — operate on these simple instructions rather than on deeply nested tree structures. When you see `t1 = b * c` appear twice, it is obvious that the second computation is redundant and can be replaced by a reuse of `t1`. That same redundancy is much harder to spot in an AST where the multiplication is buried inside different subtrees.

Generating 3AC from an AST is a recursive traversal. For each AST node, you emit instructions for its children first (to compute their values into temporaries), then emit the instruction for the node itself using those temporaries as operands. An assignment like `x = a + b * c - d` generates something like: `t1 = b * c`, `t2 = a + t1`, `t3 = t2 - d`, `x = t3`. Control flow translates to labels and conditional/unconditional jumps: an `if` statement becomes a conditional jump to a label, and loops become backward jumps. Function calls become a sequence of parameter-passing instructions followed by a `call` instruction and a result retrieval.

The concrete encoding of 3AC instructions varies. **Quadruples** store each instruction as a four-field record: `(operator, arg1, arg2, result)`. **Triples** eliminate the explicit result field by using the instruction's index as an implicit name for its result, saving space but making instruction reordering harder. **Indirect triples** add a level of indirection to recover reordering flexibility. Most teaching and many real compilers use quadruples for clarity. Regardless of encoding, the linear, low-level nature of 3AC makes it the natural bridge between the tree-structured world of semantic analysis and the register-and-instruction world of the target machine.
