---
id: independence-and-multiplication-rule
title: Independence and the Multiplication Rule
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
- id: probability-axioms
  type: hard
builds-toward:
- compound-probability
- binomial-distribution
- random-variables-intro
tags:
- independence
- multiplication-rule
- dependent-events
stage: formal-systems
status: draft
---

# Independence and the Multiplication Rule

## Core Idea
Two events A and B are independent if P(A|B) = P(A), meaning knowledge of B does not change the probability of A. For independent events, P(A ∩ B) = P(A) × P(B). The multiplication rule generalizes to: P(A ∩ B) = P(A) × P(B|A) for any events, which is essential for computing probabilities of sequences of outcomes.

## How It's Best Learned
Contrast independent scenarios (flipping two coins) with dependent ones (drawing cards without replacement). Verify independence by checking if P(A|B) = P(A).

## Common Misconceptions
Assuming events are independent when they are not (e.g., weather today and tomorrow). Confusing 'mutually exclusive' with 'independent'.
