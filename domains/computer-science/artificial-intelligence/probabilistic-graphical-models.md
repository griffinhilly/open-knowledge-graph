---
id: probabilistic-graphical-models
title: Probabilistic Graphical Models
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: bayesian-networks-inference
  type: hard
- id: probability-spaces-measure-theoretic
  type: soft
- id: probability-axioms-and-rules
  type: soft
- id: conditional-probability
  type: soft
builds-toward:
- markov-random-fields
- factor-graphs-inference
tags:
- probabilistic-reasoning
- inference
- graphical-models
- joint-distributions
stage: advanced
status: draft
---

# Probabilistic Graphical Models

## Core Idea
Probabilistic graphical models represent joint probability distributions compactly using graph structure where nodes are variables and edges encode conditional independence. This enables efficient representation and inference when the joint distribution would be exponentially large; directed acyclic graphs represent Bayesian networks while undirected graphs represent Markov random fields.
