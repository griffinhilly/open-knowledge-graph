---
id: quantum-fourier-transform
title: Quantum Fourier Transform
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-circuits
  type: hard
- id: quantum-gates
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
tags:
- QFT
- Fourier-transform
- phase-estimation
- period-finding
stage: advanced
status: validated
---
# Quantum Fourier Transform

## Core Idea
The quantum Fourier transform (QFT) maps a computational basis state |j> of an n-qubit register to (1/sqrt(2^n)) * sum_{k=0}^{2^n - 1} e^(2*pi*i*j*k/2^n) |k> — the discrete Fourier transform of the basis state amplitudes. It can be implemented with O(n^2) gates using a circuit of Hadamard gates and controlled phase rotations, compared to the O(n * 2^n) operations of the classical FFT. The QFT does not compute the Fourier transform of classical data efficiently (reading out the result requires measurement), but it is the key subroutine in quantum phase estimation, Shor's algorithm, and many other quantum algorithms that extract periodic structure.

## Questions

```yaml
- question: "The QFT on n qubits uses O(n^2) gates. The classical FFT uses O(n * 2^n) operations. Does this mean the QFT provides an exponential speedup for computing Fourier transforms?"
  type: multiple-choice
  options: ["Yes — the QFT is always exponentially faster than the classical FFT", "No — the QFT transforms quantum amplitudes, which cannot be directly read out; the speedup applies only when the QFT is used as a subroutine within a larger quantum algorithm", "Yes — but only for real-valued input data, not complex", "No — the QFT and FFT compute different transforms"]
  answer: 1
  explanation: "The QFT operates on the amplitudes of a quantum state, not on classical data. You cannot efficiently load arbitrary classical data into quantum amplitudes (the 'state preparation' problem), and you cannot read out all amplitudes after the QFT (measurement collapses to one basis state). The QFT's power lies in being a subroutine: when the input state naturally arises from a quantum computation (as in phase estimation or Shor's algorithm), the QFT efficiently extracts period or phase information that can then be measured."

- question: "The QFT circuit for 3 qubits consists of only Hadamard gates — no controlled rotations are needed for small registers."
  type: true-false
  answer: false
  explanation: "Even for 3 qubits, the QFT circuit requires Hadamard gates and controlled phase rotation gates. The circuit applies H to the first qubit, then controlled-R2 and controlled-R3 (where Rk applies a phase of e^(2*pi*i/2^k)), then H to the second qubit, then controlled-R2 from the third qubit, then H to the third qubit, plus SWAP gates to reverse the bit order. Only for 1 qubit is the QFT a single Hadamard."

- question: "Why is the QFT useful for finding the period of a function, even though measuring the QFT output gives only one random value?"
  type: short-answer
  answer: "When applied to a periodic state with period r, the QFT concentrates amplitude on multiples of 2^n/r — the peaks of the Fourier transform of a periodic function. Measuring gives a random multiple of approximately 2^n/r. From this, the period r can be extracted via continued fractions. Multiple measurements (O(1) repetitions) provide enough information to determine r with high probability."
  explanation: "The QFT converts periodicity in the computational basis into sharp peaks in the Fourier basis. A state with period r has nonzero amplitudes only at positions that are multiples of r; after the QFT, these become peaks at multiples of 2^n/r. This is the discrete version of the fact that the Fourier transform of a periodic signal has peaks at the signal's frequency. Shor's algorithm exploits exactly this: it creates a periodic state via modular exponentiation, applies the QFT, and reads off the period."
```

## Explainer

The classical discrete Fourier transform (DFT) converts a vector of N complex numbers into its frequency-domain representation. It is computable in O(N log N) time via the FFT algorithm. The quantum Fourier transform performs the same mathematical operation on quantum amplitudes — but because the amplitudes are encoded in an n-qubit state where N = 2^n, the operation takes only O(n^2) gates, which is O((log N)^2) in terms of the input size N. This exponential reduction in gate count is real, but its utility is constrained by the quantum context.

The **QFT circuit** has an elegant recursive structure. For n qubits, apply a Hadamard gate to the first qubit, then apply controlled phase rotations from each subsequent qubit (controlled-R_2 from the second qubit, controlled-R_3 from the third, and so on, where R_k applies a phase of e^(2*pi*i/2^k) to the |1> state). Then recursively apply the QFT to the remaining n-1 qubits. Finally, reverse the bit order with SWAP gates. The total gate count is n Hadamard gates plus n(n-1)/2 controlled rotations plus n/2 SWAPs, giving O(n^2) gates. In practice, rotations with very small angles (large k) can be dropped with negligible error, reducing the effective gate count further.

The QFT is not useful for "computing Fourier transforms of classical data on a quantum computer" — loading classical data into amplitudes is itself a hard problem (exponential cost in general), and measuring the output collapses it to a single basis state, losing most of the transform. The QFT is powerful when the input state arises naturally from a quantum computation. The canonical example is **period finding**: if a quantum state has a periodic structure with period r (nonzero amplitude only at positions 0, r, 2r, ...), the QFT maps this to a state with peaks at multiples of N/r. Measuring yields a random multiple of approximately N/r, from which r can be extracted using continued fraction expansion.

This is precisely how Shor's algorithm works: it constructs a periodic state via modular exponentiation, applies the QFT, and extracts the period. Quantum phase estimation follows the same pattern — it uses the QFT to convert a phase encoded in a unitary's eigenvalue into a computational basis measurement. The QFT is the Fourier analysis engine at the heart of most "algebraic" quantum algorithms (as opposed to "search" algorithms like Grover's). Understanding the QFT is understanding the core mechanism by which quantum computers extract hidden periodic structure exponentially faster than classical machines.
