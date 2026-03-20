---
id: hilbert-space-formalism
title: Hilbert Space Formalism
domain: physics
course: quantum-mechanics
prerequisites:
- id: linear-algebra
  type: hard
- id: complex-numbers
  type: hard
- id: vector-spaces-definition
  type: hard
- id: inner-product-spaces
  type: hard
- id: vector-spaces
  type: hard
builds-toward:
- dirac-notation
- quantum-postulates
- operators-and-observables
tags:
- foundations
- linear-algebra
- functional-analysis
stage: formal-systems
status: draft
---

# Hilbert Space Formalism

## Core Idea
Quantum mechanics operates in infinite-dimensional Hilbert spaces—complete inner product spaces over the complex numbers. States are represented as vectors, observables as Hermitian operators, and the inner product encodes probability amplitudes. Understanding this mathematical framework is essential for rigorous quantum theory.

## How It's Best Learned
Start with finite-dimensional examples (2D and 3D Hilbert spaces), verify inner product properties, and work through projection operators and basis expansions. Gradually extend to infinite-dimensional spaces like L² function spaces.

## Common Misconceptions
Not all infinite-dimensional spaces are Hilbert spaces; completeness is essential. The inner product is conjugate-linear in the first argument, not both.

## Explainer

You already know vector spaces and inner products from linear algebra. A **Hilbert space** is a vector space over the complex numbers equipped with an inner product, plus one additional requirement: **completeness**. Completeness means that every Cauchy sequence of vectors — sequences whose members get arbitrarily close to each other — converges to a limit that is still inside the space. Finite-dimensional inner product spaces are automatically complete; it is infinite-dimensional spaces, like the space of square-integrable functions L², where completeness must be verified. Quantum mechanics needs infinite-dimensional Hilbert spaces because the position of a particle can take a continuum of values, requiring infinitely many basis vectors.

The inner product ⟨φ|ψ⟩ plays a central role. In a finite-dimensional real vector space, the inner product is just the dot product. In a complex Hilbert space, it is conjugate-linear in the first argument: ⟨αφ|ψ⟩ = α*⟨φ|ψ⟩. This asymmetry matters because it ensures that ⟨ψ|ψ⟩ is always real and non-negative, which is necessary for probability interpretation — you want |ψ(x)|² ≥ 0. The norm ||ψ|| = √⟨ψ|ψ⟩ measures the "length" of a state vector; physical states are normalized so that ||ψ|| = 1, representing a total probability of one.

Basis expansions work exactly as in finite dimensions, but now with infinitely (or even uncountably) many basis vectors. Any state |ψ⟩ can be written as a sum (or integral) over a complete orthonormal basis: |ψ⟩ = Σₙ cₙ|n⟩ where cₙ = ⟨n|ψ⟩ are the components. The **completeness relation** Σₙ |n⟩⟨n| = 𝟙 is the infinite-dimensional generalization of the resolution of identity. When the spectrum is continuous — as for position or momentum — the sum becomes an integral: |ψ⟩ = ∫ ψ(x)|x⟩ dx, and ψ(x) = ⟨x|ψ⟩ is the wave function. The wave function is not the quantum state; it is one particular representation of the state vector in the position basis.

The power of the Hilbert space formalism is that it unifies all representations. The same abstract state vector |ψ⟩ can be expressed in the position basis (giving the wave function ψ(x)), the momentum basis (giving the momentum-space wave function ψ̃(p)), or any other basis. **Observables** are Hermitian operators on the Hilbert space — operators equal to their own adjoint, Â = Â†. Hermitian operators have real eigenvalues (which become measurement outcomes) and orthogonal eigenvectors (which form the natural basis for that observable). The entire quantum measurement theory — postulates about probability amplitudes, collapse, and expectation values — is cleanly expressed in this language, which is why the Hilbert space formalism is the foundation for everything that follows in quantum mechanics.
