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
