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

## Questions

```yaml
- question: "A pure sine wave sin(2πt) extends from t = −∞ to t = +∞. How should this signal be classified?"
  type: multiple-choice
  options:
    - "Energy signal — its amplitude is bounded, so its energy integral must converge"
    - "Neither energy nor power — sinusoids are a special class that falls outside both categories"
    - "Power signal — it is periodic with infinite total energy but finite average power per cycle"
    - "Both energy and power — it satisfies both definitions simultaneously"
  answer: 2
  explanation: "A sine wave extending to infinity has infinite total energy: ∫|sin(2πt)|² dt diverges. So it is not an energy signal. But its average power P = lim(T→∞)(1/T)∫|sin(2πt)|²dt = 1/2, which is finite and nonzero. This makes it a power signal. A signal cannot be both — the energy-power classification is mutually exclusive. The common mistake is reasoning that 'bounded amplitude means finite energy,' which confuses magnitude with total accumulated energy over infinite time."

- question: "A decaying exponential signal x(t) = e^(−t)u(t) (where u(t) is the unit step) is being classified. What type is it and why?"
  type: multiple-choice
  options:
    - "Power signal — exponentials are inherently related to power"
    - "Energy signal — the signal decays to zero, so its squared magnitude converges to a finite total when integrated over all time"
    - "Neither — it is one-sided (only exists for t ≥ 0), so neither definition applies"
    - "Both — it satisfies both the energy and power definitions"
  answer: 1
  explanation: "E = ∫₀^∞ (e^(−t))² dt = ∫₀^∞ e^(−2t) dt = 1/2, which is finite. The signal decays to zero, so its energy accumulation eventually stops — finite total energy makes it an energy signal. Its average power P = lim(T→∞)(1/T)·(finite constant) = 0, which confirms it is not a power signal. Any signal that eventually dies away to zero is an energy signal; signals that maintain nonzero amplitude forever (like sinusoids) are power signals."

- question: "A signal can be both an energy signal and a power signal if it has a finite amplitude and a periodic structure."
  type: true-false
  answer: false
  explanation: "Energy signals and power signals are mutually exclusive by definition. An energy signal has finite total energy (E < ∞), which forces its average power to be zero (P = 0, since a finite amount of energy spread over infinite time averages to nothing). A power signal has finite nonzero average power, which requires infinite total energy. A signal with finite energy cannot simultaneously have nonzero average power, and a signal with nonzero average power cannot have finite total energy. Periodic signals have infinite energy (not finite), so they can never be energy signals regardless of their amplitude."

- question: "If a signal's total energy integral diverges to infinity but its time-averaged power converges to a finite, nonzero value, the signal is classified as a power signal."
  type: true-false
  answer: true
  explanation: "This is precisely the definition of a power signal: P = lim(T→∞)(1/T)∫_{-T/2}^{T/2}|x(t)|²dt exists, is finite, and is nonzero. The divergence of total energy is a required property of power signals — a signal with finite total energy would have average power P = 0, not a nonzero power signal. Periodic signals are the canonical example: they have infinite total energy but constant average power over each cycle."

- question: "Explain why a periodic signal is never an energy signal, and describe the property it has instead."
  type: short-answer
  answer: "A periodic signal repeats indefinitely — it has no beginning and no end. Its energy integral ∫|x(t)|²dt is equivalent to summing the finite energy of one period infinitely many times, which diverges to infinity. Therefore its total energy is infinite, violating the definition of an energy signal (E < ∞). Instead, a periodic signal is a power signal: its average energy per unit time (average power) is finite and constant — equal to the average energy of one period divided by the period length. This finite average power is what makes periodic signals analyzable despite their infinite total energy."
  explanation: "The energy/power classification reflects how signals behave over time. Energy signals are transient — they deliver a finite total payload and then die. Power signals are sustained — they continuously deliver energy at a constant average rate. This distinction determines the correct analytical framework: energy signals are analyzed with the Fourier transform (producing continuous spectra), while periodic power signals are analyzed with the Fourier series (producing discrete spectra at integer multiples of the fundamental frequency). Getting this classification right is the first step in any signal analysis."
```

## Explainer

Your prerequisite, signal classification, taught you that signals come in continuous-time and discrete-time flavors. Now you need a deeper vocabulary for describing *what a signal does over time* — not its type, but its character. Three properties do most of the work: periodicity, energy, and power. They divide signals into fundamentally different classes that demand different analytical tools.

**Periodicity** is the property a signal has when it repeats exactly. A signal x(t) is periodic with period T if x(t) = x(t + T) for all t, where T is the smallest such positive value. A pure sine wave is the canonical example: sin(2πt) repeats every second, sin(4πt) repeats every half-second. Periodic signals extend infinitely in both directions — they have no beginning or end — which means they carry infinite total energy but finite *average* energy per cycle. This matters because the right mathematical tool for analyzing periodic signals is the Fourier series, which decomposes them into a sum of sinusoids at the fundamental frequency and its harmonics.

**Signal energy** is defined as E = ∫|x(t)|² dt integrated over all time (or Σ|x[n]|² for discrete signals). Think of it as the total work the signal could perform if it were a physical quantity like voltage across a resistor. A signal is an **energy signal** if this integral converges to a finite number — meaning the signal eventually dies away. A decaying exponential like e^(-t)u(t) is an energy signal: it starts at 1 and drops toward zero, accumulating a finite total. Periodic signals are never energy signals because they never die — their energy integral diverges.

**Signal power** is defined as P = lim(T→∞) (1/T) ∫|x(t)|² dt — the average energy per unit time. A signal is a **power signal** if this limit exists and is finite and nonzero. Periodic signals are power signals: their energy is infinite, but their average power over each cycle is constant. A pure sine wave has average power equal to the square of its amplitude divided by 2. The energy-power classification is mutually exclusive: a signal can be an energy signal (finite energy, zero average power), a power signal (infinite energy, finite average power), or neither (like a signal that grows without bound) — but never both.

The practical payoff is this: knowing whether a signal is energy or power type tells you how to analyze it and what to expect from its spectrum. Energy signals pair with the Fourier transform and have continuous spectra; periodic (power) signals pair with the Fourier series and have discrete spectra at integer multiples of the fundamental frequency. When you encounter a new signal, these three questions — is it periodic? does its energy converge? does its average power converge? — are your first diagnostic moves.
