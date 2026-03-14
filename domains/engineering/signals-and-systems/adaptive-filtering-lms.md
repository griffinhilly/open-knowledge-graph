---
id: adaptive-filtering-lms
title: Adaptive Filtering with LMS Algorithm
domain: engineering
course: signals-and-systems
prerequisites:
- id: wiener-filter-optimal-estimation
  type: hard
- id: random-signals-autocorrelation-psd
  type: soft
builds-toward:
- rls-adaptive-filtering
tags:
- adaptive-filters
- lms
- gradient-descent
- convergence
stage: advanced
status: draft
---

# Adaptive Filtering with LMS Algorithm

## Core Idea
The Least Mean Squares (LMS) algorithm adapts filter coefficients using stochastic gradient descent: w[n+1] = w[n] – μ·e[n]·x[n]. For sufficiently small step size μ, coefficients converge in expectation to the Wiener solution. LMS has O(N) computational complexity per update, making it practical for real-time applications, with a tradeoff between convergence speed and final error.
