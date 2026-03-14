---
id: probabilistic-turing-machines
title: Probabilistic Turing Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: nondeterministic-finite-automata
  type: soft
builds-toward:
- bpp-complexity-class
- rp-corp-complexity
tags:
- randomization
- probabilistic-computation
stage: advanced
status: draft
---

# Probabilistic Turing Machines

## Core Idea
A probabilistic Turing machine (PTM) is a nondeterministic TM where each branch is taken with specified probability. Unlike NTM (existential: accept if any branch succeeds), PTM explores branches stochastically. A PTM decides a language L with error probability ε if for x ∈ L it accepts with probability ≥ 1-ε and for x ∉ L it rejects with probability ≥ 1-ε. PTMs formalize randomized algorithms and enable analysis of error probability via amplification.
