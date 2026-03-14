---
id: dynamic-panel-gmm
title: Dynamic Panel Models and System GMM Estimation
domain: economics
course: econometrics
prerequisites:
- id: hausman-specification-test
  type: hard
- id: instrumental-variables
  type: hard
builds-toward:
- vector-autoregression-models
tags:
- panel-data
- dynamic
- gmm
stage: formal-systems
status: draft
---

# Dynamic Panel Models and System GMM Estimation

## Core Idea
Dynamic panels include lagged dependent variables, which correlate with fixed effects, violating strict exogeneity. Arellano-Bond and Blundell-Bond GMM estimators use internal instruments (lags of dependent variable and regressors) for consistent estimation. Arellano-Bond (difference GMM) assumes mean stationarity; Blundell-Bond (system GMM) relaxes this.
