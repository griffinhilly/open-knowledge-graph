---
id: chi-square-analysis-in-genetics
title: Chi-Square Analysis in Genetic Data
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: mendelian-genetics
  type: hard
- id: genetic-recombination-and-linkage-mapping
  type: soft
- id: chi-square-test
  type: hard
- id: statistical-methods-analytical
  type: soft
builds-toward:
- quantitative-genetics-and-polygenic-traits
tags:
- chi-square-test
- goodness-of-fit
- expected-ratio
- degrees-of-freedom
stage: formal-systems
status: draft
---

# Chi-Square Analysis in Genetic Data

## Core Idea
Chi-square (χ²) tests determine whether observed genetic ratios significantly differ from predicted Mendelian expectations. The test compares observed versus expected frequencies for each class, computing χ² = Σ((observed - expected)²/expected). The χ² statistic is compared against a critical value for the degrees of freedom (number of classes minus 1); a χ² value above the critical value indicates statistically significant deviation from the hypothesis. Chi-square analysis is essential for validating genetic models, detecting non-Mendelian patterns, identifying hidden genetic interactions, and confirming linkage hypotheses. Large deviations may reveal unequal viability of genotypic classes, incomplete penetrance, or linked genes.
