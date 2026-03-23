---
id: hierarchical-models-epidemiology
title: Hierarchical and Multilevel Models
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: multivariable-regression-epi
  type: hard
- id: biostatistics-in-public-health
  type: soft
builds-toward:
- spatial-epidemiology
tags:
- multilevel-modeling
- mixed-effects
- clustering
stage: expert
status: validated
---

# Hierarchical and Multilevel Models

## Core Idea
Hierarchical (multilevel/mixed-effects) models handle data with nested structure—individuals within schools, patients within hospitals, repeated measurements within persons—by accounting for within-cluster correlation through random intercepts or slopes at each level. They improve statistical inference and allow investigation of cluster-level effects while borrowing strength across clusters. Partial pooling of cluster-specific estimates provides better small-sample estimates than either complete pooling or no pooling.

## How It's Best Learned
Fit models with and without random effects to clustered data; compare to standard approaches and examine intraclass correlation coefficients.

## Common Misconceptions
Random effects allow one to ignore clustering (ignoring ICC leads to invalid inference). Must check ICC to assess the practical importance of clustering for standard errors.

## Questions

```yaml
- question: "A researcher studies student test scores from 50 schools and estimates the effect of a tutoring program using standard OLS regression that ignores school membership. What is the most likely statistical consequence?"
  type: multiple-choice
  options:
    - "Coefficient estimates will be biased toward zero because the tutoring effect is diluted across schools"
    - "Standard errors will be artificially small, leading to inflated test statistics and confidence intervals that are too narrow"
    - "The model will fail to converge because clustering violates the computational assumptions of OLS"
    - "Coefficient estimates will be too large because schools with more students receive excess influence"
  answer: 1
  explanation: "Ignoring clustering violates the independence assumption of OLS. Students within the same school share environments, teachers, and resources — they are more correlated with each other than with students in other schools. This within-cluster correlation means the 'effective sample size' is smaller than the nominal N. OLS treats all N observations as independent, underestimates true standard errors, and overstates precision. The result is inflated test statistics and too-narrow confidence intervals — an elevated false positive rate. Coefficient point estimates may not be biased, but inference about them will be unreliable."

- question: "A researcher computes the intraclass correlation coefficient (ICC) for patient mortality across 30 hospitals and finds ICC = 0.25. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The pairwise correlation between any two patients' mortality outcomes within the same hospital is 0.25"
    - "25% of the total variation in mortality outcomes is attributable to which hospital a patient is in — clustering is substantial and ignoring it will bias inference"
    - "The multilevel model explains 25% of the mortality variance; the remaining 75% is unexplained"
    - "25% of hospitals in the study have statistically significantly above-average mortality rates"
  answer: 1
  explanation: "The ICC is the proportion of total outcome variance attributable to between-cluster differences. ICC = 0.25 means that 25% of the variation in mortality is explained simply by knowing which hospital a patient is in — a very large clustering effect. As a rule of thumb, ICC > 0.05 warrants a multilevel model; ICC = 0.25 makes it mandatory. Option A is close but slightly wrong: ICC measures the expected correlation between two randomly chosen individuals from the same cluster, not a simple pairwise correlation — though numerically they are equivalent in the simple two-level model."

- question: "Partial pooling in a hierarchical model produces better small-cluster estimates than estimating each cluster completely independently (no pooling)."
  type: true-false
  answer: true
  explanation: "True — when a cluster has few observations, its independent (no-pooling) estimate is highly unstable and driven by noise. Partial pooling shrinks the cluster's estimate toward the overall mean, with the degree of shrinkage proportional to how few observations are in the cluster and how much clusters vary. For small clusters, this trades a small bias for a large reduction in variance, yielding a lower mean squared error. This is formalized in the James-Stein result: under squared error loss, shrinkage estimators dominate independent estimation when there are many groups."

- question: "If the intraclass correlation coefficient for a dataset is 0.02, using a multilevel model instead of ordinary regression will substantially change the study's conclusions."
  type: true-false
  answer: false
  explanation: "False — when ICC is near zero, almost no variation in the outcome is attributable to cluster membership. The observations within clusters are barely more correlated than observations from different clusters. In this case, OLS standard errors will be approximately correct and the inferential gap between OLS and multilevel modeling will be negligible. The practical rule of thumb is ICC > 0.05 warrants the multilevel approach. ICC = 0.02 indicates clustering is unlikely to meaningfully bias inference, making the added model complexity unnecessary."

- question: "In your own words, explain what 'partial pooling' means in a hierarchical model and why it produces better estimates than either complete pooling or no pooling for clustered data."
  type: short-answer
  answer: "Partial pooling means cluster-specific estimates are pulled toward the overall mean rather than being estimated either all-identically (complete pooling) or fully independently (no pooling). The degree of shrinkage depends on cluster size and between-cluster variance: large, information-rich clusters are barely shrunk; small clusters are pulled substantially toward the global mean. Complete pooling ignores genuine between-cluster differences. No pooling gives unstable, noisy estimates for small clusters. Partial pooling navigates between these extremes, yielding better estimates by borrowing strength from the full dataset without erasing real cluster differences."
  explanation: "The intuition: if a hospital has only 5 patients in your study, its raw observed mortality rate is mostly noise. Instead of reporting that noisy rate as-is (no pooling) or ignoring the hospital's identity entirely (complete pooling), partial pooling says 'your estimate is mostly the overall mean, adjusted a little toward your 5-patient observation.' As the cluster size grows, the observation dominates and the estimate converges to the no-pooling value. This is formally optimal under squared error loss for a broad class of models."
```

