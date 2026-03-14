---
id: kalman-filter-state-estimation
title: Kalman Filter for State Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: random-signals-autocorrelation-psd
  type: soft
tags:
- state-estimation
- optimal-filtering
- recursive
- kalman
stage: advanced
status: draft
---

# Kalman Filter for State Estimation

## Core Idea
The Kalman filter provides optimal recursive state estimation for linear systems with white Gaussian noise. It alternates between time update (prediction from dynamics) and measurement update (correction using observations), using the innovation weighted by the Kalman gain. The filter minimizes estimation error covariance and scales efficiently to high-dimensional problems.
