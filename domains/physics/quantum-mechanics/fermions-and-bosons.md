---
id: fermions-and-bosons
title: Fermions and Bosons
domain: physics
course: quantum-mechanics
prerequisites:
- id: identical-particles-quantum
  type: hard
builds-toward:
- pauli-exclusion-principle
tags:
- fermions
- bosons
- statistics
stage: abstract-reasoning
status: draft
---

# Fermions and Bosons

## Core Idea
Half-integer spin particles (electrons, quarks) are fermions with antisymmetric wavefunctions; integer spin particles (photons, pions) are bosons with symmetric ones. Fermions obey Pauli exclusion; bosons allow multiple particles in one state.

## Explainer

From your study of identical particles, you know that quantum mechanics imposes a strict rule on the wavefunction of two indistinguishable particles: it must either stay the same (symmetric) or flip sign (antisymmetric) when the two particles are exchanged. What this topic reveals is that this isn't a free choice — it is determined entirely by a particle's **spin**. Nature divides all known particles into exactly two families based on this criterion, and the consequences of that division structure nearly all of matter and light.

**Fermions** have half-integer spin (1/2, 3/2, 5/2, ...) and their many-particle wavefunction is antisymmetric under exchange. Write the two-particle state as Ψ(r₁, r₂) = −Ψ(r₂, r₁). Now ask: what happens if both particles are in the same single-particle state φ(r)? The wavefunction becomes φ(r₁)φ(r₂) − φ(r₂)φ(r₁) = 0. The state vanishes — it is literally impossible for two fermions to occupy the same quantum state. This is the **Pauli exclusion principle**, emerging directly from antisymmetry. Electrons, protons, neutrons, and quarks are all fermions, and this exclusion is why matter is rigid: the electrons in an atom can't all collapse into the lowest energy state, so atoms have a shell structure, and compressed matter resists further compression.

**Bosons** have integer spin (0, 1, 2, ...) and their wavefunction is symmetric under exchange. There is no corresponding exclusion; in fact, the probability of a boson entering an already-occupied state is *enhanced* compared to distinguishable particles. This is the origin of **Bose-Einstein condensation**: below a critical temperature, a macroscopic fraction of a bosonic gas can pile into the single lowest-energy quantum state, producing phenomena like superfluidity and the laser (where many photons occupy the same mode). Light is made of photons (spin-1 bosons), which is why a laser can concentrate enormous numbers of photons into one coherent state.

The connection between spin and statistics — fermions antisymmetric, bosons symmetric — is not an independent postulate but is proven from first principles in relativistic quantum field theory (the **spin-statistics theorem**). The proof is deep, requiring causality and Lorentz invariance. At the level of non-relativistic quantum mechanics, you treat it as a rule. But it is worth appreciating that this rule, which divides all particles in nature into two classes and determines whether matter is opaque or transparent, electrical or inert, solid or superfluid, follows from the most fundamental symmetries of spacetime.
