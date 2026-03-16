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
stage: advanced
status: draft
---

# Hierarchical and Multilevel Models

## Core Idea
Hierarchical (multilevel/mixed-effects) models handle data with nested structure—individuals within schools, patients within hospitals, repeated measurements within persons—by accounting for within-cluster correlation through random intercepts or slopes at each level. They improve statistical inference and allow investigation of cluster-level effects while borrowing strength across clusters. Partial pooling of cluster-specific estimates provides better small-sample estimates than either complete pooling or no pooling.

## How It's Best Learned
Fit models with and without random effects to clustered data; compare to standard approaches and examine intraclass correlation coefficients.

## Common Misconceptions
Random effects allow one to ignore clustering (ignoring ICC leads to invalid inference). Must check ICC to assess the practical importance of clustering for standard errors.

## Explainer

Standard regression assumes that observations are independent. In practice, epidemiological data is often clustered: patients nest within hospitals, students within schools, repeated measurements within individuals, neighborhoods within cities. Individuals in the same cluster tend to be more similar to each other than to individuals in other clusters — they share environments, exposures, providers, or genetics. Ignoring this correlation violates the independence assumption and leads to artificially small standard errors, inflated test statistics, and confidence intervals that are too narrow. Hierarchical models solve this problem by explicitly modeling the structure.

The central quantity for diagnosing how serious clustering is is the **intraclass correlation coefficient (ICC)**: the proportion of total variance in the outcome attributable to between-cluster differences. If ICC = 0, there is no clustering and ordinary regression is fine. If ICC = 0.20, 20% of the variation in the outcome is explained by which cluster an individual belongs to — large enough that ignoring it will meaningfully bias your inference. A practical rule of thumb: ICC > 0.05 warrants a multilevel approach.

Hierarchical models extend your multivariable regression by adding **random effects** for cluster-level deviations. In the simplest two-level model, each cluster gets its own intercept, but these intercepts are treated as draws from a normal distribution rather than estimated independently. This is **partial pooling**: cluster-specific estimates are pulled toward the overall mean, with the degree of shrinkage proportional to how little data is in the cluster and how much variation there is between clusters. The result is better estimates — particularly for small clusters — than either ignoring clustering (complete pooling) or estimating each cluster separately (no pooling). You can also add **random slopes**, allowing the effect of a covariate to vary across clusters, which tests whether an exposure operates differently in different hospital systems, neighborhoods, or time periods.

Beyond correcting standard errors, hierarchical models enable genuine **cross-level inference**: you can simultaneously ask "what individual-level factors predict the outcome?" and "what cluster-level factors explain why some clusters have better average outcomes?" A hospital quality study might find that patient severity predicts mortality at the individual level, while nurse-to-patient staffing ratio predicts mortality at the hospital level — and that the staffing effect remains after adjusting for the patient-level case mix. This kind of analysis, which nests causal questions at multiple levels of aggregation, is impossible with standard regression and is increasingly important as epidemiology expands to studying the environments and systems that shape health.
