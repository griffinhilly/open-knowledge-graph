---
id: larmor-formula
title: Larmor Formula for Radiated Power
domain: physics
course: electrodynamics
prerequisites:
- id: radiation-from-accelerated-charges
  type: hard
- id: poynting-vector-and-energy-flux
  type: soft
builds-toward:
- electric-dipole-radiation
- synchrotron-radiation
tags:
- power
- larmor
- acceleration
stage: advanced
status: draft
---

# Larmor Formula for Radiated Power

## Core Idea
The Larmor formula P = (q²a²)/(6πε₀c³) gives power radiated by a non-relativistic accelerated point charge. Maximum power radiates perpendicular to acceleration; no power along the acceleration direction. This fundamental result connects acceleration to energy loss by radiation.

## Questions

```yaml
- question: "According to the Larmor formula, what happens to the radiated power if the charge's acceleration is doubled while everything else stays the same?"
  type: multiple-choice
  options:
    - "The power doubles"
    - "The power increases by a factor of 4"
    - "The power increases by a factor of 8"
    - "The power stays the same — only the frequency of radiation changes"
  answer: 1
  explanation: "The Larmor formula is P = q²a²/(6πε₀c³) — power is proportional to acceleration squared. Doubling a gives a factor of 2² = 4 increase in power. This quadratic dependence on acceleration is not arbitrary: the radiation field itself is proportional to a, so the energy flux (Poynting vector ∝ E²) is proportional to a², and integrating over a sphere gives the same a² dependence."

- question: "In which direction does an accelerating point charge radiate the most power?"
  type: multiple-choice
  options:
    - "Along the direction of acceleration — maximum emission in the direction of motion"
    - "Perpendicular to the acceleration — the radiation pattern peaks at 90° from the acceleration axis"
    - "Uniformly in all directions — the Larmor formula gives total power, not directional"
    - "Opposite to the direction of acceleration — the charge pushes radiation away from itself"
  answer: 1
  explanation: "The angular distribution of Larmor radiation goes as sin²θ, where θ is measured from the acceleration axis. This means zero power is radiated along the acceleration direction (θ = 0° or 180°) and maximum power is radiated perpendicular to it (θ = 90°). The pattern is shaped like a donut with the acceleration axis as the central hole — this is the characteristic dipole radiation pattern."

- question: "A charged particle moving at constant velocity in a straight line radiates electromagnetic energy according to the Larmor formula."
  type: true-false
  answer: false
  explanation: "The Larmor formula is P = q²a²/(6πε₀c³) — power depends on acceleration squared. A charge at constant velocity has zero acceleration, so P = 0: it emits no radiation. Radiation requires acceleration. This is a crucial distinction: a moving charge creates electric and magnetic fields that propagate with it (the 'velocity fields' or 'Coulomb fields'), but these fields do not carry energy away to infinity — only the radiation fields, which require acceleration, do that."

- question: "The Larmor formula predicts that an electron in a classical circular orbit around a nucleus should continuously lose energy, implying atoms cannot be stable in classical electrodynamics."
  type: true-false
  answer: true
  explanation: "A circular orbit requires centripetal acceleration directed inward. The Larmor formula gives P = q²a²/(6πε₀c³) > 0 for any nonzero centripetal acceleration. This means the electron continuously radiates energy, losing it to electromagnetic radiation. As energy decreases, the orbital radius decreases and the centripetal acceleration increases, accelerating the radiation and causing a runaway spiral inward. Classical electrodynamics predicts atoms collapse in nanoseconds — this 'classical catastrophe' was a key motivation for quantum mechanics."

- question: "Why do circular particle accelerators face a fundamental energy-loss challenge from the Larmor formula that linear accelerators avoid?"
  type: short-answer
  answer: "In a circular accelerator, particles move in a curved path, which requires centripetal acceleration directed toward the center of curvature. Even if particle speed is constant, centripetal acceleration is nonzero, so the Larmor formula gives P > 0 — the particles continuously radiate (synchrotron radiation) and lose energy. A linear accelerator accelerates particles along a straight line, so the acceleration is parallel to velocity and there is no centripetal component persisting throughout the path; once the accelerating section ends, acceleration stops and radiation ceases."
  explanation: "Synchrotron radiation scales as a⁴ in the relativistic generalization of the Larmor formula, making it an increasingly severe problem at high energies. This is why high-energy electron accelerators (like LEP at CERN) eventually hit a wall where all the energy pumped in goes straight out as synchrotron radiation. The Large Hadron Collider uses protons instead of electrons precisely because protons are ~1800× heavier, giving far less centripetal acceleration for the same momentum, and hence far less synchrotron radiation."
```

## Explainer

From your study of radiation from accelerated charges, you know that the radiation field falls off as 1/r — unlike the near (velocity) field which falls off as 1/r². This 1/r behavior means the energy flux (Poynting vector) falls off as 1/r², and when integrated over a sphere of radius r, the total power flowing outward is constant — the same at every r, meaning energy genuinely escapes to infinity. The **Larmor formula** puts a number on exactly how much power escapes: P = q²a²/(6πε₀c³). It depends on the charge squared, the acceleration squared, and three fundamental constants.

To see why acceleration squared appears, recall that the radiation field is proportional to acceleration (E_rad ∝ a/r), so the Poynting vector goes as a²/r², and integrating over the sphere gives a² with no r-dependence — consistent with power flowing away. The three constants encode the electromagnetic structure of space: ε₀ tells you how "difficult" it is for fields to exist in vacuum, while c³ reflects the fact that radiation involves the field restructuring itself at the speed of light. Larger charge radiates more (it couples more strongly to the EM field); higher acceleration radiates more (it disturbs the field more violently); weaker constants mean easier propagation.

The **radiation pattern** — which direction the power flows — is not uniform. No power is radiated along the direction of acceleration; maximum power is radiated perpendicular to it. The angular distribution goes as sin²θ, where θ is measured from the acceleration axis, giving a donut-shaped pattern with the acceleration axis as the hole. This is the characteristic signature of electric dipole radiation: you can think of the accelerated charge as an oscillating electric dipole, and dipoles don't radiate along their axis.

The practical consequences of the Larmor formula are everywhere. In classical atomic physics, an electron orbiting a nucleus is centripetally accelerated and should therefore radiate, losing energy and spiraling inward — the "classical collapse" that demanded quantum mechanics. In particle accelerators, electrons radiated via this mechanism (called **synchrotron radiation**) lose significant energy per revolution, limiting the energy achievable in circular machines. In radio antennas, it's the acceleration of electrons back and forth in the antenna wire that produces the outgoing EM wave. The Larmor formula gives the engineering relationship between antenna current (and hence charge acceleration) and radiated power. The formula's simplicity — two fundamental constants, charge, and acceleration — belies its reach across atomic, accelerator, and antenna physics.
