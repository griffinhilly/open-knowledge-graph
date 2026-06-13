---
id: atomic-structure-basics
title: Atomic Structure
domain: chemistry
course: general-chemistry
prerequisites:
- id: emission-absorption-spectra
  type: soft
builds-toward:
- periodic-table-overview
- electron-configuration
- mole-concept
tags:
- atoms
- subatomic-particles
- isotopes
- atomic-number
- mass-number
stage: formal-systems
status: validated
---

# Atomic Structure

## Core Idea
Atoms consist of a dense nucleus containing protons and neutrons, surrounded by electrons occupying shells at discrete energy levels. The atomic number (number of protons) defines the element's identity, while isotopes of the same element differ only in neutron count. Mass number equals protons plus neutrons, and atomic mass on the periodic table is a weighted average of naturally occurring isotope masses. Understanding atomic structure is the foundation for all of chemistry.

## How It's Best Learned
Build physical intuition using the planetary model as a starting point, then correct it by introducing quantized energy levels. Practice calculating average atomic mass from isotope abundances to connect nuclear structure to observable measurements.

## Common Misconceptions
- Electrons do not orbit the nucleus in fixed circular paths — they occupy probabilistic regions called orbitals.
- Atomic mass on the periodic table is a weighted average of isotope masses, not the mass of a single atom or the mass number of the most abundant isotope.

## Questions

```yaml
- question: "Chlorine has two naturally occurring isotopes: Cl-35 (abundance 75.77%, mass 34.969 u) and Cl-37 (abundance 24.23%, mass 36.966 u). Which value is closest to chlorine's atomic mass on the periodic table?"
  type: multiple-choice
  options: ["35.00 u", "35.45 u", "36.00 u", "36.97 u"]
  answer: 1
  explanation: "Atomic mass = (0.7577)(34.969) + (0.2423)(36.966) ≈ 26.50 + 8.96 ≈ 35.45 u. It is not 35.00 (the mass of the most abundant isotope alone) or 36.00 (a simple average of 35 and 37). The weighted average is pulled toward the more abundant Cl-35, giving approximately 35.45 — which is why the periodic table shows a decimal, not a whole number."

- question: "Electrons in an atom travel in fixed circular orbits around the nucleus, like planets around the sun."
  type: true-false
  answer: false
  explanation: "This describes the Bohr model, which is a useful historical approximation but physically incorrect. Electrons exist in orbitals — three-dimensional probability distributions described by quantum wavefunctions. Their exact positions are fundamentally uncertain; what quantum mechanics defines is the energy level and the probability of finding an electron in a given region of space."

- question: "Two atoms of the same element have different mass numbers. What structural difference accounts for this?"
  type: short-answer
  answer: "They are isotopes — they have the same number of protons (which defines the element) but different numbers of neutrons, resulting in different mass numbers (protons + neutrons)."
  explanation: "Atomic number (proton count) defines which element an atom is; changing the proton count changes the element entirely. Neutrons contribute to mass but not to chemical identity, so atoms with the same proton count but different neutron counts are the same element with different masses. These are called isotopes."
```

## Explainer

Every substance you encounter is built from atoms, and understanding atomic structure unlocks the logic behind nearly all of chemistry. At the center of every atom is the nucleus — an incredibly dense region containing protons and neutrons packed tightly together. Surrounding this nucleus are electrons, which occupy the much larger volume of the atom but contribute almost nothing to its mass (an electron is about 1/1836 the mass of a proton).

The atomic number — the number of protons — is the atom's identity. Change the proton count and you change the element entirely: 6 protons is always carbon, 8 is always oxygen, 79 is always gold. The number of neutrons, however, can vary without changing the element. Atoms of the same element with different neutron counts are called isotopes. Carbon-12 has 6 protons and 6 neutrons (mass number = 12); carbon-14 has 6 protons and 8 neutrons (mass number = 14). They behave nearly identically in chemical reactions because chemistry is governed by electrons, not neutrons — but carbon-14 is radioactive and carbon-12 is stable.

This explains why the atomic mass shown on the periodic table does not match any isotope's mass number exactly. The table shows a weighted average of all naturally occurring isotopes, weighted by their abundance on Earth. Chlorine's atomic mass is approximately 35.45 — between Cl-35 and Cl-37 — because both exist in nature, with Cl-35 accounting for about 76% of natural chlorine. Whenever you see a decimal atomic mass and wonder why it is not a whole number, the answer is isotopic mixing.

A common early model for the atom — the Bohr model — pictures electrons traveling in neat circular orbits like planets around the sun. This picture correctly explains why electrons occupy discrete energy levels and why atoms emit light at specific wavelengths when electrons jump between levels. But electrons do not actually follow defined paths. They occupy orbitals: three-dimensional probability distributions described by quantum mechanics. You cannot say "the electron is here" — only "the electron has a certain probability of being found in this region." The shapes of these orbitals (s, p, d, f) will matter when you study electron configuration and how atoms bond with each other.
