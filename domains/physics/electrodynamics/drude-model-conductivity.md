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
stage: expert
status: draft
---

# Drude Model of Conductivity

## Core Idea
The Drude model treats free electrons in metals as experiencing a uniform friction force proportional to velocity. This yields a frequency-dependent conductivity σ(ω) with a characteristic plasma frequency ωₚ below which waves cannot propagate.

## How It's Best Learned
Derive the equation of motion for electrons, solve for velocity response to oscillating field, and identify the plasma frequency. Show how conductivity diverges at ω=0 for collisionless case.

## Questions

```yaml
- question: "Visible light reflects off silver, but X-rays pass through it. The Drude model explains this because:"
  type: multiple-choice
  options:
    - "Silver absorbs visible light photons but is too thin to absorb the higher-energy X-ray photons"
    - "Visible light frequencies are below silver's plasma frequency (ε < 0, waves cannot propagate), while X-ray frequencies are above it (ε > 0, waves propagate freely)"
    - "X-rays carry more energy per photon and therefore penetrate any material more deeply"
    - "Silver electrons resonate with X-ray frequencies, creating constructive interference that allows transmission"
  answer: 1
  explanation: "The Drude model gives a dielectric function ε(ω) = 1 − ωₚ²/ω² in the collisionless limit. When ω < ωₚ (visible light for most metals), ε < 0, the wave vector k becomes imaginary, and electromagnetic waves cannot propagate — they are reflected or exponentially attenuated within a skin depth. When ω > ωₚ (X-rays), ε > 0, the wave vector is real, and waves propagate freely. This is why metals are shiny mirrors at optical frequencies but become transparent to high-frequency radiation. The physical cause is not energy absorption but the inability of the electron gas to respond fast enough at high frequencies."

- question: "AM radio waves (MHz range) reflect off the ionosphere, while FM radio and GPS signals (hundreds of MHz and GHz) pass through. Within the Drude model framework, this is because:"
  type: multiple-choice
  options:
    - "The ionosphere is too thin a plasma to reflect higher-frequency signals"
    - "AM signals are below the ionosphere's plasma frequency (ω < ωₚ), so they are reflected; FM and GPS are above it (ω > ωₚ), so they pass through"
    - "The ionosphere resonates at AM frequencies, selectively reflecting those signals"
    - "Higher-frequency signals are more directive and therefore avoid the ionosphere by traveling in a tighter beam"
  answer: 1
  explanation: "The ionosphere is a partially ionized plasma with a characteristic plasma frequency in the tens of MHz range. AM radio (0.5–1.7 MHz) is well below this threshold: ε < 0, waves cannot propagate, and AM signals reflect back to Earth — enabling long-range AM reception. FM radio (88–108 MHz) and GPS (∼1.2–1.6 GHz) are above the ionospheric plasma frequency: ε > 0, and these signals pass through to satellites and receivers. This is why FM and GPS require line-of-sight (or satellite relay) while AM can bounce around the globe — a direct consequence of the plasma frequency threshold."

- question: "The Drude model correctly derives Ohm's law (J = σE) as an emergent relation from the microscopic equation of motion of free electrons."
  type: true-false
  answer: true
  explanation: "Starting from the equation of motion m(dv/dt) = −eE − mγv (Newton's law with a friction term representing collisions), the steady-state DC solution (dv/dt = 0) gives v = −eE/(mγ) = −eτE/m. The current density J = −nev = (ne²τ/m)E = σ₀E, which is exactly Ohm's law J = σE with the DC conductivity σ₀ = ne²τ/m. Ohm's law is not assumed — it emerges from the balance between the electric force and the collision friction. This is one of the Drude model's genuine successes: it provides a microscopic basis for what had previously been a purely empirical law."

- question: "The Drude model fails to explain the properties of real metals because it incorrectly assumes that electrons are present and can move freely through the metal lattice."
  type: true-false
  answer: false
  explanation: "The presence of free conduction electrons is correct — this is indeed why metals conduct. The Drude model fails for a different reason: it treats electrons as classical particles obeying Maxwell-Boltzmann statistics, when in reality electrons are quantum fermions obeying Fermi-Dirac statistics. This incorrect statistics leads to a predicted electronic heat capacity roughly 100 times too large, wrong temperature dependence of resistivity, and inability to explain semiconductors (where band gaps prevent classical treatment). The Sommerfeld model keeps the free electron picture but applies correct quantum statistics, fixing most failures while preserving Drude's correct insights about optical response."

- question: "Explain what happens to electromagnetic wave propagation in a metal when the wave frequency is below the plasma frequency ωₚ, and why this explains metallic reflectivity at optical frequencies."
  type: short-answer
  answer: "When ω < ωₚ, the dielectric function ε(ω) = 1 − ωₚ²/ω² is negative. A negative ε means the wave vector k = (ω/c)√ε becomes imaginary. An imaginary wave vector means the wave does not oscillate spatially — instead, it decays exponentially with depth into the metal (within a skin depth). The wave cannot propagate and is instead reflected at the surface. At visible optical frequencies, metals like silver have ωₚ above the visible range, so ε < 0 for all visible light frequencies, and the metal reflects. Above ωₚ (into X-ray frequencies), ε > 0, k is real, and waves propagate — hence transparency."
  explanation: "The physical picture is that below ωₚ, the free electrons can respond to the oscillating field fast enough to screen it — they collectively oscillate (plasmons) and re-radiate, producing reflection. Above ωₚ, the electrons cannot keep up with the rapidly oscillating field; the response becomes negligible and the wave propagates as in free space. The plasma frequency is thus the crossover between metallic (reflective) and dielectric (transparent) behavior — a directly measurable property that determines a metal's optical color and applications in photonics."
```

