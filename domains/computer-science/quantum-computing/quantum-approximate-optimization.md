---
id: quantum-approximate-optimization
title: Quantum Approximate Optimization Algorithm (QAOA)
domain: computer-science
course: quantum-computing
prerequisites:
- id: variational-quantum-eigensolver
  type: hard
- id: quantum-circuits
  type: hard
- id: grovers-search-algorithm
  type: soft
tags:
- QAOA
- optimization
- combinatorial
- NISQ
- MaxCut
stage: expert
status: validated
---
# Quantum Approximate Optimization Algorithm (QAOA)

## Core Idea
The Quantum Approximate Optimization Algorithm (QAOA) is a variational hybrid quantum-classical algorithm for approximately solving combinatorial optimization problems. It alternates between a problem Hamiltonian (encoding the objective function as phases) and a mixing Hamiltonian (creating transitions between candidate solutions), with p layers of parameterized rotations. The circuit depth grows linearly with p, and as p increases, QAOA interpolates between a single-round heuristic and the adiabatic algorithm (which is exact in the infinite-depth limit). QAOA is a leading candidate for near-term quantum advantage on optimization problems like MaxCut, satisfiability, and portfolio optimization.

## Questions

```yaml
- question: "In QAOA for the MaxCut problem, what role does the problem unitary e^(-i*gamma*C) play, where C is the cost Hamiltonian?"
  type: multiple-choice
  options: ["It measures the quality of the current solution", "It applies a phase proportional to the cut value of each computational basis state, encoding the objective function into the quantum state", "It mixes between different solutions to explore the search space", "It projects the state onto the optimal solution"]
  answer: 1
  explanation: "The problem unitary e^(-i*gamma*C) applies a phase e^(-i*gamma*C(z)) to each computational basis state |z>, where C(z) is the cut value. States with higher cut values acquire different phases than states with lower cut values. This phase encoding is analogous to the oracle in Grover's algorithm — it marks good solutions. The subsequent mixing unitary then creates interference that can amplify high-quality solutions."

- question: "QAOA with p=1 (one layer) is guaranteed to find the optimal solution for any combinatorial optimization problem."
  type: true-false
  answer: false
  explanation: "QAOA at depth p=1 is a low-depth heuristic that provides a guaranteed approximation ratio for some problems (e.g., at least 0.6924 of optimal for MaxCut on 3-regular graphs) but does not find the exact optimum in general. As p increases, the algorithm can explore more of the solution space. In the limit p -> infinity, QAOA converges to the adiabatic algorithm and can in principle find the exact optimum, but this requires circuit depth that may grow with problem size."

- question: "How does QAOA differ from VQE in its circuit structure, and why might this difference matter for practical performance?"
  type: short-answer
  answer: "VQE uses a general parameterized ansatz (hardware-efficient or chemically inspired) with no prescribed structure. QAOA has a specific structure: alternating layers of the problem unitary e^(-i*gamma*C) and mixing unitary e^(-i*beta*B), with 2p parameters for p layers. This structure is problem-aware — the problem Hamiltonian C directly encodes the optimization objective. The structured ansatz may resist barren plateaus better than generic ansatze because the parameters have clear physical meaning (problem encoding strength and mixing rate), and the landscape has structure related to the optimization problem."
  explanation: "QAOA's structured ansatz is both its strength and limitation. The problem-specific structure means good parameters often concentrate around certain values independent of instance details, which helps with transferability and initialization. However, the rigid structure limits expressiveness at low depth. VQE's flexibility allows it to adapt to problem structure more freely but at the cost of harder optimization. In practice, both face similar challenges of measurement overhead and classical optimization difficulty."
```

## Explainer

Combinatorial optimization problems — finding the best configuration among exponentially many candidates — are ubiquitous in logistics, finance, machine learning, and physics. Many are NP-hard, so no polynomial-time classical algorithm is expected. QAOA provides a quantum approach that may offer practical advantages for approximate solutions, even on near-term hardware without error correction.

The algorithm is defined by a **problem Hamiltonian** C (a diagonal operator whose eigenvalues are the objective function values on each computational basis state) and a **mixing Hamiltonian** B (typically the sum of Pauli X operators on all qubits, generating transitions between basis states). For MaxCut, C = sum over edges (i,j) of (1 - Z_i * Z_j)/2, which counts the number of cut edges for each bit-string assignment. The initial state is |+>^n (uniform superposition). The QAOA circuit applies p alternating layers: first e^(-i*gamma_k*C) (the problem unitary), then e^(-i*beta_k*B) (the mixer), for k = 1 to p. The 2p parameters {gamma_1,...,gamma_p, beta_1,...,beta_p} are optimized classically to maximize the expected value of C.

The QAOA circuit encodes a physical process: the problem unitary imprints the objective function as phases (good solutions get different phases than bad ones), and the mixer creates superpositions that allow interference between solutions. After p rounds, constructive interference at high-quality solutions and destructive interference at low-quality solutions biases the final measurement toward good answers. At depth p=1 for MaxCut on 3-regular graphs, QAOA provably achieves an approximation ratio of at least 0.6924 — better than random but short of the best classical algorithm (Goemans-Williamson at 0.878). As p increases, the approximation ratio improves.

In the limit p -> infinity, QAOA becomes equivalent to the **quantum adiabatic algorithm**: start in the ground state of B (the uniform superposition) and slowly interpolate the Hamiltonian from B to C. The adiabatic theorem guarantees that if the interpolation is slow enough, the system stays in the ground state, arriving at the optimal solution. QAOA with finite p is a Trotterized, variational version of this process. The open question is whether QAOA at moderate depth p = O(poly(n)) can achieve better approximation ratios than the best classical algorithms for specific problems. Recent results show that QAOA can outperform classical local algorithms on certain structured instances, but a definitive quantum advantage for optimization has not yet been demonstrated. QAOA remains one of the most studied algorithms for near-term quantum devices.
