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

## Explainer

From your work with electrochemistry basics and potentiometry, you know that electrochemical reactions involve electron transfer at electrode surfaces and that electrode potentials relate to the tendency of species to gain or lose electrons. Coulometry takes a different measurement approach than potentiometry: instead of measuring a voltage to infer concentration, it measures the total electric charge consumed during a complete electrochemical reaction and uses **Faraday's law** to calculate exactly how much analyte was present. The elegance of coulometry is that it is an **absolute method** — it requires no calibration standards because the relationship between charge and moles is defined by fundamental constants.

The key equation is straightforward: **Q = nFN**, where Q is the total charge in coulombs, n is the number of electrons transferred per molecule of analyte, F is the Faraday constant (96,485 coulombs per mole of electrons), and N is the number of moles of analyte. If you electrolyze a solution of Cu²⁺ to deposit copper metal (Cu²⁺ + 2e⁻ → Cu), n equals 2, and measuring the total charge passed tells you exactly how many moles of copper were in solution. In **controlled-potential coulometry**, you set the working electrode at a potential where only your target analyte reacts, then let current flow until the reaction is complete — the current decays exponentially toward zero as the analyte is consumed. Integrating the current over time gives Q. This selectivity comes directly from what you learned about electrode potentials: different species reduce or oxidize at different potentials, so choosing the right potential lets you target one analyte while leaving others untouched.

**Coulometric titrations** work differently and are often more practical for routine analysis. Instead of directly electrolyzing the analyte, you electrogenerate a reagent at the electrode that then reacts with the analyte in solution. For example, oxidizing Br⁻ at an electrode produces Br₂, which then reacts with an unsaturated organic compound. The endpoint is detected just as in a conventional titration — by a color change, a potentiometric indicator, or an amperometric sensor — but the "titrant" is generated in situ with perfect stoichiometric control. The amount of reagent added equals the charge passed divided by nF, eliminating the need to standardize solutions or measure volumes precisely. The most commercially important coulometric titration is the **Karl Fischer titration** for trace water determination, where iodine is electrogenerated to react with water in a stoichiometric reaction.

**Electrogravimetry** combines coulometric principles with gravimetric measurement. The analyte is deposited as a solid (usually a metal) on a pre-weighed electrode, and the mass gained directly gives the analyte quantity. Copper determination is the classic example: Cu²⁺ plates out as metallic copper on a platinum cathode, and weighing the electrode before and after gives the copper content. The critical requirement for all coulometric methods is **100% current efficiency** — every electron must go toward the intended reaction. If side reactions like water electrolysis consume some of the charge, you overestimate the analyte. Ensuring current efficiency through proper potential control, supporting electrolyte selection, and electrode conditioning is what makes the difference between a coulometric result you can trust and one contaminated by systematic error.
