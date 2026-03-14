---
id: chow-test-structural-breaks
title: Chow Test and Detection of Structural Breaks
domain: economics
course: econometrics
prerequisites:
- id: f-test-joint-significance
  type: hard
- id: time-series-basics-econometrics
  type: soft
builds-toward:
- unit-roots-stationarity
tags:
- structural-breaks
- testing
- time-series
stage: formal-systems
status: draft
---

# Chow Test and Detection of Structural Breaks

## Core Idea
The Chow test detects whether regression coefficients differ across two subperiods by comparing the sum of squared residuals from pooled versus separate regressions for each period. When the break date is unknown, CUSUM and Quandt-Andrews tests search across possible dates to identify break points.
