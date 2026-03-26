---
id: coherent-states
title: Coherent States
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-harmonic-oscillator
  type: hard
- id: pure-and-mixed-states
  type: soft
builds-toward:
- path-integral-formulation
tags:
- oscillator
- states
- minimum-uncertainty
stage: advanced
status: validated
---
# Coherent States

## Core Idea
Coherent states |α⟩ are eigenstates of the lowering operator. They saturate the uncertainty principle (minimum-uncertainty states), exhibit classical-like behavior with oscillating expectation values, and naturally appear in quantum optics.

## Questions

```yaml
- question: "Physicist A prepares a quantum oscillator in the energy eigenstate |n=5⟩. Physicist B prepares one in the coherent state |α⟩ with |α|² = 5 (mean photon number 5). Which state has a position expectation value ⟨x̂⟩(t) that oscillates sinusoidally at frequency ω?"
  type: multiple-choice
  options:
    - "The energy eigenstate |5⟩, because it has definite energy and therefore a well-defined oscillation frequency"
    - "Both states, because both have the same mean energy"
    - "The coherent state |α⟩, because its expectation values follow the classical trajectory while the energy eigenstate has ⟨x̂⟩ = 0 at all times"
    - "Neither state; quantum expectation values of position never oscillate"
  answer: 2
  explanation: "Energy eigenstates |n⟩ have ⟨x̂⟩ = 0 for all time — the wavefunction's probability distribution is symmetric and stationary, so there is no net oscillation of position. They are highly non-classical. The coherent state |α(t)⟩ = |α e^{−iωt}⟩ has ⟨x̂⟩(t) = √(2ℏ/mω) |α| cos(ωt + φ), exactly the classical sinusoidal trajectory. Option A is the classic misconception: definite energy implies stationary probability distribution, which actually suppresses classical-like oscillation rather than enabling it."

- question: "What probability distribution describes the photon number statistics of a coherent state |α⟩ (the probability of finding exactly n photons)?"
  type: multiple-choice
  options:
    - "A Gaussian distribution centered at |α|²"
    - "A uniform distribution — all photon numbers are equally likely"
    - "A Poisson distribution with mean n̄ = |α|²"
    - "A delta function at n = |α|² — coherent states have definite photon number"
  answer: 2
  explanation: "The expansion |α⟩ = e^{−|α|²/2} Σ_n (αⁿ/√n!) |n⟩ gives P(n) = e^{−|α|²} |α|^{2n}/n!, which is a Poisson distribution with mean n̄ = |α|². This Poisson photon statistics is the signature of coherent light — it distinguishes laser output from thermal (Bose-Einstein statistics) or Fock-state light. Option D is wrong: coherent states are superpositions of all number eigenstates and have indefinite photon number (unless α = 0). A Gaussian would be wrong because the Poisson distribution is discrete and defined on non-negative integers."

- question: "Energy eigenstates |n⟩ are the quantum states most analogous to a classical oscillating particle, because they have definite energy corresponding to a definite classical amplitude."
  type: true-false
  answer: false
  explanation: "This is the central misconception that coherent states correct. Energy eigenstates have definite energy but are maximally non-classical in their phase-space behavior: ⟨x̂⟩ = ⟨p̂⟩ = 0 for all n, their probability densities are symmetric and stationary, and for n > 0 they do not satisfy minimum uncertainty. Coherent states |α⟩, not energy eigenstates, are the closest quantum analog to classical motion: their expectation values follow the classical orbit, they maintain their Gaussian shape without spreading, and they saturate the uncertainty bound ΔxΔp = ℏ/2 for all α."

- question: "The ground state |0⟩ of the quantum harmonic oscillator is itself a coherent state — specifically, the coherent state with α = 0."
  type: true-false
  answer: true
  explanation: "â|0⟩ = 0 = 0·|0⟩, so the ground state is an eigenstate of the lowering operator with eigenvalue α = 0. This means |0⟩ satisfies the defining property of a coherent state. It is also a minimum-uncertainty Gaussian wavepacket (ΔxΔp = ℏ/2), consistent with all coherent states. The coherent state |α⟩ for α ≠ 0 is simply the ground state wave packet displaced in phase space — 'translated' to orbit the origin classically. This is why coherent states are sometimes called 'displaced vacuum states.'"

- question: "What does it mean for a coherent state to be a 'minimum-uncertainty state,' and why does this make coherent states the closest quantum analog of classical motion?"
  type: short-answer
  answer: "A minimum-uncertainty state satisfies ΔxΔp = ℏ/2, the equality case of the Heisenberg uncertainty relation. Coherent states achieve this because their position-space wavefunctions are Gaussians: the product of position spread and momentum spread is minimized simultaneously. This makes them as localized as quantum mechanics permits. Classically, a particle has definite position and momentum; quantumly, no state can achieve that, but coherent states come as close as possible — they are the most 'particle-like' quantum states. Furthermore, the Gaussian wavepacket doesn't spread over time (unlike general wavepackets), so the state perpetually tracks the classical orbit without dispersing."
  explanation: "The connection between minimum uncertainty and classical behavior is deep: any state that saturates the Heisenberg bound must be a Gaussian in position space, and Gaussians remain Gaussian under harmonic oscillator time evolution. This means the wave packet shape is preserved, the uncertainty doesn't grow, and the center of the distribution follows exactly the classical trajectory. Energy eigenstates do not have this property for n > 0 — their uncertainties are larger than the minimum, and their probability distributions are stationary rather than oscillating."
```

