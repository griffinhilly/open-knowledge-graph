---
id: capacitor-inductor-energy-storage
title: Capacitors and Inductors as Energy Storage Elements
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: capacitance
  type: hard
- id: inductance-and-inductors
  type: hard
- id: differential-equations-intro-separable
  type: soft
- id: energy-stored-in-fields
  type: soft
builds-toward:
- first-order-transient-circuits
- second-order-transient-circuits
- phasor-representation
tags:
- capacitors
- inductors
- energy-storage
- initial-conditions
- continuity
stage: formal-systems
status: validated
---

# Capacitors and Inductors as Energy Storage Elements

## Core Idea
Capacitors store energy in the electric field: E = ½CV², with i = C(dv/dt); voltage cannot change instantaneously because that would require infinite current. Inductors store energy in the magnetic field: E = ½LI², with v = L(di/dt); current cannot change instantaneously because that would require infinite voltage. Series and parallel combinations follow rules dual to resistors (capacitors in series combine like resistors in parallel, and vice versa). Initial conditions on capacitor voltage and inductor current at the moment of a switching event determine the starting state for all transient analysis.

## How It's Best Learned
Derive the i-v relationships from the definitions of capacitance (Q = CV) and inductance (λ = LI) rather than memorizing them. Practice computing energy stored and identifying initial and final conditions before writing any differential equations.

## Common Misconceptions
- Assuming capacitor voltage or inductor current can jump instantaneously — instantaneous change requires infinite power, which is physically impossible.
- Applying resistor series/parallel rules directly to capacitors without adjustment.
- Neglecting initial conditions when solving transient circuit equations.

## Questions

```yaml
- question: "Capacitors and inductors follow a duality principle for series/parallel combinations. Which statement correctly describes this duality?"
  type: multiple-choice
  options:
    - "Capacitors in series combine like resistors in series; inductors in parallel combine like resistors in parallel."
    - "Capacitors in series combine like resistors in parallel; inductors in parallel combine like resistors in series."
    - "Capacitors in parallel combine like resistors in parallel; inductors in series combine like resistors in series."
    - "Capacitors and inductors both follow the same series/parallel rules as resistors."
  answer: 1
  explanation: "The duality flips the rules: capacitors in series add reciprocals (1/C_total = 1/C1 + 1/C2), just as resistors in parallel do, while capacitors in parallel add directly. Inductors in series add directly (like resistors in series) and in parallel add reciprocals. This duality arises because C and L play symmetric roles when you swap voltage and current."

- question: "A capacitor's voltage can change instantaneously if a large enough current pulse is applied."
  type: true-false
  answer: false
  explanation: "The capacitor's i-v relationship is i = C(dv/dt). An instantaneous voltage change would require dv/dt → ∞, which demands infinite current. No physical source can supply infinite current, so capacitor voltage cannot change instantaneously. The same logic applies dually to inductor current: v = L(di/dt) means instantaneous current change would require infinite voltage."

- question: "At the moment a switch closes in a circuit containing an inductor, why is the inductor current treated as a known initial condition rather than solved as an unknown?"
  type: short-answer
  answer: "Inductor current cannot change instantaneously because an instantaneous change would require infinite voltage (v = L·di/dt). Therefore the current immediately after switching equals the current immediately before switching. This continuity constraint sets the initial condition that the transient solution must satisfy."
  explanation: "Energy stored in the inductor's magnetic field is E = ½LI². For this energy to change instantaneously, an infinite power would be required, which is physically impossible. The initial current value anchors the solution to the differential equation governing the circuit's transient response."
```

## Explainer

The i-v relationships for capacitors and inductors are not arbitrary formulas — they follow directly from the definitions of capacitance and inductance. Capacitance is defined by Q = CV: the charge stored equals capacitance times voltage. Differentiate both sides with respect to time and you get i = C(dv/dt). Similarly, inductance is defined through magnetic flux linkage λ = LI; Faraday's law gives v = dλ/dt = L(di/dt). These two relationships are the starting point for all capacitor and inductor analysis.

The most important consequence of these relationships is the instantaneous-change prohibition. If a capacitor's voltage jumped from 5 V to 10 V in zero time, then dv/dt would be infinite, requiring infinite current — an impossibility. Likewise, if an inductor's current jumped instantaneously, v = L(di/dt) would be infinite. This means capacitor voltage and inductor current are state variables: they carry memory of the past and cannot be reset by a switching event. The moment before and the moment after a switch closes or opens, these quantities must be equal.

The energy stored in each element is E = ½CV² for a capacitor and E = ½LI² for an inductor. Notice the symmetry: voltage plays the role for the capacitor that current plays for the inductor. This duality extends to how they combine in circuits. Two capacitors in series add reciprocally (just as resistors in parallel do), while capacitors in parallel add directly — the reverse of the resistor rule. Inductors follow the standard resistor pattern: series inductances add, parallel inductances add reciprocally.

When a switch opens or closes in a circuit, the initial conditions on capacitor voltage and inductor current at that instant determine the starting state of the transient solution. Before writing any differential equation, you should identify what V_C and I_L were just before the switching event. These values persist into t = 0⁺ and pin down the arbitrary constants in the homogeneous solution. Missing or incorrectly applying initial conditions is the most common source of error in transient circuit analysis.

Understanding these elements as energy-storage devices also builds physical intuition. A capacitor resists voltage change because changing voltage means moving charge, which takes current over time. An inductor resists current change because changing current means changing magnetic flux, which requires voltage over time. Together, these resistances to change give rise to oscillatory behavior when capacitors and inductors appear in the same circuit — the energy shuttles back and forth between electric and magnetic fields.
