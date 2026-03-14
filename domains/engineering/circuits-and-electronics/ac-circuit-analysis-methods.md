---
id: ac-circuit-analysis-methods
title: AC Circuit Analysis Using Phasors
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-analysis
  type: hard
- id: node-voltage-method
  type: hard
- id: mesh-current-method
  type: soft
- id: thevenin-norton-equivalents
  type: soft
- id: operations-with-complex-numbers
  type: hard
- id: ac-circuits-fundamentals
  type: soft
builds-toward:
- ac-power-analysis-circuits
- frequency-response-and-bode-plots
- passive-filter-design
- operational-amplifier-fundamentals
tags:
- AC-analysis
- phasor-domain
- nodal-analysis
- mesh-analysis
- superposition-AC
stage: formal-systems
status: validated
---

# AC Circuit Analysis Using Phasors

## Core Idea
All DC analysis techniques — node voltage, mesh current, superposition, Thevenin/Norton — apply directly to AC circuits by replacing element resistances with complex impedances and sources with their phasor representations. The result is a system of complex algebraic equations whose solution gives phasor voltages and currents. The transfer function H(jω) = Y(jω)/X(jω) describes the ratio of output to input phasors and captures all frequency-domain behavior. When multiple source frequencies are present, superposition must be applied separately at each frequency.

## How It's Best Learned
Solve the same RLC circuit first in the time domain (differential equations) and then with phasors to appreciate the efficiency gain. Draw phasor diagrams to visualize phase relationships between voltages and currents. Practice finding Thevenin equivalents in the frequency domain with complex Z_th.

## Common Misconceptions
- Mixing time-domain quantities with phasor quantities in the same equation — all variables must be in the same domain.
- Analyzing circuits with two different source frequencies simultaneously using a single phasor analysis — each frequency requires a separate analysis.
- Forgetting to convert sources at different phases correctly before applying node or mesh equations.
