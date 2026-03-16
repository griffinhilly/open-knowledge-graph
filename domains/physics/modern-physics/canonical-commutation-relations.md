---
id: canonical-commutation-relations
title: Canonical Commutation Relations and Uncertainty
domain: physics
course: modern-physics
prerequisites:
- id: quantum-operators-observables
  type: hard
- id: commutation-relations
  type: hard
builds-toward:
- uncertainty-principle-derivation
tags:
- quantum
- commutation
- operators
stage: abstract-reasoning
status: draft
---

# Canonical Commutation Relations and Uncertainty

## Core Idea
The canonical commutation relation [x̂,p̂] = iℏ states that position and momentum operators do not commute. This non-commutativity reflects the fundamental structure of quantum mechanics and directly implies that position and momentum cannot be simultaneously diagonalized (measured with arbitrary precision).

## Explainer

From your study of quantum operators and observables, you learned that physical quantities in quantum mechanics are represented by **operators** acting on wavefunctions, and that measurements correspond to eigenvalues of these operators. You also learned about **commutators**: the commutator [Â,B̂] = ÂB̂ − B̂Â measures how much the order of applying two operators matters. For classical variables, multiplication commutes: position times momentum equals momentum times position, always. In quantum mechanics this is not the case, and the deviation from commutativity is not a technicality — it is the heart of the theory.

The **canonical commutation relation** [x̂, p̂] = iℏ is the defining postulate that distinguishes quantum mechanics from classical mechanics. To see what it means concretely, work in the position representation where x̂ acts by multiplying by x and p̂ acts by (ℏ/i)∂/∂x. Apply [x̂, p̂] to an arbitrary wavefunction ψ(x): x̂(p̂ψ) − p̂(x̂ψ) = x·(ℏ/i)∂ψ/∂x − (ℏ/i)∂(xψ)/∂x = x·(ℏ/i)∂ψ/∂x − (ℏ/i)[ψ + x∂ψ/∂x] = −(ℏ/i)ψ = iℏψ. So [x̂, p̂]ψ = iℏψ for any ψ, confirming the relation. The extra term ψ comes from the product rule — differentiation knows about x in a way that simple multiplication does not. This is why position and momentum are fundamentally incompatible observables.

The consequence is the **Heisenberg uncertainty principle**: ΔxΔp ≥ ℏ/2. This follows from a general theorem: if two Hermitian operators A and B have commutator [A,B] = iC, then ΔAΔ B ≥ |⟨C⟩|/2. The canonical commutation relation [x̂,p̂] = iℏ gives C = ℏ (a constant), so ΔxΔp ≥ ℏ/2 regardless of the state. This is not a statement about measurement disturbance (a common misconception) — it is a statement about the spread of outcomes in repeated measurements on identically prepared systems. A state with perfectly definite position (a Dirac delta in position space) has completely indefinite momentum — it would be a superposition of all momentum eigenstates with equal amplitude. Nature does not allow sharp simultaneous position and momentum, not because our measuring devices are clumsy, but because position and momentum eigenstates are mutually exclusive bases.

The canonical commutation relations generalize across quantum mechanics. For each generalized coordinate qᵢ and its conjugate momentum pⱼ, [q̂ᵢ, p̂ⱼ] = iℏδᵢⱼ, while coordinates commute with each other and momenta commute with each other. This canonical structure, inherited from the Poisson bracket structure of Hamiltonian classical mechanics (where {q,p} = 1 becomes [q̂,p̂] = iℏ), is the bridge between classical and quantum theory. The same commutation algebra underlies angular momentum quantization, bosonic field quantization, and the ladder operator approach to the harmonic oscillator — the algebraic backbone of all of quantum mechanics.
