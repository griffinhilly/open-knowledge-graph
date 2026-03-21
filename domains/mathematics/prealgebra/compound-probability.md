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

## Questions

```yaml
- question: "A bag contains 5 red marbles and 3 blue marbles. You draw one marble, it is red, and you do not replace it. What is the probability the next marble drawn is also red?"
  type: multiple-choice
  options:
    - "5/8 — the same probability as the first draw, because marble color doesn't change"
    - "4/7 — one red marble was removed, leaving 4 red among 7 remaining"
    - "5/7 — the red marble was counted once already, so we keep the same numerator"
    - "4/8 — one marble was removed, so we reduce only the total"
  answer: 1
  explanation: "Without replacement, the first draw changes the available pool. After drawing one red marble, 4 red marbles remain among 7 total, giving a probability of 4/7. Option A (5/8) is the classic independence error — treating this dependent event as if nothing changed. Option D (4/8) is wrong because both the numerator (remaining red marbles) and the denominator (remaining total) must update: one marble was removed, so both change."

- question: "Which of the following pairs of events is dependent?"
  type: multiple-choice
  options:
    - "Rolling a 4 on a number cube, then flipping tails on a coin"
    - "Drawing an ace from a standard deck without replacing it, then drawing another ace"
    - "Spinning a spinner and then rolling a die"
    - "Randomly picking a number from 1–10 and then flipping a coin"
  answer: 1
  explanation: "Events are dependent when the first outcome changes the probabilities for the second. Drawing cards without replacement is the canonical example: after drawing one ace (probability 4/52), only 3 aces remain among 51 cards, so the second draw's probability (3/51) is different from the first. The other pairs all involve genuinely separate experiments — a die roll cannot affect a coin flip, and a spinner cannot affect a die — so they are independent."

- question: "For two independent events A and B, the probability that both occur equals P(A) multiplied by P(B)."
  type: true-false
  answer: true
  explanation: "This is the multiplication rule for independent events. Independence means the outcome of A doesn't affect the probability of B, so the joint probability is simply the product of individual probabilities. For example, a coin flip (1/2) and a die roll showing 6 (1/6) together have probability (1/2)(1/6) = 1/12. Each branch in a probability tree narrows the probability multiplicatively — the final leaf is the product of all probabilities along the path."

- question: "To find the probability that both event A and event B occur, you add their individual probabilities: P(A and B) = P(A) + P(B)."
  type: true-false
  answer: false
  explanation: "Adding probabilities gives the probability of A OR B occurring (with adjustment for overlap), not A AND B. The 'and' (joint) probability uses multiplication for independent events, not addition. Adding P(A) + P(B) will always produce a value larger than P(A and B) and can even exceed 1. The confusion between 'and' (multiply) and 'or' (add) is one of the most common errors in compound probability."

- question: "A standard deck has 52 cards, 13 of which are hearts. You draw two cards without replacement. Explain why the second draw's probability is different from the first, and calculate the probability that both cards are hearts."
  type: short-answer
  answer: "The first draw changes the deck: if the first card is a heart, only 12 hearts remain among 51 cards. The events are dependent because sampling without replacement alters the pool for the second draw. P(both hearts) = (13/52) × (12/51) = 156/2652 = 1/17. If the first card were not a heart, the second probability would change differently — which is why the dependency must be accounted for before computing."
  explanation: "This problem illustrates why classifying events as dependent or independent is the essential first step. Using the original 13/52 for both draws (the independence error) would give (13/52)² = 169/2704 ≈ 1/16, which is too large — it overestimates the probability by treating the second draw as if the first never happened. The correct answer updates the numerator and denominator to reflect the changed situation."
```

## Explainer

You already know how to find the probability of a single event: count favorable outcomes, divide by total outcomes. Compound probability asks what happens when two events occur together or in sequence. The question that drives everything is: does the outcome of the first event change what's possible for the second?

When the answer is no, the events are **independent**. Flipping a coin and rolling a die are independent because the coin landing heads doesn't alter which faces the die can show. For independent events, the probability of both happening is found by **multiplying**: P(A and B) = P(A) × P(B). This rule has an intuitive reading — a 1/2 chance and a 1/6 chance together give (1/2)(1/6) = 1/12. Tree diagrams make this visible: each branch narrows the probability, and the final leaf is the product of all probabilities along the path to that outcome.

When the first event does change what's available for the second, the events are **dependent**. Drawing cards from a deck without replacement is the standard example. The probability the first card is an ace is 4/52. But if it is an ace, only 3 aces remain among the 51 remaining cards, so the probability the second card is also an ace is 3/51 — a different number. You must use the updated probability that reflects what happened first. The combined probability is (4/52) × (3/51) = 1/221. This is still multiplication — just with the second factor adjusted to reflect the changed situation after the first draw.

The critical skill is correctly classifying a pair of events before computing. Replacement is the usual signal: with replacement (or in genuinely separate experiments), events are independent; without replacement, drawing one item changes the pool and creates dependence. The most common error is assuming independence when events are actually dependent — which overestimates how likely joint events are, because favorable first outcomes deplete the pool for the second draw. When in doubt, ask: "After the first event, are the possibilities for the second event exactly the same as before?" If yes, multiply the original probabilities. If no, adjust the second probability first.
