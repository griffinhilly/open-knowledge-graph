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

## Explainer

A **fixed point** of a function g is a value x* where g(x*) = x* — the function maps x* to itself. Fixed point iteration exploits a simple idea: if you have an equation f(x) = 0, you can often rearrange it into the form x = g(x), and then guess that repeated application of g will "home in" on the answer. Starting from an initial guess x₀, you compute x₁ = g(x₀), then x₂ = g(x₁), and so on. If this sequence converges, it converges to a fixed point of g — which is also a root of f.

Why does this work? Your prerequisite on contraction mappings gives the answer. A function g is a **contraction** on an interval if it squeezes distances: |g(x) − g(y)| ≤ L|x − y| for some constant L < 1. The Banach fixed point theorem guarantees that any contraction on a complete metric space has a unique fixed point, and that iteration converges to it at a geometric rate. In practice, the condition |g'(x)| < 1 near x* is the local version of this: if g is differentiable and |g'(x*)| < 1, then iteration will converge when started close enough to x*. The closer |g'(x*)| is to 0, the faster the convergence.

The critical insight is that the *same* equation f(x) = 0 can be rearranged in many ways into x = g(x), and not all rearrangements converge. Consider f(x) = x² − 2 (whose roots are ±√2). You could rewrite it as x = x² − x + 2, giving g(x) = x² − x + 2 — but |g'(√2)| = |2√2 − 1| ≈ 1.83 > 1, so this diverges. Alternatively, x = 2/x gives g(x) = 2/x — but g'(√2) = −2/2 = −1, right at the boundary. A better choice: x = (x + 2/x)/2, which is Newton's method in disguise, and converges quadratically. Choosing the right g is both the art and the challenge of fixed point methods.

The convergence rate is determined by |g'(x*)|. If |g'(x*)| = L, then errors decrease by a factor of approximately L at each step — this is **linear convergence**. When L is close to 1, convergence is slow; when L is close to 0, it's fast. This connects directly to the order-of-convergence framework you'll study next. Newton's method achieves |g'(x*)| = 0 (by careful construction), which is why it converges quadratically — the error roughly squares at each step rather than merely scaling. Fixed point iteration in its basic form is the conceptual foundation; Newton's method is the engineered refinement.
