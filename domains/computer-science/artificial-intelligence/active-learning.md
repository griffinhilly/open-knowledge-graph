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

## Questions

```yaml
- question: "A model trained with uncertainty sampling consistently queries borderline examples between two classes but never improves on a third class that exists in a distant cluster. What is the root cause and the fix?"
  type: multiple-choice
  options:
    - "The model needs a larger architecture to handle three classes simultaneously"
    - "Uncertainty sampling is myopic — it ignores distant, unvisited regions; diversity sampling addresses this by querying examples far from any already-labeled point"
    - "The labeling budget is too small; with more labels the model will eventually reach the third cluster through uncertainty sampling"
    - "The model should switch to unsupervised learning to discover the third cluster"
  answer: 1
  explanation: "Uncertainty sampling only queries examples near the current decision boundary. A cluster that the model has never seen labeled examples from will be confidently (but incorrectly) classified as the nearest known class — it doesn't look uncertain, so uncertainty sampling never queries it. Diversity sampling explicitly selects examples that are far from any already-labeled point, ensuring broader coverage of the feature space. The best active learning strategies combine both signals: uncertain AND diverse examples."

- question: "What is the essential difference between active learning and standard supervised learning?"
  type: multiple-choice
  options:
    - "Active learning uses unlabeled data at test time to improve predictions"
    - "Active learning replaces gradient-based optimization with reinforcement signals from a reward function"
    - "The model selects which examples to request labels for, rather than passively receiving a fixed pre-labeled dataset"
    - "Active learning requires more labeled data to achieve the same accuracy as standard supervised learning"
  answer: 2
  explanation: "In standard supervised learning the dataset is fixed and the learner has no say in which examples are labeled. Active learning inverts this: the model queries an oracle (typically a human annotator) for labels on the examples it finds most informative. The practical payoff is that active learning achieves the same accuracy with far fewer labeled examples than random selection. Option D is the opposite of active learning's purpose — label efficiency is the entire motivation."

- question: "In uncertainty sampling, the model should preferentially label examples where it is most confident about the correct class label."
  type: true-false
  answer: false
  explanation: "Uncertainty sampling targets the opposite: examples where the model is *least* confident — those near the decision boundary where predicted class probabilities are closest to uniform. Labeling examples the model is already confident about would confirm what it already knows and add little information. Borderline examples, once labeled, can push the decision boundary in the right direction and improve accuracy across an entire region of the feature space."

- question: "Active learning requires a small initial labeled seed set to begin — it cannot start from a completely unlabeled pool."
  type: true-false
  answer: true
  explanation: "An initial labeled seed set is necessary to train even a minimal model, which the active learning loop uses to compute uncertainty scores and identify which unlabeled examples to query. Without any labels, the model has no learned representations and no basis for scoring examples. The seed set can be very small (sometimes just a handful of examples per class), but some starting point is required before the iterative query loop can begin."

- question: "Explain why pure uncertainty sampling can fail in practice and what additional criterion addresses this limitation."
  type: short-answer
  answer: "Uncertainty sampling queries examples near the current decision boundary — examples the model finds confusing. If the unlabeled data contains clusters far from any labeled example (perhaps an entirely unseen class), the model will confidently misclassify those examples and never query them, because they don't look uncertain. The strategy gets stuck obsessively sampling a locally confusing region while ignoring large swaths of the data distribution. Diversity sampling addresses this by selecting examples far from any already-labeled point, ensuring coverage of underrepresented regions. Combined strategies — selecting examples that are both uncertain and diverse — produce faster learning curves and more robust models than either criterion alone."
  explanation: "The failure mode is sometimes called 'query by committee bias' or 'boundary obsession.' A well-designed active learning system treats uncertainty and diversity as complementary objectives: uncertainty ensures the labels are maximally informative given what the model already knows; diversity ensures the model builds a complete picture of the data distribution rather than perfecting a small decision region."
```

## Explainer

In standard supervised learning, you assume a fixed labeled dataset and train a model on all of it. Active learning flips this assumption: instead of passively receiving labeled data, the model gets to *choose* which examples it wants labeled next. The motivation is practical — in many real-world settings, unlabeled data is abundant but labeling is expensive. A medical imaging system may have access to millions of X-rays, but getting a radiologist to annotate each one costs time and money. If the model could identify the 500 most informative images to label instead of labeling 10,000 at random, you could achieve the same performance at a fraction of the cost.

The simplest and most widely used strategy is **uncertainty sampling**: the model examines the pool of unlabeled examples and selects the ones it is most uncertain about. For a classifier, this might mean choosing the example whose predicted class probabilities are closest to uniform — the example sitting right on the decision boundary. The intuition is that labeling these ambiguous examples gives the model the most information about where the boundary should be. If the model is already confident about an example, labeling it would just confirm what it already knows. But an example near the decision boundary, once labeled, can push the boundary in the right direction and improve accuracy across an entire region of the feature space.

**Diversity sampling** takes a complementary approach: instead of focusing on model uncertainty, it selects examples that are representative of the unlabeled data distribution. The concern with pure uncertainty sampling is that it can get stuck querying examples from a small, confusing region of the space — endlessly asking about borderline cases between two classes while ignoring an entire cluster of a third class it has never seen. Diversity-based methods, such as selecting examples that are far from any already-labeled point, ensure broader coverage. In practice, the best active learning strategies often combine both signals — selecting examples that are both uncertain and diverse.

The active learning loop works as follows: start with a small labeled seed set and train an initial model. Use the model to score all unlabeled examples according to the query strategy. Select the top-scoring examples (a batch), send them to the human annotator for labeling, add the new labels to the training set, retrain the model, and repeat. Each cycle makes the model smarter about what it does not know, producing a **learning curve** that typically rises much faster than random sampling. The practical result is that active learning can achieve the same accuracy as passive learning with 10–100× fewer labeled examples — a significant cost reduction when annotation is the bottleneck.
