---
id: circuit-theorems-linearity
title: Linearity, Superposition, and Scaling
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: node-voltage-systematic-solution
  type: soft
- id: mesh-current-systematic-solution
  type: soft
- id: ohms-law-and-conductance
  type: hard
builds-toward:
- thevenin-circuit-equivalent
- norton-circuit-equivalent
tags:
- linearity
- superposition
- homogeneity
- additivity
stage: formal-systems
status: validated
---

# Linearity, Superposition, and Scaling

## Core Idea
Linear circuits satisfy superposition: response to multiple sources equals the sum of individual responses. Linearity requires homogeneity (scaling input scales output) and additivity (sum of inputs produces sum of outputs). These properties hold for circuits with R, L, C, and independent sources, enabling efficient analysis and design techniques.

## Questions

```yaml
- question: "Using superposition, you find that source I₁ alone produces 4 V across resistor R, and source I₂ alone produces 3 V across R in the same direction. Both sources are now active. What is the power dissipated in R?"
  type: multiple-choice
  options:
    - "25/R watts — add the individual power contributions (16/R + 9/R)"
    - "49/R watts — first combine voltages (4 + 3 = 7 V), then compute power: 7²/R"
    - "12.5/R watts — average the two power contributions"
    - "7/R watts — superpose voltages and divide directly by R"
  answer: 1
  explanation: "Superposition applies to voltages and currents, not power. The total voltage is 7 V (correctly found by superposition). Power must then be computed from that combined voltage: P = 7²/R = 49/R. The tempting wrong answer (25/R) incorrectly superimposes the individual power contributions (16/R + 9/R), but P = V²/R is nonlinear — (4+3)² = 49, not 4² + 3² = 25. Superposing powers only works when the two contributions are orthogonal, which is not the case in a resistive circuit."

- question: "To find the voltage contribution from source V₂ alone using superposition, how should the other voltage source V₁ be treated?"
  type: multiple-choice
  options:
    - "Remove it from the circuit (open circuit) so it does not interfere"
    - "Replace it with a short circuit (a wire) — an ideal voltage source set to zero volts becomes a short"
    - "Set its value to a very small number approaching zero"
    - "Replace it with an open circuit (a gap) — the same treatment as a current source"
  answer: 1
  explanation: "An ideal voltage source enforces a fixed voltage between two terminals. Setting it to zero means it enforces 0 V — which is the same as connecting the two terminals with a wire (short circuit). By contrast, turning off a current source means it forces zero current — which is equivalent to removing the connection (open circuit). These are opposite treatments and are a common source of error: voltage sources → short circuits, current sources → open circuits."

- question: "The superposition principle can be used to calculate power contributions from each source separately and then add them to find total power in a linear circuit."
  type: true-false
  answer: false
  explanation: "Superposition applies only to linear responses — voltages and currents. Power is nonlinear (P = V²/R = I²R), so power contributions from different sources do not simply add. The correct procedure is to use superposition to find the actual combined voltage or current, and then compute power from those combined quantities. Directly adding individual power contributions gives a wrong result whenever two sources produce nonzero individual contributions."

- question: "In a linear circuit, doubling the magnitude of every independent source exactly doubles every node voltage and branch current in the circuit."
  type: true-false
  answer: true
  explanation: "This is the homogeneity (scaling) property of linear systems. Because all element relationships (V = IR for resistors, etc.) are linear and the governing equations (KVL, KCL) are linear, the response scales proportionally with the inputs. This is a direct consequence of linearity and is why Thévenin/Norton equivalents work: the terminal behavior of any linear subcircuit is a linear function of its sources."

- question: "Explain why superposition cannot be used to directly calculate total power dissipation in a circuit with multiple sources, even though it can be used to find total voltages and currents."
  type: short-answer
  answer: "Superposition requires linearity — the output must be a linear function of the inputs. Voltages and currents satisfy this because circuit equations (KVL, KCL, Ohm's law) are linear. Power is P = V²/R or I²R, which involves a square — a nonlinear operation. Because (V₁ + V₂)² ≠ V₁² + V₂² in general, the sum of individual power contributions is not equal to the power from the combined circuit. You must first find the combined voltage or current using superposition, then compute power from that combined value."
  explanation: "This is the most common error when students first apply superposition. The linearity of the theorem is not a formality — it has a hard boundary at any nonlinear quantity like power, stored energy (½CV², ½LI²), or any product of two circuit variables."
```

## Explainer

From Ohm's law, you already know a fundamental fact: the voltage across a resistor is proportional to the current through it, V = IR. That proportionality is the seed of everything in this topic. A circuit made of resistors, capacitors, and inductors is a **linear** system — meaning the relationship between any input (source) and any output (current or voltage anywhere) is proportional and can be broken apart. This linearity is what makes circuit analysis tractable.

Linearity has two components. **Homogeneity** (also called scaling) means that if you double every source in a circuit, every voltage and current response doubles as well. **Additivity** means that if circuit A has sources S1 and circuit B has sources S2, then the combined circuit with both S1 and S2 produces the sum of the two responses. Together, these define the **superposition principle**: the response due to multiple independent sources equals the algebraic sum of the responses due to each source acting alone.

To apply superposition, you "turn off" all sources except one — replacing voltage sources with short circuits (wires) and current sources with open circuits (gaps) — and calculate the response due to that single source. You repeat for every source, then add all partial responses. This can seem like more work than solving the full circuit directly, but the power comes when individual sub-circuits are simpler to analyze than the combined system, or when you want to understand each source's separate contribution. Node-voltage and mesh-current methods solve everything simultaneously; superposition solves things piecewise.

A critical limitation: superposition applies only to **linear** responses — currents and voltages. **Power** is not linear (P = I²R involves a square), so you cannot superpose power contributions from different sources. You must find the actual currents and voltages first, then compute power from those. This is the most common error when students first apply the theorem. The linearity property is also what makes Thévenin and Norton equivalents possible — they are direct consequences of the fact that any linear subcircuit, viewed from two terminals, behaves like a single source and a single resistor.
