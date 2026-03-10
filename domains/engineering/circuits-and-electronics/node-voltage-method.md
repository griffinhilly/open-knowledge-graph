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
status: draft
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
