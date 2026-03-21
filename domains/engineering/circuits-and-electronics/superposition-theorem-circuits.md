---
id: superposition-theorem-circuits
title: Superposition Theorem
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: node-voltage-method
  type: soft
- id: mesh-current-method
  type: soft
builds-toward:
- thevenin-norton-equivalents
tags:
- linearity
- superposition
- multiple-sources
- dependent-sources
stage: formal-systems
status: validated
---

# Superposition Theorem

## Core Idea
In any linear circuit, the voltage or current at any element due to multiple independent sources equals the algebraic sum of the responses produced by each source acting alone. To isolate one independent source, all other independent voltage sources are replaced with short circuits and all other independent current sources with open circuits. Dependent sources are never deactivated — they remain active during every sub-analysis. Superposition follows directly from the linearity of Kirchhoff's laws and is foundational to Thevenin/Norton analysis.

## How It's Best Learned
Apply superposition to circuits with two or three sources and verify by comparing with full nodal or mesh analysis. Track reference directions carefully when summing partial responses — the algebraic sign of each contribution matters.

## Common Misconceptions
- Deactivating dependent sources along with independent sources — dependent sources must remain active throughout.
- Applying superposition to power, which is quadratic and nonlinear — powers from individual source contributions do not add to give total power.
- Forgetting to restore the circuit to its full topology between sub-analyses.

## Questions

```yaml
- question: "A circuit contains two independent voltage sources and one dependent current source. When applying superposition, how many sub-circuits do you analyze, and how is the dependent source treated?"
  type: multiple-choice
  options:
    - "Three sub-circuits — one per source, including the dependent source, which is deactivated in the other two"
    - "Two sub-circuits — one per independent source; the dependent source is deactivated in each"
    - "Two sub-circuits — one per independent source; the dependent source remains active in both"
    - "One sub-circuit — superposition only applies when all sources are independent"
  answer: 2
  explanation: "Superposition deactivates independent sources one at a time — here, two sub-circuits. The dependent source is never deactivated because it models a real physical coupling (its output is controlled by a circuit variable). Deactivating it would eliminate the gain mechanism it represents, giving wrong answers. Option B is the most tempting wrong answer: it correctly counts two sub-circuits but incorrectly treats the dependent source like an independent one."

- question: "Applying superposition, you find that source A contributes 3 W to a resistor and source B contributes 4 W. What is the total power dissipated by the resistor?"
  type: multiple-choice
  options:
    - "7 W — power contributions add just like voltage and current contributions"
    - "1 W — the contributions partially cancel"
    - "Cannot be determined from this information; total power must be computed from the combined voltage or current after superposition"
    - "25 W — power adds in quadrature (3² + 4² = 25)"
  answer: 2
  explanation: "Power is P = V²/R — a nonlinear (quadratic) function of voltage. Superposition only applies to linear quantities (voltages and currents). The total power is (V_A + V_B)²/R = V_A²/R + 2V_A·V_B/R + V_B²/R, which includes a cross-term 2V_A·V_B/R that vanishes only when the contributions are orthogonal. To find total power, compute the combined voltage (or current) first, then calculate power from that combined quantity."

- question: "When applying superposition, dependent sources should be deactivated (set to zero) in each sub-circuit, just like independent sources."
  type: true-false
  answer: false
  explanation: "Only independent sources are deactivated. Dependent sources model physical couplings — transistor gain, op-amp behavior — whose output depends on a circuit variable. Deactivating them would remove the coupling entirely and produce incorrect results. The rule is: independent sources go off one at a time; dependent sources stay on always."

- question: "Superposition can be used to calculate the total voltage across any element in a linear circuit with multiple independent sources."
  type: true-false
  answer: true
  explanation: "Kirchhoff's voltage and current laws are linear equations in voltages and currents. Linearity means responses from independent sources add without interaction (for voltages and currents). So the total voltage across any element equals the algebraic sum of the contributions from each source acting alone — this is exactly what superposition states. The key constraint is linearity: superposition only applies to linear circuits."

- question: "Why does superposition apply to voltages and currents in a linear circuit, but not to power dissipation?"
  type: short-answer
  answer: "Superposition follows from linearity: KVL and KCL are linear equations, so solutions from multiple sources add independently. Power, however, is P = V²/R — a quadratic (nonlinear) function of voltage. Squaring a sum introduces cross-terms: (V₁ + V₂)²/R = V₁²/R + 2V₁V₂/R + V₂²/R. The cross-term 2V₁V₂/R is missed if you add the individual powers, making the sum incorrect. Total power must always be computed from the combined voltage or current after superposition, never by summing partial powers."
  explanation: "A practical consequence: in amplifier analysis, you can superpose the signal component and the DC bias to find total voltages and currents. But to find total power dissipated (e.g., for thermal design), you must use the combined waveform — which includes the signal-bias interaction term that superposing powers would miss."
```

## Explainer

From your study of node voltage and mesh current methods, you know how to solve circuits with multiple sources by assembling and solving a system of linear equations. Superposition offers an alternative route grounded in the same mathematics: because Kirchhoff's laws are linear in voltages and currents, responses from multiple sources add independently. Instead of solving everything at once, you decompose the problem into simpler sub-circuits — one source active at a time — and sum the results.

The procedure is mechanical. To find the contribution of independent source k, **deactivate** all other independent sources: replace every other independent voltage source with a short circuit (zero volts across it) and every other independent current source with an open circuit (zero current through it). Solve the simplified circuit for the desired voltage or current. Repeat for each source. The actual value is the algebraic sum of all contributions, with careful attention to reference directions — a contribution that opposes your reference direction subtracts rather than adds.

The most important rule is that **dependent sources are never deactivated**. A dependent source's value is controlled by a circuit variable (a voltage or current elsewhere in the circuit), so deactivating it would remove a real physical coupling in the device model. Transistors and op-amps are routinely modeled with dependent sources; removing them in a sub-analysis would eliminate the gain mechanism entirely. The practical rule is: independent sources go off one at a time, dependent sources stay on always.

Superposition has both analytical and conceptual value. Analytically, it trades one N-source problem for N single-source problems, each often solvable by inspection using voltage dividers or current dividers. Conceptually, it attributes each contribution to its source — in an amplifier circuit, you can separately calculate the signal component (from the input source) and the DC bias (from the supply), then combine them. The key limitation is power: because P = V²/R = I²·R is quadratic in voltage and current, power is nonlinear and does not obey superposition. Always compute total power from the combined voltages and currents after superposition is complete, never by summing the powers from individual sub-analyses.
