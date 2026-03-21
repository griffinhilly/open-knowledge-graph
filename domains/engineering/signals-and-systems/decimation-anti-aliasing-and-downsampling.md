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

## Questions

```yaml
- question: "A digital signal sampled at 48 kHz contains a tone at 10 kHz. It is downsampled by factor M = 4 (to 12 kHz) without any prior filtering. What appears in the output?"
  type: multiple-choice
  options:
    - "A 10 kHz tone — downsampling preserves the signal content faithfully"
    - "Nothing — the 10 kHz tone is above the new Nyquist rate and is silently discarded"
    - "A spurious 2 kHz tone — the 10 kHz component folds into the baseband through aliasing"
    - "A 6 kHz tone — the component wraps to the new Nyquist boundary"
  answer: 2
  explanation: "After downsampling by 4, the new sample rate is 12 kHz and the new Nyquist is 6 kHz. The 10 kHz tone exceeds the new Nyquist and aliases: it folds to |12 − 10| = 2 kHz. A 2 kHz tone now appears in the output that was never in the original signal — this is aliasing corruption, not mere information loss. This example shows why unfiltered downsampling is destructive: it does not just discard high frequencies, it injects false low-frequency components into the band you care about."

- question: "In a properly designed decimator with downsampling factor M, where should the anti-aliasing lowpass filter's cutoff frequency be set?"
  type: multiple-choice
  options:
    - "At fs/2 — the original Nyquist rate, to reject any frequencies above that"
    - "At fs/(2M) — the new Nyquist rate after downsampling"
    - "At fs/M — the new sample rate itself"
    - "At 2fs/M — twice the new sample rate to provide margin"
  answer: 1
  explanation: "The new Nyquist rate after downsampling to fs/M is fs/(2M). Any signal energy above fs/(2M) will alias into the 0 to fs/(2M) band in the decimated output. The anti-aliasing filter must attenuate all energy above fs/(2M) before the downsampling step occurs. Setting the cutoff at the original Nyquist (fs/2) would fail to remove the components between fs/(2M) and fs/2 that cause aliasing — exactly the wrong answer and the most common design error."

- question: "Downsampling without prior anti-aliasing filtering can introduce frequency components into the output that were not present in the original signal."
  type: true-false
  answer: true
  explanation: "This is the essence of aliasing: high-frequency components fold into lower frequencies when the sampling rate is reduced. A tone at frequency f that exceeds the new Nyquist rate fs/(2M) reappears at a lower aliased frequency |k·(fs/M) − f| for some integer k. These aliased tones were never in the original baseband signal — they are fabricated artifacts of the undersampling process. This is why the filter must precede the downsampler: once aliasing occurs, there is no way to undo it."

- question: "The purpose of the anti-aliasing filter in a decimation system is primarily to remove high-frequency noise and improve signal quality before storage."
  type: true-false
  answer: false
  explanation: "Noise removal is a side benefit, but the primary purpose is to prevent aliasing — specifically, to eliminate signal energy between fs/(2M) and fs/2 that would otherwise fold into the baseband and corrupt the low-frequency content the decimator is trying to preserve. Without the filter, a clean signal with no noise can still be badly corrupted by its own high-frequency components aliasing into the passband. The filter is not optional cleanup; it is a required step for mathematically correct decimation."

- question: "A colleague claims: 'Downsampling just throws away samples, so it can only lose information — it can't add anything or corrupt the remaining signal.' What is wrong with this reasoning, and what actually happens to a high-frequency tone during unfiltered downsampling?"
  type: short-answer
  answer: "The error is treating downsampling as simple deletion. Downsampling is equivalent to re-sampling the signal at a lower rate. When a signal contains energy above the new Nyquist rate, that energy is not simply absent from the output — it folds back (aliases) into the lower frequency band through spectral wrapping. A tone at frequency f aliases to |f − k·fs_new| for the nearest integer k. This creates a new tone at a completely different frequency that was never present in the original, corrupting the passband content the decimator was supposed to preserve faithfully."
  explanation: "The intuition for why this happens: keeping every Mth sample is mathematically equivalent to multiplying the signal by a pulse train with period M, which in the frequency domain convolves with a train of impulses at multiples of fs/M. This convolution copies the spectrum at every multiple of fs/M — and these copies overlap with the baseband if the signal isn't bandlimited to fs/(2M) first. The overlap is the aliasing, and it is additive corruption, not mere truncation."
```

## Explainer

From your work on anti-aliasing filters, you know that before sampling a continuous-time signal at rate f_s, you must filter out any content above f_s/2 to prevent aliasing — the "folding back" of high-frequency content into the baseband that corrupts the sampled signal. **Decimation** applies the same reasoning in the discrete-time domain: if you have a digital signal already sampled at f_s and want to reduce the data rate by a factor of M, keeping every Mth sample is equivalent to re-sampling at f_s/M. The new Nyquist frequency is f_s/(2M). If the original signal has any energy between f_s/(2M) and f_s/2, that energy aliases into the 0 to f_s/(2M) band in the decimated output.

To see why unfiltered downsampling is destructive, consider a concrete example: a signal sampled at 48 kHz with a tone at 10 kHz, downsampled by M = 4 to 12 kHz. The new Nyquist is 6 kHz. The 10 kHz tone must be represented in the decimated signal, but 10 kHz > 6 kHz, so it folds: 10 kHz aliases to 12 − 10 = 2 kHz. The output now contains a 2 kHz tone that was never in the original signal. Decimation without filtering does not just lose high-frequency content — it actively corrupts the low-frequency content you wanted to keep.

The solution is to apply a **discrete-time anti-aliasing lowpass filter** before the downsampler. The filter must attenuate everything above the new Nyquist f_s/(2M), passing only the band of interest 0 to f_s/(2M). The system is: input → [LPF with cutoff f_s/(2M)] → [keep every Mth sample] → output. This is a complete **decimator**. The filter removes the aliases before they can be created by the downsampling step. The key design specification is that the filter's stopband must begin at or below f_s/(2M) with sufficient attenuation that the folded components are negligible relative to your signal floor.

Designing the anti-aliasing filter involves a genuine trade-off. Sharper rolloff (steeper transition from passband to stopband) requires a higher-order FIR or IIR filter, which means more computation per output sample. But in a decimator you only need one output sample for every M input samples, so the filtered output is computed at full rate but only retained at the lower rate. This means you can afford to run a more expensive filter than in a single-rate system, and the computation cost of decimation is often dominated by the filter rather than the actual downsampling operation. A common optimization is the **polyphase decomposition**, which restructures the filter so computations are shared efficiently across the M phases — but that is the next topic.

**Decimation by large factors** is typically done in multiple stages rather than one. Decimating by M = 256 in one step requires a filter with an extremely sharp cutoff (passband extending to only 1/256 of f_s/2 before attenuating), which demands a very high filter order and proportionally high computation. Instead, cascading two stages — decimate by 16, then by 16 — uses two moderate-order filters and is often far more efficient. Each stage's filter specification is more relaxed, its order is lower, and the second stage operates at 1/16th the original rate, so its computation cost is reduced proportionally. Multi-stage decimation is a standard pattern in audio codec design, software-defined radio, and any system that needs to bridge a large gap between input and output sample rates.
