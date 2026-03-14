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
