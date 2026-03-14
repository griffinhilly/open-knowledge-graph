---
id: mosfet-amplifier-circuits
title: MOSFET Amplifier Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: mosfet-transistor-fundamentals
  type: hard
- id: bjt-amplifier-configurations
  type: soft
builds-toward:
- differential-amplifier-circuits
tags:
- common-source
- common-drain
- common-gate
- source-follower
- small-signal-model
- transconductance
- mosfet-biasing
stage: formal-systems
status: draft
---

# MOSFET Amplifier Circuits

## Core Idea
MOSFETs are configured in three amplifier topologies analogous to BJT configurations. The common-source (CS) amplifier is the MOSFET counterpart of the common-emitter: it provides high voltage gain A_v = -g_m * R_D with phase inversion, where g_m = 2*I_D / (V_GS - V_th) is the transconductance. The common-drain (source follower) parallels the emitter follower with near-unity voltage gain, high input impedance (essentially infinite at DC due to the insulated gate), and low output impedance — ideal for buffering. The common-gate mirrors the common-base configuration with low input impedance and excellent high-frequency response. Small-signal analysis uses a simplified model with a voltage-controlled current source (g_m * v_gs) and output resistance r_o = V_A / I_D (or 1/lambda*I_D). A key difference from BJTs is that the MOSFET gate draws no DC bias current, simplifying bias network design but making g_m dependent on the square root of drain current rather than linearly proportional as in BJTs.

## How It's Best Learned
Draw direct parallels to the three BJT configurations, replacing r_pi with an open circuit (infinite gate impedance) and noting that g_m is set by overdrive voltage rather than collector current. For each topology, replace the MOSFET with the small-signal model and solve for gain and impedances. Design a CS amplifier with a specified gain and compare the required bias conditions to a CE amplifier achieving the same gain.

## Common Misconceptions
- Assuming MOSFET amplifiers always have higher input impedance than BJT amplifiers — while the gate itself draws no current, the bias resistor network at the gate determines the actual input impedance of the circuit.
- Using the BJT gain formula (A_v = -R_C / r_e) for MOSFETs — MOSFETs have no equivalent of r_e; gain depends on g_m, which varies with the square root of bias current, not linearly.
- Neglecting the channel-length modulation parameter (lambda or V_A) — it determines the output resistance r_o, which limits maximum achievable gain, especially in current-source-loaded designs.
