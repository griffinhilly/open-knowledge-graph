---
id: uv-vis-spectroscopy-analytical
title: UV–Vis Spectrophotometry
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: beers-law
  type: hard
- id: electronic-spectroscopy-theory
  type: soft
- id: calibration-curve-methods
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: photon-model
  type: soft
- id: emission-absorption-spectra
  type: soft
builds-toward:
- fluorescence-spectroscopy
tags:
- UV-Vis
- spectrophotometry
- absorbance
- chromophore
- quantitative analysis
stage: advanced
status: validated
---

# UV–Vis Spectrophotometry

## Core Idea
UV–Vis spectrophotometry measures the absorption of ultraviolet (200–400 nm) and visible (400–700 nm) radiation by solutions, enabling both qualitative identification and quantitative determination of analytes. Chromophores — functional groups or conjugated systems responsible for absorption — are identified by their characteristic λmax values. Single-wavelength measurements combined with calibration curves determine analyte concentrations. Diode-array instruments record full spectra simultaneously, enabling multicomponent analysis and reaction kinetics monitoring.

## How It's Best Learned
Measure the absorption spectrum of several chromophores and explain each λmax using frontier orbital theory. Then perform a simultaneous two-component analysis on a mixture by solving Beer's law equations at two wavelengths, reinforcing both the chemistry and the linear algebra.

## Common Misconceptions
- A single-beam instrument measures I₀ and I sequentially — drift between measurements introduces error that double-beam instruments minimize by splitting the beam.
- The wavelength of maximum absorbance (λmax) should be used for quantitative work to maximize sensitivity and minimize errors from small wavelength errors.
