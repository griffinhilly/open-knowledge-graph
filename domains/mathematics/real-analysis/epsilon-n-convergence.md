---
id: epsilon-n-convergence
title: 'Sequences: Epsilon-N Convergence'
domain: mathematics
course: real-analysis
prerequisites:
- id: supremum-and-infimum
  type: hard
builds-toward:
- monotone-convergence-theorem
- subsequences
- cauchy-sequences-completeness
- limit-superior-and-inferior
tags:
- sequences
- convergence
- epsilon-delta
- limits
stage: advanced
status: draft
---

# Sequences: Epsilon-N Convergence

## Core Idea
A sequence (aₙ) converges to a limit L (written lim aₙ = L) if for every ε > 0, there exists N such that n > N implies |aₙ - L| < ε. This formal definition replaces intuition: 'aₙ gets arbitrarily close to L' becomes 'aₙ stays within ε of L eventually.' It is the foundation for all rigor in calculus.

## How It's Best Learned
Start with 1/n → 0: given ε, find N = ⌈1/ε⌉ and verify n > N ⟹ |1/n| < ε. Then try sin(n)/n → 0 and a non-convergent sequence like (-1)ⁿ to see why the definition fails.

## Common Misconceptions
- Forgetting that N must work for *all* ε, not just one.
- Thinking ε is given by the sequence rather than given for us to find N.
- Confusing 'eventually within ε' with 'every term within ε of L'.
