---
id: hausman-specification-test
title: 'Hausman Test: Fixed Effects Versus Random Effects'
domain: economics
course: econometrics
prerequisites:
- id: within-estimator-panel
  type: hard
- id: between-estimator-panel
  type: hard
builds-toward:
- dynamic-panel-gmm
tags:
- panel-data
- testing
- specification
stage: formal-systems
status: draft
---

# Hausman Test: Fixed Effects Versus Random Effects

## Core Idea
The Hausman test compares fixed and random effects estimators; a large difference suggests the random effects orthogonality assumption is violated. Under the null hypothesis, the test statistic is asymptotically chi-squared, guiding practitioners toward fixed effects when the assumption fails.

## Explainer

When you studied the within estimator (fixed effects) and the between estimator, you encountered a fundamental trade-off in panel data: fixed effects eliminate unobserved time-invariant heterogeneity at the cost of throwing away cross-sectional variation, while random effects use all the variation — both within and between units — but only give consistent estimates if the unobserved heterogeneity is uncorrelated with the regressors. The Hausman test is the tool that tells you which assumption holds in your data.

The intuition is clean. Under the **null hypothesis** that random effects is appropriate (the unobserved individual effects are uncorrelated with the regressors), both the fixed effects estimator and the random effects estimator are consistent, but random effects is more efficient — it uses more variation. Under the **alternative hypothesis** that the unobserved effects are correlated with regressors, fixed effects is still consistent (it differences them out), but random effects is biased and inconsistent. So if the two estimators give similar answers, random effects is preferred for efficiency. If they give very different answers, that divergence is evidence the random effects assumption has failed, and you should use fixed effects.

The test statistic formalizes this logic. Hausman showed that, under the null, the **covariance of the difference** between the two estimators simplifies elegantly: Cov(β̂_FE − β̂_RE, β̂_RE) = 0. This means the variance of the difference equals Var(β̂_FE) − Var(β̂_RE). The test statistic H = (β̂_FE − β̂_RE)′ [Var(β̂_FE) − Var(β̂_RE)]⁻¹ (β̂_FE − β̂_RE) is asymptotically chi-squared with degrees of freedom equal to the number of time-varying regressors being compared. A large H (small p-value) rejects the null and favors fixed effects.

In practice, interpreting the Hausman test requires care. A rejection tells you that correlated unobserved heterogeneity is likely present — but it does not tell you which variables are driving the correlation. Sometimes only a subset of regressors are correlated with the unit effects, and a partial Hausman test isolating those variables is more informative. The test also has known finite-sample problems: with robust standard errors, the standard formula for the variance of the difference can yield a negative-definite matrix, requiring a generalized inverse or a bootstrap version. A rejection of the null does not mean your fixed effects estimates are perfect — it means random effects is inconsistent, and fixed effects is the safer choice. The appropriate response to a Hausman rejection is not merely to switch estimators, but to think carefully about what unobserved characteristics might be correlated with your variables of interest, since those omitted drivers may have substantive implications for your research question.
