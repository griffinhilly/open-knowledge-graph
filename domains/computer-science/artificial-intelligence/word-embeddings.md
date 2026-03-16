---
id: word-embeddings
title: Word Embeddings and Representations
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: neural-networks-intro
  type: hard
- id: vector-spaces-definition
  type: soft
- id: dot-product
  type: soft
- id: vector-spaces
  type: soft
tags:
- nlp
- embeddings
- representation-learning
stage: advanced
status: draft
---

# Word Embeddings and Representations

## Core Idea
Word embeddings map words to dense vectors capturing semantic relationships. Word2Vec (Skip-gram, CBOW) learns via context prediction; GloVe combines local and global statistics. Embeddings enable arithmetic operations and transfer to downstream tasks.

## Explainer

Before word embeddings, the standard way to represent words for machine learning was **one-hot encoding**: each word gets a vector with a single 1 and all other entries 0. In a vocabulary of 50,000 words, "king" might be [0, 0, ..., 1, ..., 0] and "queen" would be a completely different sparse vector. The problem is immediate: these vectors are orthogonal to each other, so the dot product between any two words is zero. The representation carries no information about meaning — "king" is as far from "queen" as it is from "toaster." Word embeddings solve this by learning dense, low-dimensional vectors (typically 100–300 dimensions) where semantic similarity is encoded as geometric proximity.

The breakthrough insight behind **Word2Vec** is the distributional hypothesis: words that appear in similar contexts have similar meanings. The **Skip-gram** model operationalizes this by training a shallow neural network on a simple task — given a target word, predict the words that surround it in a text corpus. The network has a single hidden layer whose weights, after training, become the word vectors. Words that predict similar context words end up with similar vectors. The **CBOW** (Continuous Bag of Words) variant reverses the task: given the surrounding context, predict the center word. Both approaches are remarkably efficient to train on large corpora because they avoid the full softmax over the vocabulary, using techniques like negative sampling instead.

**GloVe** (Global Vectors) takes a different approach. Rather than learning from local context windows, GloVe constructs a global word co-occurrence matrix — counting how often each pair of words appears together across the entire corpus — and then factorizes this matrix to produce vectors. The objective function is designed so that the dot product of two word vectors approximates the logarithm of their co-occurrence probability. This merges the advantages of count-based methods (which capture global statistics) with the embedding approach (which produces dense, useful vectors).

The most striking property of well-trained embeddings is that they encode semantic relationships as **vector arithmetic**. The famous example: vec("king") − vec("man") + vec("woman") ≈ vec("queen"). The direction from "man" to "woman" captures a gender relationship, and adding that direction to "king" lands near "queen." This works because the embedding space organizes concepts along consistent axes of meaning. In practice, pretrained word embeddings serve as the input representation for downstream NLP tasks — sentiment analysis, named entity recognition, machine translation — providing a rich starting point that encodes linguistic knowledge learned from billions of words of text.
