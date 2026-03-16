---
id: law-of-total-probability
title: Law of Total Probability
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
builds-toward:
- bayes-theorem
tags:
- probability
- conditional-probability
- partitions
stage: formal-systems
status: draft
---

# Law of Total Probability

## Core Idea
If events B₁, B₂, ..., Bₙ partition the sample space, then P(A) = Σ P(A|Bᵢ)P(Bᵢ). This rule allows us to calculate the probability of an event by conditioning on all possible ways it can occur.

## How It's Best Learned
Work through examples involving disease diagnosis or quality control where you condition on a known partition. Draw tree diagrams showing all paths to the target event. Practice recognizing when this rule applies.

## Common Misconceptions
Not verifying that the events form a partition (they must be mutually exclusive and exhaustive). Forgetting to sum over all conditioning events. Confusing this with just conditional probability.

## Explainer

You know from conditional probability that P(A|B) = P(A ∩ B) / P(B), and that rearranging gives the multiplication rule P(A ∩ B) = P(A|B) · P(B). The **Law of Total Probability** builds directly on this: it asks, what if you want P(A) but it's easier to compute P(A|Bᵢ) for several different conditioning scenarios? The law says that if you have a **partition** — a collection of events B₁, B₂, …, Bₙ that are mutually exclusive (no two can happen at once) and exhaustive (one of them must happen) — then you can decompose P(A) by conditioning on each partition piece and averaging: P(A) = Σᵢ P(A|Bᵢ) · P(Bᵢ).

The geometric picture makes this transparent. Imagine the sample space as a rectangle. The partition events B₁, B₂, …, Bₙ slice the rectangle into non-overlapping vertical strips that together cover everything. Event A is some blob spread across these strips. The probability P(A) equals the sum of the slices of A within each strip — and each slice is P(A ∩ Bᵢ) = P(A|Bᵢ) · P(Bᵢ). The law is just computing the area of A by summing its area within each strip. The partition requirement ensures the strips cover the whole space with no overlaps, so you account for A exactly once everywhere.

A classic application: suppose 1% of a population has a disease, and a diagnostic test is 90% sensitive (P(positive|disease) = 0.9) and 95% specific (P(negative|no disease) = 0.95, so P(positive|no disease) = 0.05). What is the overall probability of a positive test? The events {disease} and {no disease} partition the population. So P(positive) = P(positive|disease)·P(disease) + P(positive|no disease)·P(no disease) = 0.9 · 0.01 + 0.05 · 0.99 = 0.009 + 0.0495 = 0.0585. Without the Law of Total Probability, you couldn't combine these conditional rates into an overall rate.

This law is the essential prerequisite for **Bayes' theorem**, which you'll encounter next. Bayes' theorem needs P(A) in the denominator — the "marginal probability" of the evidence — and the Law of Total Probability is exactly how you compute it. Every Bayesian calculation, from medical diagnosis to spam filtering to scientific inference, implicitly uses the Law of Total Probability to compute the denominator. Recognizing that you have a partition, identifying the pieces, and summing the weighted conditionals is the core skill — and the tree diagram is your best tool for staying organized when the partition has more than two parts.
