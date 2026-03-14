---
id: self-attention
title: Self-Attention and Multi-Head Attention
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: attention-mechanisms
  type: hard
- id: transformer-architecture
  type: hard
builds-toward:
- transformer-variants
- vision-transformers
tags:
- self-attention
- multi-head
- transformer
stage: advanced
status: draft
---

# Self-Attention and Multi-Head Attention

## Core Idea
Self-attention computes a weighted sum of all positions in a sequence, allowing each position to attend to every other position. Multi-head attention runs multiple self-attention operations in parallel, learning different attention patterns. This mechanism is central to Transformers and enables modeling long-range dependencies more effectively than RNNs.
