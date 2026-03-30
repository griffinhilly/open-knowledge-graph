---
id: simons-algorithm
title: Simon's Algorithm
domain: computer-science
course: quantum-computing
prerequisites:
- id: bernstein-vazirani-algorithm
  type: hard
- id: quantum-circuits
  type: hard
tags:
- Simon
- hidden-subgroup
- period-finding
- exponential-speedup
stage: advanced
status: validated
---
# Simon's Algorithm

## Core Idea
Simon's algorithm finds a hidden period string s for a function f:{0,1}^n -> {0,1}^n satisfying f(x) = f(y) if and only if x = y or x = y xor s. Classically, finding s requires O(2^(n/2)) queries (birthday bound). Simon's algorithm uses O(n) quantum queries, each producing a random vector orthogonal to s, and classical Gaussian elimination recovers s — achieving an exponential speedup. It was the first algorithm to prove an exponential quantum advantage over all classical algorithms (including probabilistic ones) and directly inspired Shor's factoring algorithm.

## Questions

```yaml
- question: "Each run of Simon's quantum subroutine produces a uniformly random string y satisfying y dot s = 0 (mod 2). How many runs are needed to determine s with high probability?"
  type: multiple-choice
  options: ["1 run", "n runs (to get n-1 linearly independent constraints plus confirmation)", "2^n runs", "sqrt(2^n) runs"]
  answer: 1
  explanation: "Each query produces a random y from the (n-1)-dimensional subspace orthogonal to s. After O(n) queries, you expect to have n-1 linearly independent vectors, which define s (up to the trivial solution 0) via Gaussian elimination. The probability of getting n-1 independent vectors in cn runs (for a small constant c > 1) is high. This is polynomially many queries — exponentially better than the classical O(2^(n/2))."

- question: "Simon's algorithm achieves its speedup by using quantum parallelism to evaluate f on all inputs simultaneously, then directly reading off the period s."
  type: true-false
  answer: false
  explanation: "Quantum parallelism evaluates f on all inputs in superposition, but measurement does not directly reveal s. Instead, measuring the output register collapses the input register to a uniform superposition of two values x and x xor s. Applying Hadamard to the input register and measuring produces a random y with y dot s = 0. The period is recovered indirectly by collecting enough such constraints and solving a linear system classically. The quantum speedup comes from generating these constraints efficiently, not from reading the answer directly."

- question: "Why was Simon's algorithm historically significant for the development of quantum computing, beyond the specific problem it solves?"
  type: short-answer
  answer: "Simon's algorithm was the first to prove an exponential quantum speedup over all classical algorithms, including probabilistic ones — not just deterministic ones as in Deutsch-Jozsa. More importantly, it directly inspired Shor's factoring algorithm. Shor adapted Simon's approach of using quantum Fourier sampling to find hidden periodicity, replacing the Z_2^n group structure with modular arithmetic and the quantum Fourier transform over Z_N."
  explanation: "Simon's problem is a 'hidden subgroup problem' over the group Z_2^n. Shor's factoring algorithm is conceptually the same pattern applied to the cyclic group Z_N: use quantum parallelism to create a periodic superposition, then use a Fourier transform to extract the period. Simon's algorithm showed that this general strategy could yield exponential speedups, which motivated the search for analogous algorithms over other groups."
```

## Explainer

Simon's problem is the bridge between the toy oracle problems (Deutsch-Jozsa, Bernstein-Vazirani) and the practically significant quantum algorithms (Shor). You are given a black-box function f:{0,1}^n -> {0,1}^n with the promise that there exists a secret string s such that f(x) = f(y) if and only if x = y or x = y xor s. If s = 0...0, the function is one-to-one; otherwise, it is two-to-one with period s. Your task is to find s.

Classically, this is essentially a collision-finding problem. By the birthday paradox, you need O(2^(n/2)) queries before you expect to find a collision f(x) = f(y) with x != y, from which s = x xor y. No classical algorithm — deterministic or randomized — can do substantially better. Simon's quantum algorithm uses only O(n) queries and O(n^2) total time (including classical post-processing), achieving an exponential speedup.

The quantum subroutine works as follows. Prepare two n-qubit registers, both initialized to |0>^n. Apply Hadamard to the first register to create a uniform superposition. Apply the oracle to compute f into the second register, producing the state (1/sqrt(2^n)) sum_x |x>|f(x)>. Now measure the second register, obtaining some value f(x_0). The first register collapses to (|x_0> + |x_0 xor s>)/sqrt(2) — a superposition of the two preimages. Apply Hadamard to the first register and measure, obtaining a random n-bit string y. The key constraint is that y dot s = 0 (mod 2): only strings orthogonal to s have nonzero amplitude after the Hadamard transform, because the two terms |x_0> and |x_0 xor s> interfere constructively only for such y.

Each run yields one random equation y dot s = 0 (mod 2). After O(n) runs, you have a system of linear equations over GF(2) that you solve by Gaussian elimination. With high probability, n-1 of these equations are linearly independent, uniquely determining s (the only nontrivial element of the null space of the constraint matrix). The total cost is O(n) quantum oracle queries plus O(n^3) classical computation for Gaussian elimination — exponentially better than the classical 2^(n/2). Simon's algorithm established the template of quantum Fourier sampling that Shor later adapted: create a periodic quantum state, apply a Fourier transform to extract the period, and use classical post-processing to recover the answer.
