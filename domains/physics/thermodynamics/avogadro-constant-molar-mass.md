---
id: avogadro-constant-molar-mass
title: Avogadro's Number and Molar Mass
domain: physics
course: thermodynamics
prerequisites: []
builds-toward:
- ideal-gas-law
tags:
- atoms
- molecules
- molar-properties
stage: formal-systems
status: draft
---

# Avogadro's Number and Molar Mass

## Core Idea
Avogadro's number (6.022 × 10²³) is the number of molecules in one mole of any substance. The molar mass (in g/mol) numerically equals the molecular mass (in amu). These constants bridge microscopic atomic properties with macroscopic measurable quantities.

## Explainer

Matter is made of atoms, but atoms are fantastically small — a single hydrogen atom has a mass of about 1.67 × 10⁻²⁷ kg. Working with individual atoms would make everyday chemistry impossibly cumbersome. The **mole** is chemistry's accounting unit: one mole is defined as exactly 6.02214076 × 10²³ entities (atoms, molecules, or whatever particle you are counting). This number, **Avogadro's number** N_A, was chosen so that one mole of any element has a mass in grams numerically equal to its atomic mass in atomic mass units (amu). Carbon-12 has an atomic mass of exactly 12 amu, so one mole of carbon-12 weighs exactly 12 grams.

The bridge between microscopic and macroscopic is straightforward: if you know the **molar mass** M (in g/mol) of a substance, then a sample of mass m grams contains n = m/M moles, and therefore N = n × N_A = (m/M) × N_A individual molecules. Going the other way, if you know the mass of one molecule m_molecule (in kg), then M = m_molecule × N_A (converted to g). This is why the atomic mass unit itself is defined as 1 amu = 1 g/mol ÷ N_A ≈ 1.66 × 10⁻²⁷ kg. The numerical equality between atomic mass in amu and molar mass in g/mol is a deliberate design feature, not a coincidence.

For molecules, molar mass is additive: water (H₂O) has two hydrogen atoms (1.008 amu each) and one oxygen (15.999 amu), giving a molar mass of 18.015 g/mol. A 18.015-gram sample of water contains 6.022 × 10²³ water molecules. You can verify this scale directly: a liter of water (1000 g) contains about 55.5 moles × N_A ≈ 3.34 × 10²⁵ molecules — an almost incomprehensibly large number packed into one liter.

This framework will be essential when you study the ideal gas law and other macroscopic thermodynamic relationships. The ideal gas law PV = nRT connects the macroscopic pressure, volume, and temperature of a gas to the number of moles n and the **gas constant** R = 8.314 J/(mol·K). Notice that R = k_B × N_A, where k_B = 1.38 × 10⁻²³ J/K is the Boltzmann constant — the per-molecule version of R. Avogadro's number is the conversion factor between the molecular world described by k_B and the molar world described by R. Any time you see R in a thermodynamic equation and k_B in a statistical mechanics equation, they are the same physics separated by a factor of N_A.
