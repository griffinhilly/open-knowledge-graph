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
