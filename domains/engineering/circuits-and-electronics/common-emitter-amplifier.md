---
id: common-emitter-amplifier
title: Common-Emitter Amplifier
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: bjt-amplifier-configurations
  type: hard
- id: bjt-transistor-fundamentals
  type: hard
builds-toward:
- amplifier-biasing-stability
- multi-stage-amplifiers
- differential-amplifier-circuits
tags:
- common-emitter
- voltage-gain
- bypass-capacitor
- biasing
- small-signal
- hybrid-pi-model
- phase-inversion
stage: formal-systems
status: draft
---

# Common-Emitter Amplifier

## Core Idea
The common-emitter (CE) amplifier is the most widely used BJT amplifier topology, providing substantial voltage gain with 180-degree phase inversion between input and output. The transistor's emitter terminal is common to both the input and output circuits (grounded through a bypass capacitor at signal frequencies). Voltage gain is determined by the ratio of collector resistance to the small-signal emitter resistance: A_v = -g_m * R_C (or equivalently -R_C / r_e for the simplified T-model), where the negative sign reflects phase inversion. A voltage divider network at the base establishes a stable DC operating point (Q-point), while coupling capacitors isolate the amplifier's DC bias from signal source and load. An emitter resistor R_E provides DC stability against beta variation, but an emitter bypass capacitor must short R_E at signal frequencies to preserve full voltage gain.

## How It's Best Learned
Start by establishing the DC bias point using Thevenin equivalent analysis at the base, then replace the BJT with the hybrid-pi small-signal model. Systematically short all DC sources and large capacitors, apply KCL at the collector node, and derive gain and impedance expressions. Compare measured gain with and without the emitter bypass capacitor to see how the un-bypassed emitter resistor trades gain for linearity and bandwidth.

## Common Misconceptions
- Assuming the bypass capacitor is optional — without it, the emitter resistance R_E appears in the gain expression and reduces voltage gain dramatically (A_v = -R_C / (r_e + R_E)).
- Confusing the DC bias resistors with the small-signal input impedance — the bias network loads the input in parallel with the transistor's r_pi, so the amplifier's input impedance is lower than r_pi alone.
- Expecting the CE amplifier to have constant gain across all frequencies — coupling and bypass capacitors create low-frequency roll-off, while parasitic capacitances and the transistor's f_T limit high-frequency response.
