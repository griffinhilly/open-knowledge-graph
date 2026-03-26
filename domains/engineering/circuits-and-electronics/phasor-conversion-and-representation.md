---
id: phasor-conversion-and-representation
title: Phasor Conversion and Representation
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: sinusoidal-steady-state-analysis
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
stage: formal-systems
status: validated
---

# Phasor Conversion and Representation

## Core Idea
A phasor is a complex number representing the amplitude and phase of a sinusoid. The transformation v(t) = Re[V̅ e^(jωt)] converts time-domain sinusoids to frequency-domain phasors V̅ = |V|e^(jφ). This greatly simplifies AC circuit analysis by converting differential equations into algebraic equations.

## How It's Best Learned
Practice converting between time-domain and phasor domains. Use Euler's formula e^(jθ) = cos(θ) + j sin(θ) to move between rectangular and polar forms. Verify using circuit simulations.

## Common Misconceptions
- Phasors only apply to single-frequency signals. - A phasor magnitude is the same as peak voltage; RMS values are used in phasors. - Phasor addition in the complex plane is vector addition, not scalar addition.

## Questions

```yaml
- question: "A circuit has two voltage sources: V₁ = 10cos(100t + 30°) V and V₂ = 5cos(200t + 45°) V. How should you find the total voltage using phasors?"
  type: multiple-choice
  options:
    - "Add the phasors directly: V̅_total = 10∠30° + 5∠45° = 15∠37.5° V"
    - "You cannot add these phasors directly — they operate at different frequencies. Solve the circuit separately at 100 rad/s and at 200 rad/s, then add the resulting time-domain signals"
    - "Convert both to rectangular form and add: (10cos30° + 5cos45°) + j(10sin30° + 5sin45°)"
    - "Phasors cannot represent this circuit at all since superposition does not apply in AC circuits"
  answer: 1
  explanation: "Phasors are only valid for single-frequency steady state. The phasor representation freezes the common e^(jωt) factor — but if two sources have different ω values, there is no common factor to freeze. You must perform two separate phasor analyses (one at ω=100, one at ω=200), find the contributions from each source independently, convert both results back to time domain, and then add the time-domain expressions. Superposition is valid; phasor addition across different frequencies is not."

- question: "An inductor carries a sinusoidal current i(t) = 2cos(1000t + 30°) A. The inductor has L = 0.01 H. What is the phasor voltage across the inductor?"
  type: multiple-choice
  options:
    - "V̅ = 2∠30° V — the voltage phasor equals the current phasor for inductors"
    - "V̅ = jωL × Ī = j(1000)(0.01) × 2∠30° = j10 × 2∠30° = 20∠120° V"
    - "V̅ = L × dĪ/dt = 0.01 × j × 2∠30° = 0.02∠120° V"
    - "V̅ = 2∠(30°+90°) = 2∠120° V — inductors only shift phase by 90°"
  answer: 1
  explanation: "In the phasor domain, the inductor voltage is V̅ = jωL × Ī. Here ω = 1000 rad/s, L = 0.01 H, so jωL = j10. Multiplying: j10 × 2∠30° = 10∠90° × 2∠30° = 20∠120° V. The key transformation is that differentiation in time domain (v = L di/dt) becomes multiplication by jω in phasor domain — this is what converts the differential equation to algebra. Option D gets the phase right but loses the magnitude scaling by ωL."

- question: "A phasor representation of a sinusoidal voltage captures most of the information needed to reconstruct the original time-domain signal."
  type: true-false
  answer: false
  explanation: "A phasor captures amplitude and phase but NOT frequency. The phasor V̅ = Vm∠φ tells you the peak magnitude Vm and the phase shift φ, but to reconstruct v(t) = Vm·cos(ωt + φ) you also need to know ω. In phasor analysis, ω is assumed known and fixed throughout (single-frequency constraint); it is carried implicitly as context, not stored in the phasor itself. This is why phasors only work for single-frequency circuits — without a specified ω, the phasor is incomplete."

- question: "In phasor domain, adding two voltages is done by adding complex numbers, which is the same as adding their magnitudes directly."
  type: true-false
  answer: false
  explanation: "Phasor addition is vector addition in the complex plane — you add real parts together and imaginary parts together. Adding magnitudes directly (scalar addition) ignores phase and gives the wrong answer whenever the phases differ. For example, 10∠0° + 10∠90° = (10 + 0j) + (0 + 10j) = 10 + 10j = 10√2 ∠45°, not 20∠45°. Only when two phasors are exactly in phase (same angle) does the magnitude of the sum equal the sum of the magnitudes. The misconception arises from everyday intuition about adding 'voltages' without thinking about phase."

- question: "Explain why differentiation in the time domain becomes multiplication by jω in the phasor domain, and why this matters for AC circuit analysis."
  type: short-answer
  answer: "A sinusoid v(t) = Vm·cos(ωt + φ) can be written as Re[Vm·e^(jφ)·e^(jωt)]. Differentiating: dv/dt = Re[jω·Vm·e^(jφ)·e^(jωt)]. The e^(jωt) factor is just the rotating phasor base; multiplying Vm·e^(jφ) by jω gives jω·V̅ in the phasor domain. Since j = e^(jπ/2), multiplication by jω scales the magnitude by ω and rotates the phase by 90°. This matters because inductor voltage (v = L·di/dt) and capacitor current (i = C·dv/dt) involve derivatives — replacing differentiation with jω multiplication turns these differential equations into algebraic equations V̅ = jωL·Ī and Ī = jωC·V̅, enabling Ohm's law and KVL/KCL to work algebraically in the frequency domain."
  explanation: "This is the core payoff of phasor analysis. Without it, solving an AC circuit would require setting up and solving coupled differential equations for each branch. With it, you treat every element as having a complex impedance (Z_R = R, Z_L = jωL, Z_C = 1/jωC), apply Kirchhoff's laws as complex algebra, and solve with standard algebraic techniques. The transformation is a kind of structured simplification that works precisely because all signals share the same frequency."
```

