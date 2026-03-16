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
status: draft
---

# Kirchhoff's Voltage and Current Laws

## Core Idea
Kirchhoff's Voltage Law (KVL) states the sum of voltages around any loop equals zero, a consequence of energy conservation. Kirchhoff's Current Law (KCL) states the sum of currents at any node equals zero, a consequence of charge conservation. These fundamental laws apply to all circuits and form the basis for systematic analysis methods.

## Explainer

You already know how voltage dividers and current dividers work in simple series and parallel arrangements. KVL and KCL are the generalizations of those intuitions to circuits of arbitrary complexity — they give you a systematic procedure for writing down equations that are always true, regardless of circuit topology.

**Kirchhoff's Current Law** follows from the conservation of electric charge. At any junction (node) in a circuit, charge cannot accumulate — every electron that flows in must flow out. Formally: the sum of all currents entering a node equals the sum of all currents leaving it. Equivalently, if you define all currents as pointing *into* the node (or all *out*), they sum to zero. You used this implicitly in current divider analysis: two resistors in parallel share a node, and the total current splits between them. KCL simply states that principle for any node with any number of branches.

**Kirchhoff's Voltage Law** follows from the conservation of energy. In a closed loop, a charge carrier that travels all the way around returns to its starting potential — it cannot gain or lose net energy on a round trip. Therefore, the sum of all voltage rises and drops around any closed loop must be zero. Positive contributions come from voltage sources (batteries, active elements); negative contributions come from resistors, capacitors, and inductors where energy is dissipated or stored. You used this implicitly in voltage divider analysis: the source voltage equals the sum of the drops across the two resistors. KVL generalizes that to any loop with any number of elements.

Together, KCL and KVL let you write a complete, solvable set of equations for any circuit. For a circuit with N nodes and B branches, KCL gives N−1 independent node equations, and KVL gives B−N+1 independent loop equations. These two sets together account for all B unknowns (branch currents or branch voltages). The systematic methods you will see next — **node-voltage analysis** (applying KCL at each node to find voltages) and **mesh-current analysis** (applying KVL around each mesh to find currents) — are just structured procedures for writing and solving exactly these equations efficiently. The laws themselves are simple; the skill is applying them systematically without missing equations or introducing redundancy.
