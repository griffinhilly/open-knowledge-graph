---
id: quantum-operators-eigenvalues
title: Quantum Operators and Eigenvalues
domain: physics
course: modern-physics
prerequisites:
- id: probability-amplitude-interpretation
  type: hard
builds-toward:
- classical-limit-correspondence
- uncertainty-relation-measurements
tags:
- quantum-mechanics
- operators
stage: advanced
status: draft
---

# Quantum Operators and Eigenvalues

## Core Idea
In quantum mechanics, physical observables (position, momentum, energy) are represented by Hermitian operators. When an operator Â acts on an eigenstate |ψ⟩, it returns the same state multiplied by a scalar eigenvalue: Â|ψ⟩ = a|ψ⟩. The eigenvalue is the unique result obtained when measuring the observable on that eigenstate; the set of all eigenvalues of an operator comprises the possible measurement outcomes.

## How It's Best Learned
Learn the position and momentum operators in 1D: x̂ and p̂ = −iℏ d/dx. Apply them to simple wavefunctions and eigenstates; compute expectation values for particles in boxes.

## Common Misconceptions
- Operators are not numbers; they are mathematical objects that transform states.
- Eigenvalues of Hermitian operators are always real, but eigenstates are generally complex.
- The eigenvalue equation Âψ = aψ holds only for eigenstates, not arbitrary states.

## Explainer

From the probability amplitude interpretation, you know that the wavefunction ψ(x) encodes probability: |ψ(x)|² dx is the probability of finding the particle in a small interval around x. But the wavefunction also encodes information about momentum, energy, and every other observable — it just takes more work to extract it. **Quantum operators** are the machinery that extracts this information. Each physical observable is paired with a specific operator that "questions" the wavefunction about that quantity.

The key example is momentum. Classically, momentum is just the number p = mv. Quantum mechanically, momentum is represented by the operator p̂ = −iℏ ∂/∂x. This operator does not multiply ψ by a number; it *differentiates* it. Apply p̂ to the wavefunction ψ(x) = e^{ikx} and you get: −iℏ (ik) e^{ikx} = ℏk · e^{ikx}. The result is the *same* wavefunction multiplied by the scalar ℏk. This is the **eigenvalue equation** p̂ψ = pψ, with eigenvalue p = ℏk. The function e^{ikx} is an **eigenstate** of momentum with a definite momentum ℏk — if you measure the momentum of a particle in this state, you will always get exactly ℏk, with certainty. The eigenvalue is the measurement outcome.

What happens when the particle is *not* in a momentum eigenstate? Any normalizable wavefunction can be expanded as a superposition of eigenstates: ψ(x) = ∫ c(k) e^{ikx} dk. Each term e^{ikx} has a definite momentum ℏk, and |c(k)|² is proportional to the probability that a measurement yields that particular momentum. The operator p̂ does not return a single number when it acts on a superposition; instead, measurement causes the state to **collapse** to one eigenstate, with the corresponding eigenvalue as the outcome. Before measurement, only the probability distribution over eigenvalues is defined. This is the fundamental departure from classical mechanics: not all states have definite values for all observables simultaneously.

The requirement that operators be **Hermitian** (self-adjoint: Â† = Â) guarantees two essential properties. First, all eigenvalues of a Hermitian operator are *real numbers* — which they must be, since measurements yield real values. Second, eigenstates belonging to *different* eigenvalues are mutually **orthogonal**: ⟨ψ_a | ψ_b⟩ = 0 if a ≠ b. This orthogonality means the eigenstates form an independent "basis" for all possible states — you can decompose any state into a sum of eigenstates, and the expansion coefficients directly give the probability distribution for measurement outcomes. The position operator x̂ (which simply multiplies by x), the momentum operator p̂, and the Hamiltonian Ĥ (which represents total energy) are the foundational Hermitian operators from which all of quantum mechanics is built.
