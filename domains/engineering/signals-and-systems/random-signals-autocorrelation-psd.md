---
id: random-signals-autocorrelation-psd
title: Random Signals, Autocorrelation, and Power Spectral Density
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-properties-periodicity-energy-power
  type: hard
- id: parseval-theorem-energy-analysis
  type: hard
tags:
- random-signals
- noise
- stochastic
- power-spectral-density
stage: expert
status: draft
---

# Random Signals, Autocorrelation, and Power Spectral Density

## Core Idea
Random signals (noise, stochastic processes) are characterized by their autocorrelation R(τ) = E[x(t)x(t+τ)] and power spectral density S(f) = FT{R(τ)}. White noise has flat PSD; colored noise has frequency-dependent power. These tools enable analysis of systems driven by noise and filtering of noisy signals.

## Questions

```yaml
- question: "The autocorrelation R(τ) of a random signal decays to zero very slowly as the lag τ increases. What does this tell you about the signal?"
  type: multiple-choice
  options:
    - "The signal has very little power — most of its energy is concentrated near τ = 0"
    - "The signal has long memory — its current value is a good predictor of values far in the future"
    - "The signal is white noise — it is uncorrelated at all nonzero lags by definition"
    - "The signal must be periodic, because periodic signals maintain correlation across all lags"
  answer: 1
  explanation: "R(τ) measures how correlated the signal is with a time-shifted version of itself. When R(τ) decays slowly, the signal retains predictive power over long time intervals — it has 'memory.' Ocean waves, speech, and economic time series tend to have slowly decaying autocorrelation. Option C has it exactly backwards: white noise has R(τ) = δ(τ), meaning it decorrelates instantly at any nonzero lag. Option D confuses periodicity with correlation: periodic signals do maintain correlation at multiples of the period, but slowly-decaying correlation doesn't imply periodicity."

- question: "A random signal has a power spectral density S(f) that is concentrated almost entirely at frequencies below 10 Hz. You pass it through a bandpass filter that passes only 50–100 Hz. What can you say about the output?"
  type: multiple-choice
  options:
    - "The output power is roughly the same as the input — filters don't change total power"
    - "The output has very little power — almost all signal power was in frequencies the filter removed"
    - "The output is now white noise — filtering always whitens a signal's spectrum"
    - "The output PSD is S_out(f) = S_in(f) / |H(f)|², which amplifies the remaining components"
  answer: 1
  explanation: "The output PSD is S_out(f) = |H(f)|² · S_in(f). Since S_in(f) is near zero in the 50–100 Hz band, and the filter passes only that band, the output has very little power — the filter transmits almost none of the input signal's energy. This is a direct application of the key result: you can predict output noise statistics from input PSD without knowing the actual waveform. Option D has the formula inverted (it should be multiplication, not division, and the filter reduces rather than amplifies here)."

- question: "White noise has a flat power spectral density, which implies its autocorrelation is zero at all nonzero lags."
  type: true-false
  answer: true
  explanation: "By the Wiener-Khinchin theorem, R(τ) and S(f) are a Fourier transform pair. A constant (flat) S(f) corresponds to R(τ) = δ(τ) — a delta function at τ = 0 and zero everywhere else. This means white noise is completely uncorrelated with itself at any nonzero time delay, which is consistent with its perfectly random (memoryless) character. The signal's value right now tells you nothing about its value an instant later."

- question: "If you know the power spectral density of a random input signal and the frequency response of a linear system, you can predict the exact output waveform of the system."
  type: true-false
  answer: false
  explanation: "Knowing S_in(f) and H(f) lets you compute S_out(f) = |H(f)|² · S_in(f) — but this only predicts the *statistical properties* of the output, not the actual waveform. The actual output remains random and unpredictable sample-by-sample. PSD analysis tells you where power is distributed across frequencies and what the average power is; it cannot tell you what value the signal will take at time t = 5.3 s. This is the fundamental difference between random and deterministic signal analysis."

- question: "Why is the power spectral density (PSD) preferred over the Fourier transform for characterizing random signals? What makes direct Fourier analysis problematic for random processes?"
  type: short-answer
  answer: "Random signals don't have a well-defined Fourier transform because they are not absolutely integrable and their individual realizations differ unpredictably. Taking the Fourier transform of one specific realization gives you that realization's spectrum, not a stable characteristic of the process. The PSD instead characterizes the signal's *statistical* frequency content — the average power distribution that is stable and repeatable across realizations. Via the Wiener-Khinchin theorem, the PSD is defined as the Fourier transform of the autocorrelation R(τ), which is a deterministic function of the signal's statistics and can be reliably estimated."
  explanation: "This connects to why autocorrelation is the central tool: it converts an unpredictable random process into a stable, deterministic function (R(τ)) that captures the signal's average statistical structure. The PSD is then the frequency-domain image of that structure — predictable even when the waveform itself is not."
```

## Explainer

Deterministic signals can be described exactly by a formula — you know what the signal will be at every future time. Random signals cannot. Thermal noise in a resistor, acoustic vibrations in a room, and radio interference are all unpredictable sample-by-sample, yet they have stable *statistical structure* that repeats on average. The challenge is to characterize that structure without knowing the actual waveform.

The key tool is the **autocorrelation function** R(τ) = E[x(t)x(t+τ)]. It answers: how similar is the signal to a time-shifted version of itself, on average? When the lag τ = 0, you get the signal's average power: R(0) = E[x²]. As τ increases, a signal with slow fluctuations stays correlated over long lags, while pure noise decorrelates instantly. Intuitively, R(τ) tells you the "memory" of the signal — how long it takes for the signal's current value to stop predicting its future values. From your prerequisite on signal power, you already know that power matters more than instantaneous amplitude for most engineering problems; autocorrelation formalizes this by tracking how power is distributed across time delays.

The **power spectral density** S(f) brings this into the frequency domain via the Wiener-Khinchin theorem: S(f) = FT{R(τ)}. This is the random-signal analog of the relationship you saw in Parseval's theorem — total power can be computed either in the time domain (integrating R(0)) or in the frequency domain (integrating S(f) across all frequencies). The PSD tells you *where in frequency* the signal's power lives. **White noise** is the idealized extreme: S(f) = constant across all frequencies, meaning equal power at every frequency. This implies R(τ) = δ(τ) — the signal is completely uncorrelated with itself at any nonzero lag. In practice, white noise is an approximation; real noise is bandlimited and has some residual correlation.

**Colored noise** has frequency-dependent PSD — more power at some frequencies than others. Pink noise (1/f noise) concentrates power at low frequencies; blue noise concentrates it at high frequencies. When a random signal passes through a linear system (filter), the output PSD is S_out(f) = |H(f)|² · S_in(f), where H(f) is the system's frequency response. This is the stochastic analog of the deterministic convolution you already know. It means you can design a filter to suppress noise in certain frequency bands while preserving signal, and you can predict exactly what the output noise statistics will be — even though you cannot predict the actual output waveform. This connection between frequency-domain tools and statistical characterization is what makes PSD analysis so powerful in signal processing, communications, and control systems.
