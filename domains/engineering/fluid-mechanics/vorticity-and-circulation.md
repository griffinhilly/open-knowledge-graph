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
stage: formal-systems
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
