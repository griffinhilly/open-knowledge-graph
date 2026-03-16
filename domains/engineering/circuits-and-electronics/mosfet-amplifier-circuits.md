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

## Explainer

If you've studied BJT amplifier configurations, MOSFET amplifiers will feel immediately familiar in structure — the three configurations map directly onto each other, with the MOSFET's gate, drain, and source corresponding to the BJT's base, collector, and emitter. The critical physical difference is the insulated gate: because the gate oxide prevents DC current from flowing into the gate terminal, the MOSFET's input impedance at DC is essentially infinite. This changes how you think about biasing but not about small-signal gain.

Start with the **common-source (CS) amplifier**, the MOSFET counterpart of the common-emitter. A small AC signal v_gs is applied at the gate, the source is grounded, and the output is taken at the drain. In the small-signal model, the MOSFET is replaced by a voltage-controlled current source: the drain current is g_m × v_gs, where **transconductance** g_m = 2I_D / (V_GS − V_th) = √(2k_n'(W/L)I_D). The voltage gain is A_v = −g_m × R_D (with the negative sign indicating phase inversion, just like the CE amplifier). The gain magnitude increases with g_m, which you control by setting the DC bias point — higher quiescent drain current I_D means higher g_m, but at the cost of higher power dissipation. Unlike the BJT, where g_m = I_C / V_T scales linearly with collector current, the MOSFET's g_m scales with the square root of drain current, making it less efficient at high gain from small bias currents.

The **common-drain (source follower)** takes the output at the source with the drain connected to supply. The voltage gain is slightly less than unity (approximately g_m×R_S / (1 + g_m×R_S)), but the input impedance is set by the gate bias resistors (typically very high) and the output impedance is approximately 1/g_m (very low). This makes the source follower ideal as a **buffer stage**: it accepts a signal from a high-impedance source and delivers it to a low-impedance load without significant voltage loss, just as the emitter follower does for BJT circuits. The **common-gate** configuration has low input impedance (~1/g_m), high output impedance, and unity current gain with non-inverting voltage gain — it is primarily useful for high-frequency applications where its excellent isolation between input and output reduces the Miller effect.

The complete small-signal model also includes r_o = V_A / I_D (or 1/λI_D), the MOSFET's output resistance due to **channel-length modulation** — the slight increase in drain current as drain voltage increases, analogous to the Early effect in BJTs. In CS and CG amplifiers with resistive loads, r_o appears in parallel with R_D and slightly reduces gain. In current-source-loaded amplifiers (common in integrated circuits), r_o becomes the dominant limit on achievable voltage gain: A_v = −g_m × (r_o_device || r_o_load). Maximizing gain in IC design therefore requires maximizing g_m while maximizing r_o, which pulls in opposite directions with bias current. This fundamental tension shapes IC amplifier design methodology.
