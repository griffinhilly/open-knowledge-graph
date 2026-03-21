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

## Questions

```yaml
- question: "You apply a perturbation H' to a quantum system. The expectation value ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ = 0 for state n. What is the first-order energy correction E_n⁽¹⁾?"
  type: multiple-choice
  options:
    - "Zero — the first-order correction vanishes, though higher-order corrections may still be nonzero"
    - "Nonzero — off-diagonal matrix elements can still contribute at first order"
    - "Undefined — a zero expectation value means perturbation theory cannot be applied"
    - "Negative — a zero diagonal element always implies the energy shifts downward"
  answer: 0
  explanation: "The first-order energy correction is exactly E_n⁽¹⁾ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ — the expectation value of the perturbation in the unperturbed state. If this is zero, the first-order energy correction vanishes. This does not mean higher-order corrections also vanish (E_n⁽²⁾ depends on off-diagonal matrix elements and can be nonzero), and it does not mean perturbation theory fails — it just means you need to go to higher order to see the energy shift. The hydrogen 1s state in a uniform electric field is an example: the first-order Stark shift is zero by symmetry, and the leading effect is second-order."

- question: "The first-order wavefunction correction mixes in other unperturbed states. Which states contribute most strongly?"
  type: multiple-choice
  options:
    - "States with the largest energy gap from state n, because they are most different"
    - "States with large matrix elements ⟨ψₖ|H'|ψₙ⟩ and small energy gaps |Eₙ - Eₖ|"
    - "The highest-energy states, because they have the most room to be perturbed downward"
    - "All states contribute equally regardless of energy gap or coupling strength"
  answer: 1
  explanation: "The mixing coefficient is c_k = ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾). The numerator is the matrix element coupling state k to state n through H'; the denominator is the energy gap. Large matrix elements and small energy gaps → large mixing. Large energy gaps → small mixing. This is why nearby nearly-degenerate levels cause problems: the denominator shrinks toward zero, making the correction diverge and invalidating the perturbative expansion."

- question: "If two unperturbed energy levels are nearly degenerate, first-order non-degenerate perturbation theory gives unreliable results."
  type: true-false
  answer: true
  explanation: "The wavefunction correction formula c_k = ⟨ψₖ|H'|ψₙ⟩ / (Eₙ - Eₖ) has the energy gap in the denominator. When Eₙ ≈ Eₖ, this denominator is small, making c_k large even for modest matrix elements. A large coefficient means the perturbed state has a large admixture of state k, which contradicts the assumption that perturbations are small corrections. In such cases, degenerate perturbation theory must be used instead — it treats the nearly-degenerate subspace exactly from the start."

- question: "A large off-diagonal matrix element ⟨ψₖ|H'|ψₙ⟩ always implies a large wavefunction mixing between states k and n."
  type: true-false
  answer: false
  explanation: "The mixing coefficient depends on both the matrix element and the energy gap: c_k = ⟨ψₖ|H'|ψₙ⟩ / (Eₙ − Eₖ). A large matrix element can produce small mixing if the energy gap is correspondingly large. Conversely, a small matrix element paired with near-degeneracy (tiny denominator) can produce large mixing. This is why the validity condition for perturbation theory is phrased as: matrix elements must be small compared to the relevant energy gaps — both quantities matter jointly."

- question: "Why does the formula for the first-order wavefunction correction break down when two unperturbed energy levels are exactly degenerate?"
  type: short-answer
  answer: "The wavefunction correction coefficient is c_k = ⟨ψₖ|H'|ψₙ⟩ / (Eₙ − Eₖ). When Eₙ = Eₖ exactly, the denominator is zero, making the expression undefined. More fundamentally, if two states are degenerate, any linear combination of them is also an eigenstate with the same energy — the perturbation picks out specific combinations to mix, but the formula as written gives no guidance on which combination is the right starting point. Degenerate perturbation theory resolves this by first diagonalizing H' within the degenerate subspace to find the correct zeroth-order states, then applying the standard correction formulas."
  explanation: "The breakdown is not just a mathematical singularity — it signals a physical reality: when two states are degenerate, small perturbations can cause large reordering and mixing of those states. The perturbative assumption (corrections are small) fails entirely in the degenerate subspace. Degenerate perturbation theory effectively solves the degenerate subspace exactly, sidestepping the zero denominator problem by choosing the right basis before perturbing."
```

## Explainer

Perturbation theory starts from a problem you already know how to solve — the unperturbed Hamiltonian H⁽⁰⁾ with known eigenstates |ψₙ⁽⁰⁾⟩ and energies Eₙ⁽⁰⁾ — and asks how the solutions change when you add a small extra term H' = λV. The idea is that for small λ, the exact answers are close to the unperturbed ones, and you can write them as a power series: Eₙ = Eₙ⁽⁰⁾ + λEₙ⁽¹⁾ + λ²Eₙ⁽²⁾ + … The first-order corrections capture the dominant effect of the perturbation.

The **first-order energy correction** has a beautifully simple form: E_n⁽¹⁾ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩. This is just the expectation value of the perturbation in the unperturbed state. Intuitively, the energy shifts by however much the perturbation "weighs" against the original wavefunction. For example, if you add a weak electric field to a hydrogen atom (the Stark effect), the first-order energy shift is the average of the potential −eEz over the unperturbed hydrogen orbital. States that are symmetric under z-reflection (like 1s) get zero first-order shift; states without that symmetry can get a nonzero one.

The **first-order wavefunction correction** is more subtle. The perturbed state gets contaminated by nearby unperturbed states: |ψₙ⁽¹⁾⟩ = Σ_{k≠n} c_k |ψₖ⁽⁰⁾⟩, where the coefficient is c_k = ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾). The numerator is the **matrix element** coupling state n to state k through H'; the denominator is the energy gap between them. States that are energetically far away contribute little to the mixing. States that are close in energy but strongly coupled by H' contribute a lot — and if the gap goes to zero, this formula breaks down entirely (the degenerate case, which requires a different treatment).

The regime of validity is the key thing to check before applying these formulas. The perturbation approximation is good when |⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩| ≪ |Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾| for all k ≠ n. In plain terms: the perturbation must mix states weakly compared to their energy separation. When this fails — either because H' is too large or because levels are nearly degenerate — first-order theory gives misleading answers and you need second-order corrections or the degenerate perturbation theory you will study next. In practice, checking the size of the off-diagonal matrix elements relative to the level spacings is how you diagnose whether the perturbative expansion is trustworthy.
