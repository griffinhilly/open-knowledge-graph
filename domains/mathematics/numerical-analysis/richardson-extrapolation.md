---
id: richardson-extrapolation
title: Richardson Extrapolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: numerical-differentiation
  type: hard
builds-toward:
- romberg-integration
tags:
- extrapolation
- acceleration
- richardson
stage: abstract-reasoning
status: draft
---

# Richardson Extrapolation

## Core Idea
Richardson extrapolation combines numerical estimates at different step sizes to cancel leading-order error terms. If an estimate has error c₁h + c₂h² + ..., combining results at h and h/2 eliminates the O(h) term. This acceleration technique generalizes to any problem with known asymptotic error expansions and is the foundation for Romberg integration.
