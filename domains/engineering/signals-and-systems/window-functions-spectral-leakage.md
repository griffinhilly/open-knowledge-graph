---
id: window-functions-spectral-leakage
title: Window Functions and Spectral Leakage
domain: engineering
course: signals-and-systems
prerequisites:
- id: dft-and-fft-algorithms
  type: hard
- id: fourier-transform-definition-properties
  type: hard
builds-toward:
- power-spectral-density-estimation
- digital-spectral-analysis-nonparametric
tags:
- windowing
- spectral-analysis
- dft
- frequency-domain
stage: advanced
status: draft
---

# Window Functions and Spectral Leakage

## Core Idea
Spectral leakage occurs when analyzing finite-length signals with the DFT because the signal is not periodic within the window. Window functions taper the signal at the edges to reduce leakage at the cost of broader mainlobes. Common windows (Hann, Hamming, Blackman, Kaiser) trade off mainlobe width and sidelobe attenuation, making the choice critical for spectral accuracy.

## Questions

```yaml
- question: "A signal contains two tones: one at 100 Hz with amplitude 1.0, and another at 102 Hz with amplitude 0.001 (60 dB weaker). With a rectangular window, the weak tone is buried under sidelobes from the strong one. What window property do you need to detect the weaker tone?"
  type: multiple-choice
  options:
    - "A wider mainlobe to better resolve the 2 Hz separation"
    - "Lower sidelobes to suppress contamination from the 100 Hz tone, even at the cost of broader mainlobe"
    - "A higher sampling rate to increase the DFT's frequency resolution"
    - "A longer record length to reduce the mainlobe width below 2 Hz"
  answer: 1
  explanation: "When the goal is detecting a weak signal near a strong one, sidelobe attenuation is the critical property. The rectangular window has sidelobes at only −13 dB — the strong 100 Hz tone contaminates neighboring bins at 1/5 of its amplitude, easily burying a tone 60 dB weaker. A window with low sidelobes (e.g., Blackman at −58 dB, or a Kaiser window tuned to ≥60 dB) suppresses this contamination. The cost is a wider mainlobe (poorer frequency resolution), but that tradeoff is acceptable here since you need dynamic range, not close-frequency separation."

- question: "Why does a pure sinusoid at a non-integer bin frequency produce spectral leakage in the DFT, even though it is a single-frequency signal?"
  type: multiple-choice
  options:
    - "The DFT cannot represent sinusoids; it can only represent sums of cosines"
    - "The DFT implicitly tiles the finite record, creating a discontinuity at the boundary when the sinusoid does not complete an integer number of cycles in the window"
    - "Non-integer frequencies fall between DFT bins, causing the DFT to interpolate inaccurately"
    - "Leakage occurs only for complex exponentials, not real sinusoids"
  answer: 1
  explanation: "The DFT treats the N samples as one period of a periodic signal — it implicitly tiles the record. If a sinusoid completes 5.3 cycles in the window, the tiled signal has a phase jump at every period boundary: the end of one period does not match the beginning of the next. This discontinuity contains energy at all frequencies, so it contaminates every spectral bin — spectral leakage. A sinusoid at exactly bin 5 (an integer number of cycles) has no jump and produces energy at only one bin. Leakage is entirely about the assumed periodicity of the DFT, not about the sinusoid being non-sinusoidal."

- question: "Applying a Hann window to a signal eliminates spectral leakage by preventing signal energy from spreading to other frequency bins."
  type: true-false
  answer: false
  explanation: "Window functions reduce leakage but do not eliminate it. Any finite-length analysis produces some spectral smearing because the window's frequency-domain representation always has nonzero values at frequencies other than DC. What window functions do is shape this smearing: a good window concentrates energy near the mainlobe and suppresses sidelobes, reducing contamination at distant bins without eliminating it entirely. The Hann window drops sidelobes to −31 dB versus the rectangular window's −13 dB — a major improvement. Complete elimination of leakage would require an infinitely long analysis window."

- question: "Using a window with lower sidelobes always reduces your ability to resolve two closely spaced frequency components."
  type: true-false
  answer: true
  explanation: "This is the fundamental tradeoff in window design: sidelobe attenuation and mainlobe width are inversely related. A rectangular window has a narrow mainlobe (1/N resolution) but high sidelobes (−13 dB). A Blackman window suppresses sidelobes to −58 dB but widens the mainlobe to about 3/N — signals must be separated by 3/N rather than 1/N to be resolved. The Kaiser window parameterizes this tradeoff continuously via β, letting you choose where to operate, but cannot escape the tradeoff itself. Resolving close frequencies and detecting weak signals near strong ones are competing requirements."

- question: "Explain why computing the DFT of a finite signal segment is mathematically equivalent to multiplying by a rectangular window, and why this causes spectral leakage."
  type: short-answer
  answer: "A finite signal segment of length N is equivalent to multiplying the infinite signal by a rectangular pulse: 1 for samples 0 to N−1, 0 elsewhere. By the convolution theorem, multiplication in time equals convolution in frequency. So the DFT output is the convolution of the true spectrum with the Fourier transform of the rectangular window (a sinc-like function with a narrow mainlobe and slowly decaying sidelobes at −13 dB). This convolution spreads energy from each true frequency component across neighboring bins — spectral leakage. A tone at a non-integer bin has its energy convolved with this sinc, smearing it across all bins."
  explanation: "This perspective — finite duration equals rectangular window equals frequency-domain convolution — shows why leakage is fundamental, not incidental. All other window functions replace the rectangular window with one whose frequency-domain representation has better sidelobe properties, accepting a wider mainlobe in exchange. The goal is always to shape the convolution kernel, not to eliminate it."
```

