---
id: live-variable-analysis
title: Live Variable Analysis
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
builds-toward:
- register-allocation
- dead-code-elimination
tags:
- liveness
- dataflow
- code-quality
stage: advanced
status: draft
---

# Live Variable Analysis

## Core Idea
Live variable analysis determines which variables may be used in the future from a given program point. A variable is live if its value is reachable from the program point and may be used before being overwritten. Live variables guide register allocation (live variables cannot share a register) and dead-code elimination (assignments to non-live variables are removable).
