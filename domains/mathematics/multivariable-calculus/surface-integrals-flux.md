---
id: surface-integrals-flux
title: Surface Integrals and Flux of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: greens-theorem
  type: hard
- id: parametric-surfaces
  type: hard
builds-toward:
- stokes-and-divergence-theorems
tags:
- surface-integrals
- flux
- normal-vectors
stage: formal-systems
status: draft
---

# Surface Integrals and Flux of Vector Fields

## Core Idea
The surface integral ∬_S F · dS computes flux (net flow of F through S). Using parametrization r(u, v), dS = (r_u × r_v) du dv, and the integral becomes ∬_D F(r(u,v)) · (r_u × r_v) du dv. Orientation (choice of normal direction) affects the sign.

## Explainer

You've already seen Green's theorem relate a line integral around a closed curve to a double integral over the region it encloses. Surface integrals are the three-dimensional extension of this idea, and the concept of **flux** is the physical motivation. Imagine a vector field **F** representing fluid flow — at each point, **F** gives the velocity of the fluid. The flux through a surface S is the net volume of fluid crossing S per unit time. Fluid pushing through "with" the chosen normal counts as positive; fluid pushing against it counts as negative.

The machinery relies on your parametric surfaces knowledge. Given a parametrization **r**(u, v) mapping a parameter domain D ⊂ ℝ² to the surface S, the partial derivatives **r**_u and **r**_v are tangent vectors to the surface. Their cross product **r**_u × **r**_v is **perpendicular** to the surface (a normal vector) and its magnitude |**r**_u × **r**_v| measures the local area distortion — how much the parametrization stretches or compresses the parameter rectangle du dv onto the actual surface. The vector area element **dS** = (**r**_u × **r**_v) du dv bundles both pieces: it points in the normal direction and has magnitude equal to the surface area of the small patch.

The flux integral then becomes ∬_D **F**(**r**(u, v)) · (**r**_u × **r**_v) du dv — a standard double integral over the parameter domain. The dot product extracts the component of **F** in the normal direction: if **F** flows parallel to the surface, it contributes zero flux (it's not crossing S); only the component *through* S matters. This is why orientation is essential: flipping the normal direction negates the cross product, which negates every dot product, which negates the entire integral. For a closed surface (like a sphere), the outward normal is the conventional positive orientation.

A helpful scaling check: if **F** is constant and the surface is flat with area A and unit normal **n̂**, then the flux is simply **F** · **n̂** · A — the constant normal component of the field times the total area. The surface integral formula reduces to this in the flat constant case, confirming the geometric interpretation. For curved surfaces and non-constant fields, the integral sums infinitely many such infinitesimal contributions. This concept is foundational for Stokes' theorem and the Divergence theorem ahead: both connect surface integrals to volume integrals or to line integrals around boundary curves, completing the hierarchy of integral theorems that generalize the Fundamental Theorem of Calculus to higher dimensions.
