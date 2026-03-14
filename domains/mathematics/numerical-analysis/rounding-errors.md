---
id: rounding-errors
title: Rounding Errors and Error Propagation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: machine-epsilon
  type: hard
builds-toward:
- catastrophic-cancellation
- numerical-stability
tags:
- rounding
- error
- propagation
stage: abstract-reasoning
status: draft
---

# Rounding Errors and Error Propagation

## Core Idea
Every floating point operation introduces rounding error bounded by machine epsilon times the result's magnitude. As operations are chained, these errors accumulate unpredictably. Understanding error propagation through algorithms is essential for predicting and controlling overall numerical accuracy.
