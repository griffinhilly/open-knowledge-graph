---
id: damping-and-resonance
title: Damping, Forced Vibrations, and Resonance
domain: mathematics
course: differential-equations
prerequisites:
- id: spring-mass-systems-and-vibrations
  type: hard
- id: undetermined-coefficients
  type: hard
builds-toward:
- rlc-circuits
tags:
- application
- forced-oscillations
- resonance
stage: formal-systems
status: draft
---

# Damping, Forced Vibrations, and Resonance

## Core Idea
Adding a damping term m·y'' + c·y' + k·y = F(t) to the spring-mass equation introduces energy dissipation and external forcing. When the driving frequency matches the natural frequency, resonance occurs, producing large-amplitude oscillations. Damping prevents unbounded growth.

## How It's Best Learned
Solve forced undamped systems (c = 0) to see resonance amplitude → ∞. Then add damping to show how energy loss limits amplification. Explore the phase lag between forcing and response.

## Common Misconceptions
- Thinking resonance only occurs at the natural frequency; damping shifts the resonance frequency slightly. - Confusing Q-factor (sharpness of resonance peak) with energy dissipation rate. - Not recognizing transient versus steady-state behavior in forced systems.

## Explainer

From your work on spring-mass systems, you know that an unforced, undamped spring oscillates forever: y(t) = A cos(ω₀t + φ), where **ω₀ = √(k/m)** is the **natural frequency** — the rate at which the system wants to oscillate when left alone. Real systems don't oscillate forever because energy leaks out through friction, air resistance, or a shock absorber. Adding a damping term c·y' (a force proportional to velocity and opposing motion) gives m·y'' + c·y' + k·y = 0. Using the characteristic equation (from your second-order ODE methods), the roots involve the discriminant c² − 4mk: if c² > 4mk the system is **overdamped** (exponential decay without oscillation), if c² = 4mk it is **critically damped** (fastest approach to equilibrium without oscillating), and if c² < 4mk it is **underdamped** (oscillates with exponentially decaying amplitude).

Adding an external periodic forcing function F(t) = F₀cos(ωt) — a rhythmic push at frequency ω — gives the full equation m·y'' + c·y' + k·y = F₀cos(ωt). The **method of undetermined coefficients** (which you used to find particular solutions) produces a particular solution representing the **steady-state response**: the long-run oscillation at the *driving* frequency ω. The complementary solution — containing the decaying exponentials from the homogeneous problem — is the **transient**: it reflects the initial conditions but fades to zero as t → ∞. The system ultimately oscillates at whatever frequency it is driven at, not at its own natural frequency.

The most dramatic phenomenon is **resonance**: when the driving frequency ω equals the natural frequency ω₀ in an *undamped* system (c = 0). In this case the standard particular solution form fails — you need to multiply by t, giving terms like t·cos(ω₀t). These grow without bound as t increases. Physically, each push from the external force arrives exactly in phase with the oscillation and adds energy continuously, like pushing a child on a swing at precisely the right moment every cycle. The Tacoma Narrows Bridge collapse in 1940 is the classic illustration: wind drove the bridge near its natural frequency, and the underdamped structure accumulated energy until it failed.

In practice, damping always exists, so resonance produces large but finite amplitudes rather than infinite growth. The steady-state amplitude peaks near ω = ω₀ and falls off on either side — the **resonance curve**. The **phase lag** between force and displacement also changes with frequency: near zero when ω ≪ ω₀ (the system follows the force closely), exactly π/2 at resonance, and near π when ω ≫ ω₀ (the system responds in opposition to the force). This frequency-dependent amplitude and phase response is the foundation of mechanical filters, vibration isolators, and radio tuners — all systems engineered to respond strongly at specific frequencies and reject others.
