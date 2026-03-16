---
id: stability-of-circular-orbits
title: Stability of Circular Orbits
domain: physics
course: classical-mechanics
prerequisites:
- id: orbital-elements-and-trajectories
  type: hard
- id: circular-motion-dynamics
  type: hard
tags:
- orbits
- stability
- gravitation
- dynamics
stage: formal-systems
status: draft
---

# Stability of Circular Orbits

## Core Idea
Circular orbits in a 1/r gravitational potential are stable: small radial or tangential perturbations lead to slightly elliptical orbits that remain bound, not runaway trajectories. The effective potential U_eff(r) = L²/(2μr²) − G M μ / r has a minimum at the stable circular orbit radius. This stability is specific to the 1/r force law; other force laws (e.g., f ∝ r) can be unstable.

## Explainer

A **circular orbit** is the simplest type of bound orbit: the radius stays constant, and the orbiting body traces a perfect circle around the central mass. It exists at the specific radius r₀ where the net radial acceleration is exactly zero — where gravitational attraction perfectly balances the centrifugal effect of circular motion. The deeper question is whether this is a **stable equilibrium**: if you slightly perturb the orbit — a small rocket burn, a passing body's tug — does the orbit remain nearly circular, or does it spiral inward or outward to disaster?

From your study of **circular motion dynamics** and **orbital elements**, you know the conditions for circular motion and the geometry of orbits. The effective potential framework connects both. Recall that in the central-force treatment, radial motion obeys the same energy equation as a 1D particle in U_eff(r) = L²/(2μr²) − GMμ/r. The circular orbit corresponds to the **minimum** of U_eff — the particle sits at the bottom of a potential energy bowl. This minimum is why circular orbits in gravity are stable: U_eff has a true minimum, not a maximum or inflection point, so a small perturbation in r causes U_eff to increase, providing a restoring force that pushes r back toward r₀. The orbit rocks gently around the circular radius rather than departing from it.

To make this quantitative, expand U_eff around r₀. At the minimum, dU_eff/dr = 0 (this is the circular orbit condition), and d²U_eff/dr² > 0 (this is the stability condition — a positive second derivative means the bottom of the bowl is concave up). The **radial oscillation frequency** ω_r = √(d²U_eff/dr² / μ), evaluated at r₀, describes how fast the radius oscillates around r₀ after a perturbation. For a 1/r² gravitational force, this radial frequency equals the orbital angular frequency: ω_r = ω_orbit. This exact equality is the reason bound gravitational orbits are **closed ellipses** — the radial oscillation completes one cycle in exactly the same time as one full orbit, so the orbit traces the same path repeatedly. This is a special, non-generic property of the 1/r² force law (and also of the harmonic oscillator potential).

For other force laws, the ratio ω_r / ω_orbit need not equal one, and bound orbits **precess** — the axis of the approximately elliptical orbit slowly rotates over many orbits, tracing a rosette pattern rather than a closed curve. This is not a sign of instability; the orbit can still be stable while precessing. True **orbital instability** occurs when the effective potential has no minimum — only a maximum or no turning point at all — meaning that any perturbation causes runaway departure. Some force laws (with n > 2, where F ∝ 1/rⁿ) produce this behavior, making stable circular orbits impossible. The stability of planetary orbits in our solar system is therefore not automatic; it depends specifically on the 1/r² character of Newtonian gravity, which gives U_eff a well-defined minimum and ensures that the planets' slightly elliptical paths remain bound for billions of years.
