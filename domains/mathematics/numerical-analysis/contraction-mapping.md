---
id: contraction-mapping
title: Contraction Mapping Theorem
domain: mathematics
course: numerical-analysis
prerequisites:
- id: metric-spaces-definition
  type: hard
builds-toward:
- fixed-point-iteration
tags:
- contraction-mapping
- banach
- fixed-point
stage: abstract-reasoning
status: draft
---

# Contraction Mapping Theorem

## Core Idea
The contraction mapping theorem (Banach fixed-point theorem) guarantees that if g is a contraction with Lipschitz constant L < 1 on a complete metric space, then g has a unique fixed point and iteration x_{n+1} = g(x_n) converges to it with exponential rate. This theorem justifies fixed-point and iterative methods throughout numerical analysis.
