---
id: nonlinear-models-interpretation
title: Interpretation and Marginal Effects in Nonlinear Models
domain: economics
course: econometrics
prerequisites:
- id: logit-probit-models
  type: hard
- id: maximum-likelihood-econometrics
  type: hard
- id: polynomial-regression-econometrics
  type: soft
tags:
- nonlinear
- interpretation
- marginal-effects
stage: advanced
status: validated
---
# Interpretation and Marginal Effects in Nonlinear Models

## Core Idea
In logit, probit, and other nonlinear models, raw coefficients do not represent marginal effects on the outcome. The effect of a unit change in X depends on both the coefficient and the probability/density evaluated at specific covariate values.

## How It's Best Learned
Calculate marginal effects at the mean (MEM) and average marginal effects (AME) for a few key variables. Use plots to show how predicted probabilities change across the range of X.

## Questions

```yaml
- question: "A logit regression on voter turnout yields a coefficient of 0.25 on annual income (in thousands of dollars). What does this coefficient directly represent?"
  type: multiple-choice
  options:
    - "A $1,000 increase in income raises the probability of voting by 25 percentage points"
    - "A $1,000 increase in income raises the log-odds of voting by 0.25"
    - "A $1,000 increase in income multiplies the odds of voting by 0.25"
    - "A $1,000 increase in income raises the predicted probability of voting by 0.25 times the baseline probability"
  answer: 1
  explanation: "Logit coefficients measure the change in log-odds (the natural log of the probability of success divided by the probability of failure) per unit change in X. The log-odds scale is where the logit model is linear in the parameters, which is why MLE estimation works. However, log-odds are not probabilities — translating this coefficient into a probability effect requires computing the marginal effect, which depends on the baseline probability through the logistic function's derivative. Option A (25 percentage points) is the classic mistake of reading logit coefficients as if they were OLS regression coefficients. Option C incorrectly states multiplicative odds (that would be exp(0.25) ≈ 1.28, not 0.25)."

- question: "Two individuals are modeled in a logit regression. Individual A has a baseline predicted probability of 20% and Individual B has a baseline predicted probability of 70%. Both have the same coefficient β on variable X. Which individual has the larger marginal effect of X on their predicted probability?"
  type: multiple-choice
  options:
    - "Individual A, because people with lower baseline probabilities have more room to move upward"
    - "Individual B, because 70% is closer to the 50% midpoint where the logistic curve has its steepest slope"
    - "Both have identical marginal effects, since the coefficient β is the same for all observations"
    - "It depends on the direction of the coefficient — positive coefficients favor A, negative favor B"
  answer: 1
  explanation: "The marginal effect of X on probability in a logit model is β × p(1−p), where p is the predicted probability. At p = 0.20: ME = β × 0.20 × 0.80 = 0.16β. At p = 0.70: ME = β × 0.70 × 0.30 = 0.21β. So Individual B, at 70%, has the larger marginal effect. The logistic function is steepest at p = 0.5 (where ME = 0.25β) and flatter toward both extremes. Counterintuitively, the person with 20% probability is NOT closer to the center — 70% is closer to 50% than 20% is — so B's marginal effect is larger. Option A reflects the misconception that low-probability individuals always have the most 'room to move.' Option C is the core mistake: same coefficient does NOT mean same probability-scale marginal effect."

- question: "Average marginal effects (AME) and marginal effects at the mean (MEM) typically produce the same estimate in logit and probit models."
  type: true-false
  answer: false
  explanation: "False. AME and MEM differ whenever the relationship between covariates and outcomes is nonlinear — which is always the case in logit and probit. MEM computes the marginal effect at a single hypothetical 'average person' (plugging in mean values of all covariates). AME computes the marginal effect separately for each individual in the sample using their actual covariate values, then averages those effects. Because p(1−p) is a nonlinear function, averaging and then evaluating is not the same as evaluating and then averaging. AME is generally preferred because the 'average person' may not correspond to any real individual, and AME appropriately weights the distribution of baseline probabilities across the sample."

- question: "In a probit or logit model, reporting just the coefficient value without computing marginal effects is sufficient for a reader to judge the practical importance of a variable."
  type: true-false
  answer: false
  explanation: "False. A logit coefficient of 2.0 versus 0.1 signals relative importance, but neither coefficient tells you whether the variable raises probability by 0.5 percentage points or 15 percentage points — that depends entirely on where in the S-curve the typical observation sits. A large coefficient at an extreme predicted probability (near 0 or 1) may produce tiny probability-scale effects; a small coefficient near p = 0.5 may produce substantial effects. Without marginal effects, the reader cannot assess practical significance. This is analogous to reporting a standardized test score without the raw score — the internal comparison is meaningful but the external interpretation requires translation."

- question: "Explain why the same logit coefficient β produces different marginal effects on predicted probability for different individuals, and describe how the average marginal effect (AME) accounts for this."
  type: short-answer
  answer: "In a logit model, the marginal effect on probability is β × p(1−p), where p is the individual's predicted probability. Because p(1−p) varies with p — it is largest at p = 0.5 and approaches zero near p = 0 or p = 1 — the same β maps to different probability-scale effects depending on where each person sits on the logistic S-curve. AME accounts for this by computing β × p_i(1−p_i) for each individual i using their own predicted probability, then averaging these individual-specific marginal effects across the full sample. This gives a single summary effect that respects the actual distribution of baseline probabilities in the data."
  explanation: "The practical implication is that reporting only the AME can still be misleading if the sample is heterogeneous. In a voting example, the average marginal effect of education might be 2 percentage points, but for low-income voters already near certain abstention (p ≈ 0.05), the marginal effect might be 0.4 pp, while for engaged voters near the margin (p ≈ 0.5), it could be 5 pp. Disaggregating by subgroup reveals this heterogeneity that the AME compresses."
```

