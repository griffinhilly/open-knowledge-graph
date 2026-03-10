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
status: draft
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
