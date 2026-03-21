---
id: sinusoidal-steady-state-analysis
title: AC Steady-State Circuit Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: series-parallel-rc-and-rl-networks
  type: hard
- id: circuit-theorems-linearity
  type: hard
builds-toward:
- phasor-notation-and-complex-algebra
tags:
- ac-analysis
- steady-state
- sinusoidal
- rms
stage: formal-systems
status: draft
---

# AC Steady-State Circuit Analysis

## Core Idea
AC steady-state analysis applies when circuits are excited by sinusoidal sources at frequency ω and transients have decayed. Circuit responses are sinusoidal at the same frequency with different amplitude and phase. Analysis uses RMS (root-mean-square) values for amplitudes and phasor notation to convert time-domain differential equations to algebraic equations.

## Questions

```yaml
- question: "What is the impedance of an ideal capacitor with capacitance C at angular frequency ω?"
  type: multiple-choice
  options:
    - "jωC"
    - "1/(jωC)"
    - "jω/C"
    - "ωC"
  answer: 1
  explanation: "For a capacitor, i = C·dv/dt. In phasor form, differentiation becomes multiplication by jω, so I = jωC·V, and impedance Z = V/I = 1/(jωC). This can also be written as −j/(ωC), emphasizing that the impedance is purely imaginary and negative — current leads voltage by 90°. Option A (jωC) is the impedance of an inductor, a common mix-up. The key sign difference: inductors have positive imaginary impedance (jωL), capacitors have negative (−j/ωC)."

- question: "In AC steady-state analysis using phasors, how does Kirchhoff's Voltage Law (KVL) get applied?"
  type: multiple-choice
  options:
    - "KVL applies to peak amplitudes only, since all voltages share the same frequency"
    - "KVL applies to phasor voltages (complex numbers), using the same algebraic sum rule as in DC circuits"
    - "KVL requires integration over one complete cycle to handle the phase differences"
    - "KVL applies to RMS values only, with a separate correction for phase"
  answer: 1
  explanation: "Once voltages are represented as phasors (complex numbers encoding amplitude and phase), KVL says the sum of phasor voltages around any loop equals zero — the exact same algebraic rule as DC. This is the entire point of the phasor transformation: it converts the differential equations of time-domain AC analysis into algebraic equations, so all linear analysis tools (KVL, KCL, nodal analysis, mesh analysis, Thévenin/Norton) apply unchanged, just with complex numbers instead of real ones."

- question: "An ideal capacitor connected to an AC source dissipates significant average power because current flows through it continuously."
  type: true-false
  answer: false
  explanation: "A purely reactive element (ideal capacitor or inductor) dissipates zero average power. Average power P = V_rms · I_rms · cos(θ), where θ is the phase angle between voltage and current. For an ideal capacitor, θ = 90° (current leads voltage by 90°), so cos(90°) = 0, giving P = 0. Energy is stored and returned each half-cycle but never dissipated. Only the resistive component of impedance (the real part) dissipates power."

- question: "In sinusoidal steady state, every voltage and every current in a linear circuit oscillates at exactly the same frequency as the driving source, though with different amplitudes and phases."
  type: true-false
  answer: true
  explanation: "This is the fundamental property that makes phasor analysis possible. Because all circuit elements are linear (satisfying superposition), a sinusoidal input at frequency ω produces sinusoidal responses at the same frequency ω throughout the circuit. The frequency is preserved; only amplitude and phase change from element to element. If two sources at different frequencies were present, superposition would be applied separately for each frequency."

- question: "What is the key mathematical insight that allows the differential equations governing capacitors and inductors to be replaced by simple algebraic equations in phasor analysis?"
  type: short-answer
  answer: "In phasor analysis, differentiating with respect to time (d/dt) is equivalent to multiplying by jω. This follows from Euler's formula: if v(t) = Re[V·e^(jωt)], then dv/dt = Re[jω·V·e^(jωt)]. So the capacitor equation i = C·dv/dt becomes I = jωC·V in phasor form — a simple algebraic relation. Similarly, the inductor equation v = L·di/dt becomes V = jωL·I. Differentiation becomes multiplication by the constant jω, turning differential equations into linear algebraic equations."
  explanation: "This transformation is the core payoff of phasor analysis. The price is working with complex numbers; the reward is that all differential equations become algebraic, and the entire toolkit of linear circuit analysis applies directly. This is why electrical engineers can solve complicated AC circuits using the same techniques as DC circuits, just with complex-valued impedances instead of real resistances."
```

## Explainer

From your work with RC and RL networks, you know that when you apply a sudden step voltage, the circuit responds with an exponential transient — a decaying response that reflects the energy stored in capacitors and inductors. Sinusoidal steady-state analysis is what happens after those transients die out: the circuit has settled into a regime where every voltage and current oscillates at exactly the same frequency as the source, differing only in **amplitude** and **phase**. This is the "steady state" — not that nothing is changing, but that the pattern of change has stabilized into a permanent sinusoidal rhythm.

The mathematical insight that makes AC analysis tractable is Euler's formula: e^(jωt) = cos(ωt) + j·sin(ωt). A real sinusoid v(t) = V_m cos(ωt + φ) is the real part of the complex exponential V_m e^(j(ωt + φ)) = V_m e^(jφ) · e^(jωt). Since the e^(jωt) factor is common to every voltage and current in the circuit (they all oscillate at ω), it can be factored out, leaving only the **phasor** V = V_m e^(jφ) = V_m ∠φ — a complex number encoding amplitude and phase. Taking derivatives in time becomes multiplication by jω in phasor space, which turns the differential equations governing capacitors (i = C dv/dt) and inductors (v = L di/dt) into algebraic relations: phasor current = jωC times phasor voltage for a capacitor, and phasor voltage = jωL times phasor current for an inductor.

This is where **impedance** emerges. Define impedance Z as the phasor voltage divided by phasor current: for a resistor Z_R = R (real, no phase shift), for a capacitor Z_C = 1/(jωC) = −j/(ωC) (imaginary, current leads voltage by 90°), for an inductor Z_L = jωL (imaginary, voltage leads current by 90°). With impedances defined, all the linear circuit analysis tools you know — KVL, KCL, Thévenin/Norton equivalents, voltage dividers, nodal and mesh analysis — apply directly to phasors and impedances. The entire toolkit transfers intact; the only change is that resistances become complex impedances and real voltages become complex phasors.

**RMS values** complete the picture for power calculations. The RMS value of a sinusoid V_m cos(ωt) is V_m/√2 ≈ 0.707 V_m — it is the equivalent DC voltage that delivers the same average power to a resistor. Wall outlets are specified in RMS (120 V in the US means V_m ≈ 170 V peak), and AC power calculations use RMS amplitudes throughout. The average power delivered to an impedance is P = V_rms · I_rms · cos(θ), where θ is the phase angle between voltage and current — a result that reduces to the familiar P = V²/R = I²R for purely resistive loads (θ = 0) and gives zero average power for purely reactive loads (θ = ±90°). This frequency-domain approach, developed in full in phasor notation, is the foundation for understanding filters, resonance, power systems, and every AC circuit you will encounter in subsequent work.
