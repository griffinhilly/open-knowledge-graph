---
id: existence-and-uniqueness-theorems
title: Existence and Uniqueness Theorems for ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: first-order-linear-odes
  type: hard
- id: continuity-definition
  type: soft
builds-toward:
- autonomous-equations
- bifurcation-in-odes
- linearization-of-nonlinear-systems
tags:
- theory
- rigor
- qualitative
stage: formal-systems
status: draft
---

# Existence and Uniqueness Theorems for ODEs

## Core Idea
Picard's existence and uniqueness theorem states that under appropriate conditions (continuity and Lipschitz continuity), an initial value problem dy/dx = f(x,y) with y(x₀) = y₀ has a unique solution in some neighborhood of (x₀, y₀). This theorem justifies why solution curves don't intersect.

## Explainer

When you solved first-order linear ODEs, you likely assumed without much thought that the equation had a solution and that specifying an initial condition pinned down exactly one solution. This theorem is the result that justifies those assumptions. Before studying it, you should ask: does every IVP have a solution? And if it does, could two different solutions share the same initial condition? The answer to both questions depends on the behavior of the right-hand side f(x,y), and Picard's theorem gives precise conditions.

The **existence** part requires that f(x,y) is continuous near the initial point (x₀,y₀). Continuity alone is enough to guarantee that a solution exists — there is some interval around x₀ on which a function y(x) satisfies the ODE and the initial condition. Think of continuity as ensuring f does not have abrupt jumps that would make it impossible to "flow" a solution curve through the initial point. However, continuity alone does not guarantee uniqueness. The classic counterexample is dy/dx = y^(1/3) with y(0) = 0: f = y^(1/3) is continuous, and y(x) = 0 is one solution, but y(x) = (2x/3)^(3/2) is another. Two solutions emerge from the same initial point.

**Uniqueness** requires an additional condition called **Lipschitz continuity** in y: there exists a constant K such that |f(x,y₁) - f(x,y₂)| ≤ K|y₁ - y₂| for all y₁, y₂ near y₀. This means f cannot change too rapidly as y varies. A sufficient condition (often easier to check) is that ∂f/∂y is continuous and bounded near (x₀,y₀). In the counterexample above, ∂f/∂y = (1/3)y^(-2/3) → ∞ as y → 0 — the Lipschitz condition fails at exactly the point causing non-uniqueness.

The geometric consequence is direct: if f is continuous and Lipschitz, then solution curves cannot cross. If two solution curves intersected at a point (x₁,y₁), they would both be solutions to the IVP with initial condition y(x₁) = y₁ — violating uniqueness. This is why, when you sketch direction fields, solution curves always look like they are avoiding each other. The theorem tells you they are not just visually separated — they are provably forced apart. The theorem is local (valid near the initial point), but for linear equations the conditions hold globally, so linear IVPs have unique solutions on the entire interval where the coefficients are continuous.
