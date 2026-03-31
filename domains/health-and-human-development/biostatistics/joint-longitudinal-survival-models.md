---
id: joint-longitudinal-survival-models
title: Joint Models for Longitudinal and Survival Data
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: cox-proportional-hazards-detailed
  type: hard
- id: mixed-effects-models-biostatistics
  type: hard
- id: time-varying-covariates
  type: soft
builds-toward: []
tags:
- joint-model
- longitudinal
- survival
- shared-random-effects
- biomarker
- dynamic-prediction
stage: expert
status: validated
---

# Joint Models for Longitudinal and Survival Data

## Core Idea
Joint models simultaneously model a longitudinal biomarker process (e.g., repeated PSA measurements) and a time-to-event outcome (e.g., death or disease recurrence), linked through shared random effects. The longitudinal submodel (typically a mixed-effects model) captures the subject's true biomarker trajectory, while the survival submodel (typically a Cox-type model) relates the hazard to the current true biomarker value. The shared random effects create the dependence between the two processes: subjects whose biomarkers deteriorate faster also have higher hazard. Joint modeling solves two problems that simpler approaches cannot: (1) it handles informative dropout (subjects who die cannot provide further biomarker measurements, biasing the longitudinal analysis) and (2) it avoids the bias of naively inserting error-prone, irregularly measured biomarker values as time-varying covariates in a Cox model.

## Questions

```yaml
- question: "A standard mixed-effects model of PSA trajectories in prostate cancer patients ignores the fact that patients with rapidly rising PSA are more likely to die and stop contributing measurements. Why does this create bias?"
  type: multiple-choice
  options:
    - "The model fits fewer data points, reducing power"
    - "The dropout is informative — patients with the worst PSA trajectories disappear from the data, making the observed average trajectory appear more favorable than the true population trajectory"
    - "Mixed-effects models cannot handle unequal follow-up times"
    - "The bias affects only the random effects, not the fixed effects"
  answer: 1
  explanation: "When dropout is related to the biomarker value (informative censoring), the remaining patients at later time points are a biased sample — they are the survivors with better biomarker trajectories. A standard mixed-effects model that treats dropout as ignorable will underestimate the rate of PSA rise in the population because the fastest-rising patients are no longer observed. Joint modeling handles this by explicitly linking the dropout process (survival) to the longitudinal process through shared random effects, so the model 'knows' that missing data are not random."

- question: "Joint models use the 'true' (unobserved) biomarker value from the longitudinal submodel rather than the observed (measured) value in the survival submodel. Why is this important?"
  type: short-answer
  answer: "Observed biomarker values contain measurement error and are only available at discrete, often irregular, time points. Using raw observed values as time-varying covariates in a Cox model attenuates the association (measurement error biases toward the null) and creates problems at event times that do not coincide with measurement times. The joint model's longitudinal submodel estimates the true underlying trajectory (smooth, continuous, and free of measurement error), and the survival submodel uses this true trajectory to predict the hazard at each moment. This produces unbiased estimates of the biomarker-hazard association."
  explanation: "This is analogous to errors-in-variables bias in regression: using a noisy proxy for the true predictor attenuates the estimated effect. The joint model's longitudinal submodel acts as a denoising filter, estimating the true biomarker level at each time point by borrowing strength across the subject's entire measurement history and the population trajectory. The survival submodel then uses these cleaned values."

- question: "Dynamic prediction from a joint model updates a patient's survival probability each time a new biomarker measurement is obtained. This is more clinically useful than a single baseline prediction because it incorporates the patient's evolving trajectory."
  type: true-false
  answer: true
  explanation: "A baseline Cox model produces a single survival prediction based on characteristics measured at study entry. A joint model can update this prediction as new longitudinal data arrive — if a patient's biomarker is rising faster than expected, the predicted survival probability decreases accordingly. This dynamic prediction is computed from the posterior distribution of the patient's random effects conditional on all their observed biomarker values, combined with the survival submodel. It is particularly valuable for clinical monitoring, where decisions (continue surveillance, switch treatment, refer for surgery) should reflect the patient's current trajectory, not just their baseline risk."
```

## Explainer

In many clinical settings, a longitudinal biomarker (PSA in prostate cancer, CD4 count in HIV, troponin in heart failure) tracks disease progression and predicts the eventual clinical event (recurrence, death). Two separate analyses — a mixed-effects model for the biomarker trajectory and a Cox model for survival — each capture part of the picture but miss the critical connection between them. **Joint models** explicitly link these two processes, producing a unified analysis that is both more accurate and more clinically useful.

The standard joint model has two components connected by **shared random effects**. The **longitudinal submodel** is a mixed-effects model: Y_i(t) = X_i(t)β + Z_i(t)b_i + ε_i(t), where b_i are subject-specific random effects (random intercept and slope) that capture how each patient's trajectory deviates from the population average. The **survival submodel** relates the hazard to the current value of the true biomarker trajectory: h_i(t) = h_0(t) × exp(γ × m_i(t) + W_i α), where m_i(t) is the true (denoised) biomarker value from the longitudinal submodel. The random effects b_i appear in both submodels — this is the "joint" part. A patient with random effects indicating rapid biomarker decline will simultaneously have a steep observed trajectory in the longitudinal submodel and an elevated hazard in the survival submodel.

This joint specification solves two problems that separate analyses cannot. First, **informative dropout**: when patients with the worst biomarker trajectories die and stop providing measurements, a standalone mixed-effects model will underestimate the biomarker decline rate because the most severely affected patients disappear. The joint model accounts for this selection by modeling the dropout mechanism (survival) simultaneously. Second, **measurement error**: inserting raw, noisy biomarker values as time-varying covariates in a Cox model produces attenuated (biased toward null) hazard ratio estimates. The joint model uses the estimated true trajectory, which is smooth, continuous, and free of measurement error.

The most compelling clinical application is **dynamic prediction**. After fitting a joint model, you can predict a new patient's survival probability conditional on their observed biomarker history up to the present time. Each time a new measurement arrives, the prediction updates — a patient whose PSA is rising faster than expected receives a progressively worse prognosis, while one whose PSA stabilizes receives a more optimistic forecast. This dynamic, individualized prediction is the clinical goal of joint modeling and is increasingly used in monitoring protocols for cancer surveillance, organ transplant outcomes, and chronic disease management.
