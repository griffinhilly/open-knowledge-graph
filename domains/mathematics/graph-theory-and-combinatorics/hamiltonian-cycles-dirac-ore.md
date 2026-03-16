---
id: hamiltonian-cycles-dirac-ore
title: 'Hamiltonian Cycles: Dirac and Ore Conditions'
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: hamiltonian-circuits
  type: hard
tags:
- graph-theory
- hamiltonicity
stage: formal-systems
status: draft
---

# Hamiltonian Cycles: Dirac and Ore Conditions

## Core Idea
Dirac's Theorem states that a graph with n ≥ 3 vertices where every vertex has degree at least n/2 is Hamiltonian. Ore's Theorem generalizes: if for every non-adjacent pair u,v we have deg(u) + deg(v) ≥ n, the graph is Hamiltonian. These conditions elegantly show that high minimum degree guarantees Hamiltonian cycles, though deciding Hamiltonicity in general remains NP-hard.

## How It's Best Learned
Verify these conditions on small graphs (n ≤ 6) and check that they hold for known Hamiltonian graphs.

## Common Misconceptions
These conditions are sufficient but not necessary; graphs can be Hamiltonian without satisfying Dirac or Ore conditions.
