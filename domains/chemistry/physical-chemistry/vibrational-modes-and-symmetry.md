---
id: vibrational-modes-and-symmetry
title: Group Theory and Vibrational Mode Classification
domain: chemistry
course: physical-chemistry
prerequisites:
- id: vibrational-spectroscopy-theory
  type: hard
- id: vsepr-theory
  type: soft
builds-toward:
- electronic-spectroscopy-theory
tags:
- group-theory
- symmetry
- point-groups
- character-tables
- reducible-representations
stage: advanced
status: validated
---

# Group Theory and Vibrational Mode Classification

## Core Idea
Molecular point group symmetry classifies normal modes into irreducible representations using character tables. The reducible representation Γ_total is decomposed using the reduction formula to identify how many modes belong to each symmetry species. IR-active modes must transform as x, y, or z (components of the dipole vector); Raman-active modes must transform as quadratic functions (x², xy, etc.) of the polarizability tensor. This systematic approach predicts the number of IR and Raman peaks without computing wavefunctions, and is essential for interpreting spectra of complex molecules.

## How It's Best Learned
Master the C₂ᵥ and D₂ₕ character tables first. Classify the three modes of water (C₂ᵥ) and the four modes of CO₂ (D∞ₕ), predicting IR/Raman activity and verifying against known spectra.

## Common Misconceptions
- Thinking group theory is only for crystals; it applies to any molecule with symmetry.
- Forgetting to subtract translations (3) and rotations (3 or 2) from Γ_total before identifying vibrational modes.
