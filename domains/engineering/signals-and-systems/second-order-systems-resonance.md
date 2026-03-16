---
id: second-order-systems-resonance
title: Second-Order Systems and Resonance
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
- id: frequency-response-magnitude-phase
  type: hard
tags:
- second-order-systems
- resonance
- damping
stage: advanced
status: draft
---

# Second-Order Systems and Resonance

## Core Idea
Second-order systems H(s) = ω_n²/(s² + 2ζω_n·s + ω_n²) exhibit resonance when underdamped (ζ < 1). Resonant frequency and peak magnitude depend on damping ratio ζ. Time-domain responses range from oscillatory (low ζ) to overdamped (high ζ). Understanding resonance is critical for vibration control and filter design.

## Explainer

You already know how to read a transfer function's poles and zeros and compute the frequency response. Second-order systems put those tools to work on a family of transfer functions that appears everywhere in engineering: H(s) = ω_n²/(s² + 2ζω_n·s + ω_n²). This form has exactly two poles, and their location in the s-plane is entirely determined by two parameters — the **natural frequency** ω_n (in rad/s) and the **damping ratio** ζ (dimensionless). Learning to read these parameters at a glance is the core skill here.

The natural frequency ω_n is the frequency at which the system would oscillate forever if there were no energy loss — like a frictionless pendulum. The damping ratio ζ describes how quickly energy is removed. When ζ = 0, oscillations never die. When ζ = 1 (critical damping), the system returns to rest as fast as possible without oscillating. When ζ > 1 (overdamped), it returns sluggishly with no oscillation at all. The interesting and practical regime is **underdamped**: 0 < ζ < 1, where the system oscillates while the amplitude decays exponentially. Most real springs, electrical LC circuits, and mechanical suspensions live in this regime.

**Resonance** occurs in underdamped systems when an input frequency matches the system's natural frequency. At resonance, the frequency response magnitude peaks — sometimes dramatically so. The peak frequency is ω_r = ω_n√(1 − 2ζ²), which is close to ω_n for small ζ. The peak magnitude scales as 1/(2ζ√(1−ζ²)), so as ζ → 0, the peak becomes arbitrarily large. This explains why a child pumping a swing at exactly the right rhythm builds up large oscillations, and why the Tacoma Narrows Bridge famously collapsed — the driving frequency matched the bridge's natural frequency with insufficient damping.

Connecting back to your frequency response knowledge: the poles of H(s) are at s = −ζω_n ± jω_n√(1−ζ²). These complex poles sit in the left half-plane (stable system) but close to the imaginary axis when ζ is small. The closer they are to the imaginary axis, the sharper and taller the resonance peak. In filter design, a high-Q (low-damping) second-order system creates a sharp bandpass or notch; in mechanical design, low damping is usually dangerous and engineers add dashpots or viscoelastic materials to move the poles away from the axis. The pole locations give you both the transient behavior (decay rate, oscillation frequency) and the frequency response (where and how sharply the system resonates) — two descriptions of the same underlying physics.
