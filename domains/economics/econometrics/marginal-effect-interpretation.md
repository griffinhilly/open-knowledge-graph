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
stage: formal-systems
status: draft
---

# Marginal Effects and Partial Effects Measurement

## Core Idea
Marginal effects measure the change in predicted outcome for a unit increase in a regressor. The average marginal effect (AME) averages individual effects across the sample; the marginal effect at the mean (MEM) evaluates at sample means.

## Explainer

In a linear regression, the coefficient on a variable is directly the marginal effect — it tells you how much the predicted outcome changes for a one-unit increase in that variable, holding others constant. This holds everywhere: the slope is constant by construction. From your work on nonlinear models, you know that this clean interpretation breaks down in logit, probit, Poisson, or any model where the link function is nonlinear. The coefficient on x in a logit is the change in the **log-odds**, not the change in the probability. To translate from the model's internal scale to the quantity you actually care about (change in probability, change in count, etc.), you need marginal effects.

The **marginal effect at the mean (MEM)** is the simplest approach: evaluate the derivative ∂E[Y|X]/∂xⱼ at the sample means of all regressors. For a probit model, this is φ(X̄β̂)·β̂ⱼ, where φ is the standard normal density. It answers: "for the 'average' person in the dataset, what is the marginal effect?" The conceptual problem is that the "average person" often doesn't exist — if your sample includes both men and women, the mean gender (say, 0.52) corresponds to no real individual, and evaluating a nonlinear function at a non-existent point can be misleading.

The **average marginal effect (AME)** avoids this by computing the marginal effect for each actual observation in the sample and then averaging: AME = (1/N)Σᵢ ∂E[Y|Xᵢ]/∂xⱼ. This answers: "on average across the observed population, what is the marginal effect?" For logit, each individual's marginal effect depends on their predicted probability — people with probabilities near 0.5 have larger marginal effects than those near 0 or 1, where the response curve is flat. The AME captures this heterogeneity correctly. For this reason, the AME is generally preferred in applied work; it better represents the average effect in the actual sample rather than the effect at a hypothetical average point.

For discrete changes (like a binary variable switching from 0 to 1) or for counting nonmarginal shifts, you report a **partial effect**: the difference in predicted values at two specific covariate settings, not the derivative. For a binary regressor, the AME computed as a derivative is often approximated as the average of Ê[Y|xⱼ=1, X₋ⱼ] − Ê[Y|xⱼ=0, X₋ⱼ] across all individuals — this is the "recycled predictions" approach. The key discipline is always to be explicit about what you are holding constant and where in the covariate distribution you are evaluating the effect; nonlinear models cannot be summarized by a single number without making those choices explicit.
