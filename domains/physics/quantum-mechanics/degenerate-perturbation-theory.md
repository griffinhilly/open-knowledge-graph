---
id: degenerate-perturbation-theory
title: Degenerate Perturbation Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-independent-perturbation-theory
  type: hard
tags:
- perturbation-theory
- degeneracy
stage: advanced
status: validated
---

# Degenerate Perturbation Theory

## Core Idea
For degenerate unperturbed levels, solve the matrix eigenvalue problem of H' restricted to the degenerate subspace to find correct zeroth-order states.

## Questions

```yaml
- question: "You apply the non-degenerate perturbation theory formula for first-order state corrections to two states |n⟩ and |m⟩ with the same unperturbed energy E⁰ₙ = E⁰ₘ. What goes wrong?"
  type: multiple-choice
  options:
    - "Nothing goes wrong — the formula still gives finite corrections when the states are orthogonal"
    - "The formula gives zero corrections for all degenerate states, which is too conservative"
    - "The denominator E⁰ₙ − E⁰ₘ = 0, making the correction terms diverge, so the formula is undefined"
    - "The first-order energy correction ⟨n|H'|n⟩ is not well-defined for degenerate states"
  answer: 2
  explanation: "The non-degenerate state correction formula mixes |m⟩ into |n⟩ with coefficient ⟨m|H'|n⟩/(E⁰ₙ − E⁰ₘ). When E⁰ₙ = E⁰ₘ, this denominator is zero and the coefficient diverges — the formula breaks down entirely. Option D is wrong because ⟨n|H'|n⟩ is perfectly well-defined; it's the state corrections (mixing with degenerate partners) that fail, not the energy corrections by themselves."

- question: "In degenerate perturbation theory, what determines the 'good states' — the correct zeroth-order states to use?"
  type: multiple-choice
  options:
    - "Any orthonormal basis within the degenerate subspace works equally well; the choice is arbitrary"
    - "The eigenvectors of H' restricted to the degenerate subspace — the states that diagonalize the perturbation within that subspace"
    - "The states with the largest matrix element ⟨ψᵢ|H'|ψᵢ⟩"
    - "The original spherical harmonics, which are always the correct starting point"
  answer: 1
  explanation: "The good states are those linear combinations of the degenerate subspace that make H' diagonal within that subspace — i.e., the eigenvectors of the n×n matrix Wᵢⱼ = ⟨ψᵢ|H'|ψⱼ⟩. These are the states H' 'prefers' and the states for which the first-order energy corrections are well-defined. Option A is the central misconception: not just any basis works. In the Stark effect, for instance, the good states are specific mixtures of 2s and 2p, not the individual spherical harmonics."

- question: "When applying degenerate perturbation theory, any linear combination of the degenerate states is a valid 'good state' that can be used to compute perturbative corrections."
  type: true-false
  answer: false
  explanation: "False — this is the key misconception degenerate perturbation theory corrects. The 'good states' are specifically those combinations that diagonalize H' within the degenerate subspace. An arbitrary combination will have off-diagonal matrix elements with its degenerate partners, meaning the perturbation mixes them and the non-degenerate formula still diverges. The perturbation itself selects the preferred basis — you must diagonalize W to find it. Once you have the good states, the corrections are finite and well-defined."

- question: "If the perturbation H' completely lifts an n-fold degeneracy at first order, all n eigenvalues of the degenerate subspace matrix W are distinct."
  type: true-false
  answer: true
  explanation: "True by definition. The eigenvalues of W are the first-order energy corrections. If all n eigenvalues are distinct, then after adding H', all n levels sit at different energies — the original degeneracy has been completely resolved. If some eigenvalues are equal, that degeneracy persists at first order and you must go to higher order to resolve it. 'Complete lifting' is exactly the condition of n distinct eigenvalues."

- question: "Explain why finding 'good states' resolves the breakdown of non-degenerate perturbation theory in the degenerate case."
  type: short-answer
  answer: "Non-degenerate perturbation theory fails because it tries to mix degenerate states with each other using a formula that has zero in the denominator. The good states are eigenvectors of H' within the degenerate subspace — they diagonalize the perturbation there. Because they diagonalize H', the off-diagonal matrix elements between good states vanish: ⟨good state i|H'|good state j⟩ = 0 for i ≠ j. So when the non-degenerate formula tries to mix them, the numerator is zero (not just the denominator), and the 0/0 problem is resolved — there is no mixing between degenerate good states needed, and mixing with states outside the subspace uses the original non-degenerate formula with nonzero denominators."
  explanation: "The geometric intuition is that H' 'breaks' the symmetry of the degenerate subspace by preferring certain directions. The good states align with those preferred directions, so H' can be treated as if it simply assigns different energies to each good state — no mixing needed within the subspace."
```

## Explainer

In regular (non-degenerate) perturbation theory, you found the first-order energy correction E¹ₙ = ⟨n|H'|n⟩ and the first-order state correction by mixing in other unperturbed states. The mixing formula contains terms like ⟨m|H'|n⟩/(E⁰ₙ − E⁰ₘ). This works beautifully when all unperturbed energies are distinct. But what happens when two or more states share the same unperturbed energy? The denominator E⁰ₙ − E⁰ₘ goes to zero, and the formula blows up. Degenerate perturbation theory is the resolution to this breakdown.

The fundamental issue is that when a subspace is degenerate, any linear combination of the degenerate states is an equally valid zero-order eigenstate. The perturbation H' will in general prefer certain combinations — it lifts the degeneracy by having different matrix elements for different basis choices. The correct strategy is to find the **good states**: those linear combinations of the degenerate subspace that diagonalize H' within that subspace. These good states have well-defined first-order energies and do not suffer from the zero-denominator problem when mixed with states outside the subspace.

Concretely, if you have an n-fold degenerate level with unperturbed states |ψ₁⟩, ..., |ψₙ⟩, you form the n×n **degenerate subspace matrix** W with elements Wᵢⱼ = ⟨ψᵢ|H'|ψⱼ⟩. Diagonalizing W gives you n eigenvalues — these are the first-order energy corrections — and n eigenvectors — these are the good zeroth-order states. Each eigenvalue E¹ describes how much H' shifts the energy of the corresponding good state. When the n eigenvalues are all different, H' has completely lifted the degeneracy to first order. If some remain equal, you have a residual degeneracy and must look to higher order.

The classic example is the hydrogen atom in an external electric field (the **Stark effect**). The n = 2 level is four-fold degenerate: the 2s and three 2p states all share the same unperturbed energy. The electric field perturbation H' = eEz mixes these states. Forming the 4×4 matrix and diagonalizing it reveals which combinations are shifted (by ±3eEa₀) and which are unshifted. Crucially, the good states are specific linear combinations of 2s and 2p — not the original spherical harmonics — chosen precisely so that H' is diagonal. Degenerate perturbation theory tells you both how much the levels shift and what the physically relevant quantum states become under the perturbation.
