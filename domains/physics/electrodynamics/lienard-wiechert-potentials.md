---
id: lienard-wiechert-potentials
title: Lienard-Wiechert Potentials
domain: physics
course: electrodynamics
prerequisites:
- id: retarded-potentials
  type: hard
- id: newtons-second-law
  type: soft
builds-toward:
- radiation-from-accelerated-charges
- synchrotron-radiation
tags:
- moving-charges
- retarded-fields
stage: expert
status: validated
---

# Lienard-Wiechert Potentials

## Core Idea
Lienard-Wiechert potentials give exact potentials and fields of a point charge on arbitrary trajectory. They reveal a moving charge produces velocity fields (∝ 1/r²) and acceleration fields (∝ 1/r). The latter dominates at large distances and is responsible for radiation.

## Questions

```yaml
- question: "A proton moves at half the speed of light in a perfectly straight line at constant velocity. What electromagnetic radiation does it emit?"
  type: multiple-choice
  options:
    - "It emits radiation because the velocity fields it produces carry energy outward"
    - "It emits radiation because relativistic beaming concentrates its fields"
    - "It emits no radiation — constant-velocity motion produces only velocity fields, which carry no energy to infinity"
    - "It emits radiation because κ ≠ 1 for relativistic motion"
  answer: 2
  explanation: "A charge in uniform motion has only velocity fields (∝ 1/r²). Their energy flux falls off as 1/r⁴, which integrates to zero over any large sphere — no energy escapes to infinity. Radiation requires acceleration (a⃗ ≠ 0 at the retarded time). κ ≠ 1 for relativistic motion affects the field's angular distribution but does not create radiation; it is a feature of the velocity (bound) fields only."

- question: "The Lienard-Wiechert fields of an accelerating charge contain two components. Which has the slower spatial decay, and what is its physical significance?"
  type: multiple-choice
  options:
    - "The velocity field (∝ 1/r²) — it is responsible for radiation because it persists at large distances"
    - "The acceleration field (∝ 1/r) — it carries energy to infinity and constitutes electromagnetic radiation"
    - "Both components decay at the same rate; the distinction is only in their angular dependence"
    - "The acceleration field (∝ 1/r) — it accelerates nearby charges but carries no energy"
  answer: 1
  explanation: "The acceleration field falls off as 1/r, so its energy flux (∝ E² ∝ 1/r²) integrates to a finite nonzero value over a large sphere — energy escapes to infinity. This is radiation. The velocity field falls off as 1/r², giving energy flux ∝ 1/r⁴, which integrates to zero: no energy is carried to infinity regardless of how fast the charge moves."

- question: "A charge undergoing acceleration has an acceleration field proportional to the component of acceleration perpendicular to the observation direction."
  type: true-false
  answer: true
  explanation: "The radiation (acceleration) field is proportional to the component of a⃗ transverse to the retarded direction R̂. Acceleration along the line of sight to the observer produces no radiation in that direction — this is why a linearly oscillating charge radiates most strongly at 90° to its axis and nothing along its axis, consistent with Larmor's formula and classical antenna theory."

- question: "The κ = 1 − (v⃗·R̂)/c factor in the Lienard-Wiechert potentials primarily determines whether a charge radiates."
  type: true-false
  answer: false
  explanation: "κ appears in the denominator of both the scalar and vector potentials and controls relativistic beaming — it amplifies the fields of a charge moving toward you (κ < 1) and suppresses fields from a charge moving away (κ > 1). This is a property of the velocity (bound) fields. Radiation — whether it occurs at all — is determined solely by whether the charge is accelerating (a⃗ ≠ 0 at the retarded time), not by the value of κ."

- question: "Why does a uniformly moving charge not radiate, even though it produces electromagnetic fields that vary in time as it passes an observer?"
  type: short-answer
  answer: "Radiation requires acceleration. A uniformly moving charge produces only velocity (bound) fields that fall off as 1/r². Their energy flux falls off as 1/r⁴, integrating to zero over a distant sphere, so no net energy escapes to infinity. Radiation fields (∝ 1/r, energy flux ∝ 1/r²) appear only when acceleration is nonzero at the retarded time. This is consistent with the equivalence principle: an observer in free fall cannot detect radiation from an inertially moving charge."
  explanation: "The key is the 1/r versus 1/r² distinction. Fields that fall off faster than 1/r cannot deliver finite power flux through a large sphere (power ~ (1/r^n)² × r² → 0 if n > 1). Radiation is defined precisely as the component of the field that carries energy to infinity, which requires exactly the 1/r falloff that only acceleration produces."
```

## Explainer

You already know that electromagnetic signals travel at c, and that **retarded potentials** encode this by saying the potential at position r at time t depends on where charges were at the earlier **retarded time** t_ret = t − |r − r(t_ret)|/c — the time when the signal that reaches you now was emitted. The **Lienard-Wiechert potentials** are retarded potentials applied to a point charge moving on a specific trajectory r_s(t). They give exact, closed-form expressions: V = (q/4πε₀) · 1/(κR) and A⃗ = (μ₀q/4π) · v⃗/(κR), where R is the distance from retarded position to field point, v⃗ is the velocity at retarded time, and κ = 1 − (v⃗·R̂)/c is a critical factor encoding the "headlight effect."

The factor κ in the denominator is not a small correction — it qualitatively changes the field structure. A charge moving toward you has κ < 1, so the potential is amplified; a charge moving away has κ > 1, suppressed. This **relativistic beaming** concentrates fields in the forward direction of a fast-moving charge, which is why synchrotron radiation is beamed sharply forward. Computing the actual E⃗ and B⃗ fields from these potentials (via the usual −∇V − ∂A⃗/∂t and ∇ × A⃗) reveals two distinct contributions of very different character.

The **velocity fields** (also called "bound fields") fall off as 1/r². They point along the retarded direction modified by the particle's motion, and they look like a distorted Coulomb field dragged along with the charge. Because they fall off as 1/r², the energy flux they carry (∝ E² ∝ 1/r⁴) integrates to zero over a large sphere — they carry no energy to infinity. A uniformly moving charge has only velocity fields: it does not radiate, consistent with the equivalence principle.

The **acceleration fields** (or "radiation fields") fall off as 1/r. They arise only when the charge is accelerating — a⃗ ≠ 0 at the retarded time — and they are proportional to a⃗ projected perpendicular to the observation direction. Because they fall off as 1/r, their energy flux ∝ 1/r² integrates over a large sphere to a finite, nonzero value: energy escapes to infinity. This is radiation. The Lienard-Wiechert fields are the exact classical solution from which Larmor's formula, synchrotron radiation, and all other classical radiation results can be derived by integration.
