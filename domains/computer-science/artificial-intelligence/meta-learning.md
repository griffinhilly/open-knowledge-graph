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

## Explainer

Standard neural network training optimizes a model for one specific task: classify these images, predict these labels, generate these outputs. But consider how humans learn. After learning to identify dogs, cats, and birds, you can recognize a new animal species from just a few examples — you have learned *how to learn* visual categories, not just the categories themselves. **Meta-learning** formalizes this idea: instead of training a model to solve one task, you train it across many tasks so that it becomes good at adapting to new ones quickly.

The setup requires rethinking what "training data" means. In conventional supervised learning, your dataset is a collection of labeled examples for a single task. In meta-learning, your dataset is a collection of *tasks*, each containing its own small training set (the **support set**) and test set (the **query set**). During meta-training, the model repeatedly receives a new task, adapts to its support set, and is evaluated on its query set. The meta-learner's parameters are updated based on how well it performed *after* adaptation — optimizing not for any single task's accuracy but for the ability to adapt rapidly.

**MAML** (Model-Agnostic Meta-Learning) is the most influential approach and illustrates the core idea cleanly. MAML finds an initialization of the neural network weights such that a few gradient descent steps on a new task's support set produce strong performance on its query set. Think of it as finding a point in weight space that is equidistant from the optimal solutions of many different tasks — a "good starting position" from which any specific task is only a short walk away. The outer loop optimizes this initialization by computing gradients *through* the inner adaptation steps, which requires second-order derivatives (gradients of gradients).

Beyond MAML, other meta-learning paradigms take different approaches. **Metric-based** methods like Prototypical Networks learn an embedding space where examples from the same class cluster together, making classification a nearest-neighbor problem in that space. **Black-box** methods use a recurrent or attention-based network that takes the support set as input and directly outputs predictions, treating the entire adaptation process as a forward pass rather than explicit gradient steps. Each paradigm makes different tradeoffs between flexibility, computational cost, and the assumptions imposed on what "adaptation" means. What unifies them is the two-level structure: an inner loop that adapts to specific tasks and an outer loop that improves the adaptation process itself.
