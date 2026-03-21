---
id: potential-outcomes-framework
title: Potential Outcomes and the Rubin Causal Model
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: expected-value
  type: hard
- id: probability-axioms
  type: soft
- id: conditional-probability
  type: soft
builds-toward:
- selection-bias-econometrics
- difference-in-differences
- regression-discontinuity
tags:
- potential-outcomes
- ATE
- ATT
- counterfactual
stage: formal-systems
status: validated
---

# Potential Outcomes and the Rubin Causal Model

## Core Idea
The potential outcomes framework (Rubin, 1974) formalizes causality: unit i has two potential outcomes, Y(1) under treatment and Y(0) under control, but only one is observed. The individual treatment effect is Y_i(1) − Y_i(0), which is never directly observable. The Average Treatment Effect (ATE) = E[Y(1) − Y(0)] averages over the population; the ATT = E[Y(1) − Y(0) | D=1] averages only over the treated. Selection bias arises when E[Y(0)|D=1] ≠ E[Y(0)|D=0] — that is, when treated and untreated units would have had different outcomes even absent treatment. Randomization solves this by ensuring independence: {Y(0), Y(1)} ⊥ D.

## How It's Best Learned
Decompose the observed difference in means between treated and control groups into the ATT plus a selection bias term — this derivation makes the identification problem concrete and shows exactly what assumptions eliminate the bias.

## Common Misconceptions
- The ATE and ATT are different objects and answer different policy questions; IV typically estimates a Local ATE (LATE), not the ATE.
- The fundamental problem of causal inference is a missing data problem, not a statistical estimation problem.

## Questions

```yaml
- question: "Workers who completed a job training program earn $5,000 more per year than workers who did not. A researcher concludes the program raises wages by $5,000. The potential outcomes framework reveals this inference is flawed because:"
  type: multiple-choice
  options:
    - "The sample size is probably too small to support a $5,000 estimate with statistical significance"
    - "Workers who self-selected into training likely would have earned more anyway — the observed gap reflects both the program's effect and pre-existing differences between groups"
    - "The ATE and ATT are equal in labor market studies, so the $5,000 applies only to the treated"
    - "The estimate should be computed in log wages to avoid bias in the levels comparison"
  answer: 1
  explanation: "This is the selection bias problem. Workers who choose to enroll in job training are systematically different from those who don't — they may be more motivated, more educated, or more connected to labor markets. The potential outcomes decomposition reveals: observed gap = ATT + selection bias, where selection bias = E[Y(0)|D=1] − E[Y(0)|D=0]. If trainees would have earned more even without the program (positive selection bias), naive comparison overstates the effect. The $5,000 gap conflates the program's true impact with pre-existing differences — the fundamental problem that causal inference methods are designed to solve."

- question: "In a well-executed randomized controlled trial, the observed difference in outcomes between treated and control groups estimates the ATE. Why does randomization make this possible?"
  type: multiple-choice
  options:
    - "Randomization makes the treated and control groups the same size, eliminating statistical bias"
    - "Randomization ensures that potential outcomes are independent of treatment assignment, so the control group's average untreated outcome equals what the treated group's untreated outcome would have been"
    - "Randomization eliminates measurement error in the outcome variable"
    - "Randomization forces the ATE and ATT to be equal by design"
  answer: 1
  explanation: "Randomization achieves {Y(0), Y(1)} ⊥ D — potential outcomes are independent of which group you were assigned to. This means E[Y(0)|D=1] = E[Y(0)|D=0]: the average untreated potential outcome is the same for both groups. Selection bias is therefore zero by construction, and the observed difference in means recovers the ATE. Without randomization, treated units differ systematically from untreated units in their potential outcomes (that's selection bias), making naive comparison misleading. Randomization destroys this systematic relationship by assigning treatment independently of any individual characteristic."

- question: "The fundamental problem of causal inference is primarily a statistical problem — with a large enough sample, we can observe both Y_i(1) and Y_i(0) for the same individual and compute the individual treatment effect directly."
  type: true-false
  answer: false
  explanation: "The fundamental problem is logical, not statistical — no sample size resolves it. Y_i(1) and Y_i(0) are mutually exclusive: a person either receives treatment or they don't at a given point in time. You observe one potential outcome; the other is counterfactual, existing only in a hypothetical world where the treatment assignment was different. This is a missing data problem at the unit level. Statistics helps estimate population averages (ATE, ATT), but individual treatment effects remain permanently unobservable. Increasing sample size gives better estimates of averages — it does not allow you to observe the counterfactual outcome for any individual."

- question: "The Average Treatment Effect (ATE) and the Average Treatment Effect on the Treated (ATT) answer different policy questions and can differ substantially in observational studies."
  type: true-false
  answer: true
  explanation: "ATE = E[Y(1) − Y(0)] averages over the entire population; ATT = E[Y(1) − Y(0) | D=1] averages only over those who actually received treatment. If a job training program is effective specifically for the kind of motivated workers who self-select into it, but would be less effective for the broader population, then ATT > ATE. Policy questions determine which estimand is relevant: if you want to know the effect of mandating the program for everyone, you care about ATE; if you want to know whether it's worth continuing for current participants, you care about ATT. IV methods often estimate LATE (Local ATE) — a third estimand covering only the 'complier' subpopulation — which is different still."

- question: "What is selection bias in the potential outcomes framework, and why does it cause naive comparisons of treated and untreated groups to give misleading estimates of treatment effects?"
  type: short-answer
  answer: "Selection bias is the difference in untreated potential outcomes between those who received treatment and those who did not: E[Y(0)|D=1] − E[Y(0)|D=0]. It measures whether the groups would have differed in outcomes even without the treatment. When treatment is self-selected (not random), people who opt in typically differ systematically from those who don't — in motivation, health, socioeconomic status, or other factors. Naive comparison of treated vs. untreated outcomes conflates the treatment effect with these pre-existing differences, producing biased estimates. Positive selection bias (treated units have higher untreated potential outcomes) causes the observed gap to overstate the true effect."
  explanation: "The potential outcomes decomposition makes this concrete: E[Y|D=1] − E[Y|D=0] = ATT + (E[Y(0)|D=1] − E[Y(0)|D=0]). The second term is selection bias — present whenever treatment assignment is correlated with potential outcomes. Randomization eliminates it by making treatment assignment independent of potential outcomes. Quasi-experimental methods (DiD, RD, IV) achieve the same thing by exploiting variation in treatment that is 'as good as random' for a particular subpopulation. Understanding selection bias is what motivates the entire causal inference toolkit — every method is a different strategy for eliminating this one term from the decomposition."
```

