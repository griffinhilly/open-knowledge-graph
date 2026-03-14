---
id: gru-networks
title: Gated Recurrent Units (GRU)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: recurrent-neural-networks
  type: hard
- id: lstm-gated-networks
  type: hard
builds-toward:
- sequence-modeling
- temporal-modeling
tags:
- gru
- gated-recurrent-unit
- rnn
stage: advanced
status: draft
---

# Gated Recurrent Units (GRU)

## Core Idea
Gated Recurrent Units (GRU) simplify LSTMs by combining forget and input gates into a single update gate, reducing parameters while maintaining gradient flow. GRUs have 3 gates vs. LSTMs' 4, making them faster to train with comparable performance. GRUs are preferred when computational efficiency matters.
