---
id: beers-law
title: Beer–Lambert Law and Optical Absorbance
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: electromagnetic-spectrum
  type: soft
- id: solution-concentration
  type: hard
- id: logarithms-intro
  type: soft
- id: logarithmic-functions-review
  type: soft
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- uv-vis-spectroscopy-analytical
- atomic-absorption-spectroscopy
- fluorescence-spectroscopy
tags:
- absorbance
- Beer-Lambert
- molar absorptivity
- transmittance
- spectrophotometry
stage: advanced
status: validated
---

# Beer–Lambert Law and Optical Absorbance

## Core Idea
The Beer–Lambert law states that the absorbance A of a solution is directly proportional to the molar absorptivity ε, the path length b, and the molar concentration c: A = εbc. Absorbance is the negative log of transmittance (T = I/I₀). The law holds for monochromatic radiation and dilute solutions; deviations arise at high concentrations, with polychromatic light, or when chemical equilibria shift with dilution. Molar absorptivity is a molecular property that characterizes how strongly a species absorbs at a given wavelength.

## How It's Best Learned
Construct a calibration curve for a colored analyte (e.g., KMnO₄) by measuring absorbance at λmax across a concentration series, then determine an unknown. Examining the linear range and identifying where Beer's law breaks down is more instructive than simply applying the formula.

## Common Misconceptions
- Absorbance and percent transmittance are not linearly related — plotting %T vs concentration produces a curve, not a line.
- Beer's law deviations are not 'errors' but predictable physical phenomena; the linear range must be established experimentally.
