---
id: superdense-coding
title: Superdense Coding
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-circuits
  type: hard
- id: quantum-measurement-and-born-rule
  type: hard
- id: entanglement
  type: hard
tags:
- superdense-coding
- entanglement
- classical-communication
- Bell-states
stage: advanced
status: validated
---
# Superdense Coding

## Core Idea
Superdense coding is a quantum communication protocol that transmits two classical bits by sending only one qubit, using a pre-shared entangled pair. Alice encodes her two-bit message by applying one of four Pauli operations (I, X, Z, XZ) to her half of a Bell pair, then sends that qubit to Bob. Bob performs a Bell measurement on both qubits to recover the two-bit message with certainty. It is the dual of quantum teleportation: teleportation sends one qubit using two classical bits and shared entanglement; superdense coding sends two classical bits using one qubit and shared entanglement.

## Questions

```yaml
- question: "In superdense coding, Alice applies the Z gate to her qubit to encode message '10'. What Bell state does the shared pair become after this operation?"
  type: multiple-choice
  options: ["(|00> + |11>)/sqrt(2)", "(|00> - |11>)/sqrt(2)", "(|01> + |10>)/sqrt(2)", "(|01> - |10>)/sqrt(2)"]
  answer: 1
  explanation: "Starting from the Bell state (|00> + |11>)/sqrt(2), applying Z to Alice's qubit (the first qubit) gives Z|0>|0>/sqrt(2) + Z|1>|1>/sqrt(2) = |0>|0>/sqrt(2) - |1>|1>/sqrt(2) = (|00> - |11>)/sqrt(2). Each of the four Pauli operations maps the initial Bell state to a different, orthogonal Bell state, which is why Bob can distinguish all four messages perfectly."

- question: "Superdense coding allows transmitting information faster than light because only a qubit needs to travel."
  type: true-false
  answer: false
  explanation: "Alice still sends a physical qubit to Bob, which travels at most at the speed of light. The advantage is bandwidth, not speed: one qubit carries two classical bits of information (with the help of pre-shared entanglement). The entanglement distribution also required prior physical communication. No part of the protocol violates relativistic causality."

- question: "Why does superdense coding require a pre-shared entangled pair? What would happen if Alice just applied one of four unitaries to a single qubit in state |0> and sent it to Bob?"
  type: short-answer
  answer: "Without entanglement, Alice can only encode information in the state of a single qubit — a two-dimensional space. Four orthogonal states cannot exist in two dimensions, so Bob cannot perfectly distinguish four messages from a single qubit measurement. The entangled pair provides a second qubit at Bob's location, giving him access to a four-dimensional space (two qubits) where the four Bell states are orthogonal and perfectly distinguishable."
  explanation: "This connects to the Holevo bound: a single qubit, without entanglement assistance, can convey at most one classical bit reliably. Superdense coding achieves two bits because the entangled pair effectively provides a pre-positioned second qubit that doubles the accessible Hilbert space dimension at Bob's end. The entanglement is a resource that is consumed in the process."
```

## Explainer

Superdense coding demonstrates that entanglement has concrete operational value as a communication resource. The protocol begins with Alice and Bob sharing a Bell pair (|00> + |11>)/sqrt(2), with Alice holding the first qubit and Bob holding the second. Alice wants to send a two-bit classical message — one of {00, 01, 10, 11}. She encodes her message by applying one of four operations to her qubit: I for 00, X for 01, Z for 10, or XZ for 11. Each operation transforms the shared Bell state into a different, orthogonal Bell state.

The four Bell states are: Phi+ = (|00> + |11>)/sqrt(2), Psi+ = (|01> + |10>)/sqrt(2), Phi- = (|00> - |11>)/sqrt(2), Psi- = (|01> - |10>)/sqrt(2). They form an orthonormal basis for the two-qubit Hilbert space. After Alice's encoding, she sends her qubit to Bob. Bob now holds both qubits and performs a **Bell measurement** — CNOT followed by Hadamard on the first qubit, then computational-basis measurement of both. Because the four Bell states are orthogonal, Bob distinguishes them with certainty and recovers Alice's two-bit message perfectly.

The protocol achieves something classically impossible: sending two bits of information through one quantum channel use. Without entanglement, the Holevo bound limits a single qubit to carrying at most one classical bit of reliable information. The entangled pair provides the extra dimension — Bob already has a qubit that is correlated with Alice's, so when Alice's qubit arrives, Bob has access to the full four-dimensional two-qubit space. The entanglement is consumed: after Bob's measurement, the pair is no longer entangled.

Superdense coding and quantum teleportation are **dual protocols** with an elegant resource symmetry. Teleportation consumes one entangled pair plus two classical bits to transmit one qubit. Superdense coding consumes one entangled pair plus one qubit to transmit two classical bits. In both cases, entanglement serves as a catalyst that enhances the capacity of the other channel. This duality is one of the foundational results of quantum information theory and motivates the study of entanglement as a quantifiable, fungible resource.
