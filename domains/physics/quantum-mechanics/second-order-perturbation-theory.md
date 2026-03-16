---
id: second-order-perturbation-theory
title: Second-Order Perturbation Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: first-order-perturbation-theory
  type: hard
tags:
- perturbation-theory
- corrections
stage: formal-systems
status: draft
---

# Second-Order Perturbation Theory

## Core Idea
Second-order energy correction: E⁽²⟩ = Σ_{k≠n} |⟨k|H'|n⟩|² / (E_n⁽⁰⟩ - E_k⁽⁰⟩), always negative (energy is lowered).

## Explainer

In first-order perturbation theory, you learned to compute the leading correction to an energy level: E_n^(1) = ⟨n|H'|n⟩, the expectation value of the perturbation in the unperturbed state. This works well when H' has a nonzero diagonal matrix element. But sometimes the first-order correction vanishes — the perturbation has no direct overlap with the state — and you need to go deeper. **Second-order perturbation theory** captures the next layer of correction by accounting for how the perturbation can mix the state of interest with all other eigenstates.

The physical picture is that of **virtual transitions**. Even if H' cannot directly shift state |n⟩, it can temporarily mix |n⟩ with neighboring states |k⟩, borrowing energy from those states and then returning to |n⟩. The second-order energy correction is E_n^(2) = Σ_{k≠n} |⟨k|H'|n⟩|² / (E_n^(0) − E_k^(0)). Each term in this sum represents one such virtual excursion: the numerator |⟨k|H'|n⟩|² measures how strongly H' couples state |n⟩ to state |k⟩, and the denominator is the energy gap that must be "borrowed" to reach |k⟩. States close in energy contribute more; states far away contribute negligibly.

An important structural feature: for the **ground state**, all denominator terms are negative (since E_n^(0) < E_k^(0) for all k), so every term in the sum is negative. The ground state always shifts downward at second order. Intuitively, this makes sense: the perturbation provides additional ways for the system to lower its energy by mixing in other states. This is a general quantum mechanical principle — perturbations always push the ground state down (at second order). For excited states, some denominators are positive and some negative, so the sign of E_n^(2) is not guaranteed.

A canonical application is the **van der Waals force** between two neutral atoms. At first order, the dipole-dipole interaction averages to zero because the atoms have no permanent dipoles. But at second order, the perturbation mixes in excited states with non-zero dipoles. The result is an attractive energy that falls off as −C/r⁶ — the London dispersion force. This is an entirely second-order quantum effect: it vanishes at first order and requires the full summation over intermediate states. The same formalism underlies the polarizability of atoms (the susceptibility of an atom to an applied electric field) and the Lamb shift in atomic hydrogen, where virtual photon emissions cause tiny but measurable energy corrections.
