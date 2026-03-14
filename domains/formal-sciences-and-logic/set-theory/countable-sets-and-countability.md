---
id: countable-sets-and-countability
title: Countable Sets and Enumeration
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: bijections-establish-equinumerosity
  type: hard
- id: naive-set-theory
  type: hard
builds-toward:
- infinite-cardinal-numbers
- aleph-numbers
tags:
- countability
- enumeration
- cardinality
- infinity
stage: formal-systems
status: draft
---

# Countable Sets and Enumeration

## Core Idea
A set is countably infinite if it is equinumerous with the natural numbers ℕ. Countable sets can be listed in a sequence, though the listing may not terminate. Countable unions of countable sets remain countable, and many 'familiar' infinite sets (ℤ, ℚ, ℕ×ℕ) are countable.

## How It's Best Learned
Use explicit bijections: pair ℤ with ℕ via n ↔ ⌊n/2⌋·(-1)^(n mod 2). Show ℚ is countable via Cantor's diagonal enumeration. Prove closure under countable unions.

## Common Misconceptions
- Confusing countable with finite; countably infinite is still infinite.
- Thinking all infinite sets are countable (leads to surprise at uncountability).
