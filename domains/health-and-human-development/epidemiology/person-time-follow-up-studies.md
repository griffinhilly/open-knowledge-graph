---
id: person-time-follow-up-studies
title: Person-Time Calculations and Follow-Up Study Design
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: incidence-density-rates
  type: hard
builds-toward:
- cox-proportional-hazards
tags:
- person-years
- follow-up
- cohort-studies
- censoring
stage: expert
status: draft
---

# Person-Time Calculations and Follow-Up Study Design

## Core Idea
Person-time is the sum of follow-up time contributed by each study participant, accounting for censoring (participants lost, moving, or study completion). A person who contributes 5 years to follow-up contributes 5 person-years regardless of outcome status. Accurate person-time accounting is essential for incidence density calculations and is the denominator for rate-based measures in cohort studies.

## Questions

```yaml
- question: "In a 10-year cohort study, participant A develops the outcome at year 7. Participant B is lost to follow-up after 3 years without experiencing the outcome. How much person-time does each contribute?"
  type: multiple-choice
  options:
    - "A contributes 7 person-years; B contributes 0 (censored participants are excluded)"
    - "A contributes 10 person-years; B contributes 10 person-years (both enrolled for the full study)"
    - "A contributes 7 person-years; B contributes 3 person-years (each contributes until follow-up ends)"
    - "A contributes 7 person-years; B contributes 10 person-years (B assumed event-free for full study)"
  answer: 2
  explanation: "A contributes time until the outcome event — 7 years. B contributes time until censoring — 3 years. Censored participants are NOT excluded (option 0 is wrong); their follow-up time correctly contributes to the denominator. They are NOT assigned the full study duration (options 1 and 3) because we don't know what happened after loss to follow-up. Each participant contributes exactly the time they were actually observed — this is the fundamental accounting principle of person-time analysis."

- question: "A cohort study records 25 new cases among 500 participants. After accounting for losses to follow-up, the total person-time is 2,200 person-years rather than the maximum possible 2,500. What is the correct incidence rate?"
  type: multiple-choice
  options:
    - "5 cases per 100 participants (25/500)"
    - "11.4 cases per 1,000 person-years (25/2,200 × 1,000)"
    - "10 cases per 1,000 person-years (25/2,500 × 1,000)"
    - "5% incidence (25/500 = 0.05)"
  answer: 1
  explanation: "The incidence rate uses the actual observed person-time denominator: 25 ÷ 2,200 = 0.01136 per person-year = 11.4 per 1,000 person-years. Using 2,500 person-years (option 2) would underestimate the rate by pretending censored participants contributed time they didn't. Options 0 and 3 calculate cumulative incidence (a proportion), not an incidence rate — they ignore unequal follow-up duration entirely and cannot be directly compared across studies with different designs."

- question: "A participant who leaves a cohort study early (lost to follow-up) should be excluded from the analysis to prevent bias."
  type: true-false
  answer: false
  explanation: "Excluding censored participants would both waste valid data and introduce bias. Their observed follow-up time correctly contributes to the person-time denominator up to the point of censoring. Person-time analysis was specifically designed to handle incomplete follow-up: each participant contributes what was actually observed. Systematic exclusion of censored participants would remove those who may differ from completers in important ways, potentially biasing incidence estimates more than proper censoring handling does."

- question: "The incidence rate calculated using person-time is comparable across studies with very different follow-up durations, because it accounts for how long each person was actually observed."
  type: true-false
  answer: true
  explanation: "This is the key advantage of person-time analysis. Whether participants are followed for 1 year or 8 years, their contributions to the denominator are proportional to actual observation time. The resulting incidence rate (cases per person-year) is a rate — an intensity of event occurrence per unit of time — that is directly comparable across studies with different designs, enrollment windows, and follow-up durations. Simple cumulative incidence (a proportion) cannot do this because it depends on the length of the observation period."

- question: "What is 'non-informative censoring,' and why is it an important assumption underlying person-time analysis?"
  type: short-answer
  answer: "Non-informative censoring means the reason a participant's follow-up ended does not predict whether they would have experienced the outcome. Under this assumption, censored participants are representative of those who remained under observation — their unobserved future is similar to the observed future of those who stayed. If censoring is informative (e.g., sick participants are more likely to drop out), the incidence rate will be biased because censored individuals are not exchangeable with those still under observation."
  explanation: "This is why high loss to follow-up threatens validity in cohort studies — not because censoring itself is wrong, but because informative censoring violates the exchangeability assumption. Investigators minimize this threat by tracking participants aggressively, investigating reasons for dropout, and using sensitivity analyses to test how much informative censoring could plausibly change their conclusions."
```

## Explainer

From your study of incidence density rates, you already know that the **incidence rate** (or incidence density) is the number of new cases divided by the total person-time at risk. Person-time is the denominator — and getting that denominator right is the central challenge of follow-up study design. The concept feels simple (add up how long people were observed) but requires careful thinking about what "at risk" means and what to do when observations are incomplete.

The fundamental unit is the **person-year** (or person-month, person-day, depending on the disease timescale): one person followed for one year contributes 1 person-year; 100 people followed for 6 months each also contribute 50 person-years. This aggregation is what allows cohort studies to combine information across participants with different follow-up durations. The incidence rate then expresses the rate at which new events occur per unit of person-time at risk — it is interpretable as an instantaneous rate of event occurrence, not a simple proportion.

**Censoring** is what makes person-time calculations complex. A participant is censored when their follow-up ends before the study ends without experiencing the outcome. The three main censoring reasons are: loss to follow-up (moved away, withdrew), administrative censoring (study ended while they were still event-free), and competing events (died of something unrelated, making them no longer at risk for the outcome). Each censored participant contributes only the time they were actually observed. A 10-year study participant who moves away after 3 years contributes 3 person-years — not 10, not zero. This is the correct accounting under the key assumption that **censoring is non-informative**: that censored participants are no more or less likely to have had the outcome than those who remained under observation.

The practical mechanics matter. Typically, each participant's contributed time = (date of outcome or censoring) − (date of study entry). In a simple cohort, you sum these individual intervals. For a constant-rate incidence rate calculation: IR = (number of new cases) / (total person-years). If 20 new cases occur among a cohort contributing 4,000 person-years, the incidence rate is 20/4,000 = 0.005 cases per person-year, or 5 cases per 1,000 person-years. This rate is directly comparable across studies with different observation periods and recruitment patterns, which is the major advantage of person-time analysis over simple cumulative incidence. When rates differ across subgroups or over time, the person-time framework extends naturally into the Cox proportional hazards model — the standard tool for multivariable analysis of time-to-event data that you will study next.
