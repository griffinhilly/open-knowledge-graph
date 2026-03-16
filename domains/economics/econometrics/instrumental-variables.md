---
id: instrumental-variables
title: Instrumental Variables
domain: economics
course: econometrics
prerequisites:
- id: endogeneity
  type: hard
- id: causal-inference-econometrics
  type: soft
- id: selection-bias-econometrics
  type: soft
- id: linear-algebra
  type: hard
- id: probability-theory
  type: hard
- id: matrix-operations
  type: soft
- id: linear-regression
  type: soft
- id: linear-transformation-matrix-representation
  type: soft
builds-toward:
- two-stage-least-squares
tags:
- IV
- instrument
- exclusion-restriction
- relevance
stage: formal-systems
status: validated
---
# Instrumental Variables

## Core Idea
An instrumental variable (IV) is a variable z that is correlated with the endogenous regressor x (relevance: Cov(z,x)≠0) but affects y only through x and not directly (exclusion restriction: Cov(z,u)=0). When both conditions hold, IV consistently estimates the causal effect of x on y even when OLS is biased. The IV estimator in the bivariate case is β̂ᵢᵥ = Cov(z,y)/Cov(z,x). Classic instruments include distance to college (for education), quarter of birth (for schooling), and rainfall (for agricultural income). The exclusion restriction is the unverifiable — and hence controversial — assumption; its plausibility must be argued on economic grounds.

## How It's Best Learned
Study the Angrist-Krueger (1991) quarter-of-birth instrument for education. Discuss why it is (arguably) excluded from the wage equation and what economic story justifies it.

## Common Misconceptions
- The exclusion restriction cannot be tested directly — it requires theoretical justification, not statistical proof.
- A 'weak instrument' (low Cov(z,x)) produces IV estimates that are biased toward OLS and have very wide confidence intervals.

## Questions

```yaml
- question: "A researcher wants to use distance to the nearest college as an instrument for years of education in a wage regression. Which condition is most difficult to satisfy and cannot be verified statistically?"
  type: multiple-choice
  options:
    - "Relevance — distance to college must be correlated with years of education"
    - "Exclusion restriction — distance to college must not directly affect wages"
    - "The instrument must be binary (0/1)"
    - "The instrument must be uncorrelated with education"
  answer: 1
  explanation: "The exclusion restriction requires that the instrument affects the outcome only through the endogenous regressor — here, that distance to college affects wages only by changing education levels, not through any other channel (e.g., local labor markets). This cannot be tested statistically and must be justified on economic grounds. Relevance, by contrast, can be tested with an F-test on the first stage."

- question: "If the exclusion restriction holds but your instrument is very weakly correlated with the endogenous regressor, your IV estimate will be more reliable than OLS."
  type: true-false
  answer: false
  explanation: "A weak instrument (low first-stage F-statistic, conventionally below 10) produces IV estimates that are severely biased toward OLS and have extremely wide confidence intervals. The bias comes from finite-sample amplification of any small violation of the exclusion restriction. Weak instruments make IV worse than OLS, not better — strength of the first stage is essential."

- question: "In the bivariate IV formula β̂ᵢᵥ = Cov(z,y)/Cov(z,x), what is the intuition for why dividing by Cov(z,x) is necessary?"
  type: short-answer
  answer: "Cov(z,y) captures the total effect of z on y, but since z only affects y through x, we need to scale by how much z moves x (Cov(z,x)) to isolate the effect of x on y. Dividing by Cov(z,x) essentially asks: for each unit that z shifts x, how much does y change?"
  explanation: "The IV estimator uses z as an external shifter of x. Cov(z,y) picks up the z-induced variation in y, and Cov(z,x) measures how strongly z shifts x. Their ratio recovers the causal effect of x on y by scaling the reduced-form effect by the first-stage relationship — analogous to dividing out the channel strength."
```

## Explainer

You have already seen that OLS is biased when the regressor x is correlated with the error term u — the endogeneity problem. Instrumental variables offer a way out: find a third variable z that pushes x around but has no independent relationship with y. If you can isolate only the variation in x that z drives, that variation is clean of the omitted variable or reverse causation that corrupted OLS.

The two conditions a valid instrument must satisfy are relevance and the exclusion restriction. Relevance is straightforward: Cov(z,x) ≠ 0, meaning z is actually correlated with x. You can test this directly — regress x on z and check the F-statistic (a rule of thumb is F > 10 for a strong instrument). The exclusion restriction is harder: Cov(z,u) = 0, meaning z is uncorrelated with anything else that drives y. This assumption cannot be tested; it is an economic argument. For the quarter-of-birth instrument, you must argue that the quarter a person happened to be born in has no effect on their adult wages except by changing how long they stayed in school — and that is genuinely controversial.

The bivariate IV estimator is β̂ᵢᵥ = Cov(z,y)/Cov(z,x). The numerator captures how much y changes when z moves; the denominator scales that by how much x changes when z moves. The ratio recovers the causal effect of x on y. Intuitively, you are asking: "Of all the ways z moved x, how much did y move per unit of that x-movement?" The OLS analog, Cov(x,y)/Var(x), uses all variation in x — including the endogenous part. IV uses only the z-driven variation, which is exogenous by assumption.

A critical practical warning: weak instruments are dangerous. If Cov(z,x) is small, the denominator of the IV estimator is close to zero, which amplifies any small violation of the exclusion restriction into a huge bias. Weak instruments can produce estimates that are worse than OLS — biased in the same direction but with false precision. Always report the first-stage F-statistic when presenting IV results.

Finally, IV identifies a Local Average Treatment Effect (LATE) — the causal effect for the subpopulation whose behavior was actually changed by the instrument (the "compliers"). This is not the same as the average treatment effect for the full population. Quarter of birth only shifts education for people who would otherwise have dropped out before compulsory attendance laws required them to stay — not for everyone. Understanding what population your IV result applies to is as important as getting the mechanics right.
