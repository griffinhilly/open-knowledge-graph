---
id: time-series-social-phenomena
title: Time Series Analysis of Social Phenomena
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: sequences-and-series-review
  type: hard
- id: functions-domain-codomain-range
  type: soft
- id: differential-equations-intro
  type: soft
tags:
- time-series
- autocorrelation
- stationarity
- policy-evaluation
stage: advanced
status: draft
---

# Time Series Analysis of Social Phenomena

## Core Idea
Extends regression methods to analyze temporal social data with autocorrelation. Covers autoregressive models, moving averages, testing for stationarity, and interrupted time series designs for evaluating policy interventions. Addresses challenges of serial correlation in social data.

## How It's Best Learned
Analyze aggregate time series data (crime, unemployment, attitudes), test for stationarity and autocorrelation, estimate ARIMA models, design interrupted time series to evaluate policy.

## Common Misconceptions
- More time points always enable better inference
- Autocorrelation is a problem rather than a feature
- Interrupted time series requires random assignment

## Questions

```yaml
- question: "A regression model predicting monthly crime rates from economic indicators produces very significant results with implausibly narrow confidence intervals. A time series expert suspects the standard errors are wrong. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The sample size is too large, inflating the degrees of freedom"
    - "Serial autocorrelation was ignored — treating time-ordered observations as independent artificially deflates standard errors"
    - "The economic predictors are too strongly correlated with each other (multicollinearity)"
    - "The regression was estimated without a constant term"
  answer: 1
  explanation: "When time series data are analyzed with OLS as if observations were independent, autocorrelated errors cause standard errors to be underestimated — sometimes drastically. This produces t-statistics that are too large, p-values too small, and confidence intervals too narrow, giving false confidence in relationships that may be spurious or much weaker than they appear. Crime rates this month are correlated with last month's crime rates because underlying conditions persist — this is not a nuisance but a structural feature that must be modeled explicitly."

- question: "A policy analyst wants to assess whether a state's new gun law reduced homicide rates. Random assignment to treatment is impossible. Which design provides the strongest causal evidence?"
  type: multiple-choice
  options:
    - "A cross-sectional regression comparing states that passed the law to those that did not, controlling for demographics"
    - "A simple before-after comparison of the state's homicide rate in the year before and after the law"
    - "An interrupted time series analysis using many pre-law observations to model the counterfactual trend, then comparing post-law outcomes to that projected trajectory"
    - "A survey asking law enforcement officers whether they believe the law reduced homicides"
  answer: 2
  explanation: "Interrupted time series (ITS) is one of the strongest quasi-experimental designs for policy evaluation without random assignment. By modeling the pre-intervention trend over many time points, ITS estimates what would have happened absent the policy (the counterfactual). A law's causal effect shows up as an abrupt change in level and/or slope after its implementation. The simple before-after comparison (option B) is much weaker — it cannot distinguish a policy effect from pre-existing trends, regression to the mean, or seasonal effects. Cross-sectional comparisons (option A) have severe confounding problems."

- question: "Autocorrelation in a social time series is always a statistical problem that must be eliminated before meaningful analysis can proceed."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about autocorrelation. It is not merely a nuisance — it reflects real persistence in social processes. Unemployment this month is correlated with last month's because economic conditions change gradually; crime rates persist because their social determinants persist. ARIMA models treat autocorrelation as substantive structure to be modeled and understood, not just corrected. The problem is not autocorrelation itself but failing to account for it — which leads to incorrect standard errors and spurious inference."

- question: "A non-stationary time series — one with a unit root or drifting mean — should typically be differenced before fitting an ARIMA model."
  type: true-false
  answer: true
  explanation: "Non-stationarity means the statistical properties of the series change over time, making standard modeling unreliable. A series with a unit root (like many economic levels) can drift without bound, and regressing two such series on each other often produces spurious correlations. First-differencing (working with period-to-period changes rather than levels) typically converts a non-stationary series to a stationary one. The 'I' in ARIMA stands for 'integrated,' reflecting the number of differences needed. The Augmented Dickey-Fuller test checks for unit roots as a diagnostic step before modeling."

- question: "Why does interrupted time series analysis not require random assignment to make causal claims about a policy intervention, and what is its main threat to validity?"
  type: short-answer
  answer: "ITS constructs the counterfactual using the pre-intervention trend itself: many observations before the policy establish what the trajectory would have continued to look like absent the intervention. Any departure from that projected trend after implementation is attributed to the policy. Random assignment is unnecessary because the comparison group is the same unit's own prior trajectory. The main threat to validity is concurrent history effects — other events (economic shocks, parallel policy changes, cultural shifts) may have coincided with the intervention, making it difficult to isolate the policy's specific effect from other simultaneous changes."
  explanation: "The strength of ITS comes from using many pre-intervention time points to estimate a stable baseline trend. The more pre-intervention data, the better the counterfactual is estimated and the more confidently departures can be detected. Replicating the ITS across multiple jurisdictions that implemented the policy at different times strengthens causal inference further — if the break consistently appears at the intervention point across many units, coincidental concurrent history becomes an increasingly implausible explanation."
```

## Explainer

In your prerequisite work with regression, each observation was treated as independent — the error terms were assumed uncorrelated across cases. With social time series data, this assumption breaks down immediately. Crime rates, unemployment, public opinion, and institutional budgets all exhibit **autocorrelation**: this year's value is correlated with last year's because underlying conditions persist over time. Treating autocorrelated data as independent observations leads to artificially small standard errors, false confidence, and spurious findings. Time series methods are the toolkit for handling data where observations are ordered in time and each observation is not independent of its neighbors.

The foundational diagnostic is **stationarity** — whether the statistical properties of a series (mean, variance, autocorrelation structure) are stable over time, or whether the series is drifting or growing. A non-stationary series has a mean or variance that changes over time, making it impossible to model reliably. The classic test is the **Augmented Dickey-Fuller test**, which checks whether a series has a unit root (a sign of non-stationarity). Many social variables — unemployment levels, GDP, population — are non-stationary in levels but become stationary after differencing (working with period-to-period changes rather than raw levels). This is why macroeconomic models often work with growth rates rather than levels. Your background in sequences gives you the core intuition: a stationary series behaves like a bounded sequence, while a non-stationary series can drift without bound.

**ARIMA models** (Autoregressive Integrated Moving Average) are the workhorse of time series analysis. The autoregressive (AR) component models the current value as a linear function of past values: this month's unemployment partly depends on last month's. The moving average (MA) component models the current value as a function of past *error terms*: random shocks propagate forward through time. The "I" stands for integration — how many times you need to difference the series to achieve stationarity. An ARIMA(2,1,1) model has two autoregressive terms, is differenced once, and has one moving average term. Your background in differential equations makes the underlying logic intuitive: ARIMA is a discrete-time dynamic model of how a series evolves, analogous to a first-order difference equation with stochastic inputs.

**Interrupted time series (ITS)** designs apply time series logic to causal inference about policy interventions. The idea: collect many pre-intervention observations to model the counterfactual trend (what would have happened without the policy), then compare post-intervention observations to that projected trend. A law banning cell phone use while driving would show up as an abrupt change in accident rates (a level change) or a changed trajectory (a slope change) after implementation. ITS is one of the strongest quasi-experimental designs for policy evaluation because it doesn't require random assignment — it uses time itself to construct the counterfactual. The key threat to validity is concurrent history effects: other events may have changed at the same moment as the intervention, making it hard to attribute the change to the policy alone. Multiple replications across jurisdictions and times provide the strongest ITS evidence.
