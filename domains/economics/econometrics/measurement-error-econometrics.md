---
id: measurement-error-econometrics
title: Measurement Error and Its Consequences
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: omitted-variable-bias
  type: soft
tags:
- measurement-error
- attenuation-bias
- iv
stage: formal-systems
status: draft
---

# Measurement Error and Its Consequences

## Core Idea
Measurement error in a regressor causes classical attenuation bias, shrinking OLS coefficients toward zero. Measurement error in the outcome increases standard errors. Instrumental variables can address measurement error if valid instruments exist.

## How It's Best Learned
Simulate data with known measurement error and observe how coefficients shrink. Consider IV estimation or instrumental variable techniques if measurement error is suspected.

## Explainer

The OLS assumptions you studied require that regressors are measured accurately. In practice, nearly every economic variable is imperfectly measured: income is self-reported and underreported, education is proxied by years of schooling rather than actual human capital, calorie intake is recalled rather than observed, and survey responses contain random error. Understanding what this does to your estimates is essential before drawing policy conclusions from data.

Start with the simplest case: **classical measurement error in a regressor**. Suppose the true model is y = β·x* + ε, but you observe x = x* + u, where u is random noise uncorrelated with x*. You can only run the regression of y on x. It turns out the OLS estimator of β converges not to β, but to β · [Var(x*) / (Var(x*) + Var(u))]. This fraction — the ratio of true variance to observed variance — is always between 0 and 1. This is **attenuation bias**: measurement error shrinks the estimated coefficient toward zero. The noisier your measure, the more severe the attenuation. If you're trying to estimate the return to education and your measure of education is poor, your estimated return will be biased downward.

The intuition connects directly to your knowledge of omitted variable bias. In both cases, something in the error term correlates with your regressor. With measurement error in x, the true regressor x* is part of the composite error (since y = β·x + (ε − β·u)), and x and x* are correlated — creating endogeneity. The bias always goes toward zero for a single regressor, but with multiple regressors, measurement error in one variable can bias coefficients on others in any direction.

**Measurement error in the outcome variable** (y = y* + v) is less damaging: if v is classical measurement error uncorrelated with x, OLS remains consistent, though standard errors increase and precision falls. This asymmetry is important — researchers are often more worried about mismeasured outcomes than they need to be, while underweighting the consequences of mismeasured regressors.

The standard remedy for mismeasured regressors is **instrumental variables**: find an instrument that correlates with the true x* but is uncorrelated with the measurement error u (and with the structural error ε). A second, independent measurement of the same variable often serves as a valid instrument under the classical error assumption, since two independent measures of x* share signal but not measurement noise. The two-stage logic is the same as for standard IV — the instrument purges the endogenous variation introduced by measurement error, recovering a consistent estimate of β.
