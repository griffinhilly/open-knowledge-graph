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
stage: advanced
status: draft
---

# Person-Time Calculations and Follow-Up Study Design

## Core Idea
Person-time is the sum of follow-up time contributed by each study participant, accounting for censoring (participants lost, moving, or study completion). A person who contributes 5 years to follow-up contributes 5 person-years regardless of outcome status. Accurate person-time accounting is essential for incidence density calculations and is the denominator for rate-based measures in cohort studies.

## Explainer

From your study of incidence density rates, you already know that the **incidence rate** (or incidence density) is the number of new cases divided by the total person-time at risk. Person-time is the denominator — and getting that denominator right is the central challenge of follow-up study design. The concept feels simple (add up how long people were observed) but requires careful thinking about what "at risk" means and what to do when observations are incomplete.

The fundamental unit is the **person-year** (or person-month, person-day, depending on the disease timescale): one person followed for one year contributes 1 person-year; 100 people followed for 6 months each also contribute 50 person-years. This aggregation is what allows cohort studies to combine information across participants with different follow-up durations. The incidence rate then expresses the rate at which new events occur per unit of person-time at risk — it is interpretable as an instantaneous rate of event occurrence, not a simple proportion.

**Censoring** is what makes person-time calculations complex. A participant is censored when their follow-up ends before the study ends without experiencing the outcome. The three main censoring reasons are: loss to follow-up (moved away, withdrew), administrative censoring (study ended while they were still event-free), and competing events (died of something unrelated, making them no longer at risk for the outcome). Each censored participant contributes only the time they were actually observed. A 10-year study participant who moves away after 3 years contributes 3 person-years — not 10, not zero. This is the correct accounting under the key assumption that **censoring is non-informative**: that censored participants are no more or less likely to have had the outcome than those who remained under observation.

The practical mechanics matter. Typically, each participant's contributed time = (date of outcome or censoring) − (date of study entry). In a simple cohort, you sum these individual intervals. For a constant-rate incidence rate calculation: IR = (number of new cases) / (total person-years). If 20 new cases occur among a cohort contributing 4,000 person-years, the incidence rate is 20/4,000 = 0.005 cases per person-year, or 5 cases per 1,000 person-years. This rate is directly comparable across studies with different observation periods and recruitment patterns, which is the major advantage of person-time analysis over simple cumulative incidence. When rates differ across subgroups or over time, the person-time framework extends naturally into the Cox proportional hazards model — the standard tool for multivariable analysis of time-to-event data that you will study next.
