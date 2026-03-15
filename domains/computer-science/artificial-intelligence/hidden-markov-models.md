---
id: hidden-markov-models
title: Hidden Markov Models
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: markov-chains
  type: hard
- id: conditional-probability
  type: soft
- id: probability-mass-functions
  type: hard
- id: probability-axioms-and-rules
  type: soft
tags:
- markov-models
- sequence-models
- probabilistic-reasoning
stage: advanced
status: draft
---

# Hidden Markov Models

## Core Idea
HMMs model systems with hidden states emitting observable outputs, where state transitions follow Markov assumption. The forward algorithm computes likelihood, Viterbi decodes hidden states, and Baum-Welch learns parameters. Applications include speech recognition and sequence labeling.

## How It's Best Learned
Implement forward and Viterbi algorithms for weather prediction with hidden/observable variables.

## Common Misconceptions
Viterbi finds the most likely state sequence, not the most likely individual states. Baum-Welch convergence depends on initialization.
