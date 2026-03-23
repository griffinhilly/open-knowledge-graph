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
- id: electromagnetic-waves
  type: hard
- id: photon-concept-quanta
  type: soft
builds-toward:
- fluorescence-spectroscopy
tags:
- UV-Vis
- spectrophotometry
- absorbance
- chromophore
- quantitative analysis
stage: formal-systems
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

## Questions

```yaml
- question: "For the most accurate quantitative determination of an analyte by UV-Vis, at which wavelength should you measure absorbance?"
  type: multiple-choice
  options: ["Any wavelength where the analyte shows some absorption", "The wavelength of minimum absorbance, to stay within the linear Beer's law range", "The wavelength of maximum absorbance (λmax)", "254 nm, the standard UV analytical wavelength"]
  answer: 2
  explanation: "Measuring at λmax maximizes sensitivity (highest absorbance per unit concentration, improving signal-to-noise) and minimizes errors from small wavelength calibration errors — at the absorption peak, the curve is flat, so tiny wavelength deviations produce negligible absorbance changes. At non-peak wavelengths, the absorbance curve is steep and small wavelength errors cause larger errors in the measured absorbance."

- question: "A double-beam UV-Vis spectrophotometer is more accurate than a single-beam instrument primarily because it can measure two analytes simultaneously."
  type: true-false
  answer: false
  explanation: "The key advantage of a double-beam instrument is that it measures the reference (blank) and sample simultaneously by splitting the beam, so fluctuations in lamp intensity cancel out in the absorbance ratio. The ability to measure two analytes simultaneously (diode-array instruments) is a separate feature unrelated to beam splitting. Single-beam instruments must measure blank and sample sequentially, making them vulnerable to drift between the two measurements."

- question: "A mixture contains two analytes, A and B, both of which absorb in the visible region but with different spectra. You measure the total absorbance at two wavelengths: 450 nm and 600 nm. How do you determine the concentration of each analyte?"
  type: short-answer
  answer: "At each wavelength, the total absorbance equals the sum of contributions from A and B (Beer's law is additive). Using the known molar absorptivities of pure A and B at both wavelengths, set up two equations in two unknowns (concentrations of A and B) and solve the system."
  explanation: "This is multicomponent analysis. If εA1 and εB1 are molar absorptivities at λ1, and εA2 and εB2 at λ2, then: A_total(λ1) = εA1·[A]·b + εB1·[B]·b and A_total(λ2) = εA2·[A]·b + εB2·[B]·b. With two equations and two unknowns, the system is solvable as long as the two analytes have sufficiently different spectral profiles (if εA1/εB1 = εA2/εB2, the equations are linearly dependent and the system cannot be solved)."
```

## Explainer

UV-Vis spectrophotometry works by measuring how much light a solution absorbs at specific wavelengths. When a photon's energy matches the energy gap between a molecule's electronic ground state and an excited state, the photon is absorbed. Different functional groups (chromophores) absorb at characteristic wavelengths: conjugated pi systems absorb in the UV, and extended conjugation shifts absorption into the visible. This is why beta-carotene (with 11 conjugated double bonds) is orange — it absorbs blue light around 450 nm. The λmax of a chromophore is diagnostic: measuring the full absorption spectrum tells you what chromophores are present and in what chemical environment.

The quantitative side rests entirely on Beer's law: A = εbc, where absorbance is proportional to molar absorptivity (ε), path length (b), and concentration (c). You built this foundation already. In practice, UV-Vis adds an instrumental layer on top: you must choose the right wavelength, manage instrument drift, and ensure your calibration standards cover the concentration range of interest. The choice of λmax is not arbitrary — it maximizes sensitivity (highest ε, so the absorbance signal is largest) and also minimizes the effect of small wavelength errors, because the absorbance curve is flat at the peak.

Instrument design matters for accuracy. A single-beam instrument measures the blank (I₀) and sample (I) at different times. If the lamp intensity changes between these two measurements — which it does, especially when warming up — the ratio I/I₀ is corrupted. A double-beam instrument splits the beam simultaneously to a reference and sample detector, so lamp fluctuations affect both channels equally and cancel in the ratio. For routine work at steady state, single-beam instruments are often adequate; for kinetics measurements or high-accuracy work, double-beam designs are preferred.

Diode-array instruments extend this further by dispersing light after it passes through the sample and recording the full spectrum simultaneously across hundreds of wavelengths. This enables reaction kinetics monitoring (recording how a spectrum changes over time) and multicomponent analysis. When two analytes coexist in solution, the total absorbance at any wavelength is the sum of their individual contributions (Beer's law is additive for non-interacting absorbers). Measuring at two wavelengths gives two equations; knowing the molar absorptivities of each pure component allows you to solve for both concentrations — a linear algebra problem embedded in a spectroscopy instrument.

A practical note on calibration: the response must be linear in Beer's law for the concentration range you are measuring. Deviations from linearity occur at high concentrations (where molecules interact) and at high absorbances (where stray light becomes significant). Always verify linearity by running several standards and inspecting the calibration curve before reporting results. An R² value close to 1 is necessary but not sufficient — inspect the residuals for curvature, which indicates the Beer's law regime has been exceeded.
