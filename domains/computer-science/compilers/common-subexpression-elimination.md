---
id: common-subexpression-elimination
title: Common Subexpression Elimination (CSE)
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
- id: reaching-definitions-analysis
  type: hard
tags:
- optimization
- cse
- expression-reuse
stage: advanced
status: draft
---

# Common Subexpression Elimination (CSE)

## Core Idea
Common subexpression elimination detects and removes redundant computations. If the same expression is computed multiple times with unchanged operands, compute it once and reuse the result. CSE requires tracking when expressions are available (all operands have definitions reaching the current point) and when they are not killed (operands not reassigned).

## Explainer

Consider this fragment of intermediate code: `t1 = a + b; t2 = a + b;`. If neither `a` nor `b` is modified between the two statements, then `t2` will always equal `t1`. Computing `a + b` a second time is pure waste — the compiler can replace the second computation with `t2 = t1`. This is the essence of **common subexpression elimination (CSE)**: find expressions that have already been computed with unchanged operands, and reuse the earlier result instead of recomputing.

The challenge is determining *when* an expression is safe to reuse. From your study of dataflow analysis and reaching definitions, you have the machinery to answer this. An expression `a + b` is **available** at a program point if every path from the start of the program to that point computes `a + b`, and neither `a` nor `b` is redefined after the most recent computation. If any path redefines an operand without recomputing the expression, the earlier value may be stale and cannot be reused. The compiler solves this with **available expressions analysis**, a forward dataflow problem: the gen set at each statement includes expressions it computes, the kill set includes all expressions containing variables it redefines, and the meet operation at join points takes the intersection (an expression is only available if it is available on *all* incoming paths).

There are two scopes of CSE. **Local CSE** operates within a single basic block — a straight-line sequence of instructions with no branches. This is simple because there is only one path, so you just scan forward, maintaining a table of computed expressions and replacing duplicates. **Global CSE** operates across an entire function's control flow graph, handling branches and loops. Global CSE requires the full available expressions dataflow analysis, which propagates information across basic block boundaries. The result is more powerful: it can catch redundancies across branches, in loop bodies, and between distant parts of the function.

CSE interacts productively with other optimizations. Copy propagation can expose new common subexpressions by replacing variable copies with their originals, making previously different-looking expressions identical. Constant folding can simplify operands, again revealing matches. In loops, CSE often works hand-in-hand with loop-invariant code motion: an expression computed inside a loop whose operands never change across iterations is both a common subexpression and loop-invariant, and can be hoisted out of the loop entirely. The compiler's optimization pipeline typically runs these passes in sequence, with each pass creating opportunities for the next.
