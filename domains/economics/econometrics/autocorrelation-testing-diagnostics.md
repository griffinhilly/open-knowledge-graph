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
- id: durbin-watson-statistic
  type: soft
tags:
- autocorrelation
- durbin-watson
- breusch-godfrey
stage: advanced
status: validated
---
# Testing for Autocorrelation: Durbin-Watson and Breusch-Godfrey

## Core Idea
The Durbin-Watson statistic tests for first-order serial correlation in residuals (DW ≈ 2 means no correlation). The Breusch-Godfrey LM test is more general, testing for higher-order autocorrelation and valid when lags of X are present.

## How It's Best Learned
Compute DW or run the BG test on residuals from OLS regression. Plot residuals over time to visually detect serial correlation before relying on formal tests.

## Questions

```yaml
- question: "A researcher runs OLS on time-series data and finds a Durbin-Watson statistic of 0.8, indicating positive serial correlation. What is the PRIMARY consequence for the regression results?"
  type: multiple-choice
  options:
    - "The coefficient estimates are biased and inconsistent, making them unreliable"
    - "The coefficient estimates are unbiased, but the standard errors are unreliable so t-statistics and p-values are invalid"
    - "The regression has omitted variable bias due to the correlated residuals"
    - "The model will systematically underfit the data by ignoring temporal patterns"
  answer: 1
  explanation: "Autocorrelation does NOT bias OLS coefficient estimates (under standard conditions). The coefficients remain unbiased and consistent. The real damage is to inference: OLS underestimates standard errors when residuals are positively correlated, inflating t-statistics and making results appear more significant than they are. Option A is the most common misconception — conflating 'wrong standard errors' with 'biased estimates.'"

- question: "A researcher estimates a distributed lag model that includes a lagged dependent variable (Yₜ₋₁) as a regressor. They want to test for autocorrelation in the residuals. Which test should they use and why?"
  type: multiple-choice
  options:
    - "Durbin-Watson, because it is the standard and most widely used autocorrelation test"
    - "Durbin-Watson with a correction factor to account for the lagged dependent variable"
    - "Breusch-Godfrey LM test, because Durbin-Watson is invalid when lagged dependent variables appear as regressors"
    - "Neither test — autocorrelation cannot be detected when lagged dependent variables are present"
  answer: 2
  explanation: "The Durbin-Watson statistic is derived under the assumption that regressors are strictly exogenous. When a lagged dependent variable appears on the right-hand side, this assumption fails, and the DW statistic is biased toward 2, making it unreliable. The Breusch-Godfrey LM test does not rely on this assumption and remains valid with lagged dependent variables. It also tests for higher-order autocorrelation, not just first-order."

- question: "A Durbin-Watson statistic close to 2 indicates no first-order autocorrelation in the residuals."
  type: true-false
  answer: true
  explanation: "The DW statistic approximately equals 2(1 − r̂), where r̂ is the first-order autocorrelation of the residuals. When r̂ ≈ 0 (no autocorrelation), DW ≈ 2. Values near 0 indicate strong positive autocorrelation; values near 4 indicate strong negative autocorrelation. Note that DW only tests for first-order autocorrelation and has an inconclusive range between the lower and upper critical bounds."

- question: "Positive autocorrelation in OLS residuals typically biases the estimated regression coefficients away from zero."
  type: true-false
  answer: false
  explanation: "This is a key misconception. Under standard conditions, autocorrelation in residuals does not bias or invalidate the OLS coefficient estimates — they remain unbiased and consistent. The problem lies exclusively with inference: the estimated standard errors are too small (positive autocorrelation understates variance), so t-statistics are inflated and confidence intervals are too narrow. The coefficients themselves point in the right direction; the problem is that you overstate your certainty about them."

- question: "Why does autocorrelation in OLS residuals cause problems for hypothesis testing even when the coefficient estimates remain unbiased?"
  type: short-answer
  answer: "OLS standard errors assume residuals are uncorrelated. When residuals are positively autocorrelated, consecutive observations carry redundant information — the effective sample size is smaller than the nominal n. OLS ignores this and treats all n observations as independent, producing standard errors that are too small. Artificially small standard errors yield inflated t-statistics, leading to false rejections of true null hypotheses (type I errors). The coefficient point estimates are still correct on average, but their apparent precision is overstated."
  explanation: "Think of it this way: if your residuals follow a trend (positive autocorrelation), you are not getting n independent pieces of information — you are getting something closer to n/k independent pieces, where k is the effective autocorrelation length. OLS does not know this and divides by n, not n/k, when estimating variance. The remedy is to use HAC (heteroskedasticity and autocorrelation consistent) standard errors, such as Newey-West, which correct for both the correlation and its magnitude."
```

## Explainer

You already know from serial correlation that when regression residuals are systematically related across time periods — positive errors following positive errors, or negative following negative — the OLS standard errors are wrong. The question this topic answers is: how do you actually detect that problem in practice? The answer involves two complementary tests, each suited to different situations.

The **Durbin-Watson statistic** is the older and more famous test. After running an OLS regression, compute the DW statistic from the residuals: it roughly equals 2(1 − r̂), where r̂ is the first-order autocorrelation of the residuals. This means a DW near 2 signals no first-order autocorrelation, a value near 0 signals strong positive autocorrelation (residuals moving together), and a value near 4 signals strong negative autocorrelation (residuals alternating in sign). The test has an inconclusive zone — if DW falls between the lower and upper critical bounds, the test is indeterminate, which can be frustrating in practice. It is also limited to first-order autocorrelation and fails when lagged dependent variables appear as regressors.

The **Breusch-Godfrey LM test** is more flexible. It tests for autocorrelation up to any order you specify, and it remains valid when lagged dependent variables appear on the right-hand side — a common situation in time-series regression. The procedure is simple: regress the residuals on all original regressors plus p lags of the residuals, then use the resulting R² to form an LM statistic (n × R²), which follows a chi-squared distribution with p degrees of freedom under the null of no autocorrelation. If the statistic is large enough to reject the null, you have evidence of autocorrelation up to order p.

In practice, always start with a visual inspection: plot the residuals against time and look for patterns. Systematic runs of same-sign residuals are the fingerprint of positive autocorrelation. If you see it visually, the formal tests will almost certainly confirm it. The more important question is what to do next: autocorrelation doesn't mean your coefficient estimates are biased (they usually aren't), but it does mean your standard errors and t-statistics are unreliable. The remedies — using HAC (Newey-West) standard errors, or fitting GLS/FGLS — depend on diagnosing not just whether autocorrelation is present, but what form it takes.

## Common Misconceptions
- Autocorrelation biases coefficient estimates — it does not (under standard conditions); the problem is with inference, not point estimates.
- The Durbin-Watson test works in all settings — it does not when lagged dependent variables are included; use Breusch-Godfrey instead.
