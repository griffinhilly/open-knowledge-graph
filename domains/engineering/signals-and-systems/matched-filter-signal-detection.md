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
stage: expert
status: draft
---

# Matched Filter for Signal Detection

## Core Idea
The matched filter is the optimal detector for a known signal s(t) corrupted by white Gaussian noise, with impulse response h(t) = s(T–t). The output at time T equals the correlation between received signal and template, maximizing SNR at the decision point and minimizing probability of symbol error in binary hypothesis testing.

## Questions

```yaml
- question: "Why is the matched filter's impulse response h(t) = s(T−t) — a time-reversed copy of the target signal — rather than simply h(t) = s(t)?"
  type: multiple-choice
  options:
    - "Time reversal corrects for phase distortion introduced by the transmission channel"
    - "Because convolution involves time reversal, the output at time T equals the cross-correlation of the received signal with s(t), which maximizes the signal component at the decision point"
    - "The time reversal ensures causality — a non-reversed filter would require predicting future inputs"
    - "Using h(t) = s(t) would cancel the target signal rather than detect it"
  answer: 1
  explanation: "Convolution of the received signal r(t) with h(t) = s(T−t), evaluated at time T, gives y(T) = ∫r(τ)s(τ)dτ — the inner product (cross-correlation) of the received signal with the template. The time reversal in h is precisely what converts convolution into correlation at the output time T. When r(t) contains s(t), this inner product is large (signal aligns with its own template). The Cauchy-Schwarz inequality proves this inner product is maximized relative to noise when h is the time-reversed signal — which is why the matched filter is the optimal detector."

- question: "A radar system uses a 100 μs frequency-swept chirp pulse with 1 MHz bandwidth and matched filtering at the receiver. What does the matched filter achieve that a 100 μs unmodulated pulse cannot?"
  type: multiple-choice
  options:
    - "The chirp allows multiple targets to be detected simultaneously by correlating with different frequency segments"
    - "Time-bandwidth product compression — the matched filter collapses the long chirp into a sharp correlation peak of width ~1/B, achieving fine range resolution while transmitting the energy of the long pulse"
    - "The matched filter corrects for Doppler shifts introduced by moving targets before detection"
    - "Frequency sweeping prevents jamming, and the matched filter cancels the sweep to recover the original pulse shape"
  answer: 1
  explanation: "This is pulse compression. A chirp of duration T and bandwidth B has a time-bandwidth product TB = 100 μs × 1 MHz = 100. The matched filter compresses this to a correlation peak of width ~1/B, giving range resolution equivalent to a 1 μs pulse — while transmitting the energy of a 100 μs pulse. This resolves the fundamental radar tradeoff: long pulses give high energy (good SNR) but poor range resolution; short pulses give fine resolution but little energy. Matched filtering with chirp achieves both simultaneously."

- question: "The output of a matched filter at the decision time T equals the cross-correlation between the received signal and the target waveform."
  type: true-false
  answer: true
  explanation: "Convolution of r(t) with h(t) = s(T−t), evaluated at time T, gives y(T) = ∫r(τ)s(τ)dτ — the inner product of r and s, which is the cross-correlation at zero lag. This equivalence between LTI convolution with the time-reversed template and correlation is the key mathematical insight. When r contains s, the correlation is large; when r is noise with no structure matching s, the correlation fluctuates near zero. The matched filter is therefore a correlation detector implemented as an LTI system."

- question: "The matched filter achieves maximum SNR for detecting a known signal regardless of the noise characteristics, because its optimality depends only on the signal structure."
  type: true-false
  answer: false
  explanation: "The matched filter achieves maximum SNR specifically for WHITE GAUSSIAN noise — noise with equal power spectral density at all frequencies. The Cauchy-Schwarz proof of optimality assumes this white noise structure. For colored noise (non-uniform power spectrum), the optimal filter is a modified whitened matched filter that first decorrelates the noise before applying the template. The matched filter remains highly effective in practice for many noise models, but the theoretical guarantee of optimality is specific to white Gaussian noise."

- question: "Explain in your own words why the matched filter maximizes signal-to-noise ratio rather than simply maximizing signal amplitude."
  type: short-answer
  answer: "The matched filter maximizes the ratio of signal energy to noise power at the decision point, not just signal amplitude. At time T, the signal component equals the cross-correlation of the template with itself — a fixed quantity tied to the signal's energy. The noise component depends on the filter's bandwidth: a filter responding to more frequencies passes more noise power. By choosing h(t) = s(T−t), the filter weights its frequency response toward the frequencies where the signal has energy, avoiding amplification of frequencies containing only noise. The Cauchy-Schwarz inequality proves no other linear filter achieves a higher SNR — scaling the filter amplifies signal and noise equally, leaving the ratio unchanged."
  explanation: "This is why matched filtering is described as 'signal-specific projection.' It projects the received waveform onto the template, extracting the maximum possible signal component relative to noise by exploiting the known structure of the target waveform. Any other linear filter either passes frequencies where the signal is weak (reducing SNR) or rejects frequencies where the signal is strong (also reducing SNR)."
```

## Explainer

You have studied convolution as the fundamental operation of LTI systems — the output y(t) = x(t) * h(t) is completely determined by the input and the impulse response h(t). You have also seen that different choices of h(t) implement different filters: low-pass, high-pass, band-pass, and so on. The **matched filter** asks a different question: rather than designing h(t) to pass or reject frequency bands, what impulse response maximizes the probability of correctly detecting a known signal s(t) buried in noise? This question is the gateway from classical signal processing to optimal detection theory.

The answer comes from framing the problem precisely. At some decision time T, you want the filter output to have the signal component as large as possible relative to the noise component — that is, you want to maximize the **signal-to-noise ratio (SNR)** at time T. Using the Cauchy-Schwarz inequality, one can show that for white Gaussian noise (noise with equal power at all frequencies), the filter that achieves maximum SNR has impulse response h(t) = s(T − t). This is a time-reversed, delayed copy of the target signal — the filter is "matched" to the specific waveform you are trying to detect, hence the name.

The physical intuition is that the matched filter computes a **cross-correlation** between the received signal and the known template. Convolution with h(t) = s(T − t) evaluated at time T gives y(T) = ∫ r(τ) s(τ) dτ — the inner product of the received signal r(t) with the template s(t). When r(t) actually contains s(t), this inner product is large: the signal aligns with its own template, producing a large peak. When r(t) is pure noise, the inner product fluctuates near zero because noise has no structure that correlates with the template. The matched filter is essentially a signal-specific projection that separates structured signal from unstructured noise as effectively as any linear filter can.

This principle extends across virtually every domain that requires detecting a known signal in noise. In binary digital communications, the optimal receiver computes the correlation of the received waveform with each symbol template and selects the larger — this achieves the minimum possible bit error rate (the matched filter bound). In **radar**, the transmitted pulse is matched-filtered in the receiver to detect echoes from targets: using a frequency-swept "chirp" pulse of duration T and bandwidth B gives a time-bandwidth product TB as a compression gain, collapsing a long pulse into a sharp peak with TB× improvement in range resolution and SNR. A 1 ms chirp at 10 MHz bandwidth achieves TB = 10,000 — resolving targets that an unmatched receiver could not distinguish from noise. In sonar and medical ultrasound, the same principle applies. The matched filter is not one technique among many — it is the theoretical optimum for detecting known signals in white noise, against which all other detection strategies are benchmarked.
