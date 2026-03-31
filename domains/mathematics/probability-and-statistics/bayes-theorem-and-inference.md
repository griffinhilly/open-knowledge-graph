---
id: bayes-theorem-and-inference
title: Bayes' Theorem and Statistical Inference
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
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
status: validated
---

# Bayes' Theorem and Statistical Inference

## Core Idea
Bayes' theorem: P(B_i|A)=P(A|B_i)P(B_i)/∑P(A|B_j)P(B_j). It enables updating prior beliefs P(B_i) to posterior beliefs P(B_i|A) given evidence A. This formula is foundational for statistical inference, machine learning, and decision-making under uncertainty.

## Questions

```yaml
- question: "A disease affects 1% of a population. A test for it is 95% sensitive and 95% specific. A person tests positive. What is the approximate probability they actually have the disease?"
  type: multiple-choice
  options:
    - "95%, because the test is 95% accurate"
    - "50%, because either they have the disease or they don't"
    - "About 16%, because the low disease prevalence means most positives are false positives"
    - "About 99%, because false positives are very rare with a 95% specific test"
  answer: 2
  explanation: "Using Bayes' theorem: P(disease|positive) = (0.95 × 0.01) / [(0.95 × 0.01) + (0.05 × 0.99)] ≈ 0.0095 / 0.059 ≈ 16%. Out of 10,000 people: ~100 sick (95 test positive) and ~9,900 healthy (495 false positives). Of 590 total positives, only 95 are truly sick. The low base rate (1%) means the healthy population generates far more false positives than the sick population generates true positives, even with a highly accurate test."

- question: "Which of the following correctly identifies the three components of Bayes' theorem in the medical testing context?"
  type: multiple-choice
  options:
    - "Prior = disease prevalence; Likelihood = probability of testing positive given you have the disease; Posterior = probability of having the disease given a positive test"
    - "Prior = test accuracy; Likelihood = probability of a false positive; Posterior = probability of a true negative"
    - "Prior = probability of testing positive; Likelihood = disease severity; Posterior = probability of recovery"
    - "Prior = doctor's diagnosis; Likelihood = number of tests taken; Posterior = final diagnosis"
  answer: 0
  explanation: "In Bayesian terms: the prior P(disease) encodes background knowledge — the population prevalence before any test is run. The likelihood P(positive|disease) encodes how probable a positive result is if the person is sick — the test's sensitivity. The posterior P(disease|positive) is what you should believe after seeing the evidence — the probability of disease given the positive result. Bayes' theorem computes the posterior from the prior and likelihood."

- question: "If a medical test is 95% accurate, a patient who tests positive has a 95% probability of having the disease."
  type: true-false
  answer: false
  explanation: "False. '95% accurate' describes the test's sensitivity and specificity, but the probability of actually having the disease after a positive test — the positive predictive value — depends critically on the base rate (prior probability). When a disease is rare, most positive results are false positives, even with a highly accurate test. Ignoring the prior and equating test accuracy with diagnostic probability is called the base rate fallacy, and it is one of the most common errors in probabilistic reasoning."

- question: "Bayes' theorem provides a principled method for updating a prior probability estimate when new evidence is observed."
  type: true-false
  answer: true
  explanation: "True — this is precisely what Bayes' theorem does. It takes a prior P(B), incorporates the likelihood of the observed evidence P(A|B), and produces a posterior P(B|A) that reflects updated knowledge. Each new observation can trigger another application: the previous posterior becomes the new prior. This sequential updating is the foundation of Bayesian inference and is why the framework is powerful for reasoning under uncertainty."

- question: "Why does a rare disease have a low positive predictive value even when the diagnostic test has high sensitivity and specificity? Use the concepts of prior and likelihood in your explanation."
  type: short-answer
  answer: "The positive predictive value is the posterior P(disease|positive). By Bayes' theorem, this is proportional to the likelihood P(positive|disease) multiplied by the prior P(disease). When the disease is rare, the prior is very small. Even a high likelihood (95% sensitivity) multiplied by a tiny prior produces a small numerator. The denominator also includes false positives: P(positive|healthy) × P(healthy), which is large when the healthy population is large. The result is that most positive tests come from the large healthy population, not the small sick one."
  explanation: "The prior can dominate the posterior when it is extreme. A 1% disease prevalence means 99% of the population is healthy — even a 5% false positive rate generates far more false positives from the healthy majority than true positives from the sick minority. Bayes' theorem makes this arithmetic precise and shows that 'how accurate is the test' is always a secondary question to 'how common is what we're testing for.'"
```

## Explainer

From conditional probability, you know P(B|A) = P(A ∩ B)/P(A), and from the law of total probability, you know how to expand P(A) over a partition. **Bayes' theorem** combines these two facts into a formula for *inverting* a conditional probability: if you know P(A|B), it tells you how to find P(B|A). The algebra is straightforward — P(A ∩ B) = P(A|B)P(B) = P(B|A)P(A) — but the conceptual shift is profound.

Here is the core intuition with a medical example. Suppose a disease affects 1% of the population, and a test for it is 95% sensitive (correctly identifies sick patients) and 95% specific (correctly identifies healthy patients). You test positive — what is the probability you actually have the disease? Most people guess 95%, but Bayes' theorem gives the right answer. Let B = "you have the disease" and A = "you test positive." Then:

P(B|A) = P(A|B)P(B) / [P(A|B)P(B) + P(A|not-B)P(not-B)]
       = (0.95)(0.01) / [(0.95)(0.01) + (0.05)(0.99)]
       ≈ 0.0095 / 0.0590 ≈ 16%

Even with a highly accurate test, the positive predictive value is only 16% because the disease is rare. The low **prior** P(B) = 0.01 dominates. This example illustrates the fundamental structure: the **prior** P(B) encodes your pre-evidence belief; the **likelihood** P(A|B) encodes how probable the evidence is if the hypothesis is true; and the **posterior** P(B|A) is what you should believe *after* seeing the evidence.

For statistical inference, the same logic applies with parameters instead of disease states. Suppose θ is a parameter (say, the bias of a coin) and x is observed data (say, 7 heads in 10 flips). Bayes' theorem gives: P(θ|x) ∝ P(x|θ) · P(θ). The **posterior distribution** over θ is proportional to the likelihood times the prior. This is the foundation of Bayesian statistics: instead of estimating a single point value for θ, you maintain and update an entire probability distribution over θ. Each new observation shifts the posterior, concentrating it around parameter values consistent with the data. The more data you observe, the less the prior matters and the more the likelihood dominates — in the limit, prior and posterior converge to the same answer, making Bayesian and frequentist methods agree asymptotically.
