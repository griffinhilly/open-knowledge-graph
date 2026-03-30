---
id: quantum-phase-estimation
title: Quantum Phase Estimation
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-fourier-transform
  type: hard
- id: quantum-circuits
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
tags:
- phase-estimation
- QPE
- eigenvalue
- quantum-subroutine
stage: expert
status: validated
---
# Quantum Phase Estimation

## Core Idea
Quantum phase estimation (QPE) estimates the eigenvalue phase of a unitary operator: given a unitary U and an eigenstate |u> with U|u> = e^(2*pi*i*phi)|u>, QPE outputs an n-bit approximation of phi using O(n) controlled applications of U and an inverse QFT. It is the core subroutine of Shor's algorithm, the HHL algorithm for linear systems, quantum chemistry simulations, and many other quantum algorithms. QPE converts the inaccessible phase information stored in a unitary's eigenvalue into a measurable computational-basis state.

## Questions

```yaml
- question: "QPE uses a register of n ancilla qubits initialized in superposition, each controlling a different power of U (U^1, U^2, U^4, ..., U^(2^(n-1))). Why are powers of 2 used?"
  type: multiple-choice
  options: ["Powers of 2 are computationally cheaper than other powers", "The binary encoding means the j-th qubit picks up phase 2^j * phi, which the inverse QFT decodes into the binary representation of phi", "Only powers of 2 are implementable on quantum hardware", "The algorithm works with any powers; powers of 2 are an arbitrary convention"]
  answer: 1
  explanation: "The j-th control qubit, when in state |1>, applies U^(2^j), which maps |u> to e^(2*pi*i*2^j*phi)|u>. This means the j-th qubit acquires phase 2^j * phi — exactly the j-th bit's contribution to the binary expansion of phi. The inverse QFT then converts these phases into the binary representation of phi in the ancilla register. The powers of 2 are structurally necessary for the QFT to decode the phase into a bit string."

- question: "If phi is not exactly representable in n bits, QPE still outputs the correct value with probability 1."
  type: true-false
  answer: false
  explanation: "When phi is not an exact n-bit fraction, the inverse QFT produces a probability distribution peaked near the closest n-bit approximation of phi, but there is nonzero probability of getting neighboring values. The probability of getting the best n-bit approximation is at least 4/pi^2 ≈ 0.405. Using a few extra qubits and rounding, you can boost the success probability to 1 - epsilon for any desired epsilon."

- question: "Explain how QPE connects to Shor's algorithm — specifically, what is the unitary U and what is the eigenvalue phase phi in the factoring context?"
  type: short-answer
  answer: "In Shor's algorithm, U is the modular multiplication operator U|x> = |ax mod N>, and the eigenvalue phases are phi_s = s/r, where r is the order of a modulo N and s ranges from 0 to r-1. QPE estimates phi_s, giving a fraction close to s/r, from which r is extracted via the continued fraction algorithm. The period-finding step of Shor's algorithm is exactly a QPE applied to the modular exponentiation unitary."
  explanation: "The eigenstates of U|x> = |ax mod N> are |u_s> = (1/sqrt(r)) sum_{k=0}^{r-1} e^(-2*pi*i*s*k/r) |a^k mod N>, with eigenvalues e^(2*pi*i*s/r). QPE applied to U with input |1> (which is a superposition of the |u_s> states) yields a random s/r, from which r is recovered. This reframing of Shor's algorithm through QPE clarifies that factoring is fundamentally an eigenvalue estimation problem."
```

## Explainer

Quantum phase estimation solves a fundamental problem: given a unitary operator U and an eigenstate |u> satisfying U|u> = e^(2*pi*i*phi)|u>, determine phi. The phase phi is encoded in the complex eigenvalue of U, which cannot be directly observed through measurement of |u> (measuring |u> gives |u> with certainty, revealing nothing about phi). QPE extracts phi by converting it into a computational-basis measurement outcome using controlled unitaries and the inverse QFT.

The circuit uses two registers: an **ancilla register** of n qubits (determining the precision of the estimate) and a **target register** holding |u>. The ancilla qubits are initialized to |+> = H|0>, and each controls a different power of U applied to the target. Specifically, the j-th ancilla qubit (j = 0, 1, ..., n-1) controls U^(2^j). Because |u> is an eigenstate, U^(2^j)|u> = e^(2*pi*i * 2^j * phi)|u>, so the controlled operation applies a phase of 2^j * phi to the j-th qubit's |1> component. After all controlled unitaries, the ancilla register is in the state (1/sqrt(2^n)) sum_{k=0}^{2^n-1} e^(2*pi*i*k*phi) |k> — exactly the QFT of the state |round(2^n * phi)>.

Applying the **inverse QFT** to the ancilla register transforms it to a state peaked at |round(2^n * phi)>. If phi is exactly an n-bit binary fraction, the inverse QFT produces the exact binary representation with probability 1. If phi has more than n bits of precision, the result is a distribution peaked at the nearest n-bit approximation, with success probability at least 4/pi^2 ≈ 0.405 for the closest value. Adding a few extra ancilla qubits increases precision and success probability arbitrarily.

QPE is the engine inside many quantum algorithms. In **Shor's algorithm**, QPE is applied to the modular multiplication operator to extract the order (period) of modular exponentiation. In **quantum chemistry**, QPE applied to the time evolution operator e^(-iHt) of a molecular Hamiltonian estimates the ground-state energy. In the **HHL algorithm** for linear systems, QPE estimates eigenvalues of a matrix to enable matrix inversion. The pattern is always the same: encode a problem's answer as the phase of a unitary, then use QPE to read it out. This makes QPE perhaps the most important primitive in the quantum algorithm designer's toolkit — a universal phase-to-measurement converter.
