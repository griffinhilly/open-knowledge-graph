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

## Explainer

Text classification is the task of assigning a document — an email, a tweet, a product review, a support ticket — to one or more predefined categories. You have already encountered supervised learning and language models as prerequisites, and text classification sits at their intersection: it applies supervised learning to text data, using the representations that language modeling provides. The fundamental challenge is that text is variable-length, unstructured, and high-dimensional. A vocabulary of 50,000 words means each document lives in a 50,000-dimensional space, most of which is zeros. The history of text classification is largely a story of finding better ways to represent documents as fixed-length numerical vectors that classifiers can consume.

The classical approach is **bag-of-words** with **TF-IDF** weighting. Each document becomes a vector of word frequencies, weighted so that common words like "the" count less and distinctive words like "mortgage" count more. A logistic regression or support vector machine trained on these vectors works surprisingly well for many tasks — spam detection, topic classification, language identification. The bag-of-words representation discards word order entirely ("dog bites man" and "man bites dog" are identical), yet for many classification tasks, the presence or absence of key words carries most of the signal. This is the same insight that makes naive Bayes effective: which words appear matters more than how they are arranged, at least for coarse categorization.

When word order and context matter — as in sentiment analysis, where "not good" means the opposite of "good" — sequential and contextual models take over. Recurrent neural networks process text word by word, maintaining a hidden state that accumulates context, and the final hidden state serves as a document representation for classification. Convolutional models slide filters over word sequences to capture local n-gram patterns. But the dominant modern approach is **transfer learning** from pretrained Transformer-based language models like BERT. These models are trained on massive text corpora to develop rich, contextual word representations, and they can be **fine-tuned** for classification by adding a simple classification layer on top. Fine-tuning adapts the general language understanding to your specific task with relatively little labeled data — a few thousand examples often suffice where bag-of-words methods might need tens of thousands.

Practical text classification involves several recurring challenges. **Class imbalance** is common: in fraud detection, 99.9% of transactions are legitimate, so a classifier that always predicts "not fraud" achieves 99.9% accuracy while being useless. Strategies include oversampling the minority class, undersampling the majority, or adjusting the loss function to penalize minority-class errors more heavily. **Preprocessing** decisions — lowercasing, stemming, removing stop words, handling out-of-vocabulary tokens — can significantly affect performance, especially for classical methods. And **evaluation** must go beyond accuracy: precision, recall, and F1-score per class reveal whether the model is actually learning the categories you care about, particularly the rare ones.
