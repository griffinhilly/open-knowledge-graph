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
status: draft
---

# Three-Address Intermediate Code

## Core Idea
Three-address code is a popular intermediate representation where each instruction has at most three operands and one operation. 3AC is linear (easy to optimize sequentially), easy to generate from ASTs, and straightforward to translate to machine code.

## How It's Best Learned
Write a code generator producing 3AC from an AST. Manually optimize 3AC to understand what compilers must do.

## Common Misconceptions
Three-address code is the only intermediate representation (SSA, bytecode, and tree-based IRs exist). All 3AC is equally easy to optimize (SSA form has special properties).

## Explainer

You already know that a compiler translates the high-level AST into some intermediate representation before producing machine code, and that different IR designs make different tradeoffs between expressiveness and analyzability. **Three-address code (3AC)** is the most widely used linear IR, and its defining constraint is simple: every instruction contains at most one operator and at most three operands — two sources and one destination. The expression `a + b * c` cannot be a single 3AC instruction; instead, it becomes two: `t1 = b * c` followed by `t2 = a + t1`, where `t1` and `t2` are compiler-generated **temporaries**.

This decomposition is not bureaucratic overhead — it is the whole point. By breaking complex expressions into a sequence of primitive operations, 3AC makes the compiler's job tractable. Each instruction maps almost directly to a machine instruction (an add, a multiply, a load, a store), so code generation becomes a straightforward walk through the instruction list. Optimization passes — common subexpression elimination, constant propagation, dead code elimination — operate on these simple instructions rather than on deeply nested tree structures. When you see `t1 = b * c` appear twice, it is obvious that the second computation is redundant and can be replaced by a reuse of `t1`. That same redundancy is much harder to spot in an AST where the multiplication is buried inside different subtrees.

Generating 3AC from an AST is a recursive traversal. For each AST node, you emit instructions for its children first (to compute their values into temporaries), then emit the instruction for the node itself using those temporaries as operands. An assignment like `x = a + b * c - d` generates something like: `t1 = b * c`, `t2 = a + t1`, `t3 = t2 - d`, `x = t3`. Control flow translates to labels and conditional/unconditional jumps: an `if` statement becomes a conditional jump to a label, and loops become backward jumps. Function calls become a sequence of parameter-passing instructions followed by a `call` instruction and a result retrieval.

The concrete encoding of 3AC instructions varies. **Quadruples** store each instruction as a four-field record: `(operator, arg1, arg2, result)`. **Triples** eliminate the explicit result field by using the instruction's index as an implicit name for its result, saving space but making instruction reordering harder. **Indirect triples** add a level of indirection to recover reordering flexibility. Most teaching and many real compilers use quadruples for clarity. Regardless of encoding, the linear, low-level nature of 3AC makes it the natural bridge between the tree-structured world of semantic analysis and the register-and-instruction world of the target machine.
