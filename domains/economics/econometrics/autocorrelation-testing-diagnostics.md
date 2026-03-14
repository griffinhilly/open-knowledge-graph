---
id: autocorrelation-testing-diagnostics
title: 'Testing for Autocorrelation: Durbin-Watson and Breusch-Godfrey'
domain: economics
course: econometrics
prerequisites:
- id: time-series-basics-econometrics
  type: hard
- id: serial-correlation
  type: hard
tags:
- autocorrelation
- durbin-watson
- breusch-godfrey
stage: formal-systems
status: draft
---

# Testing for Autocorrelation: Durbin-Watson and Breusch-Godfrey

## Core Idea
The Durbin-Watson statistic tests for first-order serial correlation in residuals (DW ≈ 2 means no correlation). The Breusch-Godfrey LM test is more general, testing for higher-order autocorrelation and valid when lags of X are present.

## How It's Best Learned
Compute DW or run the BG test on residuals from OLS regression. Plot residuals over time to visually detect serial correlation before relying on formal tests.
