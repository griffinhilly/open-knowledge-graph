---
id: observability-controllability-tests
title: Tests for Controllability and Observability
domain: engineering
course: control-systems
prerequisites:
- id: state-transformation-similarity-transform
  type: hard
- id: matrix-operations
  type: soft
builds-toward:
- pole-placement-observer-design
tags:
- controllability
- observability
- rank-test
- gramian
stage: abstract-reasoning
status: draft
---

# Tests for Controllability and Observability

## Core Idea
Controllability matrix Qc = [B AB A²B ... A^(n-1)B] has full rank iff system is controllable (all states reachable). Observability matrix Qo = [C; CA; ... CA^(n-1)]ᵀ has full rank iff system is observable (all states detectable). Loss of controllability/observability creates hidden modes that cannot be controlled or observed, limiting achievable performance.
