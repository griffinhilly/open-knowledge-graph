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

## Questions

```yaml
- question: "The Word2Vec Skip-gram model learns word embeddings by:"
  type: multiple-choice
  options:
    - "Counting how often each pair of words co-occurs across the entire corpus, then factorizing the resulting matrix"
    - "Training a shallow neural network to predict surrounding context words given a center word"
    - "Assigning random dense vectors and iteratively adjusting them based on word frequency rankings"
    - "Encoding each word as a weighted sum of the vectors of its definition words"
  answer: 1
  explanation: "Skip-gram trains a network on a prediction task: given a target word, predict the words in its surrounding context window. The hidden layer weights after training become the word vectors. Option A describes GloVe (Global Vectors), which factorizes a global co-occurrence matrix — a different approach that incorporates corpus-wide statistics rather than local context windows. Options C and D are not how any standard embedding method works."

- question: "A well-trained embedding model produces the result: vec('Paris') − vec('France') + vec('Germany') ≈ vec('Berlin'). This works because:"
  type: multiple-choice
  options:
    - "The model memorized that Paris and Berlin are both capital cities from explicit labels in the training data"
    - "Cities that frequently appear together in the same sentence end up geometrically close in the embedding space"
    - "The embedding space encodes the 'capital city of' relationship as a consistent geometric direction, so subtracting and adding that direction navigates the analogy"
    - "GloVe's co-occurrence matrix directly encodes country-capital pairs as high co-occurrence counts"
  answer: 2
  explanation: "The vector arithmetic works because the distributional hypothesis causes the embedding space to organize semantically consistent relationships as consistent geometric offsets. The direction from 'France' to 'Paris' (capital relationship) is approximately the same direction as from 'Germany' to 'Berlin.' Subtracting 'France' from 'Paris' isolates this direction, then adding it to 'Germany' lands near 'Berlin.' This is not memorization or direct co-occurrence — it emerges from learning the contexts in which words appear."

- question: "In one-hot encoding, the vectors for 'cat' and 'kitten' are geometrically closer to each other than to 'airplane,' because cats and kittens are semantically related."
  type: true-false
  answer: false
  explanation: "False. One-hot vectors are mutually orthogonal — every pair of distinct words has a dot product of exactly zero and the same Euclidean distance. 'Cat' is geometrically identical in distance to 'kitten' and to 'airplane.' This is the fundamental failure of one-hot encoding: it encodes no semantic information whatsoever. Word embeddings were invented precisely to fix this — dense vectors learned from distributional patterns place semantically similar words close together in vector space."

- question: "The distributional hypothesis — the theoretical foundation of word embeddings — holds that words appearing in similar contexts tend to have similar meanings."
  type: true-false
  answer: true
  explanation: "True. This hypothesis, attributed to linguists like Firth ('a word is characterized by the company it keeps'), is the entire basis for learning meaningful word representations from raw text. If 'dog' and 'cat' both appear near words like 'pet,' 'feed,' 'veterinarian,' and 'bark/meow,' their context vectors will be similar — and their learned embeddings will reflect this shared semantic territory. The hypothesis is not perfect (polysemous words like 'bank' appear in very different contexts), but it is powerful enough to produce embeddings that encode grammar, analogy, and semantic similarity."

- question: "Why does Word2Vec learn semantically meaningful word representations even though it is trained on the seemingly simple task of predicting context words, with no explicit semantic labels?"
  type: short-answer
  answer: "Words with similar meanings naturally appear in similar linguistic contexts. To predict context words accurately, the model must learn to group together words that are interchangeable in context — which turns out to be a strong proxy for semantic similarity. The training signal forces the hidden layer to compress distributional patterns into dense vectors, and those patterns happen to encode meaning. Semantic content is latent in the statistics of how words co-occur, and the prediction task is the mechanism for extracting it."
  explanation: "This is the key insight: the task (next-word prediction) is not the goal, it is the scaffold. By solving the prediction task well, the model is implicitly forced to build internal representations that capture meaning — because meaning is what determines context. This is a general principle of representation learning: a model trained on a structured prediction task often learns representations that encode the underlying structure of the data, even without explicit supervision on that structure."
```

## Explainer

Before word embeddings, the standard way to represent words for machine learning was **one-hot encoding**: each word gets a vector with a single 1 and all other entries 0. In a vocabulary of 50,000 words, "king" might be [0, 0, ..., 1, ..., 0] and "queen" would be a completely different sparse vector. The problem is immediate: these vectors are orthogonal to each other, so the dot product between any two words is zero. The representation carries no information about meaning — "king" is as far from "queen" as it is from "toaster." Word embeddings solve this by learning dense, low-dimensional vectors (typically 100–300 dimensions) where semantic similarity is encoded as geometric proximity.

The breakthrough insight behind **Word2Vec** is the distributional hypothesis: words that appear in similar contexts have similar meanings. The **Skip-gram** model operationalizes this by training a shallow neural network on a simple task — given a target word, predict the words that surround it in a text corpus. The network has a single hidden layer whose weights, after training, become the word vectors. Words that predict similar context words end up with similar vectors. The **CBOW** (Continuous Bag of Words) variant reverses the task: given the surrounding context, predict the center word. Both approaches are remarkably efficient to train on large corpora because they avoid the full softmax over the vocabulary, using techniques like negative sampling instead.

**GloVe** (Global Vectors) takes a different approach. Rather than learning from local context windows, GloVe constructs a global word co-occurrence matrix — counting how often each pair of words appears together across the entire corpus — and then factorizes this matrix to produce vectors. The objective function is designed so that the dot product of two word vectors approximates the logarithm of their co-occurrence probability. This merges the advantages of count-based methods (which capture global statistics) with the embedding approach (which produces dense, useful vectors).

The most striking property of well-trained embeddings is that they encode semantic relationships as **vector arithmetic**. The famous example: vec("king") − vec("man") + vec("woman") ≈ vec("queen"). The direction from "man" to "woman" captures a gender relationship, and adding that direction to "king" lands near "queen." This works because the embedding space organizes concepts along consistent axes of meaning. In practice, pretrained word embeddings serve as the input representation for downstream NLP tasks — sentiment analysis, named entity recognition, machine translation — providing a rich starting point that encodes linguistic knowledge learned from billions of words of text.
