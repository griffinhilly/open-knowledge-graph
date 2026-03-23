---
id: circuit-laws-kvl-and-kcl
title: Kirchhoff's Voltage and Current Laws
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: voltage-divider-and-attenuation
  type: hard
- id: current-divider-and-distribution
  type: hard
builds-toward:
- node-voltage-systematic-solution
- mesh-current-systematic-solution
tags:
- kirchhoff-laws
- kvl
- kcl
- energy-conservation
- charge-conservation
stage: formal-systems
status: validated
---

# Kirchhoff's Voltage and Current Laws

## Core Idea
Kirchhoff's Voltage Law (KVL) states the sum of voltages around any loop equals zero, a consequence of energy conservation. Kirchhoff's Current Law (KCL) states the sum of currents at any node equals zero, a consequence of charge conservation. These fundamental laws apply to all circuits and form the basis for systematic analysis methods.

## Questions

```yaml
- question: "A node in a circuit has three branches: currents I₁ and I₂ flow in, and I₃ flows out. What does KCL tell you about these currents?"
  type: multiple-choice
  options:
    - "I₁ + I₂ = I₃"
    - "I₁ - I₂ + I₃ = 0"
    - "I₁ × I₂ = I₃"
    - "I₁ + I₂ + I₃ = 0, regardless of direction"
  answer: 0
  explanation: "KCL states that the sum of currents entering a node equals the sum of currents leaving it. With I₁ and I₂ entering and I₃ leaving, conservation of charge requires I₁ + I₂ = I₃. Option D would be correct if all currents were defined with the same sign convention (all into or all out of the node), in which case the algebraic sum is zero — but mixing actual directions gives I₁ + I₂ = I₃."

- question: "A loop contains a 12 V source and three resistors with voltage drops of 3 V, 5 V, and 4 V. You apply KVL around this loop. Which statement is correct?"
  type: multiple-choice
  options:
    - "12 − 3 − 5 − 4 = 0 confirms energy conservation — this is a valid KVL equation"
    - "The sum of drops exceeds the source voltage, so KVL is violated in this circuit"
    - "The drops must sum to more than 12 V to account for energy losses in the resistors"
    - "KVL only applies if all resistors are in series; it cannot be applied to a general loop"
  answer: 0
  explanation: "KVL states that the sum of all voltage rises and drops around any closed loop is zero. The 12 V source is a rise (+12), and the resistor drops are −3, −5, −4 V. Sum: 12 − 3 − 5 − 4 = 0. This is exactly energy conservation: a charge that travels around the loop returns to its starting potential, gaining and losing exactly equal amounts of energy."

- question: "KCL implies that current is partially 'used up' or consumed by a resistor, so the current leaving a resistor is always less than the current entering it."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about current and KCL. Resistors convert electrical energy into heat, but they do not consume charge. The same current that enters a resistor exits the other side — KCL guarantees it. What changes across a resistor is voltage (potential energy per charge), not current (charge flow rate). 'Voltage drops' across resistors; current is conserved."

- question: "KCL and KVL together provide exactly enough independent equations to solve for all unknown branch currents and voltages in any circuit."
  type: true-false
  answer: true
  explanation: "For a circuit with N nodes and B branches, KCL yields N−1 independent node equations and KVL yields B−N+1 independent loop equations. These two counts add to exactly B — one equation per unknown branch quantity. This completeness is guaranteed by the topology of the circuit graph, which is why the two laws together form a complete and solvable system for any circuit."

- question: "Why do physicists say KVL is a consequence of energy conservation and KCL is a consequence of charge conservation?"
  type: short-answer
  answer: "KCL follows from the fact that electric charge cannot accumulate at a node in steady state — every electron that flows in must flow out. If charge built up, an ever-growing electric field would quickly stop current flow. KVL follows from energy conservation: a charge carrier traveling around a closed loop and returning to its starting point must gain and lose exactly equal amounts of energy, so the net potential change around any loop is zero. If it were not, charges could spontaneously gain energy on each loop — violating conservation."
  explanation: "Connecting the circuit laws to their physical foundations helps you know when they apply and why: KCL holds as long as charge isn't accumulating (valid for DC and quasi-static AC), and KVL holds as long as changing magnetic flux through loops is negligible (valid for lumped-circuit models). Knowing the foundations lets you recognize the edge cases."
```

## Explainer

You already know how voltage dividers and current dividers work in simple series and parallel arrangements. KVL and KCL are the generalizations of those intuitions to circuits of arbitrary complexity — they give you a systematic procedure for writing down equations that are always true, regardless of circuit topology.

**Kirchhoff's Current Law** follows from the conservation of electric charge. At any junction (node) in a circuit, charge cannot accumulate — every electron that flows in must flow out. Formally: the sum of all currents entering a node equals the sum of all currents leaving it. Equivalently, if you define all currents as pointing *into* the node (or all *out*), they sum to zero. You used this implicitly in current divider analysis: two resistors in parallel share a node, and the total current splits between them. KCL simply states that principle for any node with any number of branches.

**Kirchhoff's Voltage Law** follows from the conservation of energy. In a closed loop, a charge carrier that travels all the way around returns to its starting potential — it cannot gain or lose net energy on a round trip. Therefore, the sum of all voltage rises and drops around any closed loop must be zero. Positive contributions come from voltage sources (batteries, active elements); negative contributions come from resistors, capacitors, and inductors where energy is dissipated or stored. You used this implicitly in voltage divider analysis: the source voltage equals the sum of the drops across the two resistors. KVL generalizes that to any loop with any number of elements.

Together, KCL and KVL let you write a complete, solvable set of equations for any circuit. For a circuit with N nodes and B branches, KCL gives N−1 independent node equations, and KVL gives B−N+1 independent loop equations. These two sets together account for all B unknowns (branch currents or branch voltages). The systematic methods you will see next — **node-voltage analysis** (applying KCL at each node to find voltages) and **mesh-current analysis** (applying KVL around each mesh to find currents) — are just structured procedures for writing and solving exactly these equations efficiently. The laws themselves are simple; the skill is applying them systematically without missing equations or introducing redundancy.
