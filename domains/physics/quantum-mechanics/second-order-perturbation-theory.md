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
stage: advanced
status: validated
---

# Second-Order Perturbation Theory

## Core Idea
Second-order energy correction: E⁽²⟩ = Σ_{k≠n} |⟨k|H'|n⟩|² / (E_n⁽⁰⟩ - E_k⁽⁰⟩), always negative (energy is lowered).

## Questions

```yaml
- question: "A student calculates the second-order energy correction for the ground state of a quantum system and obtains a positive value. What can you immediately conclude?"
  type: multiple-choice
  options:
    - "The perturbation destabilizes the ground state, which is unusual but possible"
    - "The calculation contains an error — the second-order correction to the ground state is always negative or zero"
    - "The result is physically reasonable because perturbations can raise or lower energy at second order"
    - "The ground state is degenerate, requiring a different formalism"
  answer: 1
  explanation: "For the ground state, every term in E_n^(2) = Σ_{k≠n} |⟨k|H'|n⟩|² / (E_n^(0) − E_k^(0)) has a negative denominator: since the ground state has the lowest energy, E_n^(0) < E_k^(0) for all k ≠ n, making every denominator E_n^(0) − E_k^(0) < 0. The numerator |⟨k|H'|n⟩|² is always non-negative. Therefore every term is non-positive, and the total sum is negative (or zero if the perturbation has no off-diagonal matrix elements). A positive second-order ground-state correction is impossible — any such result indicates a computational error."

- question: "Two neutral atoms with no permanent electric dipoles exhibit a weak attractive interaction proportional to −C/r⁶. At what order of perturbation theory does this London dispersion force first appear, and why not at lower order?"
  type: multiple-choice
  options:
    - "Zeroth order — it is a direct classical electrostatic effect between the electron distributions"
    - "First order — the dipole-dipole interaction Hamiltonian gives a first-order energy correction"
    - "Second order — the first-order correction averages to zero because the atoms have no permanent dipoles, but second-order terms capture virtual excitations that create and destroy induced dipoles"
    - "Third order — dipole-dipole coupling is too weak to appear at second order"
  answer: 2
  explanation: "The perturbation here is the dipole-dipole interaction between the two atoms. At first order, E_n^(1) = ⟨n|H'|n⟩ — the expectation value of the dipole-dipole interaction in the unperturbed ground state. Since the atoms have no permanent dipoles, this expectation value averages to zero over all orientations (the ground state has no preferred dipole orientation). At second order, however, the perturbation mixes in excited states with non-zero dipole matrix elements. These 'virtual excitations' create temporary induced dipoles that attract, giving a net second-order energy shift proportional to −C/r⁶. The van der Waals force is genuinely a second-order quantum effect."

- question: "Second-order perturbation theory is only needed when the first-order energy correction E_n^(1) = ⟨n|H'|n⟩ is exactly zero."
  type: true-false
  answer: false
  explanation: "Second-order perturbation theory captures corrections that are of order (H')² — a systematically smaller contribution than the first-order (H')¹ term. You may need it even when the first-order correction is nonzero, if you want a more accurate approximation. More commonly, it is *most crucial* when the first-order correction happens to be zero (as for the van der Waals force), since in that case second order gives the leading nonzero correction. But 'needing' second order does not require first order to vanish — it depends on the required precision."

- question: "For an excited state (not the ground state), the second-order energy correction can be either positive or negative depending on the perturbation and the energy spectrum."
  type: true-false
  answer: true
  explanation: "For an excited state with energy E_n^(0), some states |k⟩ have E_k^(0) > E_n^(0) (higher excited states), giving negative denominators and negative contributions; other states have E_k^(0) < E_n^(0) (lower states including the ground state), giving positive denominators and positive contributions. The total sign of E_n^(2) therefore depends on which contributions dominate — determined by the matrix elements ⟨k|H'|n⟩ and the energy gaps. Only for the ground state is the sign guaranteed (always negative), because no state is lower in energy."

- question: "Explain the physical picture of 'virtual transitions' that underlies the second-order energy correction formula. Why do states close in energy to the perturbed state contribute more to the correction than distant states?"
  type: short-answer
  answer: "In the second-order picture, the perturbation H' can temporarily mix state |n⟩ with other eigenstates |k⟩. Even if this mixing does not produce a permanent transition (H' is not strong enough to permanently change the state), the transient mixing shifts the energy. This temporary excursion to state |k⟩ and back is called a 'virtual transition.' The energy cost of this excursion is the gap |E_n^(0) − E_k^(0)|, which appears in the denominator of E_n^(2) = Σ_{k≠n} |⟨k|H'|n⟩|² / (E_n^(0) − E_k^(0)). States close in energy have small denominators, making their contribution large; states far away have large denominators that suppress their contribution. The formula encodes the intuition that 'cheap' virtual transitions (small energy gap to borrow) have the largest effect."
  explanation: "The energy-denominator structure is central to many quantum mechanical phenomena beyond perturbation theory. It appears in Fermi's golden rule, in the derivation of effective Hamiltonians, and in the renormalization of physical quantities by virtual processes in quantum field theory. The key insight is always the same: coupling to nearby states is energetically cheap and therefore large; coupling to distant states is energetically costly and therefore small."
```

## Explainer

In first-order perturbation theory, you learned to compute the leading correction to an energy level: E_n^(1) = ⟨n|H'|n⟩, the expectation value of the perturbation in the unperturbed state. This works well when H' has a nonzero diagonal matrix element. But sometimes the first-order correction vanishes — the perturbation has no direct overlap with the state — and you need to go deeper. **Second-order perturbation theory** captures the next layer of correction by accounting for how the perturbation can mix the state of interest with all other eigenstates.

The physical picture is that of **virtual transitions**. Even if H' cannot directly shift state |n⟩, it can temporarily mix |n⟩ with neighboring states |k⟩, borrowing energy from those states and then returning to |n⟩. The second-order energy correction is E_n^(2) = Σ_{k≠n} |⟨k|H'|n⟩|² / (E_n^(0) − E_k^(0)). Each term in this sum represents one such virtual excursion: the numerator |⟨k|H'|n⟩|² measures how strongly H' couples state |n⟩ to state |k⟩, and the denominator is the energy gap that must be "borrowed" to reach |k⟩. States close in energy contribute more; states far away contribute negligibly.

An important structural feature: for the **ground state**, all denominator terms are negative (since E_n^(0) < E_k^(0) for all k), so every term in the sum is negative. The ground state always shifts downward at second order. Intuitively, this makes sense: the perturbation provides additional ways for the system to lower its energy by mixing in other states. This is a general quantum mechanical principle — perturbations always push the ground state down (at second order). For excited states, some denominators are positive and some negative, so the sign of E_n^(2) is not guaranteed.

A canonical application is the **van der Waals force** between two neutral atoms. At first order, the dipole-dipole interaction averages to zero because the atoms have no permanent dipoles. But at second order, the perturbation mixes in excited states with non-zero dipoles. The result is an attractive energy that falls off as −C/r⁶ — the London dispersion force. This is an entirely second-order quantum effect: it vanishes at first order and requires the full summation over intermediate states. The same formalism underlies the polarizability of atoms (the susceptibility of an atom to an applied electric field) and the Lamb shift in atomic hydrogen, where virtual photon emissions cause tiny but measurable energy corrections.
