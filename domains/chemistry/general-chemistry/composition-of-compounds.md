---
id: composition-of-compounds
title: Percent Composition and Empirical Formulas
domain: chemistry
course: general-chemistry
prerequisites:
- id: molar-mass-and-conversions
  type: hard
builds-toward:
- writing-ionic-formulas
- chemical-equations-and-balancing
tags:
- percent composition
- empirical formula
- molecular formula
stage: formal-systems
status: validated
---

# Percent Composition and Empirical Formulas

## Core Idea
Percent composition describes the mass percentage of each element in a compound. Empirical formula is the simplest whole-number ratio of atoms in a compound, determined from percent composition or experimental data. Molecular formula is the actual number of atoms, found by dividing molecular mass by empirical formula mass.

## Questions

```yaml
- question: "A compound is found to be 40.0% carbon, 6.7% hydrogen, and 53.3% oxygen by mass, with a measured molar mass of 60 g/mol. What is its molecular formula?"
  type: multiple-choice
  options:
    - "CH₂O — the empirical formula matches the molar mass"
    - "C₂H₄O₂ — the empirical formula mass (30 g/mol) multiplies by 2 to reach 60 g/mol"
    - "C₂H₄O — the hydrogen and oxygen counts are adjusted to reach 60 g/mol"
    - "C₃H₆O₃ — the empirical formula repeats three times"
  answer: 1
  explanation: "First find the empirical formula: 40.0g C / 12.01 = 3.33 mol, 6.7g H / 1.008 = 6.65 mol, 53.3g O / 16.00 = 3.33 mol. Dividing by the smallest (3.33) gives CH₂O, with an empirical formula mass of 30 g/mol. To get the molecular formula, divide the measured molar mass by the empirical formula mass: 60 / 30 = 2. Multiply each subscript by 2 to get C₂H₄O₂. The common misconception (option A) confuses empirical and molecular formulas — they are only the same when the multiplier is 1."

- question: "A compound is 75.0% carbon and 25.0% hydrogen by mass. What is its empirical formula?"
  type: multiple-choice
  options:
    - "CH₃ — a 1:3 ratio of C to H"
    - "CH₄ — a 1:4 ratio of C to H"
    - "C₂H₆ — a 2:6 ratio of C to H"
    - "C₃H₁₂ — a 3:12 ratio of C to H"
  answer: 1
  explanation: "Assume 100g: 75.0g C / 12.01 g/mol = 6.25 mol C; 25.0g H / 1.008 g/mol = 24.8 mol H. Divide by the smaller (6.25): C = 1, H = 24.8/6.25 ≈ 3.97 ≈ 4. The empirical formula is CH₄. Note that C₂H₈ (option D simplified) is the same ratio and is equivalent, but CH₄ is the simplest whole-number form. C₃H₁₂ and C₂H₆ represent different ratios and are incorrect."

- question: "Glucose (C₆H₁₂O₆) and acetic acid (C₂H₄O₂) have different empirical formulas."
  type: true-false
  answer: false
  explanation: "Both glucose and acetic acid share the same empirical formula: CH₂O. Glucose has a C:H:O ratio of 6:12:6, which simplifies to 1:2:1. Acetic acid has 2:4:2, which also simplifies to 1:2:1. This is exactly why percent composition alone cannot distinguish between them — you also need the molar mass to determine the molecular formula."

- question: "To determine a compound's molecular formula from experimental data, percent composition alone is sufficient."
  type: true-false
  answer: false
  explanation: "Percent composition gives you the empirical formula — the simplest whole-number ratio of atoms. But many different molecular formulas can share the same empirical formula (e.g., CH₂O, C₂H₄O₂, C₆H₁₂O₆ all reduce to CH₂O). To find the molecular formula, you additionally need the compound's actual molar mass, typically from mass spectrometry. The molecular formula multiplier is: (measured molar mass) / (empirical formula mass)."

- question: "Why can't percent composition data alone determine a compound's molecular formula? What additional information is needed, and how is it used?"
  type: short-answer
  answer: "Percent composition gives only the simplest atom ratio (the empirical formula), not the actual count. Multiple different compounds can have identical percent compositions if their molecular formulas are integer multiples of the same empirical formula. To determine the molecular formula, you need the compound's measured molar mass (from an experiment like mass spectrometry). Divide the measured molar mass by the empirical formula mass to get a whole-number multiplier, then multiply each subscript in the empirical formula by that number."
  explanation: "The key distinction is ratio vs. count. Formaldehyde (CH₂O, 30 g/mol), acetic acid (C₂H₄O₂, 60 g/mol), and glucose (C₆H₁₂O₆, 180 g/mol) all yield identical percent compositions — they are chemically distinct but share a 1:2:1 C:H:O ratio. Only by combining percent composition (to get the empirical formula) with molar mass (to get the multiplier) can you uniquely identify the molecular formula."
```

## Explainer

Building on your understanding of molar mass, you can now ask a quantitative question about any compound: what fraction of its mass comes from each element? This is **percent composition**, calculated by dividing the total mass contributed by each element (number of atoms × molar mass of that element) by the compound's molar mass, then multiplying by 100%. For water (H₂O, molar mass 18.02 g/mol), hydrogen contributes 2 × 1.008 = 2.016 g/mol, so its percent composition is (2.016 / 18.02) × 100% = 11.19%. Oxygen accounts for the remaining 88.81%. This calculation works for any compound whose formula you know.

The more powerful application runs in reverse. Suppose a chemist analyzes an unknown compound and finds it is 40.0% carbon, 6.7% hydrogen, and 53.3% oxygen by mass. To find the **empirical formula**, assume a 100-gram sample so the percentages become grams directly: 40.0 g C, 6.7 g H, 53.3 g O. Convert each to moles using molar masses: 40.0 / 12.01 = 3.33 mol C, 6.7 / 1.008 = 6.65 mol H, 53.3 / 16.00 = 3.33 mol O. Divide each by the smallest value (3.33) to get the simplest ratio: C₁H₂O₁, or CH₂O. This is the empirical formula — the simplest whole-number ratio of atoms.

The empirical formula tells you the ratio but not the actual count. The compound could be CH₂O (formaldehyde, molar mass 30.03), C₂H₄O₂ (acetic acid, 60.05), or C₆H₁₂O₆ (glucose, 180.16) — all share the same empirical formula. To determine the **molecular formula**, you need one additional piece of data: the compound's actual molar mass, typically obtained from mass spectrometry or another experimental method. Divide the measured molar mass by the empirical formula mass to get a whole-number multiplier, then multiply each subscript in the empirical formula. If the measured molar mass is 180 g/mol and the empirical formula mass (CH₂O) is 30 g/mol, the multiplier is 6, giving C₆H₁₂O₆. This two-step process — percent composition to empirical formula, then empirical formula to molecular formula — is how chemists identify unknown compounds from experimental mass data.
