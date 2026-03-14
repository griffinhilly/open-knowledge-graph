---
id: branch-prediction-techniques
title: Branch Prediction and Speculative Execution
domain: computer-science
course: computer-architecture
prerequisites:
- id: data-hazards-control-hazards
  type: hard
builds-toward:
- superscalar-and-vliw-design
- out-of-order-execution-design
tags:
- branch
- prediction
- speculation
- performance
stage: formal-systems
status: draft
---

# Branch Prediction and Speculative Execution

## Core Idea
Branch prediction guesses the outcome of conditional branches and speculatively fetches the predicted path, minimizing pipeline stalls from control hazards. Prediction tables track branch history; incorrect predictions require rollback and re-execution.
