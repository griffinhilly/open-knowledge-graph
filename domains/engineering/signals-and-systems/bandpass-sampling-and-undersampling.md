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

## Explainer

The Nyquist theorem you already know states that to recover a signal without aliasing, you must sample at least twice the highest frequency it contains. A 10 kHz audio signal needs at least 20 kHz sampling rate. That rule is correct — but it is actually more general than it first appears, and the generalization is what makes bandpass sampling powerful.

The real requirement behind the Nyquist theorem is not "sample at twice the highest frequency" but rather "sample fast enough that spectral copies don't overlap." When you sample at rate f_s, the spectrum of the sampled signal is the original spectrum repeated at every multiple of f_s. As long as those copies don't overlap each other, you can recover the original signal with a filter. For a low-pass signal from DC to B Hz, the copies are spaced f_s apart and you need f_s ≥ 2B to prevent overlap. But a **bandpass signal** is different: it lives in a narrow band from f_low to f_high, with a bandwidth B = f_high − f_low, and contains no energy below f_low. Its spectral copies only need to avoid each other — not avoid DC — which means a lower sampling rate can suffice.

Consider an FM radio signal centered at 100 MHz with 200 kHz bandwidth. A naïve interpretation of Nyquist says sample at 200 MHz. But the signal only occupies 200 kHz of bandwidth. Bandpass sampling says: choose a sampling rate f_s ≥ 2B = 400 kHz such that when the spectral copies land, they don't overlap. The condition is that there exists an integer n such that 2f_high/n ≥ f_s ≥ 2f_low/(n−1) — a window of valid sampling rates for each n. The copies fold the high-frequency signal down to a lower frequency band, effectively performing **downconversion for free** by exploiting aliasing deliberately. The output is a low-frequency replica of the original bandpass signal that a cheaper ADC and processor can handle.

The critical requirement is that the spectral copies must land cleanly — the folded spectrum must occupy a frequency slot without overlapping adjacent copies. If you choose f_s carelessly within the allowed range, the folded copy might partially overlap its neighbor, creating irrecoverable aliasing even though the rate technically satisfies a bandpass condition. This is why the "valid sampling windows" require careful calculation of the integer n and the exact f_s. The reward is significant: sampling a 1 GHz-centered signal with 10 MHz bandwidth at 25 MHz instead of 2 GHz, reducing data rates, converter cost, and power by 80× — which is why **undersampling** architectures are standard in software-defined radio receivers and radar signal processing.
