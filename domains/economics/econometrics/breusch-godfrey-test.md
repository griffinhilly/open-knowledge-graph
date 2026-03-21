---
id: breusch-godfrey-test
title: Breusch-Godfrey Test for Serial Correlation
domain: economics
course: econometrics
prerequisites:
- id: serial-correlation
  type: hard
- id: f-test-joint-significance
  type: hard
builds-toward:
- dynamic-panel-gmm
tags:
- serial-correlation
- testing
- diagnostics
stage: advanced
status: draft
---

# Breusch-Godfrey Test for Serial Correlation

## Core Idea
The Breusch-Godfrey test detects serial correlation of any order by regressing residuals on lagged residuals and original regressors, then testing joint significance of the lagged residuals. This extends the Durbin-Watson test to higher-order autocorrelation and higher-order lags, providing a flexible diagnostic tool.

## Questions

```yaml
- question: "The Breusch-Godfrey auxiliary regression regresses residuals on lagged residuals AND the original model's regressors. Why are the original regressors included?"
  type: multiple-choice
  options:
    - "To increase the R² of the auxiliary regression and make the test more powerful"
    - "To remove mechanical correlation induced when the main model contains a lagged dependent variable, making the test valid in that setting"
    - "Because the original regressors serve as instrumental variables for the lagged residuals"
    - "To ensure the auxiliary regression has the same degrees of freedom as the main model"
  answer: 1
  explanation: "This is the key design feature that makes Breusch-Godfrey superior to Durbin-Watson. When the main model includes a lagged dependent variable (e.g., y_{t-1} as a regressor), the Durbin-Watson test is invalid because the residuals are mechanically correlated with this regressor. Including the original regressors in the auxiliary regression purges this mechanical dependence, allowing the test statistic to correctly reflect genuine serial correlation in the disturbances. Without this inclusion, the test would be biased in exactly the cases where serial correlation testing is most needed."

- question: "A researcher runs the Durbin-Watson test on a quarterly time series model and fails to reject no serial correlation. They then run Breusch-Godfrey with p=4 and reject. What does this tell us?"
  type: multiple-choice
  options:
    - "The Breusch-Godfrey test is producing a false positive because DW already confirmed no serial correlation"
    - "The model likely has higher-order serial correlation (beyond lag 1) that DW cannot detect"
    - "The model must contain a lagged dependent variable, which invalidates both tests"
    - "Four lags is too many — reducing p would likely also fail to reject"
  answer: 1
  explanation: "Durbin-Watson only tests for AR(1) serial correlation — correlation between adjacent residuals. Quarterly economic data often carries memory across multiple periods (a shock in Q1 may still affect residuals in Q4). BG with p=4 tests whether any of the first four lags carry predictive power. Failing DW but rejecting BG at p=4 is exactly the scenario BG was designed to catch: higher-order autocorrelation invisible to DW. This doesn't indicate a false positive; it reveals DW's fundamental limitation."

- question: "The Breusch-Godfrey test can detect serial correlation at multiple lags simultaneously, unlike the Durbin-Watson test which is restricted to first-order autocorrelation."
  type: true-false
  answer: true
  explanation: "Correct. By including p lagged residuals in the auxiliary regression and testing their joint significance, BG detects any autocorrelation structure up to order p. The choice of p is a judgment call based on data frequency and prior expectations. DW, by contrast, produces a single statistic targeting AR(1) and has well-known failure modes (inconclusive zones, invalidity with lagged regressors). This flexibility is the primary practical advantage of BG over DW."

- question: "The Breusch-Godfrey test is invalid when the original model includes a lagged dependent variable as a regressor."
  type: true-false
  answer: false
  explanation: "This is precisely backwards — it describes the Durbin-Watson test's limitation, not BG's. The Durbin-Watson test IS invalid with lagged dependent variables because the test statistic is biased toward 2 (no serial correlation) in that setting. The Breusch-Godfrey test was specifically designed to handle this case by including the original regressors in the auxiliary regression, removing the mechanical correlation that invalidates DW. BG is the recommended diagnostic precisely when lagged dependent variables are present."

- question: "What does rejecting the null hypothesis in a Breusch-Godfrey test tell you, and what are the two main remedies depending on the likely source of the serial correlation?"
  type: short-answer
  answer: "Rejection means at least one of the p lagged residual coefficients is significantly different from zero — the residuals carry predictable autocorrelation structure. The source diagnosis determines the remedy: if serial correlation reflects dynamic misspecification (the model's conditional mean is wrong), add lags of the dependent variable to the main equation. If it reflects pure disturbance autocorrelation (the DGP genuinely has correlated errors), use Newey-West HAC standard errors to produce valid inference without changing the point estimates."
  explanation: "The distinction between a misspecified model and a correctly specified model with autocorrelated errors is crucial. Adding lags fixes the former by capturing dynamics erroneously left in the residuals. HAC standard errors fix inference for the latter without altering point estimates. Applying the wrong remedy — HAC when the true problem is omitted dynamics — produces consistent but potentially inefficient estimates and leaves the misspecification in place."
```

## Explainer

You already know from your study of serial correlation that OLS residuals becoming predictable from their own past is a serious diagnostic problem — it means the error terms are not independent draws, which inflates standard errors and distorts inference. The Durbin-Watson test you may have encountered handles the simplest case: AR(1) serial correlation, where each residual correlates only with the one immediately before it. But economic time series often carry memory across multiple periods. A shock today may reverberate for three or four quarters. The **Breusch-Godfrey test** is designed to catch exactly that.

The procedure starts from your estimated OLS residuals — the leftover variation your model couldn't explain. The key insight is that if those residuals carry genuine serial structure, they should be predictable from their own lags. So the test runs an **auxiliary regression**: regress the residuals ê_t on the original regressors from your main model plus p lagged residuals (ê_{t-1}, ê_{t-2}, ..., ê_{t-p}). The original regressors are included to remove any mechanical correlation induced by lagged dependent variables that may appear in the main equation — this is why Breusch-Godfrey improves on Durbin-Watson, which is invalid in that setting.

The test statistic follows from your F-test prerequisite. The null hypothesis H₀ is that all p lagged residual coefficients are jointly zero — meaning no serial correlation up to order p. You compute the F-statistic (or equivalently, n times the R² of the auxiliary regression, which is asymptotically χ²(p)) and compare to the critical value. **Rejection** means at least one lag carries predictive power, confirming serial correlation. Failure to reject suggests the residuals are approximately white noise up to the order you tested.

Choosing p requires judgment. A natural starting point is the data frequency: quarterly data might suggest testing up to order 4 (one year of lags), annual data up to 2 or 3. Testing too few lags misses high-order autocorrelation; testing too many burns degrees of freedom unnecessarily. Many practitioners run the test at multiple values of p and look for consistency. When serial correlation is detected, the appropriate remedy depends on its source: if it reflects a misspecified dynamic model, add lags of the dependent variable; if it reflects pure disturbance autocorrelation, switch to Newey-West heteroskedasticity-and-autocorrelation-consistent (HAC) standard errors rather than refitting the conditional mean.
