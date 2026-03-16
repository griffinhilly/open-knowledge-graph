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
status: draft
---

# Conservative Vector Fields and Potential Functions

## Core Idea
A vector field F is conservative if F = ∇f for some scalar potential f. For conservative fields, ∫_C F · dr depends only on endpoints (path-independent). If F is conservative and curl-free (∂Q/∂x = ∂P/∂y for F = ⟨P, Q⟩), then ∫ F · dr around any closed path is zero.

## Explainer

A vector field assigns a vector to each point in space — think of a force field, a velocity field, or the gradient of temperature. From your work with line integrals, you know that computing ∫_C F · dr along a path C generally depends on which path you take. **Conservative vector fields** are the special class where this path-dependence disappears: the integral between two points depends only on the endpoints, not on the route. This is called **path independence**.

The connection between path independence and a potential function is the central theorem. A vector field F is conservative if and only if F = ∇f for some scalar-valued function f, called a **potential function**. The gradient structure makes path independence transparent via the fundamental theorem for line integrals: ∫_C ∇f · dr = f(endpoint) − f(startpoint). The integral telescopes to a simple difference, just as in single-variable calculus ∫_a^b f'(x)dx = f(b) − f(a). Only the endpoint values of f matter; the path is irrelevant.

To test whether a field F = ⟨P, Q⟩ is conservative on a simply connected region, check the **curl condition**: ∂Q/∂x = ∂P/∂y. If F = ∇f, Clairaut's theorem requires that the mixed partials of f are equal, which forces this condition. On simply connected domains, the condition is also sufficient — you can then construct f explicitly by integrating P with respect to x, then differentiating the result with respect to y and matching it to Q to pin down the y-dependent part.

The physical intuition is energy: in a conservative force field (gravity, electrostatics), moving an object between two points costs the same work regardless of path — energy depends only on position. A round trip back to the starting point costs zero net work. Non-conservative fields (friction, magnetic forces) do not have this property: work dissipated or injected depends on how you travel, not just where you start and end. Identifying whether a field is conservative is often the first diagnostic step in classical mechanics and electromagnetism problems.
