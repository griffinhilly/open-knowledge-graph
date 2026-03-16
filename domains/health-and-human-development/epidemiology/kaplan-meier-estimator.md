---
id: kaplan-meier-estimator
title: Kaplan-Meier Survival Analysis and Curves
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: disease-frequency-measures
  type: hard
- id: person-time-follow-up-studies
  type: soft
builds-toward:
- cox-proportional-hazards
tags:
- survival-analysis
- kaplan-meier
- censoring
- time-to-event
stage: advanced
status: draft
---

# Kaplan-Meier Survival Analysis and Curves

## Core Idea
The Kaplan-Meier estimator is a non-parametric method for estimating survival probability over time, properly accounting for censored observations. It calculates the cumulative probability of surviving to each event time by multiplying conditional survival probabilities. Kaplan-Meier curves allow visual comparison of survival between groups and provide median survival estimates, forming the foundation for survival analysis.

## Explainer

From your study of disease frequency measures and person-time, you know that **incidence** — the rate at which new events occur in a population over time — requires careful accounting for how long each person was under observation. Not everyone is followed for the same duration, and some people experience the outcome while others do not. **Survival analysis** is the branch of statistics built specifically for this situation: you have time-to-event data, you want to estimate the probability of an event occurring by a given time, and you have to handle the fact that some participants never experienced the event during follow-up.

The fundamental challenge is **censoring**. A participant is censored if they leave follow-up before the event occurs — they moved away, the study ended, or they were lost to follow-up. A censored observation is not a "missing" outcome in the usual sense; it is real information: this person survived at least until the censoring time. Simply ignoring censored participants would overestimate survival (you're only counting people who experienced the event) while counting them as events would underestimate it. The Kaplan-Meier estimator threads this needle by using censored observations fully for the time they were observed, then removing them from the risk set when they are censored.

The **Kaplan-Meier (KM) estimator** works by computing survival probability as a product of conditional probabilities. At each time point when an event occurs, it estimates the probability of surviving past that moment given survival up to that point: (number at risk − number with events) / (number at risk). It then multiplies all these conditional probabilities together up to time t to get the cumulative survival probability S(t). This is the **product-limit estimator** — "product" because survival over an interval is the product of survival conditional on each event time; "limit" because the estimator uses actual event times, not arbitrary time intervals. The formula is: S(t) = ∏ [(n_i − d_i) / n_i] for all event times t_i ≤ t, where n_i is the number at risk and d_i is the number of events at time t_i.

The resulting **KM curve** is a step function that starts at 1 (everyone is event-free at the start) and drops at each event time. Each drop represents one or more events. When a censoring occurs, no drop happens — the individual is silently removed from the risk set for subsequent calculations. The curve flattens to a plateau if a substantial proportion of participants are censored before the event, reflecting uncertainty about long-term survival. A useful summary statistic is the **median survival time** — the time at which the curve crosses 0.5, meaning half the cohort has experienced the event. If the curve never reaches 0.5, the median cannot be estimated, which is itself informative.

KM curves become most powerful in comparison. When two groups are plotted together — treated vs. untreated, high-risk vs. low-risk — the visual separation of the curves communicates the magnitude and timing of the treatment effect. Curves that separate early and stay apart suggest an early, sustained benefit. Curves that cross suggest that one group does better initially but worse later (e.g., an aggressive treatment with short-term benefit but long-term harm). The **log-rank test** is the standard statistical test for comparing KM curves: it tests whether the observed vs. expected number of events differs between groups at each event time. The log-rank test, however, cannot estimate the size of the effect or adjust for confounders — that requires Cox regression, which builds directly on the conceptual foundation the KM estimator establishes.
