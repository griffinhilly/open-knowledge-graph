---
id: time-series-cross-section
title: Time Series Cross-Section (TSCS) Models
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: longitudinal-data-analysis
  type: hard
- id: time-series-social-phenomena
  type: hard
builds-toward:
- vector-autoregression-var
- dynamic-panel-models
tags:
- panel-time-series
- comparative
- countries-regions
- dynamics
stage: advanced
status: draft
---

# Time Series Cross-Section (TSCS) Models

## Core Idea
TSCS data combines the temporal dimension (many time periods) with the cross-sectional dimension (many units like countries or organizations), creating a grid of observations. TSCS models account for complex dependence structures: within-unit autocorrelation, contemporaneous correlation across units, and panel-specific heteroskedasticity. These methods are essential in comparative political economy, international relations, and organizational research where panel length and breadth are both substantial.

## Explainer

You arrive here having studied both longitudinal data and time series analysis separately. TSCS data is what you get when both dimensions are large and neither can be ignored: imagine a dataset of 20 countries observed annually from 1970 to 2020. This is not simply repeated cross-sections (too much temporal structure to ignore) nor is it a pure time series (too many units to treat as a single sequence). The TSCS structure demands methods that respect both dimensions simultaneously.

The defining challenge of TSCS data is **error dependence** along three axes. First, **serial autocorrelation**: observations for the same country in year *t* and year *t-1* are not independent — past GDP growth predicts current growth, past conflict predicts current conflict. Ignoring this produces artificially small standard errors and overconfident inference. Second, **contemporaneous cross-unit correlation** (also called spatial dependence): a global recession hits all countries at once; a regional contagion spreads simultaneously. Units observed in the same period tend to co-move in ways unrelated to the covariates. Third, **panel heteroskedasticity**: the variance of the error differs across units — large economies simply have larger absolute shocks than small ones. The standard TSCS estimation procedure, using **panel-corrected standard errors (PCSEs)**, addresses all three of these problems in a principled way.

The substantive modeling choices in TSCS involve how to handle the dynamics of the dependent variable. A **lagged dependent variable (LDV)** model includes the prior period's outcome as a predictor, absorbing much of the serial dependence and allowing coefficients on other variables to be interpreted as effects net of prior state. Fixed effects models — adding unit dummies — control for all time-invariant unit characteristics, which is powerful for causal identification but at the cost of discarding between-unit variation entirely. The **error correction model (ECM)** framework is particularly appropriate when theory distinguishes short-run dynamics from long-run equilibrium: it models how units adjust toward their equilibrium level over time and allows you to separately estimate immediate and cumulative effects of a shock.

A distinctive concern in TSCS analysis is the **unit of analysis**: are you treating countries as the units, or are country-years the units? This choice shapes what "clustering" the errors means. Clustering standard errors at the country level accounts for the fact that all observations within a country are correlated across time — it is almost always appropriate. A second concern is **causal direction and simultaneity**: in a TSCS dataset studying whether trade openness causes economic growth, growth also affects trade openness, creating simultaneity bias. This is where TSCS analysis intersects with the broader causal inference toolkit — lagged variables, natural experiments, and IV methods all get deployed within TSCS frameworks.

The payoff to mastering TSCS methods is access to the richest datasets in comparative social science. Most of what we know empirically about long-run development, democratization, welfare state expansion, and interstate conflict comes from TSCS analysis. The methods let you leverage both the variation across countries (comparative leverage) and the variation within countries over time (longitudinal leverage), and carefully specified models can distinguish country-specific trajectories from common global trends — which is, in the end, what most big questions in comparative social science are asking.
