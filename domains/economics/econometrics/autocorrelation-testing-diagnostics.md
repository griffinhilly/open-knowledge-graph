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

## Explainer

You already know from serial correlation that when regression residuals are systematically related across time periods — positive errors following positive errors, or negative following negative — the OLS standard errors are wrong. The question this topic answers is: how do you actually detect that problem in practice? The answer involves two complementary tests, each suited to different situations.

The **Durbin-Watson statistic** is the older and more famous test. After running an OLS regression, compute the DW statistic from the residuals: it roughly equals 2(1 − r̂), where r̂ is the first-order autocorrelation of the residuals. This means a DW near 2 signals no first-order autocorrelation, a value near 0 signals strong positive autocorrelation (residuals moving together), and a value near 4 signals strong negative autocorrelation (residuals alternating in sign). The test has an inconclusive zone — if DW falls between the lower and upper critical bounds, the test is indeterminate, which can be frustrating in practice. It is also limited to first-order autocorrelation and fails when lagged dependent variables appear as regressors.

The **Breusch-Godfrey LM test** is more flexible. It tests for autocorrelation up to any order you specify, and it remains valid when lagged dependent variables appear on the right-hand side — a common situation in time-series regression. The procedure is simple: regress the residuals on all original regressors plus p lags of the residuals, then use the resulting R² to form an LM statistic (n × R²), which follows a chi-squared distribution with p degrees of freedom under the null of no autocorrelation. If the statistic is large enough to reject the null, you have evidence of autocorrelation up to order p.

In practice, always start with a visual inspection: plot the residuals against time and look for patterns. Systematic runs of same-sign residuals are the fingerprint of positive autocorrelation. If you see it visually, the formal tests will almost certainly confirm it. The more important question is what to do next: autocorrelation doesn't mean your coefficient estimates are biased (they usually aren't), but it does mean your standard errors and t-statistics are unreliable. The remedies — using HAC (Newey-West) standard errors, or fitting GLS/FGLS — depend on diagnosing not just whether autocorrelation is present, but what form it takes.

## Common Misconceptions
- Autocorrelation biases coefficient estimates — it does not (under standard conditions); the problem is with inference, not point estimates.
- The Durbin-Watson test works in all settings — it does not when lagged dependent variables are included; use Breusch-Godfrey instead.
