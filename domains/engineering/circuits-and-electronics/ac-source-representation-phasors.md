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
builds-toward:
- phasor-algebra-complex-impedance
- ac-circuit-analysis-methods
tags:
- ac-sources
- phasors
- ac-analysis
stage: formal-systems
status: draft
---

# AC Sources and Phasor Representation

## Core Idea
AC sources produce sinusoidal voltage and current: v(t) = V_m·sin(ωt + φ). Phasor representation converts sinusoidal signals to complex numbers in the frequency domain: V = V_m∠φ = V_m·e^(jφ). This transformation converts differential equations to algebraic equations, making AC circuit analysis practical. Phasors assume all signals operate at the same frequency, a reasonable assumption for circuits with one source frequency.
