---
id: stochastic-gradient-descent
title: Stochastic Gradient Descent and Variants
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: gradient-descent-optimization
  type: hard
- id: partial-derivatives
  type: soft
tags:
- optimization
- learning-algorithms
stage: advanced
status: draft
---

# Stochastic Gradient Descent and Variants

## Core Idea
SGD updates parameters using single examples or small batches instead of full datasets, enabling online learning and large-scale training. Mini-batch SGD balances gradient quality and efficiency. Momentum, Adam, and adaptive methods adjust learning rates per parameter.
