---
id: impulse-invariance-discretization
title: Impulse Invariance for Digital Filter Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: z-transform-discrete-time-signals
  type: hard
- id: laplace-transform-fundamentals
  type: hard
- id: aliasing-reconstruction-signals
  type: hard
tags:
- filter-design
- digital-filters
- discretization
- impulse-response
stage: advanced
status: draft
---

# Impulse Invariance for Digital Filter Design

## Core Idea
Impulse invariance maps analog filter impulse response to digital by sampling: h[n] = T·ha(nT). This preserves the shape of the analog response at sample times but introduces aliasing if the analog filter is not sufficiently bandlimited. Unlike bilinear transform, it does not preserve stability for poles outside the left half-plane.
