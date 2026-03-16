---
id: topic-modeling
title: Topic Modeling and Latent Dirichlet Allocation
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: nlp-language-models
  type: hard
builds-toward:
- document-understanding
- semantic-analysis
tags:
- topic-modeling
- lda
- latent-dirichlet
stage: advanced
status: draft
---

# Topic Modeling and Latent Dirichlet Allocation

## Core Idea
Topic modeling discovers abstract topics in document collections. Latent Dirichlet Allocation (LDA) models each document as a topic mixture and each topic as a word mixture. Topics are latent variables inferred via EM or Gibbs sampling. LDA enables document representations, theme discovery, and corpus organization.

## Explainer

Suppose you have thousands of news articles and want to discover what they are about — not by reading each one, but by having an algorithm automatically surface the recurring themes. **Topic modeling** does exactly this: it is an unsupervised technique that discovers abstract "topics" in a collection of documents. Unlike sentiment analysis or text classification where you provide labels, topic modeling finds structure you did not know was there, making it a powerful tool for exploratory analysis of large text corpora.

The most influential topic model is **Latent Dirichlet Allocation (LDA)**, which rests on an elegant generative story. LDA assumes each document was produced by a simple process: first, pick a mixture of topics (say, 30% sports, 50% politics, 20% economics); then, for each word in the document, pick a topic from that mixture and then pick a word from that topic's vocabulary distribution. A "topic" in LDA is just a probability distribution over words — the sports topic might assign high probability to "game," "score," "player," and "team," while the politics topic emphasizes "election," "policy," "vote," and "candidate." The model never sees these labels; it discovers the word clusters purely from co-occurrence patterns.

The challenge is that we only observe the documents — the topic mixtures and word assignments are **latent variables** that must be inferred. Since the exact posterior distribution is intractable, LDA uses approximate inference: either **Expectation-Maximization (EM)**, which iteratively estimates topic assignments and updates parameters, or **Gibbs sampling**, which repeatedly resamples each word's topic assignment conditioned on all other assignments until the distribution stabilizes. Both approaches converge to discover topics that explain the observed word patterns. The key hyperparameter is the number of topics *k*, which, like K-Means clustering, must be chosen by the modeler — too few topics are overly broad, too many fragment coherent themes.

What makes topic modeling practically valuable is the dual representation it produces. Each **document** gets a topic proportion vector (this article is 40% healthcare, 35% economics, 25% politics), and each **topic** gets a word distribution (the healthcare topic emphasizes "patient," "treatment," "hospital," "insurance"). These representations enable applications from document similarity and recommendation (find articles with similar topic profiles) to trend analysis (how has the prevalence of the climate topic changed over the past decade?) to content organization (automatically tag and categorize a large archive). While neural approaches like embedded topic models have extended the paradigm, LDA remains the conceptual foundation for understanding how latent structure can be extracted from text.
