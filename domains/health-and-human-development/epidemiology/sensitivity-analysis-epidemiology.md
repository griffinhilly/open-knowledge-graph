---
id: sensitivity-analysis-epidemiology
title: Sensitivity Analysis for Unmeasured Confounding
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: counterfactual-framework
  type: hard
- id: confounding-epidemiology
  type: hard
tags:
- unmeasured-confounding
- bias-analysis
- robustness
stage: advanced
status: draft
---

# Sensitivity Analysis for Unmeasured Confounding

## Core Idea
Sensitivity analysis assesses whether conclusions remain robust under violations of unmeasured confounding. Methods (e.g., E-value, Rotnitzky-Robins bounds) quantify the minimum strength of unmeasured confounding needed to reverse or nullify an observed association. Sensitivity analysis supplements point estimates with assessments of hidden bias.

## Explainer

From the counterfactual framework, you know that valid causal inference from observational data requires **exchangeability**: conditional on measured covariates, the exposed and unexposed groups must be comparable in their potential outcomes. This is the assumption of no unmeasured confounding. In a randomized trial, it holds by design. In observational studies, it is always an untestable assumption — you cannot rule out that some unmeasured variable simultaneously predicts both who gets exposed and who gets the outcome. Sensitivity analysis does not test this assumption; it asks a sharper question: **how strongly would unmeasured confounding have to act to explain away your finding?**

The **E-value** (introduced by VanderWeele and Ding) is the most widely used tool for this purpose. It answers: what is the minimum strength, on the risk ratio scale, that an unmeasured confounder would need to have with *both* the exposure and the outcome — simultaneously — to fully explain away the observed association? If you observe a risk ratio of 3.0, the E-value tells you precisely how large the confounder-exposure and confounder-outcome associations would each need to be. The calculation is simple: E-value = RR + √(RR × (RR − 1)). For an RR of 3.0, E-value ≈ 5.2. This means any unmeasured confounder would need associations of at least 5.2-fold with both the exposure and the outcome to explain the result away. You then ask: is there any plausible confounder with that magnitude of association? If the strongest known predictors of the outcome all have associations below 5.2, the result is robust.

**Rotnitzky-Robins bounds** (and related **Cornfield conditions**) approach the same problem differently — they impose parameter constraints on what a confounding variable would have to look like (its prevalence, its association with exposure and outcome) and derive bounds on the true causal effect under those constraints. Rather than a single threshold, bounds analysis yields an interval: the true effect could be anywhere from [lower bound] to [upper bound] if unmeasured confounding exists at a specified level. This is more informative than a point estimate when uncertainty about confounding is substantial.

The practical workflow is to report the E-value alongside every point estimate in an observational study. A large E-value provides a degree of protection: you are saying "for this finding to be spurious, confounding would need to be implausibly extreme." A small E-value is a warning: the finding is fragile and could easily be explained by modest unmeasured confounding. Critics cannot simply assert "there might be confounding" — they must propose a specific confounder with the required magnitude, which is a much harder scientific argument to make. Sensitivity analysis thus converts a logical impossibility (proving the absence of unmeasured confounding) into a tractable empirical question (is there anything plausible with that effect size?), and in doing so it disciplines the rhetoric around causal claims from observational data.

## How It's Best Learned
Calculate E-values for published observational findings across a range of reported effect sizes, and evaluate whether plausible unmeasured confounders could meet the threshold. This trains the intuition for what "robust" actually means quantitatively.
