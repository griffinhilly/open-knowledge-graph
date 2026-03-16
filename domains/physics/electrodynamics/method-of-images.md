---
id: method-of-images
title: Method of Images in Electrostatics
domain: physics
course: electrodynamics
prerequisites:
- id: electric-field-and-coulombs-law
  type: hard
- id: electric-potential-and-potential-energy
  type: hard
builds-toward:
- boundary-value-problems-em
tags:
- boundary-value-problems
- images
- boundary-conditions
stage: abstract-reasoning
status: draft
---

# Method of Images in Electrostatics

## Core Idea
Method of images solves boundary value problems by replacing boundaries with image charges producing the same boundary conditions. A charge near a grounded conducting plane is equivalent to the charge plus its opposite image at the mirror position. This elegant technique gives exact solutions for high-symmetry geometries.

## Explainer

When a charge +q sits near a grounded conducting plane, something nontrivial happens: the field of the charge induces a distribution of surface charges on the conductor, and those induced charges produce their own field that modifies the total field in the space above the plane. Solving for the induced charge distribution directly requires solving an integral equation — difficult. The **method of images** sidesteps this entirely with a clever trick: forget the conductor and its surface charges, and ask instead whether there is a simple arrangement of point charges that produces exactly the same boundary condition.

The answer for a grounded plane is yes. Place a **image charge** of −q at the mirror-image position below the plane. The combined field of +q and −q has exactly zero potential on the plane (by symmetry, the plane is equidistant from both charges, so their contributions cancel in potential there). Since the boundary condition — zero potential on the grounded plane — is satisfied, and the field equation (Laplace's equation) holds everywhere above the plane with the correct source at +q's location, the uniqueness theorem guarantees this is the correct solution. The image charge is a mathematical fiction — it lives in the conductor where we are not solving — but its field in the region of interest is real.

The key conceptual steps are: (1) identify a set of image charges outside the domain where you want the solution, (2) choose their magnitudes and positions so that the boundary conditions are satisfied on every boundary, and (3) invoke uniqueness to guarantee that this configuration is the unique correct solution. The method works beautifully for a charge near a grounded sphere — the image charge has magnitude q' = −(R/d)q and is placed at the inverse point inside the sphere — and for charges near the junction of two conducting planes at right angles.

Why does this matter beyond clever problem-solving? The method of images reveals a deep physical truth: a conductor responds to nearby charges by rearranging its surface charges to enforce its boundary condition, and this response is mathematically identical to what a set of image charges would produce. The induced surface charge density on the plane can be read off directly from the image-charge solution using σ = −ε₀ ∂V/∂n. You can then compute the force on the real charge — which turns out to be exactly the Coulomb force between the real charge and its image: F = −kq²/(2d)² toward the plane. This "image force" is the reason that charged particles are attracted to nearby conductors even when the conductor carries no net charge.
