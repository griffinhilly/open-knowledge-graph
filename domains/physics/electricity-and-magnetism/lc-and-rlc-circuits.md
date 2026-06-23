---
id: lc-and-rlc-circuits
title: LC and RLC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: rl-circuits
  type: hard
- id: rc-circuits
  type: hard
- id: simple-harmonic-motion
  type: soft
- id: complex-numbers-intro
  type: soft
- id: differential-equations-intro
  type: hard
- id: self-inductance-of-circuits
  type: hard
builds-toward:
- ac-circuits-fundamentals
- ac-power-and-resonance
tags:
- LC-circuit
- RLC-circuit
- oscillation
- resonance
- damping
stage: formal-systems
status: validated
---

# LC and RLC Circuits

## Core Idea
An ideal LC circuit oscillates indefinitely, with charge on the capacitor and current in the inductor exchanging energy at angular frequency ω₀ = 1/√(LC) — the natural resonance frequency. This is directly analogous to a spring-mass oscillator (C ↔ m, L ↔ 1/k, Q ↔ x). Adding resistance gives an RLC circuit with damped oscillations; the quality factor Q = ω₀L/R describes how many oscillations occur before energy dissipates. When driven at ω₀, the circuit resonates.

## How It's Best Learned
Exploit the mechanical analogy: L ↔ mass (inertia), C ↔ compliance (inverse spring constant), R ↔ damping. Write the differential equation for Q(t) and recognize it as the damped harmonic oscillator equation. Solve for underdamped, critically damped, and overdamped cases.

## Common Misconceptions
- The resonance frequency ω₀ = 1/√(LC) is a property of the circuit, not the driving source.
- In an ideal LC circuit, energy oscillates between electric (capacitor) and magnetic (inductor) forms — total energy is conserved.
- The quality factor Q in circuits is different from charge Q — context determines meaning.

## Questions

```yaml
- question: "In an ideal LC circuit undergoing oscillation, at the moment when the capacitor is fully charged (at maximum voltage), which statement best describes the energy state?"
  type: multiple-choice
  options:
    - "All energy is stored as magnetic field energy in the inductor; current is at its peak"
    - "All energy is stored as electric field energy in the capacitor; current through the inductor is instantaneously zero"
    - "Energy is split equally between the capacitor and inductor at all times"
    - "Total energy is zero because no external source is driving the circuit"
  answer: 1
  explanation: "When the capacitor is at maximum charge, all energy is stored as electric potential energy (U_C = Q²/2C is maximum). At this moment current is instantaneously zero, so the inductor stores no magnetic energy (U_L = ½LI² = 0). This is exactly analogous to a spring at maximum displacement: all energy is potential, and the mass (inductor / current) is momentarily stopped. As the capacitor begins to discharge, current builds in the inductor and energy transfers from electric to magnetic form."

- question: "A radio receiver uses a tunable LC circuit to select stations. When ω₀ = 1/√(LC) is adjusted to match a broadcast frequency, why is that station's signal selected over others?"
  type: multiple-choice
  options:
    - "At resonance the circuit's impedance is infinite, blocking all other frequencies"
    - "At resonance, inductive and capacitive reactances cancel, leaving only resistance; impedance is minimized and the circuit draws maximum current at that frequency"
    - "At resonance the circuit converts the electromagnetic signal to a DC voltage that can be amplified"
    - "At resonance the quality factor Q drops to zero, eliminating frequency selectivity"
  answer: 1
  explanation: "At resonance, X_L = ω₀L equals X_C = 1/(ω₀C), so the reactive components cancel and total impedance is minimized (purely resistive). The signal at that frequency drives maximum current. At other frequencies, the reactances do not cancel, impedance is higher, and far less current flows. A higher Q factor means a sharper, more selective resonance peak — better discrimination between adjacent stations."

- question: "In an ideal LC circuit, total electromagnetic energy is conserved; energy oscillates between the electric field of the capacitor and the magnetic field of the inductor."
  type: true-false
  answer: true
  explanation: "With no resistance there is no dissipation mechanism. As the capacitor discharges it drives current through the inductor, which stores energy magnetically. As current decreases, the inductor's collapsing field drives charge back onto the capacitor. The total energy U = Q²/(2C) + LI²/2 remains constant throughout, oscillating between its two forms — a direct electrical analog of a frictionless spring-mass system."

- question: "Adding more resistance to an RLC circuit increases its quality factor Q, producing a sharper and more selective resonance."
  type: true-false
  answer: false
  explanation: "Quality factor Q = ω₀L/R: increasing R decreases Q. A higher Q means more oscillation cycles before energy dissipates (longer ring-down) and a narrower resonance peak — better frequency selectivity. More resistance means more energy lost per cycle, a broader flatter peak, and worse frequency discrimination. High-Q components (low-loss inductors and capacitors) are prized precisely because they minimize resistance relative to reactive impedance."

- question: "Describe the mechanical analogy for an LC circuit: what circuit element corresponds to mass, what corresponds to the spring, and what corresponds to displacement? Use the analogy to explain why increasing L or C lowers the resonance frequency."
  type: short-answer
  answer: "The inductor L corresponds to mass (inertia — it resists changes in current). The capacitor C corresponds to the spring's compliance (inverse stiffness — it stores potential energy proportional to charge squared). Charge Q corresponds to displacement. The resonance frequency ω₀ = 1/√(LC) parallels ω₀ = √(k/m) in mechanics. A larger inductance (more 'inertia') slows the oscillation. A larger capacitance (more 'compliance,' softer 'spring') also slows it."
  explanation: "The analogy is mathematically exact: L d²Q/dt² + Q/C = 0 is identical in form to m d²x/dt² + kx = 0, with L ↔ m, 1/C ↔ k, and Q ↔ x. This mapping lets you transfer all of simple harmonic motion's insights — energy conservation, phase relationships, resonance behavior — directly to LC circuits without re-deriving them from scratch."
```

