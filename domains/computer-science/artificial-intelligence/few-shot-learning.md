---
id: few-shot-learning
title: Few-Shot Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: transfer-learning-neural
  type: hard
builds-toward:
- zero-shot-learning
- prototypical-networks
tags:
- few-shot
- low-data
- rapid-adaptation
stage: advanced
status: draft
---

# Few-Shot Learning

## Core Idea
Few-shot learning enables models to learn new classes from very few examples (1-shot, 5-shot) by leveraging prior knowledge. Metric learning approaches learn similarity functions; model-agnostic meta-learning discovers good initializations. Prototypical networks classify based on distances to learned class prototypes in embedding space.
