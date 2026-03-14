---
id: bandpass-sampling-and-undersampling
title: Bandpass Sampling and Undersampling
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
builds-toward:
- complex-baseband-iq-representation-analysis
tags:
- bandpass-sampling
- undersampling
- sampling-theorem
stage: abstract-reasoning
status: draft
---

# Bandpass Sampling and Undersampling

## Core Idea
Bandpass signals containing no DC or low-frequency content can be sampled below the Nyquist rate of the full signal bandwidth without aliasing. The sampling rate must exceed twice the signal bandwidth (not twice the highest frequency) and must be chosen to place the signal spectrum in the correct location after downsampling. Bandpass sampling enables lower sampling rates for high-frequency signals, reducing data rates and processing complexity.

## How It's Best Learned
Design a bandpass signal (FM radio example: 100 MHz bandwidth). Apply bandpass sampling theorem to calculate minimum sampling rate below the naive 2×100MHz. Verify no aliasing occurs.

## Common Misconceptions
- Confusing bandpass Nyquist rate with lowpass (depends on bandwidth, not highest frequency).
- Thinking any sampling rate less than 2fc works (must satisfy bandpass conditions).
- Not accounting for spectral folding into correct position for useful downsampling.