## Explainer

In a linear regression model, the coefficient β on a variable X has a clean interpretation: a one-unit increase in X shifts the predicted outcome by exactly β, regardless of where X starts, who the observation is, or what other variables look like. This constant-effect property is what makes linear regression coefficients so easy to communicate. Nonlinear models like logit and probit, which you studied as prerequisites, trade away this simplicity in exchange for a more appropriate model of binary outcomes — and the price is that interpretation requires an extra step.

In a **logit model**, the coefficient β on X tells you how much the **log-odds** (the log of the probability of success divided by the probability of failure) changes for a one-unit increase in X. The log-odds scale is linear in the parameters, which is why maximum likelihood estimation works cleanly. But log-odds are not probabilities, and the translation from log-odds to probabilities is nonlinear — it runs through the logistic function, which produces the familiar S-shaped curve. This means the effect of X on the probability of success depends on where on the S-curve you are sitting. Near the tails (very high or very low predicted probabilities), the curve is nearly flat, so a coefficient of 0.5 on X translates into a very small probability change. Near the middle of the curve (baseline probability around 0.5), the same coefficient translates into a much larger probability change.

This is why raw logit or probit coefficients should never be directly interpreted as probability effects. Instead, economists compute **marginal effects** — the derivative of the predicted probability with respect to X, evaluated at specific covariate values. Two approaches are standard. **Marginal effects at the mean (MEM)** evaluate the derivative at the sample mean of each covariate: you plug in the average age, average income, average education level, and compute the probability change for a one-unit shift in X at that hypothetical "average" individual. **Average marginal effects (AME)** compute the derivative for every observation in the sample using their actual covariate values, then average those individual effects. AME is generally preferred because the "average individual" may not represent anyone in the data — averages of many characteristics may not correspond to any real person.

Consider a concrete example: estimating the effect of years of education on the probability of voting. A logit coefficient of 0.2 on education means log-odds increase by 0.2 per year of education. But for someone currently at a 20% baseline voting probability, this might translate into a 3 percentage-point increase per year of education. For someone at a 70% baseline probability, the same coefficient might translate into only 1.5 percentage points. The AME across the full sample might be 2.2 percentage points — that is the number you would report and discuss. **Discrete change effects** extend this logic to dummy variables: for a binary X (e.g., college degree vs. no degree), you compute the change in predicted probability when X switches from 0 to 1, rather than taking a derivative. The same nonlinearity applies, reinforcing that no single number captures the "effect" of a variable — context always determines magnitude.
