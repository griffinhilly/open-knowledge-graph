---
id: likelihood-ratios-and-belief-updates
title: "Likelihood Ratios and Belief Updates"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: bayesian-thinking-in-practice
    type: hard
  - id: bayes-theorem
    type: hard
  - id: conditional-probability
    type: soft
builds-toward:
  - calibration-training
  - reference-class-forecasting
tags: ["bayesian", "likelihood-ratio", "belief-updating", "quantitative-reasoning"]
stage: advanced
status: validated
---

## Core Idea

The likelihood ratio is the engine of Bayesian updating: it measures how much more (or less) likely a piece of evidence is under one hypothesis compared to another. A likelihood ratio of 10 means the evidence is 10 times more likely if the hypothesis is true than if it is false — a strong update. A ratio near 1 means the evidence is equally expected either way — no update warranted. Thinking in likelihood ratios rather than raw probabilities makes Bayesian reasoning more intuitive: instead of juggling joint probabilities, you ask "how much more expected is this evidence under my hypothesis?" and shift your confidence proportionally. In log-odds form, updates become simple addition: log-odds posterior = log-odds prior + log likelihood ratio.

## How It's Best Learned

Practice with the classic medical diagnosis example: a test with 99% sensitivity and 5% false positive rate gives a likelihood ratio of 99/5 ≈ 20. For a disease with 1% base rate (prior odds 1:99), a positive test gives posterior odds of 20:99, or about 17% — far from certainty despite a 99% accurate test. Work problems in both probability and log-odds form to build fluency with both representations.

## Common Misconceptions

- A high likelihood ratio does not mean the hypothesis is probably true — it depends on the prior. A likelihood ratio of 100 applied to a prior of 1 in a million still yields a tiny posterior.
- Likelihood ratios are not the same as the probability of the hypothesis given the evidence — that is the posterior, which combines the ratio with the prior.

## Explainer

From Bayesian thinking in practice, you know the habit of updating beliefs on evidence. From Bayes' theorem, you know the formula: P(H|E) = P(E|H) x P(H) / P(E). Likelihood ratios are the engine that makes this machinery intuitive rather than formulaic. Once you understand them, Bayesian updating becomes something you can do in your head, in real time, for everyday reasoning.

The **likelihood ratio** for a piece of evidence is simply: how much more likely is this evidence if my hypothesis is true than if it is false? Formally, LR = P(E|H) / P(E|not-H). A likelihood ratio of 10 means the evidence is 10 times more expected under the hypothesis than under the alternative -- a strong update toward H. A ratio of 1 means the evidence is equally likely either way -- no update at all. A ratio of 0.1 means the evidence is 10 times more expected if the hypothesis is false -- a strong update against H. The beauty of this formulation is that it separates the evidence's diagnostic power from your prior beliefs. The likelihood ratio tells you how much to shift; your prior tells you where you started. Together they determine where you end up.

Consider the classic medical diagnosis example. A test has 99% sensitivity (it catches 99% of true cases) and a 5% false positive rate. The likelihood ratio for a positive test is 99/5 = roughly 20. For a disease with a 1% base rate, your prior odds are 1:99. A positive test multiplies those odds by 20, giving posterior odds of 20:99, or about 17% probability of disease. This is far from the 99% that the test's "accuracy" might suggest -- and the likelihood ratio framework makes it immediately clear why. The test is good (LR of 20 is a strong update), but the prior is low (1:99 odds), and the prior has not been overcome. Without likelihood ratios, this result is counterintuitive and frequently miscalculated; with them, it is transparent.

The **log-odds** representation makes multi-evidence updating even more natural. In log-odds, Bayesian updating becomes simple addition: log-odds(posterior) = log-odds(prior) + log(LR1) + log(LR2) + ... . Each piece of evidence contributes an additive term. Weak evidence (log-LR near 0) barely shifts the sum; strong evidence (large log-LR) moves it substantially. Opposing pieces of evidence cancel. You can see at a glance how many weak pieces of evidence it takes to equal one strong one, and how a strong prior (large negative or positive log-odds) resists movement from moderate evidence. This additive structure is not just computational convenience -- it reflects the genuine way evidential weight accumulates, and it makes the relationship between evidence strength and belief change immediately legible.

## Questions

