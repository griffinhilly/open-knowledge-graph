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
status: draft
---

# Conditional Probability

## Core Idea
Conditional probability P(A|B) is the probability of event A given that event B has occurred. It is defined as P(A|B) = P(A ∩ B) / P(B) when P(B) > 0. Conditioning on new information updates the sample space to only those outcomes where the conditioning event occurred, rescaling probabilities accordingly.
