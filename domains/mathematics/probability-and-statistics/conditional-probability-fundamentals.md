---
id: conditional-probability-fundamentals
title: Conditional Probability Fundamentals
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms-and-rules
  type: hard
builds-toward:
- bayes-theorem
- independence-of-events
tags:
- conditional
- probability
stage: formal-systems
status: draft
---

# Conditional Probability Fundamentals

## Core Idea
Conditional probability P(A|B)=P(A∩B)/P(B) measures the probability of A given that B has occurred. The law of total probability states P(A)=∑P(A|B_i)P(B_i) over a partition {B_i}. Conditional probability formalizes how information updates our beliefs.

## Explainer

You've learned the **probability axioms**: probabilities are non-negative, the full sample space has probability 1, and disjoint events have additive probabilities. Conditional probability is the tool that lets you update probabilities when you learn new information. The key idea: if you know event B has occurred, you're no longer working with the full sample space — you've restricted your attention to the outcomes where B is true. Conditional probability renormalizes your probabilities to fit this smaller space.

Formally, **P(A|B) = P(A ∩ B) / P(B)**: the probability of A given B is the fraction of B's probability that also lies in A. Picture a Venn diagram: B is a region of the sample space; within B, the region also in A is A ∩ B. Conditioning on B means zooming in on B and asking what fraction of it is A. The denominator P(B) rescales so that probabilities within the conditioned space still sum to 1. If A and B have no overlap, P(A|B) = 0 — knowing B makes A impossible. If A contains all of B, P(A|B) = 1 — knowing B guarantees A.

The **law of total probability** is conditional probability used in reverse. If {B₁, B₂, ..., Bₙ} partition the sample space (they're mutually exclusive and cover everything), then P(A) = Σ P(A|Bᵢ) · P(Bᵢ). The intuition: every way that A can happen passes through exactly one Bᵢ, so you sum up the contributions from each scenario, weighted by how likely each scenario is. For example, a factory has two machines: Machine 1 makes 60% of items with a 2% defect rate; Machine 2 makes 40% with a 5% defect rate. P(defect) = (0.02)(0.60) + (0.05)(0.40) = 0.012 + 0.020 = 0.032 — a weighted average over the partition of machines.

Conditional probability is the gateway to **Bayes' theorem**, which you'll encounter next. Bayes' theorem is nothing more than applying the definition twice: P(B|A) = P(A|B) P(B) / P(A). Everything in Bayesian reasoning — updating a prior belief with new evidence, reversing the direction of conditioning — builds on P(A|B) = P(A ∩ B)/P(B). The algebra is simple; the skill is reading a problem, identifying which event is being conditioned on, and correctly translating sentences like "given that we drew a red ball" into a conditioning statement. Practice setting up these problems carefully: define the sample space, identify A and B, and apply the formula.
