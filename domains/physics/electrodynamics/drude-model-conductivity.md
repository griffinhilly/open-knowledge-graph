---
id: drude-model-conductivity
title: Drude Model of Conductivity
domain: physics
course: electrodynamics
prerequisites:
- id: electric-current-and-resistance
  type: hard
- id: oscillations-damping
  type: soft
builds-toward:
- conductivity-complex-dielectric
- em-waves-in-conductors
tags:
- conductivity
- free-electrons
- plasma-frequency
stage: advanced
status: draft
---

# Drude Model of Conductivity

## Core Idea
The Drude model treats free electrons in metals as experiencing a uniform friction force proportional to velocity. This yields a frequency-dependent conductivity σ(ω) with a characteristic plasma frequency ωₚ below which waves cannot propagate.

## How It's Best Learned
Derive the equation of motion for electrons, solve for velocity response to oscillating field, and identify the plasma frequency. Show how conductivity diverges at ω=0 for collisionless case.

## Explainer

You know from studying resistance and current that metals conduct electricity well because they contain free electrons that can move through the lattice. The **Drude model** (Paul Drude, 1900) puts a precise dynamical picture to this: treat the free electrons as classical point particles bouncing through a background of positive ions. Between collisions, electrons respond to the electric field. At each collision — occurring on average every time τ — an electron's momentum is randomized, effectively resetting it to zero drift velocity. This collision frequency γ = 1/τ acts like a velocity-proportional friction: the equation of motion for the average electron is m(dv/dt) = −eE − mγv.

At DC (ω = 0), this gives the **DC conductivity** σ₀ = ne²τ/m, where n is the electron density. This is the Drude result: higher electron density, longer collision time, or lighter electrons all increase conductivity. It correctly reproduces Ohm's law J = σE as an emergent relation from microscopic dynamics. For an AC electric field E = E₀e^(−iωt), the equation of motion has a steady-state solution v ∝ e^(−iωt), giving a **frequency-dependent conductivity** σ(ω) = σ₀/(1 − iωτ). At low frequencies (ωτ ≪ 1), σ ≈ σ₀ and the metal responds essentially as it does at DC. At high frequencies (ωτ ≫ 1), σ becomes purely imaginary — the response is inertial, not resistive.

The most striking consequence is the **plasma frequency** ωₚ = √(ne²/mε₀). This emerges when you write the dielectric function ε(ω) = 1 − ωₚ²/ω² (in the collisionless limit). When ε < 0 (for ω < ωₚ), the wave vector k becomes imaginary and electromagnetic waves cannot propagate — they are reflected or attenuated. When ε > 0 (for ω > ωₚ), waves propagate freely. This explains why metals are shiny and reflective at optical frequencies (below their plasma frequency) but become transparent to X-rays (far above it). The ionosphere's plasma frequency in the MHz range is why AM radio waves reflect off the upper atmosphere but higher-frequency signals (FM, GPS) pass through.

The Drude model's success is remarkable for its simplicity, but its failures are equally instructive. It predicts the wrong temperature dependence of conductivity, gets the heat capacity of metals wrong by a factor of ~100, and cannot explain semiconductors. These failures all point to the same root cause: electrons in metals are quantum objects obeying Fermi-Dirac statistics, not classical billiard balls. The Sommerfeld model (free electron gas with quantum statistics) fixes most of these issues while keeping the Drude spirit. Still, Drude's model captures the essential physics of optical response and plasma behavior with high-school-level mechanics, making it an indispensable first step.