## Explainer

Standard regression assumes that observations are independent. In practice, epidemiological data is often clustered: patients nest within hospitals, students within schools, repeated measurements within individuals, neighborhoods within cities. Individuals in the same cluster tend to be more similar to each other than to individuals in other clusters — they share environments, exposures, providers, or genetics. Ignoring this correlation violates the independence assumption and leads to artificially small standard errors, inflated test statistics, and confidence intervals that are too narrow. Hierarchical models solve this problem by explicitly modeling the structure.

The central quantity for diagnosing how serious clustering is is the **intraclass correlation coefficient (ICC)**: the proportion of total variance in the outcome attributable to between-cluster differences. If ICC = 0, there is no clustering and ordinary regression is fine. If ICC = 0.20, 20% of the variation in the outcome is explained by which cluster an individual belongs to — large enough that ignoring it will meaningfully bias your inference. A practical rule of thumb: ICC > 0.05 warrants a multilevel approach.

Hierarchical models extend your multivariable regression by adding **random effects** for cluster-level deviations. In the simplest two-level model, each cluster gets its own intercept, but these intercepts are treated as draws from a normal distribution rather than estimated independently. This is **partial pooling**: cluster-specific estimates are pulled toward the overall mean, with the degree of shrinkage proportional to how little data is in the cluster and how much variation there is between clusters. The result is better estimates — particularly for small clusters — than either ignoring clustering (complete pooling) or estimating each cluster separately (no pooling). You can also add **random slopes**, allowing the effect of a covariate to vary across clusters, which tests whether an exposure operates differently in different hospital systems, neighborhoods, or time periods.

Beyond correcting standard errors, hierarchical models enable genuine **cross-level inference**: you can simultaneously ask "what individual-level factors predict the outcome?" and "what cluster-level factors explain why some clusters have better average outcomes?" A hospital quality study might find that patient severity predicts mortality at the individual level, while nurse-to-patient staffing ratio predicts mortality at the hospital level — and that the staffing effect remains after adjusting for the patient-level case mix. This kind of analysis, which nests causal questions at multiple levels of aggregation, is impossible with standard regression and is increasingly important as epidemiology expands to studying the environments and systems that shape health.
