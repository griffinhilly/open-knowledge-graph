---
id: complexity-class-p-definition
title: 'Complexity Class P: Polynomial Time'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: p-vs-np-problem
  type: hard
- id: time-complexity-classes
  type: soft
builds-toward:
- complexity-class-np-definition
tags:
- p-class
- polynomial-time
- tractable
- efficient
- definition
stage: advanced
status: draft
---

# Complexity Class P: Polynomial Time

## Core Idea
The class P contains languages decided by deterministic TMs in polynomial time. P represents problems solvable efficiently in theory (sorting, shortest paths, primality testing). P is robust: all standard polynomial-time models (RAM, circuits, multi-tape TMs) agree on P due to polynomial equivalence. P is widely believed tractable; whether P = NP is the central open problem in CS.
