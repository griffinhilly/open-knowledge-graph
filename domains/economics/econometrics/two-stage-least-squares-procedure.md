---
id: two-stage-least-squares-procedure
title: 'Two-Stage Least Squares: Procedure and Inference'
domain: economics
course: econometrics
prerequisites:
- id: two-stage-least-squares
  type: hard
- id: instrumental-variables-validity
  type: hard
builds-toward:
- overidentification-test
tags:
- instrumental-variables
- two-stage
- estimation
stage: formal-systems
status: draft
---

# Two-Stage Least Squares: Procedure and Inference

## Core Idea
2SLS: Stage 1 regresses X on Z to obtain X̂; Stage 2 regresses Y on X̂. This yields consistent and asymptotically normal causal effect estimates under IV assumptions. Standard errors must account for first-stage estimation, typically using robust sandwich formulas.
