---
id: bernstein-vazirani-algorithm
title: Bernstein-Vazirani Algorithm
domain: computer-science
course: quantum-computing
prerequisites:
- id: deutsch-jozsa-algorithm
  type: hard
- id: quantum-circuits
  type: hard
tags:
- Bernstein-Vazirani
- oracle
- hidden-string
- quantum-query-complexity
stage: advanced
status: validated
---
# Bernstein-Vazirani Algorithm

## Core Idea
The Bernstein-Vazirani algorithm finds a hidden n-bit string s given an oracle for f(x) = s dot x (mod 2), where dot denotes the bitwise inner product. Classically, n queries are required (one for each standard basis vector). The quantum algorithm recovers s exactly in a single query using the same Hadamard-oracle-Hadamard structure as Deutsch-Jozsa. It demonstrates a linear-to-constant quantum speedup and illustrates the power of phase kickback for extracting global properties from a function oracle.

## Questions

```yaml
- question: "In the Bernstein-Vazirani algorithm, what is the output state of the input register after the Hadamard-oracle-Hadamard sequence, before measurement?"
  type: multiple-choice
  options: ["|0...0>", "|s> where s is the hidden string", "An equal superposition of all n-bit strings", "|s_perp> — the bitwise complement of s"]
  answer: 1
  explanation: "The final state is exactly |s>. After the first Hadamard, the input register is in a uniform superposition. The oracle applies phase (-1)^(s dot x) to each |x>. The final Hadamard transform converts this phase pattern into the basis state |s> with probability 1. This works because the Hadamard transform is its own inverse and the function f(x) = s dot x (mod 2) produces exactly the phase pattern that the Hadamard transform 'decodes' to |s>."

- question: "The Bernstein-Vazirani algorithm uses the same circuit structure as Deutsch-Jozsa: Hadamard, oracle, Hadamard."
  type: true-false
  answer: true
  explanation: "Both algorithms use the identical circuit skeleton: prepare |0>^n|1>, apply H to all qubits, query the oracle (which applies phase kickback via the ancilla in |->), apply H to the input register, and measure. The difference is in the oracle and what the measurement reveals. In Deutsch-Jozsa, you check if the output is |0...0>. In Bernstein-Vazirani, the output directly encodes the hidden string s."

- question: "Why does a classical algorithm need exactly n queries to find s, while the quantum algorithm needs only one?"
  type: short-answer
  answer: "Classically, each query f(x) returns one bit — the inner product s dot x mod 2. To recover all n bits of s, you need n linearly independent queries (the standard basis vectors e_1,...,e_n work, since f(e_i) = s_i). The quantum algorithm queries f on a superposition of all 2^n inputs simultaneously, and phase kickback encodes all n bits of s into the quantum state's phase pattern. The final Hadamard transform converts this global phase information into the computational basis state |s>, recovering all n bits at once."
  explanation: "This highlights a genuine quantum advantage: a single quantum query can extract n bits of information about a function through interference, while a single classical query yields only one bit. The mathematical reason is that the Hadamard transform is the discrete Fourier transform over Z_2^n, and the function f(x) = s dot x is a character of this group. The Fourier transform localizes the character to a single point — exactly the hidden string s."
```

## Explainer

The Bernstein-Vazirani problem is a natural extension of Deutsch-Jozsa that further illustrates how quantum algorithms extract information from oracles. You are given a black-box function f(x) = s dot x (mod 2), where s is an unknown n-bit string and dot is the bitwise inner product: s dot x = s_1*x_1 + s_2*x_2 + ... + s_n*x_n (mod 2). Your goal is to find s using as few oracle queries as possible.

Classically, each query returns a single bit of information. Querying f(e_i) — where e_i is the i-th standard basis vector with a 1 in position i and 0s elsewhere — returns s dot e_i = s_i, the i-th bit of s. So n queries suffice and are clearly necessary: each query reveals at most one linear constraint on s, and you need n independent constraints to determine n unknowns. No clever classical strategy can do better.

The quantum algorithm uses the same circuit as Deutsch-Jozsa. Initialize n input qubits to |0> and one ancilla to |1>, apply Hadamard to all, query the oracle, apply Hadamard to the input register, and measure. The oracle acts as |x>|-> -> (-1)^(f(x))|x>|-> = (-1)^(s dot x)|x>|->. After the first Hadamard, the input is (1/sqrt(2^n)) sum_x |x>. After the oracle, it becomes (1/sqrt(2^n)) sum_x (-1)^(s dot x) |x>. Applying Hadamard again performs the Fourier transform over Z_2^n, and because the phase pattern (-1)^(s dot x) is exactly a character of this group, the transform localizes it to the single basis state |s>. The measurement outcome is s with probability 1.

The Bernstein-Vazirani algorithm achieves a linear speedup (n queries classically vs. 1 quantumly) rather than the exponential speedup of Deutsch-Jozsa, but it demonstrates a cleaner and more practical pattern. The algorithm reveals how the Hadamard transform acts as a Fourier transform that "decodes" phase information into basis states. This Fourier-transform-based extraction of hidden structure — here a hidden linear function — is the same principle that powers the quantum Fourier transform and ultimately Shor's algorithm for factoring. Bernstein-Vazirani is the simplest case of the "hidden subgroup problem" framework that unifies many quantum algorithms.
