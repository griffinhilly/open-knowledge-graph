---
id: cross-sections-decay-rates
title: Cross Sections and Decay Rates
domain: physics
course: quantum-field-theory
prerequisites:
- id: s-matrix-scattering-amplitudes
  type: hard
tags:
- cross-section
- decay-rate
- phase-space
stage: expert
status: validated
---

# Cross Sections and Decay Rates

## Core Idea
Cross sections and decay rates are the measurable quantities extracted from S-matrix elements. The differential cross section is proportional to |M|^2 times the phase space available to the final-state particles. Decay rates follow the same structure but for a single initial particle at rest. Fermi's golden rule is the non-relativistic limit of these formulas.

## Questions

```yaml
- question: "The cross section formula contains a factor of Lorentz-invariant phase space (LIPS) for the final state. What does this factor represent physically?"
  type: multiple-choice
  options:
    - "The density of available final states consistent with energy-momentum conservation — more available states means higher probability of the transition"
    - "The Lorentz contraction of the target particle"
    - "The quantum interference between different final states"
    - "The normalization of the initial-state wave functions"
  answer: 0
  explanation: "Phase space is the volume of momentum space accessible to the final-state particles, weighted by the relativistic density of states and subject to the constraint of total energy-momentum conservation. A process with more available final states (more phase space) has a higher rate, even if |M|^2 is the same. This is why heavy particles have more decay channels and higher total decay rates than light particles — more final states become kinematically accessible as the mass increases. Phase space also explains why three-body decays are typically slower than two-body decays: the phase space integration is more restrictive."

- question: "Two processes have the same |M|^2 but different final-state multiplicities. Process A produces 2 final particles; process B produces 4. Which has the larger phase space, and why?"
  type: multiple-choice
  options:
    - "Process B, because more particles always means more phase space"
    - "Process A, because each additional particle introduces a factor of (2pi)^{-3} and a mass-shell delta function, which restricts the available phase space despite adding more degrees of freedom"
    - "They have equal phase space because |M|^2 is the same"
    - "It depends entirely on the masses of the final-state particles"
  answer: 3
  explanation: "The comparison depends on the kinematics — specifically, the masses of the final-state particles relative to the total available energy. Each additional particle adds three momentum components but also adds an on-shell constraint and a factor of 1/(2E_i). If the total energy is much larger than the sum of final-state masses, adding particles can increase the phase space volume. If the energy is barely enough to produce all particles, phase space is severely restricted. There is no universal rule — the specific masses and total energy determine the outcome."

- question: "The lifetime of an unstable particle is the inverse of its total decay rate: tau = 1/Gamma_total, where Gamma_total is the sum of partial decay rates to all kinematically allowed channels."
  type: true-false
  answer: true
  explanation: "Each decay channel i has a partial decay rate Gamma_i computed from |M_i|^2 integrated over phase space. The total decay rate is Gamma_total = sum of all Gamma_i. The lifetime is tau = hbar/Gamma_total (or 1/Gamma_total in natural units). The branching ratio for channel i is BR_i = Gamma_i/Gamma_total. This means that adding new decay channels (for example, by increasing the particle's mass so that heavier final states become accessible) increases Gamma_total and decreases the lifetime."

- question: "Derive the formula for the two-body decay rate of a particle of mass M decaying into two particles of masses m1 and m2, and explain the role of each factor."
  type: short-answer
  answer: "In the rest frame of the decaying particle, Gamma = |p_f|/(8 pi M^2) |M|^2, where |p_f| = (1/2M)sqrt{[M^2-(m1+m2)^2][M^2-(m1-m2)^2]} is the magnitude of the final-state momentum. The factor |M|^2 encodes the dynamics (the interaction strength and structure). The factor |p_f| comes from the phase space — it vanishes at threshold (M = m1 + m2), where the decay products have zero kinetic energy, and grows as M increases. The factor 1/(8 pi M^2) combines the normalization conventions and the phase space measure. For a spin-averaged decay, an additional factor of 1/(2J+1) averages over the initial spin states."
  explanation: "This formula is the workhorse for computing particle lifetimes. It separates the dynamics (|M|^2, computed from Feynman diagrams) from the kinematics (phase space factors). The threshold behavior |p_f| -> 0 as M -> m1 + m2 is universal and explains why particles just barely above threshold decay slowly, while highly off-shell decays proceed rapidly."
```

## Explainer

The S-matrix gives probability amplitudes, but experiments measure **cross sections** (for scattering) and **decay rates** (for unstable particles). Converting amplitudes to observables requires squaring the amplitude, summing over unobserved final-state quantum numbers (spins, colors), averaging over initial-state quantum numbers, and integrating over the phase space of the final-state particles. The differential cross section for 2 -> n scattering is d sigma = (1 / 4E_a E_b |v_a - v_b|) |M|^2 d(LIPS_n), where LIPS_n is the n-body Lorentz-invariant phase space.

**Phase space** measures the density of available final states. For n final-state particles, it is d(LIPS_n) = product over final particles of [d^3p_i / ((2pi)^3 2E_i)] times (2pi)^4 delta^4(p_initial - sum p_i). The delta function enforces energy-momentum conservation, which constrains the final momenta. For a 2 -> 2 process in the center-of-mass frame, the phase space reduces to an integral over the scattering angle, giving d sigma/d Omega = |M|^2 / (64 pi^2 s), where s is the center-of-mass energy squared.

**Decay rates** have the same structure but with a single initial particle. For a particle of mass M at rest decaying into n particles, Gamma = (1/2M) integral |M|^2 d(LIPS_n). The lifetime is tau = 1/Gamma_total. The total width Gamma_total has a direct physical interpretation: it determines the width of the resonance peak in the invariant mass distribution via the Breit-Wigner formula, sigma ~ 1/[(s - M^2)^2 + M^2 Gamma^2]. A short-lived particle has a broad resonance; a long-lived particle has a narrow one. This is the energy-time uncertainty relation made precise.

These formulas connect the theoretical output of quantum field theory (the amplitude M computed from Feynman diagrams) to the experimental input (measured cross sections and lifetimes). The separation into dynamics (|M|^2) and kinematics (phase space) is clean and universal. The same phase-space formulas apply regardless of the underlying theory -- QED, QCD, or the full Standard Model. All the theory-specific physics is encoded in the invariant amplitude M.
