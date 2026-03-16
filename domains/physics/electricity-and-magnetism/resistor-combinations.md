---
id: resistor-combinations
title: Resistor Combinations and Equivalent Resistance
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: joule-heating
  type: hard
builds-toward:
- dc-circuit-analysis
tags:
- series
- parallel
- equivalent
stage: formal-systems
status: draft
---

# Resistor Combinations and Equivalent Resistance

## Core Idea
Resistors in series carry the same current; voltages add: V_total = IR₁ + IR₂ + ... and R_eq = R₁ + R₂ + .... Resistors in parallel have the same voltage; currents add: I_total = V/R₁ + V/R₂ + ... and 1/R_eq = 1/R₁ + 1/R₂ + .... Complex networks are simplified by repeatedly combining series and parallel sections or using Kirchhoff's laws.

## Explainer

To understand resistor combinations, start with what you know from Joule heating: power dissipated in a resistor is P = I²R = V²/R. Whether resistors are in series or parallel, energy must be conserved — the total power dissipated must equal the power delivered by the source. The combination rules for equivalent resistance follow almost inevitably from this constraint together with the definitions of current and voltage.

In a **series circuit**, there is only one path for current. Every electron flowing through R₁ must also flow through R₂ — there is no alternative route. So the current I is identical everywhere in the loop. Each resistor produces a voltage drop, and these drops add: V_total = IR₁ + IR₂ = I(R₁ + R₂). A single equivalent resistor R_eq = R₁ + R₂ produces the same total voltage drop at the same current. Adding resistors in series always increases the equivalent resistance. Think of it as adding more toll booths on the only highway: traffic flows at the same rate, but total delay accumulates.

In a **parallel circuit**, both ends of each resistor connect to the same two nodes. Every resistor sees the same voltage V, regardless of the others. But the current from the source splits: some goes through R₁ and the rest through R₂. The total current is I_total = V/R₁ + V/R₂ = V(1/R₁ + 1/R₂), so 1/R_eq = 1/R₁ + 1/R₂. Adding resistors in parallel always decreases the equivalent resistance — you are opening additional paths for current to flow. This is why plugging more appliances in parallel at home doesn't dim the others: each device sees the full line voltage (until the total current exceeds the breaker rating).

Complex networks — ladder circuits, bridge circuits, combinations of combinations — are tackled by identifying sub-groups that are purely series or purely parallel, reducing them step by step until a single equivalent remains. When no subset is cleanly either (the Wheatstone bridge is the classic example), you must apply Kirchhoff's laws directly, treating the network as a system of linear equations for the unknown currents. The guiding question is always: do these elements share the same current (series) or the same voltage (parallel)?
