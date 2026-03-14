---
id: raised-cosine-pulse-shaping
title: Raised-Cosine Pulse Shaping
domain: engineering
course: signals-and-systems
prerequisites:
- id: nyquist-criterion-intersymbol-interference
  type: hard
tags:
- pulse-shaping
- raised-cosine
- isi
- bandwidth-efficiency
stage: advanced
status: draft
---

# Raised-Cosine Pulse Shaping

## Core Idea
Raised-cosine pulse shaping satisfies the Nyquist criterion with smooth spectral roll-off. The impulse response is p(t) = sinc(t/Ts)·cos(παt/Ts)/(1 – 4α²t²/Ts²), where roll-off factor α ∈ [0,1] trades bandwidth efficiency for time decay rate. Root-raised-cosine splits the response between transmit and receive filters, optimizing noise performance in communication systems.
