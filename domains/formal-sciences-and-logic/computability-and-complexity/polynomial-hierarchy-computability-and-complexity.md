---
id: polynomial-hierarchy-computability-and-complexity
title: 'The Polynomial Time Hierarchy: Levels Beyond NP'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: complexity-class-definitions-hierarchy
  type: hard
- id: p-versus-np
  type: soft
builds-toward:
- pspace-completeness
tags:
- polynomial-hierarchy
- quantified-formulas
- complexity-levels
stage: advanced
status: draft
---

# The Polynomial Time Hierarchy: Levels Beyond NP

## Core Idea
The polynomial time hierarchy (PH) extends beyond P and NP by iterating quantification: Σ₁P = NP, Π₁P = coNP, Σ₂P allows alternating quantifiers, and so on. If P = NP, then PH collapses to P; proving hierarchy separation is an open problem. PH captures the complexity of problems with multiple levels of existential and universal quantification.

## How It's Best Learned
Use quantified Boolean formulas (QBF) as examples: existential quantifiers give Σ classes, universal give Π classes. Compare TQBF (true QBF) at different levels.

## Common Misconceptions
- Assuming the polynomial hierarchy always has infinitely many distinct levels. It does unless P = NP, which is unknown.
- Confusing alternation in grammar with complexity level. The number of quantifier alternations determines the level.
