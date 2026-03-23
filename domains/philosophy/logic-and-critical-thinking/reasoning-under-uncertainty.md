---
id: reasoning-under-uncertainty
title: Reasoning Under Uncertainty
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: statistical-reasoning-basics
  type: hard
- id: probabilistic-reasoning
  type: soft
tags:
- uncertainty
- probability
- bayesian
stage: formal-systems
status: validated
---

# Reasoning Under Uncertainty

## Core Idea
Bayesian reasoning provides a framework for updating beliefs based on evidence. Starting from background probabilities and incorporating new information lets us reason soundly when certainty is impossible, avoiding both overconfidence and undue skepticism. This approach applies to scientific hypotheses, medical diagnosis, legal reasoning, and everyday decisions.

## Questions

```yaml
- question: "A disease affects 1 in 1,000 people. A test has 99% sensitivity (true positive rate) and 99% specificity (true negative rate). A randomly selected person tests positive. What is the approximate probability they actually have the disease?"
  type: multiple-choice
  options:
    - "About 99%, because the test is 99% accurate"
    - "About 50%, because a positive result is equally likely to be a true or false positive"
    - "About 9%, because the low base rate means most positives come from the many disease-free people"
    - "About 0.1%, because the disease affects only 1 in 1,000"
  answer: 2
  explanation: "In a population of 1,000: ~1 person has the disease and tests positive (true positive); ~999 people are disease-free and about 10 test positive (false positives at 1% rate). Of roughly 11 positive tests, only 1 is a true positive — about 9%. The test is highly accurate, yet most positive results are false. This is base rate neglect: ignoring the prior probability (prevalence) leads to dramatically inflated confidence in a positive result. The intuition 'the test is 99% accurate so I'm 99% likely to have it' is the most common and consequential error in Bayesian reasoning."

- question: "Hypotheses H₁ and H₂ are equally plausible a priori (50/50). You observe evidence E, which is ten times more likely under H₁ than under H₂. After observing E, what is your posterior probability for H₁?"
  type: multiple-choice
  options:
    - "50%, because the prior was equal and you should not update dramatically on one piece of evidence"
    - "About 91%, since the likelihood ratio is 10:1 and the prior odds were 1:1, giving posterior odds of 10:1"
    - "100%, because H₁ predicted E much better than H₂"
    - "10%, because E is 10 times more likely under H₁ than H₂"
  answer: 1
  explanation: "Posterior odds = prior odds × likelihood ratio = (1:1) × (10:1) = 10:1. Converting to probability: 10/(10+1) ≈ 91%. Option A (no update) ignores the evidence entirely. Option C (certainty) commits the error of demanding a conclusive result before updating — any evidence short of infinite likelihood ratios leaves residual uncertainty. Option D misreads the likelihood as the posterior. Strong but finite evidence shifts beliefs strongly but not all the way to certainty."

- question: "Evidence that is equally probable under all competing hypotheses provides no information for distinguishing between them."
  type: true-false
  answer: true
  explanation: "Bayesian updating works through the likelihood ratio — how much more probable E is under H₁ than under H₂. If E is equally probable under all hypotheses (likelihood ratio = 1), the ratio leaves prior odds unchanged: posterior odds = prior odds × 1 = prior odds. This means no update occurs. Useful evidence must be differentially predicted by the hypotheses — it must be more probable under some than others. This is why a positive coin flip result gives no information about whether a coin is fair: heads is 50% probable under both 'fair' and 'biased' hypotheses if 'biased' is undefined."

- question: "A well-calibrated Bayesian reasoner demands near-certainty (very high posterior probability) before acting on a conclusion, to avoid overconfidence."
  type: true-false
  answer: false
  explanation: "Demanding certainty before action is itself a calibration failure — a form of undue skepticism. Well-calibrated reasoners act on probable conclusions proportional to the stakes and the cost of waiting. Requiring certainty effectively treats the posterior as 0 until evidence is overwhelming, which is not a rational update policy. The Bayesian ideal is to act when the expected benefit of acting, weighted by posterior probability, exceeds the cost — not to wait for a certainty that uncertainty prevents. Both overconfidence and paralytic skepticism are calibration errors."

- question: "Why can a diagnostic test with 99% sensitivity and 99% specificity still produce more false positives than true positives in a screened population?"
  type: short-answer
  answer: "Because the base rate (disease prevalence) determines the ratio of disease-positive to disease-negative individuals in the population. When prevalence is very low (say 1 in 1,000), there are approximately 999 disease-free people for every 1 sick person. At 99% specificity, 1% of those 999 — about 10 people — generate false positives. But only ~1 sick person generates a true positive. So roughly 10 of 11 positive results are false. The test's 99% accuracy describes its performance on individual cases, but the population composition determines the predictive value of a positive result. Ignoring the prior (base rate neglect) produces systematic overconfidence in positive tests for rare conditions."
  explanation: "This illustrates why Bayesian reasoning requires both the likelihood (test performance) and the prior (base rate). The posterior probability of disease given a positive test depends on both, not on test accuracy alone. Medical trainees, lawyers, and judges routinely commit base rate neglect, making this one of the most practically important applications of Bayesian thinking."
```

## Explainer

You already understand probability and statistics: you know that events have likelihoods, that distributions describe populations, and that samples provide evidence about underlying parameters. **Bayesian reasoning** is what happens when you apply probability to *beliefs* rather than just to events. Instead of asking "how often does this type of event occur?", you ask "how confident should I be that this particular hypothesis is true, given the evidence I have?" This shift from frequencies to credences — degrees of belief — is how careful reasoners navigate a world where certainty is the exception and uncertainty is the default.

The core mechanism is **Bayes' theorem**. Your **prior probability** for a hypothesis H is how confident you are in H before examining new evidence — based on background knowledge, base rates, and prior experience. When you observe evidence E, you update your confidence by asking: how probable is this evidence if H is true (the **likelihood**), versus how probable is it across all hypotheses (the marginal probability)? The result is a **posterior probability** that reflects your revised confidence in H after incorporating E. Crucially, the strength of an update depends not just on how well H predicts E, but on how much more likely E is under H than under competing hypotheses. Evidence that is equally probable under all hypotheses gives you no information.

A medical example makes this concrete. Suppose a screening test for a rare disease (1 in 1000 prevalence) has a 99% true-positive rate and a 1% false-positive rate. You test positive. Should you conclude you have the disease? Your prior is 0.001. Most positive tests in this population come from false positives among the 999 disease-free people, not from the rare true positives. The posterior probability of disease given a positive test is roughly 9% — striking, but far from certain. This is **base rate neglect** in action: ignoring the prior leads to badly miscalibrated conclusions, a systematic failure that occurs in medical diagnosis, legal reasoning, and everyday judgment.

Bayesian reasoning disciplines two symmetric errors: **overconfidence** (setting priors too high, under-weighting disconfirming evidence) and **undue skepticism** (demanding certainty before updating, effectively treating posteriors as 0 unless evidence is perfect). A well-calibrated reasoner updates proportionally to the evidential force of new information. They do not require proof beyond a logical doubt to act on probable conclusions, but they also do not treat a single positive result as decisive. The same framework applies equally to scientific hypothesis testing, legal arguments, intelligence assessments, and the calibration of everyday judgment — anywhere that beliefs must be formed and revised under conditions of irreducible uncertainty.
