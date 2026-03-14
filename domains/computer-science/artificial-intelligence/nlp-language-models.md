---
id: nlp-language-models
title: Language Models and Neural Language Modeling
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: transformer-architecture
  type: hard
tags:
- nlp
- language-models
- deep-learning
stage: advanced
status: draft
---

# Language Models and Neural Language Modeling

## Core Idea
Language models compute P(next_token|context) autoregressively. Neural LMs use RNNs or Transformers. Large pre-trained models (GPT, BERT) learn via self-supervised tasks: next-token (decoder) or masked token (encoder) prediction.
