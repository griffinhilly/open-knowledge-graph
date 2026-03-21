---
id: series-parallel-resistor-analysis
title: Series and Parallel Resistor Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: kirchhoff-voltage-law
  type: hard
- id: kirchhoff-current-law
  type: hard
builds-toward:
- dc-analysis-steady-state
- series-parallel-capacitor-networks
- series-parallel-inductor-networks
- impedance-admittance-networks
tags:
- circuit-topology
- resistive-circuits
- network-analysis
stage: formal-systems
status: draft
---

# Series and Parallel Resistor Networks

## Core Idea
Resistors in series sum their resistances: R_eq = R₁ + R₂ + ... Resistors in parallel sum reciprocals: 1/R_eq = 1/R₁ + 1/R₂ + ... Real circuits often contain both series and parallel sections, which can be simplified by iteratively combining adjacent elements. This systematic reduction technique simplifies analysis while preserving circuit behavior.

## Questions

```yaml
- question: "Three identical 6Ω resistors are connected in parallel. An engineer calculates the equivalent resistance as 18Ω. What error did they make?"
  type: multiple-choice
  options:
    - "They forgot to account for the power supply's internal resistance"
    - "They applied the series formula (R_eq = R₁ + R₂ + R₃) instead of the parallel formula"
    - "They used the wrong rule — only two resistors can be combined at a time"
    - "They should have squared the resistance before summing"
  answer: 1
  explanation: "For three 6Ω resistors in parallel: 1/R_eq = 1/6 + 1/6 + 1/6 = 3/6 = 0.5, so R_eq = 2Ω. The engineer used R_eq = 3 × 6 = 18Ω, which is the series formula. Adding parallel branches always decreases the equivalent resistance — you're giving current more paths to flow through, making the circuit easier to drive, not harder."

- question: "Resistors R₁ = 4Ω and R₂ = 12Ω are connected in parallel. What is the equivalent resistance?"
  type: multiple-choice
  options:
    - "16Ω — sum of the two resistances"
    - "8Ω — average of the two resistances"
    - "3Ω — less than either individual resistor"
    - "6Ω — harmonic mean estimate"
  answer: 2
  explanation: "1/R_eq = 1/4 + 1/12 = 3/12 + 1/12 = 4/12, so R_eq = 3Ω. Equivalently, R_eq = R₁R₂/(R₁ + R₂) = 48/16 = 3Ω. The result is less than the smaller resistor (4Ω) — this is always the case for parallel combinations. The parallel path gives current an additional route, so the overall opposition to current decreases."

- question: "Adding any additional resistor in parallel to an existing circuit will always decrease the total equivalent resistance, regardless of the added resistor's value."
  type: true-false
  answer: true
  explanation: "When you add a resistor in parallel, you add a new term 1/R_new to the sum 1/R_eq. Since 1/R_new > 0 for any finite resistor, the total sum increases, and therefore R_eq decreases. Even a very large added resistor (say, 1 MΩ) provides a tiny extra current path and reduces R_eq slightly. This follows directly from KCL: total current always increases when a new branch is added at the same voltage."

- question: "In a parallel circuit, each branch carries the same current."
  type: true-false
  answer: false
  explanation: "In a parallel circuit, each branch sees the same terminal voltage (enforced by KVL — the voltage loop around any two parallel branches is zero). The current in each branch is determined independently by Ohm's law: I = V/R. A branch with lower resistance carries more current; a branch with higher resistance carries less. It is the series circuit where all elements carry the same current. Confusing these two facts is a persistent source of errors in circuit analysis."

- question: "Explain why the parallel resistor formula uses reciprocals (1/R_eq = 1/R₁ + 1/R₂) rather than directly summing resistances. Which circuit law drives this result?"
  type: short-answer
  answer: "KCL: in a parallel circuit, all branches share the same voltage, so the current through each branch is I_k = V/R_k by Ohm's law. The total current from the source is the sum of branch currents: I_total = V/R₁ + V/R₂ = V(1/R₁ + 1/R₂). Since the equivalent resistance satisfies I_total = V/R_eq, we get 1/R_eq = 1/R₁ + 1/R₂. Summing resistances would be wrong because it would imply currents multiply rather than add."
  explanation: "The key is that parallel elements share voltage, not current. KCL forces us to add currents; Ohm's law converts those currents into 1/R terms. The reciprocal structure is not an arbitrary formula — it emerges directly from the physics. By contrast, series resistors share current (enforced by KCL with no branching nodes), so KVL gives additive voltage drops and directly additive resistances."
```

## Explainer

You know from KVL that voltages sum to zero around any closed loop, and from KCL that currents sum to zero at any node. These two laws are the foundation for understanding why series and parallel resistors combine the way they do — the combination rules are not arbitrary formulas to memorize but direct consequences of the laws you already know.

For **series resistors**, all the same current flows through each element (KCL — there are no branching nodes). KVL around the loop says the source voltage equals the sum of voltage drops: V = I×R₁ + I×R₂ = I(R₁+R₂). By definition, the equivalent resistance is V/I, so R_eq = R₁ + R₂. The more resistors you stack in series, the harder it is for current to flow — resistance accumulates. You can think of series resistors as a single long pipe: each segment adds to the total friction against flow.

For **parallel resistors**, both elements share the same two terminal nodes, so they see the same voltage (KVL — the voltage around any loop containing just those two elements is zero). But KCL says the total current from the source splits between the branches: I_total = V/R₁ + V/R₂ = V(1/R₁ + 1/R₂). The equivalent resistance satisfies I_total = V/R_eq, so 1/R_eq = 1/R₁ + 1/R₂. Adding a parallel branch always reduces the equivalent resistance — you are giving current an additional path, making the overall circuit easier to drive. For two resistors, the result simplifies to R_eq = R₁R₂/(R₁+R₂), always less than the smaller of the two.

Real circuits combine both structures. The technique for analysis is **iterative reduction**: find the innermost series or parallel group, replace it with its equivalent, redraw the circuit, and repeat until you are left with a single equivalent resistance. The order of operations matters — you can only combine elements that are strictly in series (same current, no other branches between them) or strictly in parallel (same terminal voltage, connected to the same two nodes). A common error is combining resistors that look geometrically adjacent on a schematic but are not electrically series or parallel; always trace the current path and node connections carefully. Once you have the equivalent resistance and the total current or voltage from the source, you can work backward through the reductions — reintroducing original elements and applying Ohm's law at each stage — to find the current and voltage at every element in the original network. This backward-tracing technique, combined with the voltage divider and current divider rules, gives you a complete toolkit for analyzing any resistive circuit without writing large systems of equations.
