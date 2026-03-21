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

## Questions

```yaml
- question: "A silicon diode is connected in series with a 1 kΩ resistor and a 5 V supply, with the diode forward biased. Using the constant-voltage-drop model, what current flows through the circuit?"
  type: multiple-choice
  options:
    - "5 mA — apply Ohm's law using the full 5 V supply across the 1 kΩ resistor"
    - "4.3 mA — subtract the 0.7 V diode drop first, leaving 4.3 V across the resistor"
    - "0.7 mA — the diode drop of 0.7 V divided by 1 kΩ gives the current"
    - "0 mA — a forward-biased diode blocks current in this configuration"
  answer: 1
  explanation: "With 0.7 V dropped across the forward-biased diode, only 4.3 V remains across the resistor: I = 4.3 V / 1 kΩ = 4.3 mA. Option A is the most common error — applying the full supply voltage to the resistor while ignoring the diode drop. The 0.7 V forward voltage matters whenever it is comparable to signal levels; always subtract it from the available voltage before computing current through the rest of the circuit."

- question: "After assuming a diode is OFF (reverse biased) and solving the circuit, a student finds that the voltage across the diode is +1.5 V with positive polarity at the anode. What should the student do next?"
  type: multiple-choice
  options:
    - "Accept the result — a positive anode voltage confirms the diode is reverse biased"
    - "Reject the assumption and re-analyze assuming the diode is ON, because +1.5 V at the anode would actually forward bias the diode"
    - "Conclude the diode is in Zener breakdown, since 1.5 V exceeds the forward threshold"
    - "Average the ON and OFF solutions to find the actual operating point"
  answer: 1
  explanation: "The assume-solve-verify cycle is the core methodology for diode circuits. An assumed-OFF diode with +1.5 V at the anode is self-contradictory: a positive anode voltage forward biases the diode, meaning it would actually be ON. The inconsistency invalidates the assumption. The student must restart with the diode assumed ON and verify that the resulting solution (positive current through the diode) is consistent. Option A represents the failure mode of skipping verification."

- question: "A Zener diode operating in its reverse-breakdown region maintains an approximately constant voltage across its terminals over a wide range of currents."
  type: true-false
  answer: true
  explanation: "This is the defining property exploited for voltage regulation. In the Zener breakdown region, large changes in reverse current produce very small changes in the voltage across the diode — the V-I curve is nearly vertical. A Zener in this region acts as a practical voltage reference: whatever current the rest of the circuit demands, the terminal voltage holds at approximately V_Z. This assumes the current stays within the rated range so power dissipation remains acceptable."

- question: "The ideal diode model is more accurate than the constant-voltage-drop model for analyzing circuits with supply voltages around 0.5 V."
  type: true-false
  answer: false
  explanation: "At low supply voltages, the ideal model (zero forward drop) is actually less accurate. The constant-voltage-drop model predicts the diode barely conducts or does not conduct at all when the supply voltage (0.5 V) is less than the 0.7 V forward threshold — which is physically correct. The ideal model incorrectly predicts full conduction and gives a significantly wrong current. The ideal model's approximation is only valid when the supply voltage is large enough that 0.7 V is negligible in comparison (typically at least a few volts)."

- question: "Why must a student verify the assumed on/off state of a diode after solving a diode circuit, and what does it mean if the verification fails?"
  type: short-answer
  answer: "A diode's behavior depends on its operating state, but its state in turn depends on the circuit — creating a circular dependency. The analysis breaks this circle by assuming a state, solving the resulting linear circuit, then checking self-consistency: an assumed-OFF diode must have zero or reverse current and forward voltage below ~0.7 V; an assumed-ON diode must have positive (forward) current and ~0.7 V forward drop. If the solution contradicts the assumption, the assumption is wrong and the analysis must be restarted with the opposite state. Skipping verification is the primary source of errors in diode circuit analysis."
  explanation: "For circuits with multiple diodes, every possible combination of on/off states may need to be checked. The valid solution is the unique one where all assumptions are self-consistent simultaneously — there is always exactly one physically correct operating point."
```

## Explainer

You've learned that circuit elements are characterized by their voltage-current relationship. A resistor's I-V relationship is linear: double the voltage, double the current. A diode is fundamentally different — its I-V relationship is exponential and asymmetric, and understanding that asymmetry is the key to understanding everything a diode does.

A diode is built from a **PN junction**: a piece of semiconductor where one side has been doped with electron donors (N-type, extra electrons) and the other with electron acceptors (P-type, extra "holes"). At the junction, electrons and holes recombine, creating a **depletion region** with an internal electric field that opposes further charge migration. This built-in field is the source of the diode's directional behavior. When you apply **forward bias** — connecting positive voltage to the P-side — you push against the depletion region's field and narrow it, allowing current to flow freely once the applied voltage exceeds roughly 0.6–0.7 V (for silicon). When you apply **reverse bias** — positive voltage to the N-side — you widen the depletion region and reinforce the blocking field. Current is reduced to a tiny leakage current (I_s, typically nanoamps) that comes from thermally generated carriers crossing the junction.

The **Shockley equation** I = I_s(e^(V/nV_T) − 1) captures this behavior precisely. At room temperature, V_T ≈ 26 mV, so the exponential term grows enormously once V reaches 0.6–0.7 V in forward bias. In reverse bias (V negative), the exponential term becomes negligible and I ≈ −I_s — a tiny current independent of voltage magnitude. Practical circuit analysis rarely uses the full Shockley equation for hand calculations because the arithmetic is unwieldy. Instead, you choose a **model** matched to your accuracy needs. The **ideal model** treats the forward-biased diode as a short circuit (zero resistance, zero voltage drop) and reverse-biased as an open circuit — useful for topology analysis and rough calculations. The **constant-voltage-drop model** (0.7 V for silicon) adds a fixed forward voltage, capturing the knee of the I-V curve without the exponential math. Use the Shockley equation only when the exact operating point matters, such as in logarithmic amplifier design.

The analysis procedure for diode circuits is: **assume** a state for each diode (on or off), **solve** the resulting linear circuit, then **verify** that the assumed states are consistent with the solution. If a diode assumed on has reverse current, or a diode assumed off has forward voltage exceeding 0.7 V, the assumption is wrong and must be corrected. **Zener diodes** exploit the reverse-breakdown region: by engineering the doping concentration, manufacturers can specify an exact breakdown voltage (e.g., 5.1 V) at which reverse current flows freely. Unlike uncontrolled avalanche breakdown, Zener breakdown is stable and reversible as long as power dissipation is managed. The result is a simple, robust voltage reference: whatever current flows through the circuit, the voltage across the Zener holds at V_Z — the foundation of basic voltage regulation.


