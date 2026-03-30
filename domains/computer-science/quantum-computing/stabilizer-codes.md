---
id: stabilizer-codes
title: Stabilizer Codes
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-error-correction-basics
  type: hard
- id: quantum-gates
  type: hard
tags:
- stabilizer
- Pauli-group
- CSS-codes
- code-space
- syndrome
stage: expert
status: validated
---
# Stabilizer Codes

## Core Idea
Stabilizer codes are the dominant framework for quantum error correction, defining the code space as the simultaneous +1 eigenspace of an abelian subgroup of the n-qubit Pauli group (the stabilizer group). An [[n,k,d]] stabilizer code encodes k logical qubits into n physical qubits with minimum distance d, correcting up to floor((d-1)/2) errors. Syndrome measurement amounts to measuring each stabilizer generator, identifying which Pauli error occurred without disturbing the encoded state. CSS codes, a major subclass, separately correct bit-flip (X) and phase-flip (Z) errors using classical linear codes, connecting quantum error correction directly to classical coding theory.

## Questions

```yaml
- question: "In an [[n,k,d]] stabilizer code, the stabilizer group S has n-k independent generators. What do the remaining k degrees of freedom correspond to?"
  type: multiple-choice
  options: ["k physical qubits that are not used for error correction", "k logical qubits whose information is encoded in the code space", "k possible error syndromes", "k ancilla qubits needed for syndrome measurement"]
  answer: 1
  explanation: "The n-k stabilizer generators constrain the state to lie in a 2^k-dimensional code subspace of the 2^n-dimensional Hilbert space. This 2^k-dimensional space encodes k logical qubits. The logical operators (logical X and Z for each logical qubit) commute with all stabilizers but are not themselves in the stabilizer group — they act within the code space to manipulate the encoded information."

- question: "If two different errors E1 and E2 produce the same syndrome, the stabilizer code cannot distinguish them and error correction fails."
  type: true-false
  answer: false
  explanation: "Two errors with the same syndrome differ by an element of the stabilizer group: E1*E2^dagger is in the stabilizer (or is proportional to a logical operator). If E1*E2^dagger is in the stabilizer, both errors have the same effect on the code space, so correcting either one corrects both — no failure occurs. Error correction fails only when E1*E2^dagger is a nontrivial logical operator, meaning the two errors differ by an undetectable logical operation. This is why the minimum distance d matters: it determines the weight of the lightest undetectable error."

- question: "How do CSS codes simplify the construction of quantum error-correcting codes?"
  type: short-answer
  answer: "CSS (Calderbank-Shor-Steane) codes are built from two classical linear codes C1 and C2 with C2 subset of C1. X errors are corrected using C1 and Z errors are corrected using C2^perp, with the two correction procedures operating independently. This means you can design the quantum code by choosing classical codes with the right properties, leveraging decades of classical coding theory rather than designing quantum codes from scratch."
  explanation: "The separation of X and Z error correction in CSS codes is powerful because it reduces quantum code design to classical code design. The Steane code ([[7,1,3]]) is a CSS code built from the classical Hamming [7,4,3] code. The constraint that C2 is contained in C1 ensures that X and Z corrections do not interfere with each other. CSS codes are also the foundation for surface codes, the leading candidates for practical quantum error correction."
```

## Explainer

Stabilizer codes provide a unified mathematical framework for nearly all known quantum error-correcting codes. The framework is built on the **n-qubit Pauli group** — the group of all n-fold tensor products of {I, X, Y, Z} with phases {+1, -1, +i, -i}. A stabilizer code is defined by an abelian subgroup S of this group (the **stabilizer**) such that -I is not in S. The code space is the simultaneous +1 eigenspace of all elements of S: the set of states |psi> satisfying g|psi> = |psi> for every g in S.

The stabilizer group S is specified by n-k independent generators g_1, ..., g_{n-k}, where n is the number of physical qubits and k is the number of encoded logical qubits. The code space has dimension 2^k. **Syndrome measurement** measures each generator and records whether the eigenvalue is +1 or -1, producing an (n-k)-bit string called the syndrome. An error E from the Pauli group either commutes or anticommutes with each generator: if Eg_i = g_iE, the i-th syndrome bit is 0; if Eg_i = -g_iE, it is 1. Different errors produce different syndromes (up to elements of the stabilizer), allowing the decoder to identify and correct the error.

**CSS codes** are a major subclass constructed from two classical linear codes C1 and C2 satisfying C2 subset of C1. The X-type stabilizers are derived from C2^perp and correct Z errors; the Z-type stabilizers are derived from C1 and correct X errors. The beautiful feature is that X and Z error correction decouple completely, reducing the quantum code design problem to choosing two classical codes with appropriate containment. The Steane [[7,1,3]] code uses C1 = C2 = the Hamming [7,4,3] code; the code corrects any single-qubit error.

The minimum distance d of the code is the weight of the lightest Pauli operator that commutes with all stabilizers but is not itself in the stabilizer group — that is, the lightest nontrivial logical operator. A code with distance d can detect any error of weight up to d-1 and correct any error of weight up to floor((d-1)/2). The notation [[n,k,d]] compactly describes a code's parameters. The stabilizer framework also provides tools for analyzing code properties, constructing fault-tolerant gates (Clifford gates preserve the Pauli group and are naturally transversal for many stabilizer codes), and understanding the information-theoretic limits of quantum error correction. Virtually all practical QEC proposals — from Steane and Shor codes to surface codes and color codes — are stabilizer codes.
