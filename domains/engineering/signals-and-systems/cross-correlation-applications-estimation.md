---
id: cross-correlation-applications-estimation
title: Cross-Correlation Applications and Time Delay Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: convolution-continuous-discrete-systems
  type: hard
builds-toward:
- matched-filter-signal-detection
- signal-detection-and-hypothesis-testing
tags:
- correlation
- cross-correlation
- time-delay
- estimation
stage: formal-systems
status: draft
---

# Cross-Correlation Applications and Time Delay Estimation

## Core Idea
Cross-correlation between two signals measures their similarity as a function of relative time delay. The peak of the cross-correlation function indicates the delay of maximum similarity, enabling time-delay estimation and synchronization. Normalized cross-correlation (correlation coefficient) is independent of signal amplitudes. Applications include radar/sonar target detection, audio alignment, and template matching.

## How It's Best Learned
Cross-correlate a known template with a signal containing the template at unknown delay. Find the delay by locating the correlation peak. Add noise and observe robustness.

## Common Misconceptions
- Confusing cross-correlation with convolution (they differ by time reversal of one signal).
- Thinking high correlation magnitude implies causation.
- Not normalizing when comparing different signal pairs.
