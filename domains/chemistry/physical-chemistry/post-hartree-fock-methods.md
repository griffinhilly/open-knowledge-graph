---
id: post-hartree-fock-methods
title: 'Post-Hartree-Fock Methods: MP and CC Theory'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: hartree-fock-method
  type: hard
- id: perturbation-theory-quantum-chemistry
  type: hard
builds-toward:
- configuration-interaction-methods
- time-dependent-dft-excited-states
tags:
- quantum
- electron-correlation
- computational
- wavefunction
stage: advanced
status: draft
---

# Post-Hartree-Fock Methods: MP and CC Theory

## Core Idea
Møller-Plesset (MP) perturbation theory and Coupled Cluster (CC) theory systematically account for electron correlation beyond Hartree-Fock. MP2 and CCSD(T) are industry-standard methods that provide qualitatively and quantitatively improved predictions for energies, geometries, and properties. Coupled cluster theory, based on an exponential ansatz, is particularly robust and defines the 'gold standard' of single-reference quantum chemistry.

## How It's Best Learned
Compare Hartree-Fock, MP2, and CCSD(T) calculations for a series of molecules (closed-shell and open-shell); track computational time and accuracy against experimental thermochemistry; examine how correlation energy depends on molecular size and electron density.

## Common Misconceptions
- Thinking CCSD(T) is ab initio 'exact'; it is still an approximation that neglects higher excitations. - Assuming larger basis sets always improve CC results; basis set incompleteness and missing physics (relativity, QED) also matter.
