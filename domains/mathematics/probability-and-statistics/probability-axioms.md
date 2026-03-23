---
id: probability-axioms
title: Probability Axioms
domain: mathematics
course: probability-and-statistics
prerequisites: []
builds-toward:
- sample-spaces-and-events
- conditional-probability
- random-variables-intro
tags:
- probability
- foundations
- axioms
stage: formal-systems
status: validated
---

# Probability Axioms

## Core Idea
The three axioms of probability establish a consistent mathematical framework: (1) probabilities are non-negative real numbers; (2) the probability of the sample space is 1; (3) for disjoint events, P(A ∪ B) = P(A) + P(B). These axioms ensure that any valid probability assignment is logically consistent and provides the foundation for all probability theory.

## How It's Best Learned
Start with familiar examples (coin flips, dice) and verify that intuitive probabilities satisfy the axioms. Then explore why these axioms prevent contradictions.

## Common Misconceptions
Thinking probabilities can be negative or greater than 1. Confusing the sample space with individual outcomes.

## Questions

```yaml
- question: "If P(A) = 0.3 and P(B) = 0.5 and events A and B are disjoint (mutually exclusive), what is P(A ∪ B)?"
  type: multiple-choice
  options: ["0.15", "0.2", "0.8", "1.0"]
  answer: 2
  explanation: "By the third axiom, for disjoint events P(A ∪ B) = P(A) + P(B) = 0.3 + 0.5 = 0.8. The answer 0.15 would be P(A) × P(B), which applies to independent events under a different rule, not disjoint events under the addition axiom."

- question: "It is possible for a valid probability assignment to give P(A) = -0.1 for some event A."
  type: true-false
  answer: false
  explanation: "The first axiom of probability requires that P(A) ≥ 0 for every event A. A negative probability has no meaningful interpretation — you cannot have less than no chance of something occurring. Any assignment that violates this axiom is not a valid probability measure."

- question: "Why must the probability of the sample space equal exactly 1?"
  type: short-answer
  answer: "The sample space contains all possible outcomes of the experiment, so some outcome must always occur. An event that is certain to happen has probability 1, and since exactly one outcome in the sample space must occur, P(S) = 1."
  explanation: "The second axiom encodes the idea of certainty. When you run an experiment, something happens — one of the outcomes in S occurs. The probability of 'something happens' must be 1 (certainty). Setting P(S) = 1 ensures the entire probability 'budget' is distributed across outcomes, which in turn means all probabilities must sum to at most 1 and individual probabilities cannot exceed 1."
```

## Explainer

Before the axioms of probability were formalized by Andrei Kolmogorov in 1933, probability was an informal, intuition-driven concept. People used it to reason about dice, card games, and insurance — but there was no consensus on what rules a probability *had* to follow. Kolmogorov's contribution was to write down three simple axioms that any coherent probability assignment must satisfy, turning probability into a rigorous mathematical theory.

The setup begins with a *sample space* S — the set of all possible outcomes of some experiment. Rolling a die: S = {1, 2, 3, 4, 5, 6}. Flipping two coins: S = {HH, HT, TH, TT}. An *event* is any subset of S — for instance, "rolling an even number" is the event {2, 4, 6}. Probability is then a function P that assigns a real number to each event. The three axioms constrain which functions P are valid probability assignments.

**Axiom 1** (Non-negativity): P(A) ≥ 0 for any event A. Probabilities cannot be negative — there is no such thing as "less than no chance." **Axiom 2** (Normalization): P(S) = 1. Something must happen; the probability that we land somewhere in the sample space is 1. **Axiom 3** (Additivity): If A and B are disjoint events (they share no outcomes), then P(A ∪ B) = P(A) + P(B). If two outcomes cannot both occur, the chance of one or the other is the sum of their individual chances.

These three axioms seem minimal, but they have enormous consequences. From them alone, you can *derive* everything else in probability theory: that P(∅) = 0, that P(Aᶜ) = 1 − P(A), that P(A ∪ B) = P(A) + P(B) − P(A ∩ B) for non-disjoint events, and that probabilities of all outcomes in a finite sample space must sum to 1. None of these are additional assumptions — they follow from the three axioms by pure logic.

A useful way to internalize the axioms is to check that intuitive probability assignments satisfy them. A fair die assigns probability 1/6 to each face: each value is ≥ 0 ✓, they sum to 1 ✓, and disjoint events like "even" and "odd" add correctly (1/2 + 1/2 = 1 = P(S)) ✓. Any time you encounter a proposed probability model, verify the axioms first — they are the bare minimum that separates coherent probability reasoning from contradiction.
