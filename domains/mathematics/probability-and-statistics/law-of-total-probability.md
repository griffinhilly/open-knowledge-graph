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
status: validated
---

# Law of Total Probability

## Core Idea
If events B₁, B₂, ..., Bₙ partition the sample space, then P(A) = Σ P(A|Bᵢ)P(Bᵢ). This rule allows us to calculate the probability of an event by conditioning on all possible ways it can occur.

## How It's Best Learned
Work through examples involving disease diagnosis or quality control where you condition on a known partition. Draw tree diagrams showing all paths to the target event. Practice recognizing when this rule applies.

## Common Misconceptions
Not verifying that the events form a partition (they must be mutually exclusive and exhaustive). Forgetting to sum over all conditioning events. Confusing this with just conditional probability.

## Questions

```yaml
- question: "A disease affects 1% of a population. A test is 90% sensitive (P(positive|disease) = 0.90) and 95% specific (P(negative|no disease) = 0.95). What is the overall probability that a randomly chosen person tests positive?"
  type: multiple-choice
  options:
    - "90%, because the test is 90% accurate for people with the disease"
    - "5.85%, by summing weighted conditional probabilities over the disease/no-disease partition"
    - "1%, because only 1% of the population has the disease"
    - "47.5%, by averaging the sensitivity and false-positive rate"
  answer: 1
  explanation: "The events {disease} and {no disease} partition the population. By the Law of Total Probability: P(positive) = P(positive|disease)·P(disease) + P(positive|no disease)·P(no disease) = 0.90·0.01 + 0.05·0.99 = 0.009 + 0.0495 = 0.0585. Option A is the most tempting wrong answer — it mistakes the conditional rate P(positive|disease) for the unconditional rate P(positive), ignoring that most of the population is disease-free and the false-positive rate dominates."

- question: "You want to apply the Law of Total Probability to compute P(A). Which condition on your conditioning events B₁, B₂, B₃ is strictly required?"
  type: multiple-choice
  options:
    - "The events must be independent of A"
    - "The events must cover at least half the sample space"
    - "The events must be mutually exclusive and together cover the entire sample space"
    - "Each event must have equal probability"
  answer: 2
  explanation: "The Law of Total Probability requires a partition: the Bᵢ must be mutually exclusive (no overlap — they can't both occur) AND exhaustive (they cover the whole sample space — one of them must occur). If the Bᵢ overlap, you double-count the probability of A in the overlap region. If they don't cover the whole space, you miss the contribution of A in the uncovered region. Equal probability (option D) is irrelevant — unequal partition pieces work fine. Independence from A (option A) is not required at all."

- question: "If events B₁, B₂, …, Bₙ form a partition of the sample space, then the sum P(B₁) + P(B₂) + … + P(Bₙ) must equal 1."
  type: true-false
  answer: true
  explanation: "This follows directly from the partition definition. The Bᵢ are mutually exclusive (no overlaps) and exhaustive (they cover the entire sample space). Since probability is additive over disjoint events and the Bᵢ cover everything, their probabilities must sum to exactly 1. This is also why the Law of Total Probability works: you are computing a weighted average of the conditional probabilities P(A|Bᵢ), with weights P(Bᵢ) that sum to 1, so the result is a valid probability."

- question: "The Law of Total Probability applies to any collection of events B₁, …, Bₙ so long as they are mutually exclusive — it does not matter whether they cover the entire sample space."
  type: true-false
  answer: false
  explanation: "Both conditions are required: mutual exclusivity AND exhaustiveness. If the events are mutually exclusive but don't cover the full sample space, then Σ P(A|Bᵢ)·P(Bᵢ) will undercount P(A) — it misses the probability contributed by outcomes outside all the Bᵢ. For example, if B₁ = {even numbers} and B₂ = {multiples of 3} in a roll of a die, these are not mutually exclusive (6 is in both) and don't exhaust the space. You must have a true partition to apply the law correctly."

- question: "Why must the conditioning events form a partition (both mutually exclusive and exhaustive) for the Law of Total Probability to yield the correct answer? What goes wrong if each condition is violated separately?"
  type: short-answer
  answer: "Mutual exclusivity ensures no double-counting: if two Bᵢ events can both occur, the probability of A ∩ Bᵢ ∩ Bⱼ would be added twice. Exhaustiveness ensures complete coverage: if some outcomes belong to no Bᵢ, the probability of A in that uncovered region is missed entirely. Together, the partition carves the sample space into non-overlapping strips that together account for all of probability — so summing the contributions P(A|Bᵢ)·P(Bᵢ) adds up to P(A) exactly once."
  explanation: "The geometric picture makes this clear: think of the sample space as a rectangle. A partition divides it into non-overlapping strips that together tile the whole rectangle. Event A is a blob that crosses these strips; P(A) equals the sum of A's area in each strip, which is exactly Σ P(A∩Bᵢ) = Σ P(A|Bᵢ)·P(Bᵢ). Overlapping strips would count some area of A twice; gaps would miss some area of A. Both conditions are load-bearing."
```

## Explainer

You know from conditional probability that P(A|B) = P(A ∩ B) / P(B), and that rearranging gives the multiplication rule P(A ∩ B) = P(A|B) · P(B). The **Law of Total Probability** builds directly on this: it asks, what if you want P(A) but it's easier to compute P(A|Bᵢ) for several different conditioning scenarios? The law says that if you have a **partition** — a collection of events B₁, B₂, …, Bₙ that are mutually exclusive (no two can happen at once) and exhaustive (one of them must happen) — then you can decompose P(A) by conditioning on each partition piece and averaging: P(A) = Σᵢ P(A|Bᵢ) · P(Bᵢ).

The geometric picture makes this transparent. Imagine the sample space as a rectangle. The partition events B₁, B₂, …, Bₙ slice the rectangle into non-overlapping vertical strips that together cover everything. Event A is some blob spread across these strips. The probability P(A) equals the sum of the slices of A within each strip — and each slice is P(A ∩ Bᵢ) = P(A|Bᵢ) · P(Bᵢ). The law is just computing the area of A by summing its area within each strip. The partition requirement ensures the strips cover the whole space with no overlaps, so you account for A exactly once everywhere.

A classic application: suppose 1% of a population has a disease, and a diagnostic test is 90% sensitive (P(positive|disease) = 0.9) and 95% specific (P(negative|no disease) = 0.95, so P(positive|no disease) = 0.05). What is the overall probability of a positive test? The events {disease} and {no disease} partition the population. So P(positive) = P(positive|disease)·P(disease) + P(positive|no disease)·P(no disease) = 0.9 · 0.01 + 0.05 · 0.99 = 0.009 + 0.0495 = 0.0585. Without the Law of Total Probability, you couldn't combine these conditional rates into an overall rate.

This law is the essential prerequisite for **Bayes' theorem**, which you'll encounter next. Bayes' theorem needs P(A) in the denominator — the "marginal probability" of the evidence — and the Law of Total Probability is exactly how you compute it. Every Bayesian calculation, from medical diagnosis to spam filtering to scientific inference, implicitly uses the Law of Total Probability to compute the denominator. Recognizing that you have a partition, identifying the pieces, and summing the weighted conditionals is the core skill — and the tree diagram is your best tool for staying organized when the partition has more than two parts.
