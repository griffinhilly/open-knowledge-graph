---
id: polynomial-hierarchy
title: The Polynomial Hierarchy
domain: computer-science
course: theory-of-computation
prerequisites:
- id: complexity-class-np-definition
  type: hard
- id: pspace-complexity-class
  type: soft
tags:
- complexity-classes
- quantified-formulas
- hierarchy
stage: advanced
status: draft
---

# The Polynomial Hierarchy

## Core Idea
The polynomial hierarchy (PH) generalizes P and NP by permitting multiple alternations of existential (∃) and universal (∀) quantifiers in polynomial time. Σ₁^P = NP (∃-quantified), Π₁^P = coNP (∀-quantified), Σ₂^P adds ∃∀ conditions. The hierarchy is believed infinite and contained in PSPACE. If any level collapses (Σᵢ^P = Πᵢ^P), the entire hierarchy collapses to that level. PH captures all polynomial-time problems expressible with bounded quantifier depth.
