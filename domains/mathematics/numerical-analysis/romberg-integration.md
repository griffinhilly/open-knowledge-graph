---
id: romberg-integration
title: Romberg Integration
domain: mathematics
course: numerical-analysis
prerequisites:
- id: richardson-extrapolation
  type: hard
- id: composite-quadrature-rules
  type: hard
tags:
- romberg
- extrapolation
- acceleration
stage: advanced
status: draft
---

# Romberg Integration

## Core Idea
Romberg integration combines composite trapezoidal rules at progressively finer step sizes using Richardson extrapolation, achieving rapid convergence. A table is built where each row represents finer meshes, and extrapolation eliminates error terms successively, increasing convergence order at each step. The method is adaptive and practical for smooth integrands.
