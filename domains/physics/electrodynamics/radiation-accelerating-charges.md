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

## Questions

```yaml
- question: "An electron travels at half the speed of light in a perfectly straight line through vacuum. Does it radiate electromagnetic energy?"
  type: multiple-choice
  options:
    - "Yes — any charged particle moving through vacuum radiates due to the Cherenkov effect"
    - "Yes — high-velocity charges always radiate because of their large kinetic energy"
    - "No — a charge in uniform motion (constant velocity, straight line) produces only bound Coulomb-like fields that carry no net energy to infinity"
    - "No — radiation only occurs at speeds exceeding the speed of light"
  answer: 2
  explanation: "Radiation requires acceleration. A charge at constant velocity produces fields that are purely electrostatic in the instantaneous rest frame. These Coulomb-like fields fall off as 1/r² and carry zero net energy flux through any distant sphere — they are bound fields accompanying the charge. The Larmor formula P ∝ a² confirms this: zero acceleration gives zero radiated power. Note: the Cherenkov effect (option A) occurs when a charge travels faster than light *in a medium*, not in vacuum, and arises from a different mechanism entirely."

- question: "Why does the 1/r falloff of radiation fields — rather than the 1/r² falloff of Coulomb fields — determine whether energy escapes to infinity?"
  type: multiple-choice
  options:
    - "1/r fields are stronger near the source, so they carry more total energy outward"
    - "Energy flux (Poynting vector) scales as |E|², so a 1/r field gives flux ∝ 1/r², which integrates to a constant over a sphere of area 4πr², giving nonzero power at any distance"
    - "1/r fields have lower frequency than 1/r² fields and therefore propagate further"
    - "The falloff rate is irrelevant; what matters is that radiation fields oscillate while Coulomb fields are static"
  answer: 1
  explanation: "The energy flux (Poynting vector magnitude) scales as |E|². A field that falls as 1/r gives flux ∝ 1/r². Integrated over a sphere of radius r (area 4πr²), this gives total power ∝ 4πr² · (1/r²) = constant — independent of r. Energy passes through every sphere at the same rate: it has truly escaped to infinity. For 1/r² Coulomb fields, flux ∝ 1/r⁴, which integrated over a sphere gives zero as r → ∞. The bound fields carry no net energy outward."

- question: "A uniformly charged sphere moving at constant velocity radiates electromagnetic energy because the charges within it undergo centripetal acceleration to maintain their relative positions."
  type: true-false
  answer: false
  explanation: "Charges within a rigidly moving sphere do not accelerate if the sphere moves at constant velocity in a straight line — every charge undergoes the same translational motion, and in the center-of-mass frame each is stationary. More fundamentally, uniform translational motion (constant velocity) produces no radiation regardless of the geometry. The Larmor formula P ∝ a² gives zero radiated power for zero acceleration. The misconception conflates 'rigid body motion' with 'individual charge acceleration.'"

- question: "The classical picture of an electron orbiting a nucleus fails because an orbiting electron is continuously accelerating and should therefore radiate energy, spiraling inward."
  type: true-false
  answer: true
  explanation: "Centripetal acceleration is real acceleration — the electron's direction changes continuously even if its speed is constant. By the Larmor formula P = q²a²/(6πε₀c³), any acceleration produces radiated power. For a classical orbiting electron, this power loss would cause it to spiral inward in a tiny fraction of a second. This 'ultraviolet catastrophe' for atomic stability was one of the central crises classical physics could not resolve, ultimately requiring quantum mechanics and the quantization of orbital angular momentum."

- question: "Explain why accelerating charges radiate but charges moving at constant velocity do not. What physically happens to the electric field lines when a charge is suddenly accelerated?"
  type: short-answer
  answer: "When a charge moves at constant velocity, its field lines rearrange smoothly and continuously, always appearing as the field of a charge at its current position. When a charge is suddenly accelerated, the field lines cannot rearrange instantaneously — information propagates at the speed of light. The 'old' Coulomb-field configuration persists at large distances while the 'new' configuration propagates outward from the charge. The mismatch creates a kink in the field lines that propagates outward as an electromagnetic wave — the radiation field. This 1/r kink carries energy independently of the source and persists at arbitrary distance, unlike the 1/r² bound Coulomb field."
  explanation: "The key concept is retardation: field rearrangement takes time, and when a charge accelerates, the field structure at large distances cannot keep up. This kink is permanent — it propagates outward forever — while the bound fields of a uniformly moving charge carry no energy to infinity. Every radiating antenna, synchrotron, and emitting atom exploits exactly this mechanism."
```

## Explainer

Consider what happens when a charge moves at constant velocity. From the Liénard-Wiechert potentials you have studied, the fields of a uniformly moving charge are those of a "Lorentz-boosted" Coulomb field — they fall off as 1/r² and carry no net energy to infinity. The energy in the fields is tightly bound to the charge, accompanying it as it moves. Now accelerate that charge. The field lines, which connect to the charge like rubber bands, cannot instantly rearrange — they are limited by the speed of light. This mismatch between where the field lines "want" to be and where they "actually" are at large distances creates a kink that propagates outward. That propagating kink is **electromagnetic radiation**.

The key mathematical signature is the 1/r falloff. The energy flux (Poynting vector) scales as |E|²; a 1/r field produces a flux proportional to 1/r², which integrated over a sphere of area 4πr² gives a constant — independent of r. This means energy escapes to infinity. The Coulomb 1/r² field, when squared, gives flux ∝ 1/r⁴, which integrated over a sphere goes to zero: bound fields carry no net energy to infinity. **Radiation fields are the 1/r terms in the Liénard-Wiechert expressions** — they survive arbitrarily far from the source, while bound fields vanish. Every antenna exploits this: the accelerating electrons in the antenna wire create 1/r fields that propagate to your radio or phone.

The total radiated power is given by the **Larmor formula**: P = q²a²/(6πε₀c³) in SI units. The dependence on a² means power goes up rapidly with acceleration, and the dependence on 1/c³ makes radiation a relativistic effect — in the non-relativistic limit, it's small. The angular distribution is not isotropic: radiation is strongest perpendicular to the acceleration and zero along the acceleration axis, following a sin²θ pattern (donut-shaped, with the donut axis along the acceleration direction). This explains why antennas designed for omnidirectional coverage orient their driven element vertically — the radiation is strongest in the horizontal plane.

The physical consequences are profound. An electron in a circular orbit — as in the Bohr model — is constantly accelerating centripetally, so it should continuously radiate and spiral inward. This "ultraviolet catastrophe" of classical atomic physics was one of the crises quantum mechanics resolved by quantizing orbital angular momentum. In modern particle physics, synchrotron radiation from electrons in circular accelerators (unavoidable due to centripetal acceleration) both limits achievable energies and creates a valuable X-ray light source used in material science. In astrophysics, synchrotron emission from relativistic electrons spiraling in cosmic magnetic fields produces the characteristic radio emission of pulsars and active galactic nuclei. The principle — **accelerating charges radiate** — is one of the most consequential in all of physics.
