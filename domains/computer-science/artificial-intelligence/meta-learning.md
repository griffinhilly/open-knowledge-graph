---
id: meta-learning
title: Meta-Learning (Learning to Learn)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: few-shot-learning
  type: hard
- id: neural-networks-intro
  type: hard
builds-toward:
- few-shot-learning
- transfer-learning-neural
tags:
- meta-learning
- learning-to-learn
- adaptation
stage: advanced
status: draft
---

# Meta-Learning (Learning to Learn)

## Core Idea
Meta-learning trains models to learn quickly from few examples by optimizing for rapid task adaptation. Algorithms like MAML (Model-Agnostic Meta-Learning) discover initializations amenable to fine-tuning on new tasks with minimal gradient steps. This mimics human learning by leveraging prior knowledge for generalization.
