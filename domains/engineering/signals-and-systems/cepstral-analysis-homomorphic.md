---
id: cepstral-analysis-homomorphic
title: Cepstral Analysis and Homomorphic Filtering
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
- id: hilbert-transform-analytic-signals
  type: soft
tags:
- cepstral
- homomorphic
- deconvolution
stage: advanced
status: draft
---

# Cepstral Analysis and Homomorphic Filtering

## Core Idea
The cepstrum is the inverse Fourier transform of log-magnitude spectrum: c[n] = IFFT[log|FFT[x[n]]|]. Cepstral analysis deconvolves multiplicative components in the frequency domain (e.g., separating voice source from vocal tract response). Homomorphic filtering applies linear operations in the cepstral domain then inverts, useful for speech processing, pitch detection, and seismic deconvolution.
