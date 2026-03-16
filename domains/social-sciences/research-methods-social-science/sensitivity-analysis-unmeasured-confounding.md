---
id: sensitivity-analysis-unmeasured-confounding
title: 'Sensitivity Analysis: Robustness to Unmeasured Confounding'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: matching-and-weighting-causal-estimation
  type: hard
- id: covariance-between-random-variables
  type: soft
tags:
- sensitivity-analysis
- unmeasured-confounding
- robustness
stage: advanced
status: draft
---

# Sensitivity Analysis: Robustness to Unmeasured Confounding

## Core Idea
All observational causal estimates depend on unverifiable assumptions about unmeasured confounders. Sensitivity analysis quantifies how large unmeasured confounding must be to overturn conclusions. This acknowledges uncertainty while assessing robustness.

## Explainer

From your work on matching and weighting, you know that these methods balance observed covariates between treatment and control groups — essentially eliminating the influence of confounders you can measure. But matching and weighting cannot touch what you cannot see. The fundamental limitation of any observational study is the **no unmeasured confounding assumption** (also called ignorability or exchangeability): the claim that all variables that affect both treatment assignment and the outcome have been measured and controlled for. This assumption is unverifiable from the data itself. Sensitivity analysis is the discipline of reasoning carefully about how wrong this assumption can be before your conclusion falls apart.

The intuition is best grasped through an example. Suppose you estimate that a job training program raises earnings by $4,000. You have matched participants to comparable non-participants on age, education, and prior employment history. But what if motivated individuals — people with ambition not captured in your measured variables — were both more likely to enroll in the program and more likely to earn more regardless of the program? **Unmeasured confounding by motivation** could explain some or all of the estimated effect. Sensitivity analysis asks: how strong would this unmeasured confounder need to be — how much more likely are motivated people to enroll, and how much more do they earn on average — to reduce the $4,000 estimate to zero? If the answer is "implausibly strong," your conclusion is robust. If a modest, plausible amount of confounding would do it, your conclusion is fragile.

The most widely used formal framework is the **Rosenbaum sensitivity analysis** for matched studies, which parameterizes unmeasured confounding as a single value Γ (gamma): the maximum odds ratio by which an unmeasured confounder could differ between a matched pair. At Γ = 1, no unmeasured confounding exists. As Γ increases, the p-value for your treatment effect eventually crosses the significance threshold. Reporting "results remain significant at Γ = 2" tells readers that an unmeasured confounder would need to double the odds of treatment assignment — holding all measured covariates constant — to explain away the result. Your knowledge of covariance between random variables helps here: confounders do damage in proportion to how strongly they covary with both treatment assignment and the outcome. A variable that strongly predicts treatment but is unrelated to the outcome (or vice versa) cannot confound the estimate, no matter how unobserved it is.

The key conceptual shift sensitivity analysis demands is treating causal conclusions as conditional rather than absolute. The output of an observational study is not "X causes Y" but "if unmeasured confounding is smaller than a certain threshold, X causes Y." Reporting this conditional conclusion honestly, alongside substantive reasoning about whether that threshold is plausible given domain knowledge, is what distinguishes careful causal inference from naive correlation. Sensitivity analysis does not fix unmeasured confounding — nothing can — but it transforms a hidden vulnerability into an explicit, arguable claim about how fragile or robust your finding really is.
