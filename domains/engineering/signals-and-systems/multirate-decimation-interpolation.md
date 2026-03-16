---
id: multirate-decimation-interpolation
title: Multirate Signal Processing and Filter Banks
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
- id: aliasing-reconstruction-signals
  type: hard
- id: dft-and-fft-algorithms
  type: soft
tags:
- multirate
- decimation
- interpolation
- filter-banks
stage: advanced
status: draft
---

# Multirate Signal Processing and Filter Banks

## Core Idea
Decimation reduces sampling rate by integer factor M after anti-aliasing filtering; interpolation increases rate by factor L by inserting zeros and low-pass filtering. Polyphase filter structures decompose filters into parallel paths operating at reduced rates, enabling efficient implementation. Multirate systems are fundamental in audio codecs, communication systems, and signal processing applications.

## Explainer

From sampling theory, you know that a signal with bandwidth B Hz requires a sampling rate of at least 2B Hz to be reconstructed perfectly. From aliasing, you know what goes wrong when that rule is violated: high-frequency components fold back into the baseband and are indistinguishable from genuine low-frequency content. Multirate processing asks a more practical question: what if you have already sampled a signal and need to work with it at a *different* rate — either lower (to save computation or storage) or higher (to interface with another system)? The answers are **decimation** and **interpolation**, and both require careful anti-aliasing logic you already know how to reason about.

**Decimation by M** means keeping only every M-th sample and discarding the rest. Naively doing this would compress the time axis by M, which in the frequency domain expands the spectrum by M — any content between f_s/(2M) and f_s/2 would alias into the lower-frequency band. The solution is to low-pass filter the signal to bandwidth f_s/(2M) *before* discarding samples. This anti-aliasing filter ensures the content that would alias has been removed. The combined operation — filter then downsample — is decimation. The result is a signal at rate f_s/M that faithfully represents the original signal's content up to f_s/(2M). The computational payoff is that all subsequent processing happens at the lower rate, with fewer multiplications per second.

**Interpolation by L** is the reverse: you want more samples per second from a signal that currently has fewer. The procedure is to insert L−1 zeros between every existing sample (upsampling), then apply a low-pass filter at cutoff f_s/2 (in the new higher rate). The zero-insertion step creates a signal at rate L·f_s, but examining its DTFT reveals that the original spectrum now repeats at multiples of the original f_s — in other words, imaging artifacts (the interpolation analog of aliasing). The low-pass filter removes these images, leaving a smoothly interpolated signal. Conceptually, the filter "fills in" the inserted zeros with values that make the waveform continuous and bandlimited. Rational rate conversions by a factor L/M are achieved by cascading interpolation by L with decimation by M.

The efficiency bottleneck in both operations is the anti-aliasing or anti-imaging filter. A direct implementation of an N-tap FIR filter applied before decimation by M would compute N multiplications per input sample, even though M−1 out of every M outputs are immediately discarded — clearly wasteful. **Polyphase decomposition** resolves this by rearranging the filter computation. The filter's coefficients are split into M sub-filters (polyphase components), each of which operates at the lower rate. The computation now costs N/M multiplications per output sample — exactly what you'd expect after moving filtering to the lower rate. This factor-of-M efficiency gain is what makes multirate processing practical in real-time systems. In audio codecs (MP3, AAC), video processing, and software-defined radio, signals are routinely processed at different rates in different stages, and polyphase filter banks are the core computational structure enabling all of it.

