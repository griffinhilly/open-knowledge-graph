---
id: boundary-conditions-em-fields
title: Boundary Conditions at Conducting and Dielectric Interfaces
domain: physics
course: electrodynamics
prerequisites:
- id: maxwells-equations-integral-form
  type: hard
- id: electric-field-and-coulombs-law
  type: soft
builds-toward:
- boundary-value-problems-em
- electromagnetic-waves-in-media
tags:
- boundary-conditions
- conductors
- dielectrics
stage: abstract-reasoning
status: draft
---

# Boundary Conditions at Conducting and Dielectric Interfaces

## Core Idea
Boundary conditions encode field behavior at interfaces. At perfect conductors: normal E is discontinuous (= σ/ε₀), tangential E = 0; normal B continuous, tangential B discontinuous (= μ₀K). At dielectric interfaces: normal D continuous, tangential E continuous. Essential for solving realistic problems with boundaries.

## Explainer

Maxwell's equations in integral form tell you about fields averaged over surfaces and loops. Boundary conditions are what you get when you shrink those surfaces and loops to a thin sliver right at an interface — they are Maxwell's equations in the limit where the integration region straddles the boundary. You already know both tools: the divergence theorem relates volume integrals to surface fluxes (used for Gauss's law), and Stokes' theorem relates surface integrals to line integrals (used for Faraday's and Ampère's laws). Boundary conditions are those theorems applied at the boundary itself.

To derive the **normal boundary conditions**, apply Gauss's law to a thin "pillbox" straddling the interface with vanishingly thin height. The flux through the two flat faces gives the discontinuity in the normal component of the field. For the electric field, ∇·D = ρ_free gives (D₂ − D₁) · n̂ = σ_free, where σ_free is any free surface charge density. If there is no surface charge, the normal component of D is continuous. Since D = ε₀εE, this means normal E can be discontinuous if the dielectric constant ε changes across the boundary. For the magnetic field, ∇·B = 0 always, so normal B is always continuous — there are no magnetic "surface charges."

For the **tangential boundary conditions**, apply Faraday's or Ampère's law to a thin rectangular loop that straddles the interface with vanishingly thin height. The contributions from the short sides vanish, leaving only the two long sides parallel to the interface. Faraday's law (with ∂B/∂t → 0 for the thin loop) gives continuous tangential E across any interface. Ampère's law gives a discontinuity in tangential H equal to any surface current density K: (H₂ − H₁) × n̂ = K. At a perfect conductor, tangential E = 0 (otherwise infinite current would flow) and normal B = 0 inside, which forces specific surface conditions outside.

These conditions are not just abstract rules — they are the matching conditions that make unique solutions possible in problems with boundaries. When you solve for fields in two regions (say, vacuum above and dielectric below a flat interface), you solve the governing equations in each region separately, then stitch the solutions together by demanding the boundary conditions are satisfied. Without these conditions, the problem is underdetermined: infinitely many field configurations could satisfy Maxwell's equations in each region individually. Boundary conditions select the unique physical solution, and they are the indispensable bridge between theory and realistic geometry in electromagnetism.
