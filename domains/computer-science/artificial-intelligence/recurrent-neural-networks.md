---
id: recurrent-neural-networks
title: Recurrent Neural Networks
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: backpropagation
  type: hard
- id: markov-chains
  type: soft
- id: partial-derivatives
  type: soft
- id: matrix-operations
  type: soft
- id: sequences-and-series-review
  type: soft
tags:
- deep-learning
- sequence-models
- neural-networks
stage: advanced
status: draft
---

# Recurrent Neural Networks

## Core Idea
RNNs process sequences maintaining hidden states updated at each time step. Information propagates temporally enabling sequence modeling. Backpropagation through time (BPTT) unfolds the network across time but suffers from vanishing/exploding gradients.
