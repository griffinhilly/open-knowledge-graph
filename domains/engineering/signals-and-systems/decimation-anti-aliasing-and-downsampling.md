---
id: decimation-anti-aliasing-and-downsampling
title: Decimation, Anti-Aliasing, and Downsampling
domain: engineering
course: signals-and-systems
prerequisites:
- id: anti-aliasing-filters-pre-sampling-design
  type: hard
builds-toward: []
tags:
- decimation
- downsampling
- anti-aliasing
- multirate
stage: advanced
status: draft
---
# Decimation, Anti-Aliasing, and Downsampling

## Core Idea
Decimation by factor M involves lowpass filtering to avoid aliasing, then downsampling by keeping every Mth sample. The anti-aliasing filter must eliminate frequencies above the new Nyquist rate (fs/M). Unfiltered downsampling causes aliasing from frequency components between fs/M and fs/2 to fold into the passband. Proper decimation preserves information in the signal band of interest while reducing data rate.

## How It's Best Learned
Demonstrate aliasing from direct downsampling by factor 3 on a signal containing energy above the new Nyquist rate. Design anti-aliasing filter, apply, then downsample. Verify aliasing is eliminated.

## Common Misconceptions
- Thinking downsampling preserves the entire signal (information outside new Nyquist rate is lost).
- Confusing the original and reduced Nyquist rates in filter design.
- Not accounting for filter order when specifying decimation system complexity.

## Explainer

From your work on anti-aliasing filters, you know that before sampling a continuous-time signal at rate f_s, you must filter out any content above f_s/2 to prevent aliasing — the "folding back" of high-frequency content into the baseband that corrupts the sampled signal. **Decimation** applies the same reasoning in the discrete-time domain: if you have a digital signal already sampled at f_s and want to reduce the data rate by a factor of M, keeping every Mth sample is equivalent to re-sampling at f_s/M. The new Nyquist frequency is f_s/(2M). If the original signal has any energy between f_s/(2M) and f_s/2, that energy aliases into the 0 to f_s/(2M) band in the decimated output.

To see why unfiltered downsampling is destructive, consider a concrete example: a signal sampled at 48 kHz with a tone at 10 kHz, downsampled by M = 4 to 12 kHz. The new Nyquist is 6 kHz. The 10 kHz tone must be represented in the decimated signal, but 10 kHz > 6 kHz, so it folds: 10 kHz aliases to 12 − 10 = 2 kHz. The output now contains a 2 kHz tone that was never in the original signal. Decimation without filtering does not just lose high-frequency content — it actively corrupts the low-frequency content you wanted to keep.

The solution is to apply a **discrete-time anti-aliasing lowpass filter** before the downsampler. The filter must attenuate everything above the new Nyquist f_s/(2M), passing only the band of interest 0 to f_s/(2M). The system is: input → [LPF with cutoff f_s/(2M)] → [keep every Mth sample] → output. This is a complete **decimator**. The filter removes the aliases before they can be created by the downsampling step. The key design specification is that the filter's stopband must begin at or below f_s/(2M) with sufficient attenuation that the folded components are negligible relative to your signal floor.

Designing the anti-aliasing filter involves a genuine trade-off. Sharper rolloff (steeper transition from passband to stopband) requires a higher-order FIR or IIR filter, which means more computation per output sample. But in a decimator you only need one output sample for every M input samples, so the filtered output is computed at full rate but only retained at the lower rate. This means you can afford to run a more expensive filter than in a single-rate system, and the computation cost of decimation is often dominated by the filter rather than the actual downsampling operation. A common optimization is the **polyphase decomposition**, which restructures the filter so computations are shared efficiently across the M phases — but that is the next topic.

**Decimation by large factors** is typically done in multiple stages rather than one. Decimating by M = 256 in one step requires a filter with an extremely sharp cutoff (passband extending to only 1/256 of f_s/2 before attenuating), which demands a very high filter order and proportionally high computation. Instead, cascading two stages — decimate by 16, then by 16 — uses two moderate-order filters and is often far more efficient. Each stage's filter specification is more relaxed, its order is lower, and the second stage operates at 1/16th the original rate, so its computation cost is reduced proportionally. Multi-stage decimation is a standard pattern in audio codec design, software-defined radio, and any system that needs to bridge a large gap between input and output sample rates.
