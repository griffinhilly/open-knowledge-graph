---
id: time-independent-perturbation-theory
title: Time-Independent Perturbation Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: hydrogen-atom-solution
  type: hard
- id: observables-and-operators
  type: hard
builds-toward:
- first-order-perturbation-theory
- degenerate-perturbation-theory
tags:
- perturbation-theory
- approximations
stage: advanced
status: draft
---

# Time-Independent Perturbation Theory

## Core Idea
For a solvable unperturbed Hamiltonian H₀ with small perturbation H', energies and states are power series expansions: E = E⁽⁰⟩ + λE⁽¹⟩ + ...., |ψ⟩ = |ψ⁽⁰⟩⟩ + λ|ψ⁽¹⟩⟩ + ....

## Questions

```yaml
- question: "What is the first-order energy correction E_n^(1) for a state |n⟩ in time-independent perturbation theory?"
  type: multiple-choice
  options:
    - "The eigenvalue of H' (the perturbation Hamiltonian) in isolation"
    - "The expectation value of H' evaluated in the unperturbed state: ⟨n^(0)|H'|n^(0)⟩"
    - "The overlap integral ⟨n^(0)|n^(1)⟩ between the unperturbed and first-order corrected states"
    - "The sum of all off-diagonal matrix elements of H' connecting state n to all other states"
  answer: 1
  explanation: "The first-order energy correction is E_n^(1) = ⟨n^(0)|H'|n^(0)⟩ — simply the expectation value of the perturbation Hamiltonian in the unperturbed state. The elegance is that you need no new wavefunction at this order: just integrate the known unperturbed state against the perturbation. This is the most important practical result in perturbation theory, used whenever you need a first estimate of how a small perturbation (a magnetic field, a weak potential, a relativistic correction) shifts an energy level."

- question: "In the first-order state correction, which factor determines how strongly an unperturbed state |m^(0)⟩ mixes into the perturbed state |ψ_n^(1)⟩?"
  type: multiple-choice
  options:
    - "The magnitude of the energy difference E_n^(0) − E_m^(0); states far in energy mix more strongly"
    - "Whether m and n have the same parity; only states of opposite parity can mix"
    - "The matrix element ⟨m^(0)|H'|n^(0)⟩ and the inverse of the energy gap; large matrix element and small gap means strong mixing"
    - "The population of state m in thermal equilibrium at the system temperature"
  answer: 2
  explanation: "The mixing coefficient for state m into the corrected state n is ⟨m^(0)|H'|n^(0)⟩ / (E_n^(0) − E_m^(0)). Two factors matter: (1) The matrix element must be nonzero — if symmetry (a selection rule) forbids ⟨m|H'|n⟩, that state contributes nothing. (2) The energy denominator E_n − E_m must be large — states nearly degenerate with state n (small denominator) mix in most strongly, and the formula actually diverges when the gap goes to zero, signaling the breakdown of non-degenerate perturbation theory."

- question: "If the matrix element ⟨m^(0)|H'|n^(0)⟩ = 0 for all m ≠ n due to a symmetry selection rule, then the first-order correction to the state |ψ_n⟩ vanishes."
  type: true-false
  answer: true
  explanation: "The first-order state correction is a sum over all other states m, weighted by ⟨m|H'|n⟩/(E_n − E_m). If every off-diagonal matrix element ⟨m|H'|n⟩ = 0 (e.g., because H' has odd parity and the states are all even, or by some other symmetry), every term in the sum vanishes and |ψ_n^(1)⟩ = 0. The energy still receives a first-order correction (the diagonal element ⟨n|H'|n⟩ may be nonzero), but the wavefunction is unmodified at first order."

- question: "Time-independent perturbation theory remains valid even when two unperturbed energy levels are nearly degenerate, because the first-order energy correction formula handles this case correctly."
  type: true-false
  answer: false
  explanation: "Near-degeneracy is precisely where non-degenerate perturbation theory breaks down. The first-order state correction contains the denominator E_n^(0) − E_m^(0): when two levels are close in energy, this denominator approaches zero and the mixing coefficient diverges, making the perturbative expansion uncontrolled. Exact degeneracy makes the formula undefined. Degenerate perturbation theory handles this by first diagonalizing H' within the degenerate subspace, choosing a good basis before applying the expansion."

- question: "Why is the first-order energy correction E_n^(1) = ⟨n^(0)|H'|n^(0)⟩ particularly elegant, and what does it tell you physically about the relationship between the perturbation and the unperturbed wavefunction?"
  type: short-answer
  answer: "It is elegant because you obtain the first-order energy shift using only the unperturbed wavefunction — no correction to the state is needed at this order. Physically, it says that to first approximation, the energy shift equals the average value of the perturbation as experienced by the unperturbed probability distribution |ψ_n^(0)|². The wavefunction has not yet 'responded' to the perturbation; it simply samples the perturbation according to the unperturbed probability density."
  explanation: "This interpretation connects naturally to the Hellmann-Feynman theorem and to classical intuition: if you turn on a weak external field slowly, the first-order energy change is what the original state would feel on average. The fact that no new wavefunction is needed makes first-order energy corrections computationally inexpensive and explains why they appear everywhere in atomic and molecular physics: Zeeman splitting, Stark effect, fine structure corrections all start with this expectation value calculation."
```

## Explainer

From your study of the hydrogen atom, you know that the Schrödinger equation has exact, closed-form solutions for the Coulomb potential. But the real world is richer: atoms sit in external fields, nuclei have finite size, electrons interact relativistically at high enough energies. None of these additions preserve the exact solvability of the bare hydrogen problem. Perturbation theory is the systematic strategy for handling these complications when the additional term is small compared to the unperturbed Hamiltonian.

The central idea is a power series expansion in a smallness parameter λ. Write H = H₀ + λH', where H₀ is the exactly solvable part and you know its eigenvalues E_n⁽⁰⁾ and eigenstates |n⁽⁰⁾⟩. Now assume the true eigenvalues and eigenstates of H can be written as series in λ. Substituting into the full eigenvalue equation Hψ = Eψ and collecting terms order by order in λ turns one hard problem into a sequence of tractable ones. At each order you are solving for corrections using the already-known unperturbed states as a basis.

The first-order energy correction is the most important result: **E_n⁽¹⁾ = ⟨n⁽⁰⁾|H'|n⁽⁰⁾⟩**. This is just the expectation value of the perturbation in the unperturbed state. From your work with observables and operators, you know this is a real number for Hermitian H'. The physical interpretation is elegant: to first order, the energy shift is simply the average value of the perturbation as experienced by the unperturbed wavefunction. No new wavefunction is needed at this order — you evaluate an integral over something you already have.

The first-order state correction is more intricate. The perturbed state mixes in contributions from all other unperturbed states: |ψ_n⁽¹⁾⟩ = Σ_{m≠n} [⟨m⁽⁰⁾|H'|n⁽⁰⁾⟩ / (E_n⁽⁰⁾ − E_m⁽⁰⁾)] |m⁽⁰⁾⟩. Two lessons emerge from this formula. First, the perturbation mixes states through its **matrix elements** ⟨m|H'|n⟩ — if H' has no matrix element connecting state m to state n (for instance, due to selection rules from symmetry), that state contributes nothing. Second, states close in energy are mixed more strongly than states far away — the energy denominator E_n − E_m appears in the denominator, so the expansion breaks down when two levels are nearly degenerate, requiring the separate treatment of degenerate perturbation theory.
