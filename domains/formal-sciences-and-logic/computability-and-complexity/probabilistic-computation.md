---
id: probabilistic-computation
title: Probabilistic Computation and BPP
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-and-polynomial-time
  type: hard
- id: time-complexity-classes-formal
  type: hard
- id: probability-axioms
  type: hard
- id: nondeterministic-turing-machines
  type: soft
- id: conditional-probability
  type: soft
tags:
- complexity
- randomness
- BPP
- probabilistic-algorithms
stage: advanced
status: validated
---

# Probabilistic Computation and BPP

## Core Idea
A probabilistic Turing machine has access to random coin flips at each step. BPP (bounded-error probabilistic polynomial time) is the class of problems solvable by a polynomial-time PTM that errs with probability at most 1/3 on every input — either direction. Error amplification by repeated independent trials shows the specific threshold 1/3 is arbitrary; any constant less than 1/2 defines the same class. Most researchers believe BPP = P (randomness does not help asymptotically), supported by hardness-vs-randomness connections in derandomization theory, though this is unproven.

## How It's Best Learned
Study concrete randomized algorithms first: Miller-Rabin primality testing and Schwartz-Zippel polynomial identity testing. Understand the error-amplification argument (majority vote over independent trials) to see why the error bound is flexible. Then compare BPP to NP: in NP, a single witness suffices for acceptance; in BPP, a majority of random paths must accept.

## Common Misconceptions
- BPP is not the same as NP: in NP, a single accepting path suffices; in BPP, acceptance requires a majority of computation paths to accept with high probability.
- A BPP algorithm can err, but the error probability is over the algorithm's internal random choices, not over adversarial inputs — for every fixed input, the algorithm is correct with high probability.