## Explainer

From your study of the quantum harmonic oscillator, you know that the energy eigenstates |n⟩ form a complete basis and that the ladder operators â and â† step between them: â|n⟩ = √n |n−1⟩. The energy eigenstates have definite energy but wildly oscillating position and momentum uncertainties — they are as far from classical oscillation as a quantum state can be. Coherent states take a different approach: instead of demanding definite energy, they demand definite complex amplitude. A **coherent state** |α⟩ is defined as an eigenstate of the lowering operator, â|α⟩ = α|α⟩, where α is any complex number. This deceptively simple definition has far-reaching consequences.

The most striking property of coherent states is that their expectation values behave exactly like a classical oscillator. If you compute ⟨x̂⟩ and ⟨p̂⟩ for a coherent state |α(t)⟩, you find they oscillate sinusoidally at frequency ω — exactly the classical trajectory. The quantum state is following the classical path through phase space. This is what "classical-like" means: not that uncertainty disappears, but that the wave packet's center moves along the classical orbit without spreading. The uncertainties in position and momentum remain constant at their minimum values Δx = Δp = √(ℏ/2mω), so the wave packet glides around the potential well maintaining its shape forever.

Why do coherent states saturate the uncertainty principle? Recall that the Heisenberg relation ΔxΔp ≥ ℏ/2 is a lower bound. Equality holds only for Gaussian wave packets whose position and momentum spreads are related in a specific way. Coherent states are precisely such **minimum-uncertainty states** — their position-space wavefunctions are Gaussians centered on the classical trajectory. Energy eigenstates are also minimum-uncertainty states (the ground state |0⟩ is in fact the coherent state with α = 0), but excited eigenstates |n⟩ are not — they have larger ΔxΔp than the minimum. Coherent states generalize the ground state's Gaussian shape to all classical amplitudes.

To find the expansion of |α⟩ in the energy basis, you can apply â|α⟩ = α|α⟩ directly. The result is |α⟩ = e^{−|α|²/2} Σ_n (αⁿ/√n!) |n⟩ — a Poisson-weighted superposition of all energy eigenstates. The probability of finding energy E_n = ℏω(n + 1/2) is P(n) = e^{−|α|²} |α|^{2n}/n!, a Poisson distribution with mean n̄ = |α|². This Poisson photon statistics is the signature of **coherent light** — laser output. When |α|² ≫ 1, the Poisson distribution becomes sharply peaked relative to its mean, so coherent states of large amplitude are nearly classical: well-defined intensity with small relative fluctuations, just as you observe from a laser pointer.
