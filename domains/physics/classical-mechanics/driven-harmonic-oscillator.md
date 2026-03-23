---
id: driven-harmonic-oscillator
title: Driven Harmonic Oscillator
domain: physics
course: classical-mechanics
prerequisites:
- id: damped-harmonic-oscillator
  type: hard
- id: higher-order-linear-odes
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
- id: differential-equations-intro
  type: hard
- id: characteristic-equation-method
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- resonance-and-resonance-frequency
tags:
- oscillations
- driven
- forcing
- steady-state
stage: formal-systems
status: validated
---

# Driven Harmonic Oscillator

## Core Idea
When a periodic external force F(t) = F₀ cos(ωt) drives a damped oscillator, the system reaches a steady-state oscillation at the driving frequency ω. The amplitude and phase depend strongly on ω and damping: near the natural frequency (resonance), the amplitude is large. Far from resonance, the oscillator is either in phase (below resonance) or 180° out of phase (above resonance) with the drive.

## Questions

```yaml
- question: "A lightly damped oscillator with natural frequency ω₀ = 10 rad/s is driven at ω = 7 rad/s for a very long time. At what frequency does the resulting steady-state oscillation occur?"
  type: multiple-choice
  options:
    - "10 rad/s — systems always oscillate at their natural frequency in the long run"
    - "7 rad/s — the steady state follows the driving frequency, not the natural frequency"
    - "8.5 rad/s — the steady state settles at the average of the driving and natural frequencies"
    - "The system doesn't oscillate — far from resonance, amplitude approaches zero"
  answer: 1
  explanation: "After transients decay, the system forgets its natural frequency and oscillates purely at the driving frequency. The complementary solution (which contains the natural frequency ω₀) decays exponentially due to damping and eventually vanishes. The remaining steady-state response — the particular solution — oscillates at ω = 7 rad/s. The amplitude may be small (since 7 rad/s is below resonance), but the frequency is unambiguously the driving frequency. Option A is the most common misconception: students expect systems to 'want' to oscillate at their natural frequency."

- question: "A driven harmonic oscillator is excited at a frequency well above its natural frequency. How does the displacement relate to the driving force in the steady state?"
  type: multiple-choice
  options:
    - "The displacement is in phase with the force — when the force is maximum, the displacement is maximum"
    - "The displacement lags the force by exactly 90° — the phase shift is the same as at resonance"
    - "The displacement is approximately 180° out of phase — the mass moves opposite to the applied force"
    - "The phase relationship is random above the natural frequency and cannot be predicted"
  answer: 2
  explanation: "Phase behavior is one of the most important and underemphasized aspects of forced oscillations. Below resonance: displacement ≈ in phase with force. At resonance: displacement lags force by exactly 90°. Above resonance: displacement is approximately 180° out of phase — push right, it goes left. At high frequency, inertia dominates and the mass barely has time to respond before the force reverses. The 180° phase flip above resonance has real engineering consequences: if you try to drive a stiff structure above its natural frequency, your actuator pushes in the wrong direction relative to motion."

- question: "At resonance (ω = ω₀), the steady-state amplitude of a driven harmonic oscillator diverges to infinity."
  type: true-false
  answer: false
  explanation: "Amplitude diverges only in the idealized case of zero damping. With any real damping, the resonance amplitude is finite — large, but bounded by b/(mω₀) in the denominator of the amplitude formula. The lighter the damping, the taller and narrower the resonance peak, but real physical systems always have some damping. The idealized zero-damping result is a useful limit for understanding the trend, but it is not physically achievable."

- question: "The complementary (homogeneous) solution to the driven oscillator equation represents a transient that decays with time, leaving only the particular solution as the long-term behavior."
  type: true-false
  answer: true
  explanation: "This is the mathematical reason why steady-state behavior is well-defined. The complementary solution (the damped free oscillation at the natural frequency) decays exponentially as e^(-bt/2m). Eventually it becomes negligible, leaving only the particular solution — the steady-state oscillation at the driving frequency ω. This is why 'transient' is the right word: the natural-frequency component is only visible early on, before damping has had time to suppress it."

- question: "Why does a driven harmonic oscillator exhibit especially large amplitude oscillations near resonance? Explain in terms of what the drive and the system are doing relative to each other."
  type: short-answer
  answer: "Near resonance, the driving frequency closely matches the system's natural frequency, so the drive pushes the system in approximately the same direction it is already moving for most of each cycle. At resonance exactly, the displacement lags the force by 90°, which means the force is maximally aligned with the velocity — every push does positive work on the system. Energy is being added at nearly the maximum possible rate per cycle, while damping dissipates energy at a rate proportional to velocity. The large amplitude arises because energy input nearly overwhelms energy dissipation, and the system builds up a large oscillation before a steady state is reached where the two rates balance."
  explanation: "The phase relationship at resonance is the key: force and velocity are in phase (not force and displacement), so the work done per cycle W = ∫F·v dt is maximized. With lighter damping, the system needs a larger amplitude before the dissipation rate equals the input rate — hence a taller resonance peak for smaller damping coefficients."
```

