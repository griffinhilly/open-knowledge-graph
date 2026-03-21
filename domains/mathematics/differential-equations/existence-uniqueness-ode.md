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

## Questions

```yaml
- question: "Consider the IVP dy/dx = y^(2/3), y(0) = 0. What does the Picard-Lindelöf theorem say about this problem?"
  type: multiple-choice
  options:
    - "It guarantees a unique solution because f(x,y) = y^(2/3) is continuous everywhere"
    - "It guarantees at least one solution but not uniqueness, because ∂f/∂y is not continuous at y = 0"
    - "It guarantees no solution exists because the conditions fail"
    - "It is irrelevant because the trivial solution y ≡ 0 is obvious by inspection"
  answer: 1
  explanation: "The theorem requires both f continuous AND ∂f/∂y continuous near the initial point. Here f = y^(2/3) is continuous, but ∂f/∂y = (2/3)y^(−1/3) blows up at y = 0 — the Lipschitz condition fails. The theorem gives no uniqueness guarantee. In fact, this IVP has multiple solutions: y ≡ 0 and y = (x/3)³. Option A is the tempting mistake: continuity of f alone is not enough."

- question: "An IVP satisfies both conditions of Picard-Lindelöf near the initial point. What does the theorem actually guarantee?"
  type: multiple-choice
  options:
    - "The solution is valid on the entire real line because the conditions hold everywhere near the initial point"
    - "A unique solution exists in some neighborhood of the initial point — the theorem says nothing about global existence"
    - "The solution is unique globally because it is the only one found by standard methods"
    - "The theorem guarantees the solution is defined for all initial conditions, not just this one"
  answer: 1
  explanation: "The Picard-Lindelöf theorem is a local result: it guarantees a unique solution in some neighborhood of x₀, not for all x. Global existence requires separate analysis. For example, dy/dx = y², y(0) = 1 satisfies the theorem's conditions near (0,1), yet the solution y = 1/(1−x) blows up at x = 1. The conditions guarantee local existence and uniqueness; how far the solution extends is a separate question."

- question: "If the Picard-Lindelöf conditions fail for an IVP, the IVP has no solution."
  type: true-false
  answer: false
  explanation: "Failing the theorem's conditions means the theorem provides no guarantee — it says nothing about what actually happens. The IVP may still have a solution (or even multiple solutions). The classic example dy/dx = y^(2/3), y(0) = 0 fails the Lipschitz condition but has multiple solutions. The theorem is a sufficient condition for existence and uniqueness, not a necessary one."

- question: "The Picard-Lindelöf theorem guarantees that when its conditions hold, the solution to an IVP is unique in some neighborhood of the initial point."
  type: true-false
  answer: true
  explanation: "This is precisely what the theorem states. Continuity of f and continuity of ∂f/∂y (the Lipschitz condition) near (x₀, y₀) together guarantee both existence and uniqueness of a solution near x₀. The Picard iteration argument constructs the solution as a converging sequence, and the Lipschitz condition is what prevents divergence — and therefore what prevents multiple solutions from branching off the same initial point."

- question: "Why does the Lipschitz condition on ∂f/∂y prevent non-uniqueness of solutions, while continuity of f alone is not sufficient?"
  type: short-answer
  answer: "Continuity of f ensures the right-hand side doesn't jump discontinuously, which helps existence, but it doesn't control how rapidly f can change in the y-direction. If f varies too steeply in y, two solution curves starting at the same point can diverge — the equation pushes them apart. The Lipschitz condition (bounded ∂f/∂y) limits this y-sensitivity: nearby solutions can't diverge faster than exponentially, and the Picard iteration converges to a unique limit. Without it, multiple solution curves can pass through the same initial point, as in the y^(2/3) example."
  explanation: "The intuition is that the Lipschitz condition bounds the spread rate of nearby solutions. If ∂f/∂y is unbounded, solutions can branch at the initial point. Continuity of f is necessary to construct a candidate solution, but uniqueness requires the additional control on how f varies with y."
```

## Explainer

When you solve a differential equation, you are finding a function — and the natural first question is whether such a function even exists. The **Picard-Lindelöf Theorem** (also called the existence and uniqueness theorem) answers this: under mild conditions on the right-hand side f(x, y), the initial value problem dy/dx = f(x, y), y(x₀) = y₀ is guaranteed to have exactly one solution near x₀. This might seem obvious, but it fails in subtle cases, and understanding when it fails is just as important as knowing when it holds.

The two conditions are: **continuity** of f (which you know from your study of continuity) and continuity of ∂f/∂y, the partial derivative with respect to y. The partial derivative condition is a **Lipschitz condition** in disguise: it says f doesn't change too rapidly in the y-direction, which prevents solutions from veering off in divergent directions. Together, these conditions rule out two types of bad behavior: non-existence (where the equation forces a blow-up before a solution can be constructed) and non-uniqueness (where multiple solution curves pass through the same initial point).

Failure cases build the intuition. Consider dy/dx = y^(2/3) with y(0) = 0. Here f = y^(2/3) is continuous, but ∂f/∂y = (2/3)y^(−1/3) is undefined at y = 0 — the Lipschitz condition fails. Sure enough, this IVP has multiple solutions: y ≡ 0 (the trivial solution) and y = (x/3)³ (a non-trivial solution that also passes through the origin). Without uniqueness, the ODE becomes an ambiguous model — you can't predict which solution nature "chooses." For blow-up, consider dy/dx = y², y(0) = 1: the solution is y = 1/(1 − x), which goes to infinity at x = 1. Here f and ∂f/∂y are continuous near (0, 1), so the theorem guarantees a local solution, but the solution only exists on (−∞, 1), not for all x.

The **Picard iteration** scheme provides both the proof and the intuition. Starting with the constant function y₀(x) = y₀, define y_{n+1}(x) = y₀ + ∫ f(t, yₙ(t)) dt from x₀ to x. Under the Lipschitz condition, this sequence of approximations converges — each iteration is a better approximation to the true solution, and the convergence argument shows both that a limit exists and that it's unique. This iteration is impractical for computation but conceptually illuminating: the solution is built as a limit of successive approximations, and the Lipschitz condition is exactly what makes those approximations converge rather than diverge.

Practically, the theorem tells you when to trust your solution. If you solved an IVP and the theorem's conditions hold near the initial point, you know your solution is the only one — there's no alternative to find. If the conditions fail, you should check for multiple solutions or blow-up. This theorem is the theoretical backbone of the entire course in differential equations: every solution method you learn produces a candidate, and existence-uniqueness is the guarantee that the candidate is definitive.
