---
id: independence-and-mutually-exclusive-events
title: Independence and Mutually Exclusive Events
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-rules-for-events
  type: hard
- id: conditional-probability
  type: hard
builds-toward:
- joint-probability-distributions
- conditional-distributions-of-random-variables
tags:
- probability
- independence
stage: formal-systems
status: draft
---

# Independence and Mutually Exclusive Events

## Core Idea
Two events are mutually exclusive if they cannot occur together (P(A ∩ B) = 0). Two events are independent if knowing one occurred doesn't change the probability of the other (P(A|B) = P(A)). These are distinct concepts—mutually exclusive events are actually dependent.

## How It's Best Learned
Compare concrete examples: drawing two cards with and without replacement, weather events, etc. Use conditional probability to check independence. Create Venn diagrams showing overlap (or lack thereof).

## Common Misconceptions
Thinking mutually exclusive events are independent. Assuming events are independent without checking. Confusing 'disjoint' with 'uncorrelated'. Not recognizing that P(A ∩ B) = P(A)P(B) is a test for independence.

## Explainer

You've worked with **conditional probability**: P(A|B) = P(A ∩ B) / P(B), the probability of A given that B has occurred. This is the right tool to understand **independence**, which is not about how events look on a Venn diagram but about whether one event provides information about the other. Events A and B are **independent** if P(A|B) = P(A) — learning that B occurred doesn't change your probability for A. Substituting the conditional probability formula, this is equivalent to P(A ∩ B) = P(A) · P(B): the **product rule for independent events**. This product rule is the operational definition and the test you use in practice.

**Mutually exclusive events** are a completely different concept. A and B are mutually exclusive (or **disjoint**) if they cannot both occur: P(A ∩ B) = 0. On a Venn diagram, the circles don't overlap. Examples: rolling a 3 and rolling a 5 on a single die; winning first place and winning second place in the same race. The addition rule for disjoint events is P(A ∪ B) = P(A) + P(B), with no overlap to subtract. Disjoint events may look "unrelated" on a diagram, but they are not independent in the probabilistic sense.

Here is the crucial insight: **mutually exclusive events with nonzero probability are always dependent**. If P(A) > 0 and P(B) > 0 but P(A ∩ B) = 0, then P(A|B) = P(A ∩ B)/P(B) = 0/P(B) = 0 ≠ P(A). Knowing B occurred completely rules out A — that is maximally informative, the opposite of independence. The confusion arises from conflating "these events don't overlap" (disjoint) with "these events have nothing to do with each other" (independent). In probability, "nothing to do with each other" means observing one gives zero information about the other — which requires the product rule P(A ∩ B) = P(A)P(B) > 0, impossible for disjoint events (unless one has probability 0).

Independence extends naturally to more than two events: A₁, ..., Aₙ are **mutually independent** if *every subset* satisfies the product rule, not just pairs. **Pairwise independence** does not imply mutual independence — you can construct three events that are pairwise independent but where all three occurring together violates the product rule. For practical situations: events defined by draws from separate random processes (coin flips, draws with replacement, measurements on different individuals) are typically independent. Events sharing a common underlying mechanism or drawing from the same pool without replacement are typically dependent. When in doubt, check the product rule directly rather than relying on intuition.
