---
id: uncertainty-principle-canonical
title: Canonical Uncertainty Relations
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
- id: heisenberg-uncertainty-principle
  type: soft
builds-toward:
- quantum-harmonic-oscillator
tags:
- uncertainty
- commutation
- limits
stage: advanced
status: draft
---

# Canonical Uncertainty Relations

## Core Idea
For any two observables with commutator [Â, B̂], the uncertainty product satisfies ΔA ΔB ≥ |⟨[Â, B̂]⟩|/2. The canonical relation ΔxΔp ≥ ℏ/2 shows position and momentum cannot both be arbitrarily precise. These relations are fundamental constraints on what can be simultaneously known about a quantum system.

## Explainer

From commutation relations, you know that two operators commute ([Â, B̂] = 0) if and only if they can be simultaneously diagonalized — that is, they share a complete set of eigenstates, and a state can simultaneously have definite values for both observables. Non-commuting operators cannot share eigenstates, so no quantum state can have simultaneously definite values for both. The canonical uncertainty relations translate this algebraic fact into a quantitative bound on *how much* indefiniteness is required.

The **Robertson uncertainty relation** states: for any two observables Â and B̂ in any state |ψ⟩, the product of their standard deviations satisfies ΔA · ΔB ≥ ½|⟨[Â, B̂]⟩|. This is not an approximation or a statement about measurement clumsiness — it is a theorem, proven by applying the Cauchy-Schwarz inequality to two vectors in Hilbert space. For position and momentum, [x̂, p̂] = iℏ, so ⟨[x̂, p̂]⟩ = iℏ in any state, giving the universal bound Δx · Δp ≥ ℏ/2. The bound is state-independent for this pair: no quantum state, no matter how cleverly prepared, can violate it. The minimum Δx · Δp = ℏ/2 is achieved by **Gaussian wave packets** — **coherent states** that are the quantum states most resembling classical particles.

A crucial distinction: ΔA is the standard deviation of outcomes if the same measurement is repeated on many identically prepared copies of the state. It is *not* about a single measurement disturbing the particle. The older "disturbance" picture — a position measurement kicks the momentum — captures some physical intuition but misidentifies the source of uncertainty. The Kennard inequality Δx · Δp ≥ ℏ/2 holds for a Gaussian wave packet *sitting undisturbed in free space*, before any measurement has been made. The uncertainty is a property of the state, not of the measurement procedure. Preparations that reduce Δx necessarily increase Δp, and vice versa, because the Fourier transform relationship between position-space and momentum-space wave functions is a mathematical fact: a narrow spike in x-space requires a broad superposition in p-space.

The Robertson relation is state-dependent in general. For energy eigenstates, ⟨[Ĥ, Â]⟩ = 0 for any observable Â (since energy eigenstates are stationary), so the uncertainty bound vanishes — you can measure compatible observables with arbitrary precision in a stationary state. For angular momentum: [L̂_x, L̂_y] = iℏL̂_z, giving ΔL_x · ΔL_y ≥ ½ℏ|⟨L̂_z⟩|. A state with definite L_z (an eigenstate of L̂_z with ⟨L̂_z⟩ ≠ 0) necessarily has indefinite L_x and L_y. As you move toward the quantum harmonic oscillator, you will see the Robertson relation give a lower bound on the ground-state energy: the zero-point energy ½ℏω is exactly what the uncertainty principle demands of a particle confined to a potential well.
