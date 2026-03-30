---
id: quantum-walks
title: Quantum Walks
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-circuits
  type: hard
- id: qubits-and-quantum-states
  type: hard
- id: grovers-search-algorithm
  type: soft
tags:
- quantum-walk
- discrete-time
- continuous-time
- graph-algorithm
- speedup
stage: expert
status: validated
---
# Quantum Walks

## Core Idea
Quantum walks are the quantum analog of classical random walks, where a particle traverses a graph in superposition rather than probabilistically. In a discrete-time quantum walk, a coin operator creates superposition and a shift operator moves the walker conditioned on the coin state. In a continuous-time quantum walk, the Hamiltonian is the graph's adjacency matrix and evolution is via the Schrodinger equation. Quantum walks spread quadratically faster than classical random walks (standard deviation grows linearly with time vs. sqrt(t) classically) and serve as the basis for quantum algorithms for graph problems, element distinctness, and spatial search.

## Questions

```yaml
- question: "A classical random walk on a line has standard deviation proportional to sqrt(t) after t steps. What is the standard deviation of a quantum walk on a line after t steps?"
  type: multiple-choice
  options: ["sqrt(t)", "t", "t^2", "log(t)"]
  answer: 1
  explanation: "A quantum walk on a line spreads ballistically rather than diffusively: the standard deviation grows linearly with t, not as sqrt(t). This is because quantum interference between different paths creates a bias toward the edges of the distribution rather than concentrating probability near the origin. This quadratic speedup in spreading rate underlies many quantum walk algorithms."

- question: "Continuous-time quantum walks require a coin operator, just like discrete-time quantum walks."
  type: true-false
  answer: false
  explanation: "Continuous-time quantum walks are defined by a Hamiltonian H (typically the adjacency or Laplacian matrix of the graph) and evolve via the unitary e^(-iHt). There is no coin degree of freedom — the walker's state space is just the graph vertices. Discrete-time quantum walks, by contrast, require an additional 'coin' Hilbert space to create superposition at each step. Despite this structural difference, both types can be used to achieve similar algorithmic speedups."

- question: "How do quantum walks achieve faster search than classical random walks on graphs? What is the key mechanism?"
  type: short-answer
  answer: "Quantum walks exploit constructive interference at the target node and destructive interference elsewhere. In a quantum spatial search, a marked vertex modifies the walk's Hamiltonian (or coin operator), creating interference patterns that funnel amplitude toward the marked vertex over time. On many graphs, this achieves O(sqrt(N)) hitting time compared to O(N) for classical random walks — matching Grover's quadratic speedup. The interference is the key mechanism: classical random walks diffuse probability uniformly, while quantum walks direct it through wave-like constructive/destructive interference."
  explanation: "The quantum walk search algorithm by Childs and Goldstone (continuous-time) and Ambainis, Kempe, Rivosh (discrete-time) achieve Grover-like O(sqrt(N)) search on various graph structures. The quantum walk approach is sometimes more natural than the circuit-based Grover formulation, particularly for spatial search problems where the underlying geometry matters."
```

## Explainer

Classical random walks are a fundamental algorithmic primitive: a walker on a graph moves to a random neighbor at each step, and properties of the walk (hitting times, mixing times, stationary distributions) underlie algorithms for sampling, graph connectivity, and approximate counting. Quantum walks replace probabilistic transitions with unitary evolution, enabling coherent superposition over graph vertices and interference between paths.

**Discrete-time quantum walks** augment the walker's position with a **coin** degree of freedom. At each step, a coin operator (a unitary on the coin space) creates superposition over possible directions, and a conditional shift operator moves the walker to different neighbors based on the coin state. On a line with a 2-dimensional coin, the walk uses a Hadamard coin: H creates equal superposition of "left" and "right," and the shift moves the walker accordingly. After t steps, the probability distribution is strikingly different from the classical case — instead of a Gaussian centered at the origin with width sqrt(t), the quantum walk produces a distribution with two peaks near positions +/- t/sqrt(2), giving a linear spread rate.

**Continuous-time quantum walks** dispense with the coin entirely. The walker's state is a vector in the Hilbert space of graph vertices, and evolution is governed by the Hamiltonian H = -gamma * A (where A is the adjacency matrix and gamma is a hopping rate). The state evolves as |psi(t)> = e^(-iHt)|psi(0)>. The eigenvectors of A determine the walk's behavior: interference between eigenmodes produces spreading patterns that differ qualitatively from classical diffusion.

Quantum walks have direct algorithmic applications. **Spatial search** is the most celebrated: place a quantum walker on a graph and modify the dynamics at a marked vertex (add a phase or Hamiltonian term). On many graph structures — the complete graph, hypercubes, grids of dimension 4 or higher — the quantum walk finds the marked vertex in O(sqrt(N)) steps, matching Grover's quadratic speedup. Ambainis used quantum walks to achieve a quantum algorithm for **element distinctness** (finding two equal elements in a list) running in O(N^(2/3)) time, beating both classical O(N) and Grover-based approaches. Quantum walks also enable faster algorithms for triangle finding, matrix product verification, and other graph problems. They provide an alternative algorithmic framework to the circuit model, sometimes yielding more natural or efficient algorithms for problems with inherent geometric or graph structure.
