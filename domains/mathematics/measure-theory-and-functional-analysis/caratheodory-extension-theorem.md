---
id: caratheodory-extension-theorem
title: Carathéodory's Extension Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: outer-measure-definition
  type: hard
builds-toward:
- lebesgue-outer-measure
tags:
- measure-theory
- extension-theorems
stage: abstract-reasoning
status: draft
---

# Carathéodory's Extension Theorem

## Core Idea
Carathéodory's theorem states that any outer measure μ* induces a measure on the σ-algebra of 'μ*-measurable' sets (those satisfying μ*(A) = μ*(A∩E) + μ*(A∩Eᶜ)). This is the standard method for constructing Lebesgue measure from an elementary definition.

## How It's Best Learned
Work through the proof that μ*-measurable sets form a σ-algebra and that μ* restricted to it is σ-additive.

## Common Misconceptions
The Carathéodory condition is non-obvious; it's not automatic that the μ*-measurable sets form a σ-algebra without this specific requirement.
