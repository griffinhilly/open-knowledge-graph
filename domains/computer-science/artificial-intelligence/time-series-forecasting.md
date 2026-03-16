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
- id: calculus
  type: soft
- id: moving-averages-exponential-smoothing
  type: soft
builds-toward:
- temporal-dependencies
- seq2seq-models
tags:
- time-series
- forecasting
- sequence
stage: advanced
status: draft
---

# Time Series Forecasting

## Core Idea
Time series forecasting predicts future values based on historical patterns in sequentially-dependent data (stocks, weather, demand). RNNs, LSTMs, and Transformers capture temporal dependencies. Challenges include trend, seasonality, external variables, and non-stationarity. Evaluation requires careful temporal splitting to prevent data leakage.

## Explainer

Time series data is fundamentally different from the tabular datasets you have worked with in supervised learning. Each observation is indexed by time, and the order matters — shuffling the rows destroys the information. This temporal structure creates both opportunities and constraints. The opportunities come from **autocorrelation**: today's temperature, stock price, or sales volume is heavily influenced by yesterday's values, and by the values from a week or year ago. The constraints come from the fact that you cannot randomly split the data into train and test sets. You must always train on the past and evaluate on the future, because anything else simulates a form of time travel that your model will not have in production.

From your work with recurrent neural networks, you know that RNNs process sequences step by step, maintaining a hidden state that accumulates information from past inputs. This makes them natural candidates for time series: feed in observations one timestep at a time, and the hidden state captures the relevant history for predicting the next value. LSTMs improve on vanilla RNNs by using gating mechanisms to selectively remember and forget, which is critical for time series with both short-term fluctuations and long-term patterns. A retail sales series, for example, has daily noise, weekly cycles (weekend spikes), and annual seasonality (holiday surges) — the model must simultaneously track patterns at all these scales.

The components of a time series — **trend**, **seasonality**, and **residual** — must be understood before modeling. Trend is the long-term direction (rising, falling, flat). Seasonality is the repeating pattern at fixed intervals (daily, weekly, annual). The residual is what remains after removing trend and seasonality. Classical methods like ARIMA model the residual as a linear function of past values and past errors, requiring the series to be **stationary** (constant mean and variance over time). Neural approaches are more flexible — they can learn non-linear relationships and handle non-stationarity more gracefully — but they need substantially more data and are harder to interpret. Moving averages and exponential smoothing, which you have already seen, represent the simplest end of this spectrum: weighted averages of past values where the weights decay over time.

Evaluation in time series forecasting requires particular discipline. **Walk-forward validation** (also called rolling-origin evaluation) is the gold standard: train on data up to time t, forecast from t+1 to t+h, then advance the training window and repeat. This simulates how the model will actually be used. Common pitfalls include using future information in feature engineering (e.g., normalizing with statistics computed over the entire dataset including the test period), and failing to account for the forecast horizon — a model that predicts one step ahead well may degrade rapidly at longer horizons. Metrics like MAE and RMSE measure absolute error, while MAPE normalizes by actual values but breaks down near zero. Comparing against naive baselines (predicting the last observed value, or the value from the same season last year) is essential — many sophisticated models fail to beat these simple benchmarks on well-behaved series.
