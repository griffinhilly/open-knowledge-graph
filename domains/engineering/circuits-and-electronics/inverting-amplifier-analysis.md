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
stage: advanced
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

## Explainer

From your work on op-amp fundamentals, you know the two golden rules that make ideal op-amp analysis tractable: no current enters the input terminals (virtual open), and negative feedback drives the differential input voltage to zero (virtual short, or in this circuit, **virtual ground**). The inverting amplifier is the circuit where these rules produce a result that initially seems paradoxical: the inverting input is held at 0 V even though it is not physically connected to ground.

Here is how the feedback loop creates virtual ground. Suppose the input V_in is positive. Current flows through R_in toward the inverting terminal. If that terminal were truly floating, voltage would build up there and the output would swing negative. But the op-amp's output swings negative in response — and the feedback resistor R_f connects that negative output back to the inverting terminal, pulling its voltage back toward zero. The feedback loop continuously corrects any departure from 0 V at the inverting node. In the ideal case (infinite open-loop gain), the correction is perfect: the inverting input is held exactly at 0 V. This is virtual ground — not a physical connection, but an enforced potential.

Once you accept virtual ground, the gain derivation follows directly from Ohm's Law. The current through R_in is I = V_in / R_in (since the inverting node is at 0 V). Because no current enters the op-amp input terminal itself (virtual open), this entire current must flow through R_f. The voltage at the output is V_out = 0 − I × R_f = −(R_f / R_in) × V_in. The gain magnitude is R_f / R_in, and the negative sign reflects the phase inversion. Notice what sets the gain: not the op-amp itself, but the external resistor ratio. The op-amp's job is to provide enough open-loop gain that the feedback loop enforces virtual ground; the precision of the closed-loop gain depends on the resistors, not on the exact value of the op-amp's open-loop gain (as long as it is large).

The practical tradeoff to internalize is the input impedance penalty. In a non-inverting configuration, the signal feeds directly into the op-amp's input (near-infinite impedance). In the inverting configuration, the source sees R_in as its load, because the inverting terminal is held at virtual ground — any current into the node flows through R_in to the virtual ground, so the source must supply it. High-gain inverting designs require small R_in (to keep R_f manageable), which loads down high-impedance sources. This is why you'll encounter the non-inverting configuration for sensors and low-impedance-sensitive applications, while the inverting configuration is preferred when gain accuracy, signal summation (summing amplifier), or current-to-voltage conversion (transimpedance amplifier) are the priority.
