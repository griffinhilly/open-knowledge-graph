---
id: feasible-generalized-least-squares-fgls
title: Feasible GLS (FGLS) with Estimated Covariance Structure
domain: economics
course: econometrics
prerequisites:
- id: generalized-least-squares
  type: hard
builds-toward:
- dynamic-panel-gmm
tags:
- estimation
- heteroskedasticity
- fgls
stage: formal-systems
status: draft
---

# Feasible GLS (FGLS) with Estimated Covariance Structure

## Core Idea
FGLS estimates the error covariance matrix from residuals, then applies GLS using the estimated structure. While more practical than GLS (which requires knowing covariance a priori), FGLS is sensitive to misspecification of the covariance form and sacrifices some efficiency through the two-step estimation.
