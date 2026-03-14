---
id: pspace-complete-problems
title: PSPACE-Complete Problems
domain: computer-science
course: theory-of-computation
prerequisites:
- id: pspace-complexity-class
  type: hard
- id: np-completeness
  type: hard
tags:
- hardness
- completeness
- quantified-formulas
stage: advanced
status: draft
---

# PSPACE-Complete Problems

## Core Idea
A problem is PSPACE-complete if it is in PSPACE and every PSPACE problem polynomial-time reduces to it. The canonical example is TQBF: given a fully quantified Boolean formula with alternating ∃∀ quantifiers, determine if it evaluates to true. Other PSPACE-complete problems include game-position evaluation (can the current player force a win?) and certain pattern-matching with counting. PSPACE-completeness indicates inherent intractability that polynomial space cannot overcome.
