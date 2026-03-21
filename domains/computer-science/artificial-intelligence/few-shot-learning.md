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

## Questions

```yaml
- question: "A large model trained on 1000 classes is given 5 examples of a new class and fine-tuned for 100 epochs. Why does this approach typically fail in practice?"
  type: multiple-choice
  options:
    - "The model's architecture cannot be extended to new classes without retraining from scratch"
    - "The model catastrophically overfits to the 5 examples, memorizing them without learning a generalizable representation"
    - "Standard fine-tuning requires at least 100 examples per class to update weights meaningfully"
    - "The learning rate must be specially tuned for each new class, requiring a separate validation set"
  answer: 1
  explanation: "With only 5 examples, fine-tuning a large model has far more free parameters than data points — gradient descent will overfit by memorizing the specific examples rather than learning to generalize. Few-shot learning addresses this not by adjusting hyperparameters, but by changing what the model learns during training: a generalizable similarity metric or parameter initialization rather than class-specific boundaries."

- question: "What is the fundamental difference between how prototypical networks and MAML handle a new task at test time?"
  type: multiple-choice
  options:
    - "Prototypical networks require fine-tuning via gradient descent; MAML classifies by nearest prototype without gradient updates"
    - "Prototypical networks classify by distance to learned class prototypes without gradient updates; MAML performs a few gradient steps to adapt to the new task"
    - "Prototypical networks use second-order optimization; MAML uses only first-order distance metrics"
    - "Both require the same number of gradient steps at test time; they differ only in training procedure"
  answer: 1
  explanation: "Prototypical networks are a metric learning approach: at test time, embed the support examples, compute class prototypes (mean embeddings), and classify by nearest prototype — no gradient updates needed. MAML meta-learns an initialization: at test time, take a few gradient steps on the support examples before classifying. This makes prototypical networks faster at inference, while MAML is more flexible but computationally expensive."

- question: "In episodic training for few-shot learning, the model is trained on the same fixed set of classes it will be tested on, just with fewer labeled examples per class."
  type: true-false
  answer: false
  explanation: "Episodic training explicitly uses different class subsets each episode so the model never sees test classes during training. If it trained on the same classes, it would memorize those classes rather than learning the general ability to classify new ones from few examples. By repeatedly solving N-way K-shot problems across different class subsets, the model learns transferable skills — how to quickly discriminate any new classes from limited evidence."

- question: "Prototypical networks require no gradient updates at test-time inference because the embedding network has been trained to create a space where computing the mean of K support examples captures a class's identity sufficiently for classification."
  type: true-false
  answer: true
  explanation: "Once the embedding function is trained, inference is just a forward pass plus nearest-prototype lookup. The training objective pushed same-class examples to cluster together and different-class examples to separate in embedding space. The prototype (mean embedding over K support examples) gives the 'center of mass' for a new class in that well-structured space, immediately enabling classification without any adaptation."

- question: "What does it mean to say few-shot learning models 'learn how to learn,' and how does episodic training implement this goal?"
  type: short-answer
  answer: "Rather than training to classify specific fixed classes, few-shot learning trains a model to solve the general problem of classifying previously unseen classes from minimal examples. Episodic training implements this by repeatedly sampling N-way K-shot problems from different class subsets. Across thousands of episodes, the model develops meta-level skills — either a well-structured embedding space (metric learning) or a parameter initialization that rapidly adapts to any new task (MAML) — that transfer to novel classification problems."
  explanation: "The training objective is reframed: standard supervised learning asks 'which fixed class does this belong to?'; few-shot learning asks 'given K examples of each of N new classes, which class does this query belong to?' Solving this across many different class subsets forces the model to develop generalizable representations rather than class-specific ones."
```

## Explainer

From your study of transfer learning, you know that a model trained on one task can be adapted to a new task by reusing learned representations — typically by fine-tuning a pretrained network on new labeled data. But what if you have only one or five examples of each new class? Standard fine-tuning on so little data will catastrophically overfit. **Few-shot learning** addresses this extreme low-data regime by training models that are explicitly designed to generalize from minimal examples, typically framed as **N-way K-shot** problems: classify among N new classes given only K labeled examples per class.

The training paradigm is fundamentally different from standard supervised learning. Instead of training on a fixed set of classes, few-shot learning uses **episodic training**: each training episode samples a small subset of classes and a handful of examples per class, mimicking the few-shot scenario the model will face at test time. The model learns not to classify specific classes, but to *learn how to classify* — a form of **meta-learning** (learning to learn). Over thousands of episodes with different class subsets, the model develops general-purpose abilities for rapid adaptation.

The two dominant approaches differ in what they meta-learn. **Metric learning** methods learn an embedding function that maps examples into a space where same-class examples cluster together and different-class examples are far apart. **Prototypical networks** are the clearest example: embed all K support examples for each class, compute the mean embedding (the **prototype**) for each class, and classify a new query by finding the nearest prototype. The training objective simply pushes the embedding network to create clusters that are tight within each class and well-separated between classes. **Siamese networks** take a pairwise approach, learning to predict whether two examples belong to the same class. These methods are elegant because at test time, they require no gradient updates — just a forward pass and a distance computation.

**Model-Agnostic Meta-Learning (MAML)** takes the alternative approach of meta-learning an initialization. The idea is to find a set of network parameters that, when fine-tuned with just a few gradient steps on K examples of new classes, rapidly achieves good performance. MAML trains by simulating this inner fine-tuning loop across many episodes and optimizing the initial parameters so that the post-fine-tuning performance is maximized. This requires computing gradients through gradients (second-order optimization), which is computationally expensive but remarkably flexible — it works with any model architecture and any differentiable loss. The intuition is that MAML finds a point in parameter space that is close to good solutions for many tasks simultaneously, so a few steps of gradient descent on any specific task lands in the right neighborhood.
