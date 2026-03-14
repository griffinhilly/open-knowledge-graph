---
id: endogeneity
title: Endogeneity
domain: economics
course: econometrics
prerequisites:
- id: omitted-variable-bias
  type: hard
- id: ols-assumptions
  type: hard
builds-toward:
- instrumental-variables
- panel-data-basics
tags:
- endogeneity
- simultaneity
- measurement-error
- bias
stage: formal-systems
status: validated
---

# Endogeneity

## Core Idea
Endogeneity is a general term for any situation where a regressor is correlated with the error term, making OLS biased and inconsistent. There are three main sources: omitted variable bias (a confound is excluded from the model), simultaneity (y and x are jointly determined, as when price and quantity are both endogenous in a supply-demand system), and measurement error (x is measured with noise, attenuating its coefficient toward zero via 'attenuation bias'). Endogeneity is the central identification problem in applied economics, and most advanced methods — instrumental variables, panel fixed effects, regression discontinuity, difference-in-differences — are designed to address specific forms of it.

## How It's Best Learned
Work through three separate examples, one for each source of endogeneity, and derive the direction of bias for each. The supply-demand simultaneity example is essential for macroeconomics applications.

## Common Misconceptions
- Endogeneity is not about the dependent variable being 'determined inside a model'; it specifically means Cov(xⱼ, u) ≠ 0.
- Measurement error in y does not cause endogeneity; only measurement error in x creates attenuation bias.
