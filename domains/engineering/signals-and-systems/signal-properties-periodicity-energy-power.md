---
id: signal-properties-periodicity-energy-power
title: 'Signal Properties: Periodicity, Energy, and Power'
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
builds-toward:
- fourier-series-representation
- parseval-theorem-energy-analysis
tags:
- signals
- properties
- energy
stage: advanced
status: draft
---

# Signal Properties: Periodicity, Energy, and Power

## Core Idea
Every signal can be characterized by whether it is periodic, its total energy (integral of squared magnitude), or its average power (energy per unit time). These properties determine which mathematical representations and analysis techniques are most suitable.

## Explainer

Your prerequisite, signal classification, taught you that signals come in continuous-time and discrete-time flavors. Now you need a deeper vocabulary for describing *what a signal does over time* — not its type, but its character. Three properties do most of the work: periodicity, energy, and power. They divide signals into fundamentally different classes that demand different analytical tools.

**Periodicity** is the property a signal has when it repeats exactly. A signal x(t) is periodic with period T if x(t) = x(t + T) for all t, where T is the smallest such positive value. A pure sine wave is the canonical example: sin(2πt) repeats every second, sin(4πt) repeats every half-second. Periodic signals extend infinitely in both directions — they have no beginning or end — which means they carry infinite total energy but finite *average* energy per cycle. This matters because the right mathematical tool for analyzing periodic signals is the Fourier series, which decomposes them into a sum of sinusoids at the fundamental frequency and its harmonics.

**Signal energy** is defined as E = ∫|x(t)|² dt integrated over all time (or Σ|x[n]|² for discrete signals). Think of it as the total work the signal could perform if it were a physical quantity like voltage across a resistor. A signal is an **energy signal** if this integral converges to a finite number — meaning the signal eventually dies away. A decaying exponential like e^(-t)u(t) is an energy signal: it starts at 1 and drops toward zero, accumulating a finite total. Periodic signals are never energy signals because they never die — their energy integral diverges.

**Signal power** is defined as P = lim(T→∞) (1/T) ∫|x(t)|² dt — the average energy per unit time. A signal is a **power signal** if this limit exists and is finite and nonzero. Periodic signals are power signals: their energy is infinite, but their average power over each cycle is constant. A pure sine wave has average power equal to the square of its amplitude divided by 2. The energy-power classification is mutually exclusive: a signal can be an energy signal (finite energy, zero average power), a power signal (infinite energy, finite average power), or neither (like a signal that grows without bound) — but never both.

The practical payoff is this: knowing whether a signal is energy or power type tells you how to analyze it and what to expect from its spectrum. Energy signals pair with the Fourier transform and have continuous spectra; periodic (power) signals pair with the Fourier series and have discrete spectra at integer multiples of the fundamental frequency. When you encounter a new signal, these three questions — is it periodic? does its energy converge? does its average power converge? — are your first diagnostic moves.
