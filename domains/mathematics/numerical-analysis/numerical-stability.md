---
id: numerical-stability
title: Numerical Stability and Conditioning
domain: mathematics
course: numerical-analysis
prerequisites:
- id: catastrophic-cancellation
  type: hard
builds-toward:
- condition-number
tags:
- stability
- conditioning
- error-analysis
stage: abstract-reasoning
status: draft
---

# Numerical Stability and Conditioning

## Core Idea
A numerical algorithm is stable if small perturbations in inputs produce only small changes in outputs. Stability depends on both the problem (conditioning) and the algorithm (implementation). A well-conditioned problem solved with a stable algorithm yields accurate results; poor conditioning or instability can make even theoretically simple problems numerically unreliable.
