---
id: diode-fundamentals
title: Diode Characteristics and Models
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: band-theory-intro
  type: soft
- id: electrical-properties-of-materials
  type: soft
- id: electrochemistry-basics
  type: soft
- id: electric-current-and-resistance
  type: soft
- id: atomic-structure-and-atoms
  type: soft
builds-toward:
- diode-circuit-applications
- bjt-transistor-fundamentals
- mosfet-transistor-fundamentals
tags:
- diode
- PN-junction
- I-V-characteristic
- forward-bias
- reverse-bias
- Shockley-equation
- Zener
stage: advanced
status: validated
---

# Diode Characteristics and Models

## Core Idea
A diode is a two-terminal semiconductor device based on a PN junction that conducts strongly in one direction (forward bias) and blocks in the other (reverse bias). Three models of increasing accuracy are commonly used: the ideal diode model (short circuit forward, open circuit reverse), the constant-voltage-drop model (0.7 V forward drop for silicon), and the Shockley equation I = I_s(e^(V/nV_T) − 1) capturing the exponential I-V relationship. Reverse breakdown (Zener effect) at a specified voltage is exploited for voltage regulation. The choice of model depends on the required accuracy and the circuit's signal levels.

## How It's Best Learned
Plot and interpret the I-V characteristic curve for a real silicon diode, noting the forward voltage threshold, the reverse leakage current, and the breakdown region. Analyze several circuits with each model and compare results to understand when simplifications are valid.

## Common Misconceptions
- Assuming a diode always drops exactly 0.7 V — this is an approximation for silicon at moderate currents; it varies with current and temperature.
- Forgetting to verify assumed on/off states after solving — an inconsistent assumption must be corrected by trying another assumption.
- Confusing Zener breakdown (engineered, controlled, reversible) with avalanche breakdown damage from exceeding the maximum rated current.

## Explainer

You've learned that circuit elements are characterized by their voltage-current relationship. A resistor's I-V relationship is linear: double the voltage, double the current. A diode is fundamentally different — its I-V relationship is exponential and asymmetric, and understanding that asymmetry is the key to understanding everything a diode does.

A diode is built from a **PN junction**: a piece of semiconductor where one side has been doped with electron donors (N-type, extra electrons) and the other with electron acceptors (P-type, extra "holes"). At the junction, electrons and holes recombine, creating a **depletion region** with an internal electric field that opposes further charge migration. This built-in field is the source of the diode's directional behavior. When you apply **forward bias** — connecting positive voltage to the P-side — you push against the depletion region's field and narrow it, allowing current to flow freely once the applied voltage exceeds roughly 0.6–0.7 V (for silicon). When you apply **reverse bias** — positive voltage to the N-side — you widen the depletion region and reinforce the blocking field. Current is reduced to a tiny leakage current (I_s, typically nanoamps) that comes from thermally generated carriers crossing the junction.

The **Shockley equation** I = I_s(e^(V/nV_T) − 1) captures this behavior precisely. At room temperature, V_T ≈ 26 mV, so the exponential term grows enormously once V reaches 0.6–0.7 V in forward bias. In reverse bias (V negative), the exponential term becomes negligible and I ≈ −I_s — a tiny current independent of voltage magnitude. Practical circuit analysis rarely uses the full Shockley equation for hand calculations because the arithmetic is unwieldy. Instead, you choose a **model** matched to your accuracy needs. The **ideal model** treats the forward-biased diode as a short circuit (zero resistance, zero voltage drop) and reverse-biased as an open circuit — useful for topology analysis and rough calculations. The **constant-voltage-drop model** (0.7 V for silicon) adds a fixed forward voltage, capturing the knee of the I-V curve without the exponential math. Use the Shockley equation only when the exact operating point matters, such as in logarithmic amplifier design.

The analysis procedure for diode circuits is: **assume** a state for each diode (on or off), **solve** the resulting linear circuit, then **verify** that the assumed states are consistent with the solution. If a diode assumed on has reverse current, or a diode assumed off has forward voltage exceeding 0.7 V, the assumption is wrong and must be corrected. **Zener diodes** exploit the reverse-breakdown region: by engineering the doping concentration, manufacturers can specify an exact breakdown voltage (e.g., 5.1 V) at which reverse current flows freely. Unlike uncontrolled avalanche breakdown, Zener breakdown is stable and reversible as long as power dissipation is managed. The result is a simple, robust voltage reference: whatever current flows through the circuit, the voltage across the Zener holds at V_Z — the foundation of basic voltage regulation.


