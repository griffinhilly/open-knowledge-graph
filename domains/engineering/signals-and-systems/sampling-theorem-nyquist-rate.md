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
stage: expert
status: validated
---

# Sampling Theorem and Nyquist Sampling Rate

## Core Idea
The Nyquist sampling theorem states that a bandlimited signal with maximum frequency f_max must be sampled at f_s ≥ 2·f_max to avoid losing information. If this condition is violated, aliasing—overlap of frequency components—corrupts the discrete signal and makes reconstruction impossible.

## Questions

```yaml
- question: "A signal contains frequency components up to 4 kHz and is sampled at 6 kHz. What happens?"
  type: multiple-choice
  options:
    - "The signal is reconstructed perfectly — 6 kHz is above 4 kHz so the Nyquist condition is satisfied"
    - "Aliasing occurs because the sampling rate (6 kHz) is below the required Nyquist rate (2 × 4 kHz = 8 kHz)"
    - "The signal is slightly degraded but recoverable with a good lowpass filter applied after sampling"
    - "There is no problem as long as a high-resolution analog-to-digital converter is used"
  answer: 1
  explanation: "The Nyquist theorem requires f_s ≥ 2 × f_max — the sampling rate must be at least twice the highest frequency in the signal. Here f_max = 4 kHz requires f_s ≥ 8 kHz; sampling at 6 kHz violates this. The spectral copies created by sampling will overlap (alias), corrupting the signal. The common mistake is comparing f_s to f_max directly (6 > 4 looks fine) rather than to 2 × f_max. Option C is also wrong — once aliasing has occurred, it cannot be undone by post-sampling filtering."

- question: "A 3 kHz tone is sampled at 5 kHz, causing aliasing. After sampling, which of the following is true?"
  type: multiple-choice
  options:
    - "A high-quality lowpass filter applied to the sampled data can recover the original 3 kHz tone"
    - "The aliasing only affects frequencies above 2.5 kHz, so the lower portion of the signal is intact"
    - "The aliased image at 5 − 3 = 2 kHz is indistinguishable from an original 2 kHz component, making perfect recovery impossible"
    - "The original signal can be recovered if the sampling rate was only slightly below the Nyquist rate"
  answer: 2
  explanation: "Aliasing is irreversible. When f_s = 5 kHz and a 3 kHz tone is present, the spectral copy centered at 5 kHz places an image at 5 − 3 = 2 kHz — right inside the signal band. The sampled signal now contains energy at 2 kHz, but you cannot tell whether it originated from an actual 2 kHz component or from the aliased 3 kHz component. No post-processing can distinguish the two contributions. This is why anti-aliasing filters must be applied *before* sampling — once aliasing occurs, the information is permanently corrupted."

- question: "If a bandlimited signal is sampled at exactly the Nyquist rate (f_s = 2 × f_max), the original continuous signal can theoretically be recovered exactly from its discrete samples using ideal sinc interpolation."
  type: true-false
  answer: true
  explanation: "This is the positive result of the Nyquist-Shannon sampling theorem. When the sampling criterion is met, sampling is not an approximation — it is a lossless representation. The spectral copies created by sampling are spaced far enough apart that they don't overlap, and an ideal lowpass filter (or equivalently, sinc interpolation in the time domain) can perfectly reconstruct the original signal. This bridges discrete-time and continuous-time representations without any information loss."

- question: "Sampling a continuous signal inevitably introduces some information loss, regardless of how high the sampling rate is, because continuous signals have infinite resolution."
  type: true-false
  answer: false
  explanation: "This is a fundamental misconception. For bandlimited signals, the Nyquist theorem guarantees that sampling above the Nyquist rate is perfectly lossless — the original continuous signal can be exactly recovered. The key condition is bandlimiting: if all energy is confined below f_max and you sample at f_s ≥ 2 × f_max, no information is lost. Sampling is not an approximation; it is a lossless change of representation when the bandwidth condition is satisfied. (Truly infinite-bandwidth signals cannot be sampled without loss, but practical signals are always bandlimited.)"

- question: "Why must an anti-aliasing filter be applied to a signal *before* sampling rather than after, and what does this tell us about the reversibility of aliasing?"
  type: short-answer
  answer: "An anti-aliasing filter removes frequency components above f_s/2 (the Nyquist frequency) before sampling, ensuring no energy exists that could alias. It must come before sampling because aliasing is irreversible: once spectral copies overlap in the sampled signal, the aliased components are mixed with original signal components and cannot be separated. Applying a filter after sampling cannot undo this — you would be filtering both the original signal and the aliased imposters together. The pre-sampling filter prevents the problem from occurring at all."
  explanation: "This reveals that aliasing is not noise that can be cleaned up later — it is a fundamental loss of information structure. The overlapping copies create ambiguity about which energy came from where, and ambiguity cannot be resolved by filtering alone. Anti-aliasing filters are therefore part of the correct system design, not an afterthought."
```

## Explainer

From your work with the Fourier transform, you know that any signal can be decomposed into sinusoidal components at specific frequencies. A **bandlimited signal** is one where all energy is confined to frequencies below some maximum value f_max — there are no components above that cutoff. The Nyquist theorem is a statement about what it takes to perfectly capture that signal in a sequence of discrete samples.

Here is the core intuition. When you sample a continuous signal at rate f_s, you are essentially multiplying it by a train of impulses spaced 1/f_s apart in time. In the frequency domain (recall from your Fourier transform prerequisite), multiplication in time corresponds to convolution with another impulse train — one spaced f_s apart in frequency. This creates **copies** of the original spectrum centered at every multiple of f_s. If f_s ≥ 2·f_max, those copies are spaced far enough apart that they don't overlap, and a lowpass filter can cleanly isolate the original spectrum, perfectly reconstructing the signal. If f_s < 2·f_max, the copies overlap — this is **aliasing**.

Aliasing is irreversible: once the frequency images overlap, you cannot tell which contribution came from the original signal and which from the copy. A concrete example: suppose you have a 3 kHz tone and sample at 5 kHz. The copy centered at 5 kHz places an image at 5 − 3 = 2 kHz, which lands right inside your signal band. Your reconstructed signal will contain a spurious 2 kHz tone that was never present in the original. The **Nyquist rate** 2·f_max is the minimum sampling frequency that prevents this — in practice, engineers sample at higher rates and use analog **anti-aliasing filters** before sampling to ensure no energy remains above f_s/2, the **Nyquist frequency**.

The theorem has a powerful converse: if the Nyquist criterion is met, the original continuous signal can be recovered *exactly* from its samples using ideal sinc interpolation. This is the bridge between your two prerequisite concepts — the discrete-time samples you classified earlier and the Fourier representation of continuous signals. Sampling is not an approximation; it is a lossless representation when the bandwidth condition is satisfied.

Understanding the Nyquist rate is the foundation for everything that comes next in digital signal processing. The DFT and FFT you'll encounter later operate on finite blocks of samples, and aliasing issues re-emerge at the block boundary. Reconstruction filters, audio codecs, communications systems, and medical imaging all depend on correctly honoring the Nyquist condition — or deliberately exploiting its violation in techniques like undersampling of narrowband signals centered at high frequencies.
