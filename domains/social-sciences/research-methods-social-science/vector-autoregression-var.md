---
id: vector-autoregression-var
title: Vector Autoregression (VAR) Models
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: time-series-cross-section
  type: hard
- id: causal-inference-observational-data
  type: soft
builds-toward:
- structural-var-models
- impulse-response-analysis
tags:
- time-series
- multivariate
- dynamics
- causal
stage: advanced
status: draft
---

# Vector Autoregression (VAR) Models

## Core Idea
Vector autoregression models capture dynamic interdependencies among multiple time series. Each variable is regressed on its own past values and the past values of all other variables. VARs reveal which variables Granger-cause others, and impulse-response functions show how a shock to one variable propagates through the system. VARs are used to study feedback loops in economic systems, policy dynamics, and social processes.
