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
