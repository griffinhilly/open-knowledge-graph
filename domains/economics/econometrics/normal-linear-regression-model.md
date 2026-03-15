---
id: normal-linear-regression-model
title: Normal Linear Regression Model
domain: economics
course: econometrics
prerequisites:
- id: simple-linear-regression-estimation
  type: hard
- id: normal-distribution
  type: soft
builds-toward:
- t-statistic-individual-coefficient
- f-statistic-overall-significance
tags:
- regression
- normality
- inference
- assumptions
stage: formal-systems
status: draft
---

# Normal Linear Regression Model

## Core Idea
The normal regression model assumes u ~ N(0,σ²) in addition to OLS assumptions. This distributional assumption enables hypothesis testing and confidence intervals via t and F statistics, allowing exact inference in finite samples rather than relying on asymptotics.
