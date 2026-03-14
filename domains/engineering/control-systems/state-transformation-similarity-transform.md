---
id: state-transformation-similarity-transform
title: State Transformations and Similarity Transformations
domain: engineering
course: control-systems
prerequisites:
- id: state-space-canonical-forms
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
builds-toward:
- observability-controllability-tests
- pole-placement-observer-design
tags:
- state-transformation
- similarity-transform
- change-of-basis
- invariants
stage: abstract-reasoning
status: draft
---

# State Transformations and Similarity Transformations

## Core Idea
State transformations x̄ = Tx change the state-space representation but not the input-output behavior. Ā = TAT⁻¹, B̄ = TB, C̄ = CT⁻¹. Similarity transformations preserve eigenvalues, transfer function, and controllability/observability properties. Diagonalization and modal forms are special cases used to decouple and simplify analysis.
