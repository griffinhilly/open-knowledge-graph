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
tags:
- zero-shot
- semantic-attributes
- transfer
stage: advanced
status: validated
---

# Zero-Shot Learning

## Core Idea
Zero-shot learning classifies unseen classes by leveraging semantic embeddings or attribute descriptions shared across seen and unseen classes. A model trained on seen classes transfers knowledge to unseen classes through semantic space. This enables generalization beyond training classes without task-specific fine-tuning.

## Questions

```yaml
- question: "A zero-shot classifier is tested on images of a pangolin — a species never seen during training. How does the model classify it correctly without any pangolin training examples?"
  type: multiple-choice
  options:
    - "The model guesses among all known classes and picks the one with the highest training-time accuracy"
    - "The model projects the pangolin image into semantic space and finds it nearest to the 'pangolin' class embedding, which encodes the species' semantic properties"
    - "The model retrains on a few similar species and interpolates to the pangolin class"
    - "The model falls back to the nearest visually similar class from the training set"
  answer: 1
  explanation: "In zero-shot learning, both the input (the image) and every class label (including unseen ones) are embedded in a shared semantic space. During training, the model learned to project inputs into this space so that images of zebras land near the 'zebra' embedding. At test time, the pangolin image is projected into the same space, and the 'pangolin' class embedding — derived from word vectors or attribute descriptions — is already positioned there based on semantic relationships. The model finds the nearest class embedding and predicts 'pangolin.' No retraining or pangolin examples are needed."

- question: "What is the fundamental difference between a conventional classifier and a zero-shot classifier in how they represent output classes?"
  type: multiple-choice
  options:
    - "Conventional classifiers use neural networks; zero-shot classifiers use rule-based systems"
    - "Conventional classifiers have fixed output slots — one per training class; zero-shot classifiers represent classes as points in a shared semantic space accessible at any time"
    - "Conventional classifiers require more training data; zero-shot classifiers use less data but are less accurate"
    - "Conventional classifiers can handle any class at test time; zero-shot classifiers only handle classes seen during training"
  answer: 1
  explanation: "A conventional classifier's output layer has a fixed number of neurons — one per training class. There is no mechanism for predicting a class not present during training. Zero-shot classifiers replace fixed output slots with a semantic space: any class that has a semantic embedding (word vector, attribute vector) can be queried at test time, regardless of whether examples of that class were in the training set. This architectural difference is what enables generalization to unseen classes."

- question: "Zero-shot learning means the model receives zero training examples in total — it performs classification without any training at most."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about zero-shot learning. The 'zero shots' refers specifically to zero examples of the *unseen* classes — the model is heavily trained on *seen* classes and on the semantic embedding space. The model learns from seen-class examples how to project inputs into semantic space; zero-shot generalization is then possible because unseen classes already have semantic embeddings that position them meaningfully in that space. Zero-shot learning requires substantial training; what it avoids is training on the specific classes encountered at test time."

- question: "In generalized zero-shot learning, a model that always predicts seen classes is likely to outperform a model that treats seen and unseen classes equally, because seen classes have richer learned representations."
  type: true-false
  answer: true
  explanation: "This is precisely why generalized zero-shot learning is harder than standard zero-shot learning. When test examples can come from either seen or unseen classes, the model's projection function — optimized on seen-class examples — creates richer, more confident representations for seen classes. Unseen class embeddings, derived purely from semantic descriptions without any training signal, may be less precisely positioned. The result is a strong bias toward predicting seen classes, even for inputs from unseen classes. Calibration techniques and transductive methods are needed to correct this bias."

- question: "Explain why a zero-shot classifier can correctly classify a new animal species it has never seen, even though no examples of that species were in the training data."
  type: short-answer
  answer: "Zero-shot classification works by projecting both inputs and class labels into a shared semantic space. During training, the model learns to map input features (e.g., image pixels) to positions in this space using seen-class examples — images of zebras are trained to project near the 'zebra' embedding. Unseen classes like 'okapi' already have semantic embeddings from word vectors or attribute descriptions that encode their properties — the word 'okapi' sits near 'giraffe' and 'deer' in the embedding space. At test time, the unseen image is projected into the same space, and the nearest class embedding is predicted. The model succeeds not by recognizing okapis specifically, but by leveraging the structure of semantic space: the visual features of an okapi project near the semantic region where okapi-like concepts live."
  explanation: "The key insight is that zero-shot learning transfers knowledge not through examples but through semantic structure. Word embeddings and attribute vectors capture meaningful relationships between concepts — those relationships were learned from language and human-defined descriptions, not from visual examples. By bridging the visual input space and the semantic class space, the model inherits structural knowledge encoded in language."
```

## Explainer

Standard classification assumes that every class the model will encounter at test time was present during training. But consider an image classifier trained on 1,000 animal species that encounters a photograph of an okapi — a species it has never seen. A conventional classifier has no output node for "okapi" and must fail. **Zero-shot learning** solves this by never classifying into fixed output slots. Instead, it learns to map inputs into a shared **semantic space** where both seen and unseen classes have representations, then classifies by finding the nearest class representation in that space.

The key ingredient is the **semantic embedding** of classes, which you know from your study of word embeddings. Each class is represented not by an arbitrary integer label but by a rich vector — typically a word embedding of the class name, or a vector of human-defined attributes (has stripes, is tall, is herbivorous). During training, the model learns to project input features (image pixels, text tokens) into this same semantic space so that images of zebras land near the "zebra" embedding. At test time, the model projects the okapi image into semantic space and finds that it is closest to the "okapi" class embedding — even though no okapi image was ever used in training. The model succeeds because "okapi" has a meaningful position in semantic space (near "giraffe" and "deer") that captures its visual properties.

Two main approaches dominate. **Attribute-based methods** define each class by a binary or continuous attribute vector — for animals, attributes might include "has fur," "has hooves," "is domesticated." The model learns to predict attributes from inputs, then matches predicted attributes to class attribute vectors. **Embedding-based methods** use pre-trained word vectors or sentence embeddings as class representations and learn a compatibility function between input features and class embeddings. The embedding approach is more scalable since it requires no manual attribute annotation, and it benefits directly from the structure that word embeddings capture — semantically similar classes have similar embeddings, so knowledge about horses transfers naturally to zebras.

A critical challenge is the **hubness problem** and **domain shift**. In high-dimensional spaces, some points (hubs) tend to be nearest neighbors of many other points, causing certain classes to be predicted far too often. Domain shift occurs because the model's projection function was optimized on seen classes and may not generalize well to unseen ones. **Generalized zero-shot learning** addresses an even harder setting where test examples may come from either seen or unseen classes, requiring the model to avoid the temptation of always predicting a familiar seen class. Solutions include calibration techniques and transductive methods that use unlabeled test data to adapt the projection. Zero-shot learning connects naturally to the broader transfer learning paradigm: instead of transferring learned features across tasks, it transfers semantic structure across classes.
