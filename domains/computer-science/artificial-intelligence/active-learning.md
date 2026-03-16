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

## Explainer

In standard supervised learning, you assume a fixed labeled dataset and train a model on all of it. Active learning flips this assumption: instead of passively receiving labeled data, the model gets to *choose* which examples it wants labeled next. The motivation is practical — in many real-world settings, unlabeled data is abundant but labeling is expensive. A medical imaging system may have access to millions of X-rays, but getting a radiologist to annotate each one costs time and money. If the model could identify the 500 most informative images to label instead of labeling 10,000 at random, you could achieve the same performance at a fraction of the cost.

The simplest and most widely used strategy is **uncertainty sampling**: the model examines the pool of unlabeled examples and selects the ones it is most uncertain about. For a classifier, this might mean choosing the example whose predicted class probabilities are closest to uniform — the example sitting right on the decision boundary. The intuition is that labeling these ambiguous examples gives the model the most information about where the boundary should be. If the model is already confident about an example, labeling it would just confirm what it already knows. But an example near the decision boundary, once labeled, can push the boundary in the right direction and improve accuracy across an entire region of the feature space.

**Diversity sampling** takes a complementary approach: instead of focusing on model uncertainty, it selects examples that are representative of the unlabeled data distribution. The concern with pure uncertainty sampling is that it can get stuck querying examples from a small, confusing region of the space — endlessly asking about borderline cases between two classes while ignoring an entire cluster of a third class it has never seen. Diversity-based methods, such as selecting examples that are far from any already-labeled point, ensure broader coverage. In practice, the best active learning strategies often combine both signals — selecting examples that are both uncertain and diverse.

The active learning loop works as follows: start with a small labeled seed set and train an initial model. Use the model to score all unlabeled examples according to the query strategy. Select the top-scoring examples (a batch), send them to the human annotator for labeling, add the new labels to the training set, retrain the model, and repeat. Each cycle makes the model smarter about what it does not know, producing a **learning curve** that typically rises much faster than random sampling. The practical result is that active learning can achieve the same accuracy as passive learning with 10–100× fewer labeled examples — a significant cost reduction when annotation is the bottleneck.
