---
id: ohms-law-and-conductance
title: Ohm's Law and Resistance
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: electric-potential-and-voltage
  type: hard
- id: charge-and-current-flow
  type: hard
builds-toward:
- resistive-networks-combinations
- circuit-laws-kvl-and-kcl
tags:
- ohms-law
- resistance
- conductance
- linearity
stage: formal-systems
status: validated
---

# Ohm's Law and Resistance

## Core Idea
Ohm's law states V = IR for a resistor, establishing linear proportionality between voltage and current. Resistance quantifies opposition to current flow and is material and geometry dependent. Power dissipated is P = I²R = V²/R. Conductance G = 1/R simplifies parallel circuit analysis.

## Questions

```yaml
- question: "A 10Ω resistor has 5V across it. The voltage is then doubled to 10V. What happens to the current through the resistor?"
  type: multiple-choice
  options:
    - "It stays the same — current depends only on the power supply's internal resistance"
    - "It doubles, from 0.5A to 1.0A"
    - "It quadruples, since power increases as the square of voltage"
    - "It halves — higher voltage increases effective resistance"
  answer: 1
  explanation: "By Ohm's Law, I = V/R. With R constant at 10Ω: at 5V, I = 0.5A; at 10V, I = 1.0A. The linear proportionality between V and I is the defining property of an ohmic resistor — double the voltage, double the current. Option D is the classic misconception: for an ohmic material, resistance is a fixed material property and does not change with applied voltage. Non-ohmic behavior (where effective resistance changes with voltage) would be a different kind of device entirely."

- question: "Two resistors — 100Ω and 10Ω — each have 10V applied across them. Which dissipates more power, and by what factor?"
  type: multiple-choice
  options:
    - "The 100Ω resistor, because greater resistance means more power dissipated"
    - "The 10Ω resistor, by a factor of 10"
    - "They dissipate equal power, since the voltage across each is identical"
    - "The 10Ω resistor, by a factor of 100"
  answer: 1
  explanation: "Use P = V²/R when voltage is known. P₁₀₀ = (10)²/100 = 1W; P₁₀ = (10)²/10 = 10W. The 10Ω resistor dissipates 10× more power. This is counterintuitive: lower resistance means more power at constant voltage, because less resistance allows larger current to flow. Option A confuses P = I²R (where more resistance means more power at constant current) with P = V²/R (where more resistance means less power at constant voltage). The formula to use depends on whether current or voltage is held fixed by the circuit."

- question: "A longer wire of the same material and cross-sectional area has lower resistance than a shorter wire of the same material."
  type: true-false
  answer: false
  explanation: "Resistance is proportional to length: R = ρL/A. A longer wire has higher resistance — more resistive material for charge carriers to traverse. Resistance is inversely proportional to cross-sectional area — a thicker wire has lower resistance than a thinner one of the same length and material. This is why undersized wiring for high-current loads causes voltage drop and overheating: the wire's resistance is too high for the current being pushed through it."

- question: "Conductance G = 1/R is useful in parallel circuit analysis because conductances in parallel add directly, just as resistances add directly in series."
  type: true-false
  answer: true
  explanation: "This duality is exact. In series circuits, the same current flows through all elements, so resistances add: R_total = R₁ + R₂ + …. In parallel circuits, the same voltage appears across all branches, so conductances add: G_total = G₁ + G₂ + …. Both follow from V = IR — it's a matter of which quantity is shared. Choosing to work in resistance or conductance is a computational convenience depending on which topology dominates the circuit being analyzed."

- question: "Explain why you should use P = I²R in some situations and P = V²/R in others. What determines which form is appropriate?"
  type: short-answer
  answer: "Both forms are derived from P = VI combined with V = IR. The choice depends on which quantity is fixed by the circuit configuration. In a series circuit, the same current flows through all elements, so I is known — use P = I²R. In a parallel circuit, the same voltage appears across all branches, so V is known — use P = V²/R. Using the wrong formula implicitly assumes a different circuit topology and gives an incorrect result."
  explanation: "A concrete example: a 100Ω and 10Ω resistor in series carrying 1A — use P = I²R: the 100Ω dissipates 100W, the 10Ω dissipates 10W. The same resistors in parallel with 10V applied — use P = V²/R: the 100Ω dissipates 1W, the 10Ω dissipates 10W. Same resistors, completely different power distribution, because the circuit topology changes which quantity is fixed."
```

## Explainer

From your study of electric potential and current, you know that **voltage** (V) is the energy per unit charge—the electrical "pressure" that pushes charges through a circuit—and that **current** (I) is the rate of charge flow. **Ohm's Law**, V = IR, connects them through a third quantity: **resistance** (R), which measures how strongly a material opposes the flow of current. A large resistance means a large voltage is required to drive even a modest current; a small resistance allows large currents at low voltages.

The proportionality in V = IR is the key insight: for an ohmic material, doubling the voltage exactly doubles the current. This linearity makes resistors the most mathematically tractable circuit element. Resistance depends on the material's **resistivity** (ρ) and its geometry: R = ρL/A, where L is the length of the conductor and A is its cross-sectional area. A long, thin wire has much higher resistance than a short, thick one of the same material. Metals have low resistivity (good conductors); rubber and glass have high resistivity (good insulators). This geometry dependence is why wiring gauge matters in practical circuits—undersized wire for a given current is a fire hazard.

**Power dissipation** follows directly from combining V = IR with the definition of power P = VI. Substituting V = IR gives P = I²R; substituting I = V/R gives P = V²/R. Both forms are useful—use P = I²R when you know the current (typical in series circuits), and P = V²/R when you know the voltage (typical in parallel circuits). This power becomes heat in the resistor, which is the physical basis for toaster wires, electric heaters, and incandescent light bulbs. Every real component has a maximum power rating; exceeding it causes failure, so power calculations are as important as voltage and current calculations in any real design.

**Conductance** G = 1/R, measured in Siemens (S), is simply resistance inverted: it measures how *easily* current flows. When resistors are connected in parallel, their conductances add directly (G_total = G_1 + G_2 + ...), just as resistances add directly in series. This symmetry is not coincidence—it reflects the duality of series and parallel analysis. Choosing to work in resistance or conductance is a matter of which topology dominates: series-heavy circuits favor resistance arithmetic, parallel-heavy circuits favor conductance arithmetic. Both are just different lenses on the same physical relationship V = IR.
