---
id: quantum-teleportation
title: Quantum Teleportation
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
- teleportation
- entanglement
- Bell-measurement
- classical-communication
stage: advanced
status: validated
---
# Quantum Teleportation

## Core Idea
Quantum teleportation is a protocol that transmits an unknown qubit state from one party (Alice) to another (Bob) using a shared entangled pair and two classical bits of communication. Alice performs a Bell-basis measurement on her unknown qubit and her half of the entangled pair, then sends the two-bit outcome to Bob, who applies a corrective Pauli gate to recover the original state. No physical qubit travels between them, no faster-than-light communication occurs, and the original state is destroyed in the process — consistent with the no-cloning theorem.

## Questions

```yaml
- question: "In quantum teleportation, why are two classical bits of communication required?"
  type: multiple-choice
  options: ["To transmit the qubit's amplitude information directly", "To tell Bob which of four possible corrective operations to apply based on Alice's Bell measurement outcome", "To verify that the teleportation succeeded", "To establish the entangled pair between Alice and Bob"]
  answer: 1
  explanation: "Alice's Bell measurement has four equally likely outcomes, each corresponding to one of the four Pauli operators {I, X, Z, XZ} that Bob must apply to recover the original state. Two classical bits encode which of the four outcomes occurred. Without this classical message, Bob's qubit is in a completely random state — the entanglement alone does not transmit information."

- question: "Quantum teleportation allows faster-than-light communication because the state transfer is instantaneous once Alice measures."
  type: true-false
  answer: false
  explanation: "After Alice's measurement, Bob's qubit is in one of four equally likely states, each of which is maximally mixed (completely random) from Bob's perspective. Bob cannot extract any information until he receives Alice's two classical bits, which travel at most at the speed of light. The protocol therefore respects relativistic causality. Entanglement enables correlation, not communication."

- question: "After teleportation, Alice's original qubit is in the state that was teleported to Bob. True or false, and why?"
  type: short-answer
  answer: "False. Alice's original qubit has been measured as part of the Bell measurement and has collapsed into a Bell basis state. The original state no longer exists at Alice's location — it has been transferred to Bob. This is consistent with the no-cloning theorem: the state was moved, not copied."
  explanation: "Teleportation is fundamentally a state transfer, not a state copy. The Bell measurement at Alice's end irreversibly destroys the input state's coherence, projecting it onto one of four entangled states with her half of the shared pair. The quantum information is gone from Alice's side and reconstructed at Bob's side after correction. If the original survived, we would have two copies of an unknown quantum state, violating the no-cloning theorem."
```

## Explainer

Quantum teleportation seems paradoxical — transmitting a quantum state without sending a quantum particle — but the protocol is straightforward once you trace through the circuit. The setup requires three qubits: qubit 1 is Alice's unknown state |psi> = alpha|0> + beta|1> that she wants to send, and qubits 2 and 3 form a Bell pair (|00> + |11>)/sqrt(2) shared between Alice (qubit 2) and Bob (qubit 3). Alice holds qubits 1 and 2; Bob holds qubit 3.

Alice performs a **Bell measurement** on qubits 1 and 2. This is implemented by applying CNOT (control = qubit 1, target = qubit 2) followed by Hadamard on qubit 1, then measuring both in the computational basis. The four possible two-bit outcomes (00, 01, 10, 11) occur with equal probability 1/4 regardless of the input state |psi>. The key fact, which you can verify by writing out the algebra, is that for each outcome, Bob's qubit 3 is in a state related to |psi> by a known Pauli transformation: outcome 00 means Bob has |psi>, outcome 01 means Bob has X|psi>, outcome 10 means Z|psi>, and outcome 11 means XZ|psi>.

Alice sends her two-bit measurement result to Bob over a classical channel. Bob applies the corresponding correction: I, X, Z, or XZ. After correction, Bob's qubit is in exactly the state |psi>, with all amplitude and phase information preserved. The teleportation is complete. Notice that the classical communication is essential — without it, Bob's qubit is in a uniformly random state from his perspective. This is why teleportation does not violate special relativity: the useful information only arrives when the classical bits do, which cannot travel faster than light.

Several features of this protocol are worth emphasizing. First, Alice never learns the state |psi> — the Bell measurement destroys the original and produces only two classical bits. Second, the protocol works for any state, including entangled states (teleporting one half of an entangled pair). Third, the entangled pair is consumed: after the protocol, qubits 2 and 3 are no longer entangled. Teleportation thus consumes one entangled pair plus two classical bits to transmit one qubit of quantum information. This resource accounting is the starting point for quantum Shannon theory, which characterizes the fundamental communication costs of quantum information protocols.
