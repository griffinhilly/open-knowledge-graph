---
id: shors-algorithm
title: Shor's Algorithm
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-fourier-transform
  type: hard
- id: simons-algorithm
  type: hard
- id: quantum-circuits
  type: hard
- id: complexity-class-p-definition
  type: soft
- id: cook-levin-theorem
  type: soft
tags:
- Shor
- factoring
- period-finding
- RSA
- cryptography
stage: expert
status: validated
---
# Shor's Algorithm

## Core Idea
Shor's algorithm factors an n-bit integer in polynomial time O(n^3) on a quantum computer, compared to the best known classical algorithms which are sub-exponential. It works by reducing factoring to period finding: given N to factor, choose a random a coprime to N and find the period r of the function f(x) = a^x mod N using the quantum Fourier transform. From the period, factors of N can be extracted with high probability using classical number theory. Shor's algorithm threatens RSA and other cryptosystems whose security relies on the assumed classical hardness of factoring.

## Questions

```yaml
- question: "Shor's algorithm reduces integer factoring to which mathematical problem that a quantum computer can solve efficiently?"
  type: multiple-choice
  options: ["Discrete logarithm over finite fields", "Finding the period of modular exponentiation f(x) = a^x mod N", "Computing the greatest common divisor of two numbers", "Solving systems of linear equations modulo N"]
  answer: 1
  explanation: "The key insight is that factoring can be reduced to order finding (period finding): the period r of f(x) = a^x mod N gives a^r = 1 (mod N), from which gcd(a^(r/2) +/- 1, N) often yields a nontrivial factor. The quantum part efficiently finds r using the quantum Fourier transform applied to the periodic state created by modular exponentiation. GCD computation is classical and already efficient (Euclidean algorithm); the hard part that requires a quantum computer is finding r."

- question: "Shor's algorithm always succeeds in factoring N on the first attempt."
  type: true-false
  answer: false
  explanation: "The algorithm is probabilistic. Several things can go wrong: the random a might share a factor with N (easy case, but rare), the period r might be odd, or a^(r/2) might equal -1 (mod N). In these cases, the attempt fails and you retry with a different random a. Each attempt has at least a constant probability of success, so O(1) repetitions suffice to factor N with high probability. The quantum subroutine (period finding) also has a small failure probability from the QFT measurement."

- question: "Explain why the quantum Fourier transform is essential to Shor's algorithm. What does the state look like before and after the QFT, and how does the measurement outcome reveal the period?"
  type: short-answer
  answer: "After modular exponentiation, the first register is in a periodic superposition with period r (states at x_0, x_0+r, x_0+2r, ...). The QFT converts this periodic state into one with amplitude peaks at multiples of 2^n/r. Measuring gives a random value close to some multiple c * 2^n/r. From the ratio c/2^n, the continued fraction algorithm extracts r. Without the QFT, the periodic structure would be hidden in the amplitudes and inaccessible through direct measurement."
  explanation: "The QFT is performing Fourier analysis of the periodic quantum state. Just as the classical Fourier transform of a periodic signal has peaks at the signal's frequency, the QFT maps a state periodic in the computational basis to one with peaks in the Fourier basis. The measurement samples from these peaks, and classical post-processing (continued fractions) recovers the frequency — which is the period r. This is the same pattern as Simon's algorithm but over the cyclic group Z_N rather than Z_2^n."
```

## Explainer

Shor's algorithm is the most consequential quantum algorithm known, because it breaks the RSA cryptosystem whose security assumption is that factoring large integers is computationally hard. The algorithm runs in polynomial time on a quantum computer, while the best known classical algorithms for factoring (the general number field sieve) run in sub-exponential time exp(O(n^(1/3) * (log n)^(2/3))). If a sufficiently large quantum computer is built, RSA, Diffie-Hellman, and elliptic curve cryptography all become insecure.

The algorithm has a classical reduction and a quantum subroutine. The **classical reduction** uses number theory: to factor N, pick a random a < N with gcd(a, N) = 1. Find the **order** r of a modulo N — the smallest positive integer r such that a^r = 1 (mod N). If r is even and a^(r/2) != -1 (mod N), then gcd(a^(r/2) - 1, N) and gcd(a^(r/2) + 1, N) are nontrivial factors of N. This reduction works with probability at least 1/2 over the random choice of a. The hard step — finding r — is where the quantum computer comes in.

The **quantum subroutine** creates the state (1/sqrt(2^n)) sum_{x=0}^{2^n - 1} |x>|a^x mod N> using controlled modular exponentiation, then applies the quantum Fourier transform to the first register. Before the QFT, the first register (conditioned on the second register's measurement) is a periodic superposition with period r. After the QFT, the amplitude is concentrated at values near multiples of 2^n/r. Measuring gives a value c approximately equal to j * 2^n/r for some random integer j. From the fraction c/2^n, the **continued fraction algorithm** extracts r (as the denominator of the best rational approximation with small denominator).

The resource cost is substantial but polynomial. The circuit requires O(n) qubits (where n = log N), and the modular exponentiation uses O(n^3) gates (the most expensive part). The QFT itself costs only O(n^2) gates. The total time is O(n^3) quantum gates plus O(n^3) classical post-processing. Current quantum hardware is far from factoring cryptographically relevant numbers (2048-bit RSA requires thousands of logical qubits, which in turn require millions of physical qubits with error correction). Shor's algorithm has been demonstrated on small numbers (factoring 15, 21) as proof-of-concept experiments. The practical threat timeline depends on advances in quantum hardware and error correction, but the theoretical result has already motivated the development of post-quantum cryptography — lattice-based and other schemes believed to be hard even for quantum computers.
