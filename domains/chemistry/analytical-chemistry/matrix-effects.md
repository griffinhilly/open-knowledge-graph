---
id: matrix-effects
title: Matrix Effects
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: sample-preparation
  type: hard
- id: calibration-curve-methods
  type: hard
tags:
- matrix effects
- matrix suppression
- matrix enhancement
- standard addition
- matrix matching
- ion suppression
stage: formal-systems
status: draft
---

# Matrix Effects

## Core Idea
Matrix effects occur when components of the sample other than the analyte alter the measured signal, causing it to differ from what the same analyte concentration would produce in a pure solvent or simple standard. In mass spectrometry with electrospray ionization, co-eluting matrix components can suppress or enhance ionization efficiency, sometimes by 50% or more. In flame and furnace atomic absorption, matrix components can affect atomization temperature, nebulization efficiency, or cause molecular absorption. Matrix effects make external calibration with solvent-based standards unreliable; countermeasures include matrix-matched calibration (preparing standards in blank matrix), the standard addition method (spiking the sample itself at multiple levels), isotope-dilution mass spectrometry, and thorough sample cleanup to remove offending matrix components before measurement.

## How It's Best Learned
Prepare calibration curves for a compound in both pure solvent and in a post-extraction matrix blank (e.g., plasma extract), compare the slopes, and calculate the matrix effect as a percentage. Then apply the standard addition method to the matrix sample and compare the result to the external calibration result to see how much the matrix bias affected quantification.

## Common Misconceptions
- Matrix effects are not limited to mass spectrometry; they occur in virtually every analytical technique, including AAS, ICP, fluorescence, and electrochemical methods — any time the sample environment differs from the calibration environment.
- Diluting the sample reduces matrix effects but also reduces the analyte signal, potentially pushing it below the LOQ; there is always a tradeoff between matrix dilution and sensitivity.
