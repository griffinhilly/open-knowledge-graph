---
id: multivariate-calibration-pls-pcr
title: 'Multivariate Calibration: PLS and PCR Models'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: calibration-curve-methods
  type: hard
- id: chemometrics-multivariate-analysis
  type: hard
- id: matrix-operations
  type: soft
builds-toward:
- chromatographic-resolution-and-selectivity
- multianalyte-panel-determination
tags:
- calibration
- chemometrics
- spectroscopy
- multivariate-analysis
stage: advanced
status: draft
---

# Multivariate Calibration: PLS and PCR Models

## Core Idea
Partial least squares (PLS) and principal component regression (PCR) are multivariate calibration methods that extract latent variables from complex spectral or chromatographic data with many correlated variables. These methods construct models that relate full spectra or multiple wavelengths simultaneously to analyte concentration, enabling quantification even when direct univariate approaches fail due to spectral overlap or strong background interference.

## Explainer

In traditional univariate calibration — which you studied in calibration curve methods — you measure absorbance at a single wavelength, plot it against concentration, and fit a straight line. This works beautifully when your analyte has a clean, isolated absorption band. But real-world analytical problems are often messier: the analyte's band overlaps with an interferent, the baseline drifts unpredictably, or you need to quantify multiple components in a mixture simultaneously. **Multivariate calibration** addresses these problems by using information from many wavelengths (or many variables) at once, extracting the signal buried in complex, overlapping data.

The challenge with using hundreds or thousands of wavelengths directly is that most of them are highly correlated — neighboring wavelengths in a spectrum carry nearly identical information. Ordinary least squares regression fails catastrophically with this many correlated predictors (the math becomes numerically unstable, and the model overfits noise). Both **principal component regression (PCR)** and **partial least squares (PLS)** solve this by compressing the spectral data into a small number of **latent variables** (also called components or factors) that capture the essential patterns. From your chemometrics prerequisite, you know that principal component analysis identifies directions of maximum variance in the spectral data. PCR takes these principal components and uses them as predictors in a standard regression against concentration.

**PLS** takes a fundamentally different approach that often produces better calibration models with fewer components. While PCR finds latent variables that explain maximum variance in the spectra *without considering concentration*, PLS finds latent variables that maximize the *covariance* between spectra and concentration. In other words, PLS asks: "Which spectral patterns are most correlated with the concentration I'm trying to predict?" This means PLS ignores spectral variation that is unrelated to the analyte (instrument noise, irrelevant matrix absorption) and focuses on the signal that matters. The practical result is that PLS models typically need fewer latent variables than PCR models to achieve the same predictive accuracy.

Building a reliable multivariate calibration model requires careful attention to the **calibration set** and **validation strategy**. You need calibration samples that span the full concentration range and capture the variability in matrix composition, temperature, and other factors that will be encountered in routine use. **Cross-validation** — systematically leaving out subsets of calibration data and testing prediction accuracy — guides the critical decision of how many latent variables to include. Too few components and the model underfits, missing real spectral-concentration relationships. Too many components and the model overfits, memorizing noise in the calibration data and predicting poorly on new samples. The optimal number of components is typically found at the minimum of the cross-validated prediction error, and this selection step is where most practical multivariate calibration problems succeed or fail.
