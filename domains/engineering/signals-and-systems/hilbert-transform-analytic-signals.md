---
id: hilbert-transform-analytic-signals
title: Hilbert Transform and Analytic Signals
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
builds-toward:
- quadrature-modulation-iq-representation
tags:
- hilbert-transform
- analytic-signals
- envelope
- phase
stage: advanced
status: draft
---

# Hilbert Transform and Analytic Signals

## Core Idea
The Hilbert transform H[x(t)] produces output whose spectrum is the original spectrum multiplied by –j·sgn(f). The analytic signal z(t) = x(t) + j·H[x(t)] suppresses negative frequencies, enabling instantaneous amplitude and phase extraction. Phase unwrapping recovers instantaneous frequency as dφ/dt.
