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
