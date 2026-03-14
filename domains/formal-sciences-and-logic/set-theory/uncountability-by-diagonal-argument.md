---
id: uncountability-by-diagonal-argument
title: Uncountability and the Diagonal Argument
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: countable-sets-and-countability
  type: hard
- id: cantor-theorem
  type: soft
builds-toward:
- continuum-hypothesis
- cardinality-hierarchy-uncountable
tags:
- uncountability
- diagonal-argument
- cardinality
- reals
stage: formal-systems
status: draft
---

# Uncountability and the Diagonal Argument

## Core Idea
The real numbers ℝ are uncountable, meaning no bijection with ℕ exists. Cantor's diagonal argument proves this: assume an enumeration of reals exists, then construct a new real (via the diagonal) that contradicts the enumeration. This technique generalizes to show the power set P(X) is always larger than X.

## How It's Best Learned
Work through the decimal-expansion version: list assumed sequence of reals as infinite decimals, modify the diagonal to create a real not on the list. Verify this works even with overcounting concerns (address the 0.999... = 1 subtlety).

## Common Misconceptions
- Thinking uncountable means 'not enumerable' is trivial; the proof's cleverness lies in the self-referential construction.
- Conflating 'no bijection with ℕ' with 'strictly larger'—must use Cantor-Bernstein to justify the latter.
