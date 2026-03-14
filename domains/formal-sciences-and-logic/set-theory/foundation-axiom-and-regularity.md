---
id: foundation-axiom-and-regularity
title: The Axiom of Foundation and Regularity
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: axiom-of-regularity
  type: hard
- id: well-founded-relations
  type: hard
builds-toward:
- cumulative-hierarchy-ranks
- hereditarily-finite-sets
tags:
- foundation
- regularity
- well-founded
- no-cycles
stage: formal-systems
status: draft
---

# The Axiom of Foundation and Regularity

## Core Idea
The axiom of foundation (or regularity) states: every nonempty set has an ∈-minimal element. This forbids cycles like x ∈ y ∈ x and infinite descending chains. Foundation is equivalent to saying every set appears in the cumulative hierarchy V. It ensures the ∈ relation is well-founded, grounding the set-theoretic universe.

## How It's Best Learned
Show that foundation rules out x ∈ x (take {x} as the nonempty set; if x ∈ x then x ∈ {x} and x ∈ x, violating minimality). Discuss the rank function as a direct consequence. Note ZFC + ¬Foundation is consistent (non-well-founded set theories exist) but uncommon.

## Common Misconceptions
- Assuming foundation is 'obvious' (historically, it was debated and is independent of other axioms).
- Confusing the no-cycle consequence with the axiom itself; the axiom is stronger.