## Explainer

In your prerequisite work, you learned that AC circuits in steady state have voltages and currents oscillating at the same frequency as the source — only the amplitudes and phases differ from branch to branch. You also learned Euler's formula: e^(jθ) = cos(θ) + j·sin(θ), which connects complex exponentials to sinusoids. Phasors bring these two ideas together into one powerful transformation: they let you represent any sinusoidal signal as a single complex number, freezing the time-varying behavior into a static amplitude and phase angle that you can manipulate with algebra instead of calculus.

The conversion starts from the observation that any sinusoid v(t) = Vm·cos(ωt + φ) can be written as the real part of Vm·e^(j(ωt + φ)) = Vm·e^(jφ) · e^(jωt). In a single-frequency circuit, every voltage and current shares the same e^(jωt) factor — it represents the common rotation in the complex plane at frequency ω. Since this factor is the same everywhere, you can factor it out and set it aside. The **phasor** V̅ = Vm·e^(jφ) = Vm∠φ captures everything that distinguishes one sinusoid from another: its peak amplitude and its phase angle. Written in polar form Vm∠φ or in rectangular form Vm·cos(φ) + j·Vm·sin(φ), it's a static complex number you can add, subtract, and multiply using ordinary complex arithmetic.

The algebraic payoff is immediate and substantial. Consider KVL: in the time domain, summing voltages means adding sinusoids with different phases — messy trigonometric manipulations. In the phasor domain, summing voltages means adding complex numbers: V̅_total = V̅_1 + V̅_2, which is just vector addition in the complex plane. Differentiation — needed for inductors (v = L·di/dt) and capacitors (i = C·dv/dt) — becomes multiplication by jω in the phasor domain. This transforms the differential equations governing inductor and capacitor voltages into algebraic equations: V̅_L = jωL·Ī and Ī_C = jωC·V̅_C. The concept of **complex impedance** follows directly: Z_L = jωL, Z_C = 1/(jωC), and Ohm's law in the phasor domain is simply V̅ = Z·Ī.

A critical boundary condition governs where phasors are valid: they only apply to **single-frequency, sinusoidal steady state**. If a circuit has two independent sources at different frequencies ω₁ and ω₂, you cannot add their phasors directly — they rotate at different rates. Instead, you solve the circuit twice, once at each frequency (two separate phasor analyses), and then add the resulting time-domain signals using superposition. This is not a workaround but reflects a fundamental principle: phasor analysis is a bijection between one frequency's sinusoidal behavior and the complex plane. Mixed-frequency circuits simply have two such bijections operating independently. Once you internalize this constraint, phasors become the natural language for any single-frequency analysis — impedance networks, AC circuit theorems, power calculations, and frequency response all live in the phasor domain.
