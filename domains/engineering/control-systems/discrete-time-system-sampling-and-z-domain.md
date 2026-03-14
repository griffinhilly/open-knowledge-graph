---
id: discrete-time-system-sampling-and-z-domain
title: 'Discrete-Time Systems: Sampling and z-Domain Analysis'
domain: engineering
course: control-systems
prerequisites:
- id: digital-control-intro
  type: hard
- id: transfer-functions-control
  type: hard
builds-toward:
- practical-control-system-implementation
tags:
- sampling
- z-transform
- discrete-time
- aliasing
- sampler-hold
stage: abstract-reasoning
status: draft
---

# Discrete-Time Systems: Sampling and z-Domain Analysis

## Core Idea
Sampling continuous signals at rate Ts produces discrete-time signals; the z-transform is the discrete analog of the Laplace transform with z = esTs. Nyquist sampling theorem requires Ts ≤ π/ωmax to avoid aliasing. Discrete-time systems are analyzed using z-domain pole-zero maps analogous to continuous s-domain analysis.
