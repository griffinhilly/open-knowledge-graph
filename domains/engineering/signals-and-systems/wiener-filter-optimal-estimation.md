---
id: wiener-filter-optimal-estimation
title: Wiener Filter for Optimal Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
- id: lti-systems-and-impulse-response
  type: hard
builds-toward:
- kalman-filter-state-estimation
- adaptive-filtering-lms
tags:
- optimal-filtering
- estimation
- wiener
- frequency-domain
stage: advanced
status: draft
---

# Wiener Filter for Optimal Estimation

## Core Idea
The Wiener filter minimizes mean-square error for linear estimation, with optimal transfer function H(ω) = Sxy(ω)/Sxx(ω) in the frequency domain. It requires knowledge of signal and noise statistics. The non-causal solution is optimal but unrealizable; causal approximations reduce performance but enable real-time implementation.
