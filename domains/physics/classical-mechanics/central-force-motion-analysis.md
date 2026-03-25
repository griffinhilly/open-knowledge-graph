---
id: central-force-motion-analysis
title: Central Force Motion and Orbital Dynamics
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-angular-momentum
  type: hard
- id: effective-potential-central-forces
  type: hard
- id: orbital-mechanics
  type: soft
- id: polar-coordinates
  type: hard
- id: stability-of-circular-orbits
  type: soft
- id: orbital-stability-mechanics
  type: soft
tags:
- central-forces
- orbits
- dynamics
stage: formal-systems
status: validated
---
# Central Force Motion and Orbital Dynamics

## Core Idea
Central forces (pointing toward or away from a center) conserve angular momentum and allow reduction to 1D radial motion via effective potential. Bound orbits are closed curves whose shapes depend on the force law and energy.

## Questions

```yaml
- question: "Why does a central force conserve angular momentum?"
  type: multiple-choice
  options:
    - "Because the magnitude of the force depends only on the distance from the center"
    - "Because the force is always perpendicular to the velocity of the particle"
    - "Because the force is parallel to the position vector, making the torque r × F equal to zero"
    - "Because the kinetic energy is constant throughout the motion"
  answer: 2
  explanation: "Angular momentum changes only when torque is applied: dL/dt = τ = r × F. For a central force, F = F(r)r̂ — it points along r̂, which is parallel to r. Since r and F are parallel, their cross product r × F = 0. Zero torque means L is conserved. Option A (magnitude depending only on r) is part of the definition of a central force but not itself the reason angular momentum is conserved — it is the direction of the force that matters."

- question: "A particle orbiting under a 1/r² attractive force has total energy E = −3 J. The effective potential has a minimum of U_eff_min = −5 J. What type of orbit does the particle follow?"
  type: multiple-choice
  options:
    - "Unbound (hyperbolic), because the total energy is negative"
    - "Circular, because E equals the minimum of U_eff"
    - "Bound, oscillating radially between a minimum and maximum radius"
    - "The orbit type cannot be determined without knowing the angular momentum"
  answer: 2
  explanation: "E = −3 J > U_eff_min = −5 J means the particle has more energy than the minimum of the effective potential but still less than the escape threshold (E < 0 for this force). It is trapped in the effective potential well, oscillating between two turning points where E = U_eff(r). This is a bound, non-circular orbit (an ellipse for a 1/r² force). Option B would be a circular orbit, which requires E = U_eff_min exactly. Option A is wrong because E < 0 alone does not determine boundedness — the shape of U_eff matters."

- question: "A particle with nonzero angular momentum moving under an attractive central force will eventually spiral into the origin (r = 0) if the attractive force is strong enough."
  type: true-false
  answer: false
  explanation: "The centrifugal term L²/(2μr²) in the effective potential diverges to +∞ as r → 0. For any particle with L ≠ 0, this creates a repulsive barrier that prevents collapse to the origin, regardless of how strongly attractive U(r) is at small r. Only a particle with exactly zero angular momentum — falling straight toward the center with no transverse motion — can actually reach r = 0. Angular momentum is the 'guard' that keeps orbiting particles from collapsing."

- question: "For a 1/r² attractive force, all bound orbits are closed ellipses. For most other central force laws, bound orbits precess rather than closing."
  type: true-false
  answer: true
  explanation: "This is Bertrand's theorem: only two central force laws produce closed bound orbits for all energies — the 1/r² force (gravity, Coulomb) and the harmonic oscillator (F ∝ r). For any other force law, the radial oscillation period and the orbital period are generally incommensurable, causing the orbit to precess. The anomalous precession of Mercury's perihelion was a key confirmation of general relativity precisely because Newtonian 1/r² gravity predicts perfectly closed ellipses, and the observed excess precession had no Newtonian explanation."

- question: "Explain physically what the centrifugal potential term L²/(2μr²) represents and why it appears in the effective potential."
  type: short-answer
  answer: "When the 2D orbit problem is reduced to a 1D radial equation, the particle's rotational kinetic energy gets absorbed into the effective potential. Angular momentum conservation gives φ̇ = L/(μr²), so the rotational kinetic energy (1/2)μr²φ̇² = L²/(2μr²) depends only on r. This term acts as a repulsive barrier: as r decreases, the particle must rotate faster to conserve angular momentum, and more of its energy is tied up in rotation rather than available for radial motion. The closer to the center, the stronger the effective repulsion."
  explanation: "The effective potential trick converts a 2D problem into a 1D one by using conservation of L to eliminate the angular degree of freedom. The price you pay is that the centrifugal term — representing the cost of rotating faster as you move inward — appears as an effective repulsion. The resulting 1D problem in U_eff(r) fully encodes the orbital behavior: bound vs unbound, circular vs elliptical, stable vs unstable, all readable from the shape of U_eff."
```

## Explainer

A **central force** is one that always points directly toward (or away from) a fixed center and whose magnitude depends only on the distance from that center: **F** = F(r) r̂. Gravity between two bodies and the Coulomb electrostatic force are both central forces. The critical consequence follows immediately from your knowledge of angular momentum: a central force exerts no torque about the center (because **r** × **F** = **r** × F(r)r̂ = 0), so angular momentum **L** = **r** × **p** is conserved throughout the motion. This single conservation law transforms a three-dimensional problem into a much simpler one.

Because **L** is constant in both magnitude and direction, the motion is confined to a fixed plane perpendicular to **L**. You now have a 2D problem instead of 3D. In **polar coordinates** (r, φ) within this plane — your prerequisite — the angular momentum conservation statement becomes L = μr²φ̇ = constant, where μ is the reduced mass. This tells you the angular velocity at every radial position. Now substitute this into the radial equation of motion, and something remarkable happens: all the angular momentum information can be packed into an **effective potential**, U_eff(r) = L²/(2μr²) + U(r), where U(r) is the real potential energy. The term L²/(2μr²) is the **centrifugal potential** — it acts like a repulsive barrier at small r, preventing the particle from collapsing to the origin if it has any angular momentum. The radial coordinate r then obeys exactly the equation of a 1D particle moving in U_eff: (1/2)μṙ² + U_eff(r) = E.

This reduction — from a 2D orbit problem to a 1D energy problem — is the central mathematical achievement of the central-force framework. Once you know U_eff(r), you can classify orbits by energy. If E < U_eff(r) at large r (the particle cannot escape to infinity), the orbit is **bound**: r oscillates between a minimum (periapsis) and a maximum (apoapsis). For a 1/r² attractive force (gravity), the effective potential has a single minimum, and the bound orbits are ellipses — Kepler's first law emerges directly. The special case E = U_eff_min is a circular orbit, where r stays constant and the particle traces a perfect circle. For E ≥ 0 (above the escape threshold), the orbit is unbound: a parabola (E = 0) or hyperbola (E > 0).

The shape of the orbit depends sensitively on the force law. For a 1/r² force, Bertrand's theorem guarantees that all bound orbits are closed ellipses — every orbit returns to its starting point. For nearly any other central force law, bound orbits are open (they precess, slowly rotating the axis of the ellipse rather than returning exactly). The anomalous precession of Mercury's perihelion — a small deviation from Newtonian 1/r² gravity — was one of the first confirmations of general relativity. The effective potential method is the tool that lets you analyze orbital shape, stability, and energy without solving the full differential equations explicitly, making it one of the most powerful techniques in classical mechanics.
