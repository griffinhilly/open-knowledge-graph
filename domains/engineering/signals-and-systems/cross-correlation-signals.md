---
id: cross-correlation-signals
title: Cross-Correlation and Time Delay Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
builds-toward:
- coherence-and-spectral-density
tags:
- cross-correlation
- time-delay
- similarity
- signals
stage: advanced
status: draft
---

# Cross-Correlation and Time Delay Estimation

## Core Idea
Cross-correlation Rxy(τ) = ∫ x(t)·y(t+τ) dt measures similarity between two signals as a function of delay τ. The peak indicates the time lag that best aligns the signals, enabling time-delay estimation for target location and synchronization. Normalized cross-correlation removes amplitude effects. In noise, matched filtering and phase-based methods improve robustness.
