---
id: titrimetric-analysis-intro
title: 'Titrimetric Analysis: Principles and Terminology'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: solution-concentration
  type: hard
- id: stoichiometry-calculations
  type: hard
- id: gravimetric-analysis
  type: soft
builds-toward:
- acid-base-titration
- redox-titration
- complexometric-titration
- precipitation-titration
tags:
- titration
- equivalence point
- endpoint
- standardization
- primary standard
stage: advanced
status: validated
---
# Titrimetric Analysis: Principles and Terminology

## Core Idea
Titrimetric (volumetric) analysis determines analyte quantity by measuring the volume of a standardized reagent solution (titrant) required to react completely with the analyte. The equivalence point is the theoretical completion of the reaction; the endpoint is the experimentally observed signal change (indicator color, potentiometric inflection). The titrant concentration must be established by standardization against a primary standard — a pure, stable substance of known composition and high molar mass. Back titrations and indirect titrations extend volumetric methods to analytes that react slowly or incompletely with the titrant.

## How It's Best Learned
Standardize a NaOH solution against potassium hydrogen phthalate (KHP), then use it to determine acetic acid in vinegar. Calculating the propagated uncertainty from each measurement step — burette reading, balance reading, sample mass — makes the advantages of large equivalence point volumes tangible.

## Common Misconceptions
- The endpoint and equivalence point are rarely identical; the difference (titration error) is minimized by choosing an appropriate indicator or detection method.
- Molarity is the most common concentration unit for titrations, but normality (based on equivalents) is still encountered in older literature.

## Questions

```yaml
- question: "A chemist is standardizing a NaOH solution using potassium hydrogen phthalate (KHP). Which property makes KHP a suitable primary standard?"
  type: multiple-choice
  options: ["KHP changes color at the equivalence point, eliminating the need for an indicator", "KHP is a pure, stable solid with a high molar mass that can be weighed accurately", "KHP reacts faster than other standards, reducing titration time", "KHP is less expensive than other available primary standards"]
  answer: 1
  explanation: "A primary standard must be pure (≥99.9%), stable (not hygroscopic or prone to decomposition), and have a high molar mass so that weighing errors produce minimal uncertainty in moles. KHP (MW = 204.2 g/mol) satisfies all three criteria and has a single titratable proton, making stoichiometry straightforward. It does not serve as its own indicator."

- question: "The endpoint and the equivalence point of a titration are the same thing."
  type: true-false
  answer: false
  explanation: "The equivalence point is the theoretical point at which stoichiometrically equivalent amounts of titrant and analyte have reacted — a calculated quantity. The endpoint is the experimentally observed signal change (indicator color shift, potentiometric inflection) that the analyst uses to stop the titration. Titration error is the difference between these two points. A well-chosen indicator minimizes this error but cannot eliminate it entirely."

- question: "Why might an analyst use a back titration instead of a direct titration?"
  type: short-answer
  answer: "A back titration is used when the analyte reacts too slowly or incompletely with the titrant, when the analyte is insoluble in the titrant solution, or when no suitable indicator exists for the direct titration. A known excess of reagent is added to react completely with the analyte, and the unreacted excess is then titrated with a second standardized solution."
  explanation: "Back titrations extend titrimetry to problematic analytes. For example, calcium carbonate dissolves slowly in acid — a direct acid titration gives a sluggish endpoint. Adding excess standardized HCl, allowing complete reaction, then back-titrating the excess HCl with NaOH gives a sharp, accurate endpoint. Analyte concentration is calculated from the difference between added and recovered reagent."
```

## Explainer

Titrimetry is one of the oldest and most precise techniques in quantitative analysis. The core idea is elegant: if you know exactly how much of a reagent reacts with your analyte in a fixed stoichiometric ratio, and you can detect the exact moment the reaction is complete, then measuring the volume of reagent consumed tells you exactly how much analyte was present. Precision comes from careful measurement of volume and concentration, not from sophisticated instrumentation.

Before any titration can yield results, the titrant's concentration must be established through standardization. You cannot simply assume a prepared solution is exactly the labeled concentration — small errors in weighing, volumetric glassware calibration, and atmospheric water absorption introduce uncertainty. Primary standards eliminate this uncertainty: they are pure, stable substances with precisely known molecular weights, weighed on an analytical balance, that react completely with the titrant in a known stoichiometric ratio. The standardized solution becomes the reference from which all subsequent analyte concentrations are calculated. This chain of traceability — from a weighed primary standard to a standardized titrant to a sample result — is what makes titrimetry metrologically sound.

The distinction between equivalence point and endpoint is not a technicality — it is the central source of error in every titration. The equivalence point exists only in theory: the exact moment stoichiometrically equivalent amounts of titrant and analyte have reacted. The endpoint is what you can actually observe: a color change, a pH inflection, a change in conductivity. A phenolphthalein indicator, for example, changes color across a pH range that may or may not perfectly coincide with the theoretical equivalence point for your specific reaction. Choosing an indicator whose color-change range brackets the equivalence point, and being consistent in how you identify the endpoint, minimizes titration error.

Back titrations and indirect titrations extend the method to difficult analytes. When a reaction is slow, produces no clean endpoint, or requires conditions incompatible with standard indicator detection, you add a known excess of a reagent that reacts completely with the analyte, then titrate the unreacted excess. The analyte quantity is determined by subtraction: moles of analyte = moles of reagent added − moles of reagent remaining. This transforms one intractable titration into two tractable ones.

Uncertainty propagation is integral to evaluating titrimetric results. Each measurement — burette reading (typically ±0.01 mL), balance reading, sample mass — contributes to the final uncertainty. Using large equivalence-point volumes dilutes the relative uncertainty of each burette reading, which is one reason analysts choose sample sizes and titrant concentrations that produce equivalence-point volumes of 20–40 mL rather than 2–4 mL. Calculating propagated uncertainty is not just a formality; it reveals which measurement step dominates the error and where improvements will have the most impact.
