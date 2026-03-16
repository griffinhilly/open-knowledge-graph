---
id: motional-emf
title: Motional EMF and Flux Change
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: faraday-induced-emf
  type: hard
builds-toward:
- self-inductance
tags:
- motional-emf
- flux
- generator
stage: formal-systems
status: draft
---

# Motional EMF and Flux Change

## Core Idea
When a conductor moves through a magnetic field, charge carriers experience Lorentz force F⃗ = q(v⃗ × B⃗), separating charges and creating EMF. For a straight conductor of length L moving perpendicular to field B at speed v: ε = BLv. This can be understood as Faraday's law applied to the changing loop area: ε = −dΦ/dt = BLv. Motional EMF is the basis for electromagnetic generators.

## Explainer

From Faraday's law, you know that a changing magnetic flux through a loop induces an EMF. But flux can change in two ways: either the magnetic field strength changes, or the area of the loop changes. **Motional EMF** is the second case — the flux changes because part of the loop is physically moving, sweeping out new area in the field.

The most instructive starting point is not the loop, but a single conducting rod of length L sliding along rails in a uniform magnetic field B⃗ pointing out of the page. The rod moves to the right at speed v. Each free electron in the rod is a charge carrier moving with the rod, so it has velocity v⃗ to the right. The Lorentz force on a positive carrier is F⃗ = qv⃗ × B⃗, which by the right-hand rule points upward along the rod. Positive charges accumulate at the top, negative at the bottom, until the electric field from the separated charges exactly balances the magnetic force. The resulting potential difference — the **EMF** — is ε = BLv, found by integrating the force per unit charge along the rod length.

Now zoom out and see the same situation through Faraday's law. The rod and its two rails form a rectangular loop. As the rod moves rightward by dx in time dt, the loop area increases by dA = L·dx. The rate of change of flux is dΦ/dt = B · dA/dt = B · L · v. Faraday's law gives ε = dΦ/dt = BLv — the same answer. This agreement is not a coincidence: the two perspectives are equivalent descriptions of the same physics. The Lorentz force on moving charges is what Faraday's law "knows" when the conductor is moving.

This principle is the foundation of **electromagnetic generators**. In a real generator, a rectangular coil rotates in a magnetic field. As it rotates, the angle between B⃗ and the area vector changes sinusoidally, so Φ = BA cos(ωt) and ε = BAω sin(ωt) — a sinusoidal AC voltage. Every power plant on Earth, regardless of whether the input energy comes from steam turbines, water, or wind, converts that energy into electricity by using this same motional EMF: mechanical rotation sweeps conducting loops through magnetic fields, turning kinetic energy into an electrical potential difference.
