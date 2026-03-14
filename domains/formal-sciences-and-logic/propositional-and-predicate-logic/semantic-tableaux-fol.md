---
id: semantic-tableaux-fol
title: Semantic Tableaux (First-Order)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-semantics
  type: hard
- id: semantic-tableaux-propositional
  type: soft
builds-toward:
- fol-soundness-completeness
tags:
- tableaux
- gamma-rule
- delta-rule
- fairness
- quantifier-instantiation
stage: formal-systems
status: draft
---

# Semantic Tableaux (First-Order)

## Core Idea
First-order tableaux extend propositional tableaux with rules for quantifiers. The gamma rule (∀-elimination) instantiates a universal formula ∀x φ(x) with any term t, producing φ(t) — and crucially, the universal formula remains on the branch for future instantiations. The delta rule (∃-elimination) introduces a fresh constant c to witness ∃x φ(x), producing φ(c). A fairness condition ensures that every universal formula is eventually instantiated with every relevant term, guaranteeing completeness. An open branch in a completed fair tableau defines a countermodel, while closure of all branches proves validity.

## How It's Best Learned
Build tableaux for simple first-order arguments, carefully tracking which terms have been used for gamma-rule instantiations. Construct a countermodel from an open branch by reading off the domain elements and predicate extensions directly from the branch literals.

## Common Misconceptions
- The gamma rule can be applied infinitely many times to the same formula — this is necessary for completeness but means the procedure may not terminate.
- Delta-rule constants must be genuinely new — reusing an existing constant conflates distinct witnesses and invalidates the proof.
- Fairness is not optional — an unfair strategy can miss the instantiation needed to close all branches, making the system incomplete.
