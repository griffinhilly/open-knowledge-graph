---
id: isotopes-and-atomic-mass
title: Isotopes and Atomic Mass Determination
domain: chemistry
course: general-chemistry
prerequisites:
- id: atomic-structure-and-atoms
  type: hard
builds-toward:
- molar-mass-and-conversions
- mass-spectrometry-intro
tags:
- isotopes
- mass number
- atomic mass unit
stage: formal-systems
status: draft
---

# Isotopes and Atomic Mass Determination

## Core Idea
Isotopes are atoms of the same element with different numbers of neutrons, resulting in different mass numbers but the same atomic number. Atomic mass is the weighted average of all naturally occurring isotopes' masses. Isotopes have different physical properties but similar chemical properties because chemistry depends on electron configuration.

## Questions

```yaml
- question: "Chlorine has an atomic mass of 35.45 amu on the periodic table. A student concludes that chlorine atoms have 17 protons and approximately 18.45 neutrons. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The atomic mass includes the mass of electrons, which shifts the value away from a whole number"
    - "35.45 is a weighted average of two naturally occurring isotopes (Cl-35 and Cl-37), not the mass of any single chlorine atom"
    - "Neutrons do not contribute to atomic mass — only protons and electrons are counted"
    - "The amu unit is defined relative to carbon-12, making all other values non-integers purely by mathematical convention"
  answer: 1
  explanation: "No chlorine atom has 18.45 neutrons — neutrons come in whole numbers. The 35.45 value is a weighted average of naturally occurring chlorine isotopes: about 75.8% Cl-35 (17 protons, 18 neutrons) and 24.2% Cl-37 (17 protons, 20 neutrons). The calculation: (0.758 × 35) + (0.242 × 37) ≈ 35.48 amu. The periodic table reports this mixture average, not a description of any individual atom. A real chlorine atom is always Cl-35 or Cl-37, never anything in between."

- question: "Carbon-12 is used in mass spectrometry for structural analysis; carbon-14 is used in radiometric dating of biological material. This difference in application reflects:"
  type: multiple-choice
  options:
    - "Carbon-14 having more electrons and therefore different chemical reactivity from carbon-12"
    - "Their different physical properties (radioactive instability in C-14) while both follow identical chemical pathways in biological systems"
    - "Carbon-12 being more abundant and therefore cheaper to produce for routine laboratory use"
    - "Carbon-14 having a different atomic number, giving it distinct metabolic behavior in living organisms"
  answer: 1
  explanation: "Carbon-12 and carbon-14 have the same number of protons and electrons — the same atomic number (6) — so they are chemically indistinguishable. Living organisms incorporate both into biological molecules without discrimination. The difference is physical: C-14 is radioactive and decays at a known half-life (5,730 years), while C-12 is stable. This radioactive decay makes C-14 useful for dating (the ratio of C-14 to C-12 decreases after death at a predictable rate), while C-12's stable mass makes it useful as a mass spectrometry standard. Chemistry is identical; physics differs."

- question: "Two isotopes of the same element have different chemical properties because their mass difference affects how their electrons interact with surrounding atoms."
  type: true-false
  answer: false
  explanation: "Chemical properties are determined by electron configuration — the number and arrangement of electrons — not by mass. Isotopes of the same element have the same atomic number, so they have the same number of protons and electrons in the same arrangement. They form the same chemical bonds, participate in the same reactions, and are incorporated into the same molecular structures. The mass difference produces different physical properties (density, diffusion rate, bond vibration frequency), but chemical behavior is essentially identical. This is why C-14 follows the same metabolic pathways as C-12."

- question: "The atomic mass listed on the periodic table for any element with more than one stable naturally occurring isotope will never be a whole number."
  type: true-false
  answer: true
  explanation: "Atomic mass is the weighted average of all naturally occurring isotopic masses weighted by natural abundance. For any element with multiple stable isotopes, the abundance proportions are fixed by natural processes and almost certainly do not produce an average that lands exactly on an integer. The non-integer value is direct evidence of isotope mixing in the natural sample. Elements with only one stable isotope (like fluorine, F-19) come closest to whole numbers, but even then small deviations occur due to nuclear binding energy effects (mass defect)."

- question: "A student measures the atomic mass of a pure sample of carbon-12 and gets exactly 12.000 amu. They then measure the atomic mass of natural carbon and get 12.011 amu. Explain the discrepancy."
  type: short-answer
  answer: "The 12.000 result is not a measurement — it is a definition. The amu is defined as exactly 1/12 the mass of a carbon-12 atom, so measuring pure C-12 gives 12.000 by definition. Natural carbon is not pure C-12: it is 98.9% carbon-12 and about 1.1% carbon-13 (mass ≈ 13.003 amu), with trace C-14. The 12.011 value is the weighted average: (0.989 × 12.000) + (0.011 × 13.003) ≈ 12.011. The heavier C-13 minority pulls the average above 12.000."
  explanation: "This example illustrates two things at once: that atomic mass units are defined relative to C-12 (making 12.000 a reference point, not a discovery), and that natural samples of elements are always isotopic mixtures. The periodic table's atomic mass values are not properties of individual atoms — they are properties of the naturally occurring mixture of isotopes. This distinction matters practically: in stoichiometry, when you use the molar mass of carbon (12.011 g/mol), you are implicitly using a weighted average that reflects the natural C-12/C-13 ratio in your sample."
```

## Explainer

From your study of atomic structure, you know that an atom's identity is defined by its number of protons — the **atomic number** (Z). Every carbon atom has 6 protons; every oxygen atom has 8. But the nucleus also contains neutrons, and here is the key: the number of neutrons can vary. **Isotopes** are atoms of the same element that differ in their neutron count. Carbon-12 has 6 protons and 6 neutrons (mass number 12), while carbon-13 has 6 protons and 7 neutrons (mass number 13). Both are carbon — same atomic number, same electron configuration, same chemical behavior. But they have different masses, which means different physical properties like density and rate of diffusion.

The notation is straightforward. The **mass number** (A) is the total count of protons plus neutrons. You write isotopes as the element symbol with the mass number as a superscript (¹²C, ¹³C, ¹⁴C) or in hyphenated form (carbon-12, carbon-13, carbon-14). The number of neutrons is simply A − Z. Since the periodic table lists elements by atomic number, and isotopes share the same atomic number, all isotopes of an element occupy the same box on the periodic table.

Now look at the atomic mass listed on the periodic table — for carbon, it reads 12.011 amu, not 12.000. That is because atomic mass is the **weighted average** of all naturally occurring isotopes, accounting for each isotope's mass and its natural abundance. Carbon is 98.9% carbon-12 (mass 12.000 amu) and 1.1% carbon-13 (mass 13.003 amu), with a trace of radioactive carbon-14. The weighted average calculation is: (0.989 × 12.000) + (0.011 × 13.003) = 12.011 amu. This is why no element has an atomic mass that is a whole number — the average always reflects the mixture of isotopes found in nature.

Understanding isotopes matters beyond just reading the periodic table. In mass spectrometry, which you will encounter later, isotopes produce distinct peaks that reveal molecular composition. Radioactive isotopes like carbon-14 are used in radiometric dating because they decay at known rates. In medicine, radioactive iodine-131 targets the thyroid gland for imaging and treatment. And the concept of weighted averages of isotopic masses is essential for converting between mass and moles — the molar mass you use in stoichiometry comes directly from these averaged atomic masses.
