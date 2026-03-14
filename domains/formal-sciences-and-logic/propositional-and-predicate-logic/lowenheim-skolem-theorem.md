---
id: lowenheim-skolem-theorem
title: Löwenheim-Skolem Theorems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: model-theory-basics
  type: hard
- id: fol-compactness
  type: soft
- id: cardinality-and-countability
  type: soft
builds-toward:
- godels-incompleteness-theorems
tags:
- Lowenheim-Skolem
- cardinality
- downward
- upward
- Skolem-paradox
stage: formal-systems
status: validated
---

# Löwenheim-Skolem Theorems

## Core Idea
The downward Löwenheim-Skolem theorem states that any first-order theory with an infinite model has a countable model. The upward version states that any theory with an infinite model of cardinality κ has models of every infinite cardinality λ ≥ κ. Together, these theorems show that first-order logic cannot pin down the cardinality of infinite structures: no first-order theory can uniquely characterize the real numbers or the natural numbers up to isomorphism. Skolem's paradox arises when set theory — which proves uncountable sets exist — itself has a countable model.

## How It's Best Learned
Prove the downward theorem using the Henkin construction and the fact that a countable language generates at most countably many terms. Then state the upward theorem via compactness and compare the philosophical implications.

## Common Misconceptions
- Skolem's paradox is not a contradiction: 'uncountable' is relative to a model — the countable model of set theory thinks some of its sets are uncountable because the bijection witnessing countability doesn't exist inside the model.
- The theorems do not apply to second-order logic, which can characterize the natural numbers categorically.
