---
id: maxwells-equations-integral-form
title: Maxwell's Equations in Integral Form
domain: physics
course: electrodynamics
prerequisites:
- id: maxwells-equations-differential-form
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- boundary-conditions-em-fields
- electromagnetic-waves-in-media
tags:
- maxwell-equations
- flux
- circulation
stage: formal-systems
status: draft
---

# Maxwell's Equations in Integral Form

## Core Idea
The integral forms relate fluxes and circulations to their sources: Gauss's law (flux = enclosed charge), Ampère-Maxwell law (circulation = enclosed current plus displacement current). These forms apply the divergence and Stokes theorems and often simplify problems with high symmetry.

## Explainer

You already know Maxwell's equations in differential form — four partial differential equations governing how E⃗ and B⃗ vary point by point in space and time. Those equations are the most compact and general statement. The integral forms are not new physics; they are the same equations viewed through the lens of two theorems from your multivariable calculus prerequisite: the **divergence theorem** (∫∫∫ ∇·F dV = ∯ F·dA) and **Stokes' theorem** (∫∫ (∇×F)·dA = ∮ F·dl). Applying these transforms the local, derivative statements into global statements about fluxes and circulations over finite surfaces and volumes.

Gauss's law for E⃗ starts from ∇·E⃗ = ρ/ε₀. Integrating both sides over any closed volume and applying the divergence theorem converts the left side into the **total electric flux** ∯ E⃗·dA⃗ through the bounding surface, and the right side into Q_enc/ε₀. Result: the total outward electric flux through any closed surface equals the total enclosed charge divided by ε₀. For a point charge, choosing a sphere centered on the charge makes the integral trivial — E⃗ is radial and uniform in magnitude on the sphere, so the flux is just 4πr²E, immediately giving Coulomb's law. Gauss's magnetic law ∇·B⃗ = 0 similarly integrates to ∯ B⃗·dA⃗ = 0 — no magnetic monopoles, so every field line that enters a closed surface must exit it.

Faraday's law (∇×E⃗ = −∂B⃗/∂t) and the Ampère-Maxwell law (∇×B⃗ = μ₀J⃗ + μ₀ε₀∂E⃗/∂t) become circulation integrals via Stokes' theorem. Integrating Faraday's law over an open surface and applying Stokes converts ∫∫(∇×E⃗)·dA⃗ into the **EMF** ∮ E⃗·dl⃗ around the boundary loop, while the right side becomes −dΦ_B/dt — the rate of change of magnetic flux. This is the mathematical statement of electromagnetic induction. The Ampère-Maxwell integral form says the circulation of B⃗ around a closed loop equals μ₀ times the total current (conduction plus displacement) passing through any surface bounded by that loop. The freedom to choose "any surface" is what forced Maxwell to add the displacement current term — without it, the two choices of surface for the same loop would give contradictory answers when a capacitor is charging.

The integral forms are often more practical than the differential forms when a problem has a symmetry that makes the integrands nearly constant over a chosen surface or loop. Gauss's law in integral form is the standard tool for finding E⃗ near a sphere, cylinder, or plane of charge. Ampère's law is the standard tool for the field of an infinite wire or inside a solenoid. The strategy is always the same: exploit symmetry to pull the field outside the integral, then solve for its magnitude in one line. The differential forms are more powerful for arbitrary geometries and for deriving wave equations, but the integral forms are what you reach for when symmetry is on your side.
