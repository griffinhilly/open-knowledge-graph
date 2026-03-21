---
id: regression-discontinuity
title: Regression Discontinuity Design
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
- id: bivariate-regression
  type: hard
tags:
- RDD
- regression-discontinuity
- threshold
- local-ATE
- bandwidth
stage: formal-systems
status: validated
---

# Regression Discontinuity Design

## Core Idea
Regression discontinuity (RD) exploits a sharp threshold in a 'running variable' x that determines treatment assignment: units just above the cutoff receive treatment while units just below do not. The key insight is that units near the threshold are nearly identical in all respects — observed and unobserved — making the discontinuous jump in outcomes at the threshold a credible causal effect estimate. The RD estimator is the difference in the intercepts of the regression lines fitted on each side of the cutoff. Identification requires that agents cannot precisely manipulate their position around the threshold; the McCrary density test checks for sorting.

## How It's Best Learned
Study Thistlethwaite and Campbell's (1960) original scholarship threshold study, then examine Lee (2008)'s incumbency advantage study to understand how running variables and cutoffs are chosen and validated.

## Common Misconceptions
- RD estimates a Local ATE at the threshold, not the ATE for the full population — external validity is often limited.
- Choosing a very narrow bandwidth around the cutoff reduces bias but also reduces precision; bandwidth selection involves a bias-variance tradeoff.

## Questions

```yaml
- question: "A researcher uses RD to estimate the effect of a college scholarship (awarded to students scoring above 75) on future earnings, finding a $5,000 higher annual earnings at the cutoff. What does this estimate tell us?"
  type: multiple-choice
  options:
    - "The average effect of the scholarship for all college-age students in the population"
    - "The effect for students near the threshold — those who scored just around 75"
    - "The effect for high-achieving students who scored well above 75"
    - "The effect for students who would have attended college regardless of the scholarship"
  answer: 1
  explanation: "RD estimates a Local Average Treatment Effect (LATE) at the threshold, not the ATE for the full population. Units far from the cutoff — very high scorers or very low scorers — may respond very differently to the scholarship than marginal students. This limited external validity is RD's principal weakness: the estimate is credibly causal but may not generalize beyond the narrow window around the cutoff."

- question: "What does the McCrary density test check for in a regression discontinuity design?"
  type: multiple-choice
  options:
    - "Whether the running variable is a strong predictor of the outcome"
    - "Whether there is a suspicious discontinuous jump in the density of the running variable at the cutoff"
    - "Whether the chosen bandwidth minimizes mean squared error"
    - "Whether outcomes trend smoothly on each side of the cutoff"
  answer: 1
  explanation: "The key RD assumption is that units cannot *precisely* manipulate their position around the cutoff. If they can, the treated group just above the threshold will be systematically different (e.g., more motivated students who studied harder to score exactly above 75), breaking the local randomization logic. The McCrary test checks for a suspicious pile-up of observations just above the cutoff in the running variable's density — a red flag for sorting."

- question: "In a regression discontinuity design, units just below the cutoff serve as a credible comparison group for units just above because they are essentially identical in both observed and unobserved characteristics."
  type: true-false
  answer: true
  explanation: "This is the local randomization intuition behind RD. A student who scored 74 vs. one who scored 76 are separated by two points of test noise — effectively random variation. They likely have similar ability, background, and all other characteristics. This near-identical comparability makes the jump in outcomes at the cutoff a credible causal estimate, rather than reflecting underlying differences between the groups."

- question: "Using a wider bandwidth in RD always produces more accurate causal estimates because more observations reduce sampling error."
  type: true-false
  answer: false
  explanation: "Bandwidth selection involves a bias-variance tradeoff. A narrow bandwidth gives highly comparable units (low bias) but few observations (high variance and imprecise estimates). A wide bandwidth increases precision but includes units farther from the cutoff who may be systematically different, introducing bias if the underlying outcome function is nonlinear. Neither extreme is always best; credible RD papers typically report results across multiple bandwidth choices."

- question: "Why does precise manipulation of the running variable threaten the validity of an RD design? What does the McCrary density test look for?"
  type: short-answer
  answer: "If agents can precisely control their score to land just above the cutoff, the treatment group will be systematically different — more motivated, higher-ability — from the control group just below, destroying the 'local randomization' logic. The McCrary test examines the density of the running variable around the cutoff. In a valid RD, the density should be smooth (continuous) at the threshold. A spike or discontinuous jump just above the cutoff suggests strategic sorting, which undermines the causal interpretation of the discontinuity."
  explanation: "Some manipulation is fine — students may study harder knowing the cutoff exists — but *precise* sorting is fatal to the design. The intuition: if the treated group just above the threshold is self-selected by determination or resources, the outcome jump reflects those traits rather than the treatment itself."
```

## Explainer

Your prerequisite on causal inference introduced the core identification problem: you can never observe the same unit in both treated and untreated states simultaneously. The potential outcomes framework formalized this — the causal effect for unit i is Yᵢ(1) − Yᵢ(0), but only one of these is ever observed. Regression discontinuity offers an elegant solution to this problem by finding a setting where nature approximates a randomized experiment: a sharp threshold rule that determines who gets treated.

The canonical example is a scholarship test: students scoring above 50 receive a scholarship, those scoring below do not. A student who scores 51 is treated; one who scores 49 is not. These two students are almost certainly very similar in ability, background, and other characteristics — the single point separating them is essentially random noise in test performance. This is the **local randomization** intuition behind RD. The **running variable** (the test score) determines treatment, and the **cutoff** (score = 50) creates two groups that are locally comparable. The RD estimator computes the **jump** in the outcome at the cutoff: the vertical gap between the regression line fitted on the right side (treated units) and the regression line fitted on the left side (control units), both evaluated at exactly x = 50.

Formally, the RD estimate is the **Local Average Treatment Effect at the threshold**: LATE = lim_{x↓c} E[Y|X=x] − lim_{x↑c} E[Y|X=x]. Notice this is inherently a local quantity — it estimates the effect for units at the cutoff, not the whole population. A student with a score of 70 might respond very differently to the scholarship than a student at 50. This limited external validity is RD's principal weakness relative to other methods.

The key identifying assumption is that agents cannot **precisely** manipulate their position around the threshold. Some manipulation is fine — students may study harder knowing the cutoff exists — but if students can precisely sort to just above 50, the "local randomization" analogy breaks down: the treated group just above the cutoff would systematically differ from the control group just below. The **McCrary density test** checks for this by looking for a discontinuous jump in the density of the running variable at the cutoff. A suspicious pile-up of observations just above the threshold is a red flag. Bandwidth selection also matters: too narrow and you have very few observations and imprecise estimates; too wide and you are comparing units that are less similar, introducing bias if the underlying outcome function is nonlinear. Reporting results across multiple bandwidth choices is standard practice in credible RD papers.
