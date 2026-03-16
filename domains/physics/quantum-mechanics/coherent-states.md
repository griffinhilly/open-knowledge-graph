---
id: coherent-states
title: Coherent States
domain: physics
course: quantum-mechanics
prerequisites:
- id: harmonic-oscillator-quantum
  type: hard
builds-toward:
- path-integral-formulation
tags:
- oscillator
- states
- minimum-uncertainty
stage: abstract-reasoning
status: draft
---

# Coherent States

## Core Idea
Coherent states |α⟩ are eigenstates of the lowering operator. They saturate the uncertainty principle (minimum-uncertainty states), exhibit classical-like behavior with oscillating expectation values, and naturally appear in quantum optics.

## Explainer

From your study of the quantum harmonic oscillator, you know that the energy eigenstates |n⟩ form a complete basis and that the ladder operators â and â† step between them: â|n⟩ = √n |n−1⟩. The energy eigenstates have definite energy but wildly oscillating position and momentum uncertainties — they are as far from classical oscillation as a quantum state can be. Coherent states take a different approach: instead of demanding definite energy, they demand definite complex amplitude. A **coherent state** |α⟩ is defined as an eigenstate of the lowering operator, â|α⟩ = α|α⟩, where α is any complex number. This deceptively simple definition has far-reaching consequences.

The most striking property of coherent states is that their expectation values behave exactly like a classical oscillator. If you compute ⟨x̂⟩ and ⟨p̂⟩ for a coherent state |α(t)⟩, you find they oscillate sinusoidally at frequency ω — exactly the classical trajectory. The quantum state is following the classical path through phase space. This is what "classical-like" means: not that uncertainty disappears, but that the wave packet's center moves along the classical orbit without spreading. The uncertainties in position and momentum remain constant at their minimum values Δx = Δp = √(ℏ/2mω), so the wave packet glides around the potential well maintaining its shape forever.

Why do coherent states saturate the uncertainty principle? Recall that the Heisenberg relation ΔxΔp ≥ ℏ/2 is a lower bound. Equality holds only for Gaussian wave packets whose position and momentum spreads are related in a specific way. Coherent states are precisely such **minimum-uncertainty states** — their position-space wavefunctions are Gaussians centered on the classical trajectory. Energy eigenstates are also minimum-uncertainty states (the ground state |0⟩ is in fact the coherent state with α = 0), but excited eigenstates |n⟩ are not — they have larger ΔxΔp than the minimum. Coherent states generalize the ground state's Gaussian shape to all classical amplitudes.

To find the expansion of |α⟩ in the energy basis, you can apply â|α⟩ = α|α⟩ directly. The result is |α⟩ = e^{−|α|²/2} Σ_n (αⁿ/√n!) |n⟩ — a Poisson-weighted superposition of all energy eigenstates. The probability of finding energy E_n = ℏω(n + 1/2) is P(n) = e^{−|α|²} |α|^{2n}/n!, a Poisson distribution with mean n̄ = |α|². This Poisson photon statistics is the signature of **coherent light** — laser output. When |α|² ≫ 1, the Poisson distribution becomes sharply peaked relative to its mean, so coherent states of large amplitude are nearly classical: well-defined intensity with small relative fluctuations, just as you observe from a laser pointer.
