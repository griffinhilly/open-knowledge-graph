---
id: planck-distribution-blackbody
title: Planck Distribution and Blackbody Radiation
domain: physics
course: statistical-mechanics
prerequisites:
- id: blackbody-radiation
  type: hard
- id: photon-model
  type: hard
builds-toward:
- photon-gas-thermodynamics
tags:
- blackbody
- photons
- thermal-radiation
stage: advanced
status: draft
---

# Planck Distribution and Blackbody Radiation

## Core Idea
Planck's law describes the spectral energy density of blackbody radiation: u_ν(ν,T) dν = (8πhν^3/c^3) dν / [exp(hν/kT)−1]. Integrating over all frequencies recovers the Stefan-Boltzmann law u(T) ∝ T^4. The Planck distribution arises from counting the partition function of a gas of photons in thermal equilibrium.

## Explainer

From the blackbody radiation problem you know the historical puzzle: classical physics (the Rayleigh-Jeans law) predicts that radiation intensity grows without bound as frequency increases — the **ultraviolet catastrophe** — because it treats each electromagnetic mode as having average energy kT regardless of frequency. Planck resolved this by quantizing the radiation field, and from the photon model you know that light comes in discrete quanta each carrying energy hν. The statistical mechanics of a photon gas is what turns these ingredients into a complete, correct formula.

A photon mode at frequency ν is a quantum harmonic oscillator that can be excited with 0, 1, 2, … photons. The key difference from classical particles: photons are bosons with no conservation law (you can have any number, and photons can be created and absorbed by the walls). The chemical potential μ = 0 for a photon gas. The mean number of photons in a mode at frequency ν is then the **Bose-Einstein distribution** with μ = 0: ⟨n⟩ = 1/(exp(hν/kT) − 1). Multiplying by hν gives the mean energy per mode: ⟨E⟩ = hν / [exp(hν/kT) − 1]. This replaces the classical kT: at high temperatures (kT ≫ hν), ⟨E⟩ → kT recovering the classical limit; at low temperatures (kT ≪ hν), ⟨E⟩ → hν exp(−hν/kT) → 0, exponentially suppressing high-frequency modes.

To get the full spectral density, multiply ⟨E⟩ by the number of modes per unit volume per unit frequency. In a 3D cavity, the mode density is 8πν²/c³ (accounting for two polarizations). This gives Planck's law: u_ν = (8πhν³/c³) / [exp(hν/kT) − 1]. The spectrum has a peak at ν_max ∝ T (**Wien's displacement law** — hotter objects peak at higher frequency, which is why iron glows red then white then blue as it heats). Integrating over all frequencies using the standard integral ∫₀^∞ x³/(eˣ−1)dx = π⁴/15 gives the total energy density u ∝ T⁴ — the **Stefan-Boltzmann law**, which you can now derive from first principles rather than treating as empirical.

The Planck distribution is the prototype for a broader class of results. The same Bose-Einstein factor with μ = 0 governs phonons (quantized lattice vibrations), which gives the Debye model of heat capacities. The factor 1/(exp(βε) − 1) for bosons versus 1/(exp(βε) + 1) for fermions (which you will encounter in the Fermi-Dirac distribution) are the two fundamental quantum statistics, replacing the classical Maxwell-Boltzmann e^{−βε}. Planck's original insight — that energy comes in discrete quanta — thus has consequences far beyond radiation, anchoring the entire framework of quantum statistical mechanics.


