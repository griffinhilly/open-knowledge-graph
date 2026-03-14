---
id: power-spectral-density-estimation
title: Power Spectral Density Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
- id: dft-and-fft-algorithms
  type: hard
builds-toward:
- coherence-and-spectral-density
tags:
- psd-estimation
- spectral-analysis
- periodogram
- welch
stage: advanced
status: draft
---

# Power Spectral Density Estimation

## Core Idea
PSD estimation computes power spectrum from finite, noisy data. Periodogram (|DFT|²) is simple but biased; Welch method averages segmented periodograms to reduce variance at the cost of frequency resolution. Parametric methods assume signal model and achieve higher resolution from shorter records but fail if the model is misspecified. All methods involve bias-variance and resolution tradeoffs.
