---
id: probability-rules-for-events
title: 'Probability Rules: Addition, Multiplication, and Complement'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sample-spaces-and-events
  type: hard
builds-toward:
- independence-and-mutually-exclusive-events
- conditional-probability
tags:
- probability
- rules
- foundations
stage: formal-systems
status: validated
---

# Probability Rules: Addition, Multiplication, and Complement

## Core Idea
The complement rule states P(A') = 1 - P(A). The addition rule gives P(A ∪ B) = P(A) + P(B) - P(A ∩ B). The multiplication rule states P(A ∩ B) = P(A)P(B|A). These rules form the foundation for all probability calculations.

## How It's Best Learned
Use Venn diagrams to visualize the addition rule. Practice with simple examples first, then move to more complex scenarios. Verify rules using simulation or physical experiments.

## Common Misconceptions
Forgetting the -P(A ∩ B) term in the addition rule when events overlap. Confusing P(A ∩ B) with P(A)P(B) without checking independence. Applying rules in wrong order or confusing union with intersection.

## Questions

```yaml
- question: "A card is drawn from a standard 52-card deck. P(red) = 26/52, P(face card) = 12/52, P(red AND face card) = 6/52. What is P(red OR face card)?"
  type: multiple-choice
  options:
    - "38/52 — add P(red) and P(face card) directly"
    - "32/52 — subtract the overlap to avoid double-counting"
    - "20/52 — subtract P(red AND face card) from each term separately"
    - "6/52 — use the intersection since both conditions must hold"
  answer: 1
  explanation: "P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = 26/52 + 12/52 − 6/52 = 32/52 = 8/13. The subtraction corrects for double-counting: the 6 red face cards were included in both P(red) and P(face card), so subtracting P(A ∩ B) once restores the correct count. Option A is the most common error — forgetting the subtraction and getting 38/52, as if red and face card were mutually exclusive."

- question: "A bag contains 3 red and 7 blue marbles. You draw two marbles without replacement. A student calculates P(both red) = (3/10) × (3/10) = 9/100. What error did they make?"
  type: multiple-choice
  options:
    - "They should have added the probabilities rather than multiplied them"
    - "They applied the simplified multiplication rule P(A∩B) = P(A)·P(B) without verifying independence; draws without replacement are not independent"
    - "They used the wrong sample space — there are only 2 marbles drawn, not 10"
    - "The calculation is correct because each draw is a random event"
  answer: 1
  explanation: "P(A∩B) = P(A)·P(B) holds only when A and B are independent. Drawing without replacement makes the events dependent: after drawing one red marble, only 2 reds remain out of 9 total. The correct calculation is P(both red) = (3/10) × (2/9) = 6/90 = 1/15 ≈ 0.067, not 9/100 = 0.09. The simplified form tempts students because it's easier to apply, but it only works when independence has been confirmed."

- question: "When two events are mutually exclusive, P(A ∪ B) = P(A) + P(B), with no subtraction needed, because mutually exclusive events share no outcomes."
  type: true-false
  answer: true
  explanation: "Mutually exclusive events have P(A ∩ B) = 0 — they cannot both occur. In the addition rule P(A ∪ B) = P(A) + P(B) − P(A ∩ B), subtracting 0 changes nothing. So the simpler form P(A ∪ B) = P(A) + P(B) is valid for mutually exclusive events. However, mutual exclusivity is a special case — for overlapping events, dropping the subtraction term is a significant error."

- question: "If P(A) = 0.4 and P(B) = 0.5, then P(A ∩ B) = 0.2, because the multiplication rule gives P(A∩B) = P(A) × P(B)."
  type: true-false
  answer: false
  explanation: "P(A) × P(B) = P(A ∩ B) only when A and B are independent. Without knowing whether A and B are independent, you cannot calculate their joint probability from their individual probabilities alone. P(A ∩ B) could range anywhere from 0 (if mutually exclusive) to 0.4 (if A is a subset of B). Applying the simplified multiplication rule without confirming independence is one of the most common errors in probability."

- question: "Why does the addition rule P(A ∪ B) = P(A) + P(B) − P(A ∩ B) subtract the intersection, and when is it valid to drop that term?"
  type: short-answer
  answer: "The subtraction corrects for double-counting. Any outcome in A ∩ B gets counted once in P(A) and again in P(B), so adding P(A) + P(B) counts the overlap twice. Subtracting P(A ∩ B) once removes the extra count, giving the correct probability of the union. It is valid to drop the subtraction term only when A and B are mutually exclusive — that is, when P(A ∩ B) = 0 — because there is no overlap to correct for."
  explanation: "The Venn diagram makes this concrete: the area of two overlapping circles equals the area of circle A plus the area of circle B minus the overlapping region (otherwise counted twice). For non-overlapping circles, there is no overlap to subtract. Recognizing whether events overlap is the first step in any union probability problem."
```

## Explainer

From your study of sample spaces and events, you know that a probability assigns a number between 0 and 1 to every event, and that the total probability of the sample space is exactly 1. These three rules — complement, addition, and multiplication — are the arithmetic that follows directly from that structure. Every probability calculation you will ever do reduces to some combination of them.

The **complement rule** is the simplest: P(A') = 1 − P(A). Because A and its complement A' together cover the entire sample space, and they don't overlap, their probabilities must add to 1. If there's a 30% chance of rain, there's a 70% chance of no rain. The complement rule is most useful when "the event doesn't happen" is easier to calculate than "the event does happen" — a technique that becomes essential in more advanced probability.

The **addition rule** computes the probability of A *or* B occurring: P(A ∪ B) = P(A) + P(B) − P(A ∩ B). The subtraction corrects for double-counting. Imagine a Venn diagram: the overlap region A ∩ B gets counted once in P(A) and again in P(B), so you subtract it once to get the true area of the union. When A and B are **mutually exclusive** (they share no outcomes), P(A ∩ B) = 0 and the formula simplifies to P(A) + P(B). Always ask whether events overlap before applying the rule.

The **multiplication rule** computes the probability of A *and* B both occurring: P(A ∩ B) = P(A) · P(B|A). Read this as: the probability that both happen equals the probability that A happens, times the probability that B happens *given that A already has*. This is the general form — it works whether or not A and B are related. When A and B are **independent**, knowing A occurred gives no information about B, so P(B|A) = P(B) and the formula simplifies to P(A) · P(B). Never apply the simplified form without confirming independence first.

Together, these three rules are a complete toolkit. Union problems call for the addition rule; intersection problems call for the multiplication rule; "at least one" or "none" problems typically call for the complement rule combined with one of the others. As you move toward conditional probability and independence, you will find that each of those topics is just a more nuanced application of rules you have already internalized here.
