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
stage: expert
status: validated
---

# Second-Order Systems and Resonance

## Core Idea
Second-order systems H(s) = ω_n²/(s² + 2ζω_n·s + ω_n²) exhibit resonance when underdamped (ζ < 1). Resonant frequency and peak magnitude depend on damping ratio ζ. Time-domain responses range from oscillatory (low ζ) to overdamped (high ζ). Understanding resonance is critical for vibration control and filter design.

## Questions

```yaml
- question: "A second-order mechanical system has poles at s = −0.05 ± 20j rad/s. A sinusoidal force is applied at several frequencies. What do the pole locations predict about the system's frequency response?"
  type: multiple-choice
  options:
    - "The poles are far from the imaginary axis, indicating heavy damping and no resonance peak"
    - "The poles are close to the imaginary axis (small real part relative to imaginary part), indicating light damping and a sharp resonance peak near ω = 20 rad/s"
    - "The imaginary part of the poles indicates the system is marginally stable and will oscillate indefinitely"
    - "Pole locations cannot predict the frequency response — only the time-domain step response"
  answer: 1
  explanation: "The real part of the poles (−0.05) represents the decay rate; the imaginary part (20) represents the damped oscillation frequency. A small real part relative to the imaginary part means the poles sit close to the imaginary axis — indicating very light damping (ζ ≈ 0.05/20 = 0.0025). Poles near the imaginary axis produce a sharp, tall resonance peak in the frequency response near ω = 20 rad/s. In the Tacoma Narrows analogy: light structural damping meant the poles were nearly on the imaginary axis, and wind driving near the natural frequency produced catastrophic amplitude buildup."

- question: "Two second-order systems share the same natural frequency ω_n. System A has ζ = 0.05 and System B has ζ = 0.7. Both are driven by a sinusoidal input at ω_n. What does each system do?"
  type: multiple-choice
  options:
    - "Both respond identically because they share the same natural frequency"
    - "System A exhibits a very large resonance peak; System B has little or no amplitude peak near ω_n"
    - "System B has a larger peak because higher ζ means more energy is stored per cycle"
    - "Neither system peaks exactly at ω_n; they both peak at lower frequencies"
  answer: 1
  explanation: "Damping ratio ζ controls peak magnitude: the resonance peak is approximately 1/(2ζ) for small ζ. System A (ζ = 0.05) has a peak of ~10 times the DC gain — a large, sharp resonance. System B (ζ = 0.7 > 1/√2 ≈ 0.707) is just barely overdamped in frequency response terms — near or below the Butterworth threshold — producing little or no peak. Resonance requires that energy input accumulates faster than the system dissipates it; high damping bleeds energy too quickly for significant amplitude buildup."

- question: "Increasing the damping ratio ζ from 0.1 to 0.8 reduces both the overshoot in the step response and the height of the resonance peak in the frequency response."
  type: true-false
  answer: true
  explanation: "This is the fundamental unity of time-domain and frequency-domain descriptions: they are two views of the same physics. In the time domain, low ζ causes underdamped ringing and overshoot after a step; higher ζ dampens this. In the frequency domain, low ζ produces a tall resonance peak; higher ζ flattens it. Both behaviors trace back to the same pole locations: poles close to the imaginary axis produce both time-domain oscillation and frequency-domain resonance. Moving poles leftward (increasing ζ) simultaneously reduces overshoot and peak magnitude."

- question: "The resonant frequency of an underdamped second-order system is generally equal to its natural frequency ω_n."
  type: true-false
  answer: false
  explanation: "The resonant frequency (where the frequency response magnitude peaks) is ω_r = ω_n√(1 − 2ζ²), which equals ω_n only when ζ = 0 (undamped). For any real underdamped system (0 < ζ < 1/√2), the resonant frequency is slightly below ω_n. The difference is small for light damping (ζ = 0.1 gives ω_r ≈ 0.99ω_n) but becomes significant as ζ increases. Above ζ = 1/√2, there is no resonance peak at all. The natural frequency ω_n is a system property; the resonant frequency ω_r depends on both ω_n and the damping ratio."

- question: "Explain why a second-order system's pole locations in the complex s-plane simultaneously determine its transient step response and its steady-state resonance behavior."
  type: short-answer
  answer: "The poles of H(s) are the values of s where the transfer function's denominator is zero: s = −ζω_n ± jω_n√(1−ζ²). In the time domain, poles correspond to the natural modes of the system — each pole contributes a term e^(pole·t) to the impulse response. The real part (−ζω_n) sets the exponential decay rate; the imaginary part (ω_n√(1−ζ²)) sets the oscillation frequency. In the frequency domain, evaluating H(jω) as ω varies sweeps along the imaginary axis; the magnitude peaks when ω is closest to the imaginary part of the poles. Poles near the imaginary axis (small real part, low damping) produce both slow-decaying oscillatory transients and sharp resonance peaks — the same proximity to the imaginary axis controls both phenomena."
  explanation: "This unification is the central insight of Laplace analysis: the s-domain representation encodes both transient and steady-state behavior in a single mathematical object. Engineers use this to design for both: a filter specification in the frequency domain (flat passband, steep rolloff) translates directly into pole placement requirements in the s-plane, which then predicts the transient ringing behavior of the same filter when exposed to sudden inputs."
```

## Explainer

You already know how to read a transfer function's poles and zeros and compute the frequency response. Second-order systems put those tools to work on a family of transfer functions that appears everywhere in engineering: H(s) = ω_n²/(s² + 2ζω_n·s + ω_n²). This form has exactly two poles, and their location in the s-plane is entirely determined by two parameters — the **natural frequency** ω_n (in rad/s) and the **damping ratio** ζ (dimensionless). Learning to read these parameters at a glance is the core skill here.

The natural frequency ω_n is the frequency at which the system would oscillate forever if there were no energy loss — like a frictionless pendulum. The damping ratio ζ describes how quickly energy is removed. When ζ = 0, oscillations never die. When ζ = 1 (critical damping), the system returns to rest as fast as possible without oscillating. When ζ > 1 (overdamped), it returns sluggishly with no oscillation at all. The interesting and practical regime is **underdamped**: 0 < ζ < 1, where the system oscillates while the amplitude decays exponentially. Most real springs, electrical LC circuits, and mechanical suspensions live in this regime.

**Resonance** occurs in underdamped systems when an input frequency matches the system's natural frequency. At resonance, the frequency response magnitude peaks — sometimes dramatically so. The peak frequency is ω_r = ω_n√(1 − 2ζ²), which is close to ω_n for small ζ. The peak magnitude scales as 1/(2ζ√(1−ζ²)), so as ζ → 0, the peak becomes arbitrarily large. This explains why a child pumping a swing at exactly the right rhythm builds up large oscillations, and why the Tacoma Narrows Bridge famously collapsed — the driving frequency matched the bridge's natural frequency with insufficient damping.

Connecting back to your frequency response knowledge: the poles of H(s) are at s = −ζω_n ± jω_n√(1−ζ²). These complex poles sit in the left half-plane (stable system) but close to the imaginary axis when ζ is small. The closer they are to the imaginary axis, the sharper and taller the resonance peak. In filter design, a high-Q (low-damping) second-order system creates a sharp bandpass or notch; in mechanical design, low damping is usually dangerous and engineers add dashpots or viscoelastic materials to move the poles away from the axis. The pole locations give you both the transient behavior (decay rate, oscillation frequency) and the frequency response (where and how sharply the system resonates) — two descriptions of the same underlying physics.
