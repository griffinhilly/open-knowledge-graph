---
id: short-time-fourier-transform
title: Short-Time Fourier Transform
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
- id: window-functions-spectral-leakage
  type: soft
builds-toward:
- wavelet-transform-analysis
tags:
- time-frequency
- stft
- spectral-analysis
- windows
stage: advanced
status: draft
---

# Short-Time Fourier Transform

## Core Idea
The Short-Time Fourier Transform (STFT) computes Fourier transform of overlapping windowed segments to provide time-frequency representation: STFT(t,ω) = ∫ x(τ)·w(τ–t)·e^(–jωτ) dτ. It trades time and frequency resolution: narrower windows improve time localization but worsen frequency resolution. Spectrograms visualize STFT magnitude showing frequency evolution over time.
