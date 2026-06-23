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
- id: chemometrics-multivariate-calibration
  type: soft
builds-toward:
- multianalyte-panel-determination
tags:
- calibration
- chemometrics
- spectroscopy
- multivariate-analysis
stage: expert
status: validated
---
# Multivariate Calibration: PLS and PCR Models

## Core Idea
Partial least squares (PLS) and principal component regression (PCR) are multivariate calibration methods that extract latent variables from complex spectral or chromatographic data with many correlated variables. These methods construct models that relate full spectra or multiple wavelengths simultaneously to analyte concentration, enabling quantification even when direct univariate approaches fail due to spectral overlap or strong background interference.

## Questions

```yaml
- question: "A chemist builds both a PCR model and a PLS model for predicting glucose concentration from near-infrared spectra of blood plasma. The plasma also strongly absorbs at wavelengths associated with albumin, which is unrelated to glucose. Which statement best explains why PLS typically achieves better glucose predictions with fewer components?"
  type: multiple-choice
  options:
    - "PLS normalizes the spectra first, removing albumin absorption automatically"
    - "PLS finds latent variables that maximize covariance with glucose concentration, so albumin-related spectral variation is deprioritized"
    - "PCR is mathematically invalid for overlapping spectra, making PLS the only valid choice"
    - "PLS uses more calibration samples than PCR, giving it an inherent accuracy advantage"
  answer: 1
  explanation: "PCR finds latent variables (principal components) that capture maximum spectral variance — but albumin's strong absorption is high-variance and will dominate early PCs even though it is irrelevant to glucose. PLS instead finds latent variables that maximize the *covariance* between the spectra and the glucose concentration response variable, so it prioritizes spectral patterns correlated with glucose and ignores albumin variation. Fewer components are needed because those components are directly relevant to the prediction task."

- question: "During cross-validation of a PLS model, the prediction error decreases as the number of latent variables increases from 1 to 6, reaches a minimum at 6 components, and then begins increasing. What is the best interpretation of this pattern?"
  type: multiple-choice
  options:
    - "The true underlying model has exactly 6 independent chemical factors contributing to the signal"
    - "The model overfits noise when more than 6 components are included, even though training error would continue to fall"
    - "Six components is the mathematical maximum for this dataset, so more cannot be added"
    - "The cross-validated error increasing after 6 components indicates the calibration samples are outliers"
  answer: 1
  explanation: "This is the classic bias-variance tradeoff in action. The training (calibration) error generally continues to fall as more components are added, because each new component can capture additional variance — including noise specific to the calibration set. Cross-validated error penalizes overfitting: when a component captures noise rather than real signal, it hurts prediction on left-out samples. The minimum cross-validated error at 6 components identifies the optimal model complexity — enough to capture real chemical signals without fitting idiosyncratic noise in the calibration data."

- question: "PLS models for spectral data typically require fewer latent variables than PCR models to achieve the same predictive accuracy."
  type: true-false
  answer: true
  explanation: "True. PCR selects components based on spectral variance, which may be dominated by interferents or instrument noise unrelated to the analyte. PLS selects components based on covariance between spectra and concentration, so the first few PLS components are specifically targeted at the analyte's contribution. This more efficient use of dimensionality means PLS typically reaches comparable prediction accuracy with fewer components — reducing the risk of overfitting and making the model more interpretable."

- question: "Ordinary least squares regression (OLS) can be reliably applied to multivariate spectral calibration problems whenever the number of calibration samples exceeds the number of wavelengths measured."
  type: true-false
  answer: false
  explanation: "False. The problem is not just having enough samples — it is collinearity. Adjacent wavelengths in a spectrum are highly correlated (nearly identical information), which makes the matrix inversion in OLS numerically unstable or singular even when samples outnumber wavelengths. High collinearity inflates coefficient variances enormously and produces wildly unstable predictions. PCR and PLS solve this by first compressing the correlated wavelengths into a small number of uncorrelated latent variables, then performing regression on those — bypassing the collinearity problem entirely."

- question: "Explain why the number of latent variables (components) in a PLS or PCR model must be determined by cross-validation rather than simply choosing the number that minimizes training error."
  type: short-answer
  answer: "Training error always decreases as more components are added because additional components can fit idiosyncratic noise in the calibration data. Cross-validation withholds subsets of calibration samples, tests prediction on them, and penalizes overfitting — components that fit noise in training samples will predict poorly on left-out samples. The minimum cross-validated error identifies the optimal number of components: enough to capture real spectral-concentration relationships, but not so many that the model memorizes noise specific to the calibration set."
  explanation: "This is the model selection problem. A model with too few components underfits — it misses real chemical signals. A model with too many overfits — it learns the noise patterns specific to the calibration samples and fails on new samples from the same analytical system. Since the goal is accurate prediction on future samples (not perfect fit to calibration data), the selection criterion must be predictive accuracy on held-out data, which is exactly what cross-validation measures."
```

## Explainer

In traditional univariate calibration — which you studied in calibration curve methods — you measure absorbance at a single wavelength, plot it against concentration, and fit a straight line. This works beautifully when your analyte has a clean, isolated absorption band. But real-world analytical problems are often messier: the analyte's band overlaps with an interferent, the baseline drifts unpredictably, or you need to quantify multiple components in a mixture simultaneously. **Multivariate calibration** addresses these problems by using information from many wavelengths (or many variables) at once, extracting the signal buried in complex, overlapping data.

The challenge with using hundreds or thousands of wavelengths directly is that most of them are highly correlated — neighboring wavelengths in a spectrum carry nearly identical information. Ordinary least squares regression fails catastrophically with this many correlated predictors (the math becomes numerically unstable, and the model overfits noise). Both **principal component regression (PCR)** and **partial least squares (PLS)** solve this by compressing the spectral data into a small number of **latent variables** (also called components or factors) that capture the essential patterns. From your chemometrics prerequisite, you know that principal component analysis identifies directions of maximum variance in the spectral data. PCR takes these principal components and uses them as predictors in a standard regression against concentration.

**PLS** takes a fundamentally different approach that often produces better calibration models with fewer components. While PCR finds latent variables that explain maximum variance in the spectra *without considering concentration*, PLS finds latent variables that maximize the *covariance* between spectra and concentration. In other words, PLS asks: "Which spectral patterns are most correlated with the concentration I'm trying to predict?" This means PLS ignores spectral variation that is unrelated to the analyte (instrument noise, irrelevant matrix absorption) and focuses on the signal that matters. The practical result is that PLS models typically need fewer latent variables than PCR models to achieve the same predictive accuracy.

Building a reliable multivariate calibration model requires careful attention to the **calibration set** and **validation strategy**. You need calibration samples that span the full concentration range and capture the variability in matrix composition, temperature, and other factors that will be encountered in routine use. **Cross-validation** — systematically leaving out subsets of calibration data and testing prediction accuracy — guides the critical decision of how many latent variables to include. Too few components and the model underfits, missing real spectral-concentration relationships. Too many components and the model overfits, memorizing noise in the calibration data and predicting poorly on new samples. The optimal number of components is typically found at the minimum of the cross-validated prediction error, and this selection step is where most practical multivariate calibration problems succeed or fail.
