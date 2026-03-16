---
id: radiation-accelerating-charges
title: Radiation from Accelerating Charges
domain: physics
course: electrodynamics
prerequisites:
- id: lienard-wiechert-potentials
  type: hard
- id: poynting-vector-energy-flow
  type: soft
builds-toward:
- larmor-formula
- electric-dipole-radiation
tags:
- radiation
- accelerating-charges
- energy-loss
stage: advanced
status: draft
---

# Radiation from Accelerating Charges

## Core Idea
Accelerating charges radiate electromagnetic waves that carry energy and momentum away from the charge. The radiated fields depend on the acceleration and fall off as 1/r (not 1/r² like Coulomb fields), indicating energy transport. This radiation causes energy loss and is the mechanism behind antenna operation, atomic transitions, and synchrotron emission.

## Explainer

Consider what happens when a charge moves at constant velocity. From the Liénard-Wiechert potentials you have studied, the fields of a uniformly moving charge are those of a "Lorentz-boosted" Coulomb field — they fall off as 1/r² and carry no net energy to infinity. The energy in the fields is tightly bound to the charge, accompanying it as it moves. Now accelerate that charge. The field lines, which connect to the charge like rubber bands, cannot instantly rearrange — they are limited by the speed of light. This mismatch between where the field lines "want" to be and where they "actually" are at large distances creates a kink that propagates outward. That propagating kink is **electromagnetic radiation**.

The key mathematical signature is the 1/r falloff. The energy flux (Poynting vector) scales as |E|²; a 1/r field produces a flux proportional to 1/r², which integrated over a sphere of area 4πr² gives a constant — independent of r. This means energy escapes to infinity. The Coulomb 1/r² field, when squared, gives flux ∝ 1/r⁴, which integrated over a sphere goes to zero: bound fields carry no net energy to infinity. **Radiation fields are the 1/r terms in the Liénard-Wiechert expressions** — they survive arbitrarily far from the source, while bound fields vanish. Every antenna exploits this: the accelerating electrons in the antenna wire create 1/r fields that propagate to your radio or phone.

The total radiated power is given by the **Larmor formula**: P = q²a²/(6πε₀c³) in SI units. The dependence on a² means power goes up rapidly with acceleration, and the dependence on 1/c³ makes radiation a relativistic effect — in the non-relativistic limit, it's small. The angular distribution is not isotropic: radiation is strongest perpendicular to the acceleration and zero along the acceleration axis, following a sin²θ pattern (donut-shaped, with the donut axis along the acceleration direction). This explains why antennas designed for omnidirectional coverage orient their driven element vertically — the radiation is strongest in the horizontal plane.

The physical consequences are profound. An electron in a circular orbit — as in the Bohr model — is constantly accelerating centripetally, so it should continuously radiate and spiral inward. This "ultraviolet catastrophe" of classical atomic physics was one of the crises quantum mechanics resolved by quantizing orbital angular momentum. In modern particle physics, synchrotron radiation from electrons in circular accelerators (unavoidable due to centripetal acceleration) both limits achievable energies and creates a valuable X-ray light source used in material science. In astrophysics, synchrotron emission from relativistic electrons spiraling in cosmic magnetic fields produces the characteristic radio emission of pulsars and active galactic nuclei. The principle — **accelerating charges radiate** — is one of the most consequential in all of physics.
