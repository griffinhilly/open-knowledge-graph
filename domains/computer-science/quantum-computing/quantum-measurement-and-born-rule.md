---
id: quantum-measurement-and-born-rule
title: Quantum Measurement and the Born Rule
domain: computer-science
course: quantum-computing
prerequisites:
- id: qubits-and-quantum-states
  type: hard
- id: born-rule-and-measurement
  type: hard
- id: quantum-gates
  type: soft
tags:
- measurement
- Born-rule
- projective-measurement
- computational-basis
- POVM
stage: advanced
status: validated
---
# Quantum Measurement and the Born Rule

## Core Idea
Measurement in quantum computing extracts classical information from a quantum state, collapsing it probabilistically according to the Born rule: measuring a qubit in state alpha|0> + beta|1> yields outcome 0 with probability |alpha|^2 and outcome 1 with probability |beta|^2, with the post-measurement state being the corresponding basis state. Measurements can be performed in any orthonormal basis by applying a change-of-basis gate before measuring in the computational basis. Understanding measurement is essential because it is the only way to extract results from a quantum computation, and its probabilistic, destructive nature is the central constraint that quantum algorithm design must navigate.

## Questions

```yaml
- question: "A qubit is in state (|0> - |1>)/sqrt(2). What is the probability of measuring 0 in the computational basis?"
  type: multiple-choice
  options: ["0", "1/4", "1/2", "1"]
  answer: 2
  explanation: "The amplitude of |0> is 1/sqrt(2), so the probability of measuring 0 is |1/sqrt(2)|^2 = 1/2. The minus sign on the |1> amplitude is a phase — it affects interference in subsequent gates but does not change |amplitude|^2. Both (|0> + |1>)/sqrt(2) and (|0> - |1>)/sqrt(2) give 50/50 outcomes in the computational basis, even though they are physically distinct states."

- question: "After measuring a qubit and obtaining outcome |1>, the qubit is in state |1> regardless of what its pre-measurement state was."
  type: true-false
  answer: true
  explanation: "This is the projection postulate (state collapse). Upon obtaining outcome 1, the qubit's state is projected onto |1> and renormalized. All information about the original superposition is irreversibly lost. The qubit is now deterministically in |1>, and any subsequent measurement in the same basis will yield 1 with certainty."

- question: "You have a qubit in state |+> = (|0> + |1>)/sqrt(2) and want to distinguish it from |-> = (|0> - |1>)/sqrt(2) with certainty. How can you do this?"
  type: short-answer
  answer: "Apply a Hadamard gate before measuring in the computational basis. H maps |+> to |0> and |-> to |1>, so the computational basis measurement after H perfectly distinguishes the two states. Measuring directly in the computational basis gives 50/50 for both states and cannot distinguish them."
  explanation: "This illustrates that the choice of measurement basis matters. The states |+> and |-> are orthogonal in the X basis (Hadamard basis) but have identical computational-basis measurement statistics. By applying H — which is a change-of-basis transformation — you rotate the measurement axis to align with the states you want to distinguish. In general, to distinguish two orthogonal states, you must measure in a basis that includes them."

- question: "Can you determine the full quantum state alpha|0> + beta|1> of a single qubit by performing measurements on it?"
  type: multiple-choice
  options: ["Yes — measure in three different bases to reconstruct alpha and beta", "Yes — a single measurement in the computational basis reveals the state", "No — measurement is probabilistic and collapses the state, so a single copy provides at most one bit of information", "No — quantum states are fundamentally unknowable"]
  answer: 2
  explanation: "A single measurement yields one classical bit (0 or 1) and destroys the state. You cannot determine alpha and beta from this. However, if you have many identical copies of the state, you can estimate the probabilities by repeated measurement, and by measuring in multiple bases (X, Y, Z), you can perform quantum state tomography to reconstruct the full state. The key constraint is that a single copy cannot be fully characterized — this is related to the no-cloning theorem."
```

## Explainer

From your study of the Born rule in quantum mechanics, you know that measurement outcomes are probabilistic and that measurement disturbs the system. In quantum computing, these facts become engineering constraints. A quantum computer performs a unitary computation on qubits, then measures some or all of them to extract a classical answer. The Born rule dictates the probability of each answer, and the post-measurement state is the projected (collapsed) state. The entire challenge of quantum algorithm design is arranging the unitary computation so that the desired answer has high measurement probability.

**Projective measurement** in the computational basis is the standard operation. For a single qubit in state alpha|0> + beta|1>, the measurement yields 0 with probability |alpha|^2 and 1 with probability |beta|^2. Afterward, the qubit is in the corresponding basis state — the superposition is gone. For multi-qubit systems, measuring one qubit collapses it and updates the remaining qubits' joint state accordingly. If two qubits are in the Bell state (|00> + |11>)/sqrt(2) and you measure the first qubit, getting 0 collapses the joint state to |00> and getting 1 collapses it to |11> — the second qubit's state is now determined.

You are not restricted to measuring in the computational basis. To measure in the X basis ({|+>, |->}), apply a Hadamard gate first, then measure in the computational basis. To measure in an arbitrary basis, apply the appropriate unitary rotation first. This is equivalent to measuring with projection operators onto the desired basis states. The choice of measurement basis is a powerful tool: the states |+> and |-> are indistinguishable in a Z-basis measurement (both give 50/50) but perfectly distinguishable in an X-basis measurement. Many quantum protocols, including BB84 key distribution, exploit exactly this basis-dependent distinguishability.

A fundamental limitation is that measurement provides at most one classical bit per qubit, and it is destructive. You cannot "peek" at a quantum state without disturbing it, and a single copy of an unknown state cannot be fully characterized. This connects to the **no-cloning theorem**: if you could copy an unknown quantum state, you could make many copies and measure each in a different basis to reconstruct the state, but cloning is forbidden. Quantum algorithms must therefore be designed to concentrate the answer into a high-probability measurement outcome, often by exploiting interference across many computational paths. The probabilistic nature of measurement also means many quantum algorithms are inherently probabilistic — they succeed with high probability but may need to be repeated a few times to boost confidence.
