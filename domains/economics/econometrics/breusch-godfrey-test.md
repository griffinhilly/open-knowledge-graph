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
stage: formal-systems
status: draft
---

# Breusch-Godfrey Test for Serial Correlation

## Core Idea
The Breusch-Godfrey test detects serial correlation of any order by regressing residuals on lagged residuals and original regressors, then testing joint significance of the lagged residuals. This extends the Durbin-Watson test to higher-order autocorrelation and higher-order lags, providing a flexible diagnostic tool.

## Explainer

You already know from your study of serial correlation that OLS residuals becoming predictable from their own past is a serious diagnostic problem — it means the error terms are not independent draws, which inflates standard errors and distorts inference. The Durbin-Watson test you may have encountered handles the simplest case: AR(1) serial correlation, where each residual correlates only with the one immediately before it. But economic time series often carry memory across multiple periods. A shock today may reverberate for three or four quarters. The **Breusch-Godfrey test** is designed to catch exactly that.

The procedure starts from your estimated OLS residuals — the leftover variation your model couldn't explain. The key insight is that if those residuals carry genuine serial structure, they should be predictable from their own lags. So the test runs an **auxiliary regression**: regress the residuals ê_t on the original regressors from your main model plus p lagged residuals (ê_{t-1}, ê_{t-2}, ..., ê_{t-p}). The original regressors are included to remove any mechanical correlation induced by lagged dependent variables that may appear in the main equation — this is why Breusch-Godfrey improves on Durbin-Watson, which is invalid in that setting.

The test statistic follows from your F-test prerequisite. The null hypothesis H₀ is that all p lagged residual coefficients are jointly zero — meaning no serial correlation up to order p. You compute the F-statistic (or equivalently, n times the R² of the auxiliary regression, which is asymptotically χ²(p)) and compare to the critical value. **Rejection** means at least one lag carries predictive power, confirming serial correlation. Failure to reject suggests the residuals are approximately white noise up to the order you tested.

Choosing p requires judgment. A natural starting point is the data frequency: quarterly data might suggest testing up to order 4 (one year of lags), annual data up to 2 or 3. Testing too few lags misses high-order autocorrelation; testing too many burns degrees of freedom unnecessarily. Many practitioners run the test at multiple values of p and look for consistency. When serial correlation is detected, the appropriate remedy depends on its source: if it reflects a misspecified dynamic model, add lags of the dependent variable; if it reflects pure disturbance autocorrelation, switch to Newey-West heteroskedasticity-and-autocorrelation-consistent (HAC) standard errors rather than refitting the conditional mean.
