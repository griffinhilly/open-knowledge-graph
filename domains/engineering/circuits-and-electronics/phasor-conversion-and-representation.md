---
id: phasor-conversion-and-representation
title: Phasor Conversion and Representation
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: sinusoidal-AC-steady-state-fundamentals
  type: hard
- id: complex-exponential-form
  type: hard
builds-toward:
- complex-impedance-networks-ac
- AC-Kirchhoff-laws-phasor-domain
tags:
- phasors
- complex-representation
- frequency-domain
stage: advanced
status: draft
---

# Phasor Conversion and Representation

## Core Idea
A phasor is a complex number representing the amplitude and phase of a sinusoid. The transformation v(t) = Re[V̅ e^(jωt)] converts time-domain sinusoids to frequency-domain phasors V̅ = |V|e^(jφ). This greatly simplifies AC circuit analysis by converting differential equations into algebraic equations.

## How It's Best Learned
Practice converting between time-domain and phasor domains. Use Euler's formula e^(jθ) = cos(θ) + j sin(θ) to move between rectangular and polar forms. Verify using circuit simulations.

## Common Misconceptions
- Phasors only apply to single-frequency signals. - A phasor magnitude is the same as peak voltage; RMS values are used in phasors. - Phasor addition in the complex plane is vector addition, not scalar addition.

## Explainer

In your prerequisite work, you learned that AC circuits in steady state have voltages and currents oscillating at the same frequency as the source — only the amplitudes and phases differ from branch to branch. You also learned Euler's formula: e^(jθ) = cos(θ) + j·sin(θ), which connects complex exponentials to sinusoids. Phasors bring these two ideas together into one powerful transformation: they let you represent any sinusoidal signal as a single complex number, freezing the time-varying behavior into a static amplitude and phase angle that you can manipulate with algebra instead of calculus.

The conversion starts from the observation that any sinusoid v(t) = Vm·cos(ωt + φ) can be written as the real part of Vm·e^(j(ωt + φ)) = Vm·e^(jφ) · e^(jωt). In a single-frequency circuit, every voltage and current shares the same e^(jωt) factor — it represents the common rotation in the complex plane at frequency ω. Since this factor is the same everywhere, you can factor it out and set it aside. The **phasor** V̅ = Vm·e^(jφ) = Vm∠φ captures everything that distinguishes one sinusoid from another: its peak amplitude and its phase angle. Written in polar form Vm∠φ or in rectangular form Vm·cos(φ) + j·Vm·sin(φ), it's a static complex number you can add, subtract, and multiply using ordinary complex arithmetic.

The algebraic payoff is immediate and substantial. Consider KVL: in the time domain, summing voltages means adding sinusoids with different phases — messy trigonometric manipulations. In the phasor domain, summing voltages means adding complex numbers: V̅_total = V̅_1 + V̅_2, which is just vector addition in the complex plane. Differentiation — needed for inductors (v = L·di/dt) and capacitors (i = C·dv/dt) — becomes multiplication by jω in the phasor domain. This transforms the differential equations governing inductor and capacitor voltages into algebraic equations: V̅_L = jωL·Ī and Ī_C = jωC·V̅_C. The concept of **complex impedance** follows directly: Z_L = jωL, Z_C = 1/(jωC), and Ohm's law in the phasor domain is simply V̅ = Z·Ī.

A critical boundary condition governs where phasors are valid: they only apply to **single-frequency, sinusoidal steady state**. If a circuit has two independent sources at different frequencies ω₁ and ω₂, you cannot add their phasors directly — they rotate at different rates. Instead, you solve the circuit twice, once at each frequency (two separate phasor analyses), and then add the resulting time-domain signals using superposition. This is not a workaround but reflects a fundamental principle: phasor analysis is a bijection between one frequency's sinusoidal behavior and the complex plane. Mixed-frequency circuits simply have two such bijections operating independently. Once you internalize this constraint, phasors become the natural language for any single-frequency analysis — impedance networks, AC circuit theorems, power calculations, and frequency response all live in the phasor domain.
