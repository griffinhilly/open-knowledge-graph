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
stage: advanced
status: validated
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

## Questions

```yaml
- question: "A professional audio studio upgrades its ADC from 16-bit to 24-bit resolution. By approximately how much does this improve the signal-to-quantization-noise ratio?"
  type: multiple-choice
  options:
    - "6 dB — one additional bit of improvement"
    - "24 dB — the number of bits times 1 dB"
    - "48 dB — eight additional bits times approximately 6 dB per bit"
    - "98 dB — the absolute SQNR of a 16-bit system"
  answer: 2
  explanation: "The SQNR formula is approximately 6.02N + 1.76 dB. For 16 bits: ~98 dB. For 24 bits: ~146 dB. The difference is (24 − 16) × 6 dB = 48 dB. The 6 dB per bit rule comes directly from the step size: each additional bit halves Δ, reducing noise power Δ²/12 by a factor of 4, which is −6 dB. This is the rule audio engineers reach for first when specifying ADC resolution requirements. CD audio (16-bit) gives ~98 dB dynamic range; professional recording (24-bit) gives ~146 dB, allowing headroom for mixing without audible noise floor."

- question: "An engineer quantizes a 100 Hz sinusoid to 8-bit resolution and examines the frequency spectrum of the quantization error. What is most likely observed?"
  type: multiple-choice
  options:
    - "A flat, spectrally white noise floor uniformly distributed across all frequencies from 0 to Nyquist"
    - "Tonal components at harmonics of 100 Hz, because the periodic signal creates correlated (non-white) quantization error"
    - "A single spike at 100 Hz because the quantization error is in phase with the signal"
    - "Energy concentrated only near the Nyquist frequency where quantization operates"
  answer: 1
  explanation: "The white-noise model for quantization error assumes the signal sweeps through quantization levels in an uncorrelated, pseudo-random way. For a pure sinusoid, the error is periodic — the same amplitude values repeat every cycle, producing the same quantization errors in the same pattern. This correlation manifests as tonal artifacts (harmonics of the signal frequency) in the error spectrum rather than flat white noise. The white-noise model holds well for broadband signals that use the full quantizer range; it breaks down for signals that are periodic relative to the step size, nearly constant, or severely underutilizing the quantizer range."

- question: "Each additional bit of ADC resolution approximately halves the quantization step size, which reduces quantization noise power by a factor of four and improves SQNR by about 6 dB."
  type: true-false
  answer: true
  explanation: "True. With N bits and full-scale range FS, step size Δ = FS/2^N. Adding one bit doubles 2^N, halving Δ. Noise power σ²_q = Δ²/12 decreases by a factor of 4 (since (Δ/2)²/12 = Δ²/48 = σ²_q/4). A factor-of-4 reduction in noise power is −6 dB in power terms (10 log₁₀(4) ≈ 6 dB). This is the '6 dB per bit' rule, one of the most important rules of thumb in digital signal processing. It holds for sinusoidal signals using the full quantizer range; signals that underutilize the quantizer give less than 6 dB per bit improvement."

- question: "Dithering improves the signal-to-quantization-noise ratio by randomizing quantization error, eliminating tonal artifacts while also reducing total noise power."
  type: true-false
  answer: false
  explanation: "False. Dithering adds a small random noise signal before quantization, which does convert structured tonal artifacts into spectrally flat (white) noise. But this comes at the cost of slightly increased total noise power — you have added noise deliberately. The ideal SQNR decreases; dithering is never a free lunch in terms of total noise. However, the perceptual trade is almost always worthwhile in audio: a flat noise floor is far less objectionable than harmonic distortion. Dithering trades a small, measurable SQNR penalty for a much larger perceptual quality improvement by converting tones (which our auditory system is highly sensitive to) into white noise (which is much less perceptually salient at the same power level)."

- question: "Under what conditions is treating quantization error as white noise a good approximation, and what happens to this approximation when the input signal is a pure low-frequency sinusoid at low amplitude?"
  type: short-answer
  answer: "The white-noise approximation is valid when the input signal is broadband, varies significantly from sample to sample, and uses most of the quantizer's full range. Under these conditions, the quantization errors at successive samples are approximately uncorrelated — each sample 'lands' in a different part of the step interval randomly — producing a flat error spectrum. For a pure low-frequency sinusoid at low amplitude, both conditions break: the signal is narrowband (periodic at one frequency) and may use only a few quantization levels. The error becomes periodic with the same period as the signal, producing correlated samples and tonal spectral artifacts (harmonics of the signal frequency) rather than white noise. The practical remedy is dithering — adding small broadband noise before quantization to decorrelate the error at the cost of slightly increased total noise power."
  explanation: "This is why professional audio engineers always apply dither when reducing bit depth (e.g., going from 24-bit recording to 16-bit distribution). Without dither, quiet passages in music — where the signal uses only the bottom few bits — develop audible harmonic distortion. With dither, those same passages have a clean noise floor. The white-noise approximation is an engineering model with known limits, not a physical law."
```

## Explainer

When you convert a continuous-time signal to digital, the process involves two steps: sampling in time and quantization in amplitude. From your study of continuous versus discrete signals, you know that time-sampling is governed by the Nyquist theorem. **Quantization** is the second step: the sampled amplitude, which can take any real value, must be rounded to the nearest of a finite set of discrete levels. This rounding introduces an error — the difference between the true amplitude and the quantized value — called **quantization error**. Understanding the statistical behavior of this error is essential for specifying ADC requirements in signal processing systems.

For a **uniform quantizer** with N bits, there are 2^N discrete output levels spanning the full-scale input range. The spacing between adjacent levels is the **step size** Δ = (full scale) / 2^N. Each quantized sample contains an error in the range [−Δ/2, +Δ/2]. For well-behaved signals that use the full quantizer range and don't dwell near a single level, this error is approximately **uniformly distributed** on that interval. A uniform distribution on [−Δ/2, +Δ/2] has mean zero and variance σ²_q = Δ²/12. This is the quantization **noise power** — independent of the signal, depending only on the step size and hence on the number of bits.

The **signal-to-quantization-noise ratio (SQNR)** is the ratio of signal power to noise power. For a full-scale sinusoid that uses the entire quantizer range, the derivation gives SQNR ≈ 6.02N + 1.76 dB. This is the famous **6 dB per bit rule**: each additional bit halves the step size Δ, reducing noise power by a factor of 4 (−6 dB) and raising SQNR by approximately 6 dB. An 8-bit ADC delivers about 50 dB SQNR; a 16-bit ADC about 98 dB; a 24-bit ADC roughly 146 dB. This rule is the first thing an audio engineer reaches for when specifying an ADC — CD audio uses 16 bits, professional recording uses 24 bits.

The white-noise model for quantization error has important limits. It holds when the signal is broadband, uses the full quantizer range, and changes significantly from sample to sample. When a signal is periodic relative to the step size, or barely changes between samples, the quantization error becomes correlated and can appear as tones — harmonics of the signal — in the spectrum. This is audible as **granulation noise** in audio applications. The practical remedy is **dithering**: adding a small random noise signal before quantization deliberately randomizes the error, converting structured tonal artifacts into spectrally flat noise. A small sacrifice in ideal SQNR is exchanged for a perceptually much cleaner error character — a trade that is almost always worthwhile in audio and precision measurement systems.
