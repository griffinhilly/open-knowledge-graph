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
status: validated
---

# Damping, Forced Vibrations, and Resonance

## Core Idea
Adding a damping term m·y'' + c·y' + k·y = F(t) to the spring-mass equation introduces energy dissipation and external forcing. When the driving frequency matches the natural frequency, resonance occurs, producing large-amplitude oscillations. Damping prevents unbounded growth.

## How It's Best Learned
Solve forced undamped systems (c = 0) to see resonance amplitude → ∞. Then add damping to show how energy loss limits amplification. Explore the phase lag between forcing and response.

## Common Misconceptions
- Thinking resonance only occurs at the natural frequency; damping shifts the resonance frequency slightly. - Confusing Q-factor (sharpness of resonance peak) with energy dissipation rate. - Not recognizing transient versus steady-state behavior in forced systems.

## Questions

```yaml
- question: "An undamped spring-mass system is driven by a periodic force at exactly its natural frequency ω₀. What happens to the amplitude of oscillation over time?"
  type: multiple-choice
  options:
    - "It remains constant — the system oscillates steadily at its natural frequency"
    - "It grows without bound — each push arrives in phase and adds energy continuously"
    - "It decays to zero — the system dissipates the driving energy"
    - "It locks onto the driving frequency and jumps to a new stable amplitude"
  answer: 1
  explanation: "At resonance in an undamped system, the particular solution requires a factor of t (multiplication by t), producing terms like t·cos(ω₀t) that grow without bound. Each push from the external force arrives exactly in phase with the oscillation, so energy accumulates with every cycle — like pushing a swing at exactly the right moment every time. Damping is what prevents this unbounded growth in real systems; the Tacoma Narrows Bridge collapse is the classic physical illustration."

- question: "A damped forced oscillator has been running for a very long time. At what frequency does the steady-state oscillation occur?"
  type: multiple-choice
  options:
    - "The natural frequency ω₀ = √(k/m), regardless of the driving frequency"
    - "The driving frequency ω — the system ultimately oscillates at the frequency it is driven"
    - "The average of the natural and driving frequencies"
    - "A frequency that depends on the damping coefficient c"
  answer: 1
  explanation: "The steady-state response is the particular solution to the forced equation, and it oscillates at the *driving* frequency ω, not the natural frequency ω₀. The complementary (homogeneous) solution — the transient — does oscillate near ω₀, but it contains decaying exponentials and fades to zero as t → ∞. After the transient dies out, the system has 'forgotten' its initial conditions and oscillates entirely at the frequency being imposed on it from outside."

- question: "In a damped forced oscillator, the transient solution (complementary solution) persists alongside the steady-state solution indefinitely."
  type: true-false
  answer: false
  explanation: "The transient solution contains decaying exponentials (from the underdamped characteristic roots with negative real parts), so it fades to zero as t → ∞. It represents the system's response to initial conditions, which gradually washes out as energy is dissipated by damping. Only the particular solution — the steady-state response at the driving frequency — remains after sufficient time. This is why 'transient' is the right word: it is temporary by definition."

- question: "Adding damping to a resonant system shifts the peak amplitude response to a frequency slightly below the undamped natural frequency ω₀."
  type: true-false
  answer: true
  explanation: "This is a subtle but real effect. The undamped resonance peak occurs exactly at ω = ω₀. When damping is added, the resonance peak (maximum steady-state amplitude) shifts to ω = √(ω₀² − c²/(2m²)), which is slightly below ω₀. For light damping this shift is small and often negligible, but it means resonance doesn't occur at exactly the natural frequency once damping is present — a common misconception."

- question: "Why does resonance cause unbounded amplitude growth in an undamped system but only a large finite peak in a damped one?"
  type: short-answer
  answer: "In an undamped system, each driving cycle adds energy in phase with no mechanism to remove it, so energy accumulates without limit — mathematically, the particular solution requires a factor of t, producing growing oscillations. In a damped system, the damping term dissipates energy on every cycle. Near resonance, each drive cycle pumps in energy and the amplitude grows, but as amplitude grows, the energy dissipated per cycle (proportional to velocity, hence to amplitude) also grows, until dissipation equals input and a finite steady-state amplitude is reached."
  explanation: "The balance between energy input and energy dissipation is the physical core of damped resonance. Higher driving force increases the steady-state amplitude; stronger damping (higher c) reduces it. The sharpness of the resonance peak — how dramatically amplitude varies near ω₀ — is characterized by the Q-factor, which is inversely proportional to damping. A lightly damped system has a very sharp, tall resonance peak; a heavily damped system has a broad, low peak."
```

## Explainer

From your work on spring-mass systems, you know that an unforced, undamped spring oscillates forever: y(t) = A cos(ω₀t + φ), where **ω₀ = √(k/m)** is the **natural frequency** — the rate at which the system wants to oscillate when left alone. Real systems don't oscillate forever because energy leaks out through friction, air resistance, or a shock absorber. Adding a damping term c·y' (a force proportional to velocity and opposing motion) gives m·y'' + c·y' + k·y = 0. Using the characteristic equation (from your second-order ODE methods), the roots involve the discriminant c² − 4mk: if c² > 4mk the system is **overdamped** (exponential decay without oscillation), if c² = 4mk it is **critically damped** (fastest approach to equilibrium without oscillating), and if c² < 4mk it is **underdamped** (oscillates with exponentially decaying amplitude).

Adding an external periodic forcing function F(t) = F₀cos(ωt) — a rhythmic push at frequency ω — gives the full equation m·y'' + c·y' + k·y = F₀cos(ωt). The **method of undetermined coefficients** (which you used to find particular solutions) produces a particular solution representing the **steady-state response**: the long-run oscillation at the *driving* frequency ω. The complementary solution — containing the decaying exponentials from the homogeneous problem — is the **transient**: it reflects the initial conditions but fades to zero as t → ∞. The system ultimately oscillates at whatever frequency it is driven at, not at its own natural frequency.

The most dramatic phenomenon is **resonance**: when the driving frequency ω equals the natural frequency ω₀ in an *undamped* system (c = 0). In this case the standard particular solution form fails — you need to multiply by t, giving terms like t·cos(ω₀t). These grow without bound as t increases. Physically, each push from the external force arrives exactly in phase with the oscillation and adds energy continuously, like pushing a child on a swing at precisely the right moment every cycle. The Tacoma Narrows Bridge collapse in 1940 is the classic illustration: wind drove the bridge near its natural frequency, and the underdamped structure accumulated energy until it failed.

In practice, damping always exists, so resonance produces large but finite amplitudes rather than infinite growth. The steady-state amplitude peaks near ω = ω₀ and falls off on either side — the **resonance curve**. The **phase lag** between force and displacement also changes with frequency: near zero when ω ≪ ω₀ (the system follows the force closely), exactly π/2 at resonance, and near π when ω ≫ ω₀ (the system responds in opposition to the force). This frequency-dependent amplitude and phase response is the foundation of mechanical filters, vibration isolators, and radio tuners — all systems engineered to respond strongly at specific frequencies and reject others.
