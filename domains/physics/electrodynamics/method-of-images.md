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

## Questions

```yaml
- question: "A charge +q is placed a distance d above a grounded, infinite conducting plane. In the method of images, what replaces the conductor to produce the same boundary conditions?"
  type: multiple-choice
  options:
    - "A continuous surface charge distribution spread evenly across the plane"
    - "A single image charge −q placed at the mirror-image position below the plane"
    - "A charge +q placed at the mirror-image position below the plane"
    - "The boundary conditions are removed, and Laplace's equation is solved numerically"
  answer: 1
  explanation: "The image charge −q placed at the mirror position below the plane ensures that the combined potential of +q and −q is exactly zero on the grounded plane (by symmetry, the plane is equidistant from both). This satisfies the boundary condition. A +q image would not cancel the potential on the plane; a surface distribution is what we are replacing, not recreating."

- question: "A student uses the image charge −q below the plane to compute the electric field everywhere above the grounded conducting plane. The student's advisor says: 'The image charge doesn't physically exist.' Which statement best resolves this?"
  type: multiple-choice
  options:
    - "The advisor is wrong — the image charge is physically real and causes the induced surface charges"
    - "The advisor is right — the image charge is a mathematical fiction that lives in the conductor region; its field above the plane is real and equals the field from the actual induced surface charges"
    - "The advisor is right, and the field from the image charge should not be included in the solution above the plane"
    - "The image charge is real only at the conducting surface, not below it"
  answer: 1
  explanation: "The image charge is a mathematical device — it lives in the region (inside the conductor) where we are *not* solving for the field. But the uniqueness theorem guarantees that any configuration satisfying the correct boundary conditions and source distribution is the unique solution in the region of interest. The field from the image charge above the plane is physically real and identical to the field the actual induced surface charges would produce."

- question: "The force on a charge +q placed a distance d above a grounded conducting plane equals the Coulomb force between +q and its image charge −q at distance 2d away."
  type: true-false
  answer: true
  explanation: "The method of images gives the force on the real charge directly: it is the Coulomb attraction between +q and −q separated by 2d (the real charge at distance d above, image at distance d below). This 'image force' explains why charged particles are attracted to nearby conductors even when the conductor carries no net charge — the conductor rearranges its surface charges to create exactly the response that an opposite image charge would."

- question: "The method of images works by directly computing the distribution of induced surface charges on the conductor, then using those charges to find the field."
  type: true-false
  answer: false
  explanation: "This is precisely what the method avoids. Computing induced surface charges directly requires solving an integral equation — the hard problem. Instead, the method asks: is there a simple arrangement of point charges (image charges) outside the domain that produces the correct boundary conditions? If yes, the uniqueness theorem guarantees that the total field in the region of interest is the unique correct solution, without ever computing the surface charge distribution explicitly."

- question: "Why does the uniqueness theorem guarantee that the image charge solution is correct, even though the image charge is not physically present in the conductor?"
  type: short-answer
  answer: "The uniqueness theorem for electrostatics states that if you find any solution to Laplace's equation in a region that satisfies the correct boundary conditions and has the correct source charges, it is the only solution. The image charge configuration satisfies both: the real charge +q is the correct source in the region above the plane, and the combined potential of +q and its image −q equals zero on the grounded plane (correct boundary condition). Therefore, this must be the unique correct solution above the plane — regardless of whether the image charge is real."
  explanation: "Uniqueness is the linchpin of the entire technique. Without it, finding one configuration that satisfies the boundary conditions would not be enough — there could be infinitely many solutions. Uniqueness collapses that possibility: one valid solution is the only solution. The image charge is a clever way to construct that one valid solution without solving the hard integral equation for the surface charge distribution."
```

## Explainer

When a charge +q sits near a grounded conducting plane, something nontrivial happens: the field of the charge induces a distribution of surface charges on the conductor, and those induced charges produce their own field that modifies the total field in the space above the plane. Solving for the induced charge distribution directly requires solving an integral equation — difficult. The **method of images** sidesteps this entirely with a clever trick: forget the conductor and its surface charges, and ask instead whether there is a simple arrangement of point charges that produces exactly the same boundary condition.

The answer for a grounded plane is yes. Place a **image charge** of −q at the mirror-image position below the plane. The combined field of +q and −q has exactly zero potential on the plane (by symmetry, the plane is equidistant from both charges, so their contributions cancel in potential there). Since the boundary condition — zero potential on the grounded plane — is satisfied, and the field equation (Laplace's equation) holds everywhere above the plane with the correct source at +q's location, the uniqueness theorem guarantees this is the correct solution. The image charge is a mathematical fiction — it lives in the conductor where we are not solving — but its field in the region of interest is real.

The key conceptual steps are: (1) identify a set of image charges outside the domain where you want the solution, (2) choose their magnitudes and positions so that the boundary conditions are satisfied on every boundary, and (3) invoke uniqueness to guarantee that this configuration is the unique correct solution. The method works beautifully for a charge near a grounded sphere — the image charge has magnitude q' = −(R/d)q and is placed at the inverse point inside the sphere — and for charges near the junction of two conducting planes at right angles.

Why does this matter beyond clever problem-solving? The method of images reveals a deep physical truth: a conductor responds to nearby charges by rearranging its surface charges to enforce its boundary condition, and this response is mathematically identical to what a set of image charges would produce. The induced surface charge density on the plane can be read off directly from the image-charge solution using σ = −ε₀ ∂V/∂n. You can then compute the force on the real charge — which turns out to be exactly the Coulomb force between the real charge and its image: F = −kq²/(2d)² toward the plane. This "image force" is the reason that charged particles are attracted to nearby conductors even when the conductor carries no net charge.
