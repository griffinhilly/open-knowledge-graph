---
id: matched-filter-signal-detection
title: Matched Filter for Signal Detection
domain: engineering
course: signals-and-systems
prerequisites:
- id: convolution-continuous-discrete-systems
  type: hard
- id: lti-systems-and-impulse-response
  type: hard
builds-toward:
- nyquist-criterion-intersymbol-interference
tags:
- filtering
- signal-detection
- optimal-filtering
- correlation
stage: advanced
status: draft
---

# Matched Filter for Signal Detection

## Core Idea
The matched filter is the optimal detector for a known signal s(t) corrupted by white Gaussian noise, with impulse response h(t) = s(T–t). The output at time T equals the correlation between received signal and template, maximizing SNR at the decision point and minimizing probability of symbol error in binary hypothesis testing.
