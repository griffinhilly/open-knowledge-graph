---
id: treatment-effect-heterogeneity
title: Treatment Effect Heterogeneity and Conditional Average Treatment Effects
domain: economics
course: econometrics
prerequisites:
- id: propensity-score-methods
  type: hard
- id: causal-inference-econometrics
  type: hard
tags:
- treatment-heterogeneity
- cate
- subgroup-analysis
stage: advanced
status: draft
---

# Treatment Effect Heterogeneity and Conditional Average Treatment Effects

## Core Idea
Treatment effects vary across individuals. Conditional average treatment effects (CATE) measure effects for specific subgroups or covariate values. Methods include subgroup analysis, interaction terms, machine learning trees, and causal forests.

## Explainer

From your study of causal inference, you know that the Average Treatment Effect (ATE) summarizes the causal impact of a treatment as a single number — as if the effect were uniform across all individuals. From propensity score methods, you know how to construct reweighted or matched estimators that balance covariates between treatment and control groups to recover this average. Both frameworks assume, for simplicity, that the average adequately captures what matters. **Treatment effect heterogeneity** relaxes this assumption and asks: does the treatment work differently for different kinds of people?

This question matters both practically and methodologically. Practically, if a medication has a large average effect but only works for patients with a specific genetic variant, knowing the average is not enough — you want to target the drug. A job training program might substantially boost earnings for displaced manufacturing workers but have little effect on recent graduates who had other options; understanding who benefits guides program design and resource allocation. Methodologically, your IV background already introduced you to one form of heterogeneity: the LATE is the effect for compliers, which may differ from the effect for always-takers or never-takers. When you use an instrument to estimate a treatment effect, you are recovering a specific weighted average over individuals, not a universal constant.

The **Conditional Average Treatment Effect** (CATE) formalizes heterogeneity: τ(x) = E[Y(1) − Y(0) | X = x] is the expected treatment effect for individuals with covariate vector x. The ATE is the average of τ(x) across the population. Estimating CATE requires not just recovering the average, but learning a *function* that describes how effects vary with covariates. Simple approaches include **subgroup analysis** (compute effects separately for pre-defined groups like men vs. women, or young vs. old) and **interaction terms** in regression (include a treatment × covariate interaction and test whether its coefficient is nonzero). These work well when you have strong prior beliefs about which subgroups matter and only a few of them.

When heterogeneity may arise along many dimensions simultaneously, machine learning methods become valuable. **Causal forests** — an extension of random forests designed for causal estimation — partition the covariate space into subgroups where the treatment effect is approximately homogeneous, then estimate effects within each subgroup. They automatically discover which covariates drive heterogeneity without requiring pre-specification. The central challenge in all CATE estimation is **overfitting**: with many covariates, it is easy to find spurious subgroup patterns in sample that do not replicate out of sample. Honest splitting (using separate subsamples to build the tree structure and estimate effects within it) and cross-validation help mitigate this, but the fundamental principle remains — any exploratory subgroup finding should be replicated in held-out data or a new study before being treated as established.
