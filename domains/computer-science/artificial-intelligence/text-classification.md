---
id: text-classification
title: Text Classification
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: nlp-language-models
  type: hard
- id: supervised-learning-intro
  type: hard
builds-toward:
- sentiment-analysis-nlp
- intent-detection
tags:
- text-classification
- document-classification
stage: advanced
status: draft
---

# Text Classification

## Core Idea
Text classification assigns documents to predefined categories (spam, sentiment, topic, intent). Approaches range from TF-IDF with logistic regression to RNNs and Transformers. Class imbalance, large vocabularies, and variable document lengths are common challenges. Transfer learning from pretrained language models (BERT, GPT) dramatically improves performance.
