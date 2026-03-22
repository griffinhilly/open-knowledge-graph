---
id: vibrations-damped-forced
title: Damped and Forced Vibrations
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: vibrations-simple-harmonic
  type: hard
- id: differential-equations-intro
  type: soft
- id: damped-harmonic-oscillator
  type: hard
tags:
- damping
- forced-vibration
- resonance
- amplitude
stage: formal-systems
status: draft
---

# Damped and Forced Vibrations

## Core Idea
Damping introduces a velocity-dependent resistance force (F = -c v) that dissipates energy and reduces oscillation amplitude over time. When a system is driven by a periodic external force, resonance occurs near the natural frequency where amplitude becomes very large. The response amplitude and phase depend on the driving frequency relative to ω_n and the damping ratio ζ = c/(2√(km)).

## How It's Best Learned
Analyze standard underdamped, critically damped, and overdamped responses. Use frequency response plots to visualize resonance phenomena. Connect to real applications like suspension systems and seismic isolation.

## Common Misconceptions
- Thinking maximum amplitude always occurs exactly at ω_n (it shifts for damped systems).
- Confusing phase lag at resonance with amplitude response.
- Assuming damping always prevents harmful vibrations (it reduces amplitude but resonance can still occur).

## Questions

```yaml
- question: "A damped mechanical system has damping ratio ζ = 0.1 and is being driven at its natural frequency. An engineer reduces the damping ratio to ζ = 0.05. The steady-state resonant amplitude will:"
  type: multiple-choice
  options:
    - "Double, because the dynamic magnification factor M = 1/(2ζ) is inversely proportional to ζ"
    - "Stay the same, because the natural frequency did not change"
    - "Decrease, because less damping means the system returns to rest faster"
    - "Become infinite, because any reduction in damping leads to unbounded amplitude"
  answer: 0
  explanation: "At resonance, M = 1/(2ζ). When ζ halves from 0.1 to 0.05, M doubles from 5 to 10. This inverse relationship is the key formula for resonant amplitude. The misconception in option C reverses the logic — less damping means energy dissipates more slowly, so steady-state amplitude builds higher, not lower. Option D is only true for the theoretical ζ = 0 case; any finite damping produces a finite resonant amplitude."

- question: "For a damped forced oscillator, where does the maximum steady-state amplitude actually occur?"
  type: multiple-choice
  options:
    - "Exactly at the undamped natural frequency ω_n, regardless of damping ratio"
    - "At a driving frequency slightly below ω_n, at ω = ω_n√(1 − 2ζ²)"
    - "At the damped natural frequency ω_d = ω_n√(1 − ζ²)"
    - "At a driving frequency slightly above ω_n, because damping shifts the peak upward"
  answer: 1
  explanation: "The resonant peak in the frequency response of a damped forced system occurs at ω = ω_n√(1 − 2ζ²), which is slightly below both ω_n and ω_d. This is a common source of confusion: for lightly damped systems the shift is negligible, but for ζ > 1/√2 ≈ 0.707, the peak disappears entirely and there is no resonance. The undamped natural frequency ω_n is where phase lag equals 90°, not where amplitude peaks."

- question: "For an underdamped system, the damped natural frequency ω_d equals the undamped natural frequency ω_n."
  type: true-false
  answer: false
  explanation: "The damped natural frequency is ω_d = ω_n√(1 − ζ²), which is always less than ω_n for any positive damping ratio. The difference is small for lightly damped systems (e.g., ζ = 0.1 gives ω_d ≈ 0.995 ω_n), but becomes significant as ζ approaches 1. At critical damping (ζ = 1), ω_d = 0 — the system no longer oscillates at all. This distinction matters when designing systems to avoid specific resonant frequencies."

- question: "At resonance, the steady-state response of a forced damped oscillator lags the driving force by exactly 90°, regardless of the value of the damping ratio ζ."
  type: true-false
  answer: true
  explanation: "The 90° phase lag at ω = ω_n is a universal property of the damped forced oscillator, independent of damping level. This is because the phase angle φ = arctan(2ζr / (1 − r²)) evaluated at r = ω/ω_n = 1 gives arctan(2ζ·0) = arctan(∞) ... wait, actually at r=1: φ = arctan(2ζ·1 / (1−1²)) = arctan(2ζ/0) = 90° for all ζ > 0. The phase is always 90° at the undamped natural frequency — it is the amplitude peak that shifts, not the 90° phase crossing."

- question: "Explain why a mechanical system can experience harmful resonance even when damping is present, and what determines the severity of the resonant response."
  type: short-answer
  answer: "Damping reduces resonant amplitude but does not eliminate resonance for ζ < 1/√2. The resonant amplitude is M = 1/(2ζ), so lightly damped systems (small ζ) still experience very large amplification near ω_n. For example, ζ = 0.05 gives M = 10 — ten times the static deflection. Whether this is harmful depends on the design requirements: a bridge or aircraft wing with insufficient damping can fail structurally because the resonant amplitude exceeds material limits, even though the vibration is not growing without bound."
  explanation: "The Tacoma Narrows Bridge is the canonical example: it had some damping, but not enough to reduce the resonant amplitude below the threshold for structural failure. The key insight is that 'damped' does not mean 'safe at resonance' — it only means 'finite amplitude at resonance.' Engineers use frequency response plots to evaluate whether the resonant peak, even with damping included, stays within acceptable displacement or stress limits. Adding more damping (via tuned mass dampers, viscoelastic materials, or active control) flattens the peak."
```

