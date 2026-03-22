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

## Questions

```yaml
- question: "A researcher studying a cholesterol drug classifies all participants by their baseline medication status and runs a standard Cox model, even though many participants initiated the drug months into follow-up. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "The effect estimate is biased toward the null because unexposed person-time is misclassified as exposed"
    - "The effect estimate is biased toward the null because exposed person-time is misclassified as unexposed"
    - "The analysis overcorrects, producing an inflated hazard ratio"
    - "Results are unaffected because Cox models automatically handle time-varying exposure"
  answer: 1
  explanation: "Participants who later initiate the drug are classified as unexposed for their entire follow-up, including the period after they actually started treatment. This misclassifies exposed person-time as unexposed, diluting the exposure contrast and pushing the hazard ratio toward 1 (null). Standard Cox models do not automatically accommodate time-varying exposure — that requires the counting process (extended Cox) data structure."

- question: "A covariate — illness severity — both predicts who initiates a treatment and is itself affected by prior treatment use, while also predicting the outcome. If you adjust for illness severity using standard Cox regression, what problem arises?"
  type: multiple-choice
  options:
    - "The model becomes overidentified and cannot converge"
    - "Adjusting blocks part of the causal effect of treatment on the outcome, biasing the estimate downward"
    - "Adjusting eliminates all confounding and provides an unbiased causal estimate"
    - "The proportional hazards assumption is violated and must be tested separately"
  answer: 1
  explanation: "When a covariate is simultaneously a confounder and a mediator — affected by prior exposure and affecting the outcome — it lies partly on the causal path from treatment to outcome. Standard regression adjustment for a mediator blocks the indirect effect, biasing the causal estimate downward. But failing to adjust leaves confounding. Neither standard approach works; this is the motivating problem for marginal structural models with IPTW, which break the feedback loop without conditioning on the mediator directly."

- question: "A time-varying confounder that is causally affected by prior exposure can be handled correctly by simply including it as a time-varying covariate in an extended Cox regression model."
  type: true-false
  answer: false
  explanation: "False. When a covariate is both a time-varying confounder and a mediator (affected by prior exposure), conditioning on it in regression — even in an extended Cox model — blocks part of the causal path you are trying to estimate. This creates bias that standard regression cannot correct. The principled solution is marginal structural models with inverse probability of treatment weighting, which create a pseudo-population where treatment at each time point is independent of prior covariate history."

- question: "Using baseline exposure classification in a study where many participants change exposure status during follow-up tends to bias the estimated effect toward the null (no effect)."
  type: true-false
  answer: true
  explanation: "True. Baseline-only classification misclassifies person-time: participants who later become exposed are treated as unexposed throughout, and participants who stop exposure continue to be classified as exposed. This non-differential misclassification of a binary exposure dilutes the true contrast between exposure groups, attenuating the effect estimate toward null. The correct approach is to restructure data into person-time intervals, each coded with the actual exposure value during that interval."

- question: "Why can't ordinary regression adjustment solve the problem of a covariate that is simultaneously a time-varying confounder and a mediator? Explain the fundamental dilemma."
  type: short-answer
  answer: "Adjusting for the covariate removes confounding but also blocks the indirect causal path (treatment → covariate → outcome), underestimating the total effect. Not adjusting leaves residual confounding that biases the estimate in the other direction. The dilemma arises because the covariate plays two incompatible roles in the causal structure. Marginal structural models with IPTW resolve this by reweighting observations to create a pseudo-population where prior covariate values no longer predict treatment, eliminating confounding without conditioning on the mediator."
  explanation: "The core problem is that standard regression cannot distinguish 'covariate as confounder' from 'covariate as mediator' when both apply simultaneously. Conditioning always blocks the path. MSMs sidestep this by modeling the probability of observed treatment history given covariate history and using inverse probability weights — rather than directly conditioning on confounders in the outcome model."
```

## Explainer

Your prerequisites give you two essential tools: the **Cox proportional hazards model**, which estimates hazard ratios for time-to-event outcomes while accommodating censoring, and the **person-time framework**, which recognizes that individuals contribute varying amounts of follow-up and that rates should be expressed per unit of person-time. Both tools assume, in their standard forms, that you have measured exposure once (at baseline) and that it represents each person's exposure throughout follow-up. This assumption is often violated in practice, and the violation creates systematic bias.

Consider a study of a cholesterol-lowering drug's effect on cardiovascular disease. People are enrolled, followed for years, and some initiate the drug during follow-up while others switch doses or stop taking it. If you classify everyone by their baseline medication status and run a standard Cox model, you are treating a person who started the drug at month 18 as unexposed for their entire follow-up — even though they were exposed for much of it. The result is a severely diluted exposure contrast that biases the effect estimate toward null. The solution is to restructure the data so that each person-period of observation is its own row, with the correct exposure value for that specific time interval. This is the **counting process formulation** of the Cox model, and it is the standard way to handle time-varying exposures.

The data structure change is fundamental: instead of one row per person, you create multiple rows per person, each representing a time interval during which exposure status and covariate values are constant. For each row, you record the start time, end time, outcome indicator (did the event occur at the end of this interval?), and current values of the exposure and all covariates. This long-format structure lets the model correctly attribute each unit of person-time to the exposure state actually in effect. Fitting an extended Cox model on this data structure correctly estimates the effect of current exposure on instantaneous hazard.

**Time-dependent confounding** is a subtler and more dangerous problem. Imagine the same drug study, but now a covariate — say, illness severity — both predicts who initiates the drug (sicker patients get the drug) and predicts the outcome (sicker patients have more events). If illness severity also changes over time and is itself affected by earlier drug use, then it is simultaneously a confounder *and* a mediator. Traditional regression adjustment creates a paradox: adjusting for the covariate blocks part of the causal path you want to estimate, biasing your answer downward; but failing to adjust leaves residual confounding. Neither option with standard regression is correct. This is the motivating problem for **marginal structural models (MSMs)**, which use **inverse probability of treatment weighting (IPTW)** to create a pseudo-population where treatment at each time point is independent of prior covariate history. MSMs break the feedback loop between exposure and time-varying confounders and are the principled solution to this problem — which is why they appear as the builds-toward node from this topic.
