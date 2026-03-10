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
status: draft
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
