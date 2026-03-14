---
id: generating-functions-intro
title: Introduction to Generating Functions
domain: mathematics
course: discrete-math
prerequisites:
- id: geometric-series
  type: hard
- id: stars-and-bars
  type: soft
- id: solving-linear-recurrences
  type: soft
- id: multinomial-coefficients
  type: soft
tags:
- generating-functions
- power-series
- combinatorics
- formal-power-series
stage: formal-systems
status: validated
---
# Introduction to Generating Functions

## Core Idea
A generating function encodes a sequence (a₀, a₁, a₂, …) as coefficients of the formal power series A(x) = a₀ + a₁x + a₂x² + ⋯. Multiplying generating functions corresponds to convolution of sequences, making them a powerful algebraic tool for counting. The generating function for binomial coefficients C(n,k) is (1+x)ⁿ, and 1/(1−x)ⁿ generates combinations with repetition. Generating functions provide a unified algebraic framework that can solve recurrences, count restricted compositions, and derive combinatorial identities.

## How It's Best Learned
Start with 1/(1−x) = 1 + x + x² + ⋯ as the simplest example, then explore 1/(1−x)² and 1/(1−x)ⁿ. Practice extracting a specific coefficient as the answer to a counting question. Solve a recurrence both by characteristic equations and by generating functions to compare methods.

## Common Misconceptions
- Worrying about convergence — in combinatorics, generating functions are formal algebraic objects, not functions evaluated at real numbers.
- Not identifying which coefficient in the expansion corresponds to the sought answer.