## Explainer

You already know from your work on causal inference that observational data does not automatically yield causal answers — the question is *why*. The potential outcomes framework gives the sharpest possible answer: for every unit i, there are two potential states of the world. **Y_i(1)** is the outcome that would occur if unit i receives treatment; **Y_i(0)** is the outcome if it does not. The individual treatment effect is the difference Y_i(1) − Y_i(0). The problem is not statistical — it is logical. You observe a person either treated or untreated, never both. Y_i(1) and Y_i(0) cannot both be realized simultaneously. This is the **fundamental problem of causal inference**: the individual treatment effect is never observed, and the challenge of causal inference is recovering population-level summaries of it.

Because individual effects are unobservable, the framework shifts focus to averages. The **Average Treatment Effect (ATE)** = E[Y(1) − Y(0)] asks: if we randomly assigned treatment to everyone in the population, what would the average effect be? The **Average Treatment Effect on the Treated (ATT)** = E[Y(1) − Y(0) | D=1] asks a more targeted question: among those who actually received treatment, what was the effect? These are distinct estimands that answer different policy questions. If a job training program works well for the people who self-select into it but would be less effective for the general population, ATE < ATT. Both numbers are real and meaningful — they just answer different questions about who benefits.

Why does naive comparison fail? The observed difference in means between treated and untreated groups can be decomposed as: E[Y|D=1] − E[Y|D=0] = ATT + **selection bias**. The selection bias term is E[Y(0)|D=1] − E[Y(0)|D=0]: the difference in untreated potential outcomes between those who chose treatment and those who didn't. If people who receive job training would have found employment at higher rates anyway (because they are more motivated), the selection bias is positive, and naive comparison overstates the treatment effect. This is not a subtle statistical issue — it is a direct consequence of the assignment mechanism not being random.

**Randomization** solves the problem cleanly. When treatment D is randomly assigned, {Y(0), Y(1)} ⊥ D — potential outcomes are independent of treatment status. This means E[Y(0)|D=1] = E[Y(0)|D=0]: the average untreated outcome of those assigned to treatment equals the average untreated outcome of those assigned to control. Selection bias is zero by construction, and the observed difference in means recovers the ATE. All subsequent methods in this course — difference-in-differences, regression discontinuity, instrumental variables — are ways of achieving the same independence condition when randomization is not available, by exploiting quasi-random variation in treatment assignment. The potential outcomes framework is the common language that makes each method's identifying assumption precise.
