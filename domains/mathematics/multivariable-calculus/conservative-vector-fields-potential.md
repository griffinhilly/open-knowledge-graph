---
id: conservative-vector-fields-potential
title: Conservative Vector Fields and Potential Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-definition-properties
  type: hard
builds-toward:
- greens-theorem-applications
tags:
- conservative-fields
- potential
- path-independence
stage: formal-systems
status: validated
---

# Conservative Vector Fields and Potential Functions

## Core Idea
A vector field F is conservative if F = ∇f for some scalar potential f. For conservative fields, ∫_C F · dr depends only on endpoints (path-independent). If F is conservative and curl-free (∂Q/∂x = ∂P/∂y for F = ⟨P, Q⟩), then ∫ F · dr around any closed path is zero.

## Questions

```yaml
- question: "For a conservative vector field F, you compute ∫_{C₁} F · dr = 7 along path C₁ from point A to point B. What is ∫_{C₂} F · dr along a completely different path C₂ from A to B?"
  type: multiple-choice
  options:
    - "It cannot be determined without knowing the specific field and path C₂."
    - "−7, because the field reverses orientation when a different path is taken."
    - "7, because path independence means the line integral depends only on the endpoints."
    - "0, because conservative fields produce zero work for any path between distinct points."
  answer: 2
  explanation: "Path independence is the defining property of conservative fields: the line integral between two fixed endpoints is the same regardless of which path connects them. Since both C₁ and C₂ go from A to B, both equal f(B) − f(A) = 7. Option D confuses path independence with the zero-circulation property — a round trip (A to B back to A) gives zero, but a one-way trip from A to B does not."

- question: "For F = ⟨P, Q⟩ on a simply connected region, which condition is necessary and sufficient to confirm F is conservative?"
  type: multiple-choice
  options:
    - "P and Q are both continuous and positive throughout the region."
    - "The line integral of F along every straight-line path equals zero."
    - "∂P/∂y = ∂Q/∂x — the cross-partial derivatives of the two components are equal."
    - "F has constant magnitude at every point in the region."
  answer: 2
  explanation: "The curl-free condition ∂P/∂y = ∂Q/∂x is both necessary and sufficient on a simply connected domain. It is necessary because if F = ∇f, then P = ∂f/∂x and Q = ∂f/∂y, and Clairaut's theorem forces the mixed partials of f to be equal. It is sufficient because on a simply connected region, this condition guarantees a potential function f can be constructed by integration. On non-simply connected regions (like a punctured plane), the condition is necessary but not sufficient."

- question: "For a conservative field F = ∇f, the line integral from A to B equals f(B) − f(A), regardless of the path taken."
  type: true-false
  answer: true
  explanation: "True — this is the fundamental theorem for line integrals. If F = ∇f, then ∫_C F · dr = ∫_C ∇f · dr = f(endpoint) − f(startpoint). The path cancels entirely; only the values of the potential function at the two endpoints matter. This mirrors the single-variable result ∫_a^b f'(x) dx = f(b) − f(a)."

- question: "If ∮_C F · dr = 0 for one specific closed loop C, then F must be conservative."
  type: true-false
  answer: false
  explanation: "False. Zero circulation around one particular loop does not prove conservatism. A conservative field has zero circulation around every closed loop, not just some. A non-conservative field could produce zero net circulation around a specific path by cancellation. To confirm conservatism, you need either the curl test (∂P/∂y = ∂Q/∂x on a simply connected domain) or verified path independence for all pairs of endpoints."

- question: "Explain why a conservative vector field has path-independent line integrals — why do only the endpoints matter?"
  type: short-answer
  answer: "A conservative field F is the gradient of a potential function f, so F = ∇f. The fundamental theorem for line integrals then gives ∫_C ∇f · dr = f(endpoint) − f(startpoint) for any path C. This holds because the integral telescopes: intermediate values of f along the path cancel in the telescoping sum, leaving only the difference between the terminal values of f. The path's shape is irrelevant — only where f starts and ends matters."
  explanation: "The physical analogy is gravitational potential energy: moving an object between two heights always requires the same energy regardless of route, because energy is a function of position alone. Conservative vector fields are exactly the force fields with this property — they are gradients of potential energy functions, and line integrals reduce to potential differences."
```

## Explainer

A vector field assigns a vector to each point in space — think of a force field, a velocity field, or the gradient of temperature. From your work with line integrals, you know that computing ∫_C F · dr along a path C generally depends on which path you take. **Conservative vector fields** are the special class where this path-dependence disappears: the integral between two points depends only on the endpoints, not on the route. This is called **path independence**.

The connection between path independence and a potential function is the central theorem. A vector field F is conservative if and only if F = ∇f for some scalar-valued function f, called a **potential function**. The gradient structure makes path independence transparent via the fundamental theorem for line integrals: ∫_C ∇f · dr = f(endpoint) − f(startpoint). The integral telescopes to a simple difference, just as in single-variable calculus ∫_a^b f'(x)dx = f(b) − f(a). Only the endpoint values of f matter; the path is irrelevant.

To test whether a field F = ⟨P, Q⟩ is conservative on a simply connected region, check the **curl condition**: ∂Q/∂x = ∂P/∂y. If F = ∇f, Clairaut's theorem requires that the mixed partials of f are equal, which forces this condition. On simply connected domains, the condition is also sufficient — you can then construct f explicitly by integrating P with respect to x, then differentiating the result with respect to y and matching it to Q to pin down the y-dependent part.

The physical intuition is energy: in a conservative force field (gravity, electrostatics), moving an object between two points costs the same work regardless of path — energy depends only on position. A round trip back to the starting point costs zero net work. Non-conservative fields (friction, magnetic forces) do not have this property: work dissipated or injected depends on how you travel, not just where you start and end. Identifying whether a field is conservative is often the first diagnostic step in classical mechanics and electromagnetism problems.
