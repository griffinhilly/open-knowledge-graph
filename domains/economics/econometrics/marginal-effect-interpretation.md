---
id: marginal-effect-interpretation
title: Marginal Effects and Partial Effects Measurement
domain: economics
course: econometrics
prerequisites:
- id: nonlinear-models-interpretation
  type: hard
tags:
- interpretation
- marginal-effects
- ame
- mem
stage: advanced
status: draft
---

# Marginal Effects and Partial Effects Measurement

## Core Idea
Marginal effects measure the change in predicted outcome for a unit increase in a regressor. The average marginal effect (AME) averages individual effects across the sample; the marginal effect at the mean (MEM) evaluates at sample means.

## Questions

```yaml
- question: "A researcher estimates a probit model of employment and reports the coefficient on 'college degree' (a binary variable) as 0.8. What does this number directly represent?"
  type: multiple-choice
  options:
    - "The probability that a college graduate is employed compared to a non-graduate"
    - "The percentage-point increase in employment probability for college graduates"
    - "The change in the latent index (log-odds scale) for a college graduate versus a non-graduate"
    - "The average marginal effect of college education, interpretable as an 8-percentage-point increase"
  answer: 2
  explanation: "In a probit model, coefficients are on the scale of the latent index (the argument of the normal CDF), not on the probability scale. A coefficient of 0.8 means the index increases by 0.8 for college graduates — which corresponds to some increase in probability that depends on where on the CDF you are evaluating. To get the probability-scale effect, you need to compute a marginal effect: multiply by the normal density φ(Xβ) at the relevant covariate values."

- question: "Researchers compute the marginal effect at the mean (MEM) for a binary gender variable (sample mean ≈ 0.52) in a logit model. A colleague argues they should use the average marginal effect (AME) instead. What is the colleague's strongest argument?"
  type: multiple-choice
  options:
    - "AME is computationally simpler because it requires only one evaluation of the model"
    - "MEM requires evaluating at the median rather than the mean, making it systematically biased"
    - "No individual in the sample has gender = 0.52, so evaluating a nonlinear function at this non-existent point can produce a misleading estimate"
    - "AME and MEM always produce identical estimates, so MEM is redundant and AME is the conventional standard"
  answer: 2
  explanation: "The MEM evaluates the predicted effect at the sample mean of all covariates. For a binary variable like gender, the sample mean (0.52) corresponds to no real individual. Evaluating a nonlinear function (like the logistic CDF) at a fictional average point differs from the average of evaluating it at each real individual — Jensen's inequality tells us f(E[X]) ≠ E[f(X)] when f is nonlinear. The AME computes effects at each actual observation and then averages, avoiding this conceptual problem."

- question: "In a linear regression model, the coefficient on a variable is the marginal effect on the outcome. The same interpretation applies to coefficients in a logit regression."
  type: true-false
  answer: false
  explanation: "In linear regression, the coefficient is directly the marginal effect on the outcome because the relationship is linear. In logit (and probit, Poisson, etc.), the coefficient is on an internal transformed scale — log-odds for logit, the latent index for probit, log-count for Poisson. The marginal effect on the probability (or count) requires computing the derivative of the predicted outcome with respect to the covariate, which involves the derivative of the link function and varies by observation."

- question: "For a binary regressor in a logit model, the average marginal effect can be estimated by computing each individual's difference in predicted probabilities when the regressor switches from 0 to 1, then averaging those differences across the sample."
  type: true-false
  answer: true
  explanation: "This 'recycled predictions' approach is the standard way to compute AME for discrete variables. For each observation, you compute two predicted probabilities — one with the binary variable set to 0, one set to 1 — and take the difference. Averaging these individual differences gives the AME. It correctly handles the heterogeneity in marginal effects that arises from observations at different points on the logistic curve."

- question: "Why is the average marginal effect (AME) generally preferred over the marginal effect at the mean (MEM) in applied work with nonlinear models? Explain the conceptual difference."
  type: short-answer
  answer: "The AME computes the marginal effect for each actual observation in the sample, then averages across real individuals. The MEM evaluates the marginal effect at a hypothetical 'average individual' constructed from sample means. In nonlinear models, these differ because the marginal effect depends on the covariate values — people near the middle of the response curve have larger marginal effects than those near the extremes. By averaging over actual people, AME correctly captures this heterogeneity. MEM relies on a non-existent 'average person,' which can be a misleading summary point when covariates are binary or highly skewed."
  explanation: "The key mathematical issue is Jensen's inequality: for a nonlinear function g, E[g(X)] ≠ g(E[X]). MEM computes g(E[X]); AME computes E[g(X)]. AME is the more interpretable quantity for most policy questions because it represents 'the average effect on the actual population' rather than 'the effect on a hypothetical average person.'"
```

## Explainer

In a linear regression, the coefficient on a variable is directly the marginal effect — it tells you how much the predicted outcome changes for a one-unit increase in that variable, holding others constant. This holds everywhere: the slope is constant by construction. From your work on nonlinear models, you know that this clean interpretation breaks down in logit, probit, Poisson, or any model where the link function is nonlinear. The coefficient on x in a logit is the change in the **log-odds**, not the change in the probability. To translate from the model's internal scale to the quantity you actually care about (change in probability, change in count, etc.), you need marginal effects.

The **marginal effect at the mean (MEM)** is the simplest approach: evaluate the derivative ∂E[Y|X]/∂xⱼ at the sample means of all regressors. For a probit model, this is φ(X̄β̂)·β̂ⱼ, where φ is the standard normal density. It answers: "for the 'average' person in the dataset, what is the marginal effect?" The conceptual problem is that the "average person" often doesn't exist — if your sample includes both men and women, the mean gender (say, 0.52) corresponds to no real individual, and evaluating a nonlinear function at a non-existent point can be misleading.

The **average marginal effect (AME)** avoids this by computing the marginal effect for each actual observation in the sample and then averaging: AME = (1/N)Σᵢ ∂E[Y|Xᵢ]/∂xⱼ. This answers: "on average across the observed population, what is the marginal effect?" For logit, each individual's marginal effect depends on their predicted probability — people with probabilities near 0.5 have larger marginal effects than those near 0 or 1, where the response curve is flat. The AME captures this heterogeneity correctly. For this reason, the AME is generally preferred in applied work; it better represents the average effect in the actual sample rather than the effect at a hypothetical average point.

For discrete changes (like a binary variable switching from 0 to 1) or for counting nonmarginal shifts, you report a **partial effect**: the difference in predicted values at two specific covariate settings, not the derivative. For a binary regressor, the AME computed as a derivative is often approximated as the average of Ê[Y|xⱼ=1, X₋ⱼ] − Ê[Y|xⱼ=0, X₋ⱼ] across all individuals — this is the "recycled predictions" approach. The key discipline is always to be explicit about what you are holding constant and where in the covariate distribution you are evaluating the effect; nonlinear models cannot be summarized by a single number without making those choices explicit.
