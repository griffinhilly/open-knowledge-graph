---
id: kets-and-bras
title: Kets, Bras, and Hilbert Space Duality
domain: physics
course: quantum-mechanics
prerequisites:
- id: dirac-notation
  type: hard
- id: vector-spaces
  type: hard
builds-toward:
- observables-and-operators
- quantum-entanglement
tags:
- hilbert-spaces
- duality
- linear-algebra
stage: formal-systems
status: draft
---

# Kets, Bras, and Hilbert Space Duality

## Core Idea
A ket |ψ⟩ represents a quantum state as a vector in Hilbert space; its dual bra ⟨ψ| is the linear functional computing inner products. The bra-ket ⟨ψ|φ⟩ encodes probabilities and expectation values.

## Explainer

From your study of **vector spaces**, you know that a vector lives in a space V and can be added to other vectors or multiplied by scalars. You also know there is a companion space — the **dual space** V* — consisting of all linear maps from V to the scalars. Dirac's bra-ket notation is precisely this mathematical structure, dressed in physics-friendly clothing. A **ket** |ψ⟩ is a vector in the Hilbert space H — the complete, normed vector space of quantum states. A **bra** ⟨ψ| is the corresponding element of the dual space H*, defined by the rule ⟨ψ|(|φ⟩) = ⟨ψ|φ⟩. What makes a Hilbert space special compared to a generic vector space is the **inner product**: a sesquilinear map ⟨·|·⟩ : H × H → ℂ that generalizes the dot product to complex-valued, infinite-dimensional spaces.

The physical meaning of the inner product is probability. If |ψ⟩ is a normalized state and |n⟩ is an eigenstate of some observable, then |⟨n|ψ⟩|² is the probability of measuring eigenvalue n when the system is in state |ψ⟩. This is the Born rule, and the bra-ket formalism makes it a tautology of notation: the bra ⟨n| is precisely the linear functional that extracts the component of |ψ⟩ along |n⟩. Normalization requires ⟨ψ|ψ⟩ = 1, which ensures that all probabilities sum to one. The transition amplitude ⟨φ|ψ⟩ gives the overlap between states; when |φ⟩ and |ψ⟩ are orthogonal (no overlap), this inner product vanishes, meaning the two states are perfectly distinguishable.

Operators enter the picture as maps from kets to kets. An **observable** Â maps |ψ⟩ to Â|ψ⟩, and the expectation value is ⟨Â⟩ = ⟨ψ|Â|ψ⟩ — a bra acting on a ket that itself has been acted on by an operator. The bra-ket sandwich packages this naturally: ⟨ψ| is on the left, Â is in the middle, |ψ⟩ is on the right. The **outer product** |φ⟩⟨ψ| — note the reversed order — is itself an operator: it maps any ket |χ⟩ to |φ⟩⟨ψ|χ⟩ = ⟨ψ|χ⟩|φ⟩, a scalar times a ket. In particular, |n⟩⟨n| is the **projection operator** onto the eigenstate |n⟩, and the completeness relation Σ_n |n⟩⟨n| = 1 — summing projection operators over a complete basis — is the statement that any state can be decomposed in that basis.

The Dirac notation pays dividends particularly when changing bases. In finite-dimensional linear algebra, changing basis requires matrix multiplication; in Dirac notation, you simply insert a completeness relation. To express |ψ⟩ in position space: |ψ⟩ = ∫ dx |x⟩⟨x|ψ⟩ = ∫ dx ψ(x)|x⟩, where ψ(x) = ⟨x|ψ⟩ is the familiar wavefunction. The wavefunction is not the quantum state — it is the components of the quantum state in the position basis, exactly as a column of numbers is not the vector but its coordinates in some basis. Bra-ket notation makes this distinction precise and keeps the formalism basis-independent until a specific representation is needed.
