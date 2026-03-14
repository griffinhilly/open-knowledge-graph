---
id: system-identification-least-squares
title: System Identification Using Least-Squares Methods
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
- id: adaptive-filtering-lms
  type: soft
tags:
- system-identification
- least-squares
- parameter-estimation
stage: advanced
status: draft
---

# System Identification Using Least-Squares Methods

## Core Idea
System identification estimates unknown parameters (filter coefficients, plant poles) from input-output measurements. Least-squares minimizes prediction error ‖y – H·θ‖², with closed-form solution θ = (H^T·H)^(–1)·H^T·y. Recursive algorithms update estimates as new data arrives. Regularization prevents overfitting to noisy data by penalizing large parameter magnitudes.
