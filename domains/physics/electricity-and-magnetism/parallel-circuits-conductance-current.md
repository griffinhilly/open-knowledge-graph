---
id: parallel-circuits-conductance-current
title: 'Parallel Circuits: Conductance and Current Division'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: circuit-topology-and-elements
  type: hard
- id: kirchhoffs-rules
  type: hard
builds-toward:
- combination-series-parallel-networks
tags:
- circuit analysis
- parallel circuits
- conductance
stage: formal-systems
status: draft
---

# Parallel Circuits: Conductance and Current Division

## Core Idea
In parallel circuits, the same voltage is across all elements. Total conductance G_total = G₁ + G₂ + ... where G = 1/R. Equivalently, 1/R_total = 1/R₁ + 1/R₂ + .... Current divides inversely with resistance: I_i = V/R_i. Parallel circuits are useful for voltage control and current distribution among branches.

## Questions

```yaml
- question: "Two resistors R₁ = 2Ω and R₂ = 8Ω are connected in parallel across a voltage source. What fraction of the total current flows through R₁?"
  type: multiple-choice
  options:
    - "1/5, because R₁ is one of two resistors and takes the smaller share"
    - "2/10 = 1/5, computed as R₁/(R₁ + R₂)"
    - "4/5, computed as R₂/(R₁ + R₂) — the smaller resistor gets the larger share"
    - "1/2, because both resistors receive the same voltage and current splits equally"
  answer: 2
  explanation: "The current divider formula gives I₁/I_total = G₁/(G₁ + G₂) = R₂/(R₁ + R₂) = 8/(2+8) = 4/5. This counter-intuitive form (current through R₁ involves R₂ in the numerator) trips beginners because it seems backward — but the logic is that current preferentially takes the path of least resistance. R₁ = 2Ω is the lower-resistance path, so it carries the larger share (4/5) of the current. Option B is the common error: writing R₁/(R₁+R₂) = 2/10 = 1/5, which gives the wrong branch."

- question: "Why does connecting more resistors in parallel always decrease the total resistance of the network?"
  type: multiple-choice
  options:
    - "Because each additional branch carries some current away from the others, reducing overall current flow"
    - "Because total resistance is the average of the branch resistances, and averaging more values pulls the result down"
    - "Because each additional branch provides another pathway for current, increasing total conductance and thus decreasing total resistance"
    - "Because parallel resistors must share the same current, forcing each to work less hard"
  answer: 2
  explanation: "In parallel, conductances add: G_total = G₁ + G₂ + .... Each additional branch adds a positive conductance, so G_total strictly increases, meaning R_total = 1/G_total strictly decreases. Conceptually, each new branch opens another route for current to flow, making the combined network easier to drive with the same voltage. This is why total parallel resistance is always less than the smallest individual resistance — adding even a high-resistance branch still adds some conductance. Option A has it backwards: parallel branches each carry more total current from the source, not less."

- question: "In a parallel circuit, the voltage across every branch is the same, regardless of the resistance of each branch."
  type: true-false
  answer: true
  explanation: "This follows directly from Kirchhoff's loop rule. All branches in a parallel group share the same two nodes. By the loop rule, the potential difference between those two nodes must be the same regardless of which path you trace between them. This equal-voltage property is the defining characteristic of parallel circuits — it is what allows household wiring to work: every appliance receives full mains voltage regardless of how many other devices are plugged in."

- question: "In the current divider formula for two parallel resistors, the current through R₁ is given by I₁ = I_total × R₁/(R₁ + R₂)."
  type: true-false
  answer: false
  explanation: "The correct formula is I₁ = I_total × R₂/(R₁ + R₂) — note that R₂ appears in the numerator, not R₁. This seems counterintuitive but follows directly from the physics: lower resistance means higher conductance means more current. The branch with smaller resistance carries the larger fraction of total current. The formula I₁ = I_total × R₁/(R₁+R₂) would give a larger share to the higher-resistance branch, which is the opposite of Ohm's law. Always check: the branch with smaller R should get the larger current fraction."

- question: "Why is conductance G = 1/R the natural unit for analyzing parallel circuits, and what property of parallel circuits does it make immediately transparent?"
  type: short-answer
  answer: "Conductance is natural for parallel circuits because conductances add directly: G_total = G₁ + G₂ + .... This mirrors how resistances add in series, revealing a symmetry between the two configurations. Using G makes the additive rule for parallel circuits as simple as the additive rule for series circuits. It also makes current distribution transparent: each branch carries current proportional to its conductance, so the highest-conductance (lowest-resistance) branch clearly carries the most current — which is exactly what we expect from 'current takes the path of least resistance.'"
  explanation: "The series-parallel duality is the deeper insight: resistance is the additive quantity in series; conductance is the additive quantity in parallel. Switching between R and G notation just depends on which configuration you're analyzing. For parallel networks, conductance arithmetic is always simpler — total conductance is a sum, and each branch current I_i = V × G_i follows transparently from G_i's contribution to G_total."
```

## Explainer

From Kirchhoff's rules you know that the voltage drop across any element in a circuit can be computed by applying the loop rule. In a parallel configuration, all branches share the same two endpoints — the same pair of nodes — so by the loop rule, every branch must have exactly the same voltage across it. There is no ambiguity: connect a voltmeter across any branch in a parallel group and you get the same reading. This is the defining feature of parallel circuits, and everything else follows from it.

Since each branch i has the same voltage V and its own resistance R_i, Ohm's law gives I_i = V/R_i independently for each branch. By the junction rule, the total current from the source equals the sum of all branch currents: I_total = V/R₁ + V/R₂ + ... = V(1/R₁ + 1/R₂ + ...). Defining **conductance** G = 1/R (measured in siemens, S) makes this cleaner: I_total = V·G_total, where G_total = G₁ + G₂ + .... Conductances add directly in parallel, exactly as resistances add in series. This symmetry is worth noticing: series and parallel are duals — resistance is additive in series, conductance is additive in parallel.

The **current divider** formula follows immediately: each branch carries a fraction of the total current proportional to its conductance (not its resistance). The branchiest path — lowest resistance, highest conductance — carries the most current. For two resistors in parallel: I₁/I_total = G₁/(G₁ + G₂) = R₂/(R₁ + R₂). This counter-intuitive form (current through R₁ involves R₂ in the numerator) trips up beginners; the logic is that more current takes the path of least resistance, which is the one with the larger G.

The practical consequence is that adding more branches to a parallel network always decreases total resistance and increases total current drawn from the source. This is why household wiring is parallel: each appliance gets full mains voltage regardless of what else is plugged in, and their currents add at the breaker. A series circuit would force all devices to share a single current, dimming lights whenever a heater turns on. The conductance framework makes this additive behavior transparent and is the natural language for analyzing multi-branch current distribution.
