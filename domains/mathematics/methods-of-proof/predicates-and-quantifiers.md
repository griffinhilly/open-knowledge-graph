---
id: predicates-and-quantifiers
title: Predicates and Quantifiers
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
- id: variable-expressions
  type: soft
builds-toward:
- negation-of-quantifiers
- proof-structure-and-terminology
- existence-proofs
tags:
- predicates
- quantifiers
- universal
- existential
- domain-of-discourse
stage: formal-systems
status: draft
---

# Predicates and Quantifiers

## Core Idea
A predicate P(x) is a statement containing a variable whose truth value depends on the value substituted for x. Quantifiers convert predicates into statements: the universal quantifier ∀x P(x) asserts P(x) is true for every element in the domain, while the existential quantifier ∃x P(x) asserts P(x) is true for at least one element. The domain of discourse — the set of allowable values for x — is always essential context.

## How It's Best Learned
Connect to familiar algebraic statements: 'for all real x, x² ≥ 0' is a universal statement. Practice identifying the domain of discourse explicitly. Translate between symbolic notation and natural language in both directions.

## Common Misconceptions
- Forgetting that the truth of a quantified statement depends on the domain (∀x x > 0 is false over ℤ but true over ℝ⁺).
- Treating ∃x P(x) as requiring a specific, named witness rather than just evidence that one exists.
- Mixing up the scope of nested quantifiers.
