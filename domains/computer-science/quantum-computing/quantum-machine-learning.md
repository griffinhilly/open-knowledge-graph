---
id: quantum-machine-learning
title: Quantum Machine Learning
domain: computer-science
course: quantum-computing
prerequisites:
- id: quantum-circuits
  type: hard
- id: variational-quantum-eigensolver
  type: hard
- id: grovers-search-algorithm
  type: soft
tags:
- quantum-ML
- variational-circuit
- kernel-method
- data-encoding
- barren-plateau
stage: expert
status: validated
---
# Quantum Machine Learning

## Core Idea
Quantum machine learning (QML) explores whether quantum computers can offer advantages for machine learning tasks through quantum-enhanced feature spaces, faster linear algebra, or variational quantum models. Approaches include quantum kernel methods (using quantum circuits to compute kernels in exponentially large Hilbert spaces), parameterized quantum circuits as trainable models (quantum neural networks), and quantum-enhanced sampling. While theoretical quantum speedups exist for specific subroutines (HHL for linear systems, quantum sampling), demonstrating practical quantum advantage for real-world ML tasks remains an open challenge, with barren plateaus, data loading bottlenecks, and dequantization results as key obstacles.

## Questions

```yaml
- question: "A quantum kernel method encodes classical data into quantum states and computes inner products in the quantum Hilbert space. What potential advantage does this provide over classical kernel methods?"
  type: multiple-choice
  options: ["Quantum kernels are always more expressive than classical kernels", "The quantum feature space is exponentially large (2^n dimensions for n qubits), potentially capturing complex patterns inaccessible to polynomial-dimensional classical feature maps", "Quantum kernels can be computed in O(1) time regardless of data dimensionality", "Quantum kernels eliminate the need for training data"]
  answer: 1
  explanation: "An n-qubit quantum circuit maps data into a 2^n-dimensional Hilbert space, which could in principle capture complex feature interactions that would require exponentially large classical feature maps. However, this potential advantage is not automatic: the quantum kernel must align with the structure of the actual learning problem, and there are classical kernels that can simulate many quantum kernels efficiently. The advantage depends on the specific data structure and encoding scheme."

- question: "The barren plateau problem does not affect quantum machine learning models — it only applies to quantum chemistry algorithms like VQE."
  type: true-false
  answer: false
  explanation: "Barren plateaus are a general problem for parameterized quantum circuits: for sufficiently random or deep circuits, the gradient of the cost function vanishes exponentially with the number of qubits. This affects QML models (quantum neural networks) at least as severely as VQE. In fact, QML models with global cost functions on many qubits are particularly susceptible. Barren plateaus are a fundamental obstacle to scaling variational QML approaches and are an active area of research."

- question: "What is the 'data loading' or 'input problem' in quantum machine learning, and why does it threaten quantum speedup claims?"
  type: short-answer
  answer: "Most quantum ML algorithms assume the classical data is already loaded into a quantum state (amplitude encoding: N classical values encoded as amplitudes of log(N) qubits). But actually loading N classical data points into a quantum state requires O(N) operations, which can negate the quantum speedup for the subsequent computation. If data loading takes as long as classical processing, the overall speedup disappears. This is the same state preparation bottleneck that limits the practical utility of the QFT for classical data."
  explanation: "The data loading problem has led to 'dequantization' results (Tang 2018 and follow-ups) showing that several quantum ML speedups — including the HHL-based quantum recommendation algorithm — can be matched classically if the classical algorithm is given the same data access model (sample-and-query access). This does not mean quantum ML is useless, but it forces the field to look for advantages in native quantum data (quantum sensing, quantum chemistry output) or in settings where data is naturally quantum."
```

## Explainer

Machine learning and quantum computing are two of the most active areas of technology research, and their intersection — quantum machine learning — has generated enormous excitement and equally significant skepticism. The fundamental question is: can quantum computers learn from data faster or better than classical computers? The answer, as of the mid-2020s, is "sometimes in theory, not yet demonstrated in practice."

**Variational quantum models** (sometimes called quantum neural networks) use parameterized quantum circuits as trainable function approximators, analogous to classical neural networks. The circuit takes encoded input data, applies parameterized gates, and produces measurement statistics that serve as the model's output. Training adjusts the parameters to minimize a loss function, typically via hybrid quantum-classical optimization. These models can be expressive — a quantum circuit with n qubits explores a 2^n-dimensional Hilbert space — but expressiveness does not guarantee learnability. The **barren plateau** problem shows that for generic circuits, gradients vanish exponentially with qubit count, making optimization intractable. Overcoming barren plateaus requires structured ansatze, local cost functions, or clever initialization strategies.

**Quantum kernel methods** take a different approach: use a quantum circuit to define a kernel function k(x, x') = |<phi(x)|phi(x')>|^2, where |phi(x)> is the quantum feature map of classical data point x. The kernel is then used in a classical support vector machine or Gaussian process. The potential advantage is that quantum feature maps can access exponentially large feature spaces that might separate data more effectively than classical features. However, recent theoretical work shows that quantum kernel advantages are data-dependent and fragile — random quantum kernels tend to produce kernel matrices that concentrate toward the identity as qubit count grows, becoming useless for classification.

**Quantum speedups for linear algebra** (the HHL algorithm for solving linear systems, quantum principal component analysis) were early hopes for QML. However, **dequantization** results by Tang and others showed that many of these speedups evaporate when classical algorithms are given comparable data access. The quantum algorithm for recommendation systems, initially claimed to provide an exponential speedup, was dequantized to a classical algorithm with comparable performance. The lesson is that quantum speedups for classical data processing are harder to achieve than initially believed.

Where might quantum advantage actually emerge? The most promising direction is **quantum data** — using quantum computers to process data that is inherently quantum (output of quantum sensors, quantum communication channels, quantum chemistry simulations). For such data, quantum computers have a natural advantage because classical processing requires exponentially many bits to represent quantum states. Beyond this, structured problems where quantum interference provides a genuine computational advantage — similar to how Shor's algorithm exploits periodicity — remain the best candidates. The field is maturing from broad optimism toward rigorous identification of where quantum advantages exist and where they do not.
