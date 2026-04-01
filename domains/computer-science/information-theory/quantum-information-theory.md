---
id: quantum-information-theory
title: Quantum Information Theory
domain: computer-science
course: information-theory
prerequisites:
- id: shannon-entropy
  type: hard
- id: mutual-information
  type: hard
- id: channel-capacity
  type: soft
builds-toward: []
tags:
- quantum entropy
- von Neumann entropy
- quantum channel
- quantum capacity
- entanglement
- quantum key distribution
stage: expert
status: validated
---

# Quantum Information Theory

## Core Idea
Quantum information theory extends Shannon's classical information theory to quantum systems. The fundamental quantum analog is the **von Neumann entropy** S(rho) = -Tr[rho log_2(rho)], where rho is a density matrix representing a quantum state. Like Shannon entropy, von Neumann entropy quantifies uncertainty and is maximized for completely mixed states. However, quantum information differs profoundly: quantum states cannot be copied (no-cloning theorem), entanglement creates correlations with no classical analog, and quantum channels have capacities for classical bits, quantum bits (qubits), and entanglement-assisted communication that differ. The quantum capacity C_Q of a channel represents the number of qubits that can be reliably transmitted per channel use. Quantum key distribution (QKD) uses quantum states to distribute cryptographic keys information-theoretically secure against eavesdroppers. Quantum information theory unifies quantum mechanics, information theory, and cryptography, with profound implications for communication, computation, and security.

## Questions

```yaml
- question: "The von Neumann entropy S(rho) = -Tr[rho log_2(rho)] is the quantum analog of Shannon entropy. For a pure quantum state |psi>, what is S(|psi>)?"
  type: multiple-choice
  options:
    - "S(|psi>) = 1 bit, because the state is deterministic"
    - "S(|psi>) = 0 bits — a pure state has zero entropy because it is completely determined"
    - "S(|psi>) = log_2(d) where d is the Hilbert space dimension"
    - "S(|psi>) cannot be defined for pure states"
  answer: 1
  explanation: "A pure state |psi> has density matrix rho = |psi><psi|, which has a single eigenvalue 1 and all others 0. Then S(rho) = -1*log_2(1) = 0. A pure state is maximally certain — if you measure the system, you get |psi> with probability 1. The maximally mixed state (equal superposition of all basis states) has S = log_2(d), where d is dimension. Pure states have zero entropy; mixed states have positive entropy. This parallels Shannon entropy: a deterministic classical variable has H = 0."

- question: "The no-cloning theorem states that an unknown quantum state cannot be perfectly cloned. This has no classical analog and fundamentally constrains quantum communication."
  type: true-false
  answer: true
  explanation: "In classical information, copying data is free (make a backup file). In quantum mechanics, Wiesner and Dieks proved independently that no quantum circuit can clone an arbitrary unknown state |psi>. Proof: suppose U clones |psi> to |psi>|psi>. For two different states |psi> and |phi>, U(|psi>|0>) = |psi>|psi> and U(|phi>|0>) = |phi>|phi>. But unitarity requires <psi|phi> = <psi|phi><psi|phi>, which is impossible unless <psi|phi> = 0 or 1 (orthogonal or identical states). Thus cloning fails for unknown non-orthogonal states. This explains why quantum key distribution achieves information-theoretic security: an eavesdropper cannot clone the quantum states used to communicate the key without disturbing them, allowing detection."

- question: "Explain the relationship between quantum capacity, classical capacity, and entanglement-assisted capacity of a quantum channel. Why are these three different?"
  type: short-answer
  answer: "A quantum channel describes how quantum states transform (decohere) when transmitted: rho -> N(rho). The **classical capacity** C is the maximum rate (in bits per channel use) of classical information that can be reliably sent by encoding into quantum states and decoding at the receiver — it is the quantum analog of Shannon capacity. The **quantum capacity** C_Q is the maximum rate of qubits (quantum information) that can be reliably transmitted and decoded in quantum form. The **entanglement-assisted capacity** C_E is the classical capacity when sender and receiver share pre-distributed entanglement. Remarkably, C_E can be twice C (for some channels), and C_Q can be positive even when C = 0 (superactivation). These differences arise because quantum entanglement creates correlations with no classical analog, allowing simultaneous encoding of both classical and quantum information in entangled states. Classical information always separates as individual bits; quantum information can be entangled across multiple qubits, allowing more efficient encoding."
  explanation: "For a depolarizing channel with high noise, classical capacity might be C ≈ 0.1 bits/use, but with shared entanglement, C_E ≈ 0.2 bits/use — entanglement doubles the classical capacity. This is possible because entanglement provides a resource (correlated states) that the sender and receiver can exploit. Quantum capacity C_Q quantifies how much quantum information (not just classical bits) can be reliably encoded and decoded, which requires more sophisticated protocols than classical communication."

- question: "In quantum key distribution (QKD), the eavesdropper is information-theoretically secure against even if they have unlimited computational power. What physical principle prevents the eavesdropper from learning the key without detection?"
  type: multiple-choice
  options:
    - "The computational complexity of certain mathematical problems (like factoring) makes eavesdropping difficult"
    - "The no-cloning theorem: the eavesdropper cannot copy the quantum states used to communicate the key, and attempting to measure them disturbs the states, introducing detectable errors"
    - "Classical encryption schemes are combined with quantum channels"
    - "The eavesdropper lacks the right quantum equipment"
  answer: 1
  explanation: "QKD (e.g., BB84 protocol) encodes the cryptographic key in quantum bits sent through a quantum channel. The legitimate parties (Alice and Bob) randomly choose bases to measure the qubits, and later publicly compare bases to establish a shared key. An eavesdropper (Eve) who tries to intercept the qubits faces a dilemma: to extract information, she must measure them, but measurement disturbs them (for non-commuting observables). The disturbance introduces errors that Alice and Bob detect via a statistical test. Since Eve cannot clone the qubits (no-cloning theorem), she cannot copy them and try multiple measurements. Either Eve learns nothing (measures in the wrong basis and causes a disturbance), or she risks detection. This is information-theoretically secure: it depends on quantum mechanics, not computational complexity."
```