## Explainer

From your study of RC and RL circuits, you know that each alone shows only exponential decay: a capacitor discharges through a resistor with time constant τ = RC; an inductor's current decays through a resistor with τ = L/R. When you combine a capacitor and an inductor without resistance, something qualitatively different happens. Instead of settling toward zero, energy bounces back and forth between the two elements indefinitely. This is **electromagnetic oscillation**, and it is the electrical counterpart of the mechanical oscillation you studied in simple harmonic motion.

The analogy is exact and worth internalizing: the capacitor plays the role of a spring (storing potential energy, proportional to charge²), and the inductor plays the role of a mass (storing kinetic energy, proportional to current²). When the capacitor is fully charged, the current is zero — analogous to a spring at maximum displacement with the mass momentarily stopped. As the capacitor discharges, current builds up in the inductor; this is like the spring releasing and the mass accelerating. When the capacitor is fully discharged, current is at its peak — analogous to the mass at the equilibrium point with maximum velocity. The inductor then forces the charge to continue flowing, recharging the capacitor in the opposite polarity, and the cycle repeats. The governing differential equation is L(d²Q/dt²) + Q/C = 0, which is mathematically identical to the harmonic oscillator equation with ω₀ = 1/√(LC).

Adding resistance creates an **RLC circuit** and introduces damping, just as friction damps a mechanical oscillator. The full equation L(d²Q/dt²) + R(dQ/dt) + Q/C = 0 has three regimes depending on the **damping ratio** ζ = R/(2√(L/C)): underdamped (ζ < 1, oscillations that decay exponentially), critically damped (ζ = 1, fastest approach to equilibrium without oscillating), and overdamped (ζ > 1, slow exponential decay). In practice, most resonant circuits are designed to be underdamped. The **quality factor** Q_factor = ω₀L/R quantifies how sharp the resonance is — a high Q circuit rings many times before its energy dissipates, while a low Q circuit loses energy quickly.

Resonance occurs when an external driving source is applied at exactly ω₀. At resonance, the capacitive and inductive **reactances** cancel (X_L = ω₀L and X_C = 1/(ω₀C) are equal), so the circuit looks like a pure resistance. This is why radio tuning works: by adjusting L or C, you shift ω₀ until it matches the broadcast frequency, at which point that station's signal drives the circuit at resonance, producing maximum current. All other frequencies drive the circuit off-resonance and produce much smaller currents. The sharper the resonance (higher Q), the better the frequency selectivity.
