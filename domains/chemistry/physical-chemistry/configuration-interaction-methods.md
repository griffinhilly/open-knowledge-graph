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
