---
id: active-learning
title: Active Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: supervised-learning-intro
  type: hard
builds-toward:
- uncertainty-sampling
- query-strategy
tags:
- active-learning
- label-efficiency
- uncertainty
stage: advanced
status: draft
---

# Active Learning

## Core Idea
Active learning reduces labeling costs by strategically selecting which examples to label. Uncertainty sampling labels examples the model is uncertain about; diversity sampling selects representative examples. This approach is critical when annotation is expensive, enabling efficient data collection by focusing labeling effort on high-impact examples.
