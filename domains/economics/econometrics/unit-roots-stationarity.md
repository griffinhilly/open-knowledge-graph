---
id: unit-roots-stationarity
title: Unit Roots and Testing for Stationarity
domain: economics
course: econometrics
prerequisites:
- id: time-series-basics-econometrics
  type: hard
- id: chow-test-structural-breaks
  type: soft
- id: characteristic-equation-method
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- autoregressive-ar-models
tags:
- time-series
- unit-roots
- stationarity
stage: formal-systems
status: draft
---

# Unit Roots and Testing for Stationarity

## Core Idea
A time series is stationary if its mean, variance, and autocovariances are time-invariant. A unit root (coefficient on lagged dependent variable equal to 1) induces nonstationarity and persistence. Tests like the Augmented Dickey-Fuller (ADF) and KPSS test detect unit roots; differencing restores stationarity for I(1) series.

## How It's Best Learned
Simulate AR(1) processes with different coefficients (e.g., 0.9 vs 1.0) and observe how unit roots produce very different time path behavior.

## Common Misconceptions
A nearly unit root process (e.g., φ = 0.99) is not the same as a unit root process; small differences have large implications for statistical properties.

## Questions

```yaml
- question: "A researcher says 'φ = 0.99 is practically a unit root — there's no meaningful difference for empirical work.' Why would an econometrician strongly object?"
  type: multiple-choice
  options:
    - "Because φ = 0.99 and φ = 1.0 produce identical statistical properties in finite samples"
    - "Because with φ = 0.99 the series eventually reverts to its mean (shocks decay), while with φ = 1.0 every shock is permanently incorporated into the level — a fundamental qualitative difference in long-run behavior"
    - "Because φ = 0.99 is actually more persistent than φ = 1.0 under certain lag structures"
    - "Because only values of φ greater than 1 create nonstationarity problems in practice"
  answer: 1
  explanation: "The difference between φ = 0.99 and φ = 1.0 is not a small quantitative difference — it is a categorical one. With φ = 0.99, the effect of any shock decays geometrically toward zero; given enough time, the series reverts to its mean. With φ = 1.0, shocks never decay — every ε_t is permanently added to the level of the series, causing it to wander without bound. The first series is stationary with finite variance; the second has variance that grows with t. Standard inference tools (t-tests, OLS) are designed for the stationary case and break down with unit roots."

- question: "Two researchers regress unemployment on sunspot activity over 60 years and find R² = 0.78 and a highly significant slope coefficient. A skeptical colleague suspects spurious regression. What would validate this concern?"
  type: multiple-choice
  options:
    - "The sample size of 60 years is too small to trust OLS results"
    - "Both series are likely nonstationary random walks, so the apparent significance reflects shared trending behavior rather than any true relationship — standard t-statistics are invalid in this setting"
    - "A high R² always indicates a spurious relationship between unrelated variables"
    - "Sunspot activity is a physical measurement and therefore cannot cause spurious correlation with economic variables"
  answer: 1
  explanation: "The spurious regression problem arises when two unrelated random walks are regressed on each other. Both series wander without mean-reversion, so they may trend together or apart by chance over long periods, producing high R² and significant coefficients even when the true relationship is zero. The standard t-statistic does not follow a t-distribution when the regressors are nonstationary, so 'significant' results are unreliable. Testing each series for unit roots first (e.g., with ADF) is the necessary diagnostic step."

- question: "The Augmented Dickey-Fuller (ADF) test uses standard t-distribution critical values, just like a regular t-test for regression coefficients."
  type: true-false
  answer: false
  explanation: "Under the null hypothesis of a unit root, the ADF test statistic does not follow a standard t-distribution. It follows the non-standard Dickey-Fuller distribution, whose critical values are more negative than standard t thresholds. For example, at the 5% significance level, the ADF critical value might be around −2.86, whereas a standard t-test would use roughly −1.96. Using standard t-critical values would lead to over-rejection of the null and false conclusions of stationarity. This is why specialized Dickey-Fuller tables are required."

- question: "First-differencing an I(1) time series (computing Δy_t = y_t − y_{t−1}) removes the unit root and produces a stationary series, making standard regression and AR modeling valid."
  type: true-false
  answer: true
  explanation: "An I(1) series has one unit root: applying the difference operator once removes it, yielding a stationary I(0) series. For a random walk y_t = y_{t−1} + ε_t, the first difference Δy_t = ε_t is simply white noise — stationary by definition. AR models and OLS regression are designed for stationary series, so differencing is the standard preprocessing step when unit roots are detected. If two series are both I(1) and cointegrated, differencing is not always the right approach (cointegration methods may be preferred), but for standard AR modeling of a single series, differencing is correct."

- question: "Explain why regressing one random walk on another unrelated random walk frequently produces high R² and statistically significant coefficients. What property of unit root processes causes this problem?"
  type: short-answer
  answer: "In a unit root process (random walk), shocks accumulate permanently — the series wanders without returning to a mean, and its variance grows over time. Two unrelated random walks can drift in the same direction for extended periods purely by chance, creating the appearance of correlation. The OLS estimator picks up this shared trending behavior and yields large R² and significant-looking t-statistics. But the t-statistics don't follow the t-distribution in this setting, so those significance levels are meaningless. The fix is to test for unit roots before modeling and to difference to stationarity (or use cointegration methods if the series are cointegrated)."
  explanation: "The core issue is that OLS assumes the regression errors are stationary and well-behaved. When both variables are I(1), the residuals may also be I(1) — trending and non-mean-reverting — which violates OLS assumptions and inflates apparent fit. Granger and Newbold (1974) demonstrated this problem in simulations, showing that two entirely independent random walks could produce R² near 1 and t-statistics in the hundreds. This result motivated the entire field of cointegration analysis."
```

