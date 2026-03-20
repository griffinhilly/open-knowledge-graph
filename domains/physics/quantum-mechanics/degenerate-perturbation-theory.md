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
status: draft
---

# Degenerate Perturbation Theory

## Core Idea
For degenerate unperturbed levels, solve the matrix eigenvalue problem of H' restricted to the degenerate subspace to find correct zeroth-order states.

## Explainer

In regular (non-degenerate) perturbation theory, you found the first-order energy correction E¹ₙ = ⟨n|H'|n⟩ and the first-order state correction by mixing in other unperturbed states. The mixing formula contains terms like ⟨m|H'|n⟩/(E⁰ₙ − E⁰ₘ). This works beautifully when all unperturbed energies are distinct. But what happens when two or more states share the same unperturbed energy? The denominator E⁰ₙ − E⁰ₘ goes to zero, and the formula blows up. Degenerate perturbation theory is the resolution to this breakdown.

The fundamental issue is that when a subspace is degenerate, any linear combination of the degenerate states is an equally valid zero-order eigenstate. The perturbation H' will in general prefer certain combinations — it lifts the degeneracy by having different matrix elements for different basis choices. The correct strategy is to find the **good states**: those linear combinations of the degenerate subspace that diagonalize H' within that subspace. These good states have well-defined first-order energies and do not suffer from the zero-denominator problem when mixed with states outside the subspace.

Concretely, if you have an n-fold degenerate level with unperturbed states |ψ₁⟩, ..., |ψₙ⟩, you form the n×n **degenerate subspace matrix** W with elements Wᵢⱼ = ⟨ψᵢ|H'|ψⱼ⟩. Diagonalizing W gives you n eigenvalues — these are the first-order energy corrections — and n eigenvectors — these are the good zeroth-order states. Each eigenvalue E¹ describes how much H' shifts the energy of the corresponding good state. When the n eigenvalues are all different, H' has completely lifted the degeneracy to first order. If some remain equal, you have a residual degeneracy and must look to higher order.

The classic example is the hydrogen atom in an external electric field (the **Stark effect**). The n = 2 level is four-fold degenerate: the 2s and three 2p states all share the same unperturbed energy. The electric field perturbation H' = eEz mixes these states. Forming the 4×4 matrix and diagonalizing it reveals which combinations are shifted (by ±3eEa₀) and which are unshifted. Crucially, the good states are specific linear combinations of 2s and 2p — not the original spherical harmonics — chosen precisely so that H' is diagonal. Degenerate perturbation theory tells you both how much the levels shift and what the physically relevant quantum states become under the perturbation.
