---
id: eigenvalues-eigenstates-quantum
title: Eigenvalues and Eigenstates
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-operators
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- quantum-observables
- hydrogen-atom-quantum
tags:
- linear-algebra
- quantum-mechanics
- eigenvalue-problem
stage: advanced
status: draft
---

# Eigenvalues and Eigenstates

## Core Idea
For an operator Â, an eigenstate |φₙ⟩ satisfies Â|φₙ⟩ = λₙ|φₙ⟩ where λₙ is the eigenvalue. In quantum mechanics, eigenvalues of an observable operator are the only possible measurement outcomes, and eigenstates are states in which the observable has a definite value. The completeness of eigenstates ensures any quantum state can be expanded in eigenbasis.

## Explainer

You already know from linear algebra that for a matrix M, an eigenvector v satisfies Mv = λv — the vector is unchanged in direction by the operation, only scaled by the eigenvalue λ. In quantum mechanics, this algebraic relationship becomes the central fact about measurement. An **eigenstate** |φₙ⟩ of operator Â satisfies Â|φₙ⟩ = λₙ|φₙ⟩, and the eigenvalue λₙ is the only value you can ever obtain when measuring A in that state. This is the sharpest form of a quantum prediction: perfect certainty about a measurement outcome is equivalent to being in an eigenstate.

Why must observables have real eigenvalues? Because measured quantities must be real numbers. You know from the prerequisite on quantum operators that observables correspond to **Hermitian** operators (Â = Â†). A fundamental theorem guarantees that Hermitian operators have real eigenvalues and that eigenstates belonging to distinct eigenvalues are orthogonal: ⟨φₘ|φₙ⟩ = δₘₙ. Orthogonality is physically essential — two distinct measurement outcomes must correspond to distinguishable states, and inner product zero means maximally distinguishable in quantum mechanics.

The real power of eigenstates comes from **completeness**: the eigenstates of any Hermitian operator span the Hilbert space. Any quantum state |ψ⟩ can be written as |ψ⟩ = Σₙ cₙ|φₙ⟩ where cₙ = ⟨φₙ|ψ⟩. This is just the projection decomposition you know from linear algebra, now applied to states. When you measure A in state |ψ⟩, the probability of obtaining λₙ is |cₙ|², and the state collapses to |φₙ⟩. The squared inner products give the Born rule; the eigenbasis provides the framework in which probabilities are computed.

A concrete example: the Hamiltonian Ĥ is the energy operator. Its eigenstates |Eₙ⟩ satisfy Ĥ|Eₙ⟩ = Eₙ|Eₙ⟩ — these are the **stationary states**, states of definite energy. For the hydrogen atom, the energy eigenvalues are Eₙ = −13.6/n² eV with n = 1, 2, 3, ... The discreteness of these eigenvalues is why atomic spectra consist of sharp lines: only these specific energy values are possible, so only photons with energies equal to differences between levels can be emitted or absorbed. Any general state of the hydrogen atom is a superposition of energy eigenstates, and an energy measurement collapses it to one of them with probability |cₙ|².
