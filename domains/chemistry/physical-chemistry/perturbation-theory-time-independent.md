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

## Explainer

From your work on quantum chemistry foundations, you know that exact solutions to the Schrödinger equation exist only for a handful of idealized systems — the particle in a box, the harmonic oscillator, the hydrogen atom. Every real chemical system involves complications (electron-electron repulsion, external fields, anharmonicity) that make exact solutions impossible. **Time-independent perturbation theory** provides a systematic way to handle these complications when they are small compared to the solvable part of the problem. The core idea is to split the full Hamiltonian into a solvable piece H₀ (whose eigenstates and energies you already know) plus a small perturbation λH', where λ is a dimensionless parameter tracking the strength of the disturbance.

The method works by expanding the true energies and wave functions as power series in λ. The **zeroth-order** terms are just the unperturbed solutions you already have. The **first-order energy correction** turns out to be remarkably simple: it is just the expectation value of the perturbation H' calculated using the unperturbed wave function, E⁽¹⁾ = ⟨ψ⁽⁰⁾|H'|ψ⁽⁰⁾⟩. This means you can estimate how much an energy level shifts without ever solving a new differential equation — you just evaluate an integral using the solutions you already know. The first-order wave function correction is more involved, requiring a sum over all other unperturbed states, weighted by how strongly H' mixes them and inversely weighted by the energy gap between states.

A helpful analogy is tuning a guitar string. The unperturbed system is the string vibrating at its natural frequency. A small perturbation — say, slightly changing the tension — shifts the frequency by an amount proportional to the perturbation strength. You do not need to re-derive the physics of vibrating strings; you just calculate how the existing solution responds to the change. Similarly, perturbation theory lets you correct hydrogen-atom solutions to account for effects like spin-orbit coupling or an applied electric field (the Stark effect) without starting from scratch.

The method has a critical limitation: it fails when two unperturbed states are very close in energy (or exactly degenerate), because the energy denominators in the correction terms blow up. This is where **degenerate perturbation theory** takes over, requiring you to first diagonalize H' within the degenerate subspace before applying the standard corrections. If you have encountered the variational method, you can appreciate the complementary nature of these approaches: the variational method gives rigorous upper bounds on energies but requires guessing a trial function, while perturbation theory gives systematic corrections order by order but demands that the perturbation be genuinely small. In practice, chemists use both — perturbation theory for understanding trends and analytical insight, variational methods for high-accuracy numerical calculations.
