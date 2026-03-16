---
id: configuration-interaction-methods
title: Configuration Interaction and Wavefunction Expansion
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-orbital-diagrams-and-bonding
  type: hard
- id: perturbation-theory-quantum-chemistry
  type: hard
builds-toward:
- time-dependent-dft-excited-states
tags:
- quantum
- wavefunction
- excited-states
- computational
stage: advanced
status: draft
---

# Configuration Interaction and Wavefunction Expansion

## Core Idea
Configuration Interaction (CI) expands the wavefunction as a linear combination of Slater determinants (electron configurations), allowing systematic recovery of electron correlation. CIS (Configuration Interaction Singles) captures single excitations and models excited states; CISD and higher add double and triple excitations for ground-state correlation. The method is exact in the complete limit (FCI) but computationally expensive for larger systems.

## How It's Best Learned
Implement a CIS calculation manually for He or H₂; examine the relative weights of Slater determinants in the CI expansion; compare CIS excitation energies to experiment for small molecules; explain size consistency issues in truncated CI.

## Common Misconceptions
- Assuming truncated CI (CIS, CISD) gives smooth convergence to FCI results; size-consistency errors cause problems for larger systems. - Treating CIS as superior to perturbation theory for excited states; CIS omits double excitations, causing overestimation of excitation energies.

## Explainer

From molecular orbital theory, you know that solving the Schrödinger equation for a molecule yields a set of molecular orbitals, and electrons fill these orbitals to produce a ground-state electron configuration — typically represented as a single **Slater determinant** (an antisymmetrized product of one-electron wavefunctions). From perturbation theory, you know that approximate solutions can be systematically improved by adding corrections. Configuration Interaction (CI) combines both ideas: it improves the wavefunction by mixing in excited-state configurations, treating the ground-state determinant as a starting point and building a better answer from a linear combination of many determinants.

The physical motivation is **electron correlation**. The Hartree-Fock method treats each electron as moving in the average field of all others, but real electrons actively avoid each other instant by instant. This correlated motion lowers the energy below the Hartree-Fock prediction. CI captures this effect by constructing excited configurations — determinants where one or more electrons have been promoted from occupied to virtual (unoccupied) orbitals — and mixing them with the ground-state determinant. The wavefunction becomes Ψ = c₀Φ₀ + c₁Φ₁ + c₂Φ₂ + ..., where each Φ is a different electron configuration and the coefficients c are determined by minimizing the energy. The more configurations you include, the more correlation you recover.

In practice, CI is organized by **excitation level**. CIS (singles only) promotes one electron at a time and is primarily used for excited-state calculations — it does not improve the ground-state energy because of Brillouin's theorem. CISD (singles and doubles) adds double excitations and captures most of the ground-state correlation energy. CISDT, CISDTQ, and so on include ever-higher excitations. **Full CI (FCI)** — including all possible excitations within the basis set — gives the exact answer for that basis, but the number of determinants grows factorially with system size, making FCI feasible only for the smallest molecules.

A critical limitation of truncated CI is the **size-consistency problem**. If you calculate two non-interacting hydrogen molecules separately with CISD and then calculate the combined four-electron system with CISD, the energies do not add up correctly. This happens because doubles for the combined system include some excitations that are quadruples relative to the individual molecules — excitations that CISD excludes. This error grows with system size, making truncated CI less reliable for large molecules. Methods like coupled-cluster theory were developed partly to fix this problem while retaining the systematic improvability that makes CI conceptually appealing.
