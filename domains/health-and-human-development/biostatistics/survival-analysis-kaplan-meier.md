---
id: survival-analysis-kaplan-meier
title: 'Survival Analysis: Kaplan-Meier Estimation'
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: study-design-biostatistics
  type: hard
- id: probability-theory
  type: soft
- id: descriptive-statistics
  type: soft
builds-toward:
- log-rank-test
- cox-proportional-hazards-detailed
tags:
- survival
- Kaplan-Meier
- censoring
- survival-function
- time-to-event
stage: advanced
status: validated
---

# Survival Analysis: Kaplan-Meier Estimation

## Core Idea
Survival analysis studies time-to-event outcomes — time to death, disease recurrence, or hospital readmission. The defining challenge is censoring: some subjects have not yet experienced the event when observation ends, so their true event times are unknown but known to exceed the censored time. The Kaplan-Meier estimator is a nonparametric method that estimates the survival function S(t) — the probability of surviving beyond time t — by computing the cumulative product of conditional survival probabilities at each observed event time. It produces the characteristic step-function survival curve that declines at each event, properly accounting for censored observations by removing them from the risk set without treating them as events.

## Questions

```yaml
- question: "In a clinical trial, Patient A dies at month 6 and Patient B is lost to follow-up at month 6. How does the Kaplan-Meier estimator treat these two observations differently?"
  type: multiple-choice
  options:
    - "Both are treated identically — both reduce the survival estimate at month 6"
    - "Patient A causes a step down in the survival curve (an event); Patient B is removed from the risk set at month 6 without causing a step down (censored)"
    - "Patient A is counted; Patient B is excluded from the analysis entirely"
    - "Patient B's survival time is imputed as the median follow-up time"
  answer: 1
  explanation: "This is the fundamental distinction in survival analysis. Patient A experienced the event (death), so the survival estimate decreases at month 6. Patient B was censored — we know they survived at least 6 months, but not how long after. The Kaplan-Meier estimator uses this information by keeping Patient B in the risk set (the denominator) for all times up to month 6, then removing them. They contribute survival information up to their censoring time without being counted as an event. Excluding them entirely (option C) would waste information; treating them as events (option A) would bias survival downward."

- question: "A Kaplan-Meier curve shows that the 1-year survival probability for Treatment A is 70% and for Treatment B is 55%. This means Treatment A is statistically significantly better than Treatment B."
  type: true-false
  answer: false
  explanation: "The Kaplan-Meier curve is a descriptive estimate — it shows the estimated survival function but does not perform a hypothesis test. The apparent difference between 70% and 55% could be due to chance, especially with small samples or wide confidence intervals. A formal statistical test (the log-rank test) is needed to determine whether the difference is statistically significant. The curves might also cross at other time points, complicating interpretation even if the difference at one year appears large."

- question: "The Kaplan-Meier estimator assumes that censoring is non-informative — that is, censored subjects have the same future survival prospects as those who remain under observation. Why is this assumption critical?"
  type: short-answer
  answer: "If censoring is related to prognosis — for example, sicker patients drop out because they seek alternative treatment or are too ill to continue — then censored subjects have different survival prospects than those remaining. The KM estimator treats censored subjects as having the same future risk as continuing subjects, so informative censoring biases the survival estimate upward (if sicker patients leave) or downward (if healthier patients leave). The survival curve would no longer represent the true survival experience of the population."
  explanation: "Non-informative censoring means that the reason for censoring is independent of the event process. Administrative censoring (study ends) and staggered entry (patients enroll at different times) are typically non-informative. Loss to follow-up is potentially informative if sicker or healthier patients are differentially lost. When informative censoring is suspected, sensitivity analyses or joint models of the event and censoring processes are needed."

- question: "Why does the Kaplan-Meier estimator use a product of conditional probabilities rather than simply dividing the number of survivors by the total number of subjects at each time point?"
  type: short-answer
  answer: "Censoring changes the number of subjects at risk over time. A simple proportion (survivors / total enrolled) would either ignore censored subjects (underestimating survival by treating missing data as events) or count them as alive (overestimating survival by assuming they all survived). The product-limit approach computes the conditional probability of surviving each event time given survival up to that point, using only subjects still at risk. Multiplying these conditional probabilities gives the cumulative survival probability that correctly accounts for the changing risk set."
  explanation: "At each event time t_i, the KM estimator computes (n_i - d_i)/n_i, where n_i is the number at risk (alive and uncensored just before t_i) and d_i is the number of events at t_i. The cumulative product S(t) = product of all these conditional survival probabilities up to time t. Censored subjects reduce n_i at the time of censoring but never appear in d_i. This product-limit formula was proposed by Kaplan and Meier in 1958 and remains the standard nonparametric survival estimator."
```

## Explainer

Standard statistical methods assume you observe the outcome for every subject, but time-to-event data violates this assumption. In a 5-year clinical trial, some patients die (the event of interest), some are still alive when the trial ends (administratively censored), and some are lost to follow-up before the trial ends (right-censored). You know these censored patients survived at least until they were last observed, but you do not know their true event time. Ignoring censored observations — either by excluding them or by treating them as events — introduces serious bias. Survival analysis methods exist precisely to handle this incomplete information.

The **Kaplan-Meier estimator** constructs the survival function S(t) — the probability of surviving beyond time t — without assuming any particular distributional form. At each observed event time, it computes the conditional probability of surviving past that time given survival up to it: (number at risk - number of events) / number at risk. The cumulative survival probability is the product of all these conditional probabilities up to time t. The resulting **step function** starts at S(0) = 1 and decreases at each event time. Censored observations reduce the risk set (the denominator) at the censoring time but do not cause a step down — they contribute information about survival up to the moment they were last observed.

Reading a Kaplan-Meier curve is a core clinical skill. The **median survival time** is the time at which the curve crosses 0.50 — the time by which half the subjects have experienced the event. If the curve never reaches 0.50, the median is undefined (more than half the subjects survived the entire observation period). Confidence intervals for the survival function at any time point can be computed using Greenwood's formula, and these widen over time as the number at risk decreases. Tick marks on the curve indicate censoring events, showing where observations were lost. A curve with heavy censoring late in follow-up has wide uncertainty, even if it appears to plateau.

The critical assumption underlying the KM estimator is **non-informative censoring**: the reason a subject was censored must be unrelated to their prognosis. If patients who are getting sicker preferentially drop out (informative censoring), the remaining subjects are healthier than the full cohort, and the survival curve will be optimistically biased. This assumption cannot be tested from the data alone — it requires understanding why subjects were censored. The Kaplan-Meier estimator describes the survival experience of a single group; to compare survival between groups, you need the log-rank test, which is the next topic in this sequence.
