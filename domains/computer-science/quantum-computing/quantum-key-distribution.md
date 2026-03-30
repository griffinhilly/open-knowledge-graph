---
id: quantum-key-distribution
title: Quantum Key Distribution (BB84)
domain: computer-science
course: quantum-computing
prerequisites:
- id: qubits-and-quantum-states
  type: hard
- id: quantum-measurement-and-born-rule
  type: hard
- id: no-cloning-theorem
  type: hard
tags:
- BB84
- QKD
- cryptography
- eavesdropping
- information-theoretic-security
stage: expert
status: validated
---
# Quantum Key Distribution (BB84)

## Core Idea
Quantum key distribution (QKD) enables two parties to establish a shared secret key whose security is guaranteed by the laws of quantum mechanics, not computational hardness assumptions. The BB84 protocol (Bennett-Brassard 1984) works by encoding random bits in one of two conjugate bases (rectilinear or diagonal). An eavesdropper measuring the qubits inevitably disturbs them (by the no-cloning theorem and measurement disturbance), introducing detectable errors. After basis reconciliation and error estimation, the parties distill a secure key. BB84 achieves information-theoretic security — it is provably secure even against adversaries with unlimited computational power, including quantum computers.

## Questions

```yaml
- question: "In BB84, Alice sends qubits encoded in one of two bases: the Z basis ({|0>, |1>}) or the X basis ({|+>, |->}). Why are two non-orthogonal bases necessary instead of just one?"
  type: multiple-choice
  options: ["Two bases are needed for error correction during key distillation", "With one basis, an eavesdropper could measure every qubit without disturbance since the measurement basis would always be correct", "Two bases double the key generation rate", "Two bases are required by the no-cloning theorem"]
  answer: 1
  explanation: "If Alice always used the Z basis, Eve could measure in the Z basis and forward the result to Bob without introducing any disturbance — perfect eavesdropping. With two bases, Eve does not know which basis Alice used for each qubit. Measuring a Z-basis qubit in the X basis (or vice versa) randomizes the result, and forwarding the wrong-basis measurement to Bob introduces a 25% error rate in the sifted key. This detectable error is the security mechanism."

- question: "BB84's security relies on computational hardness — if an eavesdropper had sufficient computing power, the key could be compromised."
  type: true-false
  answer: false
  explanation: "BB84 has information-theoretic security, meaning it is secure against any adversary regardless of computational power — including quantum computers. The security is based on the physical laws of quantum mechanics (no-cloning, measurement disturbance), not on the computational difficulty of any mathematical problem. This is a fundamental advantage over classical public-key cryptography (RSA, Diffie-Hellman), which relies on unproven computational hardness assumptions."

- question: "After the quantum transmission phase of BB84, Alice and Bob publicly compare their basis choices and discard mismatched rounds. Why doesn't this public discussion compromise security?"
  type: short-answer
  answer: "The public discussion reveals only which basis was used for each qubit, not the bit values. For matched-basis rounds, Alice's bit and Bob's bit should agree (in the absence of eavesdropping). The bit values are never communicated publicly. An eavesdropper who intercepted the qubits has already committed to a measurement basis before this discussion occurs — learning the correct basis after the fact does not help, because the measurement has already disturbed the qubits in the mismatched-basis cases."
  explanation: "The basis reconciliation step is a clever use of classical communication that extracts useful key bits from the quantum transmission without leaking them. Only the basis labels are shared, not the measurement outcomes. The key bits come from the subset of rounds where Alice and Bob happened to use the same basis — about 50% of the total. This wastes half the qubits but ensures that both parties have the same bit value for each kept round (modulo noise and eavesdropping)."
```

## Explainer

Classical cryptography faces a fundamental problem: the security of widely used public-key systems (RSA, elliptic curves) rests on assumptions about the computational hardness of certain mathematical problems — assumptions that Shor's algorithm would break. Quantum key distribution offers a qualitatively different kind of security: one based on physics rather than mathematics. The BB84 protocol, proposed by Bennett and Brassard in 1984, uses quantum mechanics to distribute a shared secret key between two parties in a way that any eavesdropping attempt is detectable.

The protocol works as follows. **Alice** prepares random qubits, each encoding a random bit in a randomly chosen basis: either the Z basis (|0> for 0, |1> for 1) or the X basis (|+> for 0, |-> for 1). She sends these qubits to **Bob**, who measures each in a randomly chosen basis (Z or X). When their bases match (about 50% of the time), their bit values agree perfectly. When bases mismatch, Bob's result is completely random. Alice and Bob publicly compare their basis choices (not bit values) and keep only the rounds where they used the same basis — this is **sifting**, producing the raw key.

**Eavesdropping detection** comes next. Suppose **Eve** intercepts qubits, measures them, and resends them to Bob (an intercept-resend attack). Eve does not know Alice's basis, so she guesses randomly. When Eve guesses wrong (50% of the time), her measurement disturbs the qubit, and when Bob subsequently measures in Alice's correct basis, he gets a random result instead of Alice's bit. This introduces an error rate of approximately 25% in the sifted key. Alice and Bob sacrifice a random subset of their sifted key bits, compare them publicly, and check the error rate. An error rate significantly above the channel noise threshold indicates eavesdropping, and they abort.

If the error rate is acceptably low, Alice and Bob apply **error correction** (to fix the remaining errors) and **privacy amplification** (to eliminate any partial information Eve may have gained). The result is a shorter but provably secure shared secret key. The security proof, formalized by Lo, Chau, Shor, Preskill, and others, shows that any eavesdropping strategy — including sophisticated quantum attacks beyond intercept-resend — is detectable. The proof relies on the **no-cloning theorem** (Eve cannot copy the qubits and keep them for later analysis) and the **information-disturbance tradeoff** (gaining information about a quantum state necessarily disturbs it). QKD has been commercially deployed over fiber-optic links and demonstrated via satellite (the Micius experiment), making it the most mature application of quantum information science.
