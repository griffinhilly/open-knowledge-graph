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
stage: expert
status: validated
---

# Kaplan-Meier Survival Analysis and Curves

## Core Idea
The Kaplan-Meier estimator is a non-parametric method for estimating survival probability over time, properly accounting for censored observations. It calculates the cumulative probability of surviving to each event time by multiplying conditional survival probabilities. Kaplan-Meier curves allow visual comparison of survival between groups and provide median survival estimates, forming the foundation for survival analysis.

## Questions

```yaml
- question: "In a clinical trial with 100 patients, 60 experienced the event and 40 were censored (lost to follow-up or study ended). How does the Kaplan-Meier estimator handle the 40 censored patients?"
  type: multiple-choice
  options:
    - "They are excluded because their outcomes are unknown, leaving 60 patients for analysis"
    - "They are counted as having experienced the event at their censoring time, to be conservative"
    - "They contribute survival time up to their censoring date, then are removed from the risk set for all subsequent event times"
    - "Their outcomes are imputed based on the average time-to-event of similar patients who experienced the event"
  answer: 2
  explanation: "A censored participant is not missing data — their censoring time is real information: this person survived at least until that point. The KM estimator uses this by including them in the risk set up to their censoring time (contributing to the denominator in conditional survival calculations) and then removing them from the risk set going forward. Option A would discard real survival information and overestimate event rates. Option B would introduce false events and underestimate survival. The KM estimator's handling of censoring is its central innovation."

- question: "Two groups are shown on a Kaplan-Meier plot. The curves cross at month 18: Group A has better survival for the first 18 months, but Group B has better survival thereafter. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The analysis contains an error — properly constructed KM curves cannot cross"
    - "The two treatments have identical overall survival and any apparent difference is random noise"
    - "The relative survival benefit changes over time — Group A's treatment may have early benefit but late harm, or the groups have time-varying hazard differences"
    - "The log-rank test result is automatically invalid whenever curves cross"
  answer: 2
  explanation: "Crossing KM curves are clinically meaningful and occur when the relative hazard between groups is not constant over time. An aggressive treatment might reduce early mortality but carry late toxicity that reverses the advantage. Curves that cross violate the proportional hazards assumption — which affects the log-rank test's sensitivity — but crossing is not an analysis error. It reflects real biology and is important clinical information about when and for whom a treatment is beneficial."

- question: "A censored observation in survival analysis contains real information: it establishes that the participant survived at least until the time of censoring."
  type: true-false
  answer: true
  explanation: "Censoring is not the same as a missing outcome. If a participant was followed for 3 years without experiencing the event before dropping out, we know they survived for at least 3 years. The KM estimator uses this information: the participant remains in the risk set for all event times up to their censoring point, contributing to the numerator and denominator of conditional survival estimates throughout that window. Treating such an observation as missing would waste real data."

- question: "If a Kaplan-Meier curve never drops below 0.5, it means all participants in the study survived to the end of follow-up."
  type: true-false
  answer: false
  explanation: "A KM curve that never reaches 0.5 means the median survival time cannot be estimated — not that all participants survived. This occurs when fewer than half the cohort experienced the event during follow-up, which can happen because of a high censoring rate, a short follow-up period, or genuinely excellent survival. The curve staying above 0.5 could reflect either a truly favorable outcome or heavy censoring, and distinguishing these interpretations requires examining the data carefully."

- question: "Explain why simply excluding censored observations from a survival analysis would produce biased results, and describe how the Kaplan-Meier estimator avoids this problem."
  type: short-answer
  answer: "Excluding censored observations creates survivorship bias: only participants who experienced the event would contribute to the analysis. Since censored participants are typically people who survived longer (otherwise they would have experienced the event), excluding them overestimates the event rate and underestimates survival time. Counting them as events does the reverse. The KM estimator avoids both errors by using censored participants for the time they were observed — including them in the risk set up to their censoring date — then removing them from subsequent calculations without assigning an outcome."
  explanation: "The product-limit formula achieves unbiased estimates by computing conditional survival probabilities at each event time. The denominator (number at risk) reflects all participants still under observation at that moment. When a censoring occurs between event times, the risk set decreases silently — no drop in the survival curve. This approach is unbiased under the assumption that censoring is independent of the event, which is the key underlying assumption of the KM method."
```

## Explainer

From your study of disease frequency measures and person-time, you know that **incidence** — the rate at which new events occur in a population over time — requires careful accounting for how long each person was under observation. Not everyone is followed for the same duration, and some people experience the outcome while others do not. **Survival analysis** is the branch of statistics built specifically for this situation: you have time-to-event data, you want to estimate the probability of an event occurring by a given time, and you have to handle the fact that some participants never experienced the event during follow-up.

The fundamental challenge is **censoring**. A participant is censored if they leave follow-up before the event occurs — they moved away, the study ended, or they were lost to follow-up. A censored observation is not a "missing" outcome in the usual sense; it is real information: this person survived at least until the censoring time. Simply ignoring censored participants would overestimate survival (you're only counting people who experienced the event) while counting them as events would underestimate it. The Kaplan-Meier estimator threads this needle by using censored observations fully for the time they were observed, then removing them from the risk set when they are censored.

The **Kaplan-Meier (KM) estimator** works by computing survival probability as a product of conditional probabilities. At each time point when an event occurs, it estimates the probability of surviving past that moment given survival up to that point: (number at risk − number with events) / (number at risk). It then multiplies all these conditional probabilities together up to time t to get the cumulative survival probability S(t). This is the **product-limit estimator** — "product" because survival over an interval is the product of survival conditional on each event time; "limit" because the estimator uses actual event times, not arbitrary time intervals. The formula is: S(t) = ∏ [(n_i − d_i) / n_i] for all event times t_i ≤ t, where n_i is the number at risk and d_i is the number of events at time t_i.

The resulting **KM curve** is a step function that starts at 1 (everyone is event-free at the start) and drops at each event time. Each drop represents one or more events. When a censoring occurs, no drop happens — the individual is silently removed from the risk set for subsequent calculations. The curve flattens to a plateau if a substantial proportion of participants are censored before the event, reflecting uncertainty about long-term survival. A useful summary statistic is the **median survival time** — the time at which the curve crosses 0.5, meaning half the cohort has experienced the event. If the curve never reaches 0.5, the median cannot be estimated, which is itself informative.

KM curves become most powerful in comparison. When two groups are plotted together — treated vs. untreated, high-risk vs. low-risk — the visual separation of the curves communicates the magnitude and timing of the treatment effect. Curves that separate early and stay apart suggest an early, sustained benefit. Curves that cross suggest that one group does better initially but worse later (e.g., an aggressive treatment with short-term benefit but long-term harm). The **log-rank test** is the standard statistical test for comparing KM curves: it tests whether the observed vs. expected number of events differs between groups at each event time. The log-rank test, however, cannot estimate the size of the effect or adjust for confounders — that requires Cox regression, which builds directly on the conceptual foundation the KM estimator establishes.
