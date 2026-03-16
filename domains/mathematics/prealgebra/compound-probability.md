---
id: compound-probability
title: Compound Probability
domain: mathematics
course: prealgebra
prerequisites:
- id: simple-probability
  type: hard
builds-toward:
- independence-and-multiplication-rule
tags:
- probability
- compound-events
- independent
- dependent
stage: abstract-reasoning
status: validated
---
# Compound Probability

## Core Idea
Compound probability deals with the likelihood of two or more events occurring together. For independent events (where one outcome does not affect the other), multiply the individual probabilities: P(A and B) = P(A) × P(B). Flipping heads then rolling a 6 gives (1/2)(1/6) = 1/12. For dependent events (where one outcome changes the available outcomes), the second probability must account for the change: drawing two aces from a deck without replacement gives (4/52)(3/51) = 12/2652 = 1/221. Distinguishing between independent and dependent events is the critical reasoning skill at this level.

## How It's Best Learned
Use tree diagrams and organized lists to map all possible outcomes of two-event experiments. Start with clearly independent events (coin and die), then move to dependent events (drawing without replacement). Have students compare experimental results from simulations with their calculated probabilities to build intuition about why multiplication works.

## Common Misconceptions
- Assuming all compound events are independent — drawing cards without replacement makes the second draw dependent on the first.
- Adding probabilities instead of multiplying for "and" events (P(A and B) is not P(A) + P(B)).

## Explainer

You already know how to find the probability of a single event: count favorable outcomes, divide by total outcomes. Compound probability asks what happens when two events occur together or in sequence. The question that drives everything is: does the outcome of the first event change what's possible for the second?

When the answer is no, the events are **independent**. Flipping a coin and rolling a die are independent because the coin landing heads doesn't alter which faces the die can show. For independent events, the probability of both happening is found by **multiplying**: P(A and B) = P(A) × P(B). This rule has an intuitive reading — a 1/2 chance and a 1/6 chance together give (1/2)(1/6) = 1/12. Tree diagrams make this visible: each branch narrows the probability, and the final leaf is the product of all probabilities along the path to that outcome.

When the first event does change what's available for the second, the events are **dependent**. Drawing cards from a deck without replacement is the standard example. The probability the first card is an ace is 4/52. But if it is an ace, only 3 aces remain among the 51 remaining cards, so the probability the second card is also an ace is 3/51 — a different number. You must use the updated probability that reflects what happened first. The combined probability is (4/52) × (3/51) = 1/221. This is still multiplication — just with the second factor adjusted to reflect the changed situation after the first draw.

The critical skill is correctly classifying a pair of events before computing. Replacement is the usual signal: with replacement (or in genuinely separate experiments), events are independent; without replacement, drawing one item changes the pool and creates dependence. The most common error is assuming independence when events are actually dependent — which overestimates how likely joint events are, because favorable first outcomes deplete the pool for the second draw. When in doubt, ask: "After the first event, are the possibilities for the second event exactly the same as before?" If yes, multiply the original probabilities. If no, adjust the second probability first.
