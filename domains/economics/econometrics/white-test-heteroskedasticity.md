---
id: white-test-heteroskedasticity
title: White Test and Detection of Heteroskedasticity
domain: economics
course: econometrics
prerequisites:
- id: heteroskedasticity
  type: hard
- id: f-test-joint-significance
  type: hard
builds-toward:
- generalized-least-squares
tags:
- heteroskedasticity
- testing
- diagnostics
stage: formal-systems
status: draft
---

# White Test and Detection of Heteroskedasticity

## Core Idea
White's test detects heteroskedasticity by regressing squared residuals on all regressors and their interactions, testing whether these variables explain squared residuals. Unlike Breusch-Pagan, it is robust to specific forms of heteroskedasticity, making it practical for applied work when the source of heteroskedasticity is unknown.
