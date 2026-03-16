---
id: conservative-fields-potential
title: Conservative Vector Fields and Potential Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: fundamental-theorem-line-integrals
  type: hard
builds-toward:
- curl-and-divergence
tags:
- conservative-fields
- potential-functions
- path-independence
stage: formal-systems
status: draft
---

# Conservative Vector Fields and Potential Functions

## Core Idea
A vector field F is conservative if F = ∇f for some potential function f. Conservative fields have zero curl (∇ × F = 0 for continuous partials) and satisfy the property that ∮_C F · dr = 0 for any closed curve C. Magnetic fields are irrotational models of conservation.

## Explainer

The **Fundamental Theorem for Line Integrals** — your prerequisite — says that if F = ∇f, then ∫_C F · dr = f(B) − f(A), where A and B are the endpoints of C. This is the multivariable analogue of the Fundamental Theorem of Calculus: the line integral depends only on the values of f at the endpoints, not on the path taken. A **conservative vector field** is precisely one for which this path-independence holds. The name "conservative" comes from physics: in a conservative force field, the work done moving a particle depends only on start and end position, so energy is conserved (no energy is gained or lost by taking a roundabout path).

The central equivalence theorem (in a simply-connected domain) is: F is conservative ↔ F = ∇f for some scalar **potential function** f ↔ ∮_C F · dr = 0 for every closed curve C ↔ the curl of F is zero (∇ × F = 0). Each of these four conditions implies all the others. Zero curl is the easiest to check computationally — it only requires partial derivatives. For F = ⟨P, Q, R⟩, the condition is ∂P/∂y = ∂Q/∂x, ∂P/∂z = ∂R/∂x, ∂Q/∂z = ∂R/∂y. In R² this reduces to ∂P/∂y = ∂Q/∂x.

When you have confirmed F is conservative and want to find the potential function f, the method is systematic: since F = ∇f means ∂f/∂x = P, ∂f/∂y = Q, ∂f/∂z = R, integrate the first component with respect to x (introducing a function of y and z as the "constant"), then differentiate with respect to y and match against Q to pin down that function, then differentiate with respect to z to pin down any remaining constant. Each integration step is like running the Fundamental Theorem of Calculus in one variable while treating others as parameters.

The condition that the domain is **simply connected** — containing no "holes" — is crucial. A vector field with zero curl on a domain with holes (like R² minus the origin) may fail to be conservative globally, even though it locally looks like a gradient field. The classic example is F = ⟨−y, x⟩/(x² + y²), which has zero curl away from the origin but whose line integral around a circle enclosing the origin is nonzero. This is why simply-connected domains are required in the equivalence theorem: holes allow closed paths that cannot be contracted to a point, which is exactly the topological obstruction to path-independence.
