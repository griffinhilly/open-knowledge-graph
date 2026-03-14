---
id: outer-measure
title: Outer Measure and Carathéodory's Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: sigma-algebras-formal-construction
  type: hard
- id: supremum-and-infimum
  type: hard
builds-toward:
- lebesgue-measure-real-line
tags:
- measure-theory
- construction
stage: advanced
status: draft
---

# Outer Measure and Carathéodory's Theorem

## Core Idea
An outer measure is a countably subadditive function μ*: P(X) → [0,∞]. Carathéodory's theorem constructs a measure from an outer measure by restricting to Carathéodory-measurable sets, which satisfy the splitting property. This is the key tool for building Lebesgue measure.

## How It's Best Learned
First verify that any outer measure satisfying the countability axiom induces a σ-algebra. Apply to concrete examples like length on intervals to see how outer measure becomes Lebesgue measure.

## Common Misconceptions
- Thinking outer measure is already a measure (it's not countably additive on all sets). - Missing why the splitting property defines measurability (it's the precise condition Carathéodory needed). - Confusing inner and outer measure (only outer measure is used in the theorem).
