---
id: ac-source-representation-phasors
title: AC Sources and Phasor Representation
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: complex-numbers-intro
  type: hard
- id: complex-exponential-function
  type: soft
- id: complex-exponential-form
  type: hard
builds-toward:
- phasor-algebra-complex-impedance
- ac-circuit-analysis-methods
tags:
- ac-sources
- phasors
- ac-analysis
stage: advanced
status: validated
---

# AC Sources and Phasor Representation

## Core Idea
AC sources produce sinusoidal voltage and current: v(t) = V_m·sin(ωt + φ). Phasor representation converts sinusoidal signals to complex numbers in the frequency domain: V = V_m∠φ = V_m·e^(jφ). This transformation converts differential equations to algebraic equations, making AC circuit analysis practical. Phasors assume all signals operate at the same frequency, a reasonable assumption for circuits with one source frequency.

## Questions

```yaml
- question: "What is the fundamental reason that phasor analysis converts differential equations (from capacitors and inductors) into algebraic equations?"
  type: multiple-choice
  options:
    - "Phasors use complex numbers, which obey special algebraic rules that bypass calculus entirely"
    - "All signals in a single-frequency circuit share the same e^(jωt) factor, so differentiation in time corresponds to multiplying the phasor by jω — a purely algebraic operation"
    - "Phasors work in the frequency domain where time does not exist, making differential equations irrelevant"
    - "Capacitors and inductors become equivalent to resistors in phasor analysis, removing all reactive behavior from the equations"
  answer: 1
  explanation: "The key is that when all signals have the same frequency ω, differentiating a sinusoid v(t) = Re{V·e^(jωt)} gives d/dt[Re{V·e^(jωt)}] = Re{jω·V·e^(jωt)}. The e^(jωt) factor is common to every signal in the circuit and cancels out of all equations — what remains is multiplication by jω, a purely algebraic operation. The differential equation i = C·dv/dt becomes I = jωC·V in the phasor domain. This is not a trick or approximation; it is an exact consequence of assuming sinusoidal steady-state with a single frequency."

- question: "An engineer analyzes a circuit driven by two AC sources: one at 60 Hz and one at 180 Hz. What problem arises if she tries to apply phasor analysis to both sources simultaneously?"
  type: multiple-choice
  options:
    - "Phasor analysis cannot handle sources with different phases, so sources at the same frequency with phase offsets must also be treated separately"
    - "The 180 Hz source is the third harmonic of the 60 Hz source, so they automatically combine and phasor analysis works normally"
    - "Phasor analysis assumes all signals share a single frequency; at two different frequencies, signals cannot be combined in a single phasor diagram — superposition across two separate single-frequency analyses is required"
    - "The two frequencies create a time-varying impedance for capacitors and inductors, making the circuit nonlinear"
  answer: 2
  explanation: "Phasors encode amplitude and phase only — they strip out the e^(jωt) factor. This is only valid when every signal in the circuit has the same ω. If two sources have different frequencies, their phasors cannot be combined directly because they correspond to different e^(jωt) factors. The correct approach is superposition: analyze the circuit twice (once for each frequency using that frequency's impedances), then add the time-domain responses. At 60 Hz, a capacitor has impedance 1/(j·2π·60·C); at 180 Hz, it has impedance 1/(j·2π·180·C) — these are different, so the circuits are effectively different problems."

- question: "Phasor analysis is an approximation that gives slightly different answers than solving the time-domain differential equations directly."
  type: true-false
  answer: false
  explanation: "Phasor analysis gives exactly the same answers as direct time-domain differential equation solution for linear circuits in sinusoidal steady state. The derivation is rigorous: a sinusoid is the real part of a complex exponential (Euler's formula), and for linear circuits, the real-part operation and the circuit equations commute. Solving in the phasor domain and then recovering the time-domain answer (attach e^(jωt), take real part) is mathematically identical to solving the differential equations directly. Phasor analysis is a transformation technique, not an approximation — it trades calculus for algebra while preserving exactness."

- question: "A sinusoidal voltage v(t) = 20·cos(500t − 45°) volts is fully described by the phasor V = 20∠−45° when the circuit's operating frequency is known."
  type: true-false
  answer: true
  explanation: "The phasor encodes the two pieces of information that distinguish one sinusoid from another in a single-frequency circuit: amplitude (20 V) and phase (−45°). The angular frequency ω = 500 rad/s is a shared circuit parameter, not carried in the phasor itself. To recover the time-domain signal: v(t) = Re{20∠−45° · e^(j500t)} = 20·cos(500t − 45°). As long as ω is known, the phasor contains complete information about the signal."

- question: "A capacitor has impedance Z_C = 1/(jωC) in phasor analysis. Explain where the 'jω' comes from — derive it from the capacitor's time-domain current-voltage relationship."
  type: short-answer
  answer: "The time-domain relationship is i(t) = C·dv/dt. In phasor analysis, if v(t) = Re{V·e^(jωt)}, then dv/dt = Re{jω·V·e^(jωt)}, so i(t) = Re{C·jω·V·e^(jωt)} = Re{I·e^(jωt)} where I = jωC·V. Solving for the impedance V/I = 1/(jωC). The jω factor arises directly from differentiating the complex exponential e^(jωt): d/dt[e^(jωt)] = jω·e^(jωt). The factor j represents the 90° phase lead of current over voltage in a capacitor; the ω represents that the current magnitude grows with frequency (a capacitor passes high-frequency signals more easily than low-frequency ones)."
  explanation: "This derivation shows that phasor impedances are not definitions or conventions — they are exact consequences of applying calculus to complex exponentials and then stripping the common e^(jωt) factor. The same derivation for an inductor gives V = L·di/dt → Z_L = jωL, capturing that inductors block high frequencies. The frequency dependence baked into j/ω and jω is what makes reactive circuit design possible."
```

