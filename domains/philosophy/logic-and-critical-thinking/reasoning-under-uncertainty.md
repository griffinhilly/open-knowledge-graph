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
stage: abstract-reasoning
status: draft
---

# Reasoning Under Uncertainty

## Core Idea
Bayesian reasoning provides a framework for updating beliefs based on evidence. Starting from background probabilities and incorporating new information lets us reason soundly when certainty is impossible, avoiding both overconfidence and undue skepticism. This approach applies to scientific hypotheses, medical diagnosis, legal reasoning, and everyday decisions.

## Explainer

You already understand probability and statistics: you know that events have likelihoods, that distributions describe populations, and that samples provide evidence about underlying parameters. **Bayesian reasoning** is what happens when you apply probability to *beliefs* rather than just to events. Instead of asking "how often does this type of event occur?", you ask "how confident should I be that this particular hypothesis is true, given the evidence I have?" This shift from frequencies to credences — degrees of belief — is how careful reasoners navigate a world where certainty is the exception and uncertainty is the default.

The core mechanism is **Bayes' theorem**. Your **prior probability** for a hypothesis H is how confident you are in H before examining new evidence — based on background knowledge, base rates, and prior experience. When you observe evidence E, you update your confidence by asking: how probable is this evidence if H is true (the **likelihood**), versus how probable is it across all hypotheses (the marginal probability)? The result is a **posterior probability** that reflects your revised confidence in H after incorporating E. Crucially, the strength of an update depends not just on how well H predicts E, but on how much more likely E is under H than under competing hypotheses. Evidence that is equally probable under all hypotheses gives you no information.

A medical example makes this concrete. Suppose a screening test for a rare disease (1 in 1000 prevalence) has a 99% true-positive rate and a 1% false-positive rate. You test positive. Should you conclude you have the disease? Your prior is 0.001. Most positive tests in this population come from false positives among the 999 disease-free people, not from the rare true positives. The posterior probability of disease given a positive test is roughly 9% — striking, but far from certain. This is **base rate neglect** in action: ignoring the prior leads to badly miscalibrated conclusions, a systematic failure that occurs in medical diagnosis, legal reasoning, and everyday judgment.

Bayesian reasoning disciplines two symmetric errors: **overconfidence** (setting priors too high, under-weighting disconfirming evidence) and **undue skepticism** (demanding certainty before updating, effectively treating posteriors as 0 unless evidence is perfect). A well-calibrated reasoner updates proportionally to the evidential force of new information. They do not require proof beyond a logical doubt to act on probable conclusions, but they also do not treat a single positive result as decisive. The same framework applies equally to scientific hypothesis testing, legal arguments, intelligence assessments, and the calibration of everyday judgment — anywhere that beliefs must be formed and revised under conditions of irreducible uncertainty.
