---
id: disability-adjusted-life-years
title: Disability-Adjusted Life Years (DALYs)
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: global-burden-of-disease
  type: hard
- id: disease-frequency-measures
  type: hard
- id: life-table-construction-and-interpretation
  type: soft
builds-toward:
- cost-effectiveness-analysis-epidemiology
tags:
- burden-of-disease
- health-metrics
- priority-setting
stage: advanced
status: draft
---

# Disability-Adjusted Life Years (DALYs)

## Core Idea
Disability-adjusted life years (DALYs) quantify total disease burden as the sum of years lost to premature death (YLL) and years lived with disability (YLD). Calculation requires age-specific mortality data, disability weights reflecting severity of each health state, and duration. DALYs enable cross-disease comparison and priority-setting for public health interventions. The Global Burden of Disease study produces standardized DALY estimates, though methods for assigning disability weights and social weighting (age-weighting, time-discounting) remain methodologically contested.

## How It's Best Learned
Calculate DALYs for multiple disease conditions using GBD methods; review GBD results and compare disease burden rankings.

## Common Misconceptions
Higher DALY burden means a disease is inherently 'worse' (reflects both severity and frequency). Disability weights are objectively measured rather than value-laden.

## Explainer

From your study of disease frequency measures and the global burden of disease, you know that mortality statistics — death rates, years of life lost — capture only part of the picture. Two diseases that kill at the same rate can have vastly different impacts on quality of life in the years before death, and a disease that rarely kills but chronically disables millions may impose a larger societal burden than a rapidly lethal but rare condition. **Disability-Adjusted Life Years (DALYs)** were designed to create a single metric that integrates both premature death and non-fatal health loss, enabling comparison across completely different disease types.

A DALY is built from two components. **Years of Life Lost (YLL)** captures premature mortality: multiply the number of deaths at each age by the years of life remaining at that age according to a reference life table (you've worked with life tables in your prerequisite). **Years Lived with Disability (YLD)** captures morbidity: multiply the prevalence (or incidence) of a condition by its **disability weight** and by duration. Disability weights are numbers between 0 (perfect health) and 1 (equivalent to death), derived from population surveys asking people to compare hypothetical health states. Blindness might receive a weight of 0.195, severe depression 0.658, lower back pain 0.269. Total DALYs = YLL + YLD. One DALY represents one year of healthy life lost, either through death or through disability.

The power of DALYs is cross-disease comparison. Mental health disorders score very high on DALY burden because they are highly prevalent, begin early in life (maximizing YLL if they shorten life, or long YLD duration if they don't), and carry non-trivial disability weights. Infectious diseases with high mortality in young children score heavily on YLL because dying at age 2 eliminates many potential life-years. This framing helped reposition mental health, musculoskeletal disorders, and substance use as major global health priorities — they had been underrepresented in frameworks that tracked only death.

The methodology carries real value judgments, and this is the most important thing to understand critically. **Disability weights** are not biological constants — they are survey responses from populations that may not include the people living with those conditions. Advocacy communities for disabilities have contested weights that imply their lives are worth substantially less than healthy lives. Historical GBD methods also used **age-weighting** (counting life-years in young adults as more valuable) and **time discounting** (counting future years as less valuable) — both of which have been criticized on equity grounds and have been modified or removed in more recent GBD iterations. DALYs are an indispensable planning tool, but interpreting them requires knowing which values were baked in.
