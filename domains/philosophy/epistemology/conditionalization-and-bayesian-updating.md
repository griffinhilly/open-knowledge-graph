---
id: conditionalization-and-bayesian-updating
title: Conditionalization and Bayesian Updating
domain: philosophy
course: epistemology
prerequisites:
- id: credences-and-epistemic-probabilities
  type: hard
- id: probabilistic-computation
  type: soft
- id: probabilistic-reasoning
  type: soft
builds-toward:
- evidential-support-formalization
tags:
- bayesian-updating
- evidence
- learning
stage: advanced
status: draft
---

# Conditionalization and Bayesian Updating

## Core Idea
Conditionalization is the rule by which rational agents update credences in response to evidence: P_new(p) = P_old(p|e), where e is the agent's total evidence. The posterior probability of p given e equals the prior probability of p conditional on e. This rule ensures that repeated updating leads to convergence on the truth given enough evidence, and formalizes the intuition that learning should shift belief toward propositions consistent with observed evidence.

## Explainer

You have learned that **credences** are degrees of belief — numbers between 0 and 1 representing how confident an agent is in a proposition. A credence of 1 is certainty, 0 is certainty of falsity, and 0.5 is maximum uncertainty. But credences are not static; rational agents receive evidence and must update their beliefs in light of it. The question is: what is the right rule for updating? Conditionalization provides a precise answer.

If your current credence in proposition *p* is P(p), and you then learn evidence *e* with certainty, your new credence in *p* should be P(p | e) — your old conditional probability of p given e. Formally: P_new(p) = P_old(p | e). This formula follows from the definition of conditional probability: P(p | e) = P(p ∧ e) / P(e). The numerator is the prior probability you assigned to worlds where both p and e are true; the denominator is the prior probability you assigned to e being true at all. The ratio tells you how much of e's prior probability-mass came from worlds where p also holds. If e is strongly correlated with p in your prior, then learning e raises your credence in p substantially.

The intuitive picture is illuminating. Imagine your beliefs as a probability distribution spread across many possible worlds. Before observing evidence, you distribute credence across those worlds according to your prior. When you learn that e is true, you eliminate all worlds where e is false and renormalize — redistributing the remaining probability mass proportionally among worlds where e holds. Propositions correlated with e become more credible; those anti-correlated become less credible. This is exactly what the conditionalization formula computes. The rule has a powerful **convergence property**: two rational agents who start with different priors but share evidence and conditionalize faithfully will, given enough evidence, converge on very similar credences. Evidence is the great leveler of disagreement. One important philosophical challenge is the **problem of old evidence**: conditionalization implies that learning something you already knew with certainty cannot change your beliefs. But it sometimes seems that recognizing old evidence bears on a new hypothesis should update you. This tension motivates ongoing Bayesian epistemology research into how to handle evidence and hypothesis formation in tandem.

