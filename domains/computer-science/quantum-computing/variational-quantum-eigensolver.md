---
id: variational-quantum-eigensolver
title: Variational Quantum Eigensolver (VQE)
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-circuits
  type: hard
- id: quantum-measurement-and-born-rule
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
tags:
- VQE
- variational
- NISQ
- quantum-chemistry
- hybrid-algorithm
stage: expert
status: validated
---
# Variational Quantum Eigensolver (VQE)

## Core Idea
The variational quantum eigensolver (VQE) is a hybrid quantum-classical algorithm that finds the ground-state energy of a Hamiltonian by variationally optimizing a parameterized quantum circuit (ansatz). The quantum computer prepares a trial state |psi(theta)> and measures the expectation value <psi(theta)|H|psi(theta)>; a classical optimizer updates theta to minimize this energy. By the variational principle, the measured energy is always an upper bound on the true ground-state energy. VQE is designed for near-term noisy intermediate-scale quantum (NISQ) devices, requiring shallow circuits that tolerate noise, at the cost of requiring many measurement repetitions and classical optimization iterations.

## Questions

```yaml
- question: "The variational principle guarantees that for any trial state |psi>, the expectation value <psi|H|psi> is:"
  type: multiple-choice
  options: ["Equal to the ground-state energy E_0", "Less than or equal to E_0", "Greater than or equal to E_0", "Unrelated to E_0"]
  answer: 2
  explanation: "The variational principle states that for any normalized state |psi>, <psi|H|psi> >= E_0 where E_0 is the ground-state energy. Equality holds only when |psi> is the ground state. This means the measured energy always provides an upper bound, and minimizing over the parameters theta approaches E_0 from above. This is what makes VQE a rigorous method: even with noise and limited optimization, the result is a valid upper bound."

- question: "VQE uses only the quantum computer for optimization — the classical computer is not involved in the parameter update."
  type: true-false
  answer: false
  explanation: "VQE is explicitly a hybrid quantum-classical algorithm. The quantum computer prepares states and measures expectation values — tasks that are hard classically for large systems. The classical computer runs the optimization loop (gradient descent, COBYLA, SPSA, etc.) that updates the circuit parameters based on the measured energies. Neither component alone suffices: the quantum computer cannot optimize, and the classical computer cannot efficiently compute expectation values for large quantum systems."

- question: "What is the 'ansatz' in VQE, and why is its choice critical to the algorithm's success?"
  type: short-answer
  answer: "The ansatz is the parameterized quantum circuit that defines the family of trial states |psi(theta)>. Its choice is critical because it determines the expressiveness of the search space. If the ansatz cannot represent the true ground state (or a good approximation), the optimization will converge to a local minimum far above the true energy. However, overly expressive ansatze with many parameters suffer from barren plateaus (vanishing gradients) and require more measurements. The best ansatze are problem-inspired — for chemistry, the Unitary Coupled Cluster ansatz captures electron correlation structure while remaining relatively compact."
  explanation: "The ansatz design is the art of VQE. Hardware-efficient ansatze use gates native to the device, minimizing circuit depth, but may lack physical motivation and suffer from optimization difficulties. Chemically-motivated ansatze like UCCSD capture the right physics but may require deeper circuits. The barren plateau phenomenon — where gradients vanish exponentially with system size for random ansatze — is a fundamental challenge that constrains the practical scalability of VQE."
```

## Explainer

Quantum chemistry is one of the most promising near-term applications of quantum computing. The core computational problem is finding the ground-state energy of a molecular Hamiltonian — determining how electrons arrange themselves to minimize energy. For small molecules, classical computers handle this well, but the Hilbert space grows exponentially with the number of electrons, making exact classical solutions intractable beyond about 50 electrons. Quantum computers can represent quantum states natively, but fault-tolerant algorithms like quantum phase estimation require error-corrected qubits that are not yet available at scale. VQE fills this gap by running on noisy, near-term hardware.

The algorithm has a simple structure. **Step 1**: Choose a parameterized quantum circuit U(theta) — the ansatz — that maps |0>^n to a trial state |psi(theta)> = U(theta)|0>^n. **Step 2**: Prepare |psi(theta)> on the quantum computer and estimate E(theta) = <psi(theta)|H|psi(theta)> by decomposing H into a sum of Pauli strings and measuring each term's expectation value. **Step 3**: Feed E(theta) to a classical optimizer, which proposes new parameters theta'. **Step 4**: Repeat until convergence. The final E(theta*) is an upper bound on the ground-state energy, with equality when the ansatz can express the true ground state.

The decomposition of H into measurable terms is a key practical step. A molecular Hamiltonian in second-quantized form is mapped to qubits using transformations like Jordan-Wigner or Bravyi-Kitaev, producing a sum of O(N^4) Pauli strings for N spin-orbitals. Each Pauli string's expectation value is estimated from repeated measurements (shots). The total number of measurements required can be very large — this **measurement overhead** is a significant bottleneck. Techniques like grouping commuting Pauli terms and using classical shadows reduce this cost.

VQE's main challenges are **barren plateaus** (exponentially vanishing gradients for deep or random circuits, making optimization intractable), **noise** (gate errors bias the energy estimate, though error mitigation techniques can partially compensate), and **local minima** in the optimization landscape. Despite these challenges, VQE has been demonstrated on real quantum hardware for small molecules (H2, LiH, BeH2) and remains a leading candidate for achieving quantum advantage in chemistry. The broader principle it embodies — using the quantum computer as a state preparation and measurement device while offloading optimization to a classical computer — is the template for all NISQ-era variational algorithms.
