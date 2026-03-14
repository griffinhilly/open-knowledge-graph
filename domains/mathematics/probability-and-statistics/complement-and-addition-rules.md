---
id: complement-and-addition-rules
title: Complement Rule and Addition Rule
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: hard
builds-toward:
- conditional-probability
- bayes-theorem
tags:
- complement-rule
- addition-rule
- mutually-exclusive
- probability-rules
stage: formal-systems
status: validated
---

# Complement Rule and Addition Rule

## Core Idea
The complement rule states P(Aᶜ) = 1 − P(A), useful when the complement is easier to compute than the event itself. The general addition rule is P(A ∪ B) = P(A) + P(B) − P(A ∩ B), which corrects for double-counting the intersection. When A and B are mutually exclusive (P(A ∩ B) = 0), this simplifies to P(A ∪ B) = P(A) + P(B).

## How It's Best Learned
Use Venn diagrams to make the double-counting in the addition rule visual. The complement rule is especially powerful for 'at least one' problems — computing P(none) is often simpler than summing multiple cases.

## Common Misconceptions
- Applying the simplified addition rule (without subtracting intersection) when events are not mutually exclusive.
- Confusing 'mutually exclusive' with 'complementary' — complementary events must together exhaust S and are a special case of mutually exclusive.
