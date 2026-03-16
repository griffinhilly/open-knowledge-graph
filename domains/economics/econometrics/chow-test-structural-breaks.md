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

## Explainer

You already know the F-test from joint significance testing: you compare a restricted model (where some coefficients are forced to zero) against an unrestricted model (where they're free), and use the ratio of improvement in fit to the cost in degrees of freedom. The **Chow test** is exactly this logic applied to a different kind of restriction — the restriction that your regression coefficients are the same in two different time periods (or subgroups).

Suppose you're modeling the relationship between unemployment and GDP growth, but you suspect the relationship changed after a major recession. The restricted model pools all data and estimates one set of coefficients. The unrestricted model estimates separate regressions for each period. The Chow test computes: how much better does fitting two regressions do versus one? If the improvement in RSS (reduction in squared residuals) is large relative to the extra parameters used, you reject the null hypothesis that the coefficients are stable — you've found a **structural break**.

The catch is that the classic Chow test requires you to nominate the break date in advance. This is often unrealistic. If you're allowed to search across all possible break dates, you'd always find *some* date where the split looks significant, even in stable data — this is the data-snooping problem. The **Quandt-Andrews test** handles this by computing a Chow-like statistic at every candidate break date and taking the maximum, then comparing it against a non-standard critical value that accounts for the search. The **CUSUM test** takes a different approach: it tracks the cumulative sum of recursive residuals over time and flags a break when the cumulative sum drifts outside a confidence band — a visual and formal method that shows *when* instability begins rather than just whether it exists.

Understanding structural breaks matters beyond methodology. A model that ignores a break will produce biased coefficient estimates because it averages over two different regimes. If your forecast period is in a different regime than your estimation sample, predictions will be systematically wrong. The tools here — testing for instability, identifying when it occurred, and splitting the sample accordingly — are foundational steps in building time series models that are actually reliable out-of-sample.
