---
id: time-varying-exposures-and-covariates
title: Time-Varying Exposures and Confounders
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: cox-proportional-hazards
  type: hard
- id: person-time-follow-up-studies
  type: hard
builds-toward:
- marginal-structural-models
tags:
- time-dependent-exposure
- confounding-control
- causal-inference
stage: advanced
status: draft
---

# Time-Varying Exposures and Confounders

## Core Idea
Many exposures and confounders change over follow-up (treatment initiation or switching, medication adherence changes, smoking cessation), creating time-varying exposure patterns. Time-varying exposure analysis requires restructuring data into person-time units and using methods like extended Cox regression or marginal structural models to properly account for time-dependent exposure and confounding. Naive analysis ignoring time-variation can severely bias causal effect estimates by conflating concurrent confounding with causal effects.

## How It's Best Learned
Reshape follow-up data into person-time records with time-varying exposure and covariates; fit extended Cox and compare to naive analysis.

## Common Misconceptions
Baseline exposure analysis is valid even when exposure changes (can severely bias causal effects). Ordinary regression adjustment handles time-varying confounding adequately.

## Explainer

Your prerequisites give you two essential tools: the **Cox proportional hazards model**, which estimates hazard ratios for time-to-event outcomes while accommodating censoring, and the **person-time framework**, which recognizes that individuals contribute varying amounts of follow-up and that rates should be expressed per unit of person-time. Both tools assume, in their standard forms, that you have measured exposure once (at baseline) and that it represents each person's exposure throughout follow-up. This assumption is often violated in practice, and the violation creates systematic bias.

Consider a study of a cholesterol-lowering drug's effect on cardiovascular disease. People are enrolled, followed for years, and some initiate the drug during follow-up while others switch doses or stop taking it. If you classify everyone by their baseline medication status and run a standard Cox model, you are treating a person who started the drug at month 18 as unexposed for their entire follow-up — even though they were exposed for much of it. The result is a severely diluted exposure contrast that biases the effect estimate toward null. The solution is to restructure the data so that each person-period of observation is its own row, with the correct exposure value for that specific time interval. This is the **counting process formulation** of the Cox model, and it is the standard way to handle time-varying exposures.

The data structure change is fundamental: instead of one row per person, you create multiple rows per person, each representing a time interval during which exposure status and covariate values are constant. For each row, you record the start time, end time, outcome indicator (did the event occur at the end of this interval?), and current values of the exposure and all covariates. This long-format structure lets the model correctly attribute each unit of person-time to the exposure state actually in effect. Fitting an extended Cox model on this data structure correctly estimates the effect of current exposure on instantaneous hazard.

**Time-dependent confounding** is a subtler and more dangerous problem. Imagine the same drug study, but now a covariate — say, illness severity — both predicts who initiates the drug (sicker patients get the drug) and predicts the outcome (sicker patients have more events). If illness severity also changes over time and is itself affected by earlier drug use, then it is simultaneously a confounder *and* a mediator. Traditional regression adjustment creates a paradox: adjusting for the covariate blocks part of the causal path you want to estimate, biasing your answer downward; but failing to adjust leaves residual confounding. Neither option with standard regression is correct. This is the motivating problem for **marginal structural models (MSMs)**, which use **inverse probability of treatment weighting (IPTW)** to create a pseudo-population where treatment at each time point is independent of prior covariate history. MSMs break the feedback loop between exposure and time-varying confounders and are the principled solution to this problem — which is why they appear as the builds-toward node from this topic.
