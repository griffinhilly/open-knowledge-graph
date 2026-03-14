---
id: amplifier-biasing-stability
title: Amplifier Biasing and Stability
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: common-emitter-amplifier
  type: hard
- id: bjt-transistor-fundamentals
  type: hard
builds-toward:
- multi-stage-amplifiers
tags:
- q-point
- voltage-divider-bias
- collector-feedback
- thermal-runaway
- beta-sensitivity
- stability-factor
- bias-design
stage: formal-systems
status: draft
---

# Amplifier Biasing and Stability

## Core Idea
A transistor amplifier requires a stable DC operating point (Q-point) to ensure linear operation across temperature changes, transistor replacement, and beta variation. Fixed-base bias (single resistor from V_CC to base) is the simplest but most unstable scheme — the Q-point shifts dramatically with beta, which varies 2:1 or more across production lots. Voltage-divider bias with an emitter resistor is the standard solution: the stiff voltage divider sets V_B independent of beta, and the emitter resistor R_E provides negative DC feedback — if I_C rises, the voltage drop across R_E increases, reducing V_BE and pulling I_C back down. The stability factor S = dI_C/dI_CO measures sensitivity to leakage current, with S = 1 being ideal. Collector-feedback bias uses a resistor from collector to base, also providing negative feedback against Q-point drift. Thermal runaway is a destructive positive-feedback loop where increased I_C raises junction temperature, which further increases I_C; proper biasing with adequate R_E prevents this by ensuring the thermal feedback loop gain stays below unity.

## How It's Best Learned
Design a voltage-divider bias circuit by choosing the bias resistors to make the divider current at least 10 times the base current (stiff divider condition). Calculate Q-point shift when beta changes by a factor of 2 to quantify the improvement over fixed-base bias. Simulate the same circuit at 25C and 75C to observe thermal drift and verify that R_E provides adequate stabilization.

## Common Misconceptions
- Assuming the Q-point is fixed once the circuit is built — temperature changes, component aging, and transistor replacement all shift the operating point unless the bias circuit is designed for stability.
- Choosing bias resistors without checking the stiff divider condition — if the divider current is comparable to the base current, the Q-point becomes beta-dependent, defeating the purpose of voltage-divider bias.
- Thinking thermal runaway only occurs at high power — it can occur in any BJT circuit without proper bias stabilization, though it is most dangerous in power amplifier stages where significant heat is generated.
