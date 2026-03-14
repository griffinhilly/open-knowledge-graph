---
id: conditional-probability
title: Conditional Probability
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: hard
- id: complement-and-addition-rules
  type: soft
builds-toward:
- independence-and-multiplication-rule
- bayes-theorem
tags:
- conditional-probability
- given-that
- restricted-sample-space
stage: formal-systems
status: validated
---

# Conditional Probability

## Core Idea
Conditional probability P(A | B) is the probability of event A given that event B is known to have occurred. It is defined as P(A | B) = P(A ∩ B) / P(B), valid when P(B) > 0. Conditioning restricts the sample space to outcomes consistent with B and renormalizes. The multiplication rule follows directly: P(A ∩ B) = P(B) · P(A | B).

## How It's Best Learned
Two-way frequency tables are the clearest entry point — students can read conditional probabilities directly from the table before seeing the formula. Then connect to tree diagrams, which organize sequential conditional reasoning visually.

## Common Misconceptions
- Confusing P(A | B) with P(B | A) — the prosecutor's fallacy.
- Treating the vertical bar as division rather than as 'given that'.
- Forgetting to restrict to the conditioning event's row or column in a two-way table.
