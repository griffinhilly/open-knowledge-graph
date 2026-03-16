---
id: limit-of-detection-loq
title: Limit of Detection and Limit of Quantification
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: method-validation
  type: hard
- id: statistical-methods-analytical
  type: hard
- id: signal-to-noise-ratio
  type: soft
- id: normal-distribution
  type: soft
- id: standard-normal-z-scores-theory
  type: soft
tags:
- LOD
- LOQ
- signal-to-noise
- sensitivity
- detection limit
- quantitation limit
stage: formal-systems
status: draft
---

# Limit of Detection and Limit of Quantification

## Core Idea
The limit of detection (LOD) is the lowest analyte concentration that can be reliably distinguished from a blank signal, conventionally defined as 3 times the standard deviation of the blank (3 sigma). The limit of quantification (LOQ) raises the bar to 10 sigma, representing the lowest concentration at which the measurement has acceptable precision for reporting a numerical result. Both are statistical constructs: they depend on the noise characteristics of the specific instrument, method, and matrix, not just on the analyte itself. Sensitivity — the slope of the calibration curve — determines how a given noise level translates into concentration uncertainty.

## How It's Best Learned
Measure replicate blanks (n >= 10) and low-level standards near the expected detection limit, calculate the standard deviation of the blank response, and derive LOD and LOQ from first principles. Compare these calculated values with the lowest calibration standard to understand whether the method's working range extends low enough for the analytical question.

## Common Misconceptions
- The LOD is not the lowest concentration that produces any signal; it is the lowest concentration distinguishable from zero with a defined confidence level — signals below the LOD are real but unreliable.
- LOD and LOQ are method-specific, not instrument specifications; changing the sample matrix, preparation procedure, or measurement conditions changes them.

## Explainer

Imagine you are in a quiet room trying to hear someone whisper. If the room is silent, even the faintest whisper is detectable. But if there is background noise — a humming ventilator, distant traffic — the whisper must be louder before you can confidently say "I heard something" rather than "that might have been the ventilator." Analytical detection limits work the same way. Your instrument always produces some **baseline noise** even when no analyte is present (the blank signal), and the question is: how much analyte signal must rise above that noise before you can trust that you are seeing real analyte rather than a random fluctuation?

From your statistics prerequisites, you know that repeated measurements of a blank produce a distribution of signal values characterized by a mean and a standard deviation (σ). The **limit of detection (LOD)** is conventionally set at 3σ above the mean blank signal — this corresponds roughly to a 99% confidence level that a signal this large did not arise from blank noise alone (assuming a one-tailed normal distribution). A signal at the LOD tells you "the analyte is probably present," but the measurement uncertainty at this level is enormous — often ±50% or more. You can detect the analyte, but you cannot reliably say *how much* is there.

The **limit of quantification (LOQ)** raises the threshold to 10σ, where measurement precision becomes acceptable for reporting a numerical concentration (typically ±10–20% relative standard deviation). The gap between LOD and LOQ is a zone where analyte is detectable but not reliably quantifiable — results in this range are often reported as "detected but below the quantitation limit." The relationship between these limits and **sensitivity** (the slope of the calibration curve) is crucial: sensitivity translates signal noise into concentration uncertainty. If your calibration curve has a steep slope (high sensitivity), a given amount of signal noise corresponds to a smaller concentration uncertainty, and your detection limit in concentration units improves. This is why LOD and LOQ are always reported in concentration units, not signal units.

A critical practical point is that LOD and LOQ are properties of the *entire method*, not just the instrument. The same spectrometer might achieve an LOD of 0.1 μg/L for lead in clean water but 5 μg/L for lead in a high-salinity brine, because the matrix contributes additional noise and may suppress the analyte signal. Changing the sample preparation procedure, switching from external calibration to standard addition, or even using different sample containers can alter the blank variability and therefore the detection limits. This is why method validation requires you to determine LOD and LOQ experimentally in the actual matrix of interest, using replicate blank measurements — theoretical values calculated from instrument specifications alone are insufficient for defending your results.
