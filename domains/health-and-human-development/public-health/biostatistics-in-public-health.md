---
id: biostatistics-in-public-health
title: Biostatistics in Public Health
domain: health-and-human-development
course: public-health
prerequisites:
- id: disease-frequency-measures
  type: hard
- id: measures-of-association
  type: hard
- id: statistical-methods-analytical
  type: soft
builds-toward:
- screening-and-early-detection
tags:
- biostatistics
- confidence-intervals
- hypothesis-testing
- regression
- p-values
stage: abstract-reasoning
status: validated
---
# Biostatistics in Public Health

## Core Idea
Biostatistics provides the quantitative methods for designing studies, analyzing data, and drawing valid inferences in public health. Key concepts include hypothesis testing (null vs. alternative hypothesis, Type I and Type II errors), confidence intervals (the range of plausible values for a population parameter), and p-values (the probability of observed data given the null hypothesis). Logistic regression models binary outcomes adjusting for multiple confounders; survival analysis handles time-to-event data with censoring, common in cohort studies. Power and sample size calculations are conducted before studies begin to ensure adequate precision to detect meaningful effect sizes.

## How It's Best Learned
Work through the analysis of a cohort study dataset: compute crude and adjusted relative risks, calculate 95% confidence intervals, interpret p-values in context, and distinguish statistical significance from clinical or public health significance.

## Common Misconceptions
- A p-value is not the probability that the null hypothesis is true; it is the probability of data as extreme as observed, assuming the null is true.
- Statistical significance is not the same as practical importance; large studies can detect trivially small effects.
- Confounding adjustment via regression requires correct model specification; including a collider instead of a confounder introduces bias rather than removing it.
