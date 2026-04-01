---
id: quantum-supremacy-complexity
title: Quantum Supremacy and Computational Complexity
domain: computer-science
course: quantum-computing
prerequisites:
- id: bqp-and-quantum-complexity
  type: hard
- id: quantum-supremacy-and-advantage
  type: hard
tags:
- quantum-supremacy
- computational-complexity
- quantum-advantage
- complexity-theory
stage: expert
status: validated
---

# Quantum Supremacy and Computational Complexity

## Core Idea
Quantum supremacy (or advantage) refers to the ability of quantum computers to solve problems faster than the best-known classical algorithms, ideally exponentially faster. Computational complexity theory formalizes this: BQP is the class of problems solvable by quantum computers in polynomial time. Strong evidence suggests BQP is larger than P (polynomial-time classical), supporting quantum advantages. Google's 2019 quantum supremacy claim demonstrated sampling a distribution from a random quantum circuit faster than classical simulation. However, supremacy claims require careful benchmarking; advantage is problem-specific, often requires asymptotic advantages (large problem instances), and practical value depends on application relevance.

## Questions

```yaml
- question: "What is the difference between quantum supremacy and quantum advantage?"
  type: short-answer
  answer: "Quantum supremacy is a specific claim: a quantum computer can solve a specific problem faster than any classical computer can. Quantum advantage is a broader term for quantum speedup, including cases where speedup is modest or problem-specific. Supremacy emphasizes the milestone of quantum computers outperforming classical; advantage acknowledges the spectrum of speedups. Both require rigorous benchmarking: comparing quantum vs. classical implementations, ensuring fair comparison (same hardware, same algorithm), and accounting for overhead (quantum error correction, compilation)."
  explanation: "Terminology matters in research claims. Supremacy is a strong claim; advantage is more nuanced. Practical quantum computing likely sees advantage in specific domains before universal supremacy."

- question: "Google's 2019 quantum supremacy result solved random circuit sampling. Why is random circuit sampling not directly useful, yet still significant?"
  type: multiple-choice
  options:
    - "Random circuit sampling is completely useless; the supremacy result has no scientific value"
    - "Random circuit sampling is not a real-world application, but demonstrates quantum speedup exists; it's a proof of concept motivating practical quantum algorithm development"
    - "Random circuit sampling is the most important quantum application; no other quantum algorithms matter"
    - "Supremacy requires solving practical problems; random circuits are too artificial"
  answer: 1
  explanation: "Random circuit sampling is a contrived problem designed to show quantum advantage with shallow circuits and high precision. It is not useful in practice, but the milestone matters: it demonstrates quantum computers can outperform classical ones for some task, proving quantum advantage is achievable. This motivates research into practical quantum algorithms and error correction. The significance is theoretical and aspirational, not practical."
```

## Explainer

Quantum supremacy represents a paradigm shift: quantum computers fundamentally faster than classical computers for at least some problems. The concept is rooted in computational complexity theory, which formalizes what problems are efficiently solvable.

**Complexity Classes**:
- **P**: Problems solvable classically in polynomial time (efficiently).
- **NP**: Problems whose solutions can be verified in polynomial time (includes P and likely much more).
- **BQP**: Problems solvable by quantum computers in polynomial time.

The relationship between P and BQP is unknown. Strong evidence suggests BQP is larger than P, meaning quantum computers can solve problems (efficiently) that classical computers cannot (efficiently). This is the basis for quantum advantage.

**Evidence for BQP > P**:
- Shor's algorithm factors in polynomial time (believed hard classically).
- Grover's algorithm searches unstructured databases with quadratic speedup.
- Hidden Subgroup Problem solved by quantum computers in polynomial time.

**Google's Quantum Supremacy Claim (2019)**: Google's 53-qubit Sycamore processor sampled from the output distribution of a random quantum circuit. The task: given a random circuit, sample from its output distribution. Google claimed the quantum computer solved this in 200 seconds; classical simulation would require 10,000 years on the world's fastest supercomputer. This was a significant milestone, but with caveats:
- Random circuit sampling is not a practical application.
- The classical benchmark (full simulation) is conservative; classical sampling heuristics may be faster.
- The advantage diminishes with error correction and larger circuits.

**Caveats and Challenges**:

1. **Problem Specificity**: Quantum advantage is often for artificial, designed problems (random circuits, specific structured instances), not real-world applications.

2. **Asymptotic vs. Practical**: Quantum advantage often applies to asymptotically large problem instances; for near-term problem sizes, classical methods may be faster.

3. **Overhead**: Error correction and quantum circuit compilation add significant overhead, reducing practical advantages.

4. **Classical Improvements**: As classical algorithms improve, the supremacy gap narrows. What looked like exponential advantage might be polynomial.

**BQP and NP**: A central open question is whether NP ⊆ BQP. If yes, quantum computers could solve NP-complete problems efficiently, revolutionizing cryptography and optimization. Evidence suggests NP ⊄ BQP (quantumly hard problems exist), but this is unproven.

**Practical Quantum Advantage**: Near-term quantum advantage is likely to be for domain-specific problems:
- **Quantum Chemistry**: Exponential classical cost, fundamental quantum advantage.
- **Combinatorial Optimization**: Potential speedup for specific instances, though not proven exponential.
- **Machine Learning**: Quantum machine learning algorithms show promise but are less developed.

**Future Directions**:
- **Fault-Tolerant Quantum Computing**: With error correction, demonstrating practical quantum advantage on useful problems.
- **Hybrid Quantum-Classical**: Combining quantum and classical for efficiency.
- **Problem-Specific Advantages**: Focusing on domains with clear quantum benefits rather than universal supremacy claims.

Quantum supremacy is a milestone demonstrating quantum computers can outperform classical ones. Achieving practical, economically valuable quantum advantage remains an open challenge.
