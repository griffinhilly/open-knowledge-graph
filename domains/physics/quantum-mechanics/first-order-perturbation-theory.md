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
status: draft
---

# First-Order Perturbation Theory

## Core Idea
First-order energy correction: E⁽¹⟩ = ⟨ψ⁽⁰⟩|H'|ψ⁽⁰⟩⟩; wavefunction correction mixes states via ⟨k|H'|n⟩/(E_n⁽⁰⁾ - E_k⁽⁰⁾).

## Explainer

The core idea of perturbation theory, which you've already encountered, is that when a Hamiltonian H = H₀ + λH' differs only slightly from a solvable system H₀, we can expand eigenstates and eigenvalues in powers of λ. First-order perturbation theory is where that expansion becomes computable. It answers the question: if you "turn on" a small perturbation H', how much does each energy level shift?

The **first-order energy correction** E⁽¹⁾ₙ = ⟨ψₙ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ has a beautifully direct interpretation: it is the expectation value of the perturbation in the unperturbed state. Physically, you're asking "if the electron were in the original unperturbed state, what would the average potential energy of the perturbation be?" That average is exactly how much the energy level shifts. There's no need to solve a new eigenvalue problem — you just compute a matrix element using states you already know.

The **first-order wavefunction correction** is more subtle. The perturbed state is not just ψₙ⁽⁰⁾ — it gets small admixtures of the other unperturbed states. The coefficient of state ψₖ⁽⁰⁾ mixing into state n is ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾). Two factors control the mixing: the numerator (how much the perturbation "connects" states n and k through off-diagonal matrix elements) and the denominator (how far apart the unperturbed energies are). States close in energy mix strongly; states far apart mix weakly. This is why near-degenerate levels require special treatment — the denominator nearly vanishes and the perturbative expansion breaks down.

The ratio of the first-order correction to the unperturbed energy gives you a rough measure of when the approximation is valid: if E⁽¹⁾ₙ ≪ Eₙ⁽⁰⁾, you're in the perturbative regime. A classic application is the Stark effect (an atom in an external electric field) or fine structure corrections to hydrogen. In both cases, the perturbation is small compared to the Coulomb energy, and the first-order formula gives quantitatively accurate predictions without solving the full problem. The power of the method is that it recycles your existing solutions — the hard work of diagonalizing H₀ already done, the correction is just arithmetic on those results.