## Explainer

Your study of simple harmonic motion gave you the undamped oscillator: a mass-spring system where energy shuttles forever between kinetic and potential form. Real systems always have some resistance — air drag, material hysteresis, friction at joints. Mathematically, adding a **damping force** proportional to velocity (F_d = −cv) gives the equation mẍ + cẋ + kx = 0. The ratio ζ = c/(2√(km)) is the **damping ratio**, which controls the character of the free response. When ζ < 1 (underdamped), the system oscillates but with an exponentially decaying envelope: x(t) = Ae^(−ζω_n t) cos(ω_d t + φ), where ω_d = ω_n√(1−ζ²) is the **damped natural frequency**, slightly below ω_n. When ζ = 1 (critically damped), the system returns to rest in minimum time without oscillating. When ζ > 1 (overdamped), the system creeps back slowly without oscillation. Each case corresponds to different real-engineering needs: suspension systems aim for slight underdamping for ride comfort, while precision positioning stages may be critically damped.

The more important engineering scenario is **forced vibration**: an external harmonic force F₀ sin(ωt) drives the system at frequency ω. The total response has a transient part (the free vibration, which damps out) and a steady-state part (at the driving frequency ω). After transients die, only the steady-state remains: x(t) = X sin(ωt + φ). The amplitude X and phase φ both depend on the ratio r = ω/ω_n and the damping ratio ζ. The **dynamic magnification factor** M = X/(F₀/k) tells you how much larger the steady-state displacement is compared to the static deflection. When ω ≪ ω_n (very slow driving), M ≈ 1: the system follows the force quasi-statically. When ω ≫ ω_n (very fast driving), M → 0: the mass can't keep up with rapid forcing. Near ω ≈ ω_n, M peaks dramatically — this is **resonance**.

At resonance, the phase of the response lags the driving force by exactly 90°, regardless of damping level. The amplitude at resonance is M = 1/(2ζ): for light damping (ζ = 0.05), the resonant amplitude is 10 times the static deflection. For zero damping (ζ = 0) in theory, the amplitude grows without bound — in practice, some nonlinearity or structural failure intervenes first. The Tacoma Narrows Bridge collapse (1940) is the canonical example: aeroelastic forces drove the bridge at near its resonant frequency, with too little damping, until it destroyed itself. One subtlety: the maximum amplitude actually occurs slightly below ω_n for damped systems (at ω = ω_n√(1−2ζ²)), not exactly at ω_n — though the difference matters only for highly precise designs.

**Frequency response plots** (amplitude and phase versus r = ω/ω_n) are the engineer's primary tool for understanding vibration behavior. You read the peak amplitude and its location, identify dangerous operating frequencies to avoid, and evaluate whether added damping (a tuned mass damper, for instance) sufficiently flattens the resonance peak. Real systems often have multiple resonant frequencies (one for each degree of freedom), and real forcing contains multiple frequencies, so the full power of this analysis extends to frequency-domain methods. But the single-degree-of-freedom damped forced oscillator is the template — understand its frequency response and you can interpret far more complex vibration spectra by superposition and modal analysis.
