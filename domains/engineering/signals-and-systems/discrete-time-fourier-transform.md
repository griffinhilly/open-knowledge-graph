---
id: discrete-time-fourier-transform
title: Discrete-Time Fourier Transform (DTFT)
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
- id: z-transform-discrete-time-signals
  type: soft
builds-toward:
- dft-and-fft-algorithms
- frequency-response-magnitude-phase
tags:
- dtft
- discrete-time
- frequency-domain
stage: advanced
status: draft
---

# Discrete-Time Fourier Transform (DTFT)

## Core Idea
The DTFT X(e^(jω)) = Σ x[n]e^(-jωn) is the Fourier transform of a discrete-time signal, relating discrete-time signals to periodic continuous frequency responses. Unlike the Z-transform (valid on the unit circle), the DTFT is defined only for |z|=1.
