---
id: vaccine-effectiveness-evaluation
title: Vaccine Effectiveness Evaluation
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: herd-immunity-and-vaccination
  type: hard
- id: relative-risk-calculation
  type: soft
- id: antibody-structure-and-function
  type: soft
- id: adaptive-immune-response-kinetics
  type: soft
tags:
- vaccine-studies
- immunization-programs
- disease-prevention
stage: advanced
status: draft
---

# Vaccine Effectiveness Evaluation

## Core Idea
Vaccine effectiveness (VE) measures the proportional reduction in disease risk among vaccinated compared to unvaccinated populations under real-world field conditions—distinct from efficacy measured in randomized trials. VE is estimated using cohort and case-control designs and must account for vaccination coverage variations, waning immunity over time, and evolving population immunity. Time-stratified VE analysis reveals seasonal and temporal patterns. Modern efficient designs (screening method, test-negative) are increasingly used for evaluating influenza and other seasonal vaccines.

## How It's Best Learned
Calculate vaccine effectiveness from published cohort and case-control studies; implement test-negative design using flu surveillance data.

## Common Misconceptions
Vaccine effectiveness estimates are universally applicable across all populations and time periods. Efficacy measured in trials equals effectiveness in the field.

## Explainer

From your work on epidemiologic study designs, you know that randomized controlled trials (RCTs) are the gold standard for estimating causal effects. When a vaccine is tested in a phase III RCT — randomized assignment, blinded outcome assessment, controlled conditions — the result is **vaccine efficacy (VE_trial)**: the proportional reduction in disease incidence in vaccinated versus placebo recipients under ideal trial conditions. This number tells you what the vaccine can do. **Vaccine effectiveness (VE_field)** is different: it measures what the vaccine actually does in real-world populations, where vaccination is not randomized, conditions vary, strains drift, and immunity wanes. The gap between efficacy and effectiveness can be substantial and is the central focus of post-licensure vaccine surveillance.

The formula is the same regardless of study design: VE = 1 − RR (or 1 − OR when using case-control designs). If vaccinated individuals have 40% the disease risk of unvaccinated, VE = 1 − 0.40 = 60%. In a **cohort study**, you follow vaccinated and unvaccinated individuals and compare incidence rates — giving you a relative risk directly. In a **case-control study**, you compare vaccination status among cases and controls, yielding an odds ratio that approximates relative risk when disease is rare. Both designs require careful attention to confounding: vaccination status in real populations is not random. The **healthy vaccinee bias** — where healthier, more health-conscious people are more likely to get vaccinated — inflates VE estimates. Conversely, the **frailty bias** — where high-risk individuals are preferentially targeted for vaccination — deflates estimates. Uncontrolled confounders can make a marginally effective vaccine look excellent or an effective vaccine look useless.

The **test-negative design** is an elegant solution developed originally for influenza VE studies. Cases are patients who present to healthcare with flu-like illness and test positive for influenza; controls are patients with the same presentation who test negative. Because both groups sought care for similar symptoms, care-seeking behavior (a major confounder) is balanced between them. Vaccination status is then compared. The test-negative design removes the healthy-vaccinee bias almost entirely and is now the dominant design for rapid seasonal influenza effectiveness evaluation, requiring only routine surveillance data and no separate enrollment.

**Waning immunity** and **strain mismatch** are the two forces that make VE a moving target rather than a fixed property. Effectiveness against influenza declines measurably within a single season as vaccine-induced antibody titers fall and circulating strains evolve away from vaccine strains. For COVID-19, early VE estimates against severe disease exceeded 90% and fell substantially over 6–12 months. **Time-stratified VE analysis** — estimating effectiveness in strata defined by time since vaccination — captures this waning and informs booster timing decisions. Understanding that VE is not a single number but a function of pathogen, population, time, and endpoint (infection vs. symptomatic disease vs. hospitalization vs. death) is the key conceptual advance that separates sophisticated vaccine surveillance from naive headline-reading.
