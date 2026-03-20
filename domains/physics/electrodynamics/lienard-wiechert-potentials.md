---
id: lienard-wiechert-potentials
title: Lienard-Wiechert Potentials
domain: physics
course: electrodynamics
prerequisites:
- id: retarded-potentials
  type: hard
- id: classical-mechanics
  type: soft
builds-toward:
- radiation-from-accelerated-charges
- synchrotron-radiation
tags:
- moving-charges
- retarded-fields
stage: advanced
status: draft
---

# Lienard-Wiechert Potentials

## Core Idea
Lienard-Wiechert potentials give exact potentials and fields of a point charge on arbitrary trajectory. They reveal a moving charge produces velocity fields (∝ 1/r²) and acceleration fields (∝ 1/r). The latter dominates at large distances and is responsible for radiation.

## Explainer

You already know that electromagnetic signals travel at c, and that **retarded potentials** encode this by saying the potential at position r at time t depends on where charges were at the earlier **retarded time** t_ret = t − |r − r(t_ret)|/c — the time when the signal that reaches you now was emitted. The **Lienard-Wiechert potentials** are retarded potentials applied to a point charge moving on a specific trajectory r_s(t). They give exact, closed-form expressions: V = (q/4πε₀) · 1/(κR) and A⃗ = (μ₀q/4π) · v⃗/(κR), where R is the distance from retarded position to field point, v⃗ is the velocity at retarded time, and κ = 1 − (v⃗·R̂)/c is a critical factor encoding the "headlight effect."

The factor κ in the denominator is not a small correction — it qualitatively changes the field structure. A charge moving toward you has κ < 1, so the potential is amplified; a charge moving away has κ > 1, suppressed. This **relativistic beaming** concentrates fields in the forward direction of a fast-moving charge, which is why synchrotron radiation is beamed sharply forward. Computing the actual E⃗ and B⃗ fields from these potentials (via the usual −∇V − ∂A⃗/∂t and ∇ × A⃗) reveals two distinct contributions of very different character.

The **velocity fields** (also called "bound fields") fall off as 1/r². They point along the retarded direction modified by the particle's motion, and they look like a distorted Coulomb field dragged along with the charge. Because they fall off as 1/r², the energy flux they carry (∝ E² ∝ 1/r⁴) integrates to zero over a large sphere — they carry no energy to infinity. A uniformly moving charge has only velocity fields: it does not radiate, consistent with the equivalence principle.

The **acceleration fields** (or "radiation fields") fall off as 1/r. They arise only when the charge is accelerating — a⃗ ≠ 0 at the retarded time — and they are proportional to a⃗ projected perpendicular to the observation direction. Because they fall off as 1/r, their energy flux ∝ 1/r² integrates over a large sphere to a finite, nonzero value: energy escapes to infinity. This is radiation. The Lienard-Wiechert fields are the exact classical solution from which Larmor's formula, synchrotron radiation, and all other classical radiation results can be derived by integration.
