---
id: uncertainty-principle-formal
title: Uncertainty Principle (Formal Treatment)
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
- id: heisenberg-uncertainty-principle
  type: soft
builds-toward:
- wkb-approximation
tags:
- uncertainty
- fundamental-limits
stage: advanced
status: draft
---

# Uncertainty Principle (Formal Treatment)

## Core Idea
The formal uncertainty principle states ΔA·ΔB ≥ ½|⟨[A,B]⟩|. For position and momentum, this gives Δx·Δp ≥ ℏ/2, a fundamental limit encoded in quantum theory's mathematical structure.

## Explainer

You've already seen the Heisenberg uncertainty principle as a qualitative statement — position and momentum cannot both be sharp at once — and you've seen that the commutator [X̂, P̂] = iℏ encodes this incompatibility. The formal treatment makes both of these precise and shows they are the same statement. The **Robertson uncertainty relation** ΔA·ΔB ≥ ½|⟨[Â,B̂]⟩| is a theorem that follows from the mathematics of Hilbert spaces, not an additional physical assumption. It says: for any state |ψ⟩ and any two observables A and B, the product of their standard deviations is bounded below by half the absolute expectation value of their commutator.

The standard deviation ΔA here has a precise meaning: ΔA² = ⟨Â²⟩ − ⟨Â⟩², which is the variance of the distribution of outcomes you would get from many identical measurements. When ΔA = 0, the state is an eigenstate of Â with a single certain outcome. The Robertson relation then says: if [Â, B̂] ≠ 0 in the state |ψ⟩, you cannot simultaneously have both ΔA = 0 and ΔB = 0. The proof uses the Cauchy-Schwarz inequality applied to two vectors in Hilbert space — the same Cauchy-Schwarz inequality you know from linear algebra, now in function space.

For position and momentum, [X̂, P̂] = iℏ (a constant operator), so ⟨[X̂, P̂]⟩ = iℏ in every state, giving Δx·Δp ≥ ℏ/2 universally. This is the **canonical uncertainty relation**. A Gaussian wavepacket — a wavefunction of the form exp(−x²/4σ²) — saturates this bound exactly: it is the minimum-uncertainty state. Squeezing the packet in position (smaller σ) automatically widens it in momentum, and vice versa. This is not measurement disturbance — it reflects the intrinsic spread of the quantum state before any measurement is made.

The formalism extends naturally to other pairs. Energy and time give ΔE·Δt ≥ ℏ/2, though this relation requires more care because time is a parameter in quantum mechanics, not an operator in the same sense. Angular momentum components satisfy [L̂_x, L̂_y] = iℏL̂_z, yielding ΔL_x·ΔL_y ≥ ℏ|⟨L̂_z⟩|/2. The structure is the same each time: nonzero commutator → unavoidable uncertainty product. The formal treatment thus unifies all these relations under a single mathematical theorem and makes clear that the uncertainty principle is not a weakness of our instruments but a feature of the underlying Hilbert-space geometry.
