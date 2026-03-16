---
id: instrumental-variables-causal-effects
title: 'Instrumental Variables: Exogenous Variation for Causal Estimation'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: instrumental-variables-methods
  type: hard
- id: causal-inference-from-observation
  type: soft
tags:
- instrumental-variables
- iv
- endogeneity
- 2sls
stage: advanced
status: draft
---

# Instrumental Variables: Exogenous Variation for Causal Estimation

## Core Idea
Instrumental variable estimation addresses endogeneity—when predictors correlate with errors due to omitted variables, simultaneity, or measurement error. An instrument correlates with treatment but affects outcomes only through the treatment. IV produces consistent estimates under strict assumptions.

## Explainer

You already understand from causal inference that observational data is plagued by **endogeneity** — situations where the treatment variable correlates with the error term of the regression, making OLS estimates biased and inconsistent. The most common cause is an **omitted variable**: something that affects both who receives the treatment and what the outcome is. If you want to estimate the effect of education on wages but smarter people both get more education and earn more, a simple regression confounds the education effect with the ability effect. Instrumental variables offer a surgical solution to this problem.

The core intuition is to find a variable — the **instrument** — that provides a source of variation in the treatment that is unrelated to the confound. A valid instrument must satisfy two conditions. First, **relevance**: the instrument must actually affect the treatment (it must predict who gets more or less education). Second, **exclusion restriction**: the instrument must affect the outcome *only* through the treatment — it has no direct effect on wages except by changing education. The exclusion restriction is the harder condition, and it cannot be tested with data alone; it must be justified on theoretical grounds. A classic instrument for education is distance to college: students who grew up near colleges got more education (relevance), and distance to college affects earnings only because it affected educational attainment (exclusion restriction — at least plausibly).

**Two-stage least squares (2SLS)** is the standard estimation procedure. In the first stage, you regress the endogenous treatment variable on the instrument (and any controls), extracting the portion of treatment variation that is driven purely by the instrument. In the second stage, you use the predicted values from stage one — the "clean" variation — as the regressor in the outcome equation. The key insight is that this predicted treatment is, by construction, uncorrelated with the error term, because the instrument is uncorrelated with it. You have effectively purged the endogeneity.

IV estimates should be interpreted carefully. When the instrument only moves some people's treatment — those who comply with the instrument — the IV estimate identifies a **local average treatment effect (LATE)**: the causal effect for compliers, not for the full population. Someone who would get a college degree regardless of distance (always-taker) or would never get one regardless (never-taker) doesn't contribute identification. This means IV estimates can differ substantially from OLS even when OLS is valid for a different estimand — the estimates answer different questions about different subpopulations.

Practical IV application also faces the **weak instruments problem**: if the instrument only weakly predicts the treatment, the first-stage is noisy and second-stage estimates become very imprecise and can even be biased. The F-statistic on the excluded instrument in the first stage (conventionally ≥10 as a rule of thumb) is the primary diagnostic. When multiple instruments are available, overidentification tests like the Sargan-Hansen test provide some purchase on whether the exclusion restriction holds — if instruments are valid, they should all point to the same estimate. Together, these diagnostics discipline the application of what is one of the most powerful but also most assumption-dependent tools in the causal inference toolkit.
