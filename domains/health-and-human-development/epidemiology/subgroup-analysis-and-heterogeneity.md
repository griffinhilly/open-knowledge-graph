---
id: subgroup-analysis-and-heterogeneity
title: Subgroup Analysis and Treatment Heterogeneity
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: multivariable-regression-epi
  type: hard
- id: meta-analysis-methods
  type: hard
- id: effect-modification-interaction
  type: soft
tags:
- heterogeneity
- treatment-interaction
- precision-medicine
stage: advanced
status: draft
---

# Subgroup Analysis and Treatment Heterogeneity

## Core Idea
Subgroup analysis investigates whether treatment effects vary across population subsets (age, sex, disease severity, genetic markers). Genuine treatment heterogeneity reflects differential causal effects; apparent heterogeneity may result from chance, multiple comparisons, or bias. Meta-regression and individual patient data (IPD) meta-analysis test heterogeneity more rigorously than separate subgroup analyses. Prespecification prevents false discoveries; testing too many subgroups inflates Type I error even with Bonferroni adjustment.

## How It's Best Learned
Perform IPD meta-analysis testing treatment × subgroup interactions using appropriate statistical tests; assess statistical heterogeneity with I².

## Common Misconceptions
Lack of statistical significance means homogeneity of effects (insufficient power). Stratified subgroup analyses are valid without prespecification.
