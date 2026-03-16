---
id: network-circuit-analysis-methods
title: DC Circuit Network Analysis Methods
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: kirchhoff-circuit-laws-rules
  type: hard
builds-toward:
- transient-response-rc-circuits
tags:
- analysis
- network
- method
stage: formal-systems
status: draft
---

# DC Circuit Network Analysis Methods

## Core Idea
Systematic methods for analyzing circuits include node voltage analysis (applying KCL at nodes) and loop current analysis (applying KVL around loops). Thévenin and Norton equivalents simplify complex networks to simple source-resistor models.

## How It's Best Learned
Solve the same circuit using multiple methods. Verify answers using different techniques (superposition, Thévenin, mesh analysis).

## Explainer

Kirchhoff's laws — your prerequisite — give you two local rules: current in equals current out at every node (KCL), and voltages around any closed loop sum to zero (KVL). For simple circuits with one or two loops these rules are easy to apply by inspection. But for a circuit with five nodes and eight branches, writing equations ad hoc leads to a mess of redundant or inconsistent equations. Systematic methods exist precisely to turn Kirchhoff's laws into a reliable algorithm that works on arbitrarily complex networks.

**Node voltage analysis** (also called nodal analysis) is built on KCL. Pick one node as the reference (ground, V = 0), then assign an unknown voltage Vₙ to every other node. Write KCL at each non-reference node: the sum of currents leaving the node equals zero. Each current is expressed as (Vₙ − Vₘ)/R using Ohm's law. The result is a system of linear equations in the node voltages. Solve the system and you know every voltage in the circuit; every current follows by Ohm's law. This method has exactly (N − 1) unknowns for N nodes, which is the minimum necessary — very efficient for circuits with many parallel branches.

**Mesh current analysis** (or loop analysis) is the dual approach, built on KVL. Identify independent loops (meshes) in the circuit and assign each a circulating mesh current Iₘ. Write KVL around each mesh, expressing branch voltages in terms of mesh currents. The result is again a system of linear equations. This method is efficient when the circuit has few meshes but many nodes. For a planar circuit with M independent meshes, you get exactly M equations.

**Thévenin and Norton equivalents** take a different perspective: instead of solving the whole circuit at once, you replace part of it with a simpler model. Thévenin's theorem says any network of resistors and sources, viewed from two terminals, is equivalent to a single voltage source Vₜₕ in series with a resistance Rₜₕ. Norton's theorem gives the dual: a current source Iₙ in parallel with Rₙ = Rₜₕ. These equivalents are powerful when you need to analyze how one part of a circuit (say, a load) interacts with a complex source — you reduce the source to its simplest possible form without losing any information about what the terminals deliver. Together, these systematic methods let you analyze any DC resistor network mechanically and correctly, with no guesswork about where to start.
