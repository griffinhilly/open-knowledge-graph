---
id: quadruple-intermediate-representation
title: Quadruple Intermediate Representation
domain: computer-science
course: compilers
prerequisites:
- id: three-address-intermediate-code
  type: hard
builds-toward:
- basic-block-analysis
tags:
- ir
- intermediate-representation
stage: advanced
status: draft
---

# Quadruple Intermediate Representation

## Core Idea
A quadruple explicitly represents a three-address instruction as a 4-tuple: (op, arg1, arg2, result). Quadruples are more explicit than textual 3AC and support easier manipulation during optimization. Triples (omitting the result field) are more compact but harder to optimize.

## How It's Best Learned
Implement both quadruple and triple representations. Compare them on a real optimization task to understand trade-offs.

## Explainer

You already understand three-address code as an intermediate representation where each instruction has at most one operator and up to two source operands producing one result. Quadruples make this structure explicit by storing every instruction as a fixed-size record with four fields: **(operator, argument1, argument2, result)**. This is not a new language — it is a concrete data structure for representing the same three-address instructions you have already seen, in a form that is easy to store in arrays and manipulate programmatically.

Consider the expression `a = b * c + d`. A three-address code listing might write `t1 = b * c` followed by `a = t1 + d`. As quadruples, these become two records: `(*, b, c, t1)` and `(+, t1, d, a)`. Each record is self-contained — you can look at any quadruple and immediately know the operation, its inputs, and where the result goes. Not every field is always used: a unary operation like `t1 = -b` becomes `(negate, b, _, t1)`, and an unconditional jump becomes `(goto, _, _, L3)`. The unused fields are simply left empty.

The main alternative is the **triple** representation, which saves space by eliminating the result field entirely. Instead of naming a temporary for each result, triples refer to the result of an instruction by its position number in the instruction list. So instruction 0 might be `(*, b, c)` and instruction 1 might be `(+, (0), d)`, where `(0)` means "the result of instruction 0." This is more compact, but it creates a fragile dependency on instruction ordering — if you reorder, delete, or insert instructions during optimization, every positional reference must be updated. Quadruples avoid this problem because results are stored in named temporaries that remain valid regardless of instruction order, making them significantly easier to optimize.

In practice, most compiler implementations use quadruples (or a closely related structure) for their intermediate representation because optimization passes constantly rearrange, delete, and insert instructions. The small overhead of an extra field per instruction is a worthwhile trade for the freedom to transform code without maintaining a web of positional back-references. When you move on to basic block analysis and optimization, you will find that quadruples make operations like dead code elimination and common subexpression elimination straightforward — you simply mark a quadruple as dead or redirect its result, without renumbering the entire instruction sequence.
