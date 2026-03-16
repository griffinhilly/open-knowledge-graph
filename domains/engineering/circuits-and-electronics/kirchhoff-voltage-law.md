---
id: kirchhoff-voltage-law
title: Kirchhoff's Voltage Law (KVL)
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
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
status: draft
---

# Kirchhoff's Voltage Law (KVL)

## Core Idea
Kirchhoff's Voltage Law states that the algebraic sum of voltages around any closed loop in a circuit equals zero. This principle, derived from energy conservation, is one of two fundamental laws for circuit analysis. KVL applies to any circuit topology and forms the basis for systematic circuit analysis methods like mesh current analysis.

## Explainer

From your study of circuit variables and elements, you know that **voltage** is the energy per unit charge between two points — it measures how much work is done moving charge from one node to another. Kirchhoff's Voltage Law (KVL) is a direct consequence of energy conservation applied to electric circuits: if you move a unit of charge around any closed path and return to the starting point, the net energy gained must be zero. No energy was created or destroyed; it was only transferred among elements. In mathematical terms: the sum of all voltage rises equals the sum of all voltage drops around any closed loop.

The sign convention is where students stumble most. The standard approach is to define a **traversal direction** around the loop (clockwise is conventional but either works consistently). As you traverse each element: if you enter the element at its positive terminal (the side labeled + or the side current enters), that element is a **voltage drop** — you are moving from high potential to low, like walking downhill, and you subtract that voltage. If you enter at the negative terminal, that element is a **voltage rise** — you are walking uphill — and you add it. Equivalently, a voltage source you traverse from − to + is a rise; one you traverse from + to − is a drop. A resistor carrying current in the same direction as your traversal is a drop (by Ohm's law: V = IR, potential falls in the direction of current flow).

Consider a simple series circuit: a 9 V battery connected to two resistors, R₁ = 3 Ω and R₂ = 6 Ω, all in series. If current I flows clockwise, KVL going clockwise gives: +9 − I(3) − I(6) = 0, yielding 9 = 9I, so I = 1 A. The battery provides 9 V; the two resistors together consume 3 V + 6 V = 9 V. The loop closes with zero net voltage — exactly as KVL demands. Notice that you can also write KVL by going counterclockwise: −9 + I(6) + I(3) = 0 gives the same result. The direction of traversal is your choice; what matters is consistent sign application.

KVL becomes especially powerful when combined with Kirchhoff's Current Law (KCL) for multi-loop circuits. In a circuit with multiple loops, each loop generates an independent KVL equation. These equations, together with KCL at the nodes and Ohm's law for resistors, form a system of linear equations that completely determines all voltages and currents. This is the foundation of **mesh current analysis**: assign a circulating current to each independent loop, apply KVL to each loop, and solve the resulting system. Every systematic circuit analysis method — node voltage, mesh current, superposition — ultimately rests on KVL and KCL as its axioms.
