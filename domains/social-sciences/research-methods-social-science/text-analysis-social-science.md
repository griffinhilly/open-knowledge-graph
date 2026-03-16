---
id: text-analysis-social-science
title: Computational Text Analysis for Social Data
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: content-analysis-systematic
  type: hard
- id: computational-social-science-intro
  type: soft
builds-toward:
- topic-modeling-lda
- sentiment-analysis-methods
tags:
- text
- nlp
- computational
- qualitative-quantitative
stage: advanced
status: draft
---

# Computational Text Analysis for Social Data

## Core Idea
Computational text analysis uses algorithms to extract patterns, themes, and meanings from large text corpora—news articles, social media, interviews, historical documents. Methods range from counting word frequencies and calculating sentiment to unsupervised topic modeling and supervised classification. These techniques bridge qualitative and quantitative approaches, enabling systematic analysis of textual data at scales humans cannot manually process.

## Explainer

You already know how to conduct content analysis: define categories, systematically code text, and report frequencies and patterns. Computational text analysis scales this process from hundreds of documents to millions, automating what human coders would take years to accomplish. The intellectual shift is not just about scale — it also changes which research questions become tractable.

The simplest computational approaches count words. **Bag-of-words** models treat a document as an unordered collection of tokens — word frequencies and co-occurrence patterns become the data, with grammar and sequence discarded. From your content analysis background, this resembles manifest coding without context. More useful are **dictionary methods**: you build or borrow a validated list of words associated with a concept (economic anxiety, democratic legitimacy, moral outrage) and measure how frequently those words appear across documents. Widely used examples include LIWC and Moral Foundations dictionaries. Dictionary methods are transparent and replicable but require confident prior theory about how the concept appears in language — a substantial assumption.

**Unsupervised methods** like Latent Dirichlet Allocation (LDA) **topic modeling** ask what themes organize a corpus without the researcher specifying them in advance. LDA treats each document as a mixture of topics and each topic as a probability distribution over words. The output is a set of word clusters that typically cohere around interpretable themes — "economy, jobs, wages, growth" cluster together because they appear in similar documents. The skill is interpreting what those statistical clusters mean substantively, which requires deep domain knowledge. The algorithm finds patterns; the researcher supplies meaning.

**Supervised classification** works differently: you hand-label a sample of documents (positive/negative sentiment, protest/non-protest, policy/non-policy), train a statistical model on those labels, and apply the trained model to classify the remaining corpus. This approach leverages human judgment at the labeling stage and scales it computationally. The danger is that the model learns whatever pattern the coders introduced — including their biases. Validation, transparent documentation of training data, and strong inter-coder reliability in the labeled sample are essential safeguards. Across all methods, computational text analysis is most powerful when it enables comparisons that humans genuinely cannot make manually: tracking how a political frame evolves across a decade of congressional speeches, mapping sentiment across millions of social media posts in real time, or detecting subtle differences in how rival news outlets cover the same event.
