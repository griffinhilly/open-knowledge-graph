---
id: mechanical-resonance-phenomena
title: Mechanical Resonance and Frequency Response
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: vibrations-single-dof
  type: hard
builds-toward:
- damping-in-mechanical-systems
tags:
- resonance
- oscillations
- frequency-response
stage: formal-systems
status: draft
---

# Mechanical Resonance and Frequency Response

## Core Idea
When periodic external forces are applied to an oscillatory system, the response amplitude depends strongly on the ratio of driving frequency to natural frequency. At resonance (when they match), even small forces cause large-amplitude oscillations in undamped systems. Understanding resonance is critical for avoiding destructive vibrations in structures and machinery.

## Explainer

From your study of single-degree-of-freedom vibrations, you know that any spring-mass system has a **natural frequency** ωₙ = √(k/m) at which it freely oscillates when disturbed. Free vibration is the system's intrinsic behavior — it rings at ωₙ when you tap it and then decays (if there's damping) or continues indefinitely (if undamped). Forced vibration is different: now an external periodic force F(t) = F₀ cos(Ωt) is continuously driving the system at frequency Ω, which you can tune independently of ωₙ.

The solution to the forced oscillation equation reveals that the steady-state amplitude is proportional to a **magnification factor** (or dynamic amplification factor): MF = 1 / |1 − (Ω/ωₙ)²|. When the driving frequency Ω is far below ωₙ, this factor is close to 1 — the system responds almost statically. When Ω is much higher than ωₙ, the factor goes to zero — the system barely moves because it can't keep up with the rapid forcing. But as Ω approaches ωₙ from below, the denominator approaches zero and the magnification factor grows without bound in an undamped system. This is **resonance**: the system's response grows catastrophically for any nonzero forcing amplitude.

In real systems with damping, the denominator never exactly reaches zero, but at resonance the magnification factor still peaks at 1/(2ζ), where ζ is the **damping ratio**. For lightly damped systems (ζ = 0.01, common in metal structures), this peak is 50 times the static deflection — a tiny alternating force produces oscillations fifty times larger than the same force applied statically. There is also a phase relationship: at low frequencies the response is in phase with the force; at resonance the response lags exactly 90° behind the driving force; above resonance the response is 180° out of phase. This phase shift is observable and is sometimes used to detect resonance experimentally.

The engineering consequences are severe. The Tacoma Narrows Bridge collapsed in 1940 when wind-induced vortices excited the bridge's torsional natural frequency — small periodic aerodynamic forces grew to destructive amplitude in minutes. Rotating machinery (engines, fans, compressors) must pass through resonant frequencies during startup and shutdown, requiring the crossing to happen quickly or the resonance to be damped. Turbine blades, building floors, and aircraft wings are all designed so that their natural frequencies lie well away from expected excitation frequencies.

The **frequency response function** (FRF) is the systematic engineering tool for all this: it maps every driving frequency Ω to the steady-state amplitude and phase of the response. Plotting the FRF reveals resonant peaks (their frequencies identify natural frequencies), anti-resonances (frequencies where the response is locally suppressed), and the overall shape that determines how the system responds to any broadband excitation. Designing around resonance means either shifting ωₙ away from excitation frequencies (by changing stiffness k or mass m), adding damping to reduce the peak magnitude, or adding a tuned vibration absorber — a secondary mass-spring system deliberately tuned to cancel the primary resonance.
