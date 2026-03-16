---
id: selection-bias-econometrics
title: Selection Bias
domain: economics
course: econometrics
prerequisites:
- id: potential-outcomes-framework
  type: hard
- id: endogeneity
  type: hard
- id: conditional-probability
  type: soft
- id: probability-axioms
  type: soft
builds-toward:
- difference-in-differences
- instrumental-variables
tags:
- selection-bias
- self-selection
- observational-data
- non-random-treatment
stage: formal-systems
status: validated
---

# Selection Bias

## Core Idea
Selection bias occurs when the units who receive treatment systematically differ from controls in ways that also affect the outcome, making the treated group a non-representative counterfactual for the untreated. A classic example: estimating returns to job training by comparing trainees to non-trainees, when those who chose to train were already more motivated. Selection on observables (confounding) can be addressed by controlling for all relevant characteristics; selection on unobservables requires an instrument, a discontinuity, or a differencing strategy. Heckman's selection model handles selection into a sample from a latent participation equation.

## Common Misconceptions
- Matching on observables does not solve selection on unobservables — it only balances measured covariates.
- Selection bias and attrition bias are related but distinct: attrition bias arises from non-random dropout from a study.

## Explainer

From the potential outcomes framework, you know that the causal effect of treatment for individual i is Yᵢ(1) − Yᵢ(0) — the difference between what would happen with and without treatment. The fundamental problem is that we observe only one of these potential outcomes. To estimate the average treatment effect (ATE) or the average treatment effect on the treated (ATT), we need a valid comparison group that stands in for the unobserved counterfactual. Selection bias is what goes wrong when that comparison group is systematically different in ways that also affect outcomes.

A canonical example: you want to estimate the wage return to a job training program. You compare wages of program completers to non-participants. If those who enrolled were already more motivated, more skilled, or more attached to the labor market — traits that raise wages independently of training — then the comparison group (non-participants) has lower baseline potential wages, even in the absence of training. The naive estimate E[Y|D=1] − E[Y|D=0] overstates the treatment effect because it conflates the effect of training with the pre-existing advantage of trainees. Formally: the naive estimator equals ATT + selection bias, where selection bias = E[Y(0)|D=1] − E[Y(0)|D=0]. If those who select into treatment would have earned more anyway (positive selection), the naive estimator is upward biased.

The endogeneity you studied earlier is the formal statement of the same problem: the treatment variable D is correlated with the error term, which here represents unobservable determinants of the outcome. **Selection on observables** means that conditional on measured covariates X, treatment assignment is independent of potential outcomes — the selection is fully explained by X. In this case, controlling for X (via regression, matching, or inverse probability weighting) recovers an unbiased estimate. The key assumption is that you've measured all the relevant confounders; if any important confounder is omitted, bias remains.

**Selection on unobservables** is the harder case: the treated and control groups differ in unmeasured ways. No amount of controlling for observed covariates fixes this. Matching balances the distribution of X between treated and control, but it cannot create balance on unobserved variables. This is why causal inference requires quasi-experimental strategies — instrumental variables exploit an external source of variation in treatment assignment that is uncorrelated with outcomes except through treatment; difference-in-differences removes fixed group-level confounders by comparing changes over time; regression discontinuity exploits threshold-based assignment to approximate random assignment near the cutoff. Each strategy targets a specific type of selection story and requires its own identifying assumption about what is and isn't correlated with potential outcomes.
