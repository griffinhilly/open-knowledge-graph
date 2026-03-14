---
id: probabilistic-reasoning
title: Probabilistic Reasoning
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: inductive-reasoning
  type: hard
- id: modus-ponens-tollens
  type: soft
tags:
- probability
- bayesian
- reasoning
- induction
stage: abstract-reasoning
status: draft
---

# Probabilistic Reasoning

## Core Idea
Probabilistic reasoning extends logic beyond certainty to handle degrees of belief. Where deductive logic deals in conclusions that follow necessarily, probabilistic reasoning evaluates how much a piece of evidence should raise or lower confidence in a hypothesis. Conditional probability — the probability of A given B — is the foundational concept. Bayesian updating provides a systematic framework: start with a prior probability, observe evidence, and compute a posterior probability that reflects how much the evidence should shift your belief. This approach formalizes the intuition that strong evidence against a very unlikely hypothesis may still leave it unlikely, while weak evidence for a likely hypothesis may be enough to confirm it.

## How It's Best Learned
Start with simple examples using coins and urns to build intuition about conditional probability. Then apply Bayes' theorem to real scenarios: medical diagnosis, legal evidence, spam filtering. Compare Bayesian updating with informal reasoning to see where intuition diverges from the math.

## Common Misconceptions
- Confusing the probability of evidence given a hypothesis with the probability of the hypothesis given evidence — this transposition error is one of the most common reasoning mistakes.
- Thinking Bayesian reasoning requires precise numerical probabilities; it can also be used qualitatively to reason about which direction evidence should push beliefs.
