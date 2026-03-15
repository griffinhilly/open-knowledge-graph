---
id: hamiltonian-cycles-discrete
title: Hamiltonian Paths and Cycles
domain: mathematics
course: discrete-math
prerequisites:
- id: hamiltonian-paths-cycles
  type: hard
- id: euler-circuits-applications
  type: soft
builds-toward:
- algorithm-complexity-discrete
tags:
- Hamiltonian-cycle
- Hamiltonian-path
- TSP
- NP-hard
stage: formal-systems
status: draft
---

# Hamiltonian Paths and Cycles

## Core Idea
A Hamiltonian path visits every vertex exactly once; a Hamiltonian cycle returns to its start. Unlike Euler circuits (which exist iff degrees are even), no simple characterization exists for Hamiltonicity. Finding them is NP-complete; the traveling salesman problem seeks the shortest Hamiltonian cycle.

## How It's Best Learned
Recognize sufficient conditions: if every vertex has degree ≥ n/2, a Hamiltonian cycle exists (Dirac's theorem). Practice finding them in small graphs by exhaustive or intelligent search. Distinguish from Euler (edges vs. vertices).

## Common Misconceptions
Hamiltonicity is hard—no polynomial-time algorithm is known. Dirac/Ore conditions are sufficient but not necessary. A graph can have many, one, or no Hamiltonian cycles.
