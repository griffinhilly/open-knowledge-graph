---
id: bose-einstein-condensation-statmech
title: Bose-Einstein Condensation and Order Parameter
domain: physics
course: statistical-mechanics
prerequisites:
- id: bose-gas-ideal-quantum
  type: hard
- id: order-parameter-phase-transition
  type: soft
builds-toward:
- phase-transition-equilibrium
- spontaneous-symmetry-breaking
tags:
- condensation
- order-parameter
- spontaneous-order
stage: advanced
status: draft
---

# Bose-Einstein Condensation and Order Parameter

## Core Idea
Below the critical temperature, a macroscopic number of bosons occupy the ground state, and the system acquires a non-zero order parameter: the condensate wavefunction ψ. This spontaneous breaking of gauge symmetry is the hallmark of a quantum phase transition and manifests in phenomena like superfluidity.

## Explainer

From your study of the ideal Bose gas, you know that bosons do not obey the Pauli exclusion principle — any number of them can occupy the same single-particle quantum state. The Bose-Einstein distribution nₖ = 1/(exp((εₖ − μ)/kT) − 1) describes the average occupation. For the chemical potential to remain negative (so that occupation numbers stay positive), μ must satisfy μ < ε₀ = 0 (the ground state energy). As temperature decreases, μ increases toward zero. At the **critical temperature** Tc, μ hits zero — and the ground state occupation n₀ = 1/(exp(−μ/kT) − 1) becomes macroscopic. Below Tc, a finite fraction of all N particles pile into the ground state. This macroscopic ground state occupation is **Bose-Einstein condensation**.

The phrase "macroscopic occupation" is key. In a normal gas at temperature T, each single-particle state has of order 1 particle on average (or much less). In the condensate, the ground state has of order N particles — a number proportional to the system size. This is a qualitative distinction. You can estimate Tc from the condition that the thermal de Broglie wavelength λ_dB becomes comparable to the interparticle spacing: nλ_dB³ ≈ 2.612. When particles are close enough together that their wavefunctions overlap significantly, they "feel" the bosonic statistics and begin to collectively pile up.

The connection to your prerequisite on **order parameters** is subtle but important. In a standard phase transition, the order parameter is a classical object (average magnetization, average density difference). For BEC, the **condensate wavefunction** ψ = √(n₀) e^(iφ) plays this role — it is a complex number, with both a magnitude (the square root of condensate density) and a phase φ. Above Tc, ψ = 0. Below Tc, ψ ≠ 0 and a definite phase is chosen, spontaneously breaking the U(1) gauge symmetry (the symmetry ψ → e^(iα)ψ). This is a quantum phase transition: the order parameter is literally a quantum mechanical wavefunction that has become macroscopic.

The physical consequences are dramatic. When a macroscopic number of particles share the same quantum state, they also share the same phase — they are **phase coherent**. This coherence is what enables **superfluidity**: the condensate flows without viscosity because there is no mechanism to scatter it into a different phase-coherent state without paying a large energy cost. The same physics appears in superconductivity (where Cooper pairs of electrons condense) and in laser light (photons in a coherent state). Bose-Einstein condensation was first achieved experimentally in ultracold atomic gases in 1995, confirming predictions made by Einstein in 1924, and has since become a leading platform for studying quantum many-body physics in controlled laboratory settings.
