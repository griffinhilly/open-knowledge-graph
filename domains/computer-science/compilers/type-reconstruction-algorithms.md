---
id: type-reconstruction-algorithms
title: Type Reconstruction and Inference
domain: computer-science
course: compilers
prerequisites:
- id: type-inference-algorithms
  type: hard
- id: unification-algorithm
  type: hard
builds-toward:
- constraint-based-type-checking
tags:
- type-systems
- inference
- algorithms
stage: advanced
status: draft
---

# Type Reconstruction and Inference

## Core Idea
Type reconstruction determines types for expressions where types aren't explicitly written. It generates constraints (variable must equal int, type-a must unify with type-b) and solves them via unification, producing a consistent type assignment that respects the language's type rules.
