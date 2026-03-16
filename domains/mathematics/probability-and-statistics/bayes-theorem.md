---
id: bayes-theorem
title: Bayes' Theorem
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability
  type: hard
- id: law-of-total-probability
  type: hard
tags:
- bayes
- posterior
- prior
- likelihood
stage: formal-systems
status: draft
---

# Bayes' Theorem

## Core Idea
Bayes' theorem gives the posterior probability P(B|A) = P(A|B) × P(B) / P(A), allowing us to reverse the direction of conditioning. It describes how to update prior beliefs P(B) when we observe evidence A, using the likelihood P(A|B). This is foundational for statistical inference and decision-making under uncertainty.

## How It's Best Learned
Start with medical testing scenarios (positive test → disease probability). Work through multi-step examples with explicit calculation of the denominator using the law of total probability.

## Common Misconceptions
Confusing P(A|B) with P(B|A) (base rate fallacy). Forgetting to normalize by P(A) in the denominator.

## Questions

```yaml
- question: "A doctor knows that P(positive test | disease) = 0.95. She wants to compute P(disease | positive test). What additional information does she need?"
  type: multiple-choice
  options:
    - "Only the total number of patients tested"
    - "P(disease) — the prior probability of having the disease — and P(positive test) — the overall probability of testing positive"
    - "Nothing — P(disease | positive test) equals P(positive test | disease) by symmetry"
    - "The sample size, because Bayes' theorem only applies to large datasets"
  answer: 1
  explanation: "Bayes' theorem states P(B|A) = P(A|B)·P(B)/P(A). To find P(disease|positive), you need P(positive|disease) (the sensitivity, already known), P(disease) (the base rate — how common is the disease?), and P(positive) (overall probability of a positive result, computed via the law of total probability). Without the base rate, the calculation is impossible — and forgetting it is the source of the base rate fallacy."

- question: "A disease test has a 95% true positive rate: P(positive test | disease) = 0.95. Therefore, if a person tests positive, there is a 95% chance they have the disease."
  type: true-false
  answer: false
  explanation: "This is the classic base rate fallacy — confusing P(positive | disease) with P(disease | positive). These are not equal. If the disease is rare (e.g., affects 0.1% of the population), even a test with 95% sensitivity will produce many more false positives than true positives among people who test positive. The actual posterior probability P(disease | positive) can be far lower than 95% when the prior P(disease) is small."

- question: "In Bayes' theorem P(B|A) = P(A|B)·P(B) / P(A), what role does the denominator P(A) play?"
  type: short-answer
  answer: "P(A) is the total probability of observing evidence A — it accounts for all ways A could occur, whether or not B is true. It acts as a normalizing constant, ensuring the posterior P(B|A) is a valid probability between 0 and 1."
  explanation: "Without dividing by P(A), the numerator P(A|B)·P(B) gives the joint probability P(A∩B), not the conditional probability P(B|A). Dividing by P(A) rescales this to be relative to the event A having occurred. In practice P(A) is computed using the law of total probability: P(A) = P(A|B)·P(B) + P(A|B^c)·P(B^c)."
```

## Explainer

You have already learned conditional probability: P(A|B) is the probability of A *given* that B has occurred. Bayes' theorem answers a subtly different and enormously useful question: if I observe A, how should I update my belief about B? It lets you **reverse the direction of conditioning** — turning P(A|B) into P(B|A).

The formula is P(B|A) = P(A|B) · P(B) / P(A). Each piece has an intuitive name in statistical reasoning. P(B) is the **prior** — your belief about B before you see any evidence. P(A|B) is the **likelihood** — how probable is the evidence A if B were true? P(A) is the **marginal likelihood** — the overall probability of seeing the evidence A regardless of whether B is true. And P(B|A) is the **posterior** — your updated belief about B after observing A. The formula says: take what you thought before, weight it by how well B explains the evidence, and normalize.

The classic application is medical testing. Suppose a disease affects 1% of the population — P(disease) = 0.01. A test correctly identifies 90% of sick people: P(positive | disease) = 0.90. It also correctly identifies 91% of healthy people: P(negative | no disease) = 0.91, so P(positive | no disease) = 0.09. A person tests positive. What is P(disease | positive)? Using the law of total probability: P(positive) = (0.90)(0.01) + (0.09)(0.99) = 0.009 + 0.0891 = 0.0981. Then P(disease | positive) = (0.90 × 0.01) / 0.0981 ≈ 0.092, or about 9%. Despite the test being fairly accurate, the prior is so low that most positive results are still false positives.

This result shocks most people — and that shock is the whole point. The **base rate fallacy** is the systematic error of ignoring P(B) and treating P(A|B) as if it were P(B|A). A doctor who says "the test is 90% accurate and you tested positive, so you probably have the disease" has committed this fallacy. The denominator P(A) is the correction term: it forces you to account for how common the evidence is *in general*, not just among cases where B is true.

Bayes' theorem extends far beyond medical diagnosis. It is the foundation of Bayesian statistical inference, spam filters, machine learning classifiers, and scientific hypothesis updating. The key habit it instills is explicit reasoning about priors: every probability estimate you make implicitly contains assumptions about base rates. Making those priors explicit — and updating them correctly when evidence arrives — is what distinguishes probabilistic thinking from intuition.
