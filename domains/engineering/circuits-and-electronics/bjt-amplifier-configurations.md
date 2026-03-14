---
id: bjt-amplifier-configurations
title: BJT Amplifier Configurations
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: bjt-transistor-fundamentals
  type: hard
- id: thevenin-norton-equivalents
  type: hard
- id: ac-circuit-analysis-methods
  type: soft
builds-toward:
- operational-amplifier-fundamentals
tags:
- common-emitter
- common-base
- common-collector
- emitter-follower
- small-signal
- hybrid-pi-model
- voltage-gain
- input-impedance
stage: formal-systems
status: validated
---

# BJT Amplifier Configurations

## Core Idea
BJTs are configured in three amplifier topologies defined by which terminal is common between input and output. The common-emitter amplifier provides high voltage and current gain with 180° phase inversion and is the most widely used. The common-collector (emitter-follower) has near-unity voltage gain but provides current gain and low output impedance, useful for driving loads. The common-base amplifier offers high voltage gain at high frequencies with no phase inversion. Small-signal analysis replaces the BJT with the hybrid-π model (voltage-controlled current source g_m·v_be, input resistance r_π = β/g_m, output resistance r_o) to compute gain and impedances for small sinusoidal signals around the Q-point.

## How It's Best Learned
Master the hybrid-π small-signal model. For each configuration, systematically set all DC sources to zero, short large bypass capacitors, replace the BJT with the small-signal model, and then apply KCL/KVL to find voltage gain, input impedance, and output impedance.

## Common Misconceptions
- Mixing large-signal DC quantities with small-signal AC quantities in the same equation.
- Forgetting to short bypass capacitors during small-signal analysis — an un-bypassed emitter resistor dramatically reduces voltage gain.
- Dismissing the emitter follower as useless because its voltage gain is less than 1 — its low output impedance is essential for impedance matching and current delivery.
