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
