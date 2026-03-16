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
status: draft
---

# Probability Rules: Addition, Multiplication, and Complement

## Core Idea
The complement rule states P(A') = 1 - P(A). The addition rule gives P(A ∪ B) = P(A) + P(B) - P(A ∩ B). The multiplication rule states P(A ∩ B) = P(A)P(B|A). These rules form the foundation for all probability calculations.

## How It's Best Learned
Use Venn diagrams to visualize the addition rule. Practice with simple examples first, then move to more complex scenarios. Verify rules using simulation or physical experiments.

## Common Misconceptions
Forgetting the -P(A ∩ B) term in the addition rule when events overlap. Confusing P(A ∩ B) with P(A)P(B) without checking independence. Applying rules in wrong order or confusing union with intersection.

## Explainer

From your study of sample spaces and events, you know that a probability assigns a number between 0 and 1 to every event, and that the total probability of the sample space is exactly 1. These three rules — complement, addition, and multiplication — are the arithmetic that follows directly from that structure. Every probability calculation you will ever do reduces to some combination of them.

The **complement rule** is the simplest: P(A') = 1 − P(A). Because A and its complement A' together cover the entire sample space, and they don't overlap, their probabilities must add to 1. If there's a 30% chance of rain, there's a 70% chance of no rain. The complement rule is most useful when "the event doesn't happen" is easier to calculate than "the event does happen" — a technique that becomes essential in more advanced probability.

The **addition rule** computes the probability of A *or* B occurring: P(A ∪ B) = P(A) + P(B) − P(A ∩ B). The subtraction corrects for double-counting. Imagine a Venn diagram: the overlap region A ∩ B gets counted once in P(A) and again in P(B), so you subtract it once to get the true area of the union. When A and B are **mutually exclusive** (they share no outcomes), P(A ∩ B) = 0 and the formula simplifies to P(A) + P(B). Always ask whether events overlap before applying the rule.

The **multiplication rule** computes the probability of A *and* B both occurring: P(A ∩ B) = P(A) · P(B|A). Read this as: the probability that both happen equals the probability that A happens, times the probability that B happens *given that A already has*. This is the general form — it works whether or not A and B are related. When A and B are **independent**, knowing A occurred gives no information about B, so P(B|A) = P(B) and the formula simplifies to P(A) · P(B). Never apply the simplified form without confirming independence first.

Together, these three rules are a complete toolkit. Union problems call for the addition rule; intersection problems call for the multiplication rule; "at least one" or "none" problems typically call for the complement rule combined with one of the others. As you move toward conditional probability and independence, you will find that each of those topics is just a more nuanced application of rules you have already internalized here.
