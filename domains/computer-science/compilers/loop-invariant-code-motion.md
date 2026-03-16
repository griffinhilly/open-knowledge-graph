---
id: loop-invariant-code-motion
title: Loop Invariant Code Motion (LICM)
domain: computer-science
course: compilers
prerequisites:
- id: code-optimization
  type: hard
- id: control-flow-graphs
  type: hard
tags:
- optimization
- loop-optimization
- code-motion
stage: advanced
status: draft
---

# Loop Invariant Code Motion (LICM)

## Core Idea
Loop invariant code motion hoists expressions that do not depend on loop iterations outside the loop. If an expression's operands are not modified in the loop, it computes the same value in each iteration and can be moved before the loop. This reduces redundant computation. Safety requires ensuring the expression is always executed before the loop's first iteration.

## Explainer

From your work on code optimization, you know that compilers look for redundant or unnecessary computation and try to eliminate it. Loops are the highest-priority target because any wasted work inside a loop is multiplied by the iteration count. **Loop invariant code motion** (LICM) identifies computations inside a loop whose results never change across iterations and moves them to a point just before the loop begins, so they execute exactly once instead of thousands or millions of times.

An expression is **loop invariant** if all of its operands are either constants or are defined outside the loop. For example, in a loop that computes `a[i] = x * y + i`, the subexpression `x * y` is invariant if neither `x` nor `y` is modified inside the loop. The compiler can hoist `t = x * y` to the loop's **preheader** — a block that executes exactly once before the loop entry — and replace the original expression with `a[i] = t + i`. The control flow graph you studied makes this analysis precise: the compiler inspects definitions within the loop's strongly connected component and checks whether any definition of an operand reaches the expression from inside the loop.

The subtlety lies in **safety**. Hoisting is only safe if the expression would have executed on every iteration anyway. If the expression sits inside a conditional branch within the loop (`if (condition) { t = x * y; }`), moving it to the preheader means it now executes even when the condition is false. This can cause problems if the expression has side effects or can fault — for instance, a division that might divide by zero. The compiler must prove that the expression **dominates** all loop exits (meaning every path through the loop passes through it) or that the expression is free of observable side effects before performing the hoist.

LICM often works in concert with other optimizations. Strength reduction might turn a loop-variant multiplication into an addition, and then LICM can hoist the initialization of that addition's base value. Conversely, LICM can expose new opportunities for common subexpression elimination outside the loop. This cascading effect is why compilers run optimization passes in carefully ordered sequences — each pass creates opportunities for the next.
