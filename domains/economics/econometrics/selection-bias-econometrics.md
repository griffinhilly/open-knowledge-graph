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

## Questions

```yaml
- question: "A researcher estimates returns to job training by comparing wages of program completers to non-participants. Participants were more motivated and job-ready before the program. What is the problem with this estimate?"
  type: multiple-choice
  options:
    - "It underestimates the treatment effect because participants are harder to train"
    - "It overestimates the treatment effect because participants had higher baseline wages even without training"
    - "It is unbiased as long as the researcher controls for age and education"
    - "It is valid because the comparison uses the same time period"
  answer: 1
  explanation: "The naive estimator confounds the training effect with pre-existing differences. More motivated workers would earn more even without training — E[Y(0)|D=1] > E[Y(0)|D=0] — so the control group underrepresents what participants would have earned absent treatment. The bias is positive: the naive estimate overstates the causal effect. Controlling for observable characteristics (option C) only helps if motivation is fully captured by those observables — in practice, motivation is typically unobserved."

- question: "A researcher matches treated and control units on age, education, and prior employment, achieving covariate balance. This guarantees the treatment effect estimate is free of selection bias."
  type: multiple-choice
  options:
    - "True — matching on all relevant covariates removes all forms of selection bias"
    - "False — matching only balances observed covariates; unobserved differences may remain"
    - "True — as long as the matched groups are large enough, unobserved differences cancel out"
    - "False — matching never reduces bias; only random assignment can"
  answer: 1
  explanation: "Matching balances the distribution of observed covariates between treated and control groups, addressing selection on observables. But it does nothing for selection on unobservables — unmeasured differences (motivation, ambition, health) may still differ systematically between groups. A well-matched study can still have severe selection bias if an important confounder is unmeasured. This is why causal inference often requires IV, DiD, or RD when selection on unobservables is plausible."

- question: "Selection bias occurs primarily when researchers use data collected non-randomly; using large datasets eliminates the problem."
  type: true-false
  answer: false
  explanation: "False. Selection bias is about the mechanism by which units enter treatment, not the size of the dataset. A massive observational dataset can have severe selection bias if those who choose treatment differ systematically from those who don't. The solution is not more data but an identification strategy that addresses how units self-selected into treatment — random assignment, an instrument, a discontinuity, or differencing."

- question: "Positive selection bias causes the naive treatment effect estimator to overstate the true causal effect."
  type: true-false
  answer: true
  explanation: "True. Formally, naive estimator = ATT + selection bias, where selection bias = E[Y(0)|D=1] − E[Y(0)|D=0]. Positive selection means the treated group would have had better outcomes even without treatment, so the selection bias term is positive and the naive estimate exceeds the true ATT. The job training example illustrates this: more motivated workers earn more even without training, inflating the apparent program effect."

- question: "Explain the difference between selection on observables and selection on unobservables, and why the distinction determines which identification strategy is appropriate."
  type: short-answer
  answer: "Selection on observables means that conditional on measured covariates X, treatment assignment is independent of potential outcomes — all confounders are captured in X. Controlling for X via regression or matching recovers an unbiased estimate. Selection on unobservables means treated and control groups differ in unmeasured ways that also affect outcomes. No amount of conditioning on observed variables fixes this — you need a quasi-experimental strategy: instrumental variables exploit external variation in treatment assignment; difference-in-differences removes fixed group-level confounders; regression discontinuity exploits threshold-based assignment."
  explanation: "The distinction determines what tools can credibly identify a causal effect. If all confounders are measured, the conditional independence assumption is plausible and standard methods work. If important confounders are unobserved, the treatment variable remains endogenous even after conditioning, and you need a strategy that creates plausibly exogenous variation in treatment. This is the core challenge of observational causal inference."
```

## Explainer

From the potential outcomes framework, you know that the causal effect of treatment for individual i is Yᵢ(1) − Yᵢ(0) — the difference between what would happen with and without treatment. The fundamental problem is that we observe only one of these potential outcomes. To estimate the average treatment effect (ATE) or the average treatment effect on the treated (ATT), we need a valid comparison group that stands in for the unobserved counterfactual. Selection bias is what goes wrong when that comparison group is systematically different in ways that also affect outcomes.

A canonical example: you want to estimate the wage return to a job training program. You compare wages of program completers to non-participants. If those who enrolled were already more motivated, more skilled, or more attached to the labor market — traits that raise wages independently of training — then the comparison group (non-participants) has lower baseline potential wages, even in the absence of training. The naive estimate E[Y|D=1] − E[Y|D=0] overstates the treatment effect because it conflates the effect of training with the pre-existing advantage of trainees. Formally: the naive estimator equals ATT + selection bias, where selection bias = E[Y(0)|D=1] − E[Y(0)|D=0]. If those who select into treatment would have earned more anyway (positive selection), the naive estimator is upward biased.

The endogeneity you studied earlier is the formal statement of the same problem: the treatment variable D is correlated with the error term, which here represents unobservable determinants of the outcome. **Selection on observables** means that conditional on measured covariates X, treatment assignment is independent of potential outcomes — the selection is fully explained by X. In this case, controlling for X (via regression, matching, or inverse probability weighting) recovers an unbiased estimate. The key assumption is that you've measured all the relevant confounders; if any important confounder is omitted, bias remains.

**Selection on unobservables** is the harder case: the treated and control groups differ in unmeasured ways. No amount of controlling for observed covariates fixes this. Matching balances the distribution of X between treated and control, but it cannot create balance on unobserved variables. This is why causal inference requires quasi-experimental strategies — instrumental variables exploit an external source of variation in treatment assignment that is uncorrelated with outcomes except through treatment; difference-in-differences removes fixed group-level confounders by comparing changes over time; regression discontinuity exploits threshold-based assignment to approximate random assignment near the cutoff. Each strategy targets a specific type of selection story and requires its own identifying assumption about what is and isn't correlated with potential outcomes.
