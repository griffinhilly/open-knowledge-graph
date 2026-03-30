---
id: parseval-theorem-energy-analysis
title: Parseval's Theorem and Energy/Power Spectral Density
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
- id: signal-properties-periodicity-energy-power
  type: hard
builds-toward:
- random-signals-autocorrelation-psd
tags:
- parseval
- energy
- spectral-density
stage: advanced
status: validated
---

# Parseval's Theorem and Energy/Power Spectral Density

## Core Idea
Parseval's theorem states that the total energy of a signal is the same whether computed in time or frequency: ∫|x(t)|² dt = ∫|X(f)|² df. The energy spectral density |X(f)|² shows how energy is distributed across frequencies.

## Questions

```yaml
- question: "A filter has |H(f)|² = 0.25 uniformly across 100–200 Hz and zero elsewhere. The input signal has energy spectral density |X(f)|² = 10 J/Hz uniformly across 100–200 Hz and zero elsewhere. What fraction of the input energy appears at the output?"
  type: multiple-choice
  options:
    - "25% — because |H(f)|² = 0.25 means the filter passes 25% of the input energy in that band"
    - "50% — because |H(f)| = 0.5 and the filter passes 50% of the signal amplitude"
    - "100% — because the entire 100–200 Hz band passes through the filter"
    - "6.25% — because we must square the 0.25 fraction again when computing energy"
  answer: 0
  explanation: "By Parseval's theorem, output energy = ∫|H(f)|²·|X(f)|² df. In the band 100–200 Hz, |H(f)|²·|X(f)|² = 0.25 × 10 = 2.5 J/Hz. Total output energy = 2.5 × 100 Hz = 250 J. Input energy = 10 × 100 = 1000 J. The fraction is 250/1000 = 25%. The key is that energy scales as |H(f)|² (power/magnitude-squared), not |H(f)|. Option B makes the classic error of using magnitude instead of magnitude-squared for energy calculations."

- question: "A student computes |H(f)| = 0.7 at a frequency of interest and concludes the filter passes 70% of the signal energy at that frequency. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — the magnitude of the frequency response directly gives the fraction of energy passed at each frequency"
    - "No — energy scales as |H(f)|² = 0.49, so the filter passes only 49% of the energy at that frequency"
    - "No — the student should use the phase of H(f), not the magnitude, for energy calculations"
    - "Yes, because Parseval's theorem states that a filter preserves total signal energy"
  answer: 1
  explanation: "Energy (and power) scale as the square of amplitude. If the magnitude response is |H(f)| = 0.7, the output amplitude at frequency f is 0.7 times the input amplitude, but the output energy density is |H(f)|² = 0.49 times the input energy density. This factor of two matters enormously in filter design: a filter specified as '–3 dB at cutoff' has |H(f)|² = 0.5 (half power), which corresponds to |H(f)| = 0.707, not 0.5. Option D is also wrong: Parseval's theorem says total energy is preserved by the Fourier transform, not by filtering."

- question: "The total energy of a signal computed in the time domain equals the total energy computed in the frequency domain."
  type: true-false
  answer: true
  explanation: "This is exactly Parseval's theorem: ∫|x(t)|² dt = ∫|X(f)|² df. The Fourier transform is a change of representation — it decomposes the signal into frequency components but does not alter the signal's total energy content. Just as rotating a coordinate system changes a vector's components but not its length, the Fourier transform changes how energy is distributed across the representation but preserves the total. This is why |X(f)|² is called energy spectral density — its integral equals the total energy."

- question: "Applying the Fourier transform to a signal changes the signal's total energy."
  type: true-false
  answer: false
  explanation: "The Fourier transform is a lossless change of representation — a bijection between time-domain and frequency-domain descriptions of the same signal. It does not add or remove energy; it re-expresses the same energy in a different basis. Parseval's theorem is the formal statement of this conservation: the L² norm is preserved under the Fourier transform. If the Fourier transform changed energy, it would not be a faithful representation of the original signal."

- question: "How does Parseval's theorem make filter analysis more practical? What can you calculate without ever computing the filtered time-domain signal?"
  type: short-answer
  answer: "Parseval's theorem lets you compute output energy (or power) entirely in the frequency domain, without ever performing an inverse Fourier transform. When a signal passes through a filter, the output spectrum is Y(f) = H(f)·X(f), so the output energy spectral density is |Y(f)|² = |H(f)|²·|X(f)|². The total output energy is ∫|H(f)|²·|X(f)|² df, and the energy in any specific frequency band is ∫_band |H(f)|²·|X(f)|² df. This means you can determine exactly how much energy a filter passes or rejects in any band — and verify that a filter design meets specifications — using only the frequency-domain representations, without computing the time-domain output. Filter specs are defined in terms of |H(f)|² (e.g., –3 dB cutoff, –40 dB stopband attenuation) for precisely this reason."
  explanation: "The practical value is computational and conceptual: frequency-domain energy analysis lets you reason about filtering effects directly from the spectra. You can ask 'how much noise (specified by its PSD) does this filter remove?' and get an exact answer without simulating the filtered output in time."
```

## Explainer

From the Fourier transform, you know that a signal can be decomposed into sinusoidal components, with X(f) telling you the amplitude and phase of each frequency component. The Fourier transform is a change of representation — the same signal, viewed through a different lens. Parseval's theorem is a statement that this change of lens conserves something important: energy. Just as rotating a 3D coordinate system changes the components of a vector but not its length, the Fourier transform changes how a signal is represented but not its total energy content.

The theorem ∫|x(t)|² dt = ∫|X(f)|² df has a straightforward interpretation. The left side is the total signal energy computed in the time domain: you square the instantaneous amplitude at every moment and integrate. The right side computes the same total by squaring the magnitude of each frequency component and summing across all frequencies. The two must be equal because both are computing the same physical quantity — just from different vantage points. The quantity |X(f)|² is the **energy spectral density**: it tells you how much energy is concentrated in each narrow band of frequencies. A pure sinusoid concentrates all its energy at a single frequency; a short pulse spreads energy broadly across many frequencies; a bandlimited signal has |X(f)|² = 0 outside some frequency range.

For **power signals** — periodic or stationary random signals that have infinite energy but finite average power — the analogous result involves the **power spectral density** (PSD). The total average power equals the integral of the PSD over all frequencies. This extension is especially important in communications and signal processing, where you care not just about whether a signal has finite energy, but about how its power is distributed across the spectrum (is the noise concentrated in a narrow band? does the useful signal overlap with the noise?).

Parseval's theorem is more than a mathematical curiosity — it is a practical tool for filter analysis and design. When a signal passes through a filter, its spectrum is multiplied by the filter's frequency response H(f): the output spectrum is Y(f) = H(f)·X(f). The output energy in any frequency band is therefore |H(f)|²·|X(f)|² integrated over that band. This lets you calculate exactly how much energy a filter passes or blocks without ever computing the filtered time-domain signal. It also explains why filter design is specified in terms of magnitude-squared (power) rather than magnitude — the quantity |H(f)|² directly tells you the fraction of input energy at each frequency that reaches the output. Understanding Parseval's theorem ties together the Fourier analysis you know, the energy and power concepts from signal properties, and the filter design concepts that follow, making it a conceptual bridge across the entire signals-and-systems curriculum.
