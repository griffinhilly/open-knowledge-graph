---
id: time-dependent-dft-excited-states
title: Time-Dependent DFT for Excited States
domain: chemistry
course: physical-chemistry
prerequisites:
- id: density-functional-theory-intro
  type: hard
- id: electronic-spectroscopy-theory
  type: soft
builds-toward:
- selection-rules-electronic-spectroscopy
tags:
- spectroscopy
- excited-states
- dft
- computational
stage: advanced
status: draft
---

# Time-Dependent DFT for Excited States

## Core Idea
Time-Dependent DFT (TDDFT) extends density functional theory to time-dependent perturbations and excited states by introducing the time-dependent density and linear response theory. TDDFT efficiently predicts excitation energies and oscillator strengths for electronic transitions without explicitly constructing excited-state wavefunctions. It balances computational cost and accuracy, making it practical for large molecules.

## How It's Best Learned
Calculate UV-Vis absorption spectra using TDDFT for organic dyes and proteins; compare results to experimental λmax and intensity; test different functionals (PBE, CAM-B3LYP, ωB97X) to understand how exchange admixture affects charge-transfer states.

## Common Misconceptions
- Assuming TDDFT is as reliable for charge-transfer states as for local excitations; standard functionals underestimate CT excitation energies due to insufficient long-range exchange. - Treating the TDDFT excitation energy as a true excited-state energy; it is an excitation energy from the ground state, not an absolute energy.

## Explainer

Standard density functional theory, which you already know, is fundamentally a ground-state theory — the Hohenberg-Kohn theorems guarantee that the ground-state electron density determines all ground-state properties. But chemistry and spectroscopy constantly demand information about excited states: What wavelength of light does a molecule absorb? What color does a dye appear? How does a photoreceptor protein respond to light? **Time-Dependent DFT (TDDFT)** extends the DFT framework to answer these questions without abandoning the computational efficiency that makes DFT practical for large molecules.

The theoretical foundation is the **Runge-Gross theorem**, the time-dependent analog of the Hohenberg-Kohn theorem. It establishes that the time-dependent external potential is uniquely determined by the time-dependent electron density (up to a trivial additive function of time). This means we can, in principle, track how the electron density evolves under a perturbation — like an oscillating electric field from a light wave — using time-dependent Kohn-Sham equations. In practice, we rarely solve the full time-dependent equations. Instead, **linear response TDDFT** asks a simpler question: if we apply an infinitesimally small perturbation to the ground state, at what frequencies does the density oscillate in response? These resonant frequencies correspond to electronic excitation energies, and their intensities give **oscillator strengths** that predict absorption spectra.

The linear response calculation reduces to solving the **Casida equations**, an eigenvalue problem built from the ground-state Kohn-Sham orbitals and a coupling matrix that depends on the exchange-correlation functional. Each eigenvalue gives an excitation energy, and the eigenvectors describe which orbital transitions contribute to each excited state. The beauty of this approach is that it requires only the ground-state Kohn-Sham calculation as input, plus one matrix diagonalization — far cheaper than wavefunction-based excited-state methods like equation-of-motion coupled cluster or multireference configuration interaction.

The choice of exchange-correlation functional matters more for TDDFT than for ground-state DFT. Local and semilocal functionals (LDA, GGA) work reasonably well for **valence excitations** — transitions where the excited electron stays near its original location. But for **charge-transfer excitations**, where electron density moves a significant distance across the molecule, these functionals dramatically underestimate excitation energies. The problem traces to the self-interaction error in approximate functionals, which fails to penalize long-range charge separation correctly. **Range-separated hybrid functionals** like CAM-B3LYP and ωB97X fix this by including increasing amounts of exact Hartree-Fock exchange at long range. Choosing the right functional for your system is arguably the most important practical decision in TDDFT calculations, and validating against experimental spectra or higher-level theory should always be part of the workflow.
