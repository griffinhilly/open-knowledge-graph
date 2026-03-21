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

## Questions

```yaml
- question: "A fluid parcel near a bathtub drain is traveling in a circular path around the drain. A student argues: 'Any particle moving in a circle must be rotating — it has angular velocity around the center, so the vorticity must be nonzero.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Fluid parcels near a drain do not actually move in circles — they spiral inward radially and never complete a full orbit"
    - "Vorticity measures the spin of a fluid parcel about its own center, not the curvature of its path around a fixed point — in a free vortex, fluid parcels orbit without spinning about themselves"
    - "The student is correct; free vortex flow has high vorticity near the center where V_θ is largest"
    - "Vorticity is only defined for forced vortices; free vortex flow is described by circulation rather than vorticity"
  answer: 1
  explanation: "Vorticity ω = ∇ × V measures local spin — rotation of a fluid parcel about its own center of mass. In a free vortex (V_θ = Γ/2πr), the curl of the velocity field is zero everywhere except the singular center: ∇ × V = 0. Fluid parcels travel in circles (orbital motion) but do not spin about themselves. The analogy: a car driving in a circle at a roundabout is not necessarily rotating (spinning) about its own center — it is translating along a curved path. A floating cork in a bathtub vortex orbits the drain but maintains the same orientation, never rotating about its own axis. This irrotational property of the free vortex is why it fits within potential flow theory."

- question: "In a free vortex (V_θ = Γ/2πr), pressure increases toward the center. In a forced vortex (V_θ = ωr, solid-body rotation), pressure also increases toward the outside. What accounts for the different pressure distribution in each case?"
  type: multiple-choice
  options:
    - "Forced vortices require continuous energy input, which manifests as elevated pressure; free vortices are passive and maintain lower pressure throughout"
    - "Both vortex types have identical pressure distributions; they differ only in their tangential velocity profiles"
    - "In both cases ∂P/∂r = ρV_θ²/r > 0, so pressure increases outward; but in the free vortex the steep rise of V_θ toward the center creates a very low-pressure core, while in the forced vortex the pressure increases monotonically from center outward with no such extreme minimum"
    - "The pressure difference is an artifact of cylindrical coordinates; in Cartesian coordinates both vortices have identical pressure fields"
  answer: 2
  explanation: "The radial momentum equation ∂P/∂r = ρV_θ²/r applies to both — pressure always increases outward (centripetal acceleration requires inward pressure gradient). In a forced vortex (V_θ = ωr), the pressure rises smoothly from the center outward: P ∝ r². In a free vortex (V_θ = Γ/2πr), V_θ increases steeply as r → 0, and integrating the pressure gradient inward gives a dramatic pressure drop toward the singular center — the low-pressure vortex core of a tornado or drain. The centrifuge exploits the forced vortex pressure rise (denser material goes outward); the tornado's destructive suction exploits the free vortex pressure drop (the core is far below atmospheric)."

- question: "According to Kelvin's circulation theorem, when a wing develops bound circulation to generate lift, an equal and opposite starting vortex must be shed into the wake to conserve total circulation."
  type: true-false
  answer: true
  explanation: "Kelvin's theorem: for an inviscid fluid, the circulation around any material loop is conserved over time. Before the wing starts moving, total circulation is zero everywhere. When the wing develops bound circulation Γ_wing (which generates lift via the Kutta-Joukowski theorem), an equal and opposite starting vortex Γ_start = −Γ_wing must be shed — so that total circulation remains zero. This starting vortex is deposited in the wake and can briefly be observed during takeoff. The bound circulation on the wing and the trailing vortices shed at the wingtips are the direct consequence of Kelvin's conservation law. Jet aircraft trailing vortices — hazardous to following planes for minutes after passage — are the real-world manifestation of this theorem."

- question: "In a free vortex, fluid farther from the center moves faster than fluid close to the center, because the larger radius gives fluid parcels more rotational momentum."
  type: true-false
  answer: false
  explanation: "In a free vortex, V_θ = Γ/(2πr) — velocity INCREASES as radius DECREASES. Fluid closest to the center moves fastest. Angular momentum per unit mass (r × V_θ = Γ/2π) is conserved, so as a parcel moves inward (r decreases), its tangential speed must increase proportionally — just as a figure skater spins faster when pulling in her arms. The rapid increase in velocity near the center creates the low-pressure core characteristic of drains and tornadoes. This is opposite to a forced vortex (solid-body rotation, V_θ = ωr), where fluid farther from the center does move faster. Distinguishing these two cases is fundamental to understanding rotating flow."

- question: "Explain why the free vortex flow field is described as 'irrotational' even though fluid parcels travel in circular paths. What physical picture clarifies the distinction between the parcel's orbital motion and its local rotation?"
  type: short-answer
  answer: "Irrotational means each fluid parcel does not spin about its own center of mass — its vorticity (∇ × V) is zero. In a free vortex, parcels orbit the center but each parcel maintains a fixed orientation, never rotating about itself. Mathematically, computing ∇ × V for V_θ = Γ/(2πr) gives zero everywhere outside the singular center. The physical picture: imagine a small cork floating in a bathtub drain vortex. The cork orbits the drain but always faces the same wall — it translates along a curved path without spinning. In a forced vortex (solid-body rotation, V_θ = ωr), the cork would spin like a pinwheel, completing one self-rotation per orbit. Vorticity measures only that local spin, not the curvature of the path. The free vortex's irrotational character places it within potential flow theory, making it analytically tractable and directly applicable to aerodynamic lift calculations."
  explanation: "The distinction between orbital motion and self-rotation is the central conceptual trap of vortex mechanics. Fluid dynamics students who conflate 'circular path' with 'rotation' will incorrectly classify free vortex flow as rotational. The cork thought experiment gives a concrete, physical way to test: does the parcel spin about itself? If not, vorticity is zero regardless of path curvature."
```

