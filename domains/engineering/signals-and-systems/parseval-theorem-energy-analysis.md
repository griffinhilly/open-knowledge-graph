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
status: draft
---

# Parseval's Theorem and Energy/Power Spectral Density

## Core Idea
Parseval's theorem states that the total energy of a signal is the same whether computed in time or frequency: ∫|x(t)|² dt = ∫|X(f)|² df. The energy spectral density |X(f)|² shows how energy is distributed across frequencies.

## Explainer

From the Fourier transform, you know that a signal can be decomposed into sinusoidal components, with X(f) telling you the amplitude and phase of each frequency component. The Fourier transform is a change of representation — the same signal, viewed through a different lens. Parseval's theorem is a statement that this change of lens conserves something important: energy. Just as rotating a 3D coordinate system changes the components of a vector but not its length, the Fourier transform changes how a signal is represented but not its total energy content.

The theorem ∫|x(t)|² dt = ∫|X(f)|² df has a straightforward interpretation. The left side is the total signal energy computed in the time domain: you square the instantaneous amplitude at every moment and integrate. The right side computes the same total by squaring the magnitude of each frequency component and summing across all frequencies. The two must be equal because both are computing the same physical quantity — just from different vantage points. The quantity |X(f)|² is the **energy spectral density**: it tells you how much energy is concentrated in each narrow band of frequencies. A pure sinusoid concentrates all its energy at a single frequency; a short pulse spreads energy broadly across many frequencies; a bandlimited signal has |X(f)|² = 0 outside some frequency range.

For **power signals** — periodic or stationary random signals that have infinite energy but finite average power — the analogous result involves the **power spectral density** (PSD). The total average power equals the integral of the PSD over all frequencies. This extension is especially important in communications and signal processing, where you care not just about whether a signal has finite energy, but about how its power is distributed across the spectrum (is the noise concentrated in a narrow band? does the useful signal overlap with the noise?).

Parseval's theorem is more than a mathematical curiosity — it is a practical tool for filter analysis and design. When a signal passes through a filter, its spectrum is multiplied by the filter's frequency response H(f): the output spectrum is Y(f) = H(f)·X(f). The output energy in any frequency band is therefore |H(f)|²·|X(f)|² integrated over that band. This lets you calculate exactly how much energy a filter passes or blocks without ever computing the filtered time-domain signal. It also explains why filter design is specified in terms of magnitude-squared (power) rather than magnitude — the quantity |H(f)|² directly tells you the fraction of input energy at each frequency that reaches the output. Understanding Parseval's theorem ties together the Fourier analysis you know, the energy and power concepts from signal properties, and the filter design concepts that follow, making it a conceptual bridge across the entire signals-and-systems curriculum.
