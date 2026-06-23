---
id: node-voltage-method
title: Node Voltage Method (Nodal Analysis)
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: kirchhoffs-rules
  type: hard
- id: dc-circuits-series-parallel
  type: soft
- id: gaussian-elimination
  type: soft
- id: systems-elimination
  type: soft
- id: kirchhoff-current-law
  type: hard
builds-toward:
- mesh-current-method
- superposition-theorem-circuits
- thevenin-norton-equivalents
- ac-circuit-analysis-methods
tags:
- nodal-analysis
- KCL
- systematic-analysis
- linear-systems
stage: formal-systems
status: validated
---

# Node Voltage Method (Nodal Analysis)

## Core Idea
The node voltage method assigns a voltage variable to each non-reference node and applies KCL to write a system of linear equations. The reference (ground) node is chosen to simplify the algebra, often the node with the most connections. When voltage sources are present, supernodes are formed by grouping the two nodes connected by a voltage source, requiring an additional constraint equation from the source. Solving the linear system yields all node voltages, from which branch currents and power can be computed.

## How It's Best Learned
Practice identifying nodes and choosing a reference before writing any equations. Use the conductance matrix formulation (G·v = i) to organize the system. Handle supernodes explicitly. Always verify results by checking KCL at every node including those inside supernodes.

## Common Misconceptions
- Forgetting the supernode constraint equation relating the two nodes connected by a voltage source.
- Writing a KCL equation at a node inside a supernode boundary rather than at the supernode itself.
- Sign errors when summing currents: establish one convention (currents leaving = 0) and apply it consistently.

## Questions

```yaml
- question: "A circuit has 5 nodes (including the reference/ground node). How many independent node voltage equations must you write to solve the circuit (assuming no voltage sources)?"
  type: multiple-choice
  options: ["5", "4", "3", "It depends on the number of branches"]
  answer: 1
  explanation: "The node voltage method requires one equation per non-reference node, which is always (total nodes - 1). With 5 nodes, you write 4 equations. The reference node is assigned v = 0, so it does not need an equation. The number of branches affects how many terms appear in each equation, not how many equations you need."

- question: "When a voltage source connects two non-reference nodes, you can write a standard KCL equation at each of those two nodes independently."
  type: true-false
  answer: false
  explanation: "A voltage source between two non-reference nodes creates a supernode. You cannot write individual KCL equations at each node because the current through the voltage source is unknown. Instead, you treat the two nodes as a combined supernode — writing one KCL for the boundary of the supernode as a whole — and add a separate constraint equation from the voltage source: v_a - v_b = V_s."

- question: "Why is the reference node assigned a voltage of zero, and how does the choice of reference node affect the final answer?"
  type: short-answer
  answer: "The reference node is assigned v = 0 by definition to give all other voltages a common baseline to be measured against. The choice of reference does not change the physical voltages across elements or branch currents; it only changes which node voltages are positive or negative. Choosing a node with many connections simplifies the algebra by reducing the number of terms per equation."
  explanation: "Node voltages are potential differences relative to a chosen datum. Any node can serve as ground — the circuit physics are unchanged. Choosing the node with the most connections is a practical convenience: every branch connected to ground contributes a simple v_k/R term rather than (v_k - v_j)/R, reducing algebraic complexity."
```

## Explainer

The node voltage method is a systematic procedure for analyzing any linear circuit by reducing it to a solvable system of linear equations. Rather than tracking each branch current individually, the method exploits the fact that voltages at the nodes completely determine all branch currents through Ohm's law. Once you know every node voltage, every current and every power value follows immediately.

The procedure starts by designating one node as the reference — commonly called ground — and assigning it a voltage of zero. Every other node gets a voltage variable (v₁, v₂, …). For each non-reference node, you apply KCL in the form "sum of currents leaving the node = 0." Using Ohm's law, each current through a resistor between nodes i and j is (vᵢ - vⱼ)/R, which keeps every term in terms of the node voltages. This produces exactly (n − 1) equations for (n − 1) unknowns, where n is the total number of nodes.

The complication arises when a voltage source connects two non-reference nodes. The current through a voltage source is not directly computable from the voltage source value alone, so you cannot write a standard KCL equation at either of those nodes. The solution is to form a **supernode**: treat the pair of connected nodes as a single entity with one combined KCL equation written around the outer boundary of that pair. You then add a constraint equation that directly expresses the voltage difference: v_a − v_b = V_s. The supernode technique always adds one constraint equation for each voltage source between non-reference nodes, keeping the system fully determined.

After solving the linear system — by substitution, elimination, or matrix methods — verify your answer by checking KCL at every node, including any nodes inside supernodes. A single sign error in setting up the equations will propagate through the entire solution, so careful sign conventions (consistently using "currents leaving = 0" or "currents entering = 0") are essential. Most errors in nodal analysis trace not to misunderstanding the method but to inconsistent sign choices mid-problem.
