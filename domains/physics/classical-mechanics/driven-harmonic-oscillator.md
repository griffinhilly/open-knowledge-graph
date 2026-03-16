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
status: draft
---

# Driven Harmonic Oscillator

## Core Idea
When a periodic external force F(t) = F₀ cos(ωt) drives a damped oscillator, the system reaches a steady-state oscillation at the driving frequency ω. The amplitude and phase depend strongly on ω and damping: near the natural frequency (resonance), the amplitude is large. Far from resonance, the oscillator is either in phase (below resonance) or 180° out of phase (above resonance) with the drive.

## Explainer

You've already studied the damped harmonic oscillator — a mass on a spring with a friction-like damping term that bleeds energy away until the system comes to rest. You've also worked through second-order linear ODEs and the characteristic equation method. The driven harmonic oscillator puts a new forcing term on the right-hand side: mx'' + bx' + kx = F₀ cos(ωt). From your ODE work, you know that the general solution to this non-homogeneous equation is the sum of a **complementary solution** (solving the homogeneous part) and a **particular solution** (any function satisfying the full equation). The damping from the previous topic is exactly why this decomposition matters physically, not just mathematically.

The complementary solution is the damped transient you already know — it decays exponentially with time. Given long enough, it disappears. What remains is the **steady-state response**: the particular solution, which oscillates at the *driving* frequency ω, not the natural frequency ω₀ = √(k/m). This is a key conceptual point: after transients die out, the system forgets its natural frequency and just follows the driver. To find the particular solution, guess x_p = A cos(ωt) + B sin(ωt) (equivalently, a complex exponential if you're using complex number methods), substitute, and match coefficients. The result gives you the steady-state amplitude and phase as functions of ω.

The amplitude of the steady-state response, as a function of driving frequency ω, tells the most important story. Far below ω₀ (driving slowly), the spring dominates and the oscillator follows the force closely — the amplitude approaches F₀/k (the static displacement). Far above ω₀ (driving fast), the inertia dominates, the oscillator can't keep up, and the amplitude falls toward zero. Near ω₀, something interesting happens: the system's energy builds up because the driving force is nearly in sync with the natural oscillation. This is **resonance**. With lighter damping, the resonance peak is taller and narrower; with heavy damping, the peak broadens and flattens. In the limit of zero damping, the amplitude at ω = ω₀ diverges — it would grow without bound.

The **phase shift** between force and displacement is equally important and often underemphasized. Below resonance, the displacement is approximately in phase with the force — push right, it goes right. At resonance, the displacement lags the force by exactly 90°: when the force is maximum, the velocity is maximum but the displacement is zero. Above resonance, the displacement is approximately 180° out of phase — push right, it goes left. This phase behavior has real engineering consequences. When you want maximum energy transfer into a system (tuning a radio, driving a resonant circuit, shaking a building), you want to drive at the natural frequency. When you want to isolate a system from vibrations (car suspension, building seismic dampers), you want your driving frequencies far from the natural frequency, so the amplitude response stays small.

The driven harmonic oscillator is the prototype for an enormous range of physical phenomena: AC circuits (with RLC standing in for the mechanical parts), optical absorption, NMR spectroscopy, structural engineering under periodic loads. Every instance involves the same interplay of a natural frequency, a driving frequency, a damping coefficient, and the resulting steady-state amplitude and phase. Mastering this system gives you a physical intuition that transfers across all of these domains.

