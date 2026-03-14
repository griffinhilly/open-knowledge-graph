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
