---
id: incidence-density-rates
title: Incidence Density and Rate Calculations
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: disease-frequency-measures
  type: hard
builds-toward:
- person-time-follow-up-studies
- kaplan-meier-estimator
tags:
- incidence-density
- rates
- person-years
- follow-up-studies
stage: advanced
status: draft
---

# Incidence Density and Rate Calculations

## Core Idea
Incidence density (also called incidence rate) is the frequency of new cases per person-time of observation, not per persons at risk. It is calculated as new cases / total person-time (e.g., cases per 1000 person-years). Incidence density accounts for varying follow-up times across participants and is appropriate when follow-up time varies substantially or when analyzing survival data.

## Explainer

From your study of disease frequency measures, you're familiar with **cumulative incidence** — the proportion of an initially disease-free population that develops disease over a defined period. Cumulative incidence works well when everyone is followed for the same length of time and nobody drops out. But in reality, cohort studies are messy: participants join at different times, some are lost to follow-up, some develop competing outcomes, and some studies run for decades. When follow-up times vary substantially across participants, cumulative incidence becomes misleading. A cohort where 10 cases occur in 1,000 people followed for one year and a cohort where 10 cases occur in 100 people followed for ten years look very different but yield the same cumulative incidence (1%). **Incidence density** solves this by shifting the denominator from persons to **person-time**.

The calculation is straightforward: count all new cases, divide by the total person-time contributed by all participants during their follow-up. **Person-time** is the sum of each individual's time at risk. If 4 participants are followed for 2 years, 3 years, 1 year, and 4 years respectively, total person-time is 10 person-years, regardless of whether any of them developed disease. A participant who leaves the study after 6 months contributes 0.5 person-years; they are not counted as if they were at risk for the full study period. The resulting rate — say, 3 cases per 10 person-years = 0.3 cases per person-year — captures the *instantaneous risk* of developing disease at any point in time, assuming that risk is constant over the follow-up period.

Incidence density has an important probabilistic interpretation: it represents the **force of morbidity** or, in mortality studies, the **hazard rate** — the instantaneous probability of experiencing the outcome per unit time, conditional on not yet having experienced it. This connects directly to the hazard function in survival analysis and is the quantity that Kaplan-Meier estimators and Cox proportional hazards models are fundamentally about. When you see a Cox model output a "hazard ratio" of 2.3 for a treatment, that means the incidence rate in the treatment group is 2.3 times that of the reference group at any instant during follow-up.

A practical nuance is the assumption of **constant hazard** over time. Incidence density as a summary measure assumes that the rate of new cases is roughly constant throughout follow-up. If disease risk is highly concentrated in early or late follow-up (as it often is), a single summary rate can obscure important temporal patterns. This is why survival analyses stratify time or use flexible hazard models rather than relying on a single aggregate rate. Understanding incidence density is not just a calculation skill — it is the conceptual foundation for all of time-to-event analysis.
