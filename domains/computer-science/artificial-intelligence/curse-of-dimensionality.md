---
id: curse-of-dimensionality
title: Curse of Dimensionality
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: dimensionality-reduction
  type: soft
- id: feature-engineering-selection
  type: soft
builds-toward:
- principal-component-analysis
- feature-selection
tags:
- dimensionality
- high-dimensional
- sparsity
stage: advanced
status: draft
---

# Curse of Dimensionality

## Core Idea
As feature count increases, the feature space volume grows exponentially, making data increasingly sparse and distances between points less meaningful. This phenomenon, known as the curse of dimensionality, requires more data to maintain model performance. Dimensionality reduction and feature selection are critical mitigation strategies.
