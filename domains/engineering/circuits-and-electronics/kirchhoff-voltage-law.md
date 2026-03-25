---
id: kirchhoff-voltage-law
title: Kirchhoff's Voltage Law (KVL)
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: current-divider-circuit
  type: soft
builds-toward:
- voltage-divider-circuit
- series-parallel-resistor-analysis
- dc-analysis-steady-state
- mesh-current-method
tags:
- kirchhoff-laws
- circuit-analysis
- fundamental
stage: formal-systems
status: validated
---
# Kirchhoff's Voltage Law (KVL)

## Core Idea
Kirchhoff's Voltage Law states that the algebraic sum of voltages around any closed loop in a circuit equals zero. This principle, derived from energy conservation, is one of two fundamental laws for circuit analysis. KVL applies to any circuit topology and forms the basis for systematic circuit analysis methods like mesh current analysis.

## Questions

```yaml
- question: "A series loop contains a 12 V battery, R₁ = 4 Ω, and R₂ = 8 Ω. Applying KVL clockwise (entering the battery at its negative terminal), what equation do you write and what current results?"
  type: multiple-choice
  options:
    - "+12 − 4I − 8I = 0, yielding I = 1 A"
    - "−12 + 4I + 8I = 0, yielding I = 1 A (same result, different traversal)"
    - "+12 + 4I + 8I = 0, yielding I = −1 A"
    - "I = 12/4 = 3 A from R₁ alone"
  answer: 0
  explanation: "Traversing clockwise: entering the battery at − and exiting at + is a voltage rise (+12 V). Each resistor traversed in the direction of current is a drop (−4I, −8I). KVL: +12 − 4I − 8I = 0 → I = 1 A. Option B is also valid (counterclockwise traversal multiplies through by −1 but gives the same answer). Option C incorrectly makes the source a drop. Option D uses only one resistor, ignoring KVL as a loop equation."

- question: "A student applies KVL to a loop and solves for current I, getting I = −0.5 A. What does this mean?"
  type: multiple-choice
  options:
    - "The actual current flows opposite to the assumed direction — the analysis is still valid"
    - "An error was made; current cannot be negative in circuit analysis"
    - "The loop must be rewritten with the current flowing the other direction before proceeding"
    - "KVL was applied with the wrong sign convention and must be redone"
  answer: 0
  explanation: "A negative current in KVL analysis simply means the actual current flows opposite to the direction you assumed when writing the equation. The magnitude and all resulting voltages are correct — just reverse the arrow. This is a feature of linear circuit analysis, not an error. You never need to redo the loop; interpret I = −0.5 A as 0.5 A flowing the other way."

- question: "KVL is a consequence of energy conservation: moving a charge around a closed loop returns it to its original potential energy, so the net voltage change must be zero."
  type: true-false
  answer: true
  explanation: "Voltage at a point is the potential energy per unit charge relative to a reference. Moving a unit charge around any closed loop and returning to the start involves zero net energy change — otherwise energy would be created or destroyed by repeating the loop. The algebraic sum of voltage rises and drops equaling zero is precisely this energy-conservation statement."

- question: "The direction you choose to traverse a loop in KVL changes the numerical value of the current you solve for."
  type: true-false
  answer: false
  explanation: "The choice of traversal direction is arbitrary and affects only the signs of each term in the KVL equation. If you reverse traversal direction, every term flips sign, but the resulting equation is just multiplied by −1 — it yields the same current. The physical current is determined by the circuit, not by the analyst's traversal choice."

- question: "Explain what KVL is really saying physically, and why the algebraic sum of voltages around any closed loop must equal zero."
  type: short-answer
  answer: "KVL expresses conservation of energy for electric charge. Voltage measures potential energy per unit charge. If you move a unit charge around a closed loop through sources and resistors and return to the starting point, it must have the same energy as when it left — no energy was created or destroyed. Voltage rises (energy gained from sources) must exactly cancel voltage drops (energy lost to resistors and other loads), so their algebraic sum is zero."
  explanation: "The analogy: if you hike a loop trail and return to your starting elevation, your net change in altitude is zero, regardless of the hills and valleys along the way. KVL is the electrical version of this: potential is the altitude, and closing the loop guarantees zero net change."
```

## Explainer

From your study of circuit variables and elements, you know that **voltage** is the energy per unit charge between two points — it measures how much work is done moving charge from one node to another. Kirchhoff's Voltage Law (KVL) is a direct consequence of energy conservation applied to electric circuits: if you move a unit of charge around any closed path and return to the starting point, the net energy gained must be zero. No energy was created or destroyed; it was only transferred among elements. In mathematical terms: the sum of all voltage rises equals the sum of all voltage drops around any closed loop.

The sign convention is where students stumble most. The standard approach is to define a **traversal direction** around the loop (clockwise is conventional but either works consistently). As you traverse each element: if you enter the element at its positive terminal (the side labeled + or the side current enters), that element is a **voltage drop** — you are moving from high potential to low, like walking downhill, and you subtract that voltage. If you enter at the negative terminal, that element is a **voltage rise** — you are walking uphill — and you add it. Equivalently, a voltage source you traverse from − to + is a rise; one you traverse from + to − is a drop. A resistor carrying current in the same direction as your traversal is a drop (by Ohm's law: V = IR, potential falls in the direction of current flow).

Consider a simple series circuit: a 9 V battery connected to two resistors, R₁ = 3 Ω and R₂ = 6 Ω, all in series. If current I flows clockwise, KVL going clockwise gives: +9 − I(3) − I(6) = 0, yielding 9 = 9I, so I = 1 A. The battery provides 9 V; the two resistors together consume 3 V + 6 V = 9 V. The loop closes with zero net voltage — exactly as KVL demands. Notice that you can also write KVL by going counterclockwise: −9 + I(6) + I(3) = 0 gives the same result. The direction of traversal is your choice; what matters is consistent sign application.

KVL becomes especially powerful when combined with Kirchhoff's Current Law (KCL) for multi-loop circuits. In a circuit with multiple loops, each loop generates an independent KVL equation. These equations, together with KCL at the nodes and Ohm's law for resistors, form a system of linear equations that completely determines all voltages and currents. This is the foundation of **mesh current analysis**: assign a circulating current to each independent loop, apply KVL to each loop, and solve the resulting system. Every systematic circuit analysis method — node voltage, mesh current, superposition — ultimately rests on KVL and KCL as its axioms.
