---
id: matched-filter-signal-detection
title: Matched Filter for Signal Detection
domain: engineering
course: signals-and-systems
prerequisites:
- id: convolution-continuous-discrete-systems
  type: hard
- id: lti-systems-and-impulse-response
  type: hard
builds-toward:
- nyquist-criterion-intersymbol-interference
tags:
- filtering
- signal-detection
- optimal-filtering
- correlation
stage: advanced
status: draft
---

# Matched Filter for Signal Detection

## Core Idea
The matched filter is the optimal detector for a known signal s(t) corrupted by white Gaussian noise, with impulse response h(t) = s(T–t). The output at time T equals the correlation between received signal and template, maximizing SNR at the decision point and minimizing probability of symbol error in binary hypothesis testing.

## Explainer

You have studied convolution as the fundamental operation of LTI systems — the output y(t) = x(t) * h(t) is completely determined by the input and the impulse response h(t). You have also seen that different choices of h(t) implement different filters: low-pass, high-pass, band-pass, and so on. The **matched filter** asks a different question: rather than designing h(t) to pass or reject frequency bands, what impulse response maximizes the probability of correctly detecting a known signal s(t) buried in noise? This question is the gateway from classical signal processing to optimal detection theory.

The answer comes from framing the problem precisely. At some decision time T, you want the filter output to have the signal component as large as possible relative to the noise component — that is, you want to maximize the **signal-to-noise ratio (SNR)** at time T. Using the Cauchy-Schwarz inequality, one can show that for white Gaussian noise (noise with equal power at all frequencies), the filter that achieves maximum SNR has impulse response h(t) = s(T − t). This is a time-reversed, delayed copy of the target signal — the filter is "matched" to the specific waveform you are trying to detect, hence the name.

The physical intuition is that the matched filter computes a **cross-correlation** between the received signal and the known template. Convolution with h(t) = s(T − t) evaluated at time T gives y(T) = ∫ r(τ) s(τ) dτ — the inner product of the received signal r(t) with the template s(t). When r(t) actually contains s(t), this inner product is large: the signal aligns with its own template, producing a large peak. When r(t) is pure noise, the inner product fluctuates near zero because noise has no structure that correlates with the template. The matched filter is essentially a signal-specific projection that separates structured signal from unstructured noise as effectively as any linear filter can.

This principle extends across virtually every domain that requires detecting a known signal in noise. In binary digital communications, the optimal receiver computes the correlation of the received waveform with each symbol template and selects the larger — this achieves the minimum possible bit error rate (the matched filter bound). In **radar**, the transmitted pulse is matched-filtered in the receiver to detect echoes from targets: using a frequency-swept "chirp" pulse of duration T and bandwidth B gives a time-bandwidth product TB as a compression gain, collapsing a long pulse into a sharp peak with TB× improvement in range resolution and SNR. A 1 ms chirp at 10 MHz bandwidth achieves TB = 10,000 — resolving targets that an unmatched receiver could not distinguish from noise. In sonar and medical ultrasound, the same principle applies. The matched filter is not one technique among many — it is the theoretical optimum for detecting known signals in white noise, against which all other detection strategies are benchmarked.
