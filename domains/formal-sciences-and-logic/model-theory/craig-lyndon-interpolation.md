---
id: craig-lyndon-interpolation
title: Craig-Lyndon Interpolation Theorem
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: logical-consequence-and-entailment
  type: hard
- id: interpolation-theorem
  type: soft
builds-toward:
- beth-definability-implicit-explicit
tags:
- Craig
- interpolation
- interpolant
- consequence
stage: abstract-reasoning
status: draft
---

# Craig-Lyndon Interpolation Theorem

## Core Idea
If φ → ψ is a tautology, there exists an interpolant θ (using only symbols common to φ and ψ) such that φ → θ and θ → ψ are both tautologies. The Lyndon version strengthens this: the interpolant can be chosen to preserve the direction of implications in formulas. Interpolation theorems are fundamental for studying definability and relationships between formulas.