```yaml
- question: "A test for a rare disease has 95% sensitivity and a 10% false positive rate (LR ≈ 9.5). The disease affects 1% of the population. A patient tests positive. What is the approximate posterior probability the patient has the disease?"
  type: multiple-choice
  options:
    - "About 95%, because the test is highly sensitive"
    - "About 86%, because the LR of 9.5 means strong evidence and the prior is close enough to 1%"
    - "About 8.7%, because the low prior (1%) dominates despite the moderate LR"
    - "About 50%, because a positive test makes the hypothesis and its negation equally likely"
  answer: 2
  explanation: "Prior odds = 0.01/0.99 ≈ 1:99. Posterior odds = LR × prior odds = 9.5 × (1/99) ≈ 9.5/99. Posterior probability ≈ 9.5/(9.5 + 99) ≈ 8.7%. Despite a reasonably good test, the extremely low base rate dilutes the update dramatically. This is the core lesson: a high likelihood ratio does not guarantee a high posterior — the prior matters enormously. A test that is 95% sensitive sounds impressive until you realize it's being applied to a disease that affects only 1 in 100 people."

- question: "A new blood marker is found in cancer patients 55% of the time and in healthy people 50% of the time, giving a likelihood ratio of 55/50 = 1.1. A clinician says the marker 'provides useful evidence — a positive result makes cancer 10% more likely.' What is the key error in this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — a 10% likelihood ratio boost is a clinically meaningful update"
    - "The clinician confused the likelihood ratio with a probability boost; LR = 1.1 means the evidence is nearly uninformative because the marker is barely more expected under cancer than without it"
    - "The LR should be computed as 50/55 (the reciprocal) for a positive result"
    - "The marker cannot be useful because it appears in healthy people at all"
  answer: 1
  explanation: "A likelihood ratio of 1.1 means the marker is only 10% more expected if the patient has cancer than if they don't — barely above 'equally expected either way.' In log-odds, this is log(1.1) ≈ 0.04 units, a negligible shift. The clinician's '10% more likely' confuses a 10% ratio boost with a 10 percentage-point change in posterior probability — completely different things. For a marker to substantially move beliefs, the LR must be substantially above 1 (or below 1 for evidence against). Near-1 LRs are near-zero evidence."

- question: "A likelihood ratio of 100 applied to a prior probability of 1 in 10,000 yields a posterior probability of approximately 1%."
  type: true-false
  answer: true
  explanation: "Prior odds = 1:9,999 ≈ 1:10,000. Posterior odds = 100 × (1/10,000) = 1/100. Posterior probability = 1/(1+100) ≈ 0.99% ≈ 1%. Even a very strong LR of 100 barely moves the needle when the prior is sufficiently small. The absolute change in probability depends on where you start: moving from 1-in-10,000 to ~1-in-100 is a large relative change (100×) but still a tiny absolute probability. Base rates matter as much as likelihood ratios."

- question: "A likelihood ratio of 20 means there is approximately a 95% probability that the hypothesis is true."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about likelihood ratios. The posterior probability depends on BOTH the likelihood ratio AND the prior. A LR of 20 means the evidence is 20 times more likely under the hypothesis than under its negation — but the posterior probability is LR × prior odds / (LR × prior odds + 1). With prior odds of 1:1, a LR of 20 gives posterior probability 20/21 ≈ 95%. But with prior odds of 1:100, the same LR gives 20/120 ≈ 17%. The LR is not a probability; it's a multiplier applied to the prior odds."

- question: "Explain why thinking in log-odds makes it easier to combine multiple independent pieces of evidence when updating beliefs."
  type: short-answer
  answer: "In probability form, combining independent pieces of evidence requires multiplying likelihood ratios and re-normalizing — a messy process involving fractions. In log-odds form, each piece of independent evidence becomes an additive term: log-odds(posterior) = log-odds(prior) + log(LR₁) + log(LR₂) + .... Each log likelihood ratio is simply added to a running total, like accumulating points. This makes it easy to see how many weak pieces of evidence compound, how opposing evidence cancels, and when an update is negligible (log-LR near 0). The additive structure also makes it clear that strong priors require strong evidence to overcome."
  explanation: "The log-odds representation mirrors how odds multiply in the standard Bayes update: posterior odds = prior odds × LR₁ × LR₂ × .... Taking logarithms converts products to sums. This is not just computational convenience — it reflects the genuine additive structure of evidential weight and makes the relationship between evidence strength (log-LR) and belief shift immediately legible."
```
