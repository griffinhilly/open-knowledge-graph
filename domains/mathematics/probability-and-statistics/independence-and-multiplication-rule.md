---
id: independence-and-multiplication-rule
title: Independence and the Multiplication Rule
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
builds-toward:
- bayes-theorem
- binomial-distribution
- geometric-distribution
tags:
- independence
- multiplication-rule
- independent-events
stage: formal-systems
status: validated
---

# Independence and the Multiplication Rule

## Core Idea
Two events A and B are independent if P(A | B) = P(A) — knowing B occurred gives no information about A. Equivalently, A and B are independent if and only if P(A ∩ B) = P(A) · P(B). This multiplication rule extends to sequences: for n independent events, P(A₁ ∩ A₂ ∩ … ∩ Aₙ) = P(A₁) · P(A₂) · … · P(Aₙ). Independence is a model assumption that must be justified, not assumed automatically.

## How It's Best Learned
Use coin flips and card draws with replacement vs. without replacement to illustrate the difference between independent and dependent events. Emphasize verifying independence algebraically using the product rule, not just intuition.

## Common Misconceptions
- The gambler's fallacy: believing prior coin flips influence future ones.
- Confusing independence with mutual exclusivity — mutually exclusive non-trivial events are actually dependent.
- Assuming physical separation of events implies statistical independence.
