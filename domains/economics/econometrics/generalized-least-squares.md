---
id: generalized-least-squares
title: Generalized Least Squares (GLS) for Non-Spherical Errors
domain: economics
course: econometrics
prerequisites:
- id: white-test-heteroskedasticity
  type: hard
- id: ols-assumptions
  type: hard
- id: linear-algebra
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- feasible-generalized-least-squares-fgls
tags:
- estimation
- heteroskedasticity
- gls
stage: formal-systems
status: draft
---

# Generalized Least Squares (GLS) for Non-Spherical Errors

## Core Idea
GLS transforms the regression by the inverse of the error variance-covariance matrix, restoring efficiency when errors are heteroskedastic or serially correlated. When the covariance structure is known, GLS recovers BLUE properties; when unknown and must be estimated from residuals, the procedure is feasible GLS (FGLS).
