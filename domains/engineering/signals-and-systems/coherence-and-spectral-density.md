---
id: coherence-and-spectral-density
title: Coherence and Cross-Spectral Density
domain: engineering
course: signals-and-systems
prerequisites:
- id: power-spectral-density-estimation
  type: hard
- id: cross-correlation-signals
  type: hard
tags:
- coherence
- cross-spectral-density
- correlation
- spectral-analysis
stage: expert
status: validated
---

# Coherence and Cross-Spectral Density

## Core Idea
Cross-spectral density Sxy(f) = FT[Rxy(τ)] describes frequency-domain correlation between signals. Coherence Cxy(f) = |Sxy(f)|²/(Sxx(f)·Syy(f)) normalizes to [0,1], indicating linear dependence strength at each frequency. Coherence 1 indicates perfect correlation; coherence 0 indicates independence. High coherence in narrow bands reveals channel coupling or shared noise sources.

## Questions

```yaml
- question: "An engineer simultaneously measures vibration at two locations on a machine. The coherence between the two signals is 0.92 at 60 Hz and 0.04 at 400 Hz. What does this indicate?"
  type: multiple-choice
  options:
    - "The machine vibrates more strongly at 60 Hz than at 400 Hz — coherence reflects signal amplitude"
    - "The two measurement points share a common vibration source or propagation path at 60 Hz, but are largely independent or driven by different uncorrelated sources at 400 Hz"
    - "The 400 Hz signal is contaminated by sensor noise and needs recalibration before analysis"
    - "The cross-spectral density magnitude is 23 times larger at 60 Hz than at 400 Hz"
  answer: 1
  explanation: "Coherence indicates the degree of linear dependence between two signals at each frequency — it is independent of signal amplitude. High coherence (0.92) at 60 Hz means the two sensors' signals at that frequency are strongly linearly related, suggesting a common source or transmission path. Low coherence (0.04) at 400 Hz means the signals are nearly independent at that frequency, which could indicate different local excitation sources, nonlinear behavior, or uncorrelated noise. Coherence does not measure signal strength; two weak signals can be perfectly coherent."

- question: "What information is preserved in the cross-spectral density Sxy(f) that is lost if you simply compute the product of the individual power spectral densities Sxx(f) · Syy(f)?"
  type: multiple-choice
  options:
    - "The absolute power level of each signal at each frequency"
    - "The phase relationship (time delay or lead/lag) between the two signals at each frequency"
    - "Whether each signal is stationary or non-stationary over the measurement period"
    - "The signal-to-noise ratio of each individual measurement channel"
  answer: 1
  explanation: "The cross-spectral density Sxy(f) is complex-valued: its magnitude captures the correlation strength between x and y at frequency f, and its phase captures the time delay between the two signals at that frequency — a constant propagation delay appears as a linear phase increase with frequency. The product Sxx(f)·Syy(f) uses only real-valued magnitudes and discards all phase information. Coherence, which is |Sxy(f)|²/(Sxx(f)·Syy(f)), also sacrifices phase to achieve the [0,1] normalization, but the cross-spectral density itself retains it."

- question: "Coherence is bounded between 0 and 1 and can be interpreted as a frequency-resolved squared correlation coefficient — analogous to R² in linear regression, but evaluated independently at each frequency."
  type: true-false
  answer: true
  explanation: "True. This analogy is exact. Coherence Cxy(f) = |Sxy(f)|²/(Sxx(f)·Syy(f)) at each frequency f. Like R², a value of 0 means no linear relationship, and a value of 1 means perfect linear predictability. At a given frequency, coherence tells you what fraction of the signal power in y can be linearly predicted from x. This frequency-resolved interpretation is what makes coherence so powerful: rather than one global correlation coefficient, you get a complete picture of linear dependence across the spectrum."

- question: "A coherence of exactly 1.0 between two measured signals at a given frequency proves that one signal is the sole linear cause of the other, with no noise or third-party influences at that frequency."
  type: true-false
  answer: false
  explanation: "False. Coherence of 1.0 means the two signals are perfectly linearly related at that frequency — but it does not identify causality or rule out a common third source driving both. If a third unobserved variable causes both x and y at 60 Hz in a perfectly linear way, coherence will be 1.0 even though neither signal causes the other. Additionally, in practice, coherence estimates with finite data never reach exactly 1.0 due to statistical variability; the apparent ceiling depends on the number of spectral averages used."

- question: "Why is coherence more useful for diagnosing the relationship between two signals than simply examining the magnitude of the cross-spectral density?"
  type: short-answer
  answer: "The cross-spectral density magnitude |Sxy(f)| is not normalized — it depends on the absolute power of both signals. A large magnitude could reflect a strong relationship or simply high signal power in both channels. Coherence divides by the individual PSDs, normalizing the result to [0,1] regardless of signal amplitude, making it directly interpretable: coherence 0.9 at 400 Hz means 90% of signal y's power at that frequency can be linearly predicted from x, in the same way R² = 0.9 means 90% of variance is explained. Without normalization, comparing relationships across frequencies, experiments, or different sensor sensitivities is ambiguous."
  explanation: "This is why coherence is the standard diagnostic for frequency response function validity in structural dynamics: before computing an FRF (output/input in the frequency domain), engineers check coherence to identify frequency bands where the estimate is unreliable (low coherence), which indicates extraneous noise, nonlinearity, or signal clipping at those frequencies."
```

## Explainer

From your study of cross-correlation and power spectral density, you know two things: the cross-correlation function Rxy(τ) measures the similarity between signals x and y as a function of time lag τ, and the power spectral density PSD describes how a signal's power is distributed across frequency. The **cross-spectral density** Sxy(f) brings these together — it is the Fourier transform of Rxy(τ), giving a frequency-domain description of how two signals are correlated at each frequency. Like the PSD, it can be estimated from data using the Welch method or equivalent windowed averaging procedures.

The cross-spectral density Sxy(f) is in general complex-valued. Its magnitude |Sxy(f)| captures how strongly x and y are related at frequency f. Its phase arg(Sxy(f)) captures the time delay or phase shift between the two signals at that frequency — if one signal leads the other by a constant delay, the phase of Sxy(f) increases linearly with frequency. This phase information is what distinguishes cross-spectral analysis from simply multiplying the two PSDs: the PSD product Sxx(f)·Syy(f) loses the phase relationship entirely.

**Coherence** Cxy(f) = |Sxy(f)|² / (Sxx(f)·Syy(f)) normalizes the cross-spectral density to lie between 0 and 1. Think of it as a frequency-resolved squared correlation coefficient — exactly like R² in linear regression, but evaluated at each frequency independently. Coherence equal to 1 at frequency f means x and y are perfectly linearly related at that frequency (one can be expressed as a linear filter applied to the other). Coherence equal to 0 means they are completely uncorrelated at that frequency. In practice, coherence estimates are computed with finite data and therefore never exactly reach 1 even for perfectly correlated signals; the effective lower bound for coherence significance depends on the number of averages used.

The practical diagnostic power of coherence is substantial. If you are analyzing an acoustic measurement at a microphone and you want to know which portion of the noise at 500 Hz is causally related to a specific machine vibration, coherence between the vibration sensor and the microphone gives a direct answer. Frequencies where coherence is high are dominated by the source you are measuring; frequencies where coherence is low are contaminated by independent noise or other uncorrelated sources. Similarly, in structural dynamics, coherence between an excitation force and a measured response is checked before estimating a frequency response function — low coherence warns that the FRF estimate at that frequency is unreliable, perhaps due to nonlinearity, extraneous noise, or signal clipping.
