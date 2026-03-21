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

## Questions

```yaml
- question: "Two non-interacting H₂ molecules are each calculated with CISD, giving energy E per molecule. The combined H₄ system (two H₂ molecules far apart) is also calculated with CISD, but the total energy is less negative than 2E. What causes this discrepancy?"
  type: multiple-choice
  options:
    - "CISD cannot correctly handle more than two electrons and breaks down for H₄"
    - "The larger basis set needed for H₄ introduces errors not present in individual H₂ calculations"
    - "CISD is size-inconsistent: some excitations in the combined H₄ system are quadruple excitations relative to the ground state, which CISD excludes but which were effectively included as doubles in the separate H₂ calculations"
    - "Long-range electron correlation between the two distant molecules raises the combined energy"
  answer: 2
  explanation: "Size-consistency means that the energy of two non-interacting fragments calculated together must equal the sum of their individual energies. CISD fails this test because 'double excitations' in the individual molecules become 'quadruple excitations' when viewed from the reference determinant of the combined system — and CISD truncates at doubles. This error grows with system size and is why coupled-cluster methods (which are size-consistent) are preferred for large molecules."

- question: "Why does CIS (Configuration Interaction Singles) not improve the ground-state energy compared to Hartree-Fock?"
  type: multiple-choice
  options:
    - "CIS uses too few configurations to make a meaningful energy correction for the ground state"
    - "Brillouin's theorem states that singly-excited determinants have zero matrix element with the HF ground state, so they do not mix in and contribute no first-order energy correction"
    - "CIS is only valid for excited states and cannot be applied to ground-state wavefunctions"
    - "Single excitations change the total spin, making them symmetry-forbidden for the singlet ground state"
  answer: 1
  explanation: "Brillouin's theorem is a fundamental result of Hartree-Fock theory: the Hamiltonian matrix element between the HF ground state and any singly-excited determinant is exactly zero. Consequently, including single excitations in the CI expansion doesn't lower the ground-state energy beyond HF. CIS is therefore used for excited states (where Brillouin's theorem doesn't apply), not for improving ground-state correlation. Double excitations (CISD) are the lowest-level correction that recovers ground-state electron correlation."

- question: "Full CI (FCI) gives the exact energy for a given basis set because it includes all possible electron configurations within that basis."
  type: true-false
  answer: true
  explanation: "FCI is the variational limit of CI within a given one-electron basis set. By including every possible Slater determinant — all combinations of occupied and virtual orbitals — no further configuration can be added to lower the energy. The FCI energy is therefore the exact solution of the electronic Schrödinger equation for that basis (though the basis itself introduces error relative to the true infinite-basis answer)."

- question: "Truncated CI methods like CISD become more accurate for larger molecules because more electron configurations are available to recover correlation energy."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. Truncated CI is size-inconsistent: the fraction of total correlation energy recovered by CISD *decreases* as the molecule grows, because more and more important configurations (effectively doubles for subsystems) become higher-order excitations in the larger system that CISD excludes. This is why FCI — which recovers all correlation — is only feasible for very small systems, and why size-consistent methods like coupled cluster are used for larger molecules."

- question: "What physical phenomenon does the expansion of the wavefunction as a linear combination of Slater determinants in CI capture, and why does the Hartree-Fock single-determinant miss it?"
  type: short-answer
  answer: "CI captures electron correlation — the instantaneous avoidance behavior of electrons that the Hartree-Fock mean-field approximation misses. HF treats each electron as moving in the average field of all others, smoothing out the exact electron-electron repulsion. Real electrons actively avoid each other moment-to-moment, so their actual positions are more correlated (spread apart) than HF predicts, lowering the true energy below the HF limit. By mixing in excited configurations (where electrons occupy virtual orbitals and therefore occupy different regions of space), CI describes configurations in which electrons are farther apart, recovering this correlation energy. The weights of each excited configuration are optimized variationally — configurations that effectively separate electrons from each other get large coefficients."
  explanation: "The energy difference between FCI and HF (for a given basis) is defined as the correlation energy. It ranges from small fractions to tens of kcal/mol depending on the system, and accurately recovering it is essential for calculating bond dissociation energies, reaction barriers, and spectroscopic properties."
```

## Explainer

From molecular orbital theory, you know that solving the Schrödinger equation for a molecule yields a set of molecular orbitals, and electrons fill these orbitals to produce a ground-state electron configuration — typically represented as a single **Slater determinant** (an antisymmetrized product of one-electron wavefunctions). From perturbation theory, you know that approximate solutions can be systematically improved by adding corrections. Configuration Interaction (CI) combines both ideas: it improves the wavefunction by mixing in excited-state configurations, treating the ground-state determinant as a starting point and building a better answer from a linear combination of many determinants.

The physical motivation is **electron correlation**. The Hartree-Fock method treats each electron as moving in the average field of all others, but real electrons actively avoid each other instant by instant. This correlated motion lowers the energy below the Hartree-Fock prediction. CI captures this effect by constructing excited configurations — determinants where one or more electrons have been promoted from occupied to virtual (unoccupied) orbitals — and mixing them with the ground-state determinant. The wavefunction becomes Ψ = c₀Φ₀ + c₁Φ₁ + c₂Φ₂ + ..., where each Φ is a different electron configuration and the coefficients c are determined by minimizing the energy. The more configurations you include, the more correlation you recover.

In practice, CI is organized by **excitation level**. CIS (singles only) promotes one electron at a time and is primarily used for excited-state calculations — it does not improve the ground-state energy because of Brillouin's theorem. CISD (singles and doubles) adds double excitations and captures most of the ground-state correlation energy. CISDT, CISDTQ, and so on include ever-higher excitations. **Full CI (FCI)** — including all possible excitations within the basis set — gives the exact answer for that basis, but the number of determinants grows factorially with system size, making FCI feasible only for the smallest molecules.

A critical limitation of truncated CI is the **size-consistency problem**. If you calculate two non-interacting hydrogen molecules separately with CISD and then calculate the combined four-electron system with CISD, the energies do not add up correctly. This happens because doubles for the combined system include some excitations that are quadruples relative to the individual molecules — excitations that CISD excludes. This error grows with system size, making truncated CI less reliable for large molecules. Methods like coupled-cluster theory were developed partly to fix this problem while retaining the systematic improvability that makes CI conceptually appealing.
