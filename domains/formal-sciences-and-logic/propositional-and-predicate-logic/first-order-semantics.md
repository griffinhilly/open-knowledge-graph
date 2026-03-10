---
id: first-order-semantics
title: First-Order Logic Semantics and Structures
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: set-theory-basics
  type: soft
builds-toward:
- natural-deduction-fol
- fol-soundness-completeness
- model-theory-basics
tags:
- structure
- interpretation
- satisfaction
- model
- domain
stage: formal-systems
status: draft
---

# First-Order Logic Semantics and Structures

## Core Idea
A first-order structure (or interpretation) for a signature consists of a non-empty domain D and an assignment of: each constant to an element of D, each n-ary function symbol to an n-ary function on D, and each n-ary predicate symbol to an n-ary relation on D. A variable assignment maps each variable to a domain element. Satisfaction (M, s ⊨ φ) is defined recursively: atomic formulas by checking relations, Boolean connectives compositionally, and quantifiers by ranging over all domain elements. A sentence is true in M (written M ⊨ φ) if it is satisfied under any variable assignment.

## How It's Best Learned
Work through small finite structures (sets of 2–4 elements) and evaluate FOL sentences by hand. Verify that the same formula can be true in one structure and false in another to build intuition for model-dependence.

## Common Misconceptions
- The domain is not fixed; every structure chooses its own domain, which need not be the natural numbers or any canonical set.
- Quantifier evaluation is not about logical connectives alone — ∀x φ(x) is true only if φ(a) holds for every element a in the domain.
