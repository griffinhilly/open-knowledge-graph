---
id: kolmogorov-complexity
title: Kolmogorov Complexity
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: re-and-co-re-languages
  type: soft
- id: cardinality-and-countability
  type: soft
- id: big-o-notation
  type: soft
- id: combinations
  type: soft
- id: algorithm-complexity
  type: soft
tags:
- algorithmic-information-theory
- randomness
- descriptional-complexity
stage: advanced
status: validated
---

# Kolmogorov Complexity

## Core Idea
The Kolmogorov complexity K(x) of a string x is the length of the shortest program that outputs x on a fixed universal Turing machine. It provides an objective measure of the information content or 'randomness' of a string — a string is random if its shortest description is roughly as long as itself. Kolmogorov complexity is uncomputable: no algorithm can compute K(x) for all x. It has deep connections to data compression, statistical inference, and the mathematical foundations of probability.

## How It's Best Learned
Start with concrete examples: a string of one million zeros has very low Kolmogorov complexity (a short program generates it), while a truly random string of the same length likely requires a program nearly as long as itself. Prove the incompressibility lemma to rigorously establish that most strings are almost incompressible.

## Common Misconceptions
- Kolmogorov complexity depends on the choice of universal Turing machine, but only up to an additive constant (the invariance theorem), making it machine-independent up to a fixed offset.
- Randomness in the Kolmogorov sense is a property of individual strings, not of a probability distribution — a specific string either is or is not complex, regardless of how it was generated.
