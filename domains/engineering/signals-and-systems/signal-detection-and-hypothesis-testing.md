---
id: signal-detection-and-hypothesis-testing
title: Signal Detection and Statistical Hypothesis Testing
domain: engineering
course: signals-and-systems
prerequisites:
- id: matched-filter-signal-detection
  type: soft
builds-toward:
- quantization-error-and-noise-analysis
- parametric-signal-models-ar-ma-arma
tags:
- detection
- hypothesis-testing
- statistics
- SNR
stage: formal-systems
status: draft
---

# Signal Detection and Statistical Hypothesis Testing

## Core Idea
Signal detection frames the problem as binary hypothesis testing: is the observed signal noise alone (H0) or signal plus noise (H1)? The optimal detector is the likelihood ratio test, which compares the probability of observations under each hypothesis. Detection performance is measured by probability of detection and false-alarm rate, controlled by threshold. SNR determines detection performance; higher SNR enables lower false-alarm rates for fixed detection probability.

## How It's Best Learned
Design a detector for a known sinusoid in Gaussian white noise. Compute receiver operating characteristic (ROC) curves showing detection probability vs false-alarm rate at different SNR levels.

## Common Misconceptions
- Thinking higher threshold always improves detection (increases misses).
- Confusing matched filtering with optimal detection threshold.
- Not recognizing that SNR fundamentally limits detection performance.
