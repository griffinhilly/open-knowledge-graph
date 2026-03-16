---
id: probability-with-combinatorics
title: Probability with Combinatorics
domain: mathematics
course: algebra-2
prerequisites:
- id: combinations
  type: hard
- id: permutations
  type: hard
- id: binomial-theorem
  type: soft
builds-toward:
- normal-distribution-intro
tags:
- probability
- combinatorics
- counting
- applications
stage: abstract-reasoning
status: validated
---
# Probability with Combinatorics

## Core Idea
When outcomes are equally likely, probability = (favorable outcomes)/(total outcomes). Combinatorics provides the tools to count both. Examples: probability of being dealt a certain poker hand, winning a lottery, or selecting a committee with specific composition. The key skill is translating a probability question into a counting problem, then applying permutations and combinations to compute both numerator and denominator.

## How It's Best Learned
Start with simple examples (drawing cards, rolling dice) where counting is manageable. Progress to more complex scenarios requiring combinations (poker hands, committee selections with constraints). Practice decomposing compound events using multiplication and addition principles. Introduce complementary counting: P(event) = 1 - P(not event).

## Common Misconceptions
- Counting the same outcome multiple times (overcounting due to order confusion).
- Using permutations when combinations are needed (or vice versa), leading to incorrect probabilities.
- Forgetting to account for the total sample space correctly.
- Thinking probability can exceed 1 (always check that the answer is between 0 and 1).

## Explainer

Probability measures how often an event occurs among all equally likely outcomes. When outcomes are equally likely, the formula P(event) = (favorable outcomes) / (total outcomes) is simple — but the challenge is the counting. That is exactly what you built permutations and combinations to do. Combining these tools lets you solve probability problems that would be impossible to count by hand.

Consider the probability of being dealt a specific poker hand from a 52-card deck. The **total** number of 5-card hands is C(52, 5) = 2,598,960. For a full house (three of one rank, two of another): choose the rank for the triple (13 ways), choose 3 suits for it (C(4,3) = 4), choose the rank for the pair (12 remaining ranks), choose 2 suits for it (C(4,2) = 6). Total favorable = 13 × 4 × 12 × 6 = 3,744. So P(full house) = 3,744 / 2,598,960 ≈ 0.00144. The formula is two lines; the work is methodical combinatorics.

The critical decision at every step is **whether order matters**. "How many ways can 3 committee members be chosen from 10?" — order doesn't matter, use C(10,3) = 120. "How many ways can a president, vice-president, and treasurer be chosen from 10?" — order matters (president ≠ vice-president), use P(10,3) = 720. Confusing the two inflates or deflates your count by a factor of k!, the number of orderings of k objects. Since this factor appears in both numerator and denominator of many probability calculations, the errors cancel sometimes but not always — don't rely on that.

A powerful shortcut is **complementary counting**: P(at least one) = 1 − P(none at all). The probability of drawing at least one ace in a 5-card hand is messy to compute directly (separate cases for 1, 2, 3, 4 aces). But P(no aces) = C(48,5) / C(52,5) = 1,712,304 / 2,598,960 ≈ 0.659, so P(at least one ace) ≈ 0.341 — one clean calculation. Whenever "at least one" appears in a problem, complement is almost always the efficient path. The same logic applies to "at least two," "at least three," and other lower-bounded counts.
