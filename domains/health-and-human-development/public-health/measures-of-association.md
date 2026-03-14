---
id: measures-of-association
title: Measures of Association and Impact
domain: health-and-human-development
course: public-health
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: disease-frequency-measures
  type: hard
builds-toward:
- biostatistics-in-public-health
- chronic-disease-epidemiology
- disease-prevention-levels
tags:
- relative-risk
- odds-ratio
- attributable-risk
- causation
- epidemiology
stage: abstract-reasoning
status: validated
---

# Measures of Association and Impact

## Core Idea
The relative risk (risk ratio) compares incidence between exposed and unexposed groups, conveying how much more likely exposure makes an outcome. The odds ratio approximates the risk ratio for rare diseases and is the native output of logistic regression. Attributable risk (risk difference) quantifies the absolute excess burden due to exposure, which matters more for policy prioritization than relative measures alone. Population attributable fraction estimates how much disease would be eliminated if an exposure were removed from the population entirely, combining the size of the exposed group with the strength of association.

## How It's Best Learned
Practice computing RR, OR, AR, and PAF from 2×2 contingency tables. Then interpret a set of real epidemiologic findings where RR and AR tell conflicting 'importance' stories—this crystallizes why both perspectives are necessary.

## Common Misconceptions
- A large relative risk does not mean the exposure causes many cases if baseline risk is very low; absolute risk difference matters for public health impact.
- An OR > 1 does not mean the exposure is causal; it means disease is more common among the exposed, which could reflect bias or confounding.
- PAF depends on both how common the exposure is and how strong the association is; a weak association in a highly prevalent exposure can have high PAF.
