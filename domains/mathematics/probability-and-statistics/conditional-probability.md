---
id: conditional-probability
title: Conditional Probability
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: hard
- id: sample-spaces-and-events
  type: hard
builds-toward:
- independence-and-multiplication-rule
- law-of-total-probability
- bayes-theorem
tags:
- conditional
- probability
- dependence
stage: formal-systems
status: validated
---

# Conditional Probability

## Core Idea
Conditional probability P(A|B) is the probability of event A given that event B has occurred. It is defined as P(A|B) = P(A ∩ B) / P(B) when P(B) > 0. Conditioning on new information updates the sample space to only those outcomes where the conditioning event occurred, rescaling probabilities accordingly.

## Questions

```yaml
- question: "A bag contains 3 red balls and 2 blue balls. You draw one ball and observe it is red. Without replacing it, what is the probability the next draw is also red?"
  type: multiple-choice
  options: ["3/5", "1/2", "2/5", "3/10"]
  answer: 1
  explanation: "After seeing the first ball is red, the sample space shrinks to all outcomes where that happened. Now 4 balls remain (2 red, 2 blue), so P(2nd red | 1st red) = 2/4 = 1/2. Using the formula: P(both red) = (3/5)(2/4) = 6/20, P(1st red) = 3/5 = 12/20, so P(A|B) = (6/20)/(12/20) = 1/2."

- question: "For any two events A and B with P(A) > 0 and P(B) > 0, it is always true that P(A|B) = P(B|A)."
  type: true-false
  answer: false
  explanation: "P(A|B) = P(A∩B)/P(B) and P(B|A) = P(A∩B)/P(A). These are equal only when P(A) = P(B). Consider: P(ground is wet | it is raining) is very high, but P(it is raining | ground is wet) is lower because sprinklers or other causes can also wet the ground. This asymmetry is the core insight behind Bayes' theorem."

- question: "Explain in your own words why the formula P(A|B) = P(A∩B)/P(B) divides by P(B)."
  type: short-answer
  answer: "Dividing by P(B) rescales the probabilities of the remaining outcomes (those inside B) so they sum to 1, forming a valid probability distribution on the restricted sample space."
  explanation: "When we condition on B, we discard all outcomes where B did not occur. The outcomes in A∩B now represent the only relevant cases, but their probabilities originally summed to P(B), not 1. Dividing by P(B) rescales them to form a proper probability distribution. Without this rescaling, the conditional probabilities would not sum to 1 and would violate the probability axioms."
```

## Explainer

From probability-axioms, you know that every event has a probability between 0 and 1 and that all outcomes in the sample space sum to 1. Conditional probability extends this framework: when new information arrives, it eliminates outcomes that are no longer possible and forces us to rescale the remaining probabilities so they still sum to 1.

The formal definition is P(A|B) = P(A ∩ B) / P(B). To see why this makes sense, imagine rolling a fair six-sided die. The full sample space is {1, 2, 3, 4, 5, 6}. If you learn the result is even (event B = {2, 4, 6}), the outcomes 1, 3, 5 are impossible — your effective sample space shrinks to {2, 4, 6}. Now, what is the probability the result exceeds 4 (event A = {5, 6})? Among the even outcomes only 6 qualifies, so P(A|B) = 1/3. Verify with the formula: P(A ∩ B) = P({6}) = 1/6 and P(B) = 3/6 = 1/2, so P(A|B) = (1/6)/(1/2) = 1/3. The formula performs exactly the "shrink then rescale" operation geometrically.

A critical misconception to avoid: P(A|B) is generally not equal to P(B|A). Consider a diagnostic test: P(positive test | disease) might be 0.95, meaning the test is sensitive. But P(disease | positive test) — the probability you actually have the disease given a positive result — depends heavily on how rare the disease is in the population. If only 1 in 1000 people have it, most positives will be false alarms even with a 95%-sensitive test. This asymmetry is so counterintuitive that it surprises even trained professionals, and it is the engine behind Bayes' theorem, which you will encounter next.

Conditional probability also gives a formal definition of independence. Two events A and B are independent exactly when P(A|B) = P(A) — knowing B occurred gives no information about A. Equivalently, P(A ∩ B) = P(A)P(B). You may have encountered independence informally before; conditional probability is what makes the definition precise. When conditioning on B has no effect on A's probability, the events are truly unrelated in a probabilistic sense.
