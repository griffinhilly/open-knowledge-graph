---
id: coulometry
title: Coulometry and Electrogravimetry
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: potentiometry
  type: hard
- id: electrochemistry-basics
  type: hard
- id: electric-current-and-resistance
  type: soft
- id: electric-charge-and-coulombs-law
  type: soft
- id: electric-current-definition
  type: soft
- id: electroanalytical-overview
  type: soft
- id: electrolytic-cells-and-electrolysis
  type: soft
tags:
- coulometry
- Faraday's law
- controlled potential
- coulometric titration
- electrogravimetry
stage: advanced
status: validated
---

# Coulometry and Electrogravimetry

## Core Idea
Coulometric methods determine analyte quantity by measuring the total electric charge (in coulombs) passed during a quantitative electrochemical reaction, using Faraday's law: m = MQ/(nF), where M is molar mass, Q is charge, n is electrons per mole, and F is the Faraday constant. Controlled-potential coulometry electrolytically converts 100% of the analyte; coulometric titrations electrogenerate a reactive intermediate (e.g., Br₂ from Br⁻ oxidation) that serves as the titrant. Electrogravimetry deposits the analyte as a metal film on a weighed electrode, combining electrochemistry and gravimetry.

## How It's Best Learned
Perform a Karl Fischer coulometric titration to determine trace water in a solvent, then compare to a volumetric method. The absolute nature of Faraday's law — requiring no standards — makes coulometry an ideal primary method for verifying other calibrations.

## Common Misconceptions
- Coulometry is only accurate when 100% current efficiency is achieved — any side reactions (e.g., water electrolysis) consume charge without converting analyte, causing positive errors.
- Controlled-potential coulometry must maintain selectivity through the entire electrolysis, which requires monitoring potential as the solution composition changes.

## Questions

```yaml
- question: "A chemist performs controlled-potential coulometry to measure Cu²⁺ concentration, but the result is 15% higher than expected from a parallel ICP-MS measurement. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The Faraday constant used in the calculation was incorrect"
    - "A side reaction such as water electrolysis consumed charge without converting Cu²⁺, inflating the measured Q"
    - "The molar mass of copper was not correctly accounted for in the Faraday's law calculation"
    - "The controlled potential was too low, causing incomplete electrolysis of the analyte"
  answer: 1
  explanation: "Coulometry requires 100% current efficiency — every coulomb of charge must convert analyte, not drive side reactions. If water electrolysis or oxygen reduction consumes some charge, Q is artificially high, and the calculated analyte amount is overestimated. This is the critical limitation: the method is absolute only when side reactions are suppressed. Option D would cause underestimation (incomplete conversion), not overestimation. Options A and C are calculation errors unrelated to the chemistry."

- question: "Why is coulometry considered an 'absolute' analytical method?"
  type: multiple-choice
  options:
    - "It is more accurate than all other electroanalytical methods"
    - "It requires no calibration against external standards because the charge-to-moles relationship is defined by fundamental constants"
    - "It can be applied absolutely to any analyte without modification"
    - "The electrode potential is held absolutely constant throughout the measurement"
  answer: 1
  explanation: "The term 'absolute' means the method relies on fundamental constants rather than comparisons to known samples. Faraday's law (Q = nFN) connects measurable charge to moles of analyte through F (96,485 C/mol of electrons) and n (electrons per analyte molecule), both of which are known exactly. No calibration curve or standard solution is needed. This makes coulometry a primary reference method — it can verify other analytical methods rather than relying on them."

- question: "In a coulometric titration, a chemist can calculate exactly how much titrant was delivered without measuring any volume."
  type: true-false
  answer: true
  explanation: "This is one of coulometric titration's key practical advantages. The titrant is electrogenerated in situ, and the amount produced equals Q/(nF) — charge divided by the product of electrons per molecule and the Faraday constant. No volumetric glassware, no standardized solutions, no volume measurement is required. This eliminates several sources of volumetric error and makes coulometric titrations highly precise for trace analysis. The Karl Fischer water determination is the most commercially important example of this principle."

- question: "Since coulometry requires no external calibration standards, it achieves high accuracy even when dissolved oxygen or other electroactive species are present in the solution alongside the analyte."
  type: true-false
  answer: false
  explanation: "Coulometry is an absolute method only when current efficiency is 100% — all charge must go toward converting the intended analyte. Dissolved oxygen, water, and other electroactive impurities can consume charge through side reactions, causing the measured Q to exceed what was used for the analyte. The result is a systematic positive error in the calculated analyte amount. Ensuring current efficiency requires careful potential control, degassing the solution, and selecting supporting electrolytes that minimize competing reactions."

- question: "Why does coulometry not require external calibration standards, and what experimental condition must be met for this advantage to hold?"
  type: short-answer
  answer: "Coulometry relies on Faraday's law: Q = nFN, where F is a fundamental constant and n is known from the chemistry. The relationship between charge and moles is fixed by nature, not by comparison to a standard. The condition that must be met is 100% current efficiency — every electron must participate in the intended reaction, with no charge diverted to side reactions. If current efficiency falls below 100%, the measured charge overstates what converted the analyte, and the absolute relationship between Q and N no longer holds."
  explanation: "The elegance of coulometry is that it 'counts' molecules using a quantity (electric charge) that can be measured with extreme precision using current-time integration. The Faraday constant acts as an exact conversion factor. But this only works if there's a one-to-one correspondence between charge and analyte molecules — any charge 'leaking' into side reactions breaks the accounting. This is why ensuring current efficiency is the central technical challenge in coulometric methods, requiring careful potential control and solution preparation."
```

