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

## Questions

```yaml
- question: "You add a third resistor in parallel to two existing parallel resistors in a circuit. What happens to the equivalent resistance of the parallel combination?"
  type: multiple-choice
  options:
    - "It increases, because you are adding more total resistance to the circuit"
    - "It stays the same, because parallel resistors are electrically independent"
    - "It decreases, because you have opened an additional path for current to flow"
    - "It depends on whether the new resistor is larger or smaller than the existing ones"
  answer: 2
  explanation: "Adding any resistor in parallel always decreases the equivalent resistance, regardless of its value. The formula 1/R_eq = 1/R₁ + 1/R₂ + 1/R₃ shows that each new term increases 1/R_eq, which means R_eq decreases. The physical reason: another parallel branch provides another current pathway. The total current the source must supply increases, which means the effective load seen by the source is smaller. Option A is the classic misconception from confusing series and parallel behavior."

- question: "Two resistors R₁ = 4Ω and R₂ = 4Ω are connected in series across a 12V battery. What is the current through R₂?"
  type: multiple-choice
  options:
    - "3A — applying Ohm's law directly to R₂: V/R₂ = 12V / 4Ω"
    - "1.5A — the total current through the series circuit: 12V / (4Ω + 4Ω)"
    - "6A — total voltage divided by the smallest resistor"
    - "0.75A — half the series current, since the resistors are identical"
  answer: 1
  explanation: "In a series circuit, there is only one path for current. The same current flows through every element — both resistors and the battery. The total equivalent resistance is 4 + 4 = 8Ω, so the current is 12V / 8Ω = 1.5A. Option A is the trap: using the full 12V with just R₂ would be correct if R₂ were the only element, but in series, 12V is shared across both resistors (6V each). Option D confuses series current (which is the same everywhere, not split) with parallel current."

- question: "In a parallel circuit, if one branch's resistor is replaced with a larger one, the voltage across all other branches remains unchanged."
  type: true-false
  answer: true
  explanation: "In a parallel circuit, all branches connect between the same two nodes — they all share the same terminal voltage. Changing one branch's resistor changes the current through that branch, but does not change the voltage that the source maintains across the parallel combination (assuming an ideal voltage source). This is why household appliances in parallel don't affect each other's voltage: each is independently connected to the same supply rails."

- question: "Adding resistors in series decreases the total equivalent resistance because each additional resistor provides another path for current."
  type: true-false
  answer: false
  explanation: "This describes parallel, not series. In series, there is only one path — adding more resistors in series lengthens that single path, increasing total resistance: R_eq = R₁ + R₂ + R₃ + ... Adding resistors in PARALLEL decreases resistance by providing additional current paths. Confusing these two is extremely common because both involve 'adding' resistors — the key distinction is whether you are adding more obstacles on the same path (series) or more alternative paths (parallel)."

- question: "What is the key question to ask when identifying whether resistors are in series or parallel, and why does the answer determine which formula to use?"
  type: short-answer
  answer: "The key question is: do these resistors carry the same current, or do they share the same voltage? If the same current flows through all of them (only one path), they are in series: R_eq = R₁ + R₂ + ... If they all connect between the same two nodes (same voltage), they are in parallel: 1/R_eq = 1/R₁ + 1/R₂ + ... These two topologies produce opposite effects on equivalent resistance — series always increases it, parallel always decreases it."
  explanation: "This question — shared current or shared voltage? — is the fundamental diagnostic for circuit simplification. It applies recursively to complex networks: identify a sub-group that clearly shares a current path (series) or shares two nodes (parallel), reduce it, and repeat. The physical insight behind each formula flows directly from the answer: series obeys voltage addition (drops add along one path); parallel obeys current addition (currents split at a node)."
```

## Explainer

To understand resistor combinations, start with what you know from Joule heating: power dissipated in a resistor is P = I²R = V²/R. Whether resistors are in series or parallel, energy must be conserved — the total power dissipated must equal the power delivered by the source. The combination rules for equivalent resistance follow almost inevitably from this constraint together with the definitions of current and voltage.

In a **series circuit**, there is only one path for current. Every electron flowing through R₁ must also flow through R₂ — there is no alternative route. So the current I is identical everywhere in the loop. Each resistor produces a voltage drop, and these drops add: V_total = IR₁ + IR₂ = I(R₁ + R₂). A single equivalent resistor R_eq = R₁ + R₂ produces the same total voltage drop at the same current. Adding resistors in series always increases the equivalent resistance. Think of it as adding more toll booths on the only highway: traffic flows at the same rate, but total delay accumulates.

In a **parallel circuit**, both ends of each resistor connect to the same two nodes. Every resistor sees the same voltage V, regardless of the others. But the current from the source splits: some goes through R₁ and the rest through R₂. The total current is I_total = V/R₁ + V/R₂ = V(1/R₁ + 1/R₂), so 1/R_eq = 1/R₁ + 1/R₂. Adding resistors in parallel always decreases the equivalent resistance — you are opening additional paths for current to flow. This is why plugging more appliances in parallel at home doesn't dim the others: each device sees the full line voltage (until the total current exceeds the breaker rating).

Complex networks — ladder circuits, bridge circuits, combinations of combinations — are tackled by identifying sub-groups that are purely series or purely parallel, reducing them step by step until a single equivalent remains. When no subset is cleanly either (the Wheatstone bridge is the classic example), you must apply Kirchhoff's laws directly, treating the network as a system of linear equations for the unknown currents. The guiding question is always: do these elements share the same current (series) or the same voltage (parallel)?
