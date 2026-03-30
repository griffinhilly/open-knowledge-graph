---
id: no-cloning-theorem
title: No-Cloning Theorem
domain: computer-science
course: quantum-computing
prerequisites:
- id: qubits-and-quantum-states
  type: hard
- id: quantum-gates
  type: hard
tags:
- no-cloning
- fundamental-theorem
- linearity
- quantum-information
stage: expert
status: validated
---
# No-Cloning Theorem

## Core Idea
The no-cloning theorem states that no quantum operation can create an identical copy of an arbitrary unknown quantum state. Given an unknown state |psi>, there is no unitary U such that U(|psi>|0>) = |psi>|psi> for all |psi>. The proof follows directly from the linearity of quantum mechanics: cloning two different states leads to a contradiction with the superposition principle. No-cloning has profound consequences — it prevents simple redundancy-based error correction, makes quantum information fundamentally different from classical information, and is the basis for the security of quantum key distribution.

## Questions

```yaml
- question: "The no-cloning theorem says you cannot copy an unknown quantum state. Can you copy a KNOWN quantum state?"
  type: multiple-choice
  options: ["No — the theorem forbids copying any quantum state", "Yes — if you know the state, you can prepare as many copies as you want by running the appropriate state-preparation circuit", "Only if the state is a computational basis state", "Only if you have a quantum copier calibrated for that specific state"]
  answer: 1
  explanation: "The no-cloning theorem applies to UNKNOWN states — you cannot build a device that copies an arbitrary input state without knowing what it is. But if you know the state (e.g., someone tells you it is (|0> + |1>)/sqrt(2)), you can prepare as many copies as you want by applying Hadamard to fresh |0> qubits. The theorem constrains devices that must work for all input states, not the preparation of specific known states."

- question: "The no-cloning theorem follows from the unitarity of quantum mechanics — specifically, from the fact that quantum evolution is linear."
  type: true-false
  answer: true
  explanation: "The proof is elegant. Suppose a unitary U clones: U|a>|0> = |a>|a> and U|b>|0> = |b>|b>. Taking the inner product of both sides: <a|b> = (<a|b>)^2. This equation has only two solutions: <a|b> = 0 or <a|b> = 1, meaning |a> and |b> must be either identical or orthogonal. A cloner that works for two non-orthogonal states leads to a contradiction. The linearity of U is what forces the inner product equation, so no-cloning is a direct consequence of quantum mechanics being a linear theory."

- question: "How does the no-cloning theorem make quantum key distribution secure? What would happen if cloning were possible?"
  type: short-answer
  answer: "If cloning were possible, an eavesdropper could intercept each qubit in transit, make a copy, send the original to the receiver, and later analyze the copy in the correct basis (learned from the public basis reconciliation). This would allow perfect undetectable eavesdropping, destroying QKD security. No-cloning prevents this: Eve must measure the qubit directly, which disturbs it and introduces detectable errors. The impossibility of cloning forces any information-gathering strategy to be invasive."
  explanation: "No-cloning is essential to QKD but also to the broader structure of quantum information. It means quantum information cannot be broadcast, cannot be backed up, and cannot be passively observed without disturbance. These properties are limitations from a computing perspective (making error correction harder) but resources from a cryptographic perspective (making eavesdropping detectable)."
```

## Explainer

The no-cloning theorem, proved by Wootters and Zurek (and independently by Dieks) in 1982, is one of the most fundamental results in quantum information theory. It states a simple but profound fact: there is no physical process that takes an arbitrary unknown quantum state and produces two identical copies of it. This is in stark contrast to classical information, which can be copied freely — you can duplicate a file, photocopy a document, or read a bit without destroying it.

The proof is surprisingly short. Assume a unitary operator U acts on two qubits — the input state and a blank qubit — such that U copies: U|a>|0> = |a>|a> for all states |a>. Consider two specific states |a> and |b>. By assumption, U|a>|0> = |a>|a> and U|b>|0> = |b>|b>. Take the inner product of the left-hand sides and the right-hand sides: (<a|<0|)(U^dagger U)(|b>|0>) = (<a|<a|)(|b>|b>). The left side is <a|b> (since U is unitary, U^dagger U = I, and <0|0> = 1). The right side is <a|b> * <a|b> = (<a|b>)^2. So <a|b> = (<a|b>)^2, which is satisfied only when <a|b> = 0 or <a|b> = 1 — the states are orthogonal or identical. A universal cloner that works for any pair of non-orthogonal states is impossible.

The consequences pervade quantum information science. **Error correction** cannot use classical copying — you cannot protect a qubit by making backup copies. Instead, quantum error correction encodes information into entangled multi-qubit states, a fundamentally different strategy. **State tomography** is limited — you cannot determine an unknown state from a single copy, because you cannot make copies to measure in multiple bases. You need many identically prepared copies. **Quantum teleportation** moves a state rather than copying it — the original is destroyed in the process, maintaining consistency with no-cloning.

On the positive side, no-cloning is the foundation of **quantum cryptography**. In BB84 key distribution, an eavesdropper cannot copy the transmitted qubits, analyze the copies later (after learning the correct measurement bases), and remain undetected. Any attempt to gain information about the state must involve direct measurement, which disturbs it. This information-disturbance tradeoff, rooted in no-cloning, provides the information-theoretic security guarantee. Classically, an eavesdropper can passively copy any signal on a communication line without the sender or receiver knowing. Quantum mechanics forbids this, turning a fundamental limitation (no copying) into a practical resource (secure communication).
