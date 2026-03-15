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
stage: formal-systems
status: draft
---

# Conditionalization and Bayesian Updating

## Core Idea
Conditionalization is the rule by which rational agents update credences in response to evidence: P_new(p) = P_old(p|e), where e is the agent's total evidence. The posterior probability of p given e equals the prior probability of p conditional on e. This rule ensures that repeated updating leads to convergence on the truth given enough evidence, and formalizes the intuition that learning should shift belief toward propositions consistent with observed evidence.
