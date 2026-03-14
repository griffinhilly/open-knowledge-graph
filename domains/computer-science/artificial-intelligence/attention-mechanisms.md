---
id: attention-mechanisms
title: Attention Mechanisms
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
tags:
- deep-learning
- attention
- sequence-models
stage: advanced
status: draft
---

# Attention Mechanisms

## Core Idea
Attention computes weighted combinations of values based on query-key similarity, focusing on relevant input parts. Scaled dot-product attention computes Q·K^T/√d_k before softmax weighting. Multi-head attention applies attention in parallel with different representations.
