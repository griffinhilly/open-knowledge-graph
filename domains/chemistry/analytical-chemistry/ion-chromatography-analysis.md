---
id: ion-chromatography-analysis
title: Ion Chromatography for Ionic Species
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: chromatography-fundamentals
  type: hard
- id: ion-formation-from-electron-transfer
  type: soft
tags:
- ion chromatography
- IC
- ionic species
stage: advanced
status: draft
---

# Ion Chromatography for Ionic Species

## Core Idea
Ion chromatography separates ionic analytes using ion-exchange stationary phases with suppressed-conductivity detection or alternative detectors. This method excels for simultaneous anion and cation analysis in complex matrices.

## Explainer

From your study of chromatography fundamentals, you know that separation depends on differential interaction between analytes and a stationary phase as a mobile phase carries them through a column. **Ion chromatography** (IC) applies this principle to charged species — inorganic anions like fluoride, chloride, nitrate, sulfate, and phosphate, as well as cations like sodium, potassium, calcium, and ammonium. The stationary phase consists of a polymer resin functionalized with charged groups: positively charged groups (quaternary amines) for anion exchange, or negatively charged groups (sulfonates or carboxylates) for cation exchange. Analyte ions compete with eluent ions for binding sites on the resin, and those with weaker affinity for the stationary phase elute first.

The breakthrough that made modern ion chromatography practical was **suppressed conductivity detection**. The challenge with detecting ions by conductivity is that the eluent itself is ionic — you need a carbonate or hydroxide buffer to push analyte ions through the column, and that buffer contributes a large background conductivity signal that would swamp the analyte signal. The suppressor, placed between the column and the detector, chemically converts the eluent ions into a weakly conducting form (for anion IC, it converts NaOH or Na₂CO₃ eluent into water and carbonic acid) while simultaneously converting analyte ions into their highly conducting acid or base forms. The result is a dramatic reduction in background noise and a corresponding improvement in detection limits, often reaching low parts-per-billion levels.

A typical IC analysis of common anions illustrates the power of the technique. A single injection of a water sample produces, within 10–15 minutes, well-resolved peaks for fluoride, chloride, nitrite, bromide, nitrate, phosphate, and sulfate — seven anions quantified simultaneously from one run. The elution order follows the selectivity sequence of the resin: monovalent ions with smaller hydrated radii elute before divalent ions, and within each charge class, the order reflects affinity for the exchange sites. Gradient elution (increasing eluent strength over time) can separate early-eluting monovalent anions with good resolution while still pushing the strongly retained divalent anions off the column in a reasonable time.

IC is the standard method for regulated water quality parameters (EPA Methods 300.0 and 300.1) and finds wide use in semiconductor manufacturing (where trace ionic contamination must be controlled at sub-ppb levels), food and beverage analysis, and pharmaceutical quality control. Its combination of simultaneous multi-analyte capability, low detection limits, and minimal sample preparation requirements makes it one of the most efficient techniques available for routine ionic species analysis.
