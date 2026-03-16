---
id: short-time-fourier-transform
title: Short-Time Fourier Transform
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
- id: window-functions-spectral-leakage
  type: soft
builds-toward:
- wavelet-transform-analysis
tags:
- time-frequency
- stft
- spectral-analysis
- windows
stage: advanced
status: draft
---

# Short-Time Fourier Transform

## Core Idea
The Short-Time Fourier Transform (STFT) computes Fourier transform of overlapping windowed segments to provide time-frequency representation: STFT(t,ω) = ∫ x(τ)·w(τ–t)·e^(–jωτ) dτ. It trades time and frequency resolution: narrower windows improve time localization but worsen frequency resolution. Spectrograms visualize STFT magnitude showing frequency evolution over time.

## Explainer

The standard Fourier transform is like asking, "what frequencies are present in this signal?" — and getting a complete answer, but with no information about *when* those frequencies occur. For a piece of music, the ordinary Fourier transform tells you every note ever played, but nothing about their order or timing. The **Short-Time Fourier Transform (STFT)** solves this by asking a more local question: what frequencies are present *right now*, in this short window of time?

The idea is simple: multiply the signal by a **window function** — a smooth, localized pulse like a Gaussian or Hann window — that is zero everywhere except near some moment t. Then take the Fourier transform of what remains. This gives the frequency content of the signal near time t. By sliding the window across the entire signal and repeating, you get a two-dimensional map of frequency vs. time. This map is the STFT, and its magnitude squared is the **spectrogram** — the colored time-frequency plots you see in audio analysis and speech processing.

The catch is the **time-frequency uncertainty principle** (analogous to the Heisenberg uncertainty principle in quantum mechanics): you cannot have arbitrarily sharp resolution in both time and frequency simultaneously. A narrow window gives excellent time localization — you know precisely *when* a frequency appears — but the short duration means the Fourier transform sees very few oscillations, leading to smeared frequency content. A wide window gives sharp frequency peaks (many oscillations to count) but blurs together events that happen at different times. Formally, the product of time resolution Δt and frequency resolution Δω is bounded below: Δt · Δω ≥ 1/2.

This resolution tradeoff is the fundamental limitation of the STFT and motivates its successor, the **wavelet transform**. Unlike the STFT — where every frequency is analyzed with the same fixed window width — wavelets use a window that automatically shrinks at high frequencies and widens at low ones. This provides constant *relative* resolution (high frequencies resolved in time, low frequencies resolved in pitch), which is why wavelets are preferred for signals like speech and ECG where low-frequency content evolves slowly and high-frequency transients are brief. Understanding the STFT's fixed-resolution limitation is the conceptual bridge to that more flexible framework.
