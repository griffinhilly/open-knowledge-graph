---
id: durbin-watson-statistic
title: Durbin-Watson Statistic for Autocorrelation
domain: economics
course: econometrics
prerequisites:
- id: autocorrelation-lag-structure
  type: hard
builds-toward:
- breusch-godfrey-test
tags:
- autocorrelation
- diagnostics
- testing
stage: formal-systems
status: draft
---

# Durbin-Watson Statistic for Autocorrelation

## Core Idea
The Durbin-Watson statistic DW = Σ(ûₜ - ûₜ₋₁)² / Σûₜ² approximates 2(1 - ρ̂) where ρ̂ is the first-order autocorrelation. Values near 2 suggest no autocorr, < 2 suggests positive autocorr, and > 2 suggests negative autocorr, providing a quick diagnostic.
