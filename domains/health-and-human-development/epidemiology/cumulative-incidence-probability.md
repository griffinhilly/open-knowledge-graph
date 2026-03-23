---
id: cumulative-incidence-probability
title: Cumulative Incidence and Risk Estimation
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: disease-frequency-measures
  type: hard
- id: person-time-follow-up-studies
  type: hard
builds-toward:
- competing-risks-analysis
- life-table-methods
tags:
- incidence
- risk
- probability
- follow-up-studies
stage: expert
status: draft
---

# Cumulative Incidence and Risk Estimation

## Core Idea
Cumulative incidence is the probability that an individual will experience an outcome over a defined time period, calculated as new outcomes divided by number at-risk. Unlike incidence rate, cumulative incidence accounts for loss to follow-up and varying follow-up durations, making it appropriate for communicating risk to patients.

## Questions

```yaml
- question: "A study follows 500 people for 5 years to estimate cumulative incidence. By year 5, 50 people developed the outcome. Another 100 people were lost to follow-up at various points. A researcher computes 5-year CI as 50/500 = 10%. What is the fundamental problem?"
  type: multiple-choice
  options:
    - "The numerator should include people lost to follow-up as potential cases"
    - "The denominator treats all 500 as followed for the full 5 years, ignoring that censored individuals contributed less than 5 years of risk time — overstating the at-risk pool and underestimating true risk"
    - "Cumulative incidence cannot be calculated over 5 years; it requires 10-year follow-up"
    - "The formula is correct; loss to follow-up does not affect the denominator"
  answer: 1
  explanation: "Censored individuals were not followed to the event endpoint. Including them as full observations assumes they were at risk the entire period — overstating the denominator and underestimating risk. The Kaplan-Meier estimator corrects this by updating the at-risk count at each event time."

- question: "In a 5-year study, the incidence rate is 0.02 per person-year. A colleague argues that the 5-year cumulative incidence is simply 0.02 × 5 = 0.10. This approximation is:"
  type: multiple-choice
  options:
    - "Always correct — cumulative incidence equals rate × time by definition"
    - "A valid approximation when outcomes are rare and follow-up is short, but increasingly incorrect as rates rise or durations lengthen"
    - "Only valid for propagated outbreaks, not cohort studies"
    - "Correct only when there is no censoring"
  answer: 1
  explanation: "When the outcome is rare and the time window short, CI ≈ rate × time. At longer durations or higher rates, this diverges substantially — the incidence rate is an instantaneous measure that assumes a constant hazard, while cumulative incidence is bounded at 1.0 and accounts for the shrinking at-risk pool."

- question: "A cumulative incidence of 15% is fully interpretable without knowing the time period over which it was calculated."
  type: true-false
  answer: false
  explanation: "Time horizon is integral to the definition of cumulative incidence — it answers 'probability of outcome within a specified window.' Without specifying that window (e.g., '5-year cumulative incidence'), the figure is meaningless. An annual CI of 15% and a 20-year CI of 15% convey entirely different levels of risk."

- question: "The Kaplan-Meier estimator handles censoring by updating the at-risk denominator at each event time, allowing survival probability to be estimated even when participants leave the study at different times."
  type: true-false
  answer: true
  explanation: "Kaplan-Meier works step by step: at each event time, it multiplies the cumulative survival probability by the conditional probability of surviving that step, using only individuals still under observation. Censored individuals are removed from the at-risk count before the next step — they neither inflate nor deflate the denominator inappropriately."

- question: "Why can't competing events (such as deaths from other causes) simply be treated as ordinary censored observations when calculating cumulative incidence for a specific outcome?"
  type: short-answer
  answer: "Ordinary censoring assumes the individual remains at risk of the outcome after they leave observation — it treats their future as unobserved but possible. A participant who dies of cardiovascular disease is no longer at risk of dying from cancer; treating their death as censoring implies they could still develop cancer, which inflates the cumulative incidence of cancer. Competing risks methods (e.g., cause-specific hazards, Gray's method) correctly account for this by recognizing that one event permanently removes the individual from the risk set for the other."
  explanation: "This is the central conceptual gap between simple cumulative incidence and competing risks analysis. Censoring is appropriate for dropout or administrative end-of-study; it is inappropriate for events that biologically preclude the outcome of interest. Ignoring competing risks systematically overstates the probability of the primary outcome."
```

## Explainer

From your prerequisite on disease frequency measures, you know that epidemiology distinguishes **prevalence** (existing cases at a snapshot in time) from **incidence** (new cases arising over a period). Within incidence, your person-time work introduced the **incidence rate** — events divided by total person-time at risk — as the appropriate measure when participants are followed for variable durations. **Cumulative incidence** is a distinct and complementary measure: it answers the question "what is the probability that a currently disease-free person will develop the outcome within a specified time window?" The time window is integral to the definition — cumulative incidence without a time horizon is meaningless.

The conceptual core of cumulative incidence is that it is a **probability**, bounded between 0 and 1, and directly interpretable as a **risk**. If you follow 1,000 cancer-free individuals for 5 years and 80 develop cancer, the 5-year cumulative incidence is 80/1,000 = 8%. You can tell a patient: "Your 5-year risk of developing this cancer is approximately 8%." This risk-format interpretation is why clinicians prefer cumulative incidence for patient communication, even when incidence rates are more appropriate for statistical modeling. The two are mathematically related: when the outcome is rare and the follow-up period is short, cumulative incidence ≈ incidence rate × time. At longer durations or higher rates, this approximation breaks down and the two diverge substantially.

The practical complication is **censoring** — participants who are lost to follow-up, withdraw, or have their observation period end before the study window closes. The simple formula (events / starting population) implicitly assumes everyone is followed for the full period, which is never true in practice. Censored individuals contributed risk time for part of the period but are not events; including them in the denominator as if they were fully followed overestimates the at-risk population and underestimates risk. The **Kaplan-Meier estimator** handles this correctly: it treats each event time as a distinct step, multiplying survival probabilities sequentially and treating censored observations appropriately between steps. The resulting **survival curve** traces the probability of remaining event-free over time; cumulative incidence at any time point is 1 minus the corresponding survival probability.

**Competing risks** introduce a further complication that your next topic addresses directly. If study participants can experience the outcome of interest (cancer death) or a competing event (cardiovascular death), and dying of one precludes the other, then treating competing events as ordinary censoring inflates the cumulative incidence of the primary outcome. This is because censoring assumes the censored individual remains at risk — but a participant who died of cardiovascular disease is no longer at risk of cancer death. **Competing risks methods** — including the cause-specific hazard and the **cumulative incidence function** (Gray's method) — handle this correctly. The transition from simple cumulative incidence to competing risks illustrates a general principle: the appropriate epidemiological method depends on correctly specifying what "at risk" means in the biological and clinical context of the outcome being studied.