## Explainer

Classical information theory, founded by Shannon, assumes information carriers are classical bits — 0 or 1, distinguishable and copyable. Quantum systems obey different rules: quantum bits (qubits) exist in superposition, cannot be copied without disturbance, and can be entangled in ways with no classical analog. Quantum information theory extends Shannon's framework to these quantum resources.

**Von Neumann Entropy and Quantum States**:
A quantum state is represented by a density matrix rho (a positive semidefinite matrix with trace 1). The von Neumann entropy is S(rho) = -sum_i lambda_i log_2(lambda_i), where lambda_i are the eigenvalues of rho. For a pure state |psi> (a single eigenvalue 1, rest 0), S = 0 — no uncertainty, complete information. For a maximally mixed state (all eigenvalues equal), S = log_2(d) where d is the dimension — maximum uncertainty. Quantum information parallels classical information: H(X) = -sum_i p_i log_2(p_i) for a classical random variable. The key difference: quantum superposition allows states with no classical counterpart.

**The No-Cloning Theorem**:
In classical computation, copying data is free and perfect. In quantum mechanics, Wiesner and Dieks independently proved that no operation can perfectly clone an arbitrary unknown quantum state. The proof uses unitarity and is elegant: if cloning worked for all states, it would create impossible correlations (orthogonal states would map to indistinguishable results). This prohibition is fundamental — not a technological limitation but a consequence of quantum mechanics. It has profound implications: an eavesdropper cannot clone intercepted quantum states to measure them without disturbing them, enabling secure key distribution.

**Quantum Channel Capacities**:
A quantum channel N transmits quantum states: rho -> N(rho). Three capacities characterize it:
1. **Classical Capacity C**: Maximum bits per channel use of classical information that can be reliably transmitted. Achieved by encoding classical bits into quantum states, sending through the channel, and measuring at the receiver. For many channels, computing C is an open problem.
2. **Quantum Capacity C_Q**: Maximum qubits per channel use. Requires transmitting and preserving quantum coherence. Can be positive even when C = 0 (superactivation: combining two zero-capacity channels can yield positive quantum capacity).
3. **Entanglement-Assisted Capacity C_E**: Classical capacity when sender and receiver share pre-distributed entanglement. Remarkably, C_E = 2*C for some channels (entanglement doubles classical capacity).

The gap between these capacities reveals quantum advantage: entanglement as a resource enables communication beyond classical limits.

**Quantum Key Distribution (QKD)**:
Quantum key distribution (e.g., BB84 by Bennett and Brassard, or E91 by Ekert) uses quantum states to distribute cryptographic keys with information-theoretic security. The basic idea: Alice sends qubits in random bases, Bob measures in random bases, they later compare bases publicly and keep the bits where they used the same basis. An eavesdropper (Eve) attempting to intercept the qubits must measure them to extract information. Measurement in a non-commuting basis disturbs the state, introducing errors Alice and Bob detect. Since Eve cannot clone the qubits, she cannot avoid this choice: either she learns nothing (wrong basis), or she risks detection. This is fundamentally different from computational security: the security comes from quantum mechanics, not hardness assumptions, making it resilient to future algorithmic breakthroughs (including quantum computers).

**Entanglement and Quantum Communication**:
Quantum entanglement — correlations between qubits that exceed classical limits — enables quantum advantages in communication. The **Bell states** are maximally entangled, and exploiting entanglement allows protocols like quantum teleportation (transmitting a quantum state using classical bits plus pre-shared entanglement) and dense coding (encoding two classical bits into one qubit via entanglement). These phenomena have no classical analogs.

Quantum information theory is a deep field bridging quantum mechanics, information theory, and cryptography. It has already enabled quantum key distribution systems deployed globally, and continues to shape quantum computing and communication. The theory reveals that information itself has a quantum nature, with profound implications for the limits and possibilities of communication, computation, and security.
