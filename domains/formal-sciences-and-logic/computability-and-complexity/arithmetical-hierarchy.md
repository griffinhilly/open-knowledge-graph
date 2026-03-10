---
id: arithmetical-hierarchy
title: The Arithmetical Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: re-and-co-re-languages
  type: hard
- id: first-order-logic-syntax
  type: hard
- id: formal-arithmetic-and-expressibility
  type: soft
- id: godels-incompleteness-theorems
  type: soft
- id: mathematical-induction
  type: soft
- id: cardinality-and-countability
  type: soft
tags:
- computability
- definability
- logic
- hierarchy
stage: advanced
status: draft
---

# The Arithmetical Hierarchy

## Core Idea
The arithmetical hierarchy classifies sets of natural numbers by the complexity of their first-order definitions over arithmetic. A set is Σ₁ if definable with one existential quantifier block (equivalently, RE); Π₁ if definable with one universal quantifier block (co-RE). Higher levels Σₙ and Πₙ alternate quantifier blocks, and no level collapses into the one below — each level contains strictly harder problems. This hierarchy connects computability theory to logic and forms the foundation for more refined degree theory.

## How It's Best Learned
Study both the syntactic characterization (quantifier alternation depth) and the semantic one (oracle TM computation). Verify that the halting problem is Σ₁-complete and that the totality problem (does TM M halt on all inputs?) is Π₂-complete as a concrete example of a higher-level problem.

## Common Misconceptions
- The arithmetical hierarchy is not the polynomial hierarchy from complexity theory — the former concerns computability and definability, the latter concerns polynomial-time computation.
- Σₙ and Πₙ are not disjoint; their intersection Δₙ contains problems definable both ways, and Δ₁ equals exactly the class of decidable sets.
