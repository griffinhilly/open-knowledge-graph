---
id: quantization-error-and-noise-analysis
title: Quantization Error and Noise Analysis
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
builds-toward:
- dithering-techniques-quantization-improvement
- anti-aliasing-filters-pre-sampling-design
tags:
- quantization
- ADC
- noise
- error
stage: formal-systems
status: draft
---

# Quantization Error and Noise Analysis

## Core Idea
Analog-to-digital conversion introduces quantization error when rounding continuous values to discrete levels. For uniform quantization with step size Δ, quantization error is uniformly distributed on [-Δ/2, Δ/2], producing noise power of Δ²/12. Signal-to-quantization-noise-ratio (SQNR) improves 6 dB per additional bit. For small quantization error, treating it as white noise is a reasonable approximation, though this breaks down for underutilized quantizers or signals near quantization boundaries.

## How It's Best Learned
Quantize sinusoids of various amplitudes to 8-bit resolution. Measure quantization noise power and verify SQNR matches theoretical predictions. Observe non-white behavior when signal underutilizes quantizer range.

## Common Misconceptions
- Thinking quantization noise is always white (depends on signal characteristics).
- Assuming n-bit quantization gives n bits of information (doesn't account for underutilization).
- Not recognizing the 6 dB per bit rule applies only in saturation regime.

## Explainer

When you convert a continuous-time signal to digital, the process involves two steps: sampling in time and quantization in amplitude. From your study of continuous versus discrete signals, you know that time-sampling is governed by the Nyquist theorem. **Quantization** is the second step: the sampled amplitude, which can take any real value, must be rounded to the nearest of a finite set of discrete levels. This rounding introduces an error — the difference between the true amplitude and the quantized value — called **quantization error**. Understanding the statistical behavior of this error is essential for specifying ADC requirements in signal processing systems.

For a **uniform quantizer** with N bits, there are 2^N discrete output levels spanning the full-scale input range. The spacing between adjacent levels is the **step size** Δ = (full scale) / 2^N. Each quantized sample contains an error in the range [−Δ/2, +Δ/2]. For well-behaved signals that use the full quantizer range and don't dwell near a single level, this error is approximately **uniformly distributed** on that interval. A uniform distribution on [−Δ/2, +Δ/2] has mean zero and variance σ²_q = Δ²/12. This is the quantization **noise power** — independent of the signal, depending only on the step size and hence on the number of bits.

The **signal-to-quantization-noise ratio (SQNR)** is the ratio of signal power to noise power. For a full-scale sinusoid that uses the entire quantizer range, the derivation gives SQNR ≈ 6.02N + 1.76 dB. This is the famous **6 dB per bit rule**: each additional bit halves the step size Δ, reducing noise power by a factor of 4 (−6 dB) and raising SQNR by approximately 6 dB. An 8-bit ADC delivers about 50 dB SQNR; a 16-bit ADC about 98 dB; a 24-bit ADC roughly 146 dB. This rule is the first thing an audio engineer reaches for when specifying an ADC — CD audio uses 16 bits, professional recording uses 24 bits.

The white-noise model for quantization error has important limits. It holds when the signal is broadband, uses the full quantizer range, and changes significantly from sample to sample. When a signal is periodic relative to the step size, or barely changes between samples, the quantization error becomes correlated and can appear as tones — harmonics of the signal — in the spectrum. This is audible as **granulation noise** in audio applications. The practical remedy is **dithering**: adding a small random noise signal before quantization deliberately randomizes the error, converting structured tonal artifacts into spectrally flat noise. A small sacrifice in ideal SQNR is exchanged for a perceptually much cleaner error character — a trade that is almost always worthwhile in audio and precision measurement systems.
