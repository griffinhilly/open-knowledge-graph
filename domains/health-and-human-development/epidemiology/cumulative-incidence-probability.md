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
stage: advanced
status: draft
---

# Cumulative Incidence and Risk Estimation

## Core Idea
Cumulative incidence is the probability that an individual will experience an outcome over a defined time period, calculated as new outcomes divided by number at-risk. Unlike incidence rate, cumulative incidence accounts for loss to follow-up and varying follow-up durations, making it appropriate for communicating risk to patients.

## Explainer

From your prerequisite on disease frequency measures, you know that epidemiology distinguishes **prevalence** (existing cases at a snapshot in time) from **incidence** (new cases arising over a period). Within incidence, your person-time work introduced the **incidence rate** — events divided by total person-time at risk — as the appropriate measure when participants are followed for variable durations. **Cumulative incidence** is a distinct and complementary measure: it answers the question "what is the probability that a currently disease-free person will develop the outcome within a specified time window?" The time window is integral to the definition — cumulative incidence without a time horizon is meaningless.

The conceptual core of cumulative incidence is that it is a **probability**, bounded between 0 and 1, and directly interpretable as a **risk**. If you follow 1,000 cancer-free individuals for 5 years and 80 develop cancer, the 5-year cumulative incidence is 80/1,000 = 8%. You can tell a patient: "Your 5-year risk of developing this cancer is approximately 8%." This risk-format interpretation is why clinicians prefer cumulative incidence for patient communication, even when incidence rates are more appropriate for statistical modeling. The two are mathematically related: when the outcome is rare and the follow-up period is short, cumulative incidence ≈ incidence rate × time. At longer durations or higher rates, this approximation breaks down and the two diverge substantially.

The practical complication is **censoring** — participants who are lost to follow-up, withdraw, or have their observation period end before the study window closes. The simple formula (events / starting population) implicitly assumes everyone is followed for the full period, which is never true in practice. Censored individuals contributed risk time for part of the period but are not events; including them in the denominator as if they were fully followed overestimates the at-risk population and underestimates risk. The **Kaplan-Meier estimator** handles this correctly: it treats each event time as a distinct step, multiplying survival probabilities sequentially and treating censored observations appropriately between steps. The resulting **survival curve** traces the probability of remaining event-free over time; cumulative incidence at any time point is 1 minus the corresponding survival probability.

**Competing risks** introduce a further complication that your next topic addresses directly. If study participants can experience the outcome of interest (cancer death) or a competing event (cardiovascular death), and dying of one precludes the other, then treating competing events as ordinary censoring inflates the cumulative incidence of the primary outcome. This is because censoring assumes the censored individual remains at risk — but a participant who died of cardiovascular disease is no longer at risk of cancer death. **Competing risks methods** — including the cause-specific hazard and the **cumulative incidence function** (Gray's method) — handle this correctly. The transition from simple cumulative incidence to competing risks illustrates a general principle: the appropriate epidemiological method depends on correctly specifying what "at risk" means in the biological and clinical context of the outcome being studied.
