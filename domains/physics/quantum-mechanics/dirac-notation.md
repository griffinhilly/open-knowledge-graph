---
id: dirac-notation
title: Dirac Notation (Bra-Ket Notation)
domain: physics
course: quantum-mechanics
prerequisites:
- id: linear-algebra
  type: hard
- id: vector-spaces
  type: soft
builds-toward:
- kets-and-bras
- observables-and-operators
tags:
- notation
- hilbert-spaces
- foundations
stage: formal-systems
status: draft
---

# Dirac Notation (Bra-Ket Notation)

## Core Idea
Dirac notation compactly represents quantum states and operations using kets |ψ⟩ (column vectors) and bras ⟨ψ| (row vectors). The notation separates abstract state space from coordinate representation and elegantly expresses inner products, operators, and expectation values. It is the standard language of quantum mechanics.

## Explainer

From linear algebra, you know that vectors can be represented as column matrices, and that row vectors pair with column vectors to produce scalars via the dot product. Dirac notation extends this idea to the abstract, infinite-dimensional spaces that quantum mechanics requires. A **ket** |ψ⟩ is an abstract state vector — think of it as a column vector that lives in a **Hilbert space** rather than ordinary three-dimensional space. Its **bra** partner ⟨ψ| is the corresponding row vector (the conjugate transpose). The inner product of two states is written ⟨φ|ψ⟩, which is just the abstract version of the dot product you've seen before — a complex number that measures the "overlap" between two states.

The power of the notation becomes clear when you write a basis expansion. If {|n⟩} is an orthonormal basis (⟨m|n⟩ = δ_mn), then any state can be written |ψ⟩ = Σ_n cₙ|n⟩, where cₙ = ⟨n|ψ⟩ are the components. This is exactly the vector-decomposition you did in linear algebra — Dirac notation just strips away the coordinate system, letting you manipulate states without committing to a specific representation. The same state |ψ⟩ can be expressed in the position basis (giving a wavefunction ψ(x) = ⟨x|ψ⟩), the momentum basis, the energy basis, or any other, simply by choosing different bra vectors.

**Operators** in Dirac notation act on kets from the left to produce new kets: Â|ψ⟩ = |φ⟩. A sandwich like ⟨φ|Â|ψ⟩ is a **matrix element** — a complex number. This is the inner product of |φ⟩ with the vector Â|ψ⟩, and it corresponds to a single entry in the matrix representation of Â. Expectation values take the form ⟨ψ|Â|ψ⟩, which is the average value of observable A in state |ψ⟩. Notice that the entire apparatus of quantum mechanics — wavefunctions, operators, eigenvalue equations, measurement — can be stated in these terms without ever writing an integral or picking a coordinate system.

A useful mnemonic: bra on the left, ket on the right, the bracket ⟨·|·⟩ is the inner product. The notation is designed so that complex conjugation is handled automatically — ⟨ψ|φ⟩ = ⟨φ|ψ⟩*, just as in linear algebra. Learning to read expressions like ⟨a|Â|b⟩ fluidly — "the matrix element of Â between states a and b" — is the key skill that unlocks the rest of quantum mechanics. Everything that follows, from observables to commutation relations to perturbation theory, is written in this language.
