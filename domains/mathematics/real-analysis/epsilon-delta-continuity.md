---
id: epsilon-delta-continuity
title: Epsilon-Delta Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: continuity-definition
  type: hard
builds-toward:
- sequential-characterization-continuity
- uniform-continuity
tags:
- continuity
- epsilon-delta
- limits
stage: abstract-reasoning
status: draft
---

# Epsilon-Delta Continuity

## Core Idea
A function f is continuous at a point c if for every ε > 0, there exists δ > 0 such that if |x − c| < δ, then |f(x) − f(c)| < ε. This rigorous epsilon-delta definition quantifies the informal idea that small changes in input produce small changes in output. A function is continuous on an interval if it is continuous at every point.
