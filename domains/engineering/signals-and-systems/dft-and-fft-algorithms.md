---
id: dft-and-fft-algorithms
title: Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT) Algorithms
domain: engineering
course: signals-and-systems
prerequisites:
- id: discrete-time-fourier-transform
  type: hard
- id: complex-numbers-intro
  type: hard
- id: fourier-transform-definition-properties
  type: soft
builds-toward:
- digital-signal-processing-fundamentals
tags:
- dft
- fft
- algorithms
- computational
stage: advanced
status: draft
---

# Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT) Algorithms

## Core Idea
The DFT X[k] = Σ x[n]e^(-j2πkn/N) computes the frequency content of a finite-length sequence, with O(N²) operations. The FFT (Cooley-Tukey algorithm) reduces this to O(N log N), making real-time spectral analysis practical. FFT is the foundation of digital signal processing.
