---
id: sentiment-analysis-nlp
title: Sentiment Analysis in NLP
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: nlp-language-models
  type: hard
- id: neural-networks-intro
  type: hard
- id: word-embeddings
  type: soft
tags:
- nlp
- text-classification
- sentiment
- opinion-mining
stage: advanced
status: draft
---

# Sentiment Analysis in NLP

## Core Idea
Sentiment analysis classifies text as positive, negative, or neutral by learning associations between words/phrases and sentiment labels. Approaches range from bag-of-words with linear classifiers to RNNs and transformers that capture context and word interactions; aspect-based sentiment analysis distinguishes opinions about different entities or aspects within text.

## How It's Best Learned
Train sentiment classifiers using different approaches (Naive Bayes, logistic regression, LSTM, transformer) and compare their ability to handle negation, sarcasm, and domain-specific language.

## Explainer

**Sentiment analysis** is the task of automatically determining whether a piece of text expresses a positive, negative, or neutral opinion. It is one of the most intuitive NLP applications because it maps directly to something humans do constantly — reading a product review and deciding whether the reviewer liked the product. Building on your understanding of language models, neural networks, and word embeddings, sentiment analysis shows how these tools combine to solve a concrete text classification problem.

The simplest approach treats text as a **bag of words**: ignore word order, count how often each word appears, and feed those counts into a classifier like logistic regression or Naive Bayes. This works surprisingly well for many cases because sentiment-bearing words ("excellent," "terrible," "disappointing") are strong signals on their own. But bag-of-words models fail on constructions where context matters. "Not bad" is positive despite containing "bad." "I expected it to be great but it wasn't" is negative despite containing "great" and "expected." These failures reveal why sequential and contextual models are needed.

Neural approaches address these limitations by preserving word order and learning contextual representations. Word embeddings give each word a dense vector capturing semantic similarity, so the model knows that "fantastic" and "excellent" are related even without seeing both in training data. RNNs and LSTMs process the sentence sequentially, building up a representation that captures how words modify each other — so the negation in "not good" flips the sentiment of "good." Transformer-based models like BERT go further, using bidirectional attention to understand that in "The food was great but the service was awful," the sentiment toward food and service are different and both must be captured.

This last observation leads to **aspect-based sentiment analysis**, which goes beyond assigning a single label to an entire text. A restaurant review might be positive about food but negative about wait times. Aspect-based systems identify the **target entities** (food, service, ambiance) and assign separate sentiment labels to each. This requires the model to associate opinion words with their targets, a harder problem that leverages the full power of contextual language models. Whether you are building a simple review classifier or a fine-grained opinion mining system, the progression from bag-of-words to contextual models illustrates a recurring theme in NLP: capturing more context almost always improves performance, at the cost of more data and computation.
