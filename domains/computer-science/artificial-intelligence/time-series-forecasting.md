---
id: time-series-forecasting
title: Time Series Forecasting
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: recurrent-neural-networks
  type: hard
- id: supervised-learning-intro
  type: hard
- id: probability-density-functions
  type: soft
- id: markov-chains
  type: soft
- id: derivative-as-slope-of-tangent
  type: soft
builds-toward:
- sequence-to-sequence-models
tags:
- time-series
- forecasting
- sequence
stage: advanced
status: validated
---

# Time Series Forecasting

## Core Idea
Time series forecasting predicts future values based on historical patterns in sequentially-dependent data (stocks, weather, demand). RNNs, LSTMs, and Transformers capture temporal dependencies. Challenges include trend, seasonality, external variables, and non-stationarity. Evaluation requires careful temporal splitting to prevent data leakage.

## Questions

```yaml
- question: "A data scientist randomly splits two years of hourly sales data 80/20 into train and test sets, trains an LSTM, and reports excellent test accuracy. What is the fundamental problem?"
  type: multiple-choice
  options:
    - "LSTMs are not appropriate for sales data — a simpler ARIMA model should have been used"
    - "The test set likely contains timestamps from before the end of the training set, so the model was effectively trained on 'future' information it would not have in production"
    - "An 80/20 split does not provide enough training data for a neural network"
    - "Sales data is too noisy for any forecasting model to achieve high accuracy"
  answer: 1
  explanation: "Random splitting breaks temporal causality. When timestamps are randomly distributed across folds, the training set may contain observations *after* some test observations. During training, the model learns patterns that include 'future' values it would never have in a real deployment, producing artificially inflated accuracy. The correct approach — train on the past, evaluate on the future — simulates how the model will actually be used. Walk-forward (rolling-origin) validation is the standard method."

- question: "A naive baseline that predicts the last observed value ('predict t+1 = t') outperforms a carefully tuned LSTM on a stationary demand series. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "LSTMs are computationally too slow for real-time forecasting"
    - "The naive baseline is guaranteed to have lower RMSE by mathematical construction"
    - "The series has strong autocorrelation and is well-behaved; the LSTM likely overfit to noise in training, failing to add value over a simple recency heuristic"
    - "LSTMs require more than one year of training data to outperform naive baselines"
  answer: 2
  explanation: "Naive baselines exploit autocorrelation: in many series, the most recent value is a strong predictor of the next. A model that overfits to training noise, or one that is overcomplicated relative to the series' structure, can perform worse than simply predicting yesterday's value. Comparing against naive baselines before claiming model improvement is essential discipline — if you can't beat 'last value' or 'same time last year,' the sophisticated model has added no value. This is not a quirk; many published models fail this test."

- question: "Computing normalization statistics (mean and standard deviation) over the entire dataset — including the test period — before splitting is a valid preprocessing step for time series forecasting."
  type: true-false
  answer: false
  explanation: "This is data leakage. Using statistics from the entire dataset (including the test period) to normalize the training data means the training set is subtly contaminated with information from the future — the model learns the future mean and variance through the scaling. In production, you only have access to past data, so normalization must be computed on the training period only and then applied with those fixed statistics to the test period. This is one of the most common and insidious mistakes in time series preprocessing."

- question: "Walk-forward (rolling-origin) validation is more appropriate than k-fold cross-validation for evaluating time series forecasting models."
  type: true-false
  answer: true
  explanation: "k-fold cross-validation randomly assigns observations to folds, which breaks temporal ordering and introduces future information into training folds — the equivalent of time travel. Walk-forward validation preserves causality: train on all data up to time t, forecast from t+1 to t+h, advance the window, and repeat. This accurately simulates how the model will be used in deployment and produces realistic performance estimates. k-fold is appropriate for i.i.d. data; time series data is structurally incompatible with it."

- question: "Explain why non-stationarity (trend and seasonality) must be diagnosed before fitting a classical forecasting model, and what happens if it is ignored."
  type: short-answer
  answer: "Classical models like ARIMA assume stationarity — constant mean and variance over time. Trend creates a non-constant mean (the series drifts); seasonality creates structured periodicity that violates the assumption of a constant unconditional distribution. If you fit ARIMA to a trending, seasonal series without addressing non-stationarity, the model estimates unstable parameters, produces unreliable confidence intervals, and typically forecasts by extrapolating a short-term local pattern rather than capturing the true long-run behavior. For example, a model fit to the last few months of a rising trend may forecast continued linear growth but miss the seasonal trough that follows. Standard remedies include differencing (to remove trend), seasonal differencing or decomposition (to remove seasonality), or using models that explicitly handle these components like SARIMA or Prophet."
  explanation: "Stationarity is the foundation for reliable statistical inference in time series. Even neural models (LSTMs, Transformers) benefit from understanding trend and seasonality — features encoding time of year, day of week, and trend direction often improve performance dramatically, because the model can learn seasonal effects explicitly rather than having to discover them from raw timestamps."
```

## Explainer

Time series data is fundamentally different from the tabular datasets you have worked with in supervised learning. Each observation is indexed by time, and the order matters — shuffling the rows destroys the information. This temporal structure creates both opportunities and constraints. The opportunities come from **autocorrelation**: today's temperature, stock price, or sales volume is heavily influenced by yesterday's values, and by the values from a week or year ago. The constraints come from the fact that you cannot randomly split the data into train and test sets. You must always train on the past and evaluate on the future, because anything else simulates a form of time travel that your model will not have in production.

From your work with recurrent neural networks, you know that RNNs process sequences step by step, maintaining a hidden state that accumulates information from past inputs. This makes them natural candidates for time series: feed in observations one timestep at a time, and the hidden state captures the relevant history for predicting the next value. LSTMs improve on vanilla RNNs by using gating mechanisms to selectively remember and forget, which is critical for time series with both short-term fluctuations and long-term patterns. A retail sales series, for example, has daily noise, weekly cycles (weekend spikes), and annual seasonality (holiday surges) — the model must simultaneously track patterns at all these scales.

The components of a time series — **trend**, **seasonality**, and **residual** — must be understood before modeling. Trend is the long-term direction (rising, falling, flat). Seasonality is the repeating pattern at fixed intervals (daily, weekly, annual). The residual is what remains after removing trend and seasonality. Classical methods like ARIMA model the residual as a linear function of past values and past errors, requiring the series to be **stationary** (constant mean and variance over time). Neural approaches are more flexible — they can learn non-linear relationships and handle non-stationarity more gracefully — but they need substantially more data and are harder to interpret. Moving averages and exponential smoothing, which you have already seen, represent the simplest end of this spectrum: weighted averages of past values where the weights decay over time.

Evaluation in time series forecasting requires particular discipline. **Walk-forward validation** (also called rolling-origin evaluation) is the gold standard: train on data up to time t, forecast from t+1 to t+h, then advance the training window and repeat. This simulates how the model will actually be used. Common pitfalls include using future information in feature engineering (e.g., normalizing with statistics computed over the entire dataset including the test period), and failing to account for the forecast horizon — a model that predicts one step ahead well may degrade rapidly at longer horizons. Metrics like MAE and RMSE measure absolute error, while MAPE normalizes by actual values but breaks down near zero. Comparing against naive baselines (predicting the last observed value, or the value from the same season last year) is essential — many sophisticated models fail to beat these simple benchmarks on well-behaved series.
