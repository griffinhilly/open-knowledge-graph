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
stage: advanced
status: draft
---

# Coherence and Cross-Spectral Density

## Core Idea
Cross-spectral density Sxy(f) = FT[Rxy(τ)] describes frequency-domain correlation between signals. Coherence Cxy(f) = |Sxy(f)|²/(Sxx(f)·Syy(f)) normalizes to [0,1], indicating linear dependence strength at each frequency. Coherence 1 indicates perfect correlation; coherence 0 indicates independence. High coherence in narrow bands reveals channel coupling or shared noise sources.

## Explainer

From your study of cross-correlation and power spectral density, you know two things: the cross-correlation function Rxy(τ) measures the similarity between signals x and y as a function of time lag τ, and the power spectral density PSD describes how a signal's power is distributed across frequency. The **cross-spectral density** Sxy(f) brings these together — it is the Fourier transform of Rxy(τ), giving a frequency-domain description of how two signals are correlated at each frequency. Like the PSD, it can be estimated from data using the Welch method or equivalent windowed averaging procedures.

The cross-spectral density Sxy(f) is in general complex-valued. Its magnitude |Sxy(f)| captures how strongly x and y are related at frequency f. Its phase arg(Sxy(f)) captures the time delay or phase shift between the two signals at that frequency — if one signal leads the other by a constant delay, the phase of Sxy(f) increases linearly with frequency. This phase information is what distinguishes cross-spectral analysis from simply multiplying the two PSDs: the PSD product Sxx(f)·Syy(f) loses the phase relationship entirely.

**Coherence** Cxy(f) = |Sxy(f)|² / (Sxx(f)·Syy(f)) normalizes the cross-spectral density to lie between 0 and 1. Think of it as a frequency-resolved squared correlation coefficient — exactly like R² in linear regression, but evaluated at each frequency independently. Coherence equal to 1 at frequency f means x and y are perfectly linearly related at that frequency (one can be expressed as a linear filter applied to the other). Coherence equal to 0 means they are completely uncorrelated at that frequency. In practice, coherence estimates are computed with finite data and therefore never exactly reach 1 even for perfectly correlated signals; the effective lower bound for coherence significance depends on the number of averages used.

The practical diagnostic power of coherence is substantial. If you are analyzing an acoustic measurement at a microphone and you want to know which portion of the noise at 500 Hz is causally related to a specific machine vibration, coherence between the vibration sensor and the microphone gives a direct answer. Frequencies where coherence is high are dominated by the source you are measuring; frequencies where coherence is low are contaminated by independent noise or other uncorrelated sources. Similarly, in structural dynamics, coherence between an excitation force and a measured response is checked before estimating a frequency response function — low coherence warns that the FRF estimate at that frequency is unreliable, perhaps due to nonlinearity, extraneous noise, or signal clipping.
