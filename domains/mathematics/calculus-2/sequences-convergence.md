---
id: sequences-convergence
title: Sequences and Convergence
domain: mathematics
course: calculus-2
prerequisites:
  - id: sequences-and-series-review
    type: hard
  - id: limits-at-infinity
    type: hard
builds-toward:
  - series-definition-and-partial-sums
  - divergence-test
tags: [sequences, convergence, limits]
stage: formal-systems
status: validated
---

# Sequences and Convergence

## Core Idea
A sequence {a_n} converges if lim(n->infinity) a_n = L for some finite L; otherwise it diverges. Convergence of sequences is analyzed using limit laws, the squeeze theorem, the monotone convergence theorem (bounded and monotone implies convergent), and L'Hopital's rule (by treating n as a continuous variable). Sequence convergence is prerequisite to understanding series convergence, since a series converges only if its partial sums form a convergent sequence.

## How It's Best Learned
Evaluate limits of sequences algebraically (divide by highest power of n), using L'Hopital's rule, and using the squeeze theorem. Determine monotonicity and boundedness. Practice with geometric sequences (r^n), factorial-based sequences (n!/n^n), and sequences involving exponentials.

## Common Misconceptions
- Confusing sequence convergence with series convergence (the sequence {1/n} converges to 0, but the series sum of 1/n diverges).
- Believing a bounded sequence must converge (it must also be monotone, or use a subsequence argument).
- Not recognizing that L'Hopital's rule applies to sequences by treating a_n = f(n).
