---
id: bpp-complexity-class
title: 'BPP: Bounded Error Probabilistic Polynomial Time'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: probabilistic-turing-machines
  type: hard
- id: complexity-class-p-definition
  type: hard
tags:
- complexity-classes
- randomized-algorithms
stage: advanced
status: draft
---

# BPP: Bounded Error Probabilistic Polynomial Time

## Core Idea
BPP is the class of languages decided by a probabilistic PTM in polynomial time with two-sided error at most 1/3 (amplifiable to any ε > 0 via repetition). BPP trivially contains P. It is widely believed (but unproven) that BPP ⊆ NP and BPP ⊆ P with high probability, though NP ⊆ BPP would cause PH to collapse, suggesting BPP is 'small' relative to NP. BPP captures practical randomized algorithms where error probability is controllable and output distribution matters.
