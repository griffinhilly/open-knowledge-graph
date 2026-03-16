---
id: dithering-techniques-quantization-improvement
title: Dithering Techniques and Quantization Noise Shaping
domain: engineering
course: signals-and-systems
prerequisites:
- id: quantization-error-and-noise-analysis
  type: hard
builds-toward:
- anti-aliasing-filters-pre-sampling-design
- reconstruction-filters-post-interpolation-design
tags:
- dithering
- quantization
- noise-shaping
- resolution
stage: formal-systems
status: draft
---

# Dithering Techniques and Quantization Noise Shaping

## Core Idea
Dithering adds small random noise before quantization to randomize quantization error, converting correlated (colored) error into white noise. This prevents patterns, banding, and harmonic distortion but at the cost of slightly increased noise floor. Noise-shaping dithering distributes quantization error toward frequencies where it's less perceptible (e.g., high frequencies for audio). Delta-sigma modulation uses noise-shaping to achieve high effective resolution from low-bit quantizers.

## How It's Best Learned
Quantize a low-amplitude sinusoid with and without dithering. Observe that dithering eliminates distortion at the cost of white noise. Compare frequency spectrum before and after dithering.

## Common Misconceptions
- Thinking dithering always improves SNR (it trades distortion for noise).
- Assuming all dithering is equivalent (subtractive dithering differs from noise-shaping).
- Not recognizing perceptual benefits beyond SNR improvement.

## Explainer

From your study of quantization error, you know that a uniform N-bit quantizer maps a continuous range into 2^N discrete levels, and the rounding error at each sample lies between −LSB/2 and +LSB/2, giving a theoretical signal-to-quantization-noise ratio (SQNR) of about 6.02N + 1.76 dB. This formula assumes quantization error is **white noise** — uniform, uncorrelated, and independent of the input signal. That assumption holds when the signal is large and changing rapidly enough to "visit" many quantization levels. But when a signal is small relative to the step size — as in a quiet passage of audio or a slow-moving sensor reading — the signal moves through only a few levels, and the quantization error becomes deterministically correlated with the input. The result is not white noise but **harmonic distortion**: spurious tones at harmonics of the signal frequency that are audible even when they are far below the noise floor.

**Dithering** breaks this correlation by adding a small random signal to the input *before* quantization. The random noise ensures the quantizer input is constantly fluctuating through the decision boundaries, so the output toggles between adjacent levels even when the true signal is nearly constant. The quantization error that results is now randomized — it is genuinely white noise rather than a deterministic function of the signal. You can think of it as intentionally "confusing" the quantizer so that it cannot develop any periodic relationship with the input. The cost is that you have increased the noise floor slightly (you added noise); the benefit is that you have eliminated distortion. For applications where the noise floor is not the binding constraint — especially perceptual ones like audio — this trade is strongly favorable. A faint musical note buried in white noise is audible; the same note corrupted by harmonic distortion is not.

**Noise shaping** is a further refinement that recovers some of the cost. Instead of adding flat white dither, noise-shaping feeds the quantization error back through a filter and subtracts the filtered error from the input of the next quantization step. This creates a feedback loop that pushes quantization error toward frequencies where it is less perceptible — above 15 kHz for audio, for example. The total noise power is unchanged (energy is conserved), but it is redistributed: lower in the perceptually important band, higher where it doesn't matter. A **delta-sigma (ΔΣ) modulator** implements this principle aggressively: it uses a 1-bit or low-resolution quantizer running at a very high sample rate, with noise-shaped feedback, then a digital low-pass filter decimates the output. The effective resolution in the audio band can reach 20–24 bits from a 1-bit quantizer because almost all the quantization noise has been pushed above the filter cutoff. This is how modern high-resolution audio DACs and ADCs achieve their specifications without impractical multi-bit precision at high speeds.


