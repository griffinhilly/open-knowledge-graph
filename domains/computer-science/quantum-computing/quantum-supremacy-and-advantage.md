---
id: quantum-supremacy-and-advantage
title: Quantum Supremacy and Quantum Advantage
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-circuits
  type: hard
- id: bqp-and-quantum-complexity
  type: hard
- id: quantum-error-correction-basics
  type: soft
tags:
- quantum-supremacy
- quantum-advantage
- random-circuit-sampling
- computational-hardness
stage: expert
status: validated
---
# Quantum Supremacy and Quantum Advantage

## Core Idea
Quantum supremacy (or quantum advantage) refers to a quantum computer performing a computational task that no classical computer can perform in a feasible amount of time. Google's 2019 Sycamore experiment claimed supremacy via random circuit sampling — a 53-qubit processor completed a sampling task in 200 seconds that was estimated to take 10,000 years classically. The demonstration is significant because it provides experimental evidence that quantum computational power exceeds classical, but the sampled task has no practical application. The distinction between supremacy (any task, even artificial) and practical advantage (useful tasks) remains an active frontier.

## Questions

```yaml
- question: "Google's quantum supremacy experiment used random circuit sampling. Why was this task chosen rather than a practically useful computation like factoring?"
  type: multiple-choice
  options: ["Factoring is easier to verify classically, making it a less convincing demonstration", "Random circuit sampling requires the fewest qubits", "Random circuit sampling is believed to be classically hard even at moderate circuit depth, and it can be verified probabilistically using cross-entropy benchmarking — making it the most achievable supremacy demonstration on near-term hardware", "Random circuit sampling is the only task where quantum computers are faster"]
  answer: 2
  explanation: "Random circuit sampling was chosen because: (1) computational complexity arguments (based on the polynomial hierarchy) suggest it is classically intractable even at moderate depth; (2) it does not require error correction, making it feasible on noisy hardware; and (3) cross-entropy benchmarking provides a way to verify the quantum output without full classical simulation. Factoring useful numbers requires thousands of error-corrected logical qubits, far beyond current capabilities."

- question: "After Google's supremacy claim, IBM argued that the classical simulation could be done in 2.5 days rather than 10,000 years using a different algorithm and enough disk space. This invalidates the supremacy claim entirely."
  type: true-false
  answer: false
  explanation: "IBM's response showed that the classical hardness estimate depends on assumptions about available classical resources and algorithms. The estimated classical time has shifted as better classical simulation methods have been found, and subsequent work by Chinese groups further reduced the gap. However, the fundamental point remains: as quantum circuits grow (more qubits, more depth), classical simulation costs scale exponentially while quantum execution does not. The specific threshold at which supremacy is 'achieved' is a moving target, but the asymptotic scaling argument is robust."

- question: "What is the difference between quantum supremacy and quantum advantage, and why does the distinction matter?"
  type: short-answer
  answer: "Quantum supremacy refers to performing ANY computational task faster than any classical computer, even if the task is artificial and has no practical use (like random circuit sampling). Quantum advantage refers to performing a USEFUL task faster or better than the best classical approach. Supremacy has arguably been demonstrated; practical advantage for real-world problems has not. The distinction matters because supremacy demonstrates that quantum computational power is real, but it does not yet translate to practical value for end users."
  explanation: "The path from supremacy to advantage is the central challenge of the field. Supremacy experiments validate the physical and computational principles, but the tasks they solve (sampling from random circuits) are chosen specifically because they are hard to simulate classically, not because anyone needs the output. Practical advantage requires quantum algorithms that solve problems people care about — molecular simulation, optimization, machine learning — faster than the best classical alternatives, which continues to be elusive on current hardware."
```

## Explainer

The question "can a quantum computer do something a classical computer cannot?" moved from theory to experiment in 2019, when Google's Sycamore processor performed a computation that its team estimated would take the world's most powerful supercomputer thousands of years. This event, termed **quantum supremacy**, was a milestone analogous to the first heavier-than-air powered flight — a proof of principle that quantum computational power is real, even though the task performed (random circuit sampling) has no practical use.

The experiment worked as follows. A 53-qubit superconducting processor executed **random quantum circuits** — sequences of randomly chosen one- and two-qubit gates — of depth 20. The circuit's output is a probability distribution over 2^53 bit strings. Because quantum interference creates complex correlations in this distribution, the output cannot be efficiently sampled by a classical computer (under plausible complexity-theoretic assumptions related to the non-collapse of the polynomial hierarchy). Google verified the quality of the quantum samples using **cross-entropy benchmarking (XEB)**: compare the measured bit-string frequencies to the ideal probabilities (computed classically for smaller circuits) and check that the correlation exceeds what a random or trivially simulated sampler would achieve.

The supremacy claim was immediately contested. IBM argued that with 10,000 PB of disk storage, a classical supercomputer could complete the simulation in days rather than millennia. Subsequent work by classical simulation researchers has further narrowed the gap, and Chinese experiments with 60+ qubits raised the bar. The lesson is that **supremacy is not a binary threshold but a moving frontier**: classical algorithms improve, quantum hardware improves, and the boundary shifts. What remains robust is the asymptotic argument — classical simulation cost scales exponentially with qubit count and circuit depth, while quantum execution cost scales polynomially. At some width and depth, the crossover is inevitable.

The broader challenge is moving from supremacy to **practical quantum advantage** — using a quantum computer to solve a problem that matters, faster or better than the best classical approach. Candidates include quantum chemistry simulation (molecular ground states), optimization (logistics, finance), and machine learning. None have achieved unambiguous advantage on current hardware. The obstacles are noise (limiting circuit depth and fidelity), qubit count (limiting problem size), and classical competition (classical algorithms for the same problems keep improving). The NISQ era (noisy intermediate-scale quantum) is characterized by this gap between demonstrated quantum computational power and demonstrated practical utility. Bridging this gap — through better hardware, better error mitigation, or better algorithms — is the defining challenge of quantum computing in the 2020s.