## Explainer

From your work with electrochemistry basics and potentiometry, you know that electrochemical reactions involve electron transfer at electrode surfaces and that electrode potentials relate to the tendency of species to gain or lose electrons. Coulometry takes a different measurement approach than potentiometry: instead of measuring a voltage to infer concentration, it measures the total electric charge consumed during a complete electrochemical reaction and uses **Faraday's law** to calculate exactly how much analyte was present. The elegance of coulometry is that it is an **absolute method** — it requires no calibration standards because the relationship between charge and moles is defined by fundamental constants.

The key equation is straightforward: **Q = nFN**, where Q is the total charge in coulombs, n is the number of electrons transferred per molecule of analyte, F is the Faraday constant (96,485 coulombs per mole of electrons), and N is the number of moles of analyte. If you electrolyze a solution of Cu²⁺ to deposit copper metal (Cu²⁺ + 2e⁻ → Cu), n equals 2, and measuring the total charge passed tells you exactly how many moles of copper were in solution. In **controlled-potential coulometry**, you set the working electrode at a potential where only your target analyte reacts, then let current flow until the reaction is complete — the current decays exponentially toward zero as the analyte is consumed. Integrating the current over time gives Q. This selectivity comes directly from what you learned about electrode potentials: different species reduce or oxidize at different potentials, so choosing the right potential lets you target one analyte while leaving others untouched.

**Coulometric titrations** work differently and are often more practical for routine analysis. Instead of directly electrolyzing the analyte, you electrogenerate a reagent at the electrode that then reacts with the analyte in solution. For example, oxidizing Br⁻ at an electrode produces Br₂, which then reacts with an unsaturated organic compound. The endpoint is detected just as in a conventional titration — by a color change, a potentiometric indicator, or an amperometric sensor — but the "titrant" is generated in situ with perfect stoichiometric control. The amount of reagent added equals the charge passed divided by nF, eliminating the need to standardize solutions or measure volumes precisely. The most commercially important coulometric titration is the **Karl Fischer titration** for trace water determination, where iodine is electrogenerated to react with water in a stoichiometric reaction.

**Electrogravimetry** combines coulometric principles with gravimetric measurement. The analyte is deposited as a solid (usually a metal) on a pre-weighed electrode, and the mass gained directly gives the analyte quantity. Copper determination is the classic example: Cu²⁺ plates out as metallic copper on a platinum cathode, and weighing the electrode before and after gives the copper content. The critical requirement for all coulometric methods is **100% current efficiency** — every electron must go toward the intended reaction. If side reactions like water electrolysis consume some of the charge, you overestimate the analyte. Ensuring current efficiency through proper potential control, supporting electrolyte selection, and electrode conditioning is what makes the difference between a coulometric result you can trust and one contaminated by systematic error.
