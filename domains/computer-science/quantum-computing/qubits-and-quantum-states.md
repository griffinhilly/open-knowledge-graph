---
id: qubits-and-quantum-states
title: Qubits and Quantum States
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-superposition
  type: hard
- id: dirac-notation
  type: hard
- id: linear-transformations
  type: soft
- id: probability-axioms-and-rules
  type: soft
tags:
- qubit
- quantum-state
- Bloch-sphere
- computational-basis
stage: advanced
status: validated
---
# Qubits and Quantum States

## Core Idea
A qubit is the fundamental unit of quantum information, analogous to a classical bit but capable of existing in a superposition of |0> and |1>. The general state of a single qubit is alpha|0> + beta|1>, where alpha and beta are complex amplitudes satisfying |alpha|^2 + |beta|^2 = 1. Multi-qubit systems live in tensor-product Hilbert spaces whose dimension grows exponentially: n qubits span a 2^n-dimensional space. This exponential state space is the source of quantum computing's potential power over classical computation.

## Questions

```yaml
- question: "A single qubit is in the state (3/5)|0> + (4/5)|1>. What is the probability of measuring |1>?"
  type: multiple-choice
  options: ["3/5", "4/5", "9/25", "16/25"]
  answer: 3
  explanation: "The probability of measuring |1> is |beta|^2 = (4/5)^2 = 16/25. A common mistake is confusing the amplitude with the probability — the amplitude is 4/5, but probability is the squared magnitude of the amplitude."

- question: "A system of 3 qubits requires a state vector with 8 complex amplitudes to fully describe it."
  type: true-false
  answer: true
  explanation: "Three qubits live in a 2^3 = 8-dimensional Hilbert space. The state vector has 8 complex components, one for each computational basis state |000> through |111>. This exponential growth — 2^n amplitudes for n qubits — is what makes classical simulation of quantum systems intractable for large n."

- question: "What distinguishes a qubit from a classical probabilistic bit that has, say, a 70% chance of being 0 and a 30% chance of being 1?"
  type: short-answer
  answer: "A qubit's state is described by complex amplitudes, not just probabilities, and these amplitudes can interfere constructively or destructively. A probabilistic classical bit has real, non-negative probabilities that always add — there is no interference. This interference between amplitudes is what enables quantum algorithms to amplify correct answers and suppress wrong ones."
  explanation: "The key distinction is interference. A probabilistic bit is a mixture described by real numbers that combine incoherently. A qubit is a coherent superposition described by complex amplitudes whose phases matter. Two paths to the same outcome can cancel (destructive interference) or reinforce (constructive interference), which has no classical analog."

- question: "On the Bloch sphere, where is the state |+> = (|0> + |1>)/sqrt(2) located relative to |0> and |1>?"
  type: multiple-choice
  options: ["At the north pole, same as |0>", "At the south pole, same as |1>", "On the equator, pointing along the +x axis", "Exactly halfway between the poles along the z axis"]
  answer: 2
  explanation: "|0> is the north pole and |1> is the south pole of the Bloch sphere. Equal superpositions like |+> lie on the equator. The phase of the superposition determines the azimuthal angle: |+> = (|0> + |1>)/sqrt(2) points along the +x direction, while |-> = (|0> - |1>)/sqrt(2) points along -x. States with relative phase i or -i point along +y or -y respectively."
```

## Explainer

A classical bit is either 0 or 1. A qubit can be in a **superposition** of both: the general single-qubit state is alpha|0> + beta|1>, where alpha and beta are complex numbers called **amplitudes**. The constraint |alpha|^2 + |beta|^2 = 1 ensures that the probabilities of measuring 0 or 1 sum to one. From your study of quantum superposition and Dirac notation, you know the formalism; quantum computing repurposes it as information processing. The states |0> and |1> are the **computational basis** — column vectors [1,0]^T and [0,1]^T in the two-dimensional Hilbert space C^2.

The **Bloch sphere** provides geometric intuition for single-qubit states. Any pure state can be parameterized as cos(theta/2)|0> + e^(i*phi) sin(theta/2)|0>, where theta is the polar angle and phi is the azimuthal angle. The north pole is |0>, the south pole is |1>, and equal superpositions live on the equator. Quantum gates correspond to rotations of this sphere. The Bloch sphere works only for single qubits — multi-qubit states cannot be visualized this simply because of entanglement.

When multiple qubits are combined, the state space grows exponentially. Two qubits live in C^2 tensor C^2 = C^4, spanned by |00>, |01>, |10>, |11>. Three qubits span C^8. In general, n qubits require 2^n complex amplitudes to describe. This is the fundamental resource of quantum computing: a 300-qubit system has more amplitudes than there are atoms in the observable universe. But this exponential richness is not freely accessible — measurement collapses the state to a single basis vector, and the art of quantum algorithm design is arranging interference so that the measurement outcome is useful.

The distinction between a qubit and a classical probabilistic bit is critical. A coin that is 50% heads and 50% tails is described by a probability distribution — a statistical mixture with no internal structure. The state |+> = (|0> + |1>)/sqrt(2) is also measured as 0 or 1 with equal probability, but its amplitudes are complex numbers with definite phases. Two amplitude paths to the same outcome can reinforce or cancel depending on their relative phase. This **interference** is the engine of quantum speedups: algorithms like Deutsch-Jozsa and Grover's search work by arranging phases so that correct answers receive constructive interference and wrong answers receive destructive interference. Without interference — if qubits were just probabilistic bits — no quantum advantage would exist.

Multi-qubit states can also be **entangled**, meaning the joint state cannot be factored as a product of individual qubit states. The Bell state (|00> + |11>)/sqrt(2) has this property: neither qubit has a definite state on its own, but measuring one instantly determines the other. Entanglement is a uniquely quantum resource with no classical analog, and it plays a central role in quantum teleportation, superdense coding, and quantum error correction. The combination of superposition, interference, and entanglement in an exponentially large state space is what gives quantum computing its distinctive character.
