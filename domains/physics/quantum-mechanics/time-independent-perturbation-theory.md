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

## Explainer

From your study of the hydrogen atom, you know that the Schrödinger equation has exact, closed-form solutions for the Coulomb potential. But the real world is richer: atoms sit in external fields, nuclei have finite size, electrons interact relativistically at high enough energies. None of these additions preserve the exact solvability of the bare hydrogen problem. Perturbation theory is the systematic strategy for handling these complications when the additional term is small compared to the unperturbed Hamiltonian.

The central idea is a power series expansion in a smallness parameter λ. Write H = H₀ + λH', where H₀ is the exactly solvable part and you know its eigenvalues E_n⁽⁰⁾ and eigenstates |n⁽⁰⁾⟩. Now assume the true eigenvalues and eigenstates of H can be written as series in λ. Substituting into the full eigenvalue equation Hψ = Eψ and collecting terms order by order in λ turns one hard problem into a sequence of tractable ones. At each order you are solving for corrections using the already-known unperturbed states as a basis.

The first-order energy correction is the most important result: **E_n⁽¹⁾ = ⟨n⁽⁰⁾|H'|n⁽⁰⁾⟩**. This is just the expectation value of the perturbation in the unperturbed state. From your work with observables and operators, you know this is a real number for Hermitian H'. The physical interpretation is elegant: to first order, the energy shift is simply the average value of the perturbation as experienced by the unperturbed wavefunction. No new wavefunction is needed at this order — you evaluate an integral over something you already have.

The first-order state correction is more intricate. The perturbed state mixes in contributions from all other unperturbed states: |ψ_n⁽¹⁾⟩ = Σ_{m≠n} [⟨m⁽⁰⁾|H'|n⁽⁰⁾⟩ / (E_n⁽⁰⁾ − E_m⁽⁰⁾)] |m⁽⁰⁾⟩. Two lessons emerge from this formula. First, the perturbation mixes states through its **matrix elements** ⟨m|H'|n⟩ — if H' has no matrix element connecting state m to state n (for instance, due to selection rules from symmetry), that state contributes nothing. Second, states close in energy are mixed more strongly than states far away — the energy denominator E_n − E_m appears in the denominator, so the expansion breaks down when two levels are nearly degenerate, requiring the separate treatment of degenerate perturbation theory.
