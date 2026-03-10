---
id: well-ordering-theorem
title: Well-Ordering Theorem
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: von-neumann-ordinals
  type: hard
- id: axiom-of-choice
  type: hard
- id: partial-orders
  type: soft
- id: well-ordering-principle
  type: soft
builds-toward:
- infinite-cardinal-numbers
- cardinal-arithmetic
tags:
- well-ordering
- axiom of choice
- Zermelo
- ordinals
- equivalents
stage: formal-systems
status: draft
---

# Well-Ordering Theorem

## Core Idea
The well-ordering theorem (Zermelo, 1904) states that every set can be well-ordered — given any set A, there exists a linear order on A such that every non-empty subset has a least element. This theorem is equivalent to the axiom of choice over ZF: each implies the other. The well-ordering theorem implies that every set's cardinality can be compared with any other (the infinite cardinals are linearly ordered), and it provides the basis for defining cardinal numbers as initial ordinals. The proof applies a choice function to successively pick elements via transfinite recursion until the set is exhausted.

## How It's Best Learned
Study both directions of the equivalence: AC implies well-ordering (use a choice function to define a well-ordering by transfinite recursion), and well-ordering implies AC (use the well-ordering to define a choice function). The forward direction makes explicit why AC is essential — the well-ordering of ℝ is non-constructive.

## Common Misconceptions
- A well-ordering of ℝ cannot be exhibited explicitly — it exists non-constructively but no specific example can be written down.
- The usual order ≤ on ℝ is NOT a well-order: the open interval (0,1) has no least element under the usual order.
