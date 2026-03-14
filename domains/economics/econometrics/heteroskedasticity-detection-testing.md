---
id: heteroskedasticity-detection-testing
title: Testing for Heteroskedasticity
domain: economics
course: econometrics
prerequisites:
- id: heteroskedasticity
  type: hard
- id: heteroskedasticity-types-causes
  type: hard
builds-toward:
- robust-standard-errors
tags:
- heteroskedasticity
- testing
- diagnostics
stage: formal-systems
status: draft
---

# Testing for Heteroskedasticity

## Core Idea
Tests for heteroskedasticity include: residual scatter plots vs fitted values, Breusch-Pagan regression of squared residuals on X, and White's test using fitted values and squares. Each detects dependence of error variance on regressors; rejection indicates correction is needed.
