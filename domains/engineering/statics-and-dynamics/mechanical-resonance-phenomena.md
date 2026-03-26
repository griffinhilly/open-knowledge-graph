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
status: validated
---

# Mechanical Resonance and Frequency Response

## Core Idea
When periodic external forces are applied to an oscillatory system, the response amplitude depends strongly on the ratio of driving frequency to natural frequency. At resonance (when they match), even small forces cause large-amplitude oscillations in undamped systems. Understanding resonance is critical for avoiding destructive vibrations in structures and machinery.

## Questions

```yaml
- question: "An engineer gradually increases the frequency of a periodic force applied to a lightly damped structure. As driving frequency approaches the structure's natural frequency from below, what happens to response amplitude?"
  type: multiple-choice
  options:
    - "It decreases, because the system has less time to respond to each cycle"
    - "It stays roughly constant until the frequencies match, then drops sharply"
    - "It increases dramatically, potentially reaching destructive levels even for small force magnitudes"
    - "It increases linearly with driving frequency, reaching a maximum well above the natural frequency"
  answer: 2
  explanation: "The magnification factor MF = 1/|1−(Ω/ωₙ)²| grows as Ω approaches ωₙ. As the denominator approaches zero, the magnification grows without bound in an undamped system. Even with light damping (ζ=0.01), the peak amplitude at resonance is 1/(2ζ) = 50 times the static deflection. The key insight is that force magnitude and response amplitude decouple near resonance — a tiny periodic force can produce catastrophic oscillation if its frequency matches the natural frequency."

- question: "A lightly damped metal structure has a damping ratio ζ = 0.02. When driven at its natural frequency, its steady-state amplitude is approximately how many times its static deflection?"
  type: multiple-choice
  options:
    - "2 times — the damping ratio directly limits amplification"
    - "25 times — from the resonance formula 1/(2ζ) = 1/(0.04)"
    - "50 times — from the resonance formula 1/(2ζ) = 1/(0.02)"
    - "100 times — because the damping ratio squares at resonance"
  answer: 1
  explanation: "At resonance (Ω = ωₙ) in a damped system, the magnification factor peaks at 1/(2ζ). With ζ = 0.02: MF = 1/(2×0.02) = 1/0.04 = 25. Option C would apply if ζ = 0.01. The formula 1/(2ζ) means lighter damping gives larger resonant amplification — a ζ = 0.01 structure would reach 50× at resonance."

- question: "Adding mass to a mechanical structure generally increases its risk of resonance with a fixed driving frequency."
  type: true-false
  answer: false
  explanation: "Adding mass lowers the natural frequency (ωₙ = √(k/m) — increasing m decreases ωₙ). Whether this increases or decreases resonance risk depends entirely on where ωₙ was relative to the excitation frequency before the change. If the excitation is above ωₙ, adding mass moves ωₙ further from the excitation — reducing risk. If the excitation is below ωₙ, adding mass moves ωₙ toward the excitation — increasing risk. The relationship is not monotonic; what matters is the ratio Ω/ωₙ."

- question: "At resonance, the steady-state displacement response of a damped system lags exactly 90° behind the driving force."
  type: true-false
  answer: true
  explanation: "The phase lag between response and driving force depends on Ω/ωₙ: near zero frequency the phase lag ≈ 0° (in phase); at resonance (Ω = ωₙ) the phase lag is exactly 90° regardless of damping level; above resonance the phase lag → 180° (out of phase). The 90° phase at resonance is observable experimentally and is sometimes used as the operational definition of resonance — it occurs at the exact natural frequency, while the amplitude peak shifts slightly with damping."

- question: "Explain why the Tacoma Narrows Bridge collapsed under relatively light wind forces, connecting your explanation to the concept of resonance."
  type: short-answer
  answer: "The bridge had a torsional natural frequency. Wind flowing past the bridge created vortices that shed alternately from each side at a frequency that matched (or approached) this natural frequency. Even though the periodic aerodynamic forces from vortex shedding were small, the magnification factor near resonance amplified them dramatically. Each cycle added energy that was not dissipated by the bridge's low damping, so oscillation amplitude grew progressively over minutes until the structure failed. Small force × large magnification factor = catastrophic response."
  explanation: "The key lesson: resonance decouples force magnitude from response magnitude. Engineers now calculate natural frequencies and ensure they differ from expected excitation frequencies, or add damping to limit the magnification factor."
```

## Explainer

From your study of single-degree-of-freedom vibrations, you know that any spring-mass system has a **natural frequency** ωₙ = √(k/m) at which it freely oscillates when disturbed. Free vibration is the system's intrinsic behavior — it rings at ωₙ when you tap it and then decays (if there's damping) or continues indefinitely (if undamped). Forced vibration is different: now an external periodic force F(t) = F₀ cos(Ωt) is continuously driving the system at frequency Ω, which you can tune independently of ωₙ.

The solution to the forced oscillation equation reveals that the steady-state amplitude is proportional to a **magnification factor** (or dynamic amplification factor): MF = 1 / |1 − (Ω/ωₙ)²|. When the driving frequency Ω is far below ωₙ, this factor is close to 1 — the system responds almost statically. When Ω is much higher than ωₙ, the factor goes to zero — the system barely moves because it can't keep up with the rapid forcing. But as Ω approaches ωₙ from below, the denominator approaches zero and the magnification factor grows without bound in an undamped system. This is **resonance**: the system's response grows catastrophically for any nonzero forcing amplitude.

In real systems with damping, the denominator never exactly reaches zero, but at resonance the magnification factor still peaks at 1/(2ζ), where ζ is the **damping ratio**. For lightly damped systems (ζ = 0.01, common in metal structures), this peak is 50 times the static deflection — a tiny alternating force produces oscillations fifty times larger than the same force applied statically. There is also a phase relationship: at low frequencies the response is in phase with the force; at resonance the response lags exactly 90° behind the driving force; above resonance the response is 180° out of phase. This phase shift is observable and is sometimes used to detect resonance experimentally.

The engineering consequences are severe. The Tacoma Narrows Bridge collapsed in 1940 when wind-induced vortices excited the bridge's torsional natural frequency — small periodic aerodynamic forces grew to destructive amplitude in minutes. Rotating machinery (engines, fans, compressors) must pass through resonant frequencies during startup and shutdown, requiring the crossing to happen quickly or the resonance to be damped. Turbine blades, building floors, and aircraft wings are all designed so that their natural frequencies lie well away from expected excitation frequencies.

The **frequency response function** (FRF) is the systematic engineering tool for all this: it maps every driving frequency Ω to the steady-state amplitude and phase of the response. Plotting the FRF reveals resonant peaks (their frequencies identify natural frequencies), anti-resonances (frequencies where the response is locally suppressed), and the overall shape that determines how the system responds to any broadband excitation. Designing around resonance means either shifting ωₙ away from excitation frequencies (by changing stiffness k or mass m), adding damping to reduce the peak magnitude, or adding a tuned vibration absorber — a secondary mass-spring system deliberately tuned to cancel the primary resonance.
