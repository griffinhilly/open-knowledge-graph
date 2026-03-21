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

## Questions

```yaml
- question: "An IC system is run without a suppressor between the column and the conductivity detector. What is the most likely result?"
  type: multiple-choice
  options:
    - "Analyte peaks appear larger because more ions reach the detector"
    - "Analyte signals are overwhelmed by the high background conductivity of the ionic eluent"
    - "Only cations are detected because anions are neutralized"
    - "Retention times increase because analytes compete less with eluent ions"
  answer: 1
  explanation: "The suppressor's purpose is to convert the ionic eluent into a weakly conducting form (e.g., NaOH → water) while simultaneously converting analyte ions into their more conducting forms. Without it, the eluent contributes a massive background conductivity signal that dwarfs the small analyte signal — exactly the problem that made conductivity detection impractical before suppressors were developed."

- question: "In anion-exchange IC, sulfate (SO₄²⁻) consistently elutes after chloride (Cl⁻). Why?"
  type: multiple-choice
  options:
    - "Sulfate has a higher molecular weight and migrates more slowly through the column"
    - "Sulfate is divalent and has stronger affinity for the positively charged exchange sites on the resin"
    - "Sulfate is less soluble in the eluent and forms aggregates that slow elution"
    - "Sulfate reacts with the suppressor more slowly than chloride"
  answer: 1
  explanation: "Elution order in ion chromatography reflects affinity for the stationary phase exchange sites, not molecular weight or solubility. Divalent anions like sulfate bind more strongly to the quaternary amine groups on the resin than monovalent anions like chloride, so they require more eluent strength to displace and elute later. This charge-affinity principle explains the general elution order: monovalent anions before divalent anions."

- question: "In suppressed conductivity detection, the suppressor increases the background conductivity of the eluent in order to amplify the analyte signal."
  type: true-false
  answer: false
  explanation: "The opposite is true. The suppressor dramatically *decreases* background conductivity by converting the ionic eluent into a weakly conducting form (e.g., converting Na₂CO₃ eluent to carbonic acid and water). Simultaneously, it converts analyte ions into their more highly conducting acid or base forms. The net effect is a low background with pronounced analyte peaks — the key to IC's low detection limits."

- question: "Ion chromatography can simultaneously separate and quantify multiple ionic species (e.g., seven common anions) from a single injection."
  type: true-false
  answer: true
  explanation: "This multi-analyte capability is one of IC's defining practical advantages. A typical water sample analysis produces resolved peaks for fluoride, chloride, nitrite, bromide, nitrate, phosphate, and sulfate within 10–15 minutes from one injection. This is far more efficient than techniques that require separate analysis for each ion, and is the basis for IC's dominant role in regulatory water quality analysis (EPA Methods 300.0 and 300.1)."

- question: "Explain why suppressed conductivity detection was the key breakthrough that made modern ion chromatography practical for trace ionic analysis."
  type: short-answer
  answer: "The challenge was that the ionic eluent needed to carry analytes through the column was itself highly conductive, creating a background signal that would overwhelm the small analyte contribution. The suppressor solved this by chemically converting the eluent ions into a weak electrolyte (e.g., NaOH into water) while converting analyte ions into their strongly conducting acid or base forms. The result is a near-zero background with strong analyte signals, enabling detection at low parts-per-billion levels."
  explanation: "Before the suppressor was developed (by Small, Stevens, and Bauman in 1975), conductivity detection was impractical for IC because signal-to-noise was too poor. The suppressor transforms the detection geometry entirely: instead of detecting analytes against a large background, you detect them against almost no background. This single innovation unlocked the technique's sensitivity and drove its adoption for environmental, pharmaceutical, and semiconductor applications."
```

## Explainer

From your study of chromatography fundamentals, you know that separation depends on differential interaction between analytes and a stationary phase as a mobile phase carries them through a column. **Ion chromatography** (IC) applies this principle to charged species — inorganic anions like fluoride, chloride, nitrate, sulfate, and phosphate, as well as cations like sodium, potassium, calcium, and ammonium. The stationary phase consists of a polymer resin functionalized with charged groups: positively charged groups (quaternary amines) for anion exchange, or negatively charged groups (sulfonates or carboxylates) for cation exchange. Analyte ions compete with eluent ions for binding sites on the resin, and those with weaker affinity for the stationary phase elute first.

The breakthrough that made modern ion chromatography practical was **suppressed conductivity detection**. The challenge with detecting ions by conductivity is that the eluent itself is ionic — you need a carbonate or hydroxide buffer to push analyte ions through the column, and that buffer contributes a large background conductivity signal that would swamp the analyte signal. The suppressor, placed between the column and the detector, chemically converts the eluent ions into a weakly conducting form (for anion IC, it converts NaOH or Na₂CO₃ eluent into water and carbonic acid) while simultaneously converting analyte ions into their highly conducting acid or base forms. The result is a dramatic reduction in background noise and a corresponding improvement in detection limits, often reaching low parts-per-billion levels.

A typical IC analysis of common anions illustrates the power of the technique. A single injection of a water sample produces, within 10–15 minutes, well-resolved peaks for fluoride, chloride, nitrite, bromide, nitrate, phosphate, and sulfate — seven anions quantified simultaneously from one run. The elution order follows the selectivity sequence of the resin: monovalent ions with smaller hydrated radii elute before divalent ions, and within each charge class, the order reflects affinity for the exchange sites. Gradient elution (increasing eluent strength over time) can separate early-eluting monovalent anions with good resolution while still pushing the strongly retained divalent anions off the column in a reasonable time.

IC is the standard method for regulated water quality parameters (EPA Methods 300.0 and 300.1) and finds wide use in semiconductor manufacturing (where trace ionic contamination must be controlled at sub-ppb levels), food and beverage analysis, and pharmaceutical quality control. Its combination of simultaneous multi-analyte capability, low detection limits, and minimal sample preparation requirements makes it one of the most efficient techniques available for routine ionic species analysis.
