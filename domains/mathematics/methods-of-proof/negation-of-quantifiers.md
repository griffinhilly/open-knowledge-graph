---
id: negation-of-quantifiers
title: Negation of Quantified Statements
domain: mathematics
course: methods-of-proof
prerequisites:
- id: predicates-and-quantifiers
  type: hard
builds-toward:
- proof-by-contradiction
tags:
- quantifiers
- negation
- logic
stage: formal-systems
status: draft
---

# Negation of Quantified Statements

## Core Idea
The negation of '∀x P(x)' is '∃x ¬P(x)', and the negation of '∃x P(x)' is '∀x ¬P(x)'. Understanding how negation interacts with quantifiers is essential for proof by contradiction and logical precision.

## How It's Best Learned
Practice with concrete predicates: negating 'all primes > 2 are odd' gives 'there exists a prime > 2 that is not odd'.

## Common Misconceptions
- Leaving the quantifier unchanged when negating (e.g., wrongly negating '∀x P(x)' as '∀x ¬P(x)').
- Not recognizing that one counterexample negates a universal statement.
