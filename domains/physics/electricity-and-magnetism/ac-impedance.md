---
id: ac-impedance
title: AC Circuits and Complex Impedance
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: lenzs-law
  type: soft
- id: rl-transient-response
  type: hard
- id: complex-numbers-intro
  type: hard
- id: operations-with-complex-numbers
  type: hard
builds-toward:
- rlc-resonance
tags:
- ac
- impedance
- phasor
stage: formal-systems
status: validated
---

# AC Circuits and Complex Impedance

## Core Idea
For sinusoidal AC signals at frequency ω, impedance Z relates voltage to current. For a resistor: Z = R; capacitor: Z = 1/(iωC); inductor: Z = iωL. Complex impedances combine like resistances: series adds Z, parallel adds 1/Z. Impedance captures both magnitude and phase relationship between voltage and current. AC power includes real (P = IV cos φ) and reactive components.

## Questions

```yaml
- question: "In an AC circuit, as the frequency ω increases, what happens to the magnitude of a capacitor's impedance?"
  type: multiple-choice
  options:
    - "It increases, because higher frequency means the capacitor charges and discharges faster, opposing more current."
    - "It decreases, because |Z_C| = 1/(ωC) and magnitude shrinks as ω grows."
    - "It stays the same; impedance is a fixed property of the component regardless of frequency."
    - "It becomes purely real at high frequencies because the imaginary part cancels."
  answer: 1
  explanation: "Z_C = 1/(iωC), so |Z_C| = 1/(ωC). As ω increases, the denominator grows and impedance magnitude shrinks toward zero — a capacitor becomes a near short-circuit at high frequencies. This is physically intuitive: at high frequencies, the capacitor charges and discharges so quickly that it passes AC current easily. At low frequencies (ω → 0), Z_C → ∞, meaning the capacitor blocks DC entirely. This frequency-dependence is the whole point of using capacitors as frequency-selective filters."

- question: "An inductor has impedance Z = iωL. What does the phase angle of this impedance tell you about the relationship between voltage and current?"
  type: multiple-choice
  options:
    - "Voltage and current are in phase, so all power delivered to the inductor is dissipated as heat."
    - "Voltage leads current by 90°, meaning the inductor stores and returns energy each cycle rather than dissipating it."
    - "Current leads voltage by 90°, so the inductor behaves capacitively at all frequencies."
    - "The inductor has zero resistance, so it dissipates no power and the phase angle is irrelevant."
  answer: 1
  explanation: "Z = iωL has argument (phase) = +90°. In the phasor representation, voltage is proportional to Z times current; the +90° phase means voltage leads current by a quarter cycle. This 90° phase difference is the signature of a purely reactive element: power flows into the inductor for half a cycle and returns to the source during the other half, so average power dissipation is zero. Option C (current leads voltage) describes a capacitor, where Z_C has phase −90°."

- question: "In AC circuit analysis, complex impedances combine using the same series and parallel combination rules as DC resistances."
  type: true-false
  answer: true
  explanation: "This is the central payoff of the phasor/impedance formalism. Because Kirchhoff's voltage and current laws hold for phasors (complex amplitudes), the same algebraic derivations that give Z_series = Z₁ + Z₂ and 1/Z_parallel = 1/Z₁ + 1/Z₂ for resistors apply equally to complex impedances. The only difference is that the arithmetic involves complex numbers instead of real ones. This turns AC circuit analysis — which would otherwise require solving systems of differential equations — into routine algebra."

- question: "A circuit with a high power factor draws large peak currents because it stores most of the energy supplied to it."
  type: true-false
  answer: false
  explanation: "This reverses the relationship. A *low* power factor (cos φ near 0) is the problematic case: voltage and current are nearly 90° out of phase, so large peak currents flow back and forth between source and circuit without delivering useful real power. P = (1/2)V₀I₀ cos φ, so when cos φ is small, you need large V₀I₀ to deliver modest P. A high power factor (cos φ near 1) means voltage and current are nearly in phase, so most of the current flow does useful work — exactly the efficient case. Low power factor is the engineering problem to fix."

- question: "Why does representing AC voltages and currents as complex phasors turn differential equations into algebraic equations?"
  type: short-answer
  answer: "Differentiating a complex exponential Ae^(iωt) simply multiplies it by iω — a constant. So d/dt → ×iω and ∫dt → ÷iω. This means the inductor's constitutive relation V = L dI/dt becomes V = iωL · I in phasor form (dividing out the common e^(iωt) factor), defining impedance Z_L = iωL. Similarly, the capacitor's I = C dV/dt becomes I = iωC · V, giving Z_C = 1/(iωC). The differential relationships become multiplicative ones, turning the circuit's system of differential equations into a system of linear algebraic equations solvable by standard circuit techniques."
  explanation: "The magic is the derivative rule for exponentials: d/dt[e^(iωt)] = iω·e^(iωt). Since all voltages and currents at a single frequency share the same e^(iωt) time factor, that factor cancels everywhere, leaving only the complex amplitudes (phasors) and multiplicative factors of iω. This reduces the problem from calculus to algebra — the key reason why impedance-based AC analysis is so powerful and so widely used in electrical engineering."
```

## Explainer

From your work on RL transient circuits, you know that inductors and capacitors create time delays — voltage and current don't peak at the same moment. In DC transient analysis you tracked this with exponentials. In AC circuits, the input is sinusoidal and persists forever, so you need a tool that captures steady-state phase relationships compactly. That tool is **complex impedance**.

The key insight is that complex numbers encode both magnitude and phase in one object. A sinusoidal voltage V(t) = V₀cos(ωt + φ) is represented as the real part of V₀e^(i(ωt + φ)) — a complex exponential. When you differentiate or integrate a complex exponential, you just multiply by iω or divide by iω, turning calculus into algebra. This is why the capacitor's relation V = Q/C becomes, in terms of current I = dQ/dt, the impedance Z_C = V/I = 1/(iωC). Similarly, the inductor's V = L dI/dt gives Z_L = iωL. The resistor has no time dependence, so Z_R = R — a purely real number with no phase shift.

The **phasor** is the complex amplitude itself (dropping the e^(iωt) factor). Once you represent every voltage and current as a phasor, Kirchhoff's laws still hold — but now in the complex plane. This means you can solve AC circuits using exactly the same series and parallel combination rules you learned for resistors, just with complex numbers. The magnitude |Z| gives the ratio of peak voltage to peak current, and the angle arg(Z) gives the phase by which voltage leads current. For an inductor (Z = iωL), arg(Z) = +90°, meaning voltage leads current by a quarter cycle. For a capacitor (Z = 1/iωC = -i/ωC), arg(Z) = −90°, so current leads voltage.

**AC power** adds one more subtlety. When voltage and current are in phase (as in a resistor), all power goes into heat — this is **real power** P = (1/2)V₀I₀. When they are 90° out of phase (pure inductor or capacitor), energy sloshes back and forth between source and element each cycle but averages to zero — this is **reactive power**. The **power factor** cos φ (where φ is the phase angle between voltage and current) interpolates between these extremes, so P = (1/2)V₀I₀ cos φ. A circuit with a low power factor draws large peak currents to deliver modest real power, which matters enormously in electrical engineering. The complex impedance framework makes all of this computable from the circuit topology without ever writing down a differential equation.
