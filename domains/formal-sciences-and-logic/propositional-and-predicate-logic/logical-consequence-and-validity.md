---
id: logical-consequence-and-validity
title: Logical Consequence and Validity
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: satisfaction-in-structures
  type: hard
- id: logical-implication-entailment
  type: soft
builds-toward:
- fol-soundness-completeness
- model-theory-basics
tags:
- semantics
- entailment
- first-order-logic
stage: formal-systems
status: draft
---

# Logical Consequence and Validity

## Core Idea
Γ semantically entails φ (Γ ⊨ φ) if every structure satisfying all formulas in Γ also satisfies φ. A formula is valid if it is entailed by the empty set—true in every structure. Gödel's completeness theorem establishes that syntactic consequence (provability) equals semantic consequence for first-order logic.

## How It's Best Learned
Build counterexamples to refute proposed consequences. Identify valid formulas (like ∀x (P(x) → P(x))) and satisfiable-but-invalid formulas.
