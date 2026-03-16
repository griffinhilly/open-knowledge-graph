---
id: dead-code-elimination
title: Dead Code Elimination
domain: computer-science
course: compilers
prerequisites:
- id: live-variable-analysis
  type: hard
tags:
- optimization
- code-quality
- dead-code
stage: advanced
status: draft
---

# Dead Code Elimination

## Core Idea
Dead code elimination removes statements whose results are never used. An assignment to a non-live variable is dead: the value is computed but never observed. Unreachable code (after return, throw, or unconditional jump) is also dead. This optimization reduces code size and can expose further optimization opportunities. Aggressive dead-code elimination requires interprocedural analysis.

## Explainer

Your prerequisite, live variable analysis, answers a precise question for every point in a program: which variables might still be read before being overwritten? A variable is **live** at a point if there exists some execution path from that point to a use of the variable without an intervening definition. **Dead code elimination** (DCE) is the optimization that exploits this information directly — if a statement computes a value that is not live after the statement, the computation is wasted work and can be removed.

Consider a concrete example. Suppose a function computes `x = a * b + c` on line 10, but x is reassigned on line 15 without being read in between, and line 10's value of x is never used on any path. Live variable analysis marks x as not live after line 10, which means the assignment is **dead**. The compiler deletes line 10 entirely. This is not just tidying up — it eliminates the multiplication and addition, freeing the execution unit and potentially freeing a register that was holding x. In real compilers, dead code often arises not from sloppy programming but from earlier optimization passes: constant propagation might replace all uses of a variable with a constant, leaving the original assignment dead; inlining might duplicate code where one branch becomes unreachable; and loop transformations might render intermediate computations unnecessary.

There are two distinct kinds of dead code. The first, described above, is **dead assignments**: statements that compute values nobody reads. The second is **unreachable code**: statements that no execution path can ever reach. Code after an unconditional return, code in an `if (false)` branch after constant folding, or code following an infinite loop is unreachable. Unreachable code detection uses **control flow analysis** rather than live variable analysis — it identifies basic blocks with no predecessors in the control flow graph (other than the entry block). Both kinds should be eliminated, but they rely on different analyses.

Dead code elimination is a cascading optimization, meaning that removing dead code can create more dead code. Deleting a dead assignment to x might make the computations of a, b, and c dead as well, if they were only used to compute x. This is why compilers typically run DCE iteratively or interleave it with other passes. **Aggressive dead code elimination** works in the opposite direction from the naive approach: instead of finding dead statements to delete, it starts by assuming *everything* is dead and then marks statements as live only if they contribute to observable effects — function return values, writes to memory visible outside the function, I/O operations, or stores to volatile variables. Everything not marked live is deleted. This aggressive approach naturally handles chains of dead code in a single pass and is particularly effective after inlining, where large sections of inlined code may turn out to be irrelevant in the caller's context.
