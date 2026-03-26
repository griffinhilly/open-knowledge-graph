---
id: first-order-perturbation-theory
title: First-Order Perturbation Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-independent-perturbation-theory
  type: hard
builds-toward:
- second-order-perturbation-theory
tags:
- perturbation-theory
- corrections
stage: advanced
status: validated
---
# First-Order Perturbation Theory

## Core Idea
First-order energy correction: E⁽¹⟩ = ⟨ψ⁽⁰⟩|H'|ψ⁽⁰⟩⟩; wavefunction correction mixes states via ⟨k|H'|n⟩/(E_n⁽⁰⁾ - E_k⁽⁰⁾).

## Questions

```yaml
- question: "Two energy levels of an unperturbed Hamiltonian H₀ are nearly degenerate: Eₙ⁽⁰⁾ ≈ Eₖ⁽⁰⁾. A perturbation H' has ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ ≠ 0. What happens to first-order perturbation theory in this situation?"
  type: multiple-choice
  options:
    - "The theory works fine — the correction formula is valid regardless of energy spacing"
    - "The energy correction E⁽¹⁾ₙ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ is still valid, but the wavefunction correction breaks down because the denominator Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾ is small"
    - "Both the energy and wavefunction corrections fail, but only for the states involved in the near-degeneracy"
    - "The wavefunction correction is fine; only the energy correction requires the degenerate perturbation theory treatment"
  answer: 1
  explanation: "The wavefunction correction coefficient for state k mixing into state n is ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾). When the denominator is nearly zero (near-degenerate levels), this coefficient diverges — the mixing is 'strong' and the perturbative expansion breaks down. The energy correction formula E⁽¹⁾ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ is a diagonal matrix element and doesn't directly involve the problematic denominator, but the full first-order theory is still invalid because the underlying expansion in powers of λ has broken down. Near-degenerate states require degenerate perturbation theory, where you first diagonalize H' within the nearly-degenerate subspace."

- question: "In first-order perturbation theory, what determines how strongly an unperturbed state ψₖ⁽⁰⁾ mixes into the perturbed state ψₙ?"
  type: multiple-choice
  options:
    - "Only the magnitude of the off-diagonal matrix element ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ — larger matrix elements mean more mixing"
    - "Only the energy difference Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾ — states close in energy always mix strongly"
    - "Both the off-diagonal matrix element and the energy denominator: mixing is strong when the matrix element is large AND/OR the states are close in energy"
    - "The total norm of H', summed over all states k, determines the overall mixing"
  answer: 2
  explanation: "The mixing coefficient is ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾) — a ratio of two quantities. States close in energy (small denominator) mix strongly even if the matrix element is modest. States with large off-diagonal matrix elements mix strongly even if they are far in energy. States that are both far in energy AND connected by a small matrix element contribute negligibly. This ratio structure explains why perturbation theory works when the energy levels are well-separated and the perturbation is 'small' in units of the energy spacing."

- question: "The first-order energy correction E⁽¹⁾ₙ is the expectation value of the perturbation H' in the unperturbed state ψₙ⁽⁰⁾."
  type: true-false
  answer: true
  explanation: "E⁽¹⁾ₙ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ is exactly the expectation value of H' in the unperturbed state. This is the beautifully direct interpretation of first-order perturbation theory: the shift in energy level n is simply the average value of the perturbation potential, as if the system were still in its unperturbed state. No new eigenvalue problem needs to be solved — you just compute a single matrix element using the states you already have. This is why perturbation theory is so computationally powerful: the hard work of solving H₀ was done once, and corrections are just arithmetic on top."

- question: "To find how energy levels shift under a small perturbation H', you must solve the full eigenvalue problem for H = H₀ + H' — there is no shortcut."
  type: true-false
  answer: false
  explanation: "This is exactly what first-order perturbation theory avoids. Instead of solving the new eigenvalue problem (which may be intractable), you use the already-known eigenstates and eigenvalues of H₀ to compute the correction as a simple matrix element: E⁽¹⁾ₙ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩. The power of perturbation theory is that it converts a hard problem (diagonalizing H₀ + H') into arithmetic (evaluating matrix elements of H' in the already-known basis). The approximation is valid when the correction is small compared to the unperturbed energies."

- question: "What is the physical interpretation of the energy denominator Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾ in the wavefunction mixing coefficient, and why does its smallness cause perturbation theory to break down?"
  type: short-answer
  answer: "The energy denominator measures how much 'energy penalty' there is for the perturbation to mix state k into state n. A large denominator means the two states are energetically far apart — the perturbation would have to supply a lot of energy to shift the system from one to the other, so the mixing is small and perturbation theory is well-controlled. A small denominator means the two states are nearly at the same energy — an arbitrarily weak perturbation can produce significant mixing, because no large energy barrier prevents it. When the denominator approaches zero (exact degeneracy), the expansion diverges: the perturbation, however small, can completely mix the two states and the 'zeroth-order' wavefunctions are no longer good approximations to the true states."
  explanation: "Physically, near-degenerate states are nearly interchangeable from the perspective of the Hamiltonian — they differ only slightly in energy. Any perturbation that connects them will substantially reorganize the actual eigenstates into linear combinations of both. The correct procedure is to first diagonalize H' within the degenerate (or nearly degenerate) subspace to find the right linear combinations, and then treat the coupling to states outside the subspace perturbatively. The smallness of the denominator is the diagnostic that tells you perturbation theory needs this modified treatment."
```

## Explainer

The core idea of perturbation theory, which you've already encountered, is that when a Hamiltonian H = H₀ + λH' differs only slightly from a solvable system H₀, we can expand eigenstates and eigenvalues in powers of λ. First-order perturbation theory is where that expansion becomes computable. It answers the question: if you "turn on" a small perturbation H', how much does each energy level shift?

The **first-order energy correction** E⁽¹⁾ₙ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ has a beautifully direct interpretation: it is the expectation value of the perturbation in the unperturbed state. Physically, you're asking "if the electron were in the original unperturbed state, what would the average potential energy of the perturbation be?" That average is exactly how much the energy level shifts. There's no need to solve a new eigenvalue problem — you just compute a matrix element using states you already know.

The **first-order wavefunction correction** is more subtle. The perturbed state is not just ψₙ⁽⁰⁾ — it gets small admixtures of the other unperturbed states. The coefficient of state ψₖ⁽⁰⁾ mixing into state n is ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾). Two factors control the mixing: the numerator (how much the perturbation "connects" states n and k through off-diagonal matrix elements) and the denominator (how far apart the unperturbed energies are). States close in energy mix strongly; states far apart mix weakly. This is why near-degenerate levels require special treatment — the denominator nearly vanishes and the perturbative expansion breaks down.

The ratio of the first-order correction to the unperturbed energy gives you a rough measure of when the approximation is valid: if E⁽¹⁾ₙ ≪ Eₙ⁽⁰⁾, you're in the perturbative regime. A classic application is the Stark effect (an atom in an external electric field) or fine structure corrections to hydrogen. In both cases, the perturbation is small compared to the Coulomb energy, and the first-order formula gives quantitatively accurate predictions without solving the full problem. The power of the method is that it recycles your existing solutions — the hard work of diagonalizing H₀ already done, the correction is just arithmetic on those results.
