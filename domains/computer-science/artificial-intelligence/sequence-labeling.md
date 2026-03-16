---
id: sequence-labeling
title: Sequence Labeling and CRFs
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: named-entity-recognition
  type: soft
- id: hidden-markov-models
  type: hard
builds-toward:
- structured-prediction
- dependency-parsing
tags:
- sequence-labeling
- crf
- structured
stage: advanced
status: draft
---

# Sequence Labeling and CRFs

## Core Idea
Sequence labeling assigns labels to each element in a sequence (part-of-speech tagging, named entity recognition). Conditional Random Fields (CRFs) model label dependencies, capturing that consecutive labels influence each other. As discriminative models, CRFs typically outperform generative HMMs for sequence labeling tasks.

## Explainer

From your study of Hidden Markov Models, you understand the basic structure of sequence labeling: given a sequence of observations (words in a sentence, characters in a string, signals in a time series), assign a label to each position. In part-of-speech tagging, the input "The cat sat" gets labels [DET, NOUN, VERB]. In named entity recognition, "Barack Obama visited Paris" might get [B-PER, I-PER, O, B-LOC]. The challenge is that labels are not independent — knowing the current word is tagged as a determiner makes it much more likely that the next word is a noun.

HMMs handle these dependencies by modeling the joint probability P(observations, labels) as a product of emission probabilities (how likely is this word given this tag?) and transition probabilities (how likely is this tag given the previous tag?). But HMMs make a strong independence assumption: the probability of observing a word depends *only* on its tag, not on the surrounding words or any other features. This means an HMM cannot easily use rich features like "the word ends in -ing" or "the previous word is capitalized" without dramatically expanding the state space.

**Conditional Random Fields (CRFs)** solve this by modeling the conditional probability P(labels | observations) directly, without modeling how observations are generated. This discriminative approach means CRFs can incorporate arbitrary **feature functions** that examine any part of the input sequence — the current word, neighboring words, capitalization patterns, suffixes, prefixes — without worrying about their joint distribution. A linear-chain CRF defines a score for each label sequence as a weighted sum of feature functions evaluated at each position and each pair of adjacent labels, then normalizes over all possible label sequences to produce a valid probability distribution.

Training a CRF means finding feature weights that maximize the conditional likelihood of the correct label sequences in the training data. Inference — finding the most probable label sequence for a new input — uses the **Viterbi algorithm**, the same dynamic programming approach you learned for HMMs. The partition function (normalizing constant) is computed with the **forward algorithm**, again borrowed from HMMs. The algorithmic machinery is familiar; the difference is entirely in what is being modeled. Because CRFs are discriminative and feature-rich, they consistently outperform HMMs on tasks like POS tagging and NER. Modern systems often combine a neural network (BiLSTM or Transformer) to produce contextualized features with a CRF layer on top to enforce label consistency — getting the best of learned representations and structured prediction.
