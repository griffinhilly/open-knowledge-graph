---
id: bayes-theorem-and-inference
title: Bayes' Theorem and Statistical Inference
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability-fundamentals
  type: hard
- id: law-of-total-probability
  type: hard
builds-toward:
- bayesian-inference-intro
- maximum-likelihood-estimation-theory
tags:
- bayes
- inference
stage: formal-systems
status: draft
---

# Bayes' Theorem and Statistical Inference

## Core Idea
Bayes' theorem: P(B_i|A)=P(A|B_i)P(B_i)/∑P(A|B_j)P(B_j). It enables updating prior beliefs P(B_i) to posterior beliefs P(B_i|A) given evidence A. This formula is foundational for statistical inference, machine learning, and decision-making under uncertainty.

## Explainer

From conditional probability, you know P(B|A) = P(A ∩ B)/P(A), and from the law of total probability, you know how to expand P(A) over a partition. **Bayes' theorem** combines these two facts into a formula for *inverting* a conditional probability: if you know P(A|B), it tells you how to find P(B|A). The algebra is straightforward — P(A ∩ B) = P(A|B)P(B) = P(B|A)P(A) — but the conceptual shift is profound.

Here is the core intuition with a medical example. Suppose a disease affects 1% of the population, and a test for it is 95% sensitive (correctly identifies sick patients) and 95% specific (correctly identifies healthy patients). You test positive — what is the probability you actually have the disease? Most people guess 95%, but Bayes' theorem gives the right answer. Let B = "you have the disease" and A = "you test positive." Then:

P(B|A) = P(A|B)P(B) / [P(A|B)P(B) + P(A|not-B)P(not-B)]
       = (0.95)(0.01) / [(0.95)(0.01) + (0.05)(0.99)]
       ≈ 0.0095 / 0.0590 ≈ 16%

Even with a highly accurate test, the positive predictive value is only 16% because the disease is rare. The low **prior** P(B) = 0.01 dominates. This example illustrates the fundamental structure: the **prior** P(B) encodes your pre-evidence belief; the **likelihood** P(A|B) encodes how probable the evidence is if the hypothesis is true; and the **posterior** P(B|A) is what you should believe *after* seeing the evidence.

For statistical inference, the same logic applies with parameters instead of disease states. Suppose θ is a parameter (say, the bias of a coin) and x is observed data (say, 7 heads in 10 flips). Bayes' theorem gives: P(θ|x) ∝ P(x|θ) · P(θ). The **posterior distribution** over θ is proportional to the likelihood times the prior. This is the foundation of Bayesian statistics: instead of estimating a single point value for θ, you maintain and update an entire probability distribution over θ. Each new observation shifts the posterior, concentrating it around parameter values consistent with the data. The more data you observe, the less the prior matters and the more the likelihood dominates — in the limit, prior and posterior converge to the same answer, making Bayesian and frequentist methods agree asymptotically.
