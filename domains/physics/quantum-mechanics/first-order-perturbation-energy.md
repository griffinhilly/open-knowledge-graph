---
id: first-order-perturbation-energy
title: First-Order Perturbation Energy and Wavefunction Corrections
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-independent-perturbation-theory
  type: hard
builds-toward:
- degenerate-perturbation-theory
tags:
- perturbation-theory
- corrections
- approximations
stage: advanced
status: draft
---

# First-Order Perturbation Energy and Wavefunction Corrections

## Core Idea
First-order perturbation theory gives energy correction E_n^{(1)} = ⟨ψₙ⁽⁰⟩|H'|ψₙ⁽⁰⟩⟩ and wavefunction correction |ψₙ⁽¹⟩⟩ = Σ_{k≠n} ⟨ψₖ⁽⁰⟩|H'|ψₙ⁽⁰⟩⟩/(E_n⁽⁰⟩ - E_k⁽⁰⟩)|ψₖ⁽⁰⟩⟩. The correction is small when off-diagonal matrix elements are small compared to energy level spacings. This approach is widely used in quantum chemistry and atomic physics.

## Explainer

Perturbation theory starts from a problem you already know how to solve — the unperturbed Hamiltonian H⁽⁰⁾ with known eigenstates |ψₙ⁽⁰⁾⟩ and energies Eₙ⁽⁰⁾ — and asks how the solutions change when you add a small extra term H' = λV. The idea is that for small λ, the exact answers are close to the unperturbed ones, and you can write them as a power series: Eₙ = Eₙ⁽⁰⁾ + λEₙ⁽¹⁾ + λ²Eₙ⁽²⁾ + … The first-order corrections capture the dominant effect of the perturbation.

The **first-order energy correction** has a beautifully simple form: E_n⁽¹⁾ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩. This is just the expectation value of the perturbation in the unperturbed state. Intuitively, the energy shifts by however much the perturbation "weighs" against the original wavefunction. For example, if you add a weak electric field to a hydrogen atom (the Stark effect), the first-order energy shift is the average of the potential −eEz over the unperturbed hydrogen orbital. States that are symmetric under z-reflection (like 1s) get zero first-order shift; states without that symmetry can get a nonzero one.

The **first-order wavefunction correction** is more subtle. The perturbed state gets contaminated by nearby unperturbed states: |ψₙ⁽¹⁾⟩ = Σ_{k≠n} c_k |ψₖ⁽⁰⁾⟩, where the coefficient is c_k = ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾). The numerator is the **matrix element** coupling state n to state k through H'; the denominator is the energy gap between them. States that are energetically far away contribute little to the mixing. States that are close in energy but strongly coupled by H' contribute a lot — and if the gap goes to zero, this formula breaks down entirely (the degenerate case, which requires a different treatment).

The regime of validity is the key thing to check before applying these formulas. The perturbation approximation is good when |⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩| ≪ |Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾| for all k ≠ n. In plain terms: the perturbation must mix states weakly compared to their energy separation. When this fails — either because H' is too large or because levels are nearly degenerate — first-order theory gives misleading answers and you need second-order corrections or the degenerate perturbation theory you will study next. In practice, checking the size of the off-diagonal matrix elements relative to the level spacings is how you diagnose whether the perturbative expansion is trustworthy.
