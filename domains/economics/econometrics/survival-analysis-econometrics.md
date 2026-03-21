---
id: survival-analysis-econometrics
title: Survival Analysis and Duration Models
domain: economics
course: econometrics
prerequisites:
- id: maximum-likelihood-econometrics
  type: hard
- id: time-series-basics-econometrics
  type: soft
tags:
- survival-analysis
- duration
- hazard-rate
stage: advanced
status: draft
---

# Survival Analysis and Duration Models

## Core Idea
Duration models analyze the time until an event occurs (unemployment spells, firm entry/exit, marriage dissolution). The hazard rate measures the instantaneous risk of the event; Cox proportional hazards and parametric models estimate covariate effects.

## Questions

```yaml
- question: "A researcher studying unemployment spells drops all observations where workers were still unemployed at the survey end date, keeping only workers who found jobs during the study period. What is the most likely effect on the estimated average unemployment duration?"
  type: multiple-choice
  options:
    - "No effect — the dropped observations contain no information about how long spells last"
    - "Overestimation — the retained completed spells are systematically longer than those still ongoing"
    - "Underestimation — only shorter spells are likely to complete within the study window, so the retained sample is biased toward quicker exits"
    - "Random noise — censoring is a random process that introduces symmetric error"
  answer: 2
  explanation: "Dropping censored observations creates severe selection bias. Workers whose spells completed during the study window are disproportionately short-spell workers — longer spells are more likely to be ongoing (censored) at survey's end. Retaining only completers selects for the fastest exits, systematically underestimating average duration. This is precisely why survival analysis handles censoring by including these observations in the likelihood with the information they do provide: the spell lasted at least this long."

- question: "A Cox proportional hazards model yields β = 0.5 for a binary variable indicating college education (1 = college graduate). What is the correct interpretation?"
  type: multiple-choice
  options:
    - "College graduates have unemployment spells that are 50% shorter on average"
    - "College graduates exit unemployment at a rate exp(0.5) ≈ 1.65 times higher than non-graduates at every point in time"
    - "The probability of being employed after 10 weeks is 50% higher for college graduates"
    - "The baseline hazard h₀(t) is shifted upward by 0.5 for college graduates"
  answer: 1
  explanation: "In a proportional hazards model, h(t|X) = h₀(t)·exp(Xβ). A coefficient of 0.5 means the hazard for college graduates is exp(0.5) ≈ 1.65 times the hazard for non-graduates — and this multiplicative factor is constant across time (the 'proportional' assumption). Option A confuses the hazard ratio with a duration ratio. Option C confuses the hazard with a probability. Option D misunderstands the model: the baseline hazard h₀(t) is the hazard for the reference group; covariates multiply it, they don't shift it additively."

- question: "A censored observation — where the event has not occurred by the end of the study — contains no useful information about duration and can be safely dropped from a survival analysis."
  type: true-false
  answer: false
  explanation: "Censored observations carry genuine information: we know the event had not occurred by the censoring time, meaning the true duration is at least that long. The survival likelihood correctly incorporates this by including the survival function S(t_c) for a censored observation at time t_c — the probability of surviving past the censoring time. Dropping censored observations ignores this information and, crucially, creates selection bias: longer spells are more likely to be censored, so dropping them systematically underrepresents long durations."

- question: "The Cox proportional hazards model requires the researcher to specify the shape of the baseline hazard h₀(t) in order to estimate the effects of covariates."
  type: true-false
  answer: false
  explanation: "This is precisely what makes the Cox model so widely used. Its genius is the partial likelihood: covariate coefficients β can be estimated using only the ordering of event times (who fails when, relative to others at risk), without ever specifying h₀(t). The baseline hazard is left entirely unspecified — it's 'estimated' nonparametrically and typically not of interest. This semiparametric flexibility is why the Cox model dominates applied work; parametric models (Weibull, exponential) are more efficient when the correct hazard shape is known but sensitive to misspecification."

- question: "Why is it problematic to simply remove censored observations from a survival analysis, and how does the likelihood function address this problem?"
  type: short-answer
  answer: "Removing censored observations causes selection bias: longer spells are more likely to still be ongoing (censored) at study's end, so removing them over-represents short durations and underestimates average duration. The survival likelihood solves this by including censored observations with their actual contribution: for a censored observation at time t_c, the likelihood contribution is S(t_c) — the probability of surviving at least that long. This uses the information that the event had not occurred by t_c without pretending to know when it did occur."
  explanation: "The key distinction is between 'no information' and 'right-censored information.' A censored observation at week 20 tells you the duration exceeded 20 weeks — that's real, usable information. The survival likelihood is constructed as a product over all observations: event-observations contribute the hazard (the density at failure time), censored observations contribute the survival function (the probability of no event by the censoring time). Both types of contribution correctly update our estimate of the duration distribution."
```

## Explainer

Standard regression models assume your outcome variable is a number you observe for every unit in the sample. But many economically important outcomes are *durations* — the length of time until something happens: how long a worker stays unemployed, how long a firm survives before exit, how long a loan remains current before default. These outcomes violate a basic assumption of standard regression: many observations are **censored**, meaning the event hasn't occurred yet when your data collection ends. A worker still unemployed at the end of your survey is not the same as a worker with infinite unemployment — you know their spell lasted *at least* as long as the observation window. Ignoring censoring by dropping or coding these observations causes severe selection bias. Survival analysis handles censoring correctly by building it directly into the likelihood function.

The central object in survival analysis is the **survival function** S(t), which gives the probability that the event has not yet occurred by time t: S(t) = P(T > t). Related to it is the **hazard function** h(t), which measures the instantaneous risk of the event at time t, conditional on having survived until t. Mathematically, h(t) = lim Δt→0 [P(t ≤ T < t + Δt | T ≥ t)] / Δt. The hazard is not a probability but a rate — it can exceed 1 — and its shape reveals whether the event becomes more likely over time (**positive duration dependence**, like machine failure) or less likely (**negative duration dependence**, like unemployment spells that become harder to exit the longer they last). This connection between your maximum likelihood prerequisite and survival analysis is direct: you construct the likelihood by multiplying contributions from observed events and censored observations, and maximize over the parameters.

The **Cox proportional hazards model** is the workhorse of applied survival analysis. It specifies that the hazard for individual i at time t is h(t|Xᵢ) = h₀(t) · exp(Xᵢ'β), where h₀(t) is an unspecified **baseline hazard** and exp(Xᵢ'β) is a multiplicative factor depending on covariates. The "proportional" in the name means that covariates scale the hazard by a constant factor across time — if being a college graduate reduces the unemployment exit hazard by 30% at week 10, it reduces it by 30% at week 30 too. The genius of Cox's approach is that you can estimate the covariate coefficients β using **partial likelihood** without ever specifying h₀(t). This semiparametric structure makes the model highly flexible and is why it dominates applied work: you get covariate estimates without committing to a parametric duration distribution.

Parametric alternatives — exponential (constant hazard), Weibull (monotone hazard), log-logistic (non-monotone) — impose a specific shape on h₀(t) and can be more efficient when that shape is correct, but are sensitive to misspecification. The choice between Cox and parametric models parallels the tradeoffs you've seen elsewhere in econometrics between flexibility and efficiency. A critical practical skill is testing the proportional hazards assumption — if hazard ratios change over time (e.g., the effect of education on re-employment fades as duration lengthens), stratified models or time-varying covariates are needed. Duration models connect naturally to time series concepts you've studied: duration dependence is essentially autocorrelation in the hazard, and unobserved heterogeneity in survival models (the "frailty" problem) mirrors omitted variable bias in standard regression.
