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

## Explainer

From Mendelian genetics, you know that a monohybrid cross between two heterozygotes (Aa × Aa) should produce a 3:1 phenotypic ratio. But in practice, if you cross two heterozygous pea plants and count 850 round seeds and 150 wrinkled seeds, is that close enough to 3:1 (which predicts 750:250), or is something else going on? Your eyes might say "close enough" or "that's off," but genetics demands a formal, reproducible way to decide. The **chi-square test** provides exactly this — a statistical method to determine whether deviations from expected ratios are within the range of normal sampling variation or too large to be explained by chance alone.

The calculation is straightforward. For each phenotypic class, you compute (observed − expected)² / expected, then sum these values across all classes. In the example above, χ² = (850−750)²/750 + (150−250)²/250 = 13.33 + 40.00 = 53.33. The **degrees of freedom** equal the number of classes minus one — here, 2 classes minus 1 = 1 degree of freedom. You then compare your χ² value to a critical value from a chi-square distribution table. At the conventional p = 0.05 significance level with 1 degree of freedom, the critical value is 3.84. Since 53.33 far exceeds 3.84, you reject the null hypothesis that the data fit a 3:1 ratio. Something beyond simple Mendelian segregation is at work.

What makes this test so powerful in genetics is what a significant result *means* biologically. When observed ratios deviate significantly from Mendelian expectations, it becomes a clue pointing toward deeper genetic phenomena. A dihybrid cross yielding a 9:3:3:1 ratio confirms independent assortment, but a significant deviation from 9:3:3:1 might reveal **epistasis** (one gene masking another), **linkage** (genes on the same chromosome not assorting independently), or **differential viability** (some genotypes dying before being counted). The chi-square test does not tell you *which* alternative explanation is correct — it tells you that your simple model is insufficient and further investigation is needed.

A common pitfall is misinterpreting a non-significant result. Failing to reject the null hypothesis does not prove that your genetic model is correct — it means that your data are *consistent* with the model. With small sample sizes, even substantial deviations from expected ratios may not reach statistical significance because random sampling variation is large. This is why genetics experiments benefit from large sample sizes: they give the chi-square test enough statistical power to detect real deviations. Mendel's own data, famously, fit expected ratios almost *too* well — so well that some statisticians have questioned whether the data were selectively reported. The chi-square test thus cuts both ways: suspiciously good fits deserve scrutiny just as much as poor ones.
