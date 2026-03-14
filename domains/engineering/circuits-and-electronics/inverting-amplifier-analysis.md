---
id: inverting-amplifier-analysis
title: Inverting Amplifier Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: operational-amplifier-fundamentals
  type: hard
- id: op-amp-circuit-applications
  type: soft
builds-toward:
- summing-and-difference-amplifiers
- integrator-differentiator-circuits
tags:
- inverting-amplifier
- virtual-ground
- gain
- input-impedance
- feedback-resistor
- transimpedance
stage: formal-systems
status: draft
---

# Inverting Amplifier Analysis

## Core Idea
The inverting amplifier connects the input signal through a resistor R_in to the op-amp's inverting terminal, with a feedback resistor R_f from output to inverting input, while the non-inverting terminal is grounded. Negative feedback forces the inverting input to virtual ground (0 V), so the input current I_in = V_in / R_in flows entirely through R_f (since no current enters the op-amp input), producing V_out = -I_in * R_f = -(R_f / R_in) * V_in. The closed-loop gain is A_v = -R_f / R_in, with the negative sign indicating phase inversion. Input impedance equals R_in (not infinite, because the inverting terminal is at virtual ground, not floating), which is a key practical consideration — the source must drive current into R_in. This configuration is the basis for the summing amplifier (multiple input resistors to the inverting node) and the transimpedance amplifier (current input, voltage output). Practical limitations include finite open-loop gain (causing gain error), finite bandwidth (gain-bandwidth product limits usable frequency range), and output voltage swing limited by supply rails.

## How It's Best Learned
Derive the gain formula from first principles using the virtual ground and virtual open rules rather than memorizing it. Then re-derive it including finite open-loop gain A_OL to see how the ideal formula emerges as A_OL approaches infinity and to quantify the gain error for realistic op-amps. Compare input impedance to the non-inverting configuration to understand why the choice between topologies matters for high-impedance sources.

## Common Misconceptions
- Assuming the inverting amplifier has infinite input impedance like the non-inverting configuration — because the inverting input is at virtual ground, the source sees R_in as the load, which can be problematically low for high-gain designs (small R_in).
- Believing virtual ground means the inverting node is physically connected to ground — it is held at ground potential by the feedback loop, but current flows through R_f to the output, not to ground.
- Ignoring the gain-bandwidth product constraint — an inverting amplifier with gain of -100 using an op-amp with GBW of 1 MHz has a usable bandwidth of only 10 kHz.
