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
- id: electromagnetic-waves
  type: soft
- id: electronic-transitions-excited-states
  type: soft
- id: photon-concept-quanta
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
stage: formal-systems
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

## Questions

```yaml
- question: "A solution has a transmittance of 10% (T = 0.10). What is its absorbance?"
  type: multiple-choice
  options: ["0.10", "0.90", "1.0", "2.3"]
  answer: 2
  explanation: "A = -log(T) = -log(0.10) = -(-1) = 1.0. Transmittance and absorbance are related by a logarithm, not linearly. A common error is confusing A = 1 - T, which would give 0.90 — but that formula does not exist in Beer's law."

- question: "Plotting percent transmittance (%T) versus concentration for a series of standards will produce a straight line if Beer's law holds."
  type: true-false
  answer: false
  explanation: "Beer's law states that ABSORBANCE (A = -log T) is linear with concentration, not percent transmittance. Because A = -log(%T/100), %T varies exponentially with concentration, producing a curve — not a line. Always plot absorbance when verifying Beer's law linearity."

- question: "Why does Beer's law break down at high analyte concentrations?"
  type: short-answer
  answer: "At high concentrations, solute-solute interactions alter the effective molar absorptivity, and the assumption of independent, non-interacting absorbers fails. Additionally, polychromatic light causes deviations because different wavelengths have different ε values, and the average transmittance becomes nonlinear with concentration."
  explanation: "Beer's law derivation assumes non-interacting absorbers and truly monochromatic radiation. Both assumptions degrade at high concentration. Understanding these deviations is practical: analysts must verify linearity over the calibration range and restrict measurements to the validated linear region."
```

## Explainer

When light passes through a colored solution, some of it is absorbed and some passes through. The fraction that gets through is the transmittance T = I/I₀ — the ratio of transmitted to incident intensity. Transmittance is inconvenient for quantitative work because it has a nonlinear relationship with concentration: doubling the concentration does not double T. The fix is to take the negative logarithm: A = −log(T). This quantity, absorbance, is directly proportional to concentration. That proportionality is the Beer–Lambert law: A = εbc.

The three variables in εbc each contribute independently and multiplicatively. The molar absorptivity ε is a molecular property describing how strongly a particular species absorbs light at a given wavelength — a highly conjugated dye has a large ε, while a transparent salt has a tiny one. Path length b is purely geometric: light traveling through more solution encounters more absorbing molecules. Concentration c is the amount of absorber per unit volume. Doubling any one of these while holding the others constant doubles absorbance.

A key practical consequence: measurements should be made at the wavelength of maximum absorption (λmax), where ε is largest. This gives the highest sensitivity and the widest linear range. Using polychromatic (white) light causes deviations because different wavelengths have different ε values; their combined transmittance does not follow Beer's law cleanly. This is why spectrophotometers use a monochromator or narrow-bandpass filter to select a single wavelength band.

Beer's law is linear only within a finite concentration range. At high concentrations, solute molecules start to interact — hydrogen bonding, aggregation, and other intermolecular forces change the effective ε. At very high absorbances, detector noise and stray light become proportionally significant. Practically, absorbances between 0.1 and 1.0 are most reliable. You must establish the linear range experimentally for any new system — Beer's law deviations are not measurement errors; they are predictable physical phenomena that define the valid working range.
