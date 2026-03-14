---
id: kan-extensions-pointwise
title: Kan Extensions and Pointwise Formulae
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: kan-extensions
  type: hard
- id: limits-and-colimits
  type: hard
builds-toward:
- topos-theory-intro
tags:
- kan-extension
- pointwise
- limit
- colimit
- universal
stage: advanced
status: draft
---

# Kan Extensions and Pointwise Formulae

## Core Idea
Given functors p: A → B and F: A → C, the right Kan extension Ran_p F: B → C is the universal functor extending F and compatible with p. When C is complete, pointwise formula holds: (Ran_p F)(b) ≅ lim_{a → b} F(a), a limit over the comma category (a ↓ b). Left Kan extensions are dual, using colimits. Pointwise formulae allow explicit computation and reveal Kan extensions as limit/colimit operations, connecting them to universal constructions.

## How It's Best Learned
Prove the pointwise formula directly from the universal property. Compute right Kan extensions along inclusion functors (restriction and pointwise limit). Study how adjoint functors arise as Kan extensions and how tensor products relate to Kan extension constructions.

## Common Misconceptions
Pointwise formula requires target completeness; without it, Kan extensions exist abstractly but cannot be computed via limits. Not every functor looking like a Kan extension satisfies the universal property. Left and right Kan extensions are fundamentally different—left uses colimits, not limits.
