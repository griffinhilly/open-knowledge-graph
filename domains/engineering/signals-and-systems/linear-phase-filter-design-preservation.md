---
id: linear-phase-filter-design-preservation
title: Linear Phase Response and Signal Distortion
domain: engineering
course: signals-and-systems
prerequisites:
- id: magnitude-phase-computation-pole-zero
  type: hard
builds-toward:
- fir-filter-design-realization
- group-delay-phase-characterization
tags:
- filters
- linear-phase
- distortion
- group-delay
stage: abstract-reasoning
status: draft
---

# Linear Phase Response and Signal Distortion

## Core Idea
Linear phase response (phase proportional to frequency) means all frequency components are delayed equally, preserving signal shape. Non-linear phase causes different delays at different frequencies, creating waveform distortion. Symmetric impulse responses guarantee linear phase in FIR filters; IIR filters cannot achieve true linear phase but can approximate it with all-pass equalizers.

## How It's Best Learned
Design a non-causal symmetric FIR filter and verify its linear phase. Compare its output on a chirp signal to that of a non-symmetric filter showing group delay variation.

## Common Misconceptions
- Thinking magnitude response alone determines distortion.
- Assuming constant group delay is the same as zero delay.
- Not recognizing that phase delay differs from group delay.
