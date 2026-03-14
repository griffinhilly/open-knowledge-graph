---
id: hamiltonian-circuits
title: Hamiltonian Circuits and Paths
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: euler-circuits-and-paths
  type: soft
tags:
- hamiltonian-circuit
- hamiltonian-path
- NP-complete
- traveling-salesman
- dirac-theorem
stage: formal-systems
status: validated
---

# Hamiltonian Circuits and Paths

## Core Idea
A Hamiltonian path visits every vertex exactly once; a Hamiltonian circuit does so and returns to the start. Unlike Eulerian circuits, there is no simple necessary and sufficient characterization of Hamiltonian graphs — determining existence is NP-complete. Sufficient conditions include Dirac's theorem (minimum degree ≥ n/2 implies a Hamiltonian circuit) and Ore's theorem. The traveling salesman problem — find the minimum-cost Hamiltonian circuit in a weighted graph — is one of the most studied problems in combinatorial optimization.

## How It's Best Learned
Explore small examples and feel the absence of a clean characterization. Apply Dirac's and Ore's theorems to examples, noting they give only sufficient conditions. Contrast the theoretical intractability with Eulerian circuits to appreciate how similar-sounding problems can have radically different difficulty.

## Common Misconceptions
- Confusing Hamiltonian circuits (vertices visited once) with Eulerian circuits (edges traversed once).
- Believing that if a sufficient condition like Dirac's fails, no Hamiltonian circuit exists.
