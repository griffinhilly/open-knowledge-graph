---
id: dynamic-panel-models
title: Dynamic Panel Models and Arellano-Bond/Blundell-Bond Estimation
domain: economics
course: econometrics
prerequisites:
- id: panel-data-basics
  type: hard
- id: fixed-effects-models
  type: hard
- id: instrumental-variables
  type: hard
tags:
- dynamic-panel
- gmm
- arellano-bond
stage: formal-systems
status: draft
---

# Dynamic Panel Models and Arellano-Bond/Blundell-Bond Estimation

## Core Idea
When the lagged dependent variable appears as a regressor in panel data, standard estimators are inconsistent. GMM methods (Arellano-Bond, Blundell-Bond) use internal instruments from lags of the dependent variable to achieve consistency.

## Explainer

You have already encountered **fixed effects** estimation, which controls for unobserved time-invariant characteristics of each unit by within-transforming the data — subtracting each unit's mean from its observations. This works well when the regressors are strictly exogenous: past, present, and future values of the explanatory variable are uncorrelated with the error term. The trouble begins the moment you include the **lagged dependent variable** (y_{i,t-1}) on the right-hand side, which is exactly what you want to do whenever this period's outcome depends on last period's outcome — wages, GDP growth, firm investment, and countless other economic quantities.

The problem is subtle but fatal. The within-transformation to remove fixed effects requires subtracting each unit's mean of y. But that mean includes y_{i,t-1}, which is the variable you are trying to use as a regressor. Because y_{i,t-1} and the demeaned error share the same unit mean, they are correlated — the **Nickell bias**. The fixed effects estimator is inconsistent in dynamic panels even as N grows large (the bias is of order 1/T, so it only vanishes if T is large, which it often is not). The first instinct — first-differencing to eliminate fixed effects — removes the individual effect but creates a different problem: the first-differenced lagged dependent variable (Δy_{i,t-1} = y_{i,t-1} - y_{i,t-2}) is correlated with the first-differenced error (Δε_{i,t} = ε_{i,t} - ε_{i,t-1}) because both share ε_{i,t-1}. You have escaped one form of endogeneity only to create another.

**Arellano-Bond estimation** solves this by returning to your prerequisite: instrumental variables. After first-differencing to remove fixed effects, you need instruments for Δy_{i,t-1} that are correlated with it but uncorrelated with Δε_{i,t}. The insight is that further lags of y — specifically y_{i,t-2}, y_{i,t-3}, and so on — are valid instruments. They are correlated with Δy_{i,t-1} (because y_{i,t-1} depends on its own history) but not with ε_{i,t} or ε_{i,t-1} (assuming the original errors are serially uncorrelated). Each additional time period makes more instruments available, and the estimator combines them all efficiently using **Generalized Method of Moments (GMM)**. This is the "difference GMM" approach of Arellano and Bond.

**Blundell-Bond (system GMM)** extends this by noting that lagged levels can be weak instruments for first differences when the series is highly persistent. Their fix is to stack two equation systems: the first-differenced equation (using lagged levels as instruments, as in Arellano-Bond) and the levels equation (using lagged differences as instruments). The combined system GMM estimator is more efficient when the instrument relevance of lagged levels is weak. In practice, the key diagnostic is the **Sargan/Hansen test** for instrument validity (over-identification test) and **Arellano-Bond tests** for second-order serial correlation in the residuals — if serial correlation exists at order 2, the instruments derived from t-2 lags are contaminated. Running a dynamic panel model means always reporting these tests alongside your estimates.