## Explainer

You've worked with DC circuits where voltages and currents are constant. AC circuits introduce a new complication: voltages and currents vary sinusoidally with time. A sinusoidal voltage v(t) = V_m·sin(ωt + φ) has three properties you need to track simultaneously: its **amplitude** V_m (peak value), its **angular frequency** ω (how fast it oscillates, in radians per second), and its **phase** φ (where in its cycle it starts at t = 0). Analyzing circuits with reactive elements under sinusoidal excitation means solving differential equations — the current through a capacitor is C·dv/dt, the voltage across an inductor is L·di/dt. Doing this from scratch for every circuit would be prohibitively tedious.

**Phasor representation** is the key simplification. If you know that every signal in a circuit oscillates at the same frequency ω — a reasonable assumption when there is one AC source — then the only information that distinguishes one signal from another is its amplitude and phase. The phasor for v(t) = V_m·sin(ωt + φ) is simply the complex number V = V_m∠φ = V_m·e^(jφ). You have encoded all the relevant information into a single complex number, stripping away the time-varying factor e^(jωt) that is identical for every signal in the circuit.

The power of this representation becomes apparent when you differentiate. In the time domain, differentiating a sinusoid gives another sinusoid at the same frequency but with shifted phase and scaled amplitude. In the phasor domain, this corresponds to multiplying by jω — a purely algebraic operation. This is the central insight: **differential equations in the time domain become algebraic equations in the phasor domain**. Kirchhoff's voltage and current laws still hold, but now applied to complex numbers rather than time-varying functions. Series and parallel combinations, voltage dividers, node voltage analysis — all of the techniques you know from resistive circuits carry over to AC circuits once you replace resistances with complex **impedances**: R for resistors, 1/(jωC) for capacitors, and jωL for inductors.

The connection to complex exponentials (your prerequisite) is what makes this rigorous rather than a computational trick. Euler's formula gives e^(jθ) = cos(θ) + j·sin(θ), so a sinusoid is the real part of a rotating complex exponential: V_m·cos(ωt + φ) = Re{V_m·e^(jφ)·e^(jωt)}. The phasor V = V_m·e^(jφ) is the complex amplitude — the "snapshot" of the rotating vector at t = 0. When you solve a circuit in the phasor domain and want the time-domain answer, you attach e^(jωt) back and take the real part. This formal grounding ensures that phasor analysis gives exactly the same answers as solving the differential equations directly — just far more efficiently.
