---
id: sequential-characterization-continuity
title: Sequential Characterization of Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: epsilon-n-convergence
  type: hard
builds-toward:
- uniform-continuity
- extreme-value-theorem-rigorous
tags:
- continuity
- sequences
- limits
stage: abstract-reasoning
status: draft
---

# Sequential Characterization of Continuity

## Core Idea
A function f is continuous at c if and only if for every sequence (xₙ) converging to c, the sequence (f(xₙ)) converges to f(c). This sequential characterization makes it easy to apply continuity proofs using sequence arguments rather than epsilon-delta arguments.
