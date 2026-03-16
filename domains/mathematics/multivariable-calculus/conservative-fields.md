---
id: conservative-fields
title: Conservative Vector Fields and Potential Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-vector-fields
  type: hard
- id: gradient-vector
  type: hard
- id: partial-derivatives
  type: hard
- id: directional-derivatives
  type: soft
builds-toward:
- fundamental-theorem-line-integrals
- greens-theorem
- stokes-theorem
tags:
- conservative
- potential-function
- path-independence
- exact-differential
stage: formal-systems
status: validated
---
# Conservative Vector Fields and Potential Functions

## Core Idea
A vector field F is conservative if ∫_C F · dr is independent of the path from start to end — it depends only on the endpoints. F is conservative if and only if F = ∇f for some scalar potential function f. For F = ⟨P, Q⟩ in a simply connected domain, the test for conservativeness is ∂P/∂y = ∂Q/∂x (the mixed partial equality condition). A conservative field does zero net work around any closed loop: ∮_C F · dr = 0.

## How It's Best Learned
The equivalences — path independence, zero circulation on closed loops, existence of a potential function, and the curl test — should all be presented together. Visualize: a conservative field is like a gravitational field where the work against gravity equals the change in potential energy regardless of the route taken. Finding the potential function requires integrating and comparing partial derivatives.

## Common Misconceptions
- ∂P/∂y = ∂Q/∂x is necessary but only sufficient when the domain is simply connected (no holes). On domains with holes, this test can fail to detect non-conservative fields.
- A conservative field has zero curl everywhere; the converse is true only on simply connected domains.
- The potential function f is determined only up to a constant: if F = ∇f, then F = ∇(f + C) for any constant C.

## Explainer

From your study of line integrals, you know that ∫_C F · dr computes the work done by a vector field F along a curve C, and this integral generally depends on the path taken. A **conservative vector field** is the special case where path does not matter: for any two curves connecting the same endpoints, the work integral is identical. Equivalently, any closed-loop integral ∮_C F · dr = 0 — going around a loop and returning to start nets zero work. The physical analogy is gravity or electrostatics: the work to lift a mass from ground level to height h is mgh regardless of which zigzag path you take. Path-independence is what distinguishes these "well-behaved" fields from general ones.

You also know the gradient vector ∇f from your partial derivatives work. A vector field F is conservative if and only if it equals the gradient of some scalar **potential function** f: F = ∇f = ⟨∂f/∂x, ∂f/∂y⟩. When a potential function exists, path-independence is immediate: by the chain rule, the work from point A to point B equals f(B) − f(A), just like the single-variable Fundamental Theorem of Calculus. The potential is determined only up to a constant — ∇(f + C) = ∇f for any constant C — so there is a whole family of valid potentials, and you should always specify the constant (often by setting f = 0 at a reference point) when a unique answer is needed.

To test whether F = ⟨P, Q⟩ is conservative without finding f explicitly, use the **mixed partial test**: if F = ∇f, then P = ∂f/∂x and Q = ∂f/∂y. Clairaut's theorem guarantees ∂P/∂y = ∂²f/∂y∂x = ∂²f/∂x∂y = ∂Q/∂x. So ∂P/∂y = ∂Q/∂x is necessary. It is also sufficient on **simply connected domains** — regions with no holes, where every closed loop can be continuously shrunk to a point. On domains with holes (such as ℝ² minus the origin), a field can satisfy the mixed partial test everywhere yet still fail to be conservative, because a loop encircling the hole cannot be contracted.

To find the potential function when F is confirmed conservative, integrate P with respect to x (treating y as a constant): f(x, y) = ∫P dx + g(y). Then differentiate the result with respect to y and set it equal to Q to determine g(y). This pins down any y-dependent terms that were invisible in the x-integration. The four characterizations — F = ∇f, path-independence, zero circulation on closed loops, and equal mixed partials — are all equivalent on simply connected domains. Each framing is most useful for different problems, and recognizing them as the same property is the key insight that makes conservative fields the clean foundation for Green's theorem and Stokes' theorem.
