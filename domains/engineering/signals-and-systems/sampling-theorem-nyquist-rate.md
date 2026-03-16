---
id: sampling-theorem-nyquist-rate
title: Sampling Theorem and Nyquist Sampling Rate
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
- id: fourier-transform-definition-properties
  type: hard
builds-toward:
- aliasing-reconstruction-signals
- dft-and-fft-algorithms
tags:
- sampling
- nyquist
- discrete-time
stage: advanced
status: draft
---

# Sampling Theorem and Nyquist Sampling Rate

## Core Idea
The Nyquist sampling theorem states that a bandlimited signal with maximum frequency f_max must be sampled at f_s ≥ 2·f_max to avoid losing information. If this condition is violated, aliasing—overlap of frequency components—corrupts the discrete signal and makes reconstruction impossible.

## Explainer

From your work with the Fourier transform, you know that any signal can be decomposed into sinusoidal components at specific frequencies. A **bandlimited signal** is one where all energy is confined to frequencies below some maximum value f_max — there are no components above that cutoff. The Nyquist theorem is a statement about what it takes to perfectly capture that signal in a sequence of discrete samples.

Here is the core intuition. When you sample a continuous signal at rate f_s, you are essentially multiplying it by a train of impulses spaced 1/f_s apart in time. In the frequency domain (recall from your Fourier transform prerequisite), multiplication in time corresponds to convolution with another impulse train — one spaced f_s apart in frequency. This creates **copies** of the original spectrum centered at every multiple of f_s. If f_s ≥ 2·f_max, those copies are spaced far enough apart that they don't overlap, and a lowpass filter can cleanly isolate the original spectrum, perfectly reconstructing the signal. If f_s < 2·f_max, the copies overlap — this is **aliasing**.

Aliasing is irreversible: once the frequency images overlap, you cannot tell which contribution came from the original signal and which from the copy. A concrete example: suppose you have a 3 kHz tone and sample at 5 kHz. The copy centered at 5 kHz places an image at 5 − 3 = 2 kHz, which lands right inside your signal band. Your reconstructed signal will contain a spurious 2 kHz tone that was never present in the original. The **Nyquist rate** 2·f_max is the minimum sampling frequency that prevents this — in practice, engineers sample at higher rates and use analog **anti-aliasing filters** before sampling to ensure no energy remains above f_s/2, the **Nyquist frequency**.

The theorem has a powerful converse: if the Nyquist criterion is met, the original continuous signal can be recovered *exactly* from its samples using ideal sinc interpolation. This is the bridge between your two prerequisite concepts — the discrete-time samples you classified earlier and the Fourier representation of continuous signals. Sampling is not an approximation; it is a lossless representation when the bandwidth condition is satisfied.

Understanding the Nyquist rate is the foundation for everything that comes next in digital signal processing. The DFT and FFT you'll encounter later operate on finite blocks of samples, and aliasing issues re-emerge at the block boundary. Reconstruction filters, audio codecs, communications systems, and medical imaging all depend on correctly honoring the Nyquist condition — or deliberately exploiting its violation in techniques like undersampling of narrowband signals centered at high frequencies.
