---
id: avogadro-constant-molar-mass
title: Avogadro's Number and Molar Mass
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: soft
builds-toward:
- ideal-gas-law
tags:
- atoms
- molecules
- molar-properties
stage: formal-systems
status: validated
---
# Avogadro's Number and Molar Mass

## Core Idea
Avogadro's number (6.022 × 10²³) is the number of molecules in one mole of any substance. The molar mass (in g/mol) numerically equals the molecular mass (in amu). These constants bridge microscopic atomic properties with macroscopic measurable quantities.

## Questions

```yaml
- question: "A student has 54 grams of water (H₂O, molar mass 18 g/mol). How many water molecules are in this sample?"
  type: multiple-choice
  options:
    - "54 molecules — one gram of water contains one molecule"
    - "3 × 6.022 × 10²³ molecules — three moles each contain Avogadro's number of molecules"
    - "54 × 10²³ molecules — multiply the mass in grams directly by Avogadro's number"
    - "6.022 × 10²³ molecules — any macroscopic sample contains exactly one mole of molecules"
  answer: 1
  explanation: "54 g ÷ 18 g/mol = 3 moles. Each mole contains N_A = 6.022 × 10²³ molecules, so 3 moles = 3 × 6.022 × 10²³ molecules. Option C is the classic error: you cannot multiply grams directly by Avogadro's number — you must first convert to moles using molar mass. Option D confuses 'macroscopic sample' with 'exactly one mole,' which is only true if the sample happens to be one molar mass's worth."

- question: "An element has an atomic mass of 32 amu. Which correctly explains why one mole of this element weighs 32 grams?"
  type: multiple-choice
  options:
    - "Because 32 is a round number conveniently close to the element's true mass in grams"
    - "Because the gram and the amu were independently derived from the same underlying mass standard"
    - "Because the mole is defined as the number of atoms in 12 grams of carbon-12, which makes the amu and g/mol scales numerically identical by construction"
    - "Because Avogadro's number happens to equal 6.022 × 10²³, which creates this numerical equality by coincidence"
  answer: 2
  explanation: "The equality is deliberate design, not coincidence. The mole was defined so that one mole of carbon-12 (atomic mass 12 amu) weighs exactly 12 grams, which fixes the conversion: 1 amu = 1 g/mol ÷ N_A. Every other element's molar mass in g/mol then equals its atomic mass in amu by the same construction. Option D gets causation exactly backward — Avogadro's number was chosen to produce this equality, not the other way around."

- question: "The ideal gas law can be written as PV = nRT (with n in moles) or as PV = Nk_BT (with N as the number of molecules). These are the same equation expressed in different counting units."
  type: true-false
  answer: true
  explanation: "R = k_B × N_A, so nRT = n × (k_B × N_A) × T = (n × N_A) × k_B × T = N × k_B × T, where N is total molecule count. Avogadro's number is the conversion factor between the per-molecule world (k_B) and the per-mole world (R). The physics is identical; only the bookkeeping unit changes."

- question: "The numerical equality between atomic mass in amu and molar mass in g/mol is a remarkable physical coincidence that chemists discovered experimentally."
  type: true-false
  answer: false
  explanation: "This equality is a deliberate definitional choice, not a coincidence. The mole was defined so that one mole of carbon-12 (atomic mass 12 amu) weighs exactly 12 grams. That definition fixes 1 amu = 1 g/mol ÷ N_A, ensuring the numerical equality for all elements. In the 2019 SI redefinition, Avogadro's number was fixed to an exact value precisely to preserve this relationship. It is engineered convenience, not discovered coincidence."

- question: "What problem does Avogadro's number solve for scientists working with macroscopic quantities of matter?"
  type: short-answer
  answer: "Avogadro's number bridges the microscopic scale of atoms (masses ~10⁻²⁷ kg, measured in amu) and the macroscopic scale of laboratory measurements (grams, liters). By grouping 6.022 × 10²³ atoms into one mole, scientists can apply atomic-scale properties — like atomic mass — using ordinary laboratory scales without counting individual atoms or working with absurdly small numbers. The mole converts between 'how many atoms' and 'how many grams' seamlessly."
  explanation: "The core utility is unit translation. Without this bridge, you could never connect a measurement on a scale (grams) to a prediction about atomic behavior (which operates in amu and particle counts). Avogadro's number is the conversion factor that makes atomic physics quantitatively useful in the lab."
```

## Explainer

Matter is made of atoms, but atoms are fantastically small — a single hydrogen atom has a mass of about 1.67 × 10⁻²⁷ kg. Working with individual atoms would make everyday chemistry impossibly cumbersome. The **mole** is chemistry's accounting unit: one mole is defined as exactly 6.02214076 × 10²³ entities (atoms, molecules, or whatever particle you are counting). This number, **Avogadro's number** N_A, was chosen so that one mole of any element has a mass in grams numerically equal to its atomic mass in atomic mass units (amu). Carbon-12 has an atomic mass of exactly 12 amu, so one mole of carbon-12 weighs exactly 12 grams.

The bridge between microscopic and macroscopic is straightforward: if you know the **molar mass** M (in g/mol) of a substance, then a sample of mass m grams contains n = m/M moles, and therefore N = n × N_A = (m/M) × N_A individual molecules. Going the other way, if you know the mass of one molecule m_molecule (in kg), then M = m_molecule × N_A (converted to g). This is why the atomic mass unit itself is defined as 1 amu = 1 g/mol ÷ N_A ≈ 1.66 × 10⁻²⁷ kg. The numerical equality between atomic mass in amu and molar mass in g/mol is a deliberate design feature, not a coincidence.

For molecules, molar mass is additive: water (H₂O) has two hydrogen atoms (1.008 amu each) and one oxygen (15.999 amu), giving a molar mass of 18.015 g/mol. A 18.015-gram sample of water contains 6.022 × 10²³ water molecules. You can verify this scale directly: a liter of water (1000 g) contains about 55.5 moles × N_A ≈ 3.34 × 10²⁵ molecules — an almost incomprehensibly large number packed into one liter.

This framework will be essential when you study the ideal gas law and other macroscopic thermodynamic relationships. The ideal gas law PV = nRT connects the macroscopic pressure, volume, and temperature of a gas to the number of moles n and the **gas constant** R = 8.314 J/(mol·K). Notice that R = k_B × N_A, where k_B = 1.38 × 10⁻²³ J/K is the Boltzmann constant — the per-molecule version of R. Avogadro's number is the conversion factor between the molecular world described by k_B and the molar world described by R. Any time you see R in a thermodynamic equation and k_B in a statistical mechanics equation, they are the same physics separated by a factor of N_A.
