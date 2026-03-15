---
id: calibration-curve-methods
title: 'Calibration Strategies: External Standards, Internal Standards, and Standard
  Addition'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: statistical-methods-analytical
  type: hard
- id: beers-law
  type: soft
- id: linear-regression
  type: soft
- id: scatterplots-and-correlation
  type: soft
- id: interpolation-error-analysis
  type: soft
builds-toward:
- method-validation
tags:
- calibration
- standard addition
- internal standard
- sensitivity
- dynamic range
- matrix effects
stage: advanced
status: validated
---

# Calibration Strategies: External Standards, Internal Standards, and Standard Addition

## Core Idea
Calibration relates the instrument signal to analyte concentration using prepared standards. The external standard method builds a calibration curve from independently prepared standards and reads unknown concentrations by interpolation; it assumes the sample matrix does not affect the response. Standard addition overcomes matrix effects by spiking known amounts of analyte into the sample itself. Internal standards — chemically similar compounds added at a constant concentration — correct for instrumental drift and variable injection volumes in chromatography. Limits of detection (LOD) and quantification (LOQ) are derived from the calibration regression statistics.

## How It's Best Learned
Determine a metal concentration in a complex environmental water sample using all three calibration approaches and compare results. Observing that external and standard addition methods disagree (but standard addition is reliable) makes matrix effects tangible.

## Common Misconceptions
- The LOD is not the lowest concentration on the calibration curve — it is calculated as 3σ/slope (where σ is the standard deviation of blank measurements).
- Blank subtraction corrects for a constant background signal but does not eliminate matrix effects that scale with analyte concentration.
