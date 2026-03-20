---
id: population-attributable-risk-and-impact
title: Population Attributable Risk and Disease Burden Estimation
domain: health-and-human-development
course: public-health
prerequisites:
- id: relative-risk-calculation
  type: hard
- id: disease-frequency-measures
  type: hard
builds-toward:
- burden-of-disease-and-comparative-health-assessment
- policy-analysis-and-health-impact-evaluation
tags:
- epidemiology
- burden-of-disease
- risk-metrics
stage: advanced
status: draft
---

# Population Attributable Risk and Disease Burden Estimation

## Core Idea
Population attributable risk (PAR) combines the strength of association between a risk factor and disease with the prevalence of that factor to estimate the disease burden potentially preventable by eliminating the exposure. PAR differs from relative risk (individual-level) and is essential for prioritizing public health resources. A weak risk factor with high prevalence may have greater PAR than a strong risk factor affecting few people.

## How It's Best Learned
Calculate PAR for multiple risk factors in the same disease (e.g., smoking, obesity, physical inactivity for cardiovascular disease) to compare their relative contributions to disease burden.

## Common Misconceptions
- Relative risk directly predicts population impact; high relative risk for rare exposures has minimal PAR.
- PAR assumes elimination of exposure is feasible; in practice, PAR estimates represent upper bounds on preventable disease.

## Explainer

You already know how to calculate **relative risk (RR)** from cohort data: it measures the strength of association between an exposure and a disease at the individual level. An exposed person is RR times more likely to develop disease than an unexposed person. **Population attributable risk (PAR)** asks a different — and for policy purposes more important — question: if we eliminated this exposure from the entire population, how much disease would disappear?

The formula reveals why high RR doesn't automatically translate to high PAR. PAR depends on two things: the strength of association (RR) and the **prevalence of exposure** in the population. The formula is: PAR% = p(RR − 1) / [p(RR − 1) + 1], where p is the prevalence of exposure in the general population. Consider two risk factors for lung cancer: smoking (RR ~15–25, prevalence ~15% in many countries) and a hypothetical rare genetic variant (RR = 50, prevalence 0.5%). The genetic variant has a dramatically higher relative risk, but its PAR is tiny because almost nobody carries it. Smoking's PAR is enormous because the risk is high and the exposure is widespread. The practical implication: targeting common, moderately-sized risks often prevents more disease than targeting rare, large risks.

The logic of PAR becomes clearest when comparing multiple risk factors for the same disease. Suppose you're analyzing preventable cardiovascular disease and compute PAR for smoking (35%), physical inactivity (25%), hypertension (20%), and obesity (20%). These percentages don't sum to 100% — they can overlap because risk factors co-occur and their joint effects are not simply additive. But ranking them by PAR tells public health planners where intervention resources will have the greatest expected return. A smoking intervention with a PAR of 35% theoretically prevents more cardiovascular deaths than a hypertension intervention with PAR of 20%, holding intervention effectiveness constant.

Two important limitations temper the use of PAR in practice. First, PAR rests on the causal assumption embedded in the RR estimate — if confounding inflates the apparent association, PAR is correspondingly overstated. Second, "eliminating the exposure" is a theoretical construct. People don't stop smoking simply because policy says so; dietary and physical activity patterns are shaped by environment, culture, and economics. PAR therefore represents an **upper bound** on what is preventable, not a prediction of what any specific intervention will achieve. Its value is comparative — ranking risk factors against each other — rather than absolute prediction of impact. This is why PAR is described as translating epidemiological evidence into the language of public health priority-setting.
