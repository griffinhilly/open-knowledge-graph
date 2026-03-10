---
id: intuitionistic-logic-intro
title: Introduction to Intuitionistic Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: natural-deduction-propositional
  type: hard
- id: propositional-semantics
  type: soft
builds-toward:
- modal-logic-intro
tags:
- intuitionistic-logic
- constructive-logic
- Brouwer
- BHK
- law-of-excluded-middle
stage: formal-systems
status: draft
---

# Introduction to Intuitionistic Logic

## Core Idea
Intuitionistic logic rejects the law of excluded middle (LEM: φ ∨ ¬φ) and double negation elimination as universal logical laws. In the Brouwer-Heyting-Kolmogorov (BHK) interpretation, a proof of φ is a construction: a proof of φ ∧ ψ is a pair of proofs, a proof of φ → ψ is a function transforming proofs of φ into proofs of ψ, and — crucially — a proof of φ ∨ ψ requires either a proof of φ or a proof of ψ, not merely a refutation of both being false. Intuitionistic logic is complete for Kripke semantics (possible-worlds models) and corresponds via the Curry-Howard correspondence to simply-typed lambda calculus.

## How It's Best Learned
Modify natural deduction by removing the classical rules (RAA, LEM) and see which theorems become unprovable. Verify that ¬¬p → p fails intuitionistically. Explore the Curry-Howard correspondence between proofs and programs.

## Common Misconceptions
- Intuitionistic logic is not 'weaker' logic for doubters — it is a different logic for constructive reasoning, with its own completeness theorem.
- ¬¬φ does not imply φ intuitionistically; double negation is a strictly weaker statement than the original.
