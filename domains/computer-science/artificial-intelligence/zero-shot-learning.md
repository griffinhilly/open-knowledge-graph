---
id: zero-shot-learning
title: Zero-Shot Learning
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: word-embeddings
  type: hard
- id: transfer-learning-neural
  type: soft
builds-toward:
- semantic-similarity
- knowledge-transfer
tags:
- zero-shot
- semantic-attributes
- transfer
stage: advanced
status: draft
---

# Zero-Shot Learning

## Core Idea
Zero-shot learning classifies unseen classes by leveraging semantic embeddings or attribute descriptions shared across seen and unseen classes. A model trained on seen classes transfers knowledge to unseen classes through semantic space. This enables generalization beyond training classes without task-specific fine-tuning.

## Explainer

Standard classification assumes that every class the model will encounter at test time was present during training. But consider an image classifier trained on 1,000 animal species that encounters a photograph of an okapi — a species it has never seen. A conventional classifier has no output node for "okapi" and must fail. **Zero-shot learning** solves this by never classifying into fixed output slots. Instead, it learns to map inputs into a shared **semantic space** where both seen and unseen classes have representations, then classifies by finding the nearest class representation in that space.

The key ingredient is the **semantic embedding** of classes, which you know from your study of word embeddings. Each class is represented not by an arbitrary integer label but by a rich vector — typically a word embedding of the class name, or a vector of human-defined attributes (has stripes, is tall, is herbivorous). During training, the model learns to project input features (image pixels, text tokens) into this same semantic space so that images of zebras land near the "zebra" embedding. At test time, the model projects the okapi image into semantic space and finds that it is closest to the "okapi" class embedding — even though no okapi image was ever used in training. The model succeeds because "okapi" has a meaningful position in semantic space (near "giraffe" and "deer") that captures its visual properties.

Two main approaches dominate. **Attribute-based methods** define each class by a binary or continuous attribute vector — for animals, attributes might include "has fur," "has hooves," "is domesticated." The model learns to predict attributes from inputs, then matches predicted attributes to class attribute vectors. **Embedding-based methods** use pre-trained word vectors or sentence embeddings as class representations and learn a compatibility function between input features and class embeddings. The embedding approach is more scalable since it requires no manual attribute annotation, and it benefits directly from the structure that word embeddings capture — semantically similar classes have similar embeddings, so knowledge about horses transfers naturally to zebras.

A critical challenge is the **hubness problem** and **domain shift**. In high-dimensional spaces, some points (hubs) tend to be nearest neighbors of many other points, causing certain classes to be predicted far too often. Domain shift occurs because the model's projection function was optimized on seen classes and may not generalize well to unseen ones. **Generalized zero-shot learning** addresses an even harder setting where test examples may come from either seen or unseen classes, requiring the model to avoid the temptation of always predicting a familiar seen class. Solutions include calibration techniques and transductive methods that use unlabeled test data to adapt the projection. Zero-shot learning connects naturally to the broader transfer learning paradigm: instead of transferring learned features across tasks, it transfers semantic structure across classes.
