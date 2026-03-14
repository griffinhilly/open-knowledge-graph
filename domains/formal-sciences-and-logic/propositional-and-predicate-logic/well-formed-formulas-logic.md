---
id: well-formed-formulas-logic
title: Well-Formed Formulas (WFF) in Propositional and First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-connectives
  type: hard
- id: propositional-syntax
  type: hard
builds-toward:
- atomic-versus-complex-formulas
- logical-consequence-and-entailment
- open-and-closed-formulas-fol
tags:
- syntax
- propositional-logic
- first-order-logic
- wff
stage: formal-systems
status: draft
---

# Well-Formed Formulas (WFF) in Propositional and First-Order Logic

## Core Idea
A well-formed formula (WFF) is a syntactically valid string following the grammar rules of propositional or first-order logic. In propositional logic, WFFs are built from atomic propositions and connectives (¬, ∧, ∨, →, ↔). In first-order logic, WFFs also include terms, predicates, and quantifiers (∀, ∃), with strict rules about variable binding and scope. Understanding what counts as a valid formula is foundational to defining logical consequence, proof systems, and semantics.

## How It's Best Learned
Start with propositional WFFs using simple examples and counterexamples (e.g., 'P ∧ Q' is WFF, but '∧ P' is not). Progress to first-order by adding terms and quantifiers with exercises on spotting syntactic errors. Use recursive grammar definitions and parse trees to visualize structure.

## Common Misconceptions
- Thinking that any string of symbols with logical connectives is a WFF (no — syntax matters).
- Forgetting that quantifiers must bind variables correctly (∀x P(y) is WFF but leaves y free).
- Assuming parentheses don't matter (they do — they determine scope and precedence).