## Explainer

You've already studied the damped harmonic oscillator — a mass on a spring with a friction-like damping term that bleeds energy away until the system comes to rest. You've also worked through second-order linear ODEs and the characteristic equation method. The driven harmonic oscillator puts a new forcing term on the right-hand side: mx'' + bx' + kx = F₀ cos(ωt). From your ODE work, you know that the general solution to this non-homogeneous equation is the sum of a **complementary solution** (solving the homogeneous part) and a **particular solution** (any function satisfying the full equation). The damping from the previous topic is exactly why this decomposition matters physically, not just mathematically.

The complementary solution is the damped transient you already know — it decays exponentially with time. Given long enough, it disappears. What remains is the **steady-state response**: the particular solution, which oscillates at the *driving* frequency ω, not the natural frequency ω₀ = √(k/m). This is a key conceptual point: after transients die out, the system forgets its natural frequency and just follows the driver. To find the particular solution, guess x_p = A cos(ωt) + B sin(ωt) (equivalently, a complex exponential if you're using complex number methods), substitute, and match coefficients. The result gives you the steady-state amplitude and phase as functions of ω.

The amplitude of the steady-state response, as a function of driving frequency ω, tells the most important story. Far below ω₀ (driving slowly), the spring dominates and the oscillator follows the force closely — the amplitude approaches F₀/k (the static displacement). Far above ω₀ (driving fast), the inertia dominates, the oscillator can't keep up, and the amplitude falls toward zero. Near ω₀, something interesting happens: the system's energy builds up because the driving force is nearly in sync with the natural oscillation. This is **resonance**. With lighter damping, the resonance peak is taller and narrower; with heavy damping, the peak broadens and flattens. In the limit of zero damping, the amplitude at ω = ω₀ diverges — it would grow without bound.

The **phase shift** between force and displacement is equally important and often underemphasized. Below resonance, the displacement is approximately in phase with the force — push right, it goes right. At resonance, the displacement lags the force by exactly 90°: when the force is maximum, the velocity is maximum but the displacement is zero. Above resonance, the displacement is approximately 180° out of phase — push right, it goes left. This phase behavior has real engineering consequences. When you want maximum energy transfer into a system (tuning a radio, driving a resonant circuit, shaking a building), you want to drive at the natural frequency. When you want to isolate a system from vibrations (car suspension, building seismic dampers), you want your driving frequencies far from the natural frequency, so the amplitude response stays small.

The driven harmonic oscillator is the prototype for an enormous range of physical phenomena: AC circuits (with RLC standing in for the mechanical parts), optical absorption, NMR spectroscopy, structural engineering under periodic loads. Every instance involves the same interplay of a natural frequency, a driving frequency, a damping coefficient, and the resulting steady-state amplitude and phase. Mastering this system gives you a physical intuition that transfers across all of these domains.

