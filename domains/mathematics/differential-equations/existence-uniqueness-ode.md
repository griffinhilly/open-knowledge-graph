---
id: existence-uniqueness-ode
title: Existence and Uniqueness Theorems (Picard-Lindelöf Theorem)
domain: mathematics
course: differential-equations
prerequisites:
- id: exact-differential-equations
  type: soft
- id: continuity-definition
  type: hard
builds-toward:
- autonomous-equations-phase-lines
tags:
- existence
- uniqueness
- theoretical
stage: formal-systems
status: draft
---

# Existence and Uniqueness Theorems (Picard-Lindelöf Theorem)

## Core Idea
The Picard-Lindelöf theorem establishes conditions under which an initial value problem dy/dx = f(x,y), y(x₀) = y₀ has a unique solution. If f and ∂f/∂y are continuous in a rectangular region around (x₀, y₀), then a unique solution exists in some neighborhood of x₀. This is foundational for understanding when solutions are guaranteed and where they may fail to exist or be non-unique.

## Explainer

When you solve a differential equation, you are finding a function — and the natural first question is whether such a function even exists. The **Picard-Lindelöf Theorem** (also called the existence and uniqueness theorem) answers this: under mild conditions on the right-hand side f(x, y), the initial value problem dy/dx = f(x, y), y(x₀) = y₀ is guaranteed to have exactly one solution near x₀. This might seem obvious, but it fails in subtle cases, and understanding when it fails is just as important as knowing when it holds.

The two conditions are: **continuity** of f (which you know from your study of continuity) and continuity of ∂f/∂y, the partial derivative with respect to y. The partial derivative condition is a **Lipschitz condition** in disguise: it says f doesn't change too rapidly in the y-direction, which prevents solutions from veering off in divergent directions. Together, these conditions rule out two types of bad behavior: non-existence (where the equation forces a blow-up before a solution can be constructed) and non-uniqueness (where multiple solution curves pass through the same initial point).

Failure cases build the intuition. Consider dy/dx = y^(2/3) with y(0) = 0. Here f = y^(2/3) is continuous, but ∂f/∂y = (2/3)y^(−1/3) is undefined at y = 0 — the Lipschitz condition fails. Sure enough, this IVP has multiple solutions: y ≡ 0 (the trivial solution) and y = (x/3)³ (a non-trivial solution that also passes through the origin). Without uniqueness, the ODE becomes an ambiguous model — you can't predict which solution nature "chooses." For blow-up, consider dy/dx = y², y(0) = 1: the solution is y = 1/(1 − x), which goes to infinity at x = 1. Here f and ∂f/∂y are continuous near (0, 1), so the theorem guarantees a local solution, but the solution only exists on (−∞, 1), not for all x.

The **Picard iteration** scheme provides both the proof and the intuition. Starting with the constant function y₀(x) = y₀, define y_{n+1}(x) = y₀ + ∫ f(t, yₙ(t)) dt from x₀ to x. Under the Lipschitz condition, this sequence of approximations converges — each iteration is a better approximation to the true solution, and the convergence argument shows both that a limit exists and that it's unique. This iteration is impractical for computation but conceptually illuminating: the solution is built as a limit of successive approximations, and the Lipschitz condition is exactly what makes those approximations converge rather than diverge.

Practically, the theorem tells you when to trust your solution. If you solved an IVP and the theorem's conditions hold near the initial point, you know your solution is the only one — there's no alternative to find. If the conditions fail, you should check for multiple solutions or blow-up. This theorem is the theoretical backbone of the entire course in differential equations: every solution method you learn produces a candidate, and existence-uniqueness is the guarantee that the candidate is definitive.
