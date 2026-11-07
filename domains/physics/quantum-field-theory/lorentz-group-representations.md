---
id: lorentz-group-representations
title: Representations of the Lorentz Group and Weyl Spinors
domain: physics
course: quantum-field-theory
prerequisites:
- id: lorentz-transformation
  type: hard
- id: spin-angular-momentum
  type: hard
- id: pauli-matrices
  type: hard
- id: group-representations
  type: soft
- id: lie-group-representations-intro
  type: soft
builds-toward:
- dirac-field-quantization
- spin-statistics-theorem
tags:
- lorentz-group
- spinors
- representation-theory
- symmetry
- relativistic-fields
stage: expert
status: validated
---

# Representations of the Lorentz Group and Weyl Spinors

## Core Idea
Relativistic fields are classified by how they transform under Lorentz transformations, that is, by representations of the Lorentz group. The six generators, three rotations J and three boosts K, can be recombined into two commuting sets J± = (J ± iK)/2, each obeying the angular momentum algebra. Finite-dimensional representations are therefore labelled by a pair of spins (j₁, j₂), with dimension (2j₁ + 1)(2j₂ + 1). The scalar is (0, 0), the two Weyl spinors are (½, 0) and (0, ½), the four-vector is (½, ½), and the Dirac spinor is the sum (½, 0) ⊕ (0, ½).

## How It's Best Learned
Write the Lorentz algebra from the generators of rotations and boosts, check the commutators in a 4 × 4 matrix representation, and then form J±. Use the known spin-j representations of the angular momentum algebra to build the (j₁, j₂) list. Construct the Weyl spinor transformations explicitly with Pauli matrices and see how a rotation by 2π gives a factor of −1. Finally, show that parity exchanges the two Weyl representations, which is why parity-conserving theories of massive spin-½ particles use Dirac spinors.

## Common Misconceptions
- A spinor is just a four-vector written in a different basis. (A Weyl spinor has two complex components and transforms under (½, 0) or (0, ½); a four-vector is (½, ½), a different representation.)
- The finite-dimensional representations of the Lorentz group are unitary. (The Lorentz group is non-compact, so its finite-dimensional representations, other than the trivial one, are not unitary; the unitary representations that describe particle states are infinite-dimensional.)
- The Dirac spinor is an irreducible representation of the proper Lorentz group. (It splits into two Weyl spinors; it becomes irreducible only when parity is included.)

## Questions

```yaml
- question: "What is the dimension of the (½, ½) representation, and what familiar object transforms this way?"
  type: multiple-choice
  options: ["2, a Weyl spinor", "4, a four-vector", "4, a Dirac spinor", "6, the electromagnetic field tensor"]
  answer: 1
  explanation: "The dimension is (2·½ + 1)(2·½ + 1) = 4. Four-vectors such as x^μ and the four-momentum transform as (½, ½). The Dirac spinor is also four-dimensional but is (½, 0) ⊕ (0, ½)."
- question: "Every finite-dimensional representation of the Lorentz group in which the boosts act nontrivially is unitary."
  type: true-false
  answer: false
  explanation: "The group is non-compact, so its nontrivial finite-dimensional representations cannot be unitary. Boost generators are represented by anti-Hermitian matrices in, for example, the spinor representations."
- question: "A Weyl spinor is rotated by 2π about any axis. What happens to it?"
  type: multiple-choice
  options: ["It returns unchanged", "It is multiplied by −1", "It is multiplied by i", "It becomes a right-handed spinor"]
  answer: 1
  explanation: "Rotations act on Weyl spinors as exp(−iθ·σ/2). For θ = 2π this gives −1. A rotation by 4π is needed to return the spinor to itself."
- question: "Why does quantum electrodynamics use four-component Dirac spinors rather than two-component Weyl spinors for the electron?"
  type: short-answer
  answer: "Parity exchanges the (½, 0) and (0, ½) representations because it reverses boosts but not rotations. Electromagnetism conserves parity and the electron has mass, so the field must contain both Weyl components, which together form a Dirac spinor."
  explanation: "A mass term couples the left- and right-handed Weyl spinors. In the weak interaction, which violates parity, the two components couple differently, and the Weyl description is natural."
```

## Explainer
A Lorentz transformation acts on spacetime coordinates through a 4 × 4 matrix Λ. A field must transform in a way consistent with this, φ(x) → D(Λ)φ(Λ⁻¹x), where the matrices D(Λ) form a representation of the Lorentz group. Finding all such representations amounts to listing every kind of relativistic field.

The group has six generators: three rotation generators Jᵢ and three boost generators Kᵢ. In a common convention their commutators are

[Jᵢ, Jⱼ] = iεᵢⱼₖJₖ, [Jᵢ, Kⱼ] = iεᵢⱼₖKₖ, [Kᵢ, Kⱼ] = −iεᵢⱼₖJₖ.

The last relation says that two boosts in different directions combine into a rotation, the origin of Thomas precession. Define J₊ = (J + iK)/2 and J₋ = (J − iK)/2. A short calculation shows that J₊ and J₋ commute with each other, and that each obeys the angular momentum algebra [Aᵢ, Aⱼ] = iεᵢⱼₖAₖ.

The representations of the angular momentum algebra are known from quantum mechanics: one for each spin j = 0, ½, 1, and so on, of dimension 2j + 1. A representation of the Lorentz algebra is a choice of spin for each copy, written (j₁, j₂), with dimension (2j₁ + 1)(2j₂ + 1). The ordinary angular momentum J = J₊ + J₋ then contains spins from |j₁ − j₂| to j₁ + j₂. The simplest cases are:

- (0, 0): a scalar field, one component.
- (½, 0) and (0, ½): the two Weyl spinors, each with two complex components, usually called left-handed and right-handed.
- (½, ½): a four-vector, such as the electromagnetic potential A^μ.
- (1, 0) ⊕ (0, 1): an antisymmetric tensor such as F^μν, with six components.

On a Weyl spinor, rotations act as exp(−iθ·σ/2) and boosts as exp(∓η·σ/2), with opposite signs for the two kinds. A rotation by 2π multiplies the spinor by −1, which reflects the fact that spinors are representations of SL(2, C), the double cover of the proper Lorentz group.

Parity reverses K but leaves J unchanged, so it swaps J₊ and J₋. It therefore turns a (½, 0) spinor into a (0, ½) spinor. A theory that conserves parity and describes a massive spin-½ particle needs both, combined into the four-component Dirac spinor (½, 0) ⊕ (0, ½). In the weak interaction, which violates parity, only the left-handed Weyl component of each fermion couples to the W boson.

These finite-dimensional representations are not unitary, because the Lorentz group is non-compact. Particle states instead form unitary, infinite-dimensional representations of the full Poincaré group. Eugene Wigner classified them in 1939 by mass and by spin or helicity.
