---
id: joint-longitudinal-competing-event-models
title: Joint Longitudinal-Competing Event Models
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: cox-proportional-hazards
  type: hard
- id: competing-risks-analysis
  type: hard
- id: hierarchical-models-epidemiology
  type: soft
tags:
- joint-models
- repeated-measures
- longitudinal-survival
stage: expert
status: draft
---

# Joint Longitudinal-Competing Event Models

## Core Idea
Joint models simultaneously analyze longitudinal biomarker or quality-of-life trajectories and time to competing events (death, disease progression), accounting for correlation between longitudinal marker evolution and event risk. They properly handle informative censoring (subjects with worse markers more likely to experience events). Joint models improve event prediction as longitudinal measurements accumulate and allow investigation of biomarker-event associations while avoiding selection bias from differential event probabilities. Applications include cancer prognosis and cardiovascular risk prediction incorporating repeated clinical measurements.

## Questions

```yaml
- question: "A clinical researcher uses each patient's most recently observed biomarker value (carried forward) as a time-varying covariate in a standard Cox model. Which bias does a joint model specifically correct?"
  type: multiple-choice
  options:
    - "The Cox model cannot handle time-varying covariates and requires only baseline measurements"
    - "Patients who deteriorate fastest have fewer later measurements, so their true current biomarker status is systematically underrepresented, biasing the association between biomarker and event"
    - "The Cox model underestimates sample size by excluding patients who died before any measurements were taken"
    - "Competing events cannot be incorporated into a Cox model with time-varying covariates"
  answer: 1
  explanation: "This is informative dropout: the reason measurements stop is correlated with the outcome. Patients who are deteriorating most rapidly are more likely to miss visits and die, meaning their last observed value reflects an earlier, less severe state than their true current status. This biases the biomarker-event association downward. Joint models resolve this by modeling the true underlying trajectory as a latent process, borrowing information across all observed time points simultaneously rather than relying on the last observed value."

- question: "In a joint model for competing events (e.g., cancer-specific death vs. cardiovascular death), how can the same longitudinal biomarker relate to the two competing outcomes?"
  type: multiple-choice
  options:
    - "It must have the same association with both outcomes — otherwise the model is misspecified"
    - "It enters the model only for the primary outcome; competing events are treated as independent censoring"
    - "The longitudinal trajectory can have different associations with each competing event, estimated simultaneously while respecting the competing risks structure"
    - "The biomarker trajectory predicts whichever event occurs first, with no outcome-specific distinction"
  answer: 2
  explanation: "In the competing events extension, the survival submodel becomes a competing risks model with cause-specific (or subdistribution) hazards for each event type. The longitudinal trajectory can have a strong association with one cause (e.g., rising PSA predicts cancer-specific death) but a weak or null association with another (e.g., cardiovascular death). These associations are estimated separately within the joint model, which is precisely why cause-specific joint models provide more nuanced clinical information than simple joint models."

- question: "In a joint model, the longitudinal and survival submodels are estimated separately and their results are combined in a second post-hoc stage."
  type: true-false
  answer: false
  explanation: "This describes a two-stage approach, not a joint model. In a true joint model, the two submodels are linked through shared random effects and estimated simultaneously. This joint estimation is the whole point: the same individual-level latent parameters that describe the biomarker trajectory enter the hazard model directly, so measurement error in the biomarker is properly accounted for and the two submodels borrow strength from each other. Two-stage approaches that estimate the longitudinal submodel first and plug in its predictions produce biased results."

- question: "Dynamic event prediction in a joint model improves as longitudinal measurements accumulate because the estimated true biomarker trajectory becomes more precise over time."
  type: true-false
  answer: true
  explanation: "Early in follow-up, with only a few observations, the estimated trajectory (intercept and slope of the individual random effect) is uncertain, leading to wide prediction intervals. As more measurements are observed, the individual trajectory shape becomes apparent, shrinking uncertainty in the survival submodel's hazard estimates. This is the clinically important feature of joint models: unlike Cox models where baseline covariates are fixed, joint models allow risk predictions to be dynamically updated at each patient visit as new biomarker data arrive."

- question: "Why is informative dropout a fundamental problem for standard survival models with longitudinal biomarkers, and what feature of the joint model addresses it?"
  type: short-answer
  answer: "In informative dropout, measurements stop not randomly but because the patient is deteriorating — the reason for missingness is correlated with the outcome. A standard model using observed biomarker values treats missingness as random, systematically underestimating the biomarker-event association for patients with the worst trajectories. Joint models address this by specifying a longitudinal submodel for the true underlying biomarker trajectory as a continuous latent process, linked to the survival submodel through shared random effects. The hazard model uses the estimated true trajectory, not the noisy observed values, so it properly accounts for the fact that patients with the steepest trajectories are the most likely to die earliest."
  explanation: "The key move is replacing the observed (noisy, incomplete) biomarker measurements with the estimated latent trajectory. This simultaneously handles measurement error (the observed values are noisy proxies for the true biological process) and informative dropout (the trajectory is estimated even when later observations are missing because the patient died or deteriorated). The shared random effects structure is the mechanism: the same individual parameters that predict the biomarker trajectory also directly enter the hazard function."
```

## Explainer

You already understand two building blocks that joint models combine. From Cox proportional hazards, you know how to model time to a single event as a function of covariates, handling censoring and producing hazard ratios. From competing risks analysis, you know that when multiple mutually exclusive events can terminate follow-up — death from cancer versus death from cardiovascular disease, for instance — analyzing each cause independently produces biased estimates because the competing events are not independent censoring mechanisms. A joint model brings a third dimension to this: what if one of your covariates is not fixed at baseline but evolves over time, and its evolution is itself predictive of — and predicted by — the event risk?

Consider a prostate cancer trial where PSA (prostate-specific antigen) is measured every three months and death from any cause is the outcome. PSA is not just a covariate — it is a trajectory. A patient whose PSA doubles every six months is in a different biological state than one whose PSA is stable, and that biological state is exactly what predicts both future PSA values and survival. If you naively use the last observed PSA as a time-varying covariate in a Cox model, you face **informative dropout**: patients who die or withdraw early contribute fewer PSA measurements, and their missing later values are not missing at random — they are missing *because* the patient is deteriorating. Simply ignoring this produces biased hazard estimates.

A **joint model** resolves this by specifying two linked submodels. The **longitudinal submodel** treats the biomarker trajectory as a continuous latent process — typically a linear mixed model allowing each patient their own intercept and slope over time. The **survival (event-time) submodel** is a Cox or cause-specific hazard model where the time-varying covariate is the *estimated true trajectory* from the longitudinal submodel, not the noisy observed measurements. The two submodels are linked through shared random effects: the same individual-level parameters that describe the biomarker trajectory also enter the hazard model. This linkage means that the hazard model accounts for measurement error in the biomarker and properly borrows information across all observed time points simultaneously.

In the competing events setting, the survival submodel becomes a competing risks model — with cause-specific hazards or a Fine-Gray subdistribution hazard for each event type — and the longitudinal trajectory can have different associations with each competing event. A rising biomarker might strongly predict cancer-specific death but not cardiovascular death, and the joint model estimates both associations while respecting the competing structure. The practical payoff is substantial: dynamic **event prediction** improves as measurements accumulate mid-study. Early in follow-up, with few longitudinal observations, predictions are uncertain; as the trajectory shape becomes apparent, the model dramatically narrows prediction intervals. This dynamic updating is precisely what makes joint models appealing for clinical risk monitoring, where predictions need to be refreshed at each patient visit rather than fixed at enrollment.
