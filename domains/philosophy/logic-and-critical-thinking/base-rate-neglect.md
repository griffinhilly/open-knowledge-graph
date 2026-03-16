---
id: base-rate-neglect
title: Base Rate Neglect
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: inductive-reasoning
  type: hard
- id: evaluating-evidence
  type: soft
tags:
- base-rate
- probability
- cognitive-bias
- reasoning
stage: abstract-reasoning
status: draft
---

# Base Rate Neglect

## Core Idea
Base rate neglect is the tendency to ignore prior probabilities (how common something is in the population) when evaluating specific evidence. The classic example is medical testing: a test that is 99% accurate sounds highly reliable, but if the disease affects only 1 in 10,000 people, a positive result is far more likely to be a false positive than a true positive. The prosecutor's fallacy commits the same error in legal contexts, confusing the probability of the evidence given innocence with the probability of innocence given the evidence. Correcting for base rates requires combining prior probability with the strength of new evidence — the core logic behind Bayes' theorem.

## How It's Best Learned
Work through the medical testing example with actual numbers: if 10,000 people are tested, how many true positives and false positives result? Visual aids like natural frequency trees make the math intuitive. Then apply the same reasoning to legal, security screening, and everyday probability scenarios.

## Common Misconceptions
- Thinking that a highly accurate test guarantees a correct diagnosis — accuracy must be weighed against how rare the condition is.
- Believing base rate neglect is a 'math problem' rather than a reasoning problem; the error arises from intuitive judgment, not from inability to do arithmetic.

## Explainer

From your work on inductive reasoning, you know that strong inductive arguments are those where the premises make the conclusion probable. Base rate neglect is a systematic failure of this principle — a way of reasoning that *feels* inductively strong but is actually weak because a crucial premise (the prior probability) has been ignored. The specific evidence grabs attention; the background frequency of the phenomenon quietly disappears from the calculation.

The canonical example makes the structure vivid. Suppose a disease affects 1 person in 10,000. A test for it is 99% accurate: if you have the disease, the test detects it 99% of the time; if you don't, the test is positive only 1% of the time (a false positive). You test positive. How worried should you be? Intuition says "very worried — the test is 99% accurate." But consider 10,000 people: about 1 has the disease, correctly identified by the test. Of the 9,999 healthy people, 1% — roughly 100 — also test positive. So out of approximately 101 positive results, only 1 is a true positive. The probability you actually have the disease given a positive result is roughly 1%. The test is highly accurate; you are almost certainly still healthy. This counterintuitive result is entirely driven by the **prior probability** — how rare the disease is before the test is applied.

The formal structure here is **Bayes' theorem**: the probability of a hypothesis given evidence depends on three things — the prior probability of the hypothesis (how common the disease is), the likelihood of the evidence given the hypothesis (the true positive rate), and the likelihood of the evidence overall (including false positives). Base rate neglect is the failure to weight by the prior. The evidence — a positive test — gets all the reasoning power, and the rarity of the disease gets none. When the prior is very low, even highly diagnostic evidence can barely shift the posterior probability.

The **prosecutor's fallacy** applies the same mistake in legal reasoning. A prosecutor might argue: "The probability of finding this DNA match if the defendant is innocent is 1 in a million — therefore the defendant is almost certainly guilty." But this substitutes P(evidence | innocent) for P(guilty | evidence). The latter requires knowing the base rate of the relevant profile in the population — how many people could have produced a matching sample. In a large city, even a 1-in-a-million coincidental match probability means another person might match by chance, and the posterior probability of guilt can be far lower than 1-in-a-million suggests. Recognizing base rate neglect means habitually asking: before seeing this evidence, how probable was the hypothesis? The answer always matters.
