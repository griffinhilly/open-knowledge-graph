---
id: knowledge-distillation
title: Knowledge Distillation
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: ensemble-methods-advanced
  type: soft
builds-toward:
- model-compression
- student-teacher
tags:
- distillation
- teacher-student
- compression
stage: advanced
status: draft
---

# Knowledge Distillation

## Core Idea
Knowledge distillation transfers knowledge from large, accurate teacher models to smaller, faster student models by training students to mimic teacher outputs. Using soft probability distributions instead of hard labels provides richer supervision signals. Students achieve similar accuracy with orders of magnitude fewer parameters.

## Explainer

From your work with neural networks, you know that larger models with more parameters generally achieve better accuracy — but they also consume more memory and compute at inference time. A massive model that takes seconds per prediction is useless in a real-time application. **Knowledge distillation** solves this by training a small, efficient **student model** to reproduce the behavior of a large, powerful **teacher model**, capturing most of the teacher's accuracy at a fraction of the cost.

The key insight is in *what* the student learns from. In standard supervised learning, the model trains against hard labels — a cat image gets the label "cat" and nothing else. But the teacher model produces **soft targets**: a probability distribution like 0.85 cat, 0.10 tiger, 0.03 lynx, 0.02 other. These soft probabilities carry far more information than a hard label. The fact that the teacher thinks "tiger" is more likely than "car" reveals something about the visual structure of the image — the student learns not just the right answer but the *relationships between classes*. This is sometimes called the "dark knowledge" hidden in the teacher's outputs.

In practice, the teacher's output probabilities are sharpened by a **temperature parameter** applied to the softmax function. At temperature T=1 (normal softmax), the dominant class often has probability near 1.0, washing out the informative relationships among other classes. Raising the temperature to T=3 or T=5 produces softer distributions that spread probability mass more evenly, making the inter-class relationships more visible to the student. The student is then trained on a weighted combination of two losses: one matching the soft teacher outputs (at high temperature) and one matching the true hard labels (at normal temperature).

The results can be striking. A student network with 10x fewer parameters than the teacher often recovers 95% or more of the teacher's accuracy. If you have studied ensemble methods, you will recognize a connection: an ensemble of models can serve as the teacher, and distillation compresses that ensemble's collective knowledge into a single small network. This is how knowledge distillation bridges the gap between the accuracy of large-scale training and the efficiency demands of deployment — you train big, then distill small.
