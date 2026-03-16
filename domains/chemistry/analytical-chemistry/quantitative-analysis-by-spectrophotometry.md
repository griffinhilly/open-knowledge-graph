---
id: quantitative-analysis-by-spectrophotometry
title: Quantitative Analysis by Spectrophotometry
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: beers-law
  type: hard
- id: uv-vis-spectroscopy-analytical
  type: hard
- id: linear-regression
  type: soft
tags:
- spectrophotometry
- UV-Vis
- quantitative
stage: advanced
status: draft
---

# Quantitative Analysis by Spectrophotometry

## Core Idea
Spectrophotometry measures light absorption to determine analyte concentration based on Beer-Lambert law. This method involves selecting appropriate wavelengths, preparing calibration curves, and accounting for deviations from linearity and interference effects.

## How It's Best Learned
Work through calibration curve construction, calculation of molar absorptivity, and troubleshooting nonlinear responses caused by instrumental or chemical factors.

## Explainer

You already know from Beer's Law that absorbance is directly proportional to concentration: A = εbc, where ε is the molar absorptivity, b is the path length, and c is the concentration. **Quantitative spectrophotometry** puts this relationship to work — you measure how much light a sample absorbs at a carefully chosen wavelength and use that measurement to determine how much analyte is present. The conceptual simplicity is appealing, but producing accurate quantitative results requires attention to several practical details that separate a reliable measurement from a meaningless number.

The process starts with **wavelength selection**. You want to measure at the wavelength of maximum absorbance (λ_max) for two reasons: sensitivity is highest there because the signal change per unit concentration is greatest, and the absorbance is least sensitive to small errors in wavelength setting because the absorption peak is relatively flat at its maximum. You identify λ_max by scanning the absorption spectrum of your analyte, which you already know how to do from your UV-Vis spectroscopy prerequisite. If interfering species absorb at λ_max, you may need to choose an alternative wavelength where the analyte absorbs but the interferent does not, accepting some loss of sensitivity for improved selectivity.

Next comes the **calibration curve** — a series of standards of known concentration measured under identical conditions. Using your knowledge of linear regression, you plot absorbance versus concentration and fit a line. The slope equals εb, and the y-intercept should be close to zero (a significant non-zero intercept suggests a blank correction is needed). The correlation coefficient (r²) quantifies linearity, but do not rely on it blindly: r² can be high even when the relationship is subtly curved. Always inspect the residuals plot — systematic curvature in residuals reveals deviations from Beer's Law that r² alone might miss.

**Deviations from linearity** are common and fall into three categories. Chemical deviations occur when the analyte's chemistry changes with concentration — for example, if a weak acid dissociates differently at different concentrations, the absorbing species is not simply proportional to the total analyte concentration. Instrumental deviations arise from stray light (photons reaching the detector without passing through the sample) and from using a bandwidth that is too wide relative to the absorption peak. At high absorbance values (typically above A = 1), the amount of light reaching the detector becomes very small, and the signal-to-noise ratio deteriorates rapidly — this sets a practical upper limit on the useful concentration range. Working within the linear range (typically A = 0.1 to 1.0) and diluting concentrated samples to fall within this window are essential habits for producing trustworthy quantitative results.
