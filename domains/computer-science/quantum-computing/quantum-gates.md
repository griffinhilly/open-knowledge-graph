---
id: quantum-gates
title: Quantum Gates
domain: computer-science
course: quantum-computing
prerequisites:
- id: qubits-and-quantum-states
  type: hard
- id: pauli-matrices
  type: hard
- id: linear-transformations
  type: soft
tags:
- quantum-gate
- Hadamard
- CNOT
- Pauli
- phase-gate
- unitary
stage: advanced
status: validated
---
# Quantum Gates

## Core Idea
Quantum gates are unitary transformations that manipulate qubit states, analogous to classical logic gates but reversible and operating on amplitudes rather than bits. Single-qubit gates include the Pauli gates (X, Y, Z), the Hadamard gate (H), and phase gates (S, T). The controlled-NOT (CNOT) is the standard two-qubit gate. Any unitary operation on n qubits can be decomposed into single-qubit gates plus CNOT — this is the universality theorem that makes a finite gate set sufficient for arbitrary quantum computation.

## Questions

```yaml
- question: "What is the effect of the Hadamard gate H on the basis state |0>?"
  type: multiple-choice
  options: ["|1>", "(|0> - |1>)/sqrt(2)", "(|0> + |1>)/sqrt(2)", "i|0>"]
  answer: 2
  explanation: "The Hadamard gate maps |0> to (|0> + |1>)/sqrt(2) = |+>, creating an equal superposition. It also maps |1> to (|0> - |1>)/sqrt(2) = |->. The Hadamard is its own inverse (H^2 = I), so applying it twice returns to the original state."

- question: "All quantum gates must be reversible because they are represented by unitary matrices."
  type: true-false
  answer: true
  explanation: "A unitary matrix U satisfies U*U^dagger = I, which means U^dagger is the inverse operation. Every quantum gate therefore has a well-defined reverse. This contrasts with classical gates like AND and OR, which are irreversible — you cannot recover the inputs from the output. Reversibility is a fundamental requirement of quantum mechanics, not just a design choice."

- question: "What does the CNOT gate do to the two-qubit state |10>? What about |11>?"
  type: short-answer
  answer: "CNOT|10> = |11> and CNOT|11> = |10>. The CNOT flips the target qubit (second qubit) when the control qubit (first qubit) is |1>, and leaves the target unchanged when the control is |0>."
  explanation: "The CNOT acts as a conditional NOT: it applies the X (bit-flip) gate to the target qubit conditioned on the control qubit being 1. In the computational basis: |00> -> |00>, |01> -> |01>, |10> -> |11>, |11> -> |10>. When the control is in superposition, the CNOT creates entanglement — applying H then CNOT to |00> produces the Bell state (|00> + |11>)/sqrt(2)."

- question: "The Pauli Z gate leaves |0> unchanged and maps |1> to -|1>. Since measurement probabilities depend on |amplitude|^2, does the Z gate have any observable effect?"
  type: multiple-choice
  options: ["No — since |-1|^2 = 1, Z has no physically observable consequence", "Yes — the relative phase between |0> and |1> affects subsequent interference and thus future measurement outcomes", "No — global phases and relative phases are both unobservable", "Yes — the minus sign directly changes the probability of measuring |1>"]
  answer: 1
  explanation: "While a global phase (multiplying the entire state by e^(i*theta)) is unobservable, a relative phase between basis states is physically meaningful. Z changes the relative phase between |0> and |1> in a superposition. If the state is alpha|0> + beta|1>, Z produces alpha|0> - beta|1>. On the Bloch sphere, this is a 180-degree rotation about the z-axis, changing where the state sits on the equator. Subsequent Hadamard gates or other operations will translate this phase difference into a probability difference."
```

## Explainer

From your study of Pauli matrices and linear transformations, you know that quantum states are vectors and transformations are matrices. Quantum gates are the specific matrices used in quantum computation, and the key constraint is that every gate must be **unitary**: U*U^dagger = I. Unitarity preserves the norm of the state vector (probabilities sum to 1) and ensures reversibility (every gate has an inverse). This is the quantum analog of classical logic gates, but with a crucial difference — classical gates like AND are irreversible (two inputs, one output), while quantum gates must always be invertible.

The most important **single-qubit gates** form a small toolkit. The **Pauli gates** X, Y, Z are the quantum analogs of bit-flip, bit-and-phase-flip, and phase-flip respectively. X swaps |0> and |1> (like a classical NOT). Z leaves |0> alone and maps |1> to -|1>, introducing a relative phase. The **Hadamard gate** H maps |0> to (|0> + |1>)/sqrt(2) and |1> to (|0> - |1>)/sqrt(2), creating equal superpositions. H is the workhorse that creates interference — nearly every quantum algorithm starts by applying H to each qubit to create a uniform superposition over all computational basis states. The **phase gates** S and T introduce phases of i and e^(i*pi/4) respectively to the |1> component; the T gate is particularly important because {H, T, CNOT} forms a universal gate set.

The standard **two-qubit gate** is the controlled-NOT (CNOT). It has a control qubit and a target qubit: if the control is |1>, the target is flipped; if the control is |0>, nothing happens. In matrix form, it is a 4x4 permutation matrix. The CNOT is the primary entanglement-generating gate — applying H to the first qubit followed by CNOT produces the Bell state (|00> + |11>)/sqrt(2) from |00>. Other important multi-qubit gates include the controlled-Z (CZ), the Toffoli gate (controlled-controlled-NOT), and the SWAP gate, but all can be built from CNOT and single-qubit gates.

The **universality theorem** states that any unitary operation on n qubits can be approximated to arbitrary precision using only single-qubit gates and CNOT. More precisely, the set {H, T, CNOT} is universal: any n-qubit unitary can be decomposed into a finite sequence of these three gates. This is the quantum analog of the classical fact that {NAND} is a universal gate — but with the added subtlety that quantum universality requires approximation (the Solovay-Kitaev theorem quantifies how efficiently). This means hardware designers need only implement a small set of physical gates, and compilers handle the decomposition of arbitrary operations into this basis.

Understanding quantum gates requires distinguishing **global phase** from **relative phase**. Multiplying an entire state by e^(i*theta) changes nothing observable — |psi> and e^(i*theta)|psi> are the same physical state. But a phase applied to one component relative to another is physically meaningful: alpha|0> + beta|1> and alpha|0> - beta|1> are genuinely different states that produce different measurement outcomes after further gates. Gates like Z and S manipulate relative phases, which then get converted to probability differences by subsequent Hadamard gates. This interplay between phase manipulation and interference is the core mechanism of quantum algorithms.
