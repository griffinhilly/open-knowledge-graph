---
id: epsilon-delta-continuity
title: Epsilon-Delta Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: continuity-definition
  type: soft
- id: epsilon-n-convergence
  type: hard
builds-toward:
- sequential-continuity
- uniform-continuity
- rigorous-derivative-definition
tags:
- continuity
- epsilon-delta
- rigor
stage: advanced
status: draft
---

# Epsilon-Delta Continuity

## Core Idea
A function f is continuous at a point c if for every ε > 0, there exists δ > 0 such that |x - c| < δ implies |f(x) - f(c)| < ε. This formalizes 'small changes in input give small changes in output.' Continuity on a set means continuity at every point. It is the foundational definition for rigorous calculus.