## Explainer

You know from studying resistance and current that metals conduct electricity well because they contain free electrons that can move through the lattice. The **Drude model** (Paul Drude, 1900) puts a precise dynamical picture to this: treat the free electrons as classical point particles bouncing through a background of positive ions. Between collisions, electrons respond to the electric field. At each collision — occurring on average every time τ — an electron's momentum is randomized, effectively resetting it to zero drift velocity. This collision frequency γ = 1/τ acts like a velocity-proportional friction: the equation of motion for the average electron is m(dv/dt) = −eE − mγv.

At DC (ω = 0), this gives the **DC conductivity** σ₀ = ne²τ/m, where n is the electron density. This is the Drude result: higher electron density, longer collision time, or lighter electrons all increase conductivity. It correctly reproduces Ohm's law J = σE as an emergent relation from microscopic dynamics. For an AC electric field E = E₀e^(−iωt), the equation of motion has a steady-state solution v ∝ e^(−iωt), giving a **frequency-dependent conductivity** σ(ω) = σ₀/(1 − iωτ). At low frequencies (ωτ ≪ 1), σ ≈ σ₀ and the metal responds essentially as it does at DC. At high frequencies (ωτ ≫ 1), σ becomes purely imaginary — the response is inertial, not resistive.

The most striking consequence is the **plasma frequency** ωₚ = √(ne²/mε₀). This emerges when you write the dielectric function ε(ω) = 1 − ωₚ²/ω² (in the collisionless limit). When ε < 0 (for ω < ωₚ), the wave vector k becomes imaginary and electromagnetic waves cannot propagate — they are reflected or attenuated. When ε > 0 (for ω > ωₚ), waves propagate freely. This explains why metals are shiny and reflective at optical frequencies (below their plasma frequency) but become transparent to X-rays (far above it). The ionosphere's plasma frequency in the MHz range is why AM radio waves reflect off the upper atmosphere but higher-frequency signals (FM, GPS) pass through.

The Drude model's success is remarkable for its simplicity, but its failures are equally instructive. It predicts the wrong temperature dependence of conductivity, gets the heat capacity of metals wrong by a factor of ~100, and cannot explain semiconductors. These failures all point to the same root cause: electrons in metals are quantum objects obeying Fermi-Dirac statistics, not classical billiard balls. The Sommerfeld model (free electron gas with quantum statistics) fixes most of these issues while keeping the Drude spirit. Still, Drude's model captures the essential physics of optical response and plasma behavior with high-school-level mechanics, making it an indispensable first step.
