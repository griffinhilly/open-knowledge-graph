---
id: temporal-difference-learning
title: Temporal Difference Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: reinforcement-learning-intro
  type: hard
- id: markov-decision-processes
  type: hard
- id: markov-chains
  type: hard
- id: expected-value
  type: soft
builds-toward:
- deep-q-networks
- q-learning
tags:
- reinforcement-learning
- value-based
- temporal-difference
- bootstrapping
stage: advanced
status: draft
---

# Temporal Difference Learning

## Core Idea
Temporal difference learning updates value estimates using the difference between successive value predictions (TD error), enabling online learning without full episode returns. TD combines sample-based learning (Monte Carlo) and bootstrapping (dynamic programming); the TD(λ) framework generalizes TD(0) and Monte Carlo through an eligibility trace parameter λ.

## How It's Best Learned
Implement TD(0) and TD(1) on a simple domain and observe convergence differences; then implement TD(λ) with eligibility traces to understand the spectrum between TD(0) and Monte Carlo.
