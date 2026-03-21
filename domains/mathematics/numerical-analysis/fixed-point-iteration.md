---
id: fixed-point-iteration
title: Fixed Point Iteration
domain: mathematics
course: numerical-analysis
prerequisites:
- id: contraction-mapping
  type: soft
builds-toward:
- order-of-convergence
- newton-method-convergence
tags:
- fixed-point
- iteration
- root-finding
stage: formal-systems
status: draft
---

# Fixed Point Iteration

## Core Idea
Fixed point iteration solves f(x) = 0 by rewriting it as x = g(x) and iterating x_{n+1} = g(x_n). Convergence is guaranteed by the contraction mapping theorem if |g'(x)| < 1 near the fixed point. This method is foundational to understanding iterative algorithms and generalizes to systems of equations and complex domains.

## Questions

```yaml
- question: "To solve f(x) = x² − 4 = 0, two rearrangements are tried near the positive root x* = 2: (A) g(x) = 4/x and (B) g(x) = (x + 4/x)/2. For g(x) = 4/x, g'(2) = −1; for g(x) = (x + 4/x)/2, g'(2) = 0. Which iteration converges?"
  type: multiple-choice
  options:
    - "Both converge, since both are valid rearrangements of the same equation"
    - "Neither — fixed point iteration cannot find roots of polynomial equations"
    - "Only (A), because it is a simpler expression"
    - "Only (B), because |g'(2)| = 0 < 1 for (B) while |g'(2)| = 1 for (A)"
  answer: 3
  explanation: "Convergence requires |g'(x*)| < 1. For (A), |g'(2)| = 1 — exactly at the boundary — so iteration oscillates and does not converge. For (B), |g'(2)| = 0, guaranteeing convergence (and in fact quadratic convergence, since this is Newton's method in disguise). The key insight is that the same equation produces entirely different convergence behavior depending on how it is rearranged — the equation determines x*, but the choice of g determines whether iteration finds it."

- question: "A fixed point iteration scheme has |g'(x*)| = 0.05. A second scheme for the same problem has |g'(x*)| = 0.9. How do their convergence rates compare?"
  type: multiple-choice
  options:
    - "Both converge at the same rate since they solve the same underlying problem"
    - "The second converges faster since 0.9 is closer to 1 and therefore 'stronger'"
    - "The first converges much faster — errors shrink by roughly 95% each iteration versus only 10% for the second"
    - "Neither converges — both values must equal zero for fixed point iteration to work"
  answer: 2
  explanation: "The convergence rate of fixed point iteration is determined by |g'(x*)|: at each step, the error scales by approximately this factor. With |g'| = 0.05, errors shrink by ~95% per iteration. With |g'| = 0.9, errors shrink by only ~10% per iteration — roughly 18 times slower. This is why achieving |g'(x*)| = 0, as Newton's method does by construction, gives quadratic convergence: the error doesn't merely scale, it squares at each step."

- question: "The convergence of fixed point iteration depends on which rearrangement x = g(x) is used, not just on the equation f(x) = 0 being solved."
  type: true-false
  answer: true
  explanation: "The explainer demonstrates this with f(x) = x² − 2: one rearrangement gives |g'(√2)| ≈ 1.83 (diverges), another gives |g'| = 1 (boundary, oscillates), and Newton's method gives |g'| = 0 (quadratic convergence). All three start from the same equation. The equation f(x) = 0 determines what x* is; the choice of g determines whether iteration converges to it and how fast."

- question: "If fixed point iteration converges, it always converges at a quadratic rate."
  type: true-false
  answer: false
  explanation: "Basic fixed point iteration achieves linear convergence: errors decrease by a constant factor |g'(x*)| at each step. Quadratic convergence — where the error roughly squares at each step — is special, occurring only when |g'(x*)| = 0. Newton's method achieves this by careful construction, but it is the engineered refinement, not the norm. The explainer states: 'Fixed point iteration in its basic form... converges [linearly]. Newton's method achieves |g'(x*)| = 0... which is why it converges quadratically.'"

- question: "Why can the same equation f(x) = 0 produce both convergent and divergent fixed point iterations depending on how it is rearranged?"
  type: short-answer
  answer: "Because convergence depends on |g'(x*)| < 1 for the specific function g used in the rearrangement x = g(x). Different algebraic rearrangements of the same equation produce different functions g with different derivatives at the fixed point. When |g'(x*)| < 1, g is a contraction near x* — nearby iterates are pulled toward the solution. When |g'(x*)| > 1, g repels nearby iterates and iteration diverges. The equation determines what x* is; the rearrangement determines whether iteration converges to it."
  explanation: "This is why 'just rearrange and iterate' is not a reliable strategy. The contraction condition |g'(x*)| < 1 must be verified for each specific rearrangement, and ideally |g'(x*)| should be as small as possible for fast convergence. The art of fixed point methods lies in finding a g that satisfies this condition — Newton's method is essentially an algorithm for constructing a g where g'(x*) = 0 exactly."
```

## Explainer

A **fixed point** of a function g is a value x* where g(x*) = x* — the function maps x* to itself. Fixed point iteration exploits a simple idea: if you have an equation f(x) = 0, you can often rearrange it into the form x = g(x), and then guess that repeated application of g will "home in" on the answer. Starting from an initial guess x₀, you compute x₁ = g(x₀), then x₂ = g(x₁), and so on. If this sequence converges, it converges to a fixed point of g — which is also a root of f.

Why does this work? Your prerequisite on contraction mappings gives the answer. A function g is a **contraction** on an interval if it squeezes distances: |g(x) − g(y)| ≤ L|x − y| for some constant L < 1. The Banach fixed point theorem guarantees that any contraction on a complete metric space has a unique fixed point, and that iteration converges to it at a geometric rate. In practice, the condition |g'(x)| < 1 near x* is the local version of this: if g is differentiable and |g'(x*)| < 1, then iteration will converge when started close enough to x*. The closer |g'(x*)| is to 0, the faster the convergence.

The critical insight is that the *same* equation f(x) = 0 can be rearranged in many ways into x = g(x), and not all rearrangements converge. Consider f(x) = x² − 2 (whose roots are ±√2). You could rewrite it as x = x² − x + 2, giving g(x) = x² − x + 2 — but |g'(√2)| = |2√2 − 1| ≈ 1.83 > 1, so this diverges. Alternatively, x = 2/x gives g(x) = 2/x — but g'(√2) = −2/2 = −1, right at the boundary. A better choice: x = (x + 2/x)/2, which is Newton's method in disguise, and converges quadratically. Choosing the right g is both the art and the challenge of fixed point methods.

The convergence rate is determined by |g'(x*)|. If |g'(x*)| = L, then errors decrease by a factor of approximately L at each step — this is **linear convergence**. When L is close to 1, convergence is slow; when L is close to 0, it's fast. This connects directly to the order-of-convergence framework you'll study next. Newton's method achieves |g'(x*)| = 0 (by careful construction), which is why it converges quadratically — the error roughly squares at each step rather than merely scaling. Fixed point iteration in its basic form is the conceptual foundation; Newton's method is the engineered refinement.
