---
id: rlc-resonance
title: Resonance in RLC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ac-impedance
  type: hard
builds-toward:
- maxwell-equations-overview
tags:
- resonance
- rlc
- quality-factor
stage: formal-systems
status: validated
---

# Resonance in RLC Circuits

## Core Idea
In a series RLC circuit, resonance occurs at ω₀ = 1/√(LC), where reactive impedances cancel and Z = R is minimum. Current is maximum: I₀ = V₀/R. Sharpness of resonance is characterized by quality factor Q = ω₀L/R = 1/(ω₀RC). Resonance is crucial in tuning, filtering, power transmission, and forms the bridge from circuits to electromagnetic waves.

## Questions

```yaml
- question: "An engineer doubles the resistance R in a series RLC circuit while keeping L and C unchanged. What happens to the resonant frequency ω₀ and the quality factor Q?"
  type: multiple-choice
  options:
    - "Both ω₀ and Q increase — more resistance creates a stronger resonance"
    - "ω₀ stays the same (it depends only on L and C), but Q decreases — more resistance means broader, less selective resonance"
    - "ω₀ decreases because higher resistance shifts the resonance peak to lower frequency"
    - "Q increases because higher resistance stabilizes the energy exchange between L and C"
  answer: 1
  explanation: "The resonant frequency ω₀ = 1/√(LC) depends only on L and C — not on R. Doubling R leaves ω₀ unchanged. The quality factor Q = ω₀L/R = 1/(ω₀RC) is inversely proportional to R, so doubling R halves Q. A lower Q means a broader resonance peak: the circuit responds appreciably to a wider range of frequencies near ω₀ rather than being sharply selective. This is why low-resistance (high-Q) circuits are used for radio tuners where sharp frequency selectivity is essential."

- question: "A student says: 'At resonance, the RLC circuit has zero impedance because the inductive and capacitive reactances cancel.' Why is this statement imprecise?"
  type: multiple-choice
  options:
    - "It is completely correct — at resonance, the total impedance is zero"
    - "The reactive parts cancel (X_L = X_C, so net reactive impedance is zero), but the resistive part R remains; total impedance Z = R, not zero. Current is maximum (I = V/R) but finite."
    - "At resonance, inductive and capacitive reactances add rather than cancel"
    - "The statement is wrong because impedance has no reactive component in DC circuits"
  answer: 1
  explanation: "At resonance, X_L = X_C exactly, so the imaginary (reactive) part of the impedance cancels: Z = R + j(X_L − X_C) = R + j·0 = R. The impedance equals R — its minimum value — not zero (unless the circuit is ideal with R = 0). Current I = V₀/R is maximized but finite. Saying 'impedance is zero' confuses the cancellation of reactive components with elimination of all impedance. Only in a purely ideal, lossless LC circuit (R = 0) would Z reach zero, which is a mathematical idealization."

- question: "Increasing the inductance L in a series RLC circuit while keeping R and C constant will lower the resonant frequency ω₀."
  type: true-false
  answer: true
  explanation: "The resonant frequency is ω₀ = 1/√(LC). If L increases and C is constant, LC increases, so √(LC) increases, and ω₀ = 1/√(LC) decreases. Physically: a larger inductor stores more energy per unit current, slowing the energy exchange cycle between L and C. This is analogous to adding mass to a spring-mass oscillator (larger L ↔ larger m), which reduces the natural frequency ω₀ = √(k/m)."

- question: "A high-Q RLC circuit is well-suited as a wide-band amplifier because it responds strongly to a broad range of frequencies."
  type: true-false
  answer: false
  explanation: "A high-Q circuit has a *narrow* bandwidth — it responds significantly only to frequencies very close to ω₀. This narrow selectivity makes it ideal for applications requiring discrimination between nearby frequencies (radio tuners, narrow-band filters), but exactly the opposite of a wideband amplifier. A low-Q circuit (achieved with larger R) has a broad, flat response and responds to a wider frequency range. High Q means high selectivity; low Q means wide bandwidth."

- question: "Explain why the quality factor Q determines a radio tuner's ability to select one station while rejecting adjacent ones. What does a high Q mean physically in terms of the circuit's energy storage and dissipation?"
  type: short-answer
  answer: "Q = ω₀L/R measures the ratio of energy stored per cycle to energy dissipated per cycle. A high-Q circuit (small R relative to ω₀L) stores much more energy per oscillation than it loses, so it continues to 'ring' for many cycles after excitation. In the frequency domain, this manifests as a very narrow resonance peak: only frequencies extremely close to ω₀ drive significant current, while frequencies even slightly off-resonance drive much less current. For a radio tuner, this means the circuit responds to the desired station's broadcast frequency but rejects adjacent stations broadcasting at nearby frequencies. Adjusting C changes ω₀ to match different station frequencies."
  explanation: "The bandwidth Δω = ω₀/Q, so higher Q directly means narrower bandwidth and sharper station selectivity. In engineering terms, Q is the figure of merit for frequency selectivity. The energy picture — high Q means energy sloshes between L and C for many cycles before R dissipates it — is why high-Q circuits 'ring' like a well-struck bell (high-Q mechanical analog) while low-Q circuits decay quickly."
```

## Explainer

From your study of AC impedance, you know that inductors and capacitors oppose current in frequency-dependent ways: the inductive reactance X_L = ωL grows with frequency, while the capacitive reactance X_C = 1/(ωC) shrinks with frequency. At most frequencies these are unequal, and the circuit's total impedance is larger than R alone. At exactly one special frequency, however, X_L = X_C, so their contributions cancel — leaving Z = R as the only opposition to current. This cancellation defines **resonance**, and it occurs at the **resonant frequency** ω₀ = 1/√(LC).

The physical picture is an energy exchange. An inductor stores energy in its magnetic field (proportional to I²), and a capacitor stores energy in its electric field (proportional to V²). At resonance, energy sloshes back and forth between them in perfect synchrony — like a pendulum trading kinetic and potential energy. The resistor is the only element that dissipates energy; it limits how large the oscillation can grow. Without resistance, current would theoretically grow without bound if driven precisely at ω₀.

The **quality factor** Q = ω₀L/R = 1/(ω₀RC) quantifies how sharply peaked the resonance is. A high-Q circuit (small R) has a narrow bandwidth — it responds strongly only to frequencies very close to ω₀ — while a low-Q circuit (large R) has a broad, flat response. This is exactly the selectivity you need in a radio tuner: adjusting the capacitor changes ω₀, letting you select one station from thousands by matching ω₀ to the broadcast frequency. The Q also measures the ratio of energy stored to energy dissipated per cycle — a high-Q circuit "rings" for many cycles before dying out.

The deeper significance of RLC resonance is that it provides the bridge from lumped circuits to electromagnetic waves. When you later study Maxwell's equations, you will find that an LC circuit is essentially an electromagnetic resonator — the same differential equation governs oscillations in a circuit and oscillations in a cavity. The resonant frequency of a radiation source determines the wavelength of the light it emits. The analogy is not superficial: microwave resonators, laser cavities, and atomic transitions all share the mathematics of the damped driven harmonic oscillator you are now mastering in circuit form.
