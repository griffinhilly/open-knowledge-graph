---
id: reduced-form-equations
title: Reduced Form and First-Stage Equations
domain: economics
course: econometrics
prerequisites:
- id: two-stage-least-squares-procedure
  type: hard
builds-toward:
- overidentification-test
tags:
- instrumental-variables
- reduced-form
- first-stage
stage: formal-systems
status: draft
---

# Reduced Form and First-Stage Equations

## Core Idea
The first-stage equation (X regressed on Z) is the reduced form for X, showing how exogenous variation in Z translates to variation in the endogenous X. Weak first-stage (low R² or t-statistics) indicates weak instruments; guidance suggests F-statistic > 10 for instrument strength diagnostics.
