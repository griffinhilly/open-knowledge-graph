---
id: vorticity-and-circulation
title: Vorticity and Circulation
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-kinematics
  type: hard
- id: navier-stokes-equations
  type: soft
tags:
- vorticity
- circulation
- irrotational flow
- Kelvin's theorem
- vortex dynamics
- Helmholtz theorems
stage: advanced
status: draft
---
# Vorticity and Circulation

## Core Idea
Vorticity ω = ∇×V is a vector field measuring the local spinning rate of fluid elements. It is twice the angular velocity of an infinitesimal fluid parcel and provides a more fundamental description of rotational effects than velocity alone. Circulation Γ = ∮V·ds is the line integral of velocity around a closed curve and equals the net vorticity flux through any surface bounded by that curve (by Stokes' theorem: Γ = ∫∫ω·dA). Kelvin's circulation theorem states that in an inviscid, barotropic flow with conservative body forces, the circulation around a material loop is constant in time — vorticity is neither created nor destroyed in the interior of such a flow. Vorticity is generated at solid boundaries (where the no-slip condition creates velocity gradients) and diffused by viscosity. Helmholtz's vortex theorems establish that in inviscid flow, vortex lines move with the fluid, vortex tubes have constant strength, and vortex lines cannot end in the fluid interior.

## How It's Best Learned
Compute the vorticity field for several known flows: solid-body rotation (uniform vorticity), free vortex (zero vorticity everywhere except the singular center), Poiseuille pipe flow (linear vorticity distribution), and a shear layer. Verify Stokes' theorem by computing circulation both as a line integral and as a surface integral of vorticity. Then use Kelvin's theorem to explain why a starting vortex is shed when an airfoil begins moving — total circulation must remain zero, so the bound circulation on the wing is balanced by an opposite starting vortex left behind.

## Common Misconceptions
- A free (irrotational) vortex has circular streamlines but zero vorticity everywhere except at the singular center — individual fluid particles orbit without spinning about their own axes. This counterintuitive result confuses many students who equate curved streamlines with rotation.
- Vorticity is not the same as turbulence. Laminar flows (like Poiseuille flow) have well-defined vorticity distributions. Turbulence involves chaotic, three-dimensional vorticity fluctuations, but vorticity itself is present in orderly flows.
- Kelvin's theorem does not mean vorticity cannot appear in real flows. Viscosity, baroclinic effects (density gradients not aligned with pressure gradients), and non-conservative body forces all violate the theorem's assumptions and generate or redistribute vorticity.

## Explainer

From fluid kinematics you know that the velocity gradient tensor ∇V can be decomposed into a symmetric rate-of-strain tensor and an antisymmetric rotation tensor. **Vorticity** ω = ∇×V is twice the antisymmetric part — it measures the instantaneous rate of rotation of a fluid element about its own center. Think of a tiny paddle wheel immersed in the flow: vorticity is the spin rate of that paddle wheel. A flow with ω = 0 everywhere is called **irrotational**, meaning fluid elements translate and deform but do not spin — even if their paths curve dramatically.

This leads to the most important counterintuitive result in the subject: a **free vortex** (the kind you see in a bathtub drain or a tornado far from its core) has circular streamlines — every fluid parcel orbits the center — yet has zero vorticity everywhere except at the singular vortex center itself. How can particles orbit without spinning? Because as each parcel moves along its circular path, it continuously rotates to stay tangent to the circle, but this change in travel direction exactly cancels the spin you would naively expect. In contrast, a **forced vortex** (solid-body rotation, like a spinning bucket of water) has uniform vorticity equal to twice the angular velocity. Distinguishing these two is essential for correct physical reasoning.

**Circulation** Γ = ∮ V·ds is the line integral of velocity around a closed curve. By Stokes' theorem, this equals the flux of vorticity through any surface bounded by that curve: Γ = ∫∫ ω·dA. Circulation is a global measure of rotation in a region, while vorticity is the local measure at a point. For the free vortex with velocity field V = Γ/(2πr) in the tangential direction, a contour enclosing the singular center returns circulation Γ (all contributed by the singularity at r = 0), while a contour not enclosing the center returns zero — consistent with zero vorticity in the fluid interior.

**Kelvin's circulation theorem** states that for an inviscid, barotropic (pressure depends only on density) fluid with conservative body forces, the circulation around any material loop — one that moves with the fluid — is constant in time. This is a conservation law for rotational motion: vorticity cannot be created or destroyed in the interior of such a flow. It can only be generated at solid boundaries (where viscosity enforces the no-slip condition and creates strong velocity gradients) or through baroclinic torques (when density gradients misalign with pressure gradients, as in ocean currents and atmospheric fronts). The theorem beautifully explains why a wing generates lift: as an airfoil accelerates from rest, a **starting vortex** of circulation −Γ is shed into the wake; to conserve the initially-zero total circulation, the wing develops an equal and opposite bound circulation +Γ, which by the Kutta-Joukowski theorem generates lift L = ρV∞Γ per unit span.
