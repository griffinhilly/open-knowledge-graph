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
stage: advanced
status: draft
---

# Joint Longitudinal-Competing Event Models

## Core Idea
Joint models simultaneously analyze longitudinal biomarker or quality-of-life trajectories and time to competing events (death, disease progression), accounting for correlation between longitudinal marker evolution and event risk. They properly handle informative censoring (subjects with worse markers more likely to experience events). Joint models improve event prediction as longitudinal measurements accumulate and allow investigation of biomarker-event associations while avoiding selection bias from differential event probabilities. Applications include cancer prognosis and cardiovascular risk prediction incorporating repeated clinical measurements.

## Explainer

You already understand two building blocks that joint models combine. From Cox proportional hazards, you know how to model time to a single event as a function of covariates, handling censoring and producing hazard ratios. From competing risks analysis, you know that when multiple mutually exclusive events can terminate follow-up — death from cancer versus death from cardiovascular disease, for instance — analyzing each cause independently produces biased estimates because the competing events are not independent censoring mechanisms. A joint model brings a third dimension to this: what if one of your covariates is not fixed at baseline but evolves over time, and its evolution is itself predictive of — and predicted by — the event risk?

Consider a prostate cancer trial where PSA (prostate-specific antigen) is measured every three months and death from any cause is the outcome. PSA is not just a covariate — it is a trajectory. A patient whose PSA doubles every six months is in a different biological state than one whose PSA is stable, and that biological state is exactly what predicts both future PSA values and survival. If you naively use the last observed PSA as a time-varying covariate in a Cox model, you face **informative dropout**: patients who die or withdraw early contribute fewer PSA measurements, and their missing later values are not missing at random — they are missing *because* the patient is deteriorating. Simply ignoring this produces biased hazard estimates.

A **joint model** resolves this by specifying two linked submodels. The **longitudinal submodel** treats the biomarker trajectory as a continuous latent process — typically a linear mixed model allowing each patient their own intercept and slope over time. The **survival (event-time) submodel** is a Cox or cause-specific hazard model where the time-varying covariate is the *estimated true trajectory* from the longitudinal submodel, not the noisy observed measurements. The two submodels are linked through shared random effects: the same individual-level parameters that describe the biomarker trajectory also enter the hazard model. This linkage means that the hazard model accounts for measurement error in the biomarker and properly borrows information across all observed time points simultaneously.

In the competing events setting, the survival submodel becomes a competing risks model — with cause-specific hazards or a Fine-Gray subdistribution hazard for each event type — and the longitudinal trajectory can have different associations with each competing event. A rising biomarker might strongly predict cancer-specific death but not cardiovascular death, and the joint model estimates both associations while respecting the competing structure. The practical payoff is substantial: dynamic **event prediction** improves as measurements accumulate mid-study. Early in follow-up, with few longitudinal observations, predictions are uncertain; as the trajectory shape becomes apparent, the model dramatically narrows prediction intervals. This dynamic updating is precisely what makes joint models appealing for clinical risk monitoring, where predictions need to be refreshed at each patient visit rather than fixed at enrollment.