## Explainer

Think back to what makes a time series useful for standard inference: you need the statistical properties of the series to be stable over time. If the mean, variance, and autocorrelations all stay the same regardless of when you sample, the series is **stationary**, and the familiar tools of regression and hypothesis testing apply. If those properties drift — the mean trends upward, the variance grows, or the autocovariances depend on where you are in time — the series is **nonstationary**, and standard inference breaks down in subtle and serious ways.

The most important source of nonstationarity in economic data is the **unit root**. Consider the simplest case: an AR(1) process yₜ = φyₜ₋₁ + εₜ. If |φ| < 1, the effect of a shock to y dies away over time — the series reverts toward its mean and is stationary. If φ = 1 exactly, shocks never die away; every εₜ is permanently incorporated into the level of the series. This is a **random walk**: yₜ = yₜ₋₁ + εₜ, the most common unit root process. GDP, stock prices, and interest rates often behave this way — a shock today shifts the entire future path of the series, not just the next few periods. The crucial distinction between φ = 0.99 and φ = 1.0 seems numerically small but is statistically enormous: the first eventually reverts, the second never does.

Running a regression between two unrelated random walk series produces the **spurious regression** problem: you'll find high R² and significant t-statistics even though there is no true relationship. This is why testing for unit roots before modeling is essential. The **Augmented Dickey-Fuller (ADF) test** is the standard tool. It tests the null hypothesis that a unit root is present (φ = 1) against the alternative of stationarity (|φ| < 1). A key quirk: the test statistic does not follow a standard t-distribution under the null, so you must use Dickey-Fuller critical values, which are more negative than standard thresholds. Failing to reject the null means the series likely has a unit root.

The **KPSS test** takes the opposite approach: it tests the null of stationarity against the alternative of a unit root. Using ADF and KPSS together is good practice — if ADF fails to reject and KPSS rejects, both tests point to a unit root. When a series has a unit root, the standard remedy is **differencing**: taking first differences Δyₜ = yₜ - yₜ₋₁ removes one unit root. If a series requires one difference to become stationary, it is called **integrated of order 1**, or I(1); requiring two differences gives I(2), and so on. Once differenced to stationarity, you can apply AR models and standard regression — which is exactly where the next topic, AR models, begins.
