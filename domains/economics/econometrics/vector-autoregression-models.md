---
id: vector-autoregression-models
title: Vector Autoregression (VAR) Models and Impulse Responses
domain: economics
course: econometrics
prerequisites:
- id: autoregressive-ar-models
  type: hard
- id: dynamic-panel-gmm
  type: soft
builds-toward:
- regression-discontinuity
tags:
- time-series
- var
- multivariate
stage: formal-systems
status: draft
---

# Vector Autoregression (VAR) Models and Impulse Responses

## Core Idea
A VAR(p) model extends AR to multiple series where each variable depends on its own and all other variables' lags. VARs capture dynamic cross-variable relationships without imposing strong identifying assumptions. Impulse responses show shock propagation; forecast error variance decomposition quantifies each variable's contribution to forecast error in others.
