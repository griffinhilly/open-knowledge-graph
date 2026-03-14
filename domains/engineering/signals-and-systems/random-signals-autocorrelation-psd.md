---
id: random-signals-autocorrelation-psd
title: Random Signals, Autocorrelation, and Power Spectral Density
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-properties-periodicity-energy-power
  type: hard
- id: parseval-theorem-energy-analysis
  type: hard
tags:
- random-signals
- noise
- stochastic
- power-spectral-density
stage: advanced
status: draft
---

# Random Signals, Autocorrelation, and Power Spectral Density

## Core Idea
Random signals (noise, stochastic processes) are characterized by their autocorrelation R(τ) = E[x(t)x(t+τ)] and power spectral density S(f) = FT{R(τ)}. White noise has flat PSD; colored noise has frequency-dependent power. These tools enable analysis of systems driven by noise and filtering of noisy signals.
