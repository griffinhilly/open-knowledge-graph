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
