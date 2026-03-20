---
id: rotating-flow-vortex-motion-circulation
title: Rotating Flow, Vortex Motion, and Circulation
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-kinematics
  type: hard
- id: bernoullis-equation
  type: soft
builds-toward:
- lift-and-circulation-generation-vortex
tags:
- rotation
- vortex
- circulation
stage: advanced
status: draft
---

# Rotating Flow, Vortex Motion, and Circulation

## Core Idea
Fluids in rotation exhibit tangential velocity and pressure distributions driven by centrifugal effects. Free vortex motion (constant circulation Γ, V_θ = Γ/r) occurs in drains and natural phenomena with negligible friction. Forced vortex motion (rigid-body-like rotation, V_θ = ωr) occurs in centrifuges and stirred tanks. The pressure gradient in the radial direction supplies centripetal acceleration: ∂P/∂r = ρV_θ²/r.

## How It's Best Learned
Fill a cylinder with water, spin it, and observe the parabolic free surface in forced vortex motion. Measure tangential velocity at different radii and pressure at different heights to verify theoretical predictions. Compare to free vortex behavior (e.g., bathtub drain vortex) where friction is minimal.

## Explainer

From fluid kinematics, you know that a fluid element can translate, deform, and rotate. Rotation — the spin of an infinitesimal fluid parcel about its own center — is measured by **vorticity** ω = ∇ × V. Vortex motion is what arises when rotation is organized spatially: fluid swirls in circles around an axis. But not all swirling flows are the same, and the distinction between free and forced vortices is fundamental to understanding drains, hurricanes, centrifuges, and aerodynamic lift.

In a **free vortex**, fluid swirls around a center with no viscous forces doing work — it is an irrotational flow field despite the circular path. Angular momentum is conserved: since there is no torque, ρ·r·V_θ = constant, which gives V_θ = Γ/(2πr). The tangential velocity increases as radius decreases — the same physics as a figure skater who spins faster when pulling in their arms. The pressure drops toward the center (following from Bernoulli along streamlines), which is why a drain creates a low-pressure dimple and why the central column of a tornado is at very low pressure. The **circulation** Γ = ∮ V·dl (the line integral of velocity around a closed loop) is the conserved quantity and characterizes the vortex strength.

In a **forced vortex**, an external mechanism continuously drives rotation — a stirrer, a centrifuge impeller, or the wall of a rotating drum. All fluid rotates as a rigid body: V_θ = ωr. Velocity increases with radius, not decreases. The centripetal acceleration required to keep each fluid parcel on a circular path must be supplied by a radial pressure gradient: ∂P/∂r = ρV_θ²/r. Integrating this outward gives a pressure that increases with r², and the free surface of a rotating liquid takes on a parabolic shape — the classical result from rigid-body rotation. Unlike the free vortex, this flow has nonzero vorticity everywhere (ω = 2Ω), which is why it requires continuous energy input to maintain.

Real vortices are neither purely free nor purely forced. The **Rankine vortex** is a useful model: a forced inner core of radius r_c (rigid-body rotation) surrounded by a free outer region (irrotational). This captures the essential structure of a tornado (violent solid-body rotation in the eye, decaying free-vortex structure in the spiral bands), a bathtub drain, and tip vortices trailing from aircraft wings. At r_c the velocity reaches a maximum; beyond it, V_θ ∝ 1/r falls off. This is the most common vortex model in engineering calculations.

**Kelvin's circulation theorem** states that for an inviscid fluid, Γ around any material loop is conserved in time. This has a profound consequence for aerodynamics: if a wing starts from rest (Γ = 0 everywhere), it cannot develop bound circulation (which creates lift) without shedding an equal and opposite **starting vortex** into the wake. The circulation around the wing and the circulation of the starting vortex sum to zero, satisfying Kelvin's theorem. This is why jet aircraft leave trailing vortices that persist for minutes — they are the necessary counterpart to the lift the wings generate. Rotating flow is not merely a fluid curiosity; it is the physical basis of flight.
