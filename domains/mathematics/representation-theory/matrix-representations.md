---
id: matrix-representations
title: Matrix Representations
domain: mathematics
course: representation-theory
prerequisites:
- id: group-representations
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
builds-toward:
- equivalence-of-representations
- character-theory
tags:
- matrix-representation
- change-of-basis
- coordinate-representation
stage: expert
status: validated
---

# Matrix Representations

## Core Idea
Once a basis for V is chosen, a representation ρ: G → GL(V) becomes a map G → GL_n(F), assigning an n×n invertible matrix to each group element. Different basis choices yield different matrix representations of the same abstract representation. The passage from abstract linear maps to concrete matrices makes computation possible but introduces basis-dependence that must be carefully managed.

## Questions

```yaml
- question: "Two matrix representations of the same group are called equivalent if they are related by:"
  type: multiple-choice
  options:
    - "A permutation of the rows and columns of each matrix"
    - "Conjugation by a fixed invertible matrix P: ρ'(g) = Pρ(g)P⁻¹ for all g ∈ G"
    - "Multiplying each matrix by a fixed scalar"
    - "Transposing each matrix"
  answer: 1
  explanation: "Equivalent matrix representations differ by a change of basis. If we change from basis B to basis B' via an invertible matrix P, then the matrix of ρ(g) in the new basis is Pρ(g)P⁻¹. The same P is used for all group elements — this is what makes it a uniform change of basis rather than an arbitrary reshuffling. This corresponds to the abstract representations being related by an intertwining isomorphism."

- question: "A matrix representation assigns a matrix to each group element such that the product of the matrices for g and h equals the matrix for gh."
  type: true-false
  answer: true
  explanation: "This is the homomorphism condition written in matrix language: if ρ: G → GL_n(F) is a matrix representation, then ρ(g)ρ(h) = ρ(gh) for all g, h ∈ G. Matrix multiplication corresponds to composition of linear transformations, so this says the representation preserves the group operation. In particular, ρ(e) = Iₙ (the identity matrix) and ρ(g⁻¹) = ρ(g)⁻¹."

- question: "Consider the representation of ℤ/2ℤ = {0, 1} on ℝ² given by ρ(0) = I₂ and ρ(1) = [[−1, 0], [0, 1]]. What does this representation do geometrically?"
  type: short-answer
  answer: "It reflects vectors across the y-axis. The generator 1 maps to the matrix that negates the x-coordinate and preserves the y-coordinate, which is reflection through the line x = 0."
  explanation: "This illustrates how matrix representations encode geometric transformations. The group ℤ/2ℤ has order 2, so the non-identity element must square to the identity — and indeed the reflection matrix squares to I₂. Finding such concrete geometric interpretations is one of the primary benefits of working with matrix representations rather than abstract homomorphisms."

- question: "If we change the basis of a 3-dimensional representation, the traces of the representing matrices change."
  type: true-false
  answer: false
  explanation: "The trace of a matrix is invariant under conjugation: tr(PAP⁻¹) = tr(A). Since a change of basis replaces each matrix ρ(g) with Pρ(g)P⁻¹ for a fixed invertible P, the trace tr(ρ(g)) is unchanged. This basis-independence of the trace is precisely why it becomes the foundation of character theory — it extracts representation information that does not depend on coordinate choices."
```

## Explainer

An abstract representation ρ: G → GL(V) becomes a **matrix representation** once you choose an ordered basis {v₁, …, vₙ} for V. Each linear map ρ(g): V → V is then encoded as an n×n matrix whose columns are the coordinates of ρ(g)(v₁), …, ρ(g)(vₙ) in that basis. The homomorphism condition ρ(gh) = ρ(g)ρ(h) translates directly: the matrix product of the matrices for g and h equals the matrix for gh.

The immediate advantage is computability. To check whether a proposed assignment of matrices to group elements is a representation, you verify a finite number of matrix equations. For a group with generators g₁, …, gₖ and relations r₁, …, rₘ, you only need the matrices for the generators and must check that the relations hold at the matrix level. This reduces an infinite verification (all pairs g, h) to a finite one.

The cost is basis-dependence. The same abstract representation can look very different in two bases. For instance, a rotation of ℝ² by angle θ is diagonal in the basis of eigenvectors (with eigenvalues e^{iθ} and e^{−iθ} over ℂ) but has the familiar rotation matrix [[cos θ, −sin θ], [sin θ, cos θ]] in the standard basis. The representation is the same; only the coordinates changed. Two matrix representations related by ρ'(g) = Pρ(g)P⁻¹ for a fixed invertible P and all g ∈ G are called **equivalent** — they are different coordinate descriptions of the same abstract representation.

This means that properties worth studying are those invariant under conjugation. The determinant det(ρ(g)), the trace tr(ρ(g)), and the eigenvalues of ρ(g) are all basis-independent. The trace, in particular, will become the central object of study when you reach character theory: it distills each representation into a function on the group that captures essentially all the structural information, without any reference to a basis.
