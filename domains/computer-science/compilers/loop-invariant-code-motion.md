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
- id: vectorization-and-simd
  type: soft
tags:
- optimization
- loop-optimization
- code-motion
stage: advanced
status: validated
---
# Loop Invariant Code Motion (LICM)

## Core Idea
Loop invariant code motion hoists expressions that do not depend on loop iterations outside the loop. If an expression's operands are not modified in the loop, it computes the same value in each iteration and can be moved before the loop. This reduces redundant computation. Safety requires ensuring the expression is always executed before the loop's first iteration.

## Questions

```yaml
- question: "Inside a loop, the expression `result = numerator / divisor` appears inside an `if (divisor != 0)` check. Neither `numerator` nor `divisor` is modified in the loop. A compiler identifies this as loop-invariant. Should it hoist the division to the preheader?"
  type: multiple-choice
  options:
    - "Yes — since neither operand changes, the division computes the same value every iteration and is safe to move"
    - "Yes — hoisting loop-invariant expressions to the preheader is always a performance improvement with no correctness risk"
    - "No — hoisting moves the division outside the conditional, causing it to execute even when divisor is zero, which could fault on iterations where the original code would have skipped the division"
    - "No — division operations are never loop-invariant because they depend on hardware state"
  answer: 2
  explanation: "This is the safety problem with LICM. The expression is loop-invariant (same operands, same result each iteration), but it only executes when `divisor != 0`. Moving it to the preheader causes it to execute unconditionally before every iteration. If there is any iteration where `divisor == 0` and the conditional would have protected the division, hoisting causes a fault that the original code would not have. The compiler must verify the expression dominates all loop exits — that every path through the loop executes it — before the hoist is safe."

- question: "A compiler wants to hoist `cost = base_rate * multiplier` from inside an `if (apply_rate)` block within a loop. Under what condition is this safe?"
  type: multiple-choice
  options:
    - "When `base_rate` and `multiplier` are global variables visible across the entire program"
    - "When the compiler can prove the expression executes on every iteration (dominates all loop exits) and has no observable side effects"
    - "When the loop is guaranteed to run more than a fixed threshold number of iterations"
    - "When `apply_rate` is set before the loop begins and never changes inside the loop"
  answer: 1
  explanation: "Domination is the key safety condition. 'Dominates all loop exits' means every possible execution path through the loop passes through this expression — if the loop runs, the expression executes. If `apply_rate` is sometimes false, there are paths through the loop that don't reach the expression, so it doesn't dominate. Knowing `apply_rate` is set before the loop (option D) doesn't help if it might be false — the expression still skips on some iterations. The compiler also checks for side effects: expressions that modify memory or call functions with observable effects cannot be safely hoisted even when invariant."

- question: "Any expression inside a loop whose operands are not modified by the loop can generally be safely hoisted to the loop's preheader."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about LICM. Loop-invariance (same value every iteration) is necessary but not sufficient for safe hoisting. The expression must also execute on every iteration — it must dominate all loop exits. If the expression sits inside a conditional branch, moving it to the preheader changes when it executes, which can cause faults (division by zero, null pointer dereference) or incorrect behavior for expressions with side effects. The compiler must perform dominance analysis, not just operand analysis."

- question: "LICM can only improve performance on loops that run at least twice; for a loop that always executes exactly once, hoisting an invariant expression to the preheader provides no speedup."
  type: true-false
  answer: true
  explanation: "Correct. The entire benefit of LICM is eliminating repeated computation: instead of computing x*y on every iteration, compute it once before the loop. If the loop body executes exactly once, the expression already computes exactly once, so moving it outside the loop neither increases nor decreases execution count. LICM's value scales with iteration count — the more iterations, the greater the savings from hoisting an invariant expression."

- question: "Explain why hoisting a loop-invariant expression from inside a conditional branch to the loop's preheader can be unsafe, and what condition the compiler must verify before proceeding."
  type: short-answer
  answer: "If the expression is inside a conditional, it only executes when that condition is true. Moving it to the preheader makes it execute unconditionally before the loop. If the expression can fault (division by zero, null dereference) or has observable side effects, this changes the program's behavior on iterations where the original condition would have been false. The compiler must verify that the expression dominates all loop exits — meaning every execution path through the loop necessarily reaches the expression — before hoisting is safe."
  explanation: "This is why dominance analysis is the core tool for LICM safety, not just operand analysis. The compiler builds a control-flow graph of the loop and checks whether the expression's block dominates the loop exit blocks. If it does, every iteration executes the expression, and hoisting is semantics-preserving. If it does not (the expression is inside any branch that might not execute), the compiler must either prove the expression is side-effect-free and can't fault, or leave it in place."
```

## Explainer

From your work on code optimization, you know that compilers look for redundant or unnecessary computation and try to eliminate it. Loops are the highest-priority target because any wasted work inside a loop is multiplied by the iteration count. **Loop invariant code motion** (LICM) identifies computations inside a loop whose results never change across iterations and moves them to a point just before the loop begins, so they execute exactly once instead of thousands or millions of times.

An expression is **loop invariant** if all of its operands are either constants or are defined outside the loop. For example, in a loop that computes `a[i] = x * y + i`, the subexpression `x * y` is invariant if neither `x` nor `y` is modified inside the loop. The compiler can hoist `t = x * y` to the loop's **preheader** — a block that executes exactly once before the loop entry — and replace the original expression with `a[i] = t + i`. The control flow graph you studied makes this analysis precise: the compiler inspects definitions within the loop's strongly connected component and checks whether any definition of an operand reaches the expression from inside the loop.

The subtlety lies in **safety**. Hoisting is only safe if the expression would have executed on every iteration anyway. If the expression sits inside a conditional branch within the loop (`if (condition) { t = x * y; }`), moving it to the preheader means it now executes even when the condition is false. This can cause problems if the expression has side effects or can fault — for instance, a division that might divide by zero. The compiler must prove that the expression **dominates** all loop exits (meaning every path through the loop passes through it) or that the expression is free of observable side effects before performing the hoist.

LICM often works in concert with other optimizations. Strength reduction might turn a loop-variant multiplication into an addition, and then LICM can hoist the initialization of that addition's base value. Conversely, LICM can expose new opportunities for common subexpression elimination outside the loop. This cascading effect is why compilers run optimization passes in carefully ordered sequences — each pass creates opportunities for the next.
