---
id: phasor-algebra-complex-impedance
title: Phasor Algebra and Complex Impedance
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ac-source-representation-phasors
  type: hard
- id: complex-numbers-intro
  type: soft
- id: complex-exponential-form
  type: hard
builds-toward:
- impedance-admittance-networks
- ac-power-analysis-circuits
- series-resonance-characteristics
- parallel-resonance-characteristics
tags:
- phasors
- impedance
- ac-analysis
stage: formal-systems
status: draft
---

# Phasor Algebra and Complex Impedance

## Core Idea
Impedance Z = R + jX generalizes resistance to AC circuits, where X is reactance. Resistive impedance is purely real (Z = R), capacitive is Z = -j/(ωC), and inductive is Z = jωL. Using complex arithmetic, Kirchhoff's laws apply directly to phasors, and series/parallel impedance rules follow resistor rules: series impedances sum, parallel impedances combine reciprocally.
