---
id: eeg-time-frequency-analysis
title: EEG Time-Frequency Analysis and Neural Oscillations
domain: psychology
course: cognitive-neuroscience
prerequisites:
- id: eeg-erp-temporal-dynamics
  type: hard
- id: frequency-oscillations-cognition
  type: hard
- id: fourier-series-lp-theory
  type: soft
- id: fourier-series-definition
  type: soft
builds-toward:
- attention-switching-theta-oscillations
- working-memory-theta-gamma-coupling
tags:
- EEG
- oscillations
- theta
- alpha
- beta
- gamma
- time-frequency
stage: advanced
status: draft
---

# EEG Time-Frequency Analysis and Neural Oscillations

## Core Idea
EEG recordings contain oscillatory activity across frequency bands (delta <4Hz, theta 4-8Hz, alpha 8-12Hz, beta 12-30Hz, gamma 30-100+Hz) that reflect different neural states and cognitive processes. Time-frequency decomposition reveals how the power and phase of these oscillations change during cognition, enabling inference about neural communication, attention allocation, and memory operations.

## How It's Best Learned
Begin by understanding Fourier analysis and windowed spectrograms for time-frequency decomposition. Examine published EEG time-frequency plots from different cognitive domains (attention, memory, motor control) to build intuition for characteristic oscillatory signatures.

## Common Misconceptions
- High gamma power always reflects neural spiking; gamma can arise from volume-conducted muscle artifact or EMG.
- Power increases in one frequency indicate reduced activity in others; spectral changes are interdependent.
- Oscillatory phase has no information; phase-amplitude coupling and phase-phase coupling carry cognitive significance.