## Explainer

From fluid kinematics, you know that a fluid element can translate, deform, and rotate. Rotation — the spin of an infinitesimal fluid parcel about its own center — is measured by **vorticity** ω = ∇ × V. Vortex motion is what arises when rotation is organized spatially: fluid swirls in circles around an axis. But not all swirling flows are the same, and the distinction between free and forced vortices is fundamental to understanding drains, hurricanes, centrifuges, and aerodynamic lift.

In a **free vortex**, fluid swirls around a center with no viscous forces doing work — it is an irrotational flow field despite the circular path. Angular momentum is conserved: since there is no torque, ρ·r·V_θ = constant, which gives V_θ = Γ/(2πr). The tangential velocity increases as radius decreases — the same physics as a figure skater who spins faster when pulling in their arms. The pressure drops toward the center (following from Bernoulli along streamlines), which is why a drain creates a low-pressure dimple and why the central column of a tornado is at very low pressure. The **circulation** Γ = ∮ V·dl (the line integral of velocity around a closed loop) is the conserved quantity and characterizes the vortex strength.

In a **forced vortex**, an external mechanism continuously drives rotation — a stirrer, a centrifuge impeller, or the wall of a rotating drum. All fluid rotates as a rigid body: V_θ = ωr. Velocity increases with radius, not decreases. The centripetal acceleration required to keep each fluid parcel on a circular path must be supplied by a radial pressure gradient: ∂P/∂r = ρV_θ²/r. Integrating this outward gives a pressure that increases with r², and the free surface of a rotating liquid takes on a parabolic shape — the classical result from rigid-body rotation. Unlike the free vortex, this flow has nonzero vorticity everywhere (ω = 2Ω), which is why it requires continuous energy input to maintain.

Real vortices are neither purely free nor purely forced. The **Rankine vortex** is a useful model: a forced inner core of radius r_c (rigid-body rotation) surrounded by a free outer region (irrotational). This captures the essential structure of a tornado (violent solid-body rotation in the eye, decaying free-vortex structure in the spiral bands), a bathtub drain, and tip vortices trailing from aircraft wings. At r_c the velocity reaches a maximum; beyond it, V_θ ∝ 1/r falls off. This is the most common vortex model in engineering calculations.

**Kelvin's circulation theorem** states that for an inviscid fluid, Γ around any material loop is conserved in time. This has a profound consequence for aerodynamics: if a wing starts from rest (Γ = 0 everywhere), it cannot develop bound circulation (which creates lift) without shedding an equal and opposite **starting vortex** into the wake. The circulation around the wing and the circulation of the starting vortex sum to zero, satisfying Kelvin's theorem. This is why jet aircraft leave trailing vortices that persist for minutes — they are the necessary counterpart to the lift the wings generate. Rotating flow is not merely a fluid curiosity; it is the physical basis of flight.
