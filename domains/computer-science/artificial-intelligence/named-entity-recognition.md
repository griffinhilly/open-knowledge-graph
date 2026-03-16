---
id: named-entity-recognition
title: Named Entity Recognition (NER)
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: nlp-language-models
  type: hard
- id: neural-networks-intro
  type: hard
- id: sequence-to-sequence-models
  type: soft
tags:
- nlp
- sequence-labeling
- entity-extraction
- information-extraction
stage: advanced
status: draft
---

# Named Entity Recognition (NER)

## Core Idea
Named entity recognition identifies and classifies named entities (people, organizations, locations, dates) in text as a sequence labeling task. BiLSTM-CRF models combine bidirectional context with Markov constraints on valid label transitions; transformer models achieve state-of-the-art performance through contextual embeddings that capture long-range dependencies.

## How It's Best Learned
Implement NER using BiLSTM-CRF and compare with transformer-based models (BERT fine-tuned), observing how architectural differences affect recognition accuracy and speed.

## Explainer

Named entity recognition is the task of scanning a sentence and identifying which words refer to real-world entities — and what kind of entity each one is. Given the sentence "Apple was founded by Steve Jobs in Cupertino in 1976," a NER system should tag "Apple" as an organization, "Steve Jobs" as a person, "Cupertino" as a location, and "1976" as a date. This is fundamentally a **sequence labeling** problem: each token in the input receives a label, and the model must decide the correct label for every position in the sequence.

The labeling scheme itself requires care. The standard approach is **BIO tagging** (Beginning, Inside, Outside): the first token of an entity gets a B-tag (e.g., B-PER for the start of a person name), continuation tokens get I-tags (I-PER), and non-entity tokens get O. This lets the model handle multi-word entities like "Steve Jobs" (B-PER I-PER) and distinguish adjacent entities of the same type. Without the B/I distinction, the model could not tell where one entity ends and the next begins.

The classic neural architecture for NER is the **BiLSTM-CRF**. You already know that neural networks can learn contextual representations — the BiLSTM reads the sentence in both directions, giving each token a representation informed by its full context. But sequence labeling has a structural constraint that a standard classifier ignores: adjacent labels are not independent. An I-PER tag should never follow a B-LOC tag, and an I-tag should never appear at the start of a sequence. The **CRF (Conditional Random Field)** layer on top of the BiLSTM learns a transition matrix between label pairs, scoring not just individual tag probabilities but entire label sequences. At inference time, the Viterbi algorithm efficiently finds the highest-scoring global label sequence rather than greedily picking the best tag at each position.

Transformer-based models like BERT have largely surpassed BiLSTM-CRFs by providing richer contextual embeddings. A fine-tuned BERT model for NER feeds its contextualized token representations into a classification head (with or without a CRF layer). The advantage is that BERT's pretraining on massive text corpora gives it deep knowledge of language structure and word usage patterns before it ever sees NER-labeled data. The word "Washington" in "Washington crossed the Delaware" and "Washington issued a statement" gets different contextual embeddings, helping the model distinguish person from organization or location uses. This contextual sensitivity, combined with the attention mechanism's ability to capture long-range dependencies, explains why transformer models achieve state-of-the-art NER performance across most benchmarks.
