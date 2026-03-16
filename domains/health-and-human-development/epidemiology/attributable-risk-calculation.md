---
id: attributable-risk-calculation
title: Attributable Risk and Population Attributable Fraction
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: relative-risk-calculation
  type: hard
- id: odds-ratio-interpretation
  type: soft
builds-toward:
- number-needed-to-treat
tags:
- attributable-risk
- public-health-impact
- prevention
stage: advanced
status: draft
---

# Attributable Risk and Population Attributable Fraction

## Core Idea
Attributable risk (AR) quantifies the absolute excess risk due to exposure: AR = Risk(Exposed) – Risk(Unexposed). Population attributable fraction (PAF) indicates what proportion of disease in the population results from exposure, accounting for both the RR and the prevalence of exposure. AR and PAF are essential for setting public health priorities.

## Explainer

You already know from relative risk (RR) that it answers the question: "How many times more likely is disease in the exposed group compared to the unexposed?" But RR, powerful as it is, tells you nothing about the actual burden of disease attributable to that exposure, nor about the potential impact of eliminating it. **Attributable risk (AR)** — also called the **risk difference** — closes this gap by subtracting: AR = Risk(Exposed) − Risk(Unexposed). If exposed workers have a 10% five-year risk of lung disease and unexposed workers have a 2% risk, AR = 8%. That 8% represents the absolute excess disease that would not occur if the exposure were eliminated — the directly preventable fraction among those who were exposed.

Consider two exposures with the same RR of 5 but very different baseline risks. Exposure A raises risk from 1% to 5% (AR = 4%). Exposure B raises risk from 20% to 100% (AR = 80%). The RR is identical, but exposure B is responsible for a vastly greater number of cases per 100 exposed people. This is why AR, not RR, is the correct metric for estimating clinical or policy impact: it tells you the absolute number of cases that an intervention could prevent per unit of exposed population.

The **population attributable fraction (PAF)** takes this logic to the population level, asking: "What proportion of all disease cases in the entire population — exposed and unexposed combined — are attributable to this exposure?" The formula is PAF = Pe(RR − 1) / [1 + Pe(RR − 1)], where Pe is the prevalence of exposure in the population. Alternatively, PAF = (Risk_population − Risk_unexposed) / Risk_population. The PAF depends on both the strength of the association (RR) and how common the exposure is. A moderately risky exposure that affects 60% of the population (e.g., physical inactivity) can have a larger PAF than a highly risky exposure that affects 1% (e.g., a rare occupational toxin), even though the individual risk ratio for the rare exposure is much higher.

This is the core insight for public health prioritization: **high PAF exposures are the ones where population-wide interventions yield the greatest disease reduction**. Smoking cessation campaigns, physical activity programs, and dietary interventions target exposures with both substantial RR and high prevalence, resulting in large PAF values. When setting policy, comparing PAFs across exposures — not just RRs — allows health authorities to allocate resources where elimination or reduction of exposure would prevent the most disease at the population level.
