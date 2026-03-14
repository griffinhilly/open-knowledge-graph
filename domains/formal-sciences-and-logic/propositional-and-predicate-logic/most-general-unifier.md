---
id: most-general-unifier
title: Most General Unifier (MGU)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: substitution-and-unification
  type: hard
builds-toward:
- ground-instances-and-instantiation
tags:
- first-order-logic
- unification
- automated-reasoning
stage: formal-systems
status: draft
---

# Most General Unifier (MGU)

## Core Idea
A substitution θ is a unifier of two terms if θ(s) = θ(t); a most general unifier (MGU) is a unifier such that any other unifier is an instance of it. The MGU, when it exists, is unique up to variable renaming and is the key operation enabling the resolution rule in first-order logic to work effectively.
