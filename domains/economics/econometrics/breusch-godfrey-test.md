---
id: breusch-godfrey-test
title: Breusch-Godfrey Test for Serial Correlation
domain: economics
course: econometrics
prerequisites:
- id: serial-correlation
  type: hard
- id: f-test-joint-significance
  type: hard
builds-toward:
- dynamic-panel-gmm
tags:
- serial-correlation
- testing
- diagnostics
stage: formal-systems
status: draft
---

# Breusch-Godfrey Test for Serial Correlation

## Core Idea
The Breusch-Godfrey test detects serial correlation of any order by regressing residuals on lagged residuals and original regressors, then testing joint significance of the lagged residuals. This extends the Durbin-Watson test to higher-order autocorrelation and higher-order lags, providing a flexible diagnostic tool.
