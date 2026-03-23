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
status: validated
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

## Questions

```yaml
- question: "A designer uses a BJT common-emitter amplifier at a quiescent collector current of 1 mA, giving g_m = 40 mA/V. She wants to achieve the same g_m using a MOSFET common-source amplifier. Which statement best describes the required bias current?"
  type: multiple-choice
  options:
    - "The same 1 mA — g_m scales with bias current the same way in both devices"
    - "The MOSFET will require less than 1 mA because its gate draws no current, reducing power"
    - "The MOSFET will require more than 1 mA because its g_m scales with the square root of drain current, not linearly, making it less efficient at achieving high g_m from low bias currents"
    - "The MOSFET cannot achieve the same g_m because its insulated gate limits transconductance"
  answer: 2
  explanation: "BJT transconductance is g_m = I_C / V_T, scaling linearly with collector current. MOSFET transconductance is g_m = √(2k_n'(W/L)I_D), scaling with the square root of drain current. To match a BJT's g_m, a MOSFET must typically run at a higher drain current. This square-root dependence means MOSFETs are less efficient at generating high transconductance from a small bias current — a fundamental design tradeoff when choosing between the two device types."

- question: "In a circuit design, a high-impedance sensor output must drive a low-impedance load without significant voltage loss. Which MOSFET configuration is best suited, and why?"
  type: multiple-choice
  options:
    - "Common-source, because it provides the highest voltage gain"
    - "Common-gate, because it has the best high-frequency isolation"
    - "Common-drain (source follower), because it has near-unity voltage gain, high input impedance set by the bias network, and low output impedance (~1/g_m)"
    - "Common-source with a large R_D, because larger drain resistance increases input impedance"
  answer: 2
  explanation: "The source follower (common-drain) is a buffer: it presents a high impedance to the source (set by gate bias resistors, typically MΩ) and a low output impedance (~1/g_m, typically tens to hundreds of Ω). Its gain is approximately unity, so the signal is faithfully reproduced at the output without voltage loss despite the impedance mismatch. Common-source has high gain but also moderate output impedance and phase inversion — not suitable for buffering."

- question: "A MOSFET's gate draws no DC current, which means the input impedance of a MOSFET amplifier circuit is essentially infinite."
  type: true-false
  answer: false
  explanation: "The gate itself draws no DC current — the gate oxide is an insulator — but the actual circuit input impedance is set by the bias resistor network connected to the gate. Practical MOSFET amplifiers use resistor voltage dividers (e.g., two resistors from supply to ground) to set the DC gate voltage, and the parallel combination of these resistors determines the circuit's input impedance, typically hundreds of kΩ to a few MΩ. Confusing device physics (infinite gate impedance) with circuit impedance (finite, set by bias network) is a common design error."

- question: "Doubling the quiescent drain current in a MOSFET common-source amplifier doubles the transconductance g_m."
  type: true-false
  answer: false
  explanation: "MOSFET transconductance is g_m = √(2k_n'(W/L)I_D), so it scales with the square root of drain current. Doubling I_D increases g_m by a factor of √2 ≈ 1.41, not 2. This contrasts with BJTs, where g_m = I_C/V_T scales linearly with collector current. Designers who apply BJT intuition to MOSFET gain calculations will systematically overestimate the gain achieved by increasing bias current."

- question: "Why does MOSFET transconductance scale with the square root of drain current rather than linearly, and what does this mean for amplifier design compared to BJTs?"
  type: short-answer
  answer: "MOSFET drain current in saturation follows I_D = (k_n'/2)(W/L)(V_GS − V_th)², giving g_m = dI_D/dV_GS = k_n'(W/L)(V_GS − V_th) = √(2k_n'(W/L)I_D). This square-law relationship means g_m ∝ √I_D. In contrast, the BJT's exponential I_C–V_BE relationship gives g_m = I_C/V_T, scaling linearly. The consequence is that achieving high g_m in a MOSFET requires disproportionately large drain current — the MOSFET is less 'efficient' at converting bias current into transconductance, which matters for low-power design."
  explanation: "This difference in device physics shapes design strategy: BJTs are preferred when high transconductance from small bias current is critical (e.g., low-noise, low-power analog). MOSFETs dominate digital circuits (superior switching) and high-input-impedance applications. Understanding why the scaling differs — exponential vs. square-law transfer characteristic — is the foundation of transistor-level analog design intuition."
```

## Explainer

If you've studied BJT amplifier configurations, MOSFET amplifiers will feel immediately familiar in structure — the three configurations map directly onto each other, with the MOSFET's gate, drain, and source corresponding to the BJT's base, collector, and emitter. The critical physical difference is the insulated gate: because the gate oxide prevents DC current from flowing into the gate terminal, the MOSFET's input impedance at DC is essentially infinite. This changes how you think about biasing but not about small-signal gain.

Start with the **common-source (CS) amplifier**, the MOSFET counterpart of the common-emitter. A small AC signal v_gs is applied at the gate, the source is grounded, and the output is taken at the drain. In the small-signal model, the MOSFET is replaced by a voltage-controlled current source: the drain current is g_m × v_gs, where **transconductance** g_m = 2I_D / (V_GS − V_th) = √(2k_n'(W/L)I_D). The voltage gain is A_v = −g_m × R_D (with the negative sign indicating phase inversion, just like the CE amplifier). The gain magnitude increases with g_m, which you control by setting the DC bias point — higher quiescent drain current I_D means higher g_m, but at the cost of higher power dissipation. Unlike the BJT, where g_m = I_C / V_T scales linearly with collector current, the MOSFET's g_m scales with the square root of drain current, making it less efficient at high gain from small bias currents.

The **common-drain (source follower)** takes the output at the source with the drain connected to supply. The voltage gain is slightly less than unity (approximately g_m×R_S / (1 + g_m×R_S)), but the input impedance is set by the gate bias resistors (typically very high) and the output impedance is approximately 1/g_m (very low). This makes the source follower ideal as a **buffer stage**: it accepts a signal from a high-impedance source and delivers it to a low-impedance load without significant voltage loss, just as the emitter follower does for BJT circuits. The **common-gate** configuration has low input impedance (~1/g_m), high output impedance, and unity current gain with non-inverting voltage gain — it is primarily useful for high-frequency applications where its excellent isolation between input and output reduces the Miller effect.

The complete small-signal model also includes r_o = V_A / I_D (or 1/λI_D), the MOSFET's output resistance due to **channel-length modulation** — the slight increase in drain current as drain voltage increases, analogous to the Early effect in BJTs. In CS and CG amplifiers with resistive loads, r_o appears in parallel with R_D and slightly reduces gain. In current-source-loaded amplifiers (common in integrated circuits), r_o becomes the dominant limit on achievable voltage gain: A_v = −g_m × (r_o_device || r_o_load). Maximizing gain in IC design therefore requires maximizing g_m while maximizing r_o, which pulls in opposite directions with bias current. This fundamental tension shapes IC amplifier design methodology.
