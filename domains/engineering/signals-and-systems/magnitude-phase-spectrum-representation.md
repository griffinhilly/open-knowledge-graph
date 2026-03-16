---
id: magnitude-phase-spectrum-representation
title: Magnitude and Phase Spectrum Representation
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
builds-toward:
- frequency-response-magnitude-phase
- bode-plot-construction-interpretation
tags:
- spectrum
- magnitude
- phase
- frequency-domain
stage: advanced
status: draft
---

# Magnitude and Phase Spectrum Representation

## Core Idea
The Fourier transform X(f) = |X(f)|e^(jφ(f)) can be represented as magnitude |X(f)| and phase φ(f). The magnitude spectrum shows the amplitude of frequency components; the phase spectrum shows their relative timing. Both are necessary to fully reconstruct the signal.

## Explainer

From the Fourier transform, you know that X(f) = ∫x(t)e^(−j2πft)dt produces a complex number for each frequency f. A complex number carries two independent pieces of information, and there are two natural ways to express them: rectangular form (real part + imaginary part) or polar form (magnitude × phase). The **magnitude spectrum** |X(f)| and **phase spectrum** φ(f) = ∠X(f) are the polar decomposition — and they answer two fundamentally different questions about the signal's frequency content.

The magnitude spectrum answers: "how much of frequency f is present?" A pure sinusoid at frequency f₀ has a magnitude spectrum with a single spike at f₀ (and at −f₀ for a real signal). A signal containing three different sinusoidal components has three spikes, each with a height proportional to the component's amplitude. The magnitude spectrum is the intuitive, visual summary of "what frequencies are in this signal." The **phase spectrum** answers a subtler question: "at what point in its cycle does the component at frequency f start, relative to t = 0?" A cosine at f₀ has zero phase; the same cosine delayed by half a period has a phase of π. The same content, different timing.

An illuminating analogy: imagine analyzing a symphony recording. The magnitude spectrum tells you how loud each frequency (each pitch) is at a given moment — essentially what the instruments are playing and at what volume. The phase spectrum tells you how those pitches are synchronized to each other and to the reference time. If you randomly scramble all the phase values while keeping every magnitude unchanged, the resulting audio sounds like broadband noise: all the "right" pitches are present at the "right" loudness levels, but their timing relationships are completely destroyed. Phase encodes the temporal structure of the signal, and destroying it destroys intelligibility.

Computing the two spectra is straightforward. For a complex spectrum X(f) = R(f) + jI(f), the magnitude is |X(f)| = √(R² + I²) and the phase is φ(f) = arctan2(I, R). For real-valued signals, the spectrum is **Hermitian symmetric**: |X(−f)| = |X(f)| and φ(−f) = −φ(f). The magnitude spectrum is an even function of frequency; the phase spectrum is an odd function. This means you only need to plot positive frequencies to convey all the information. A key special case: a **pure time delay** of t₀ seconds leaves the magnitude spectrum completely unchanged while shifting every phase value by exactly −2πft₀. This is one of the most important Fourier transform properties in applications — it means you can identify time shifts between signals by comparing their phase spectra.

These concepts connect directly to system analysis. The frequency response H(f) of any linear time-invariant system is also complex, with a magnitude response |H(f)| (the gain at each frequency) and a phase response φ_H(f) (the delay at each frequency). **Bode plots** — which you will encounter next — are simply magnitude and phase spectra of H(f) plotted on a logarithmic frequency axis: the magnitude in decibels (20 log₁₀|H(f)|) and the phase in degrees. Every intuition built here about signal spectra transfers directly to understanding how systems shape signals in the frequency domain.
