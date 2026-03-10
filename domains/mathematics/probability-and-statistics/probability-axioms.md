---
id: probability-axioms
title: Probability Axioms and Sample Spaces
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: simple-probability
  type: hard
- id: set-theory-basics
  type: soft
builds-toward:
- complement-and-addition-rules
- conditional-probability
- random-variables-intro
tags:
- probability-axioms
- sample-space
- events
- kolmogorov
- set-theory
stage: formal-systems
status: draft
---

# Probability Axioms and Sample Spaces

## Core Idea
A sample space S is the set of all possible outcomes of a random experiment, and an event is any subset of S. Kolmogorov's three axioms define probability formally: (1) P(A) ≥ 0 for all events A; (2) P(S) = 1; (3) for mutually exclusive events, P(A ∪ B) = P(A) + P(B). All other probability rules follow logically from these axioms, making them the foundation of the entire theory.

## How It's Best Learned
Begin with concrete experiments (dice, cards, coins) and explicitly list sample spaces. Then formalize: which subsets count as events? Derive complement rule and addition rule as theorems from the axioms. This bridges students' intuitive probability sense to a rigorous framework.

## Common Misconceptions
- Assuming all outcomes in a sample space are equally likely — they need not be.
- Confusing mutually exclusive events with independent events.
- Thinking the sample space must be finite — it can be countably or uncountably infinite.
