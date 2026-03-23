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

## Questions

```yaml
- question: "You design an inverting amplifier with Rin = 1 kΩ and Rf = 100 kΩ to achieve a gain of −100. The signal source has an output impedance of 500 kΩ. What is the primary problem with this design?"
  type: multiple-choice
  options:
    - "The gain magnitude exceeds 50, so the virtual ground assumption no longer holds"
    - "The input impedance of the amplifier is only 1 kΩ — this heavily loads the high-impedance source, causing a large voltage drop across the source impedance and attenuating the signal before it reaches the amplifier"
    - "Negative feedback becomes unstable when the gain magnitude exceeds 10"
    - "Virtual ground cannot be maintained at gains above 10 using a single op-amp stage"
  answer: 1
  explanation: "The inverting amplifier's input impedance equals Rin — not infinity. A source with 500 kΩ output impedance driving a 1 kΩ load loses nearly all its signal to the source resistance: the signal reaching the amplifier input is only 1/(1+500) ≈ 0.2% of the original. High-gain inverting designs require small Rin (to keep Rf manageable), which creates a tension: high gain demands small Rin, but small Rin loads high-impedance sources. This is the fundamental practical penalty of the inverting configuration."

- question: "In an ideal inverting amplifier, why does all of the input current (Iin = Vin / Rin) flow through Rf rather than into the op-amp input terminal?"
  type: multiple-choice
  options:
    - "The op-amp's input terminal provides a low-impedance path to ground, steering current through Rf"
    - "Current splits between Rf and the op-amp input in proportion to their impedances, but the op-amp input impedance is so high that the split is nearly 100% into Rf"
    - "By the virtual open rule, no current enters the op-amp input terminal — so Kirchhoff's current law at the inverting node forces all input current through Rf"
    - "The feedback loop redirects input current away from the op-amp terminal and into Rf to maintain gain accuracy"
  answer: 2
  explanation: "The virtual open rule states that no current enters the op-amp's input terminals (infinite input impedance in the ideal model). At the inverting node (at virtual ground, 0 V), KCL applies: current in through Rin must equal current out. With zero current entering the op-amp terminal, all of Iin = Vin/Rin must flow through Rf. This forces V_out = 0 − Iin × Rf = −(Rf/Rin) × Vin. The gain is not set by the op-amp — it falls directly from Ohm's Law applied to the two resistors."

- question: "In an ideal inverting amplifier, the closed-loop gain depends only on the ratio of the external resistors Rf and Rin, not on the op-amp's open-loop gain."
  type: true-false
  answer: true
  explanation: "True. This is the profound benefit of negative feedback. The op-amp's open-loop gain AOL appears in the exact expression for closed-loop gain, but as AOL → ∞ the expression reduces to Av = −Rf/Rin exactly. As long as AOL is large (which is the case for all practical op-amps in their bandwidth), the gain is determined entirely by the external resistor ratio — which can be set with precision resistors. The op-amp's job is simply to provide enough gain that the feedback loop enforces virtual ground; the exact value of AOL doesn't matter."

- question: "The inverting terminal of an inverting amplifier is at virtual ground, meaning it is physically connected to the 0 V supply rail through the feedback network."
  type: true-false
  answer: false
  explanation: "False. Virtual ground is a voltage condition, not a physical connection. The inverting terminal is connected only to the junction of Rin and Rf — there is no wire to ground at that node. Negative feedback continuously adjusts the output voltage to drive the differential input toward zero, holding the inverting terminal at approximately 0 V without any direct connection to ground. Current from the input flows through Rin, then through Rf to the output — not to ground. Confusing virtual ground with physical ground leads to the error of thinking input current drains to ground rather than flowing through Rf."

- question: "Explain why the gain of an inverting amplifier is determined by the resistor ratio Rf/Rin rather than by the op-amp's properties, and what this implies about practical design."
  type: short-answer
  answer: "Negative feedback drives the differential input of the op-amp toward zero (virtual short), which enforces virtual ground at the inverting terminal. With the inverting node held at 0 V, Ohm's Law completely determines the circuit behavior: input current = Vin/Rin, and since all of it flows through Rf (by the virtual open rule), V_out = −Vin × Rf/Rin. The op-amp's only role is to provide sufficient open-loop gain that the feedback loop can enforce virtual ground — its exact gain value doesn't appear in the result. This means gain accuracy depends on resistor precision, not op-amp specifications, so designers use precision resistors (0.01–0.1% tolerance) to set gain and tolerate wide variation in op-amp open-loop gain."
  explanation: "This insight reveals a key advantage of negative feedback circuits generally: they trade op-amp performance uncertainty for passive component precision. High-quality resistors are stable, cheap, and well-characterized; op-amp open-loop gain varies widely with temperature, supply voltage, and unit-to-unit manufacturing differences. By making gain depend on the ratio of two passive components rather than on the active device, the inverting amplifier topology produces reliable, reproducible results across manufacturing and environmental variations."
```

## Explainer

From your work on op-amp fundamentals, you know the two golden rules that make ideal op-amp analysis tractable: no current enters the input terminals (virtual open), and negative feedback drives the differential input voltage to zero (virtual short, or in this circuit, **virtual ground**). The inverting amplifier is the circuit where these rules produce a result that initially seems paradoxical: the inverting input is held at 0 V even though it is not physically connected to ground.

Here is how the feedback loop creates virtual ground. Suppose the input V_in is positive. Current flows through R_in toward the inverting terminal. If that terminal were truly floating, voltage would build up there and the output would swing negative. But the op-amp's output swings negative in response — and the feedback resistor R_f connects that negative output back to the inverting terminal, pulling its voltage back toward zero. The feedback loop continuously corrects any departure from 0 V at the inverting node. In the ideal case (infinite open-loop gain), the correction is perfect: the inverting input is held exactly at 0 V. This is virtual ground — not a physical connection, but an enforced potential.

Once you accept virtual ground, the gain derivation follows directly from Ohm's Law. The current through R_in is I = V_in / R_in (since the inverting node is at 0 V). Because no current enters the op-amp input terminal itself (virtual open), this entire current must flow through R_f. The voltage at the output is V_out = 0 − I × R_f = −(R_f / R_in) × V_in. The gain magnitude is R_f / R_in, and the negative sign reflects the phase inversion. Notice what sets the gain: not the op-amp itself, but the external resistor ratio. The op-amp's job is to provide enough open-loop gain that the feedback loop enforces virtual ground; the precision of the closed-loop gain depends on the resistors, not on the exact value of the op-amp's open-loop gain (as long as it is large).

The practical tradeoff to internalize is the input impedance penalty. In a non-inverting configuration, the signal feeds directly into the op-amp's input (near-infinite impedance). In the inverting configuration, the source sees R_in as its load, because the inverting terminal is held at virtual ground — any current into the node flows through R_in to the virtual ground, so the source must supply it. High-gain inverting designs require small R_in (to keep R_f manageable), which loads down high-impedance sources. This is why you'll encounter the non-inverting configuration for sensors and low-impedance-sensitive applications, while the inverting configuration is preferred when gain accuracy, signal summation (summing amplifier), or current-to-voltage conversion (transimpedance amplifier) are the priority.
