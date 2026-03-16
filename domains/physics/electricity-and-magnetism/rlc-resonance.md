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
status: draft
---

# Resonance in RLC Circuits

## Core Idea
In a series RLC circuit, resonance occurs at ω₀ = 1/√(LC), where reactive impedances cancel and Z = R is minimum. Current is maximum: I₀ = V₀/R. Sharpness of resonance is characterized by quality factor Q = ω₀L/R = 1/(ω₀RC). Resonance is crucial in tuning, filtering, power transmission, and forms the bridge from circuits to electromagnetic waves.

## Explainer

From your study of AC impedance, you know that inductors and capacitors oppose current in frequency-dependent ways: the inductive reactance X_L = ωL grows with frequency, while the capacitive reactance X_C = 1/(ωC) shrinks with frequency. At most frequencies these are unequal, and the circuit's total impedance is larger than R alone. At exactly one special frequency, however, X_L = X_C, so their contributions cancel — leaving Z = R as the only opposition to current. This cancellation defines **resonance**, and it occurs at the **resonant frequency** ω₀ = 1/√(LC).

The physical picture is an energy exchange. An inductor stores energy in its magnetic field (proportional to I²), and a capacitor stores energy in its electric field (proportional to V²). At resonance, energy sloshes back and forth between them in perfect synchrony — like a pendulum trading kinetic and potential energy. The resistor is the only element that dissipates energy; it limits how large the oscillation can grow. Without resistance, current would theoretically grow without bound if driven precisely at ω₀.

The **quality factor** Q = ω₀L/R = 1/(ω₀RC) quantifies how sharply peaked the resonance is. A high-Q circuit (small R) has a narrow bandwidth — it responds strongly only to frequencies very close to ω₀ — while a low-Q circuit (large R) has a broad, flat response. This is exactly the selectivity you need in a radio tuner: adjusting the capacitor changes ω₀, letting you select one station from thousands by matching ω₀ to the broadcast frequency. The Q also measures the ratio of energy stored to energy dissipated per cycle — a high-Q circuit "rings" for many cycles before dying out.

The deeper significance of RLC resonance is that it provides the bridge from lumped circuits to electromagnetic waves. When you later study Maxwell's equations, you will find that an LC circuit is essentially an electromagnetic resonator — the same differential equation governs oscillations in a circuit and oscillations in a cavity. The resonant frequency of a radiation source determines the wavelength of the light it emits. The analogy is not superficial: microwave resonators, laser cavities, and atomic transitions all share the mathematics of the damped driven harmonic oscillator you are now mastering in circuit form.
