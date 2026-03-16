---
id: constant-propagation
title: Constant Propagation and Folding
domain: computer-science
course: compilers
prerequisites:
- id: reaching-definitions-analysis
  type: hard
tags:
- optimization
- constant-propagation
- algebraic-simplification
stage: advanced
status: draft
---

# Constant Propagation and Folding

## Core Idea
Constant propagation identifies variables assigned constant values and replaces their uses with the constant. Constant folding evaluates constant expressions at compile-time. For example, `x = 5; y = x + 3` becomes `y = 8`. This simple optimization enables further simplifications and can expose dead code.

## Explainer

From reaching definitions analysis, you know how to determine, for each point in a program, which assignments could have produced the current value of a variable. Constant propagation builds directly on this: if every reaching definition of a variable assigns it the same constant value, then every use of that variable can be replaced with that constant. The compiler does not need to wait until runtime to look up the variable — it already knows the answer.

Consider a straightforward example. If the program says `x = 7` on line 3 and no other assignment to x reaches line 10, then at line 10 the compiler knows x is 7 and can substitute the literal value directly. **Constant propagation** performs this substitution throughout the program. **Constant folding** is the companion step: once propagation has replaced variables with constants, expressions like `7 + 3` can be evaluated at compile time to produce `10`. Together, these two transformations often chain — propagating a constant enables folding an expression, which produces a new constant that can be propagated further.

The analysis works on the control flow graph using a **lattice** of values for each variable. Each variable starts as "undefined" (no assignment has been seen), can become a specific constant (exactly one constant value reaches this point), or can become "not a constant" (multiple different values reach this point, or the value depends on runtime input). At merge points in the control flow — where two branches of an if-statement rejoin — the values from both paths are combined: if both paths agree on the same constant, the variable remains that constant; if they disagree, the variable becomes "not a constant." This is a forward dataflow analysis that iterates until the lattice values stabilize at a fixed point.

The power of constant propagation lies in what it enables downstream. Replacing a variable with a constant can make a branch condition statically evaluable — if `x` is known to be 7, then `if (x > 5)` is always true, and the compiler can eliminate the branch and its dead else-block entirely. This **dead code elimination** shrinks the program, which in turn may expose more constants by removing conflicting assignments. Many compiler optimizations work this way: each pass creates opportunities for the next, and constant propagation is often one of the first and most impactful passes in the sequence because its simplifications cascade broadly.
