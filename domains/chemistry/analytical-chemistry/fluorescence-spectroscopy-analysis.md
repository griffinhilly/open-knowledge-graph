---
id: fluorescence-spectroscopy-analysis
title: Fluorescence Spectroscopy for Quantitative Analysis
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: fluorescence-spectroscopy
  type: hard
- id: electronic-transitions-excited-states
  type: soft
- id: photon-concept-quanta
  type: soft
tags:
- fluorescence
- luminescence
- quantitative
stage: advanced
status: draft
---

# Fluorescence Spectroscopy for Quantitative Analysis

## Core Idea
Fluorescence measurements detect photon emission following light absorption and non-radiative relaxation to excited electronic states. This method offers excellent selectivity and sensitivity, with intensity proportional to analyte concentration under ideal conditions.

## Explainer

From your study of fluorescence spectroscopy and electronic transitions, you understand the physical process: a molecule absorbs a photon, reaches an excited electronic state, loses some energy through vibrational relaxation, and then emits a lower-energy photon as it returns to the ground state. The emitted photon always has a longer wavelength than the absorbed one — this wavelength difference is the **Stokes shift**. What makes fluorescence so powerful for quantitative analysis is that you measure the emitted light against a dark background (at a different wavelength and usually at 90° to the excitation beam), rather than measuring a small decrease in a bright beam as in absorbance spectroscopy. This is why fluorescence can detect analytes at concentrations 100 to 1000 times lower than UV-Vis absorption — you are counting photons above zero rather than measuring a tiny difference between two large numbers.

The fundamental quantitative relationship for dilute solutions is F = ΦF · I₀ · ε · b · c, where F is fluorescence intensity, ΦF is the **quantum yield** (fraction of absorbed photons that produce fluorescence), I₀ is the excitation intensity, ε is the molar absorptivity, b is the path length, and c is the concentration. At low concentrations, fluorescence intensity is directly proportional to concentration — a linear calibration. However, at high concentrations, the **inner filter effect** causes the excitation beam to be significantly attenuated before it reaches the center of the cuvette, and emitted photons may be reabsorbed, so the linear relationship breaks down and the calibration curve bends or even decreases. Keeping absorbance below about 0.05 AU at the excitation wavelength avoids this problem.

Selectivity in fluorescence comes from two independent wavelength selections: you choose both the **excitation wavelength** and the **emission wavelength**, so only compounds that absorb at the first and emit at the second are detected. Most molecules are not fluorescent — they lose excited-state energy through non-radiative pathways instead — so the technique is inherently selective for compounds with rigid, conjugated aromatic structures. Compounds that are not naturally fluorescent can often be made so through **derivatization**, where a fluorescent tag is chemically attached before measurement. This is widely used in HPLC with fluorescence detection for amino acids, drugs, and environmental pollutants.

Several factors can reduce fluorescence intensity and must be controlled for accurate quantitation. **Quenching** occurs when other molecules in solution deactivate the excited state through collisions (dynamic quenching) or complex formation (static quenching). Dissolved oxygen is a common quencher and is sometimes removed by purging with nitrogen. Temperature increases generally decrease fluorescence because vibrational relaxation becomes more competitive. Solvent polarity, pH, and the presence of heavy atoms also affect quantum yield. A well-designed fluorescence method accounts for these variables through careful standardization, matrix matching, and — when possible — the use of internal standards to correct for quenching and matrix effects.
