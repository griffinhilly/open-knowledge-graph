---
id: uniform-continuity
title: Uniform Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
builds-toward:
- uniform-continuity-compact-sets
- interchange-limit-integral
tags:
- uniform-continuity
- continuity
- epsilon-delta
stage: abstract-reasoning
status: draft
---

# Uniform Continuity

## Core Idea
A function f is uniformly continuous on a set S if for every ε > 0, there exists δ > 0 such that for all x, y in S with |x − y| < δ, we have |f(x) − f(y)| < ε. The key difference from continuity is that δ does not depend on the specific point; the same δ works for all points.
