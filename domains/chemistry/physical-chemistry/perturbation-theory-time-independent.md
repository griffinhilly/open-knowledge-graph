---
id: perturbation-theory-time-independent
title: Time-Independent Perturbation Theory
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: variational-method-ground-state
  type: soft
builds-toward:
- spin-orbit-coupling-fine-structure
- nmr-second-order-effects
tags:
- perturbation-theory
- approximation-methods
- quantum-mechanics
stage: advanced
status: draft
---

# Time-Independent Perturbation Theory

## Core Idea
Perturbation theory expresses corrections to energy and wave functions as a series in the perturbation strength. For weak perturbations, first-order corrections usually suffice; higher orders provide increasingly accurate results. The method applies when the system is close to a solvable reference case and builds corrections from the known solution.

## Questions

```yaml
- question: "What information is required to calculate the first-order energy correction for a non-degenerate energy level?"
  type: multiple-choice
  options:
    - "The exact perturbed wave function of the state, obtained by solving the full Schrödinger equation"
    - "The unperturbed wave function of the state and the perturbation operator H'"
    - "All other unperturbed wave functions in addition to the state of interest"
    - "The second-order correction must be computed before the first-order correction is accessible"
  answer: 1
  explanation: "The first-order energy correction is E⁽¹⁾ = ⟨ψ⁽⁰⁾|H'|ψ⁽⁰⁾⟩ — an expectation value of the perturbation operator computed using only the unperturbed wave function for that state. You do not need to solve a new differential equation or know any other states. This is the remarkable economy of the method: you reuse the solution you already have to estimate how much the energy shifts. Options C and D describe what is needed for the first-order wave function correction (C) or higher-order energy corrections — not the first-order energy correction itself."

- question: "A student applies standard perturbation theory to a system where two unperturbed energy levels are separated by a gap much smaller than the perturbation strength. What problem arises?"
  type: multiple-choice
  options:
    - "The perturbation series converges faster when levels are close, making first-order corrections exact"
    - "The energy denominators in the wave function correction terms become very large, causing the expansion to blow up and become unreliable"
    - "The zeroth-order wave functions for close-lying levels become non-orthogonal, violating the method's assumptions"
    - "The expectation value ⟨ψ⁽⁰⁾|H'|ψ⁽⁰⁾⟩ becomes imaginary when energy gaps are small"
  answer: 1
  explanation: "The first-order wave function correction involves a sum over all other states with terms proportional to ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ / (Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾). When two levels are nearly degenerate (Eₙ ≈ Eₖ), the denominator approaches zero and the correction term diverges — the series breaks down. This is why degenerate perturbation theory must be used instead, diagonalizing H' within the degenerate subspace before applying the standard expansion."

- question: "To apply first-order perturbation theory, you must solve the full perturbed Schrödinger equation to obtain corrected wave functions before computing energy corrections."
  type: true-false
  answer: false
  explanation: "This is exactly what perturbation theory avoids. The first-order energy correction E⁽¹⁾ = ⟨ψ⁽⁰⁾|H'|ψ⁽⁰⁾⟩ uses only the unperturbed wave function — no new differential equation is solved. You compute an integral using the solution you already know. This is the central practical value of perturbation theory: you can estimate energy shifts without solving an intractable new problem, as long as the perturbation is genuinely small."

- question: "Perturbation theory gives more reliable results when the perturbation H' is large relative to the spacing between unperturbed energy levels."
  type: true-false
  answer: false
  explanation: "The opposite is true. Perturbation theory is a power series in the perturbation strength; it converges only when the perturbation is small. The critical condition is that the perturbation must be small compared to the energy gaps between levels — specifically, the matrix elements ⟨ψₖ⁽⁰⁾|H'|ψₙ⁽⁰⁾⟩ must be small compared to |Eₙ⁽⁰⁾ − Eₖ⁽⁰⁾|. When levels are nearly degenerate or the perturbation is large, the expansion fails and other methods (degenerate perturbation theory or variational methods) must be used."

- question: "Explain in physical terms what the first-order energy correction ⟨ψ⁽⁰⁾|H'|ψ⁽⁰⁾⟩ is calculating, and why using the unperturbed wave function is justified."
  type: short-answer
  answer: "The first-order energy correction is the average value of the perturbation experienced by the particle as if it were still in its unperturbed state. Because the perturbation is small, the wave function changes only slightly — to first order, the particle still occupies the unperturbed orbital, so computing the expectation value of H' with that orbital is a good approximation to the true energy shift. The correction captures how much energy the perturbation adds 'on average' given the existing probability distribution."
  explanation: "This physical interpretation matters because it shows why the method works: if the perturbation is small, the state barely changes, so the unperturbed wave function is a good proxy for the true state when computing the average perturbation energy. The analogy is a guitar string tuned slightly off — you can estimate the frequency shift from the change in tension without re-deriving the physics of wave propagation. Higher-order corrections account for the fact that the wave function itself deforms in response to the perturbation, which matters progressively more as the perturbation grows."
```

## Explainer

From your work on quantum chemistry foundations, you know that exact solutions to the Schrödinger equation exist only for a handful of idealized systems — the particle in a box, the harmonic oscillator, the hydrogen atom. Every real chemical system involves complications (electron-electron repulsion, external fields, anharmonicity) that make exact solutions impossible. **Time-independent perturbation theory** provides a systematic way to handle these complications when they are small compared to the solvable part of the problem. The core idea is to split the full Hamiltonian into a solvable piece H₀ (whose eigenstates and energies you already know) plus a small perturbation λH', where λ is a dimensionless parameter tracking the strength of the disturbance.

The method works by expanding the true energies and wave functions as power series in λ. The **zeroth-order** terms are just the unperturbed solutions you already have. The **first-order energy correction** turns out to be remarkably simple: it is just the expectation value of the perturbation H' calculated using the unperturbed wave function, E⁽¹⁾ = ⟨ψ⁽⁰⁾|H'|ψ⁽⁰⁾⟩. This means you can estimate how much an energy level shifts without ever solving a new differential equation — you just evaluate an integral using the solutions you already know. The first-order wave function correction is more involved, requiring a sum over all other unperturbed states, weighted by how strongly H' mixes them and inversely weighted by the energy gap between states.

A helpful analogy is tuning a guitar string. The unperturbed system is the string vibrating at its natural frequency. A small perturbation — say, slightly changing the tension — shifts the frequency by an amount proportional to the perturbation strength. You do not need to re-derive the physics of vibrating strings; you just calculate how the existing solution responds to the change. Similarly, perturbation theory lets you correct hydrogen-atom solutions to account for effects like spin-orbit coupling or an applied electric field (the Stark effect) without starting from scratch.

The method has a critical limitation: it fails when two unperturbed states are very close in energy (or exactly degenerate), because the energy denominators in the correction terms blow up. This is where **degenerate perturbation theory** takes over, requiring you to first diagonalize H' within the degenerate subspace before applying the standard corrections. If you have encountered the variational method, you can appreciate the complementary nature of these approaches: the variational method gives rigorous upper bounds on energies but requires guessing a trial function, while perturbation theory gives systematic corrections order by order but demands that the perturbation be genuinely small. In practice, chemists use both — perturbation theory for understanding trends and analytical insight, variational methods for high-accuracy numerical calculations.
