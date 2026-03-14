---
id: cardinality-and-equinumerosity
title: Cardinality and Equinumerosity
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: injections-surjections-bijections-classification
  type: hard
builds-toward:
- finite-sets-and-natural-numbers
- countably-infinite-sets
tags:
- cardinality
- equinumerosity
- size
- bijection
stage: formal-systems
status: draft
---

# Cardinality and Equinumerosity

## Core Idea
Two sets have the same cardinality if there exists a bijection between them. This extends the notion of set size beyond finite collections to all sets, allowing meaningful comparison of infinite sets. For any two sets A and B, exactly one of |A| < |B|, |A| = |B|, or |A| > |B| holds by the Cantor-Schröder-Bernstein theorem.

## How It's Best Learned
Construct explicit bijections: f(n) = 2n shows ℕ and the even natural numbers have equal cardinality. Use Cantor-Schröder-Bernstein: if injections f: A → B and g: B → A exist, then |A| = |B|. Verify with standard pairs: ℕ ≅ ℤ ≅ ℚ.

## Common Misconceptions
- Thinking ℕ and 2ℕ have different cardinalities because 2ℕ ⊂ ℕ (they are equinumerous). - Assuming cardinality is always a number; cardinality is an equivalence class of sets. - Confusing 'same cardinality' with 'same elements'—cardinality measures size, not identity.
