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

## Explainer

Your study of simple harmonic motion gave you the undamped oscillator: a mass-spring system where energy shuttles forever between kinetic and potential form. Real systems always have some resistance — air drag, material hysteresis, friction at joints. Mathematically, adding a **damping force** proportional to velocity (F_d = −cv) gives the equation mẍ + cẋ + kx = 0. The ratio ζ = c/(2√(km)) is the **damping ratio**, which controls the character of the free response. When ζ < 1 (underdamped), the system oscillates but with an exponentially decaying envelope: x(t) = Ae^(−ζω_n t) cos(ω_d t + φ), where ω_d = ω_n√(1−ζ²) is the **damped natural frequency**, slightly below ω_n. When ζ = 1 (critically damped), the system returns to rest in minimum time without oscillating. When ζ > 1 (overdamped), the system creeps back slowly without oscillation. Each case corresponds to different real-engineering needs: suspension systems aim for slight underdamping for ride comfort, while precision positioning stages may be critically damped.

The more important engineering scenario is **forced vibration**: an external harmonic force F₀ sin(ωt) drives the system at frequency ω. The total response has a transient part (the free vibration, which damps out) and a steady-state part (at the driving frequency ω). After transients die, only the steady-state remains: x(t) = X sin(ωt + φ). The amplitude X and phase φ both depend on the ratio r = ω/ω_n and the damping ratio ζ. The **dynamic magnification factor** M = X/(F₀/k) tells you how much larger the steady-state displacement is compared to the static deflection. When ω ≪ ω_n (very slow driving), M ≈ 1: the system follows the force quasi-statically. When ω ≫ ω_n (very fast driving), M → 0: the mass can't keep up with rapid forcing. Near ω ≈ ω_n, M peaks dramatically — this is **resonance**.

At resonance, the phase of the response lags the driving force by exactly 90°, regardless of damping level. The amplitude at resonance is M = 1/(2ζ): for light damping (ζ = 0.05), the resonant amplitude is 10 times the static deflection. For zero damping (ζ = 0) in theory, the amplitude grows without bound — in practice, some nonlinearity or structural failure intervenes first. The Tacoma Narrows Bridge collapse (1940) is the canonical example: aeroelastic forces drove the bridge at near its resonant frequency, with too little damping, until it destroyed itself. One subtlety: the maximum amplitude actually occurs slightly below ω_n for damped systems (at ω = ω_n√(1−2ζ²)), not exactly at ω_n — though the difference matters only for highly precise designs.

**Frequency response plots** (amplitude and phase versus r = ω/ω_n) are the engineer's primary tool for understanding vibration behavior. You read the peak amplitude and its location, identify dangerous operating frequencies to avoid, and evaluate whether added damping (a tuned mass damper, for instance) sufficiently flattens the resonance peak. Real systems often have multiple resonant frequencies (one for each degree of freedom), and real forcing contains multiple frequencies, so the full power of this analysis extends to frequency-domain methods. But the single-degree-of-freedom damped forced oscillator is the template — understand its frequency response and you can interpret far more complex vibration spectra by superposition and modal analysis.
