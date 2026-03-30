---
id: bqp-and-quantum-complexity
title: BQP and Quantum Complexity Classes
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-circuits
  type: hard
- id: complexity-class-p-definition
  type: hard
- id: complexity-class-np-definition
  type: hard
- id: bpp-complexity-class
  type: soft
tags:
- BQP
- complexity-class
- quantum-complexity
- P-vs-NP
- QMA
stage: expert
status: validated
---
# BQP and Quantum Complexity Classes

## Core Idea
BQP (Bounded-Error Quantum Polynomial Time) is the class of decision problems solvable by a polynomial-time quantum computer with error probability at most 1/3. It is the quantum analog of BPP. The known containments are P subset of BPP subset of BQP subset of PSPACE, and BQP is believed to be strictly between BPP and PSPACE. Factoring is in BQP but not known to be in BPP, providing evidence that BQP is strictly larger than BPP. BQP is believed not to contain NP-complete problems, implying quantum computers are not expected to solve all of NP efficiently. QMA (Quantum Merlin Arthur) is the quantum analog of NP/MA, with a quantum proof verified by a quantum computer.

## Questions

```yaml
- question: "Which of the following best describes the relationship between BQP and NP?"
  type: multiple-choice
  options: ["BQP contains NP — quantum computers can solve all NP problems efficiently", "NP contains BQP — every quantum polynomial-time problem is also in NP", "BQP and NP are believed to be incomparable — neither contains the other", "BQP equals NP — they are the same class"]
  answer: 2
  explanation: "BQP and NP are believed to be incomparable. BQP contains problems (like factoring and simulating quantum systems) that are not known to be in NP. NP contains NP-complete problems (like SAT) that Grover's algorithm can speed up only quadratically, not enough for polynomial time. There is no proof of separation — just strong evidence from the structure of known algorithms. The oracle separation results support incomparability."

- question: "BQP is contained in PSPACE because a classical computer with polynomial space can simulate any polynomial-time quantum computation."
  type: true-false
  answer: true
  explanation: "A quantum circuit on n qubits has a state vector of 2^n amplitudes, each requiring polynomial bits of precision. A classical computer can simulate the entire computation by tracking this state vector, using exponential time but only polynomial space (process one amplitude at a time, or use the Feynman path integral approach). Since PSPACE allows exponential time with polynomial space, BQP is in PSPACE. This does not make quantum computers useless — the time savings can be exponential, even if the space requirements are the same."

- question: "What is QMA, and how does it relate to NP? Give an example of a QMA-complete problem."
  type: short-answer
  answer: "QMA (Quantum Merlin Arthur) is the class of problems where a quantum verifier can check a quantum proof (witness state) in polynomial time. It is the quantum analog of NP (or more precisely, MA). NP is contained in QMA because a classical proof can be encoded as a quantum state. The Local Hamiltonian problem is QMA-complete: given a sum of local Hamiltonians, determine whether the ground-state energy is below a threshold. This is the quantum analog of the Cook-Levin theorem — it was proved by Kitaev."
  explanation: "QMA generalizes NP in two ways: the proof can be a quantum state (exponentially hard to describe classically), and the verifier is a quantum computer. The Local Hamiltonian problem being QMA-complete means it is the hardest problem in QMA — if you could solve it efficiently, you could solve all QMA problems. The connection to physics is direct: determining the ground-state energy of a quantum system is computationally hard even for quantum computers (QMA-hard), which is why quantum chemistry simulation requires clever algorithms rather than brute force."
```

## Explainer

Complexity theory classifies problems by the resources needed to solve them. Classical complexity has P (deterministic polynomial time), BPP (randomized polynomial time), NP (nondeterministic polynomial time), and PSPACE (polynomial space). Quantum computing introduces BQP — the problems solvable by a quantum computer in polynomial time with bounded error. Understanding where BQP sits relative to classical classes reveals what quantum computers can and cannot do.

The formal definition: a language L is in BQP if there exists a polynomial-time uniform family of quantum circuits {C_n} such that for every input x of length n, C_n accepts x with probability at least 2/3 if x is in L, and rejects with probability at least 2/3 if x is not in L. The 2/3 threshold is arbitrary (as with BPP) — any constant bounded away from 1/2 works, because repeated execution and majority voting amplify the success probability exponentially.

The known containments are **P subset of BPP subset of BQP subset of PSPACE**. P in BPP is obvious (deterministic is a special case of randomized). BPP in BQP follows because a quantum computer can simulate any classical randomized computation. BQP in PSPACE is because a classical computer can simulate quantum computation using polynomial space (track the 2^n-dimensional state vector one amplitude at a time). The key question is **where BQP sits strictly**: is BQP larger than BPP? Is it smaller than PSPACE?

Evidence that **BQP is strictly larger than BPP** comes from Shor's algorithm: factoring is in BQP but not known to be in BPP (and the best classical algorithms are sub-exponential). Evidence that **BQP does not contain NP** comes from Grover's lower bound: unstructured search (the essence of NP-hard problems) gets only a quadratic speedup, not enough for polynomial time. If BQP contained NP, then NP would be in PSPACE, which is believed true, but it would also mean NP-complete problems have polynomial quantum algorithms — contradicting the structural evidence. The current consensus is that BQP and NP are **incomparable**: BQP contains problems outside NP (like quantum simulation), and NP contains problems outside BQP (like NP-complete satisfiability).

**QMA** extends this landscape to quantum verification. A QMA problem has a quantum prover who sends a polynomial-size quantum state as proof, and a quantum verifier who checks it in polynomial time. Kitaev proved that the **Local Hamiltonian problem** (determining whether a many-body quantum system's ground-state energy is below a threshold) is QMA-complete — the quantum analog of SAT being NP-complete. This establishes that certain quantum physics problems are computationally hard even for quantum computers, and it connects quantum complexity theory directly to condensed matter physics and quantum chemistry.