## Explainer

The DFT assumes the N samples you provide represent one complete period of a periodic signal. When you compute the N-point DFT, you are implicitly tiling the signal — pretending the N samples repeat forever. If the signal contains a frequency that does not fit an integer number of cycles within your window, the signal's value jumps discontinuously at the boundary between repetitions. That jump has energy at all frequencies, so it contaminates every spectral bin — this is **spectral leakage**. A pure sinusoid at exactly bin 5 produces energy only at bin 5; a sinusoid at frequency 5.3 (not a whole number of cycles in the window) smears its energy across all N bins.

This connects directly to what you learned about the Fourier transform and the DFT. Computing the N-point DFT of a finite segment of a signal is mathematically equivalent to multiplying the infinite signal by a rectangular pulse of width N, then transforming. In the frequency domain, multiplication becomes convolution: the DFT output is the convolution of the true spectrum with the Fourier transform of the rectangular window. The rectangular window's spectrum is a sinc-like function with a narrow mainlobe but **sidelobes** at only −13 dB below the peak — meaning a strong frequency can contaminate neighboring bins at 1/5 of its amplitude. The sidelobes fall off slowly, so leakage from a strong tone can bury a nearby weak tone.

The solution is a **window function**: taper the signal to zero at both edges before computing the DFT. A Hann window multiplies each sample n by w(n) = 0.5(1 − cos(2πn/N)), smoothly reaching zero at n = 0 and n = N−1. This eliminates the edge discontinuity. The cost is that the window's frequency-domain representation has a wider mainlobe — instead of resolving frequencies that differ by 1/N, you now need a separation of roughly 2/N. But the sidelobes drop to −31 dB, dramatically reducing the contamination. A Blackman window achieves −58 dB sidelobes at the cost of a 3/N mainlobe width.

The **Kaiser window** makes this tradeoff continuous via a parameter β: β = 0 gives a rectangular window, and increasing β widens the mainlobe while suppressing sidelobes. This lets you design the window to meet a specification — if you need to detect a signal 40 dB weaker than a nearby tone, choose β to give ≥40 dB sidelobe attenuation, then accept the resulting resolution loss. The design question is always: do you need to *resolve* close frequencies (want narrow mainlobe, tolerate sidelobes) or *detect* weak signals near strong ones (want low sidelobes, tolerate wider mainlobe)? These requirements pull in opposite directions, and no window satisfies both simultaneously.
