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

## Questions

```yaml
- question: "You run a Hausman test comparing fixed effects (FE) and random effects (RE) estimators on panel data. The test statistic H is large with a very small p-value. What should you conclude and do?"
  type: multiple-choice
  options:
    - "Reject the null; both estimators are consistent but FE is more efficient, so use FE"
    - "Fail to reject the null; RE is preferred because it uses more variation and is more efficient"
    - "Reject the null; the RE orthogonality assumption likely fails, so use FE which remains consistent"
    - "Reject the null; neither estimator is reliable and you should use first-differences instead"
  answer: 2
  explanation: "A large H (small p-value) rejects the null hypothesis that the unobserved unit effects are uncorrelated with the regressors. Under the alternative, RE is biased and inconsistent (because it assumes orthogonality that doesn't hold), while FE remains consistent by differencing out the unit effects. You switch to FE. Option A has the efficiency claim backwards: it is RE that is more efficient under the null, not FE. Option D overstates the result — a Hausman rejection doesn't make FE unreliable, just RE."

- question: "Under the null hypothesis of the Hausman test, why is random effects preferred over fixed effects despite both being consistent?"
  type: multiple-choice
  options:
    - "Random effects uses only within-unit variation, which is more reliable than cross-sectional variation"
    - "Random effects uses both within-unit and between-unit variation, producing estimates with smaller variance than fixed effects"
    - "Random effects is preferred because it does not require the strict exogeneity assumption that fixed effects does"
    - "Random effects has fewer parameters to estimate, making it computationally more tractable"
  answer: 1
  explanation: "Fixed effects eliminates unobserved heterogeneity by demeaning within each unit — but in doing so, it discards all cross-sectional (between-unit) variation. Random effects, when its orthogonality assumption holds, incorporates both within-unit and between-unit variation into a GLS-type estimator, using more information. More information translates to more efficient (lower variance) estimates. Efficiency is the precise statistical term for this advantage: under the null, RE is consistent AND uses more variation, so it is the better estimator."

- question: "Rejecting the null hypothesis on the Hausman test means your fixed effects estimates are unbiased and fully reliable for causal inference."
  type: true-false
  answer: false
  explanation: "A Hausman rejection tells you that RE is inconsistent — not that FE is perfect. FE is consistent under correlated unit effects, but it faces its own limitations: it cannot identify time-invariant variables (they are differenced out), it requires strict exogeneity of the regressors, and with short panels it can have finite-sample bias. A Hausman rejection is the beginning of careful analysis, not the end — it should prompt investigation of which variables drive the correlation between unit effects and regressors, since those omitted drivers may have substantive implications."

- question: "Under the null hypothesis of the Hausman test, both the fixed effects and random effects estimators are consistent, but random effects is more efficient."
  type: true-false
  answer: true
  explanation: "This is the core logic of the test. When the RE orthogonality assumption holds (unit effects uncorrelated with regressors), RE exploits both within-unit and between-unit variation — giving consistent estimates with smaller standard errors than FE, which only uses within variation. Under the alternative (correlated effects), RE becomes inconsistent while FE remains consistent. The test's power comes from comparing the two: if they agree (small H), RE's efficiency gain makes it the better choice; if they diverge (large H), only FE can be trusted."

- question: "What is the key assumption of the random effects estimator that the Hausman test probes, and why does its violation render RE estimates inconsistent?"
  type: short-answer
  answer: "The RE estimator assumes that the unobserved individual-specific effects (α_i) are uncorrelated with the regressors (X_it). If this orthogonality assumption fails — if, say, a person's unobserved ability is correlated with their observed education level — then the RE estimator attributes some of α_i's effect to the observed regressors, biasing the coefficient estimates. Because this bias does not vanish as the sample grows (the same mis-attribution persists for every unit), RE is inconsistent. FE avoids this by demeaning within each unit, which differences out α_i entirely and eliminates the source of bias."
  explanation: "The intuition parallels omitted variable bias: if an omitted variable (here, the unit effect) is correlated with an included regressor, its effect 'leaks' into that regressor's coefficient. RE's GLS structure implicitly controls for the unit effect only under the orthogonality assumption. When that fails, the control is incomplete. FE's within-transformation is exact — it removes the unit effect algebraically — at the cost of losing between-unit information. The Hausman test asks: is the information loss worth it? If the RE assumption fails, yes."
```

## Explainer

When you studied the within estimator (fixed effects) and the between estimator, you encountered a fundamental trade-off in panel data: fixed effects eliminate unobserved time-invariant heterogeneity at the cost of throwing away cross-sectional variation, while random effects use all the variation — both within and between units — but only give consistent estimates if the unobserved heterogeneity is uncorrelated with the regressors. The Hausman test is the tool that tells you which assumption holds in your data.

The intuition is clean. Under the **null hypothesis** that random effects is appropriate (the unobserved individual effects are uncorrelated with the regressors), both the fixed effects estimator and the random effects estimator are consistent, but random effects is more efficient — it uses more variation. Under the **alternative hypothesis** that the unobserved effects are correlated with regressors, fixed effects is still consistent (it differences them out), but random effects is biased and inconsistent. So if the two estimators give similar answers, random effects is preferred for efficiency. If they give very different answers, that divergence is evidence the random effects assumption has failed, and you should use fixed effects.

The test statistic formalizes this logic. Hausman showed that, under the null, the **covariance of the difference** between the two estimators simplifies elegantly: Cov(β̂_FE − β̂_RE, β̂_RE) = 0. This means the variance of the difference equals Var(β̂_FE) − Var(β̂_RE). The test statistic H = (β̂_FE − β̂_RE)′ [Var(β̂_FE) − Var(β̂_RE)]⁻¹ (β̂_FE − β̂_RE) is asymptotically chi-squared with degrees of freedom equal to the number of time-varying regressors being compared. A large H (small p-value) rejects the null and favors fixed effects.

In practice, interpreting the Hausman test requires care. A rejection tells you that correlated unobserved heterogeneity is likely present — but it does not tell you which variables are driving the correlation. Sometimes only a subset of regressors are correlated with the unit effects, and a partial Hausman test isolating those variables is more informative. The test also has known finite-sample problems: with robust standard errors, the standard formula for the variance of the difference can yield a negative-definite matrix, requiring a generalized inverse or a bootstrap version. A rejection of the null does not mean your fixed effects estimates are perfect — it means random effects is inconsistent, and fixed effects is the safer choice. The appropriate response to a Hausman rejection is not merely to switch estimators, but to think carefully about what unobserved characteristics might be correlated with your variables of interest, since those omitted drivers may have substantive implications for your research question.
