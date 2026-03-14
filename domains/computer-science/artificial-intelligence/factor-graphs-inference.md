---
id: factor-graphs-inference
title: Factor Graphs and Inference
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: probabilistic-graphical-models
  type: hard
- id: bayesian-networks-inference
  type: soft
builds-toward:
- belief-propagation-algorithm
tags:
- graphical-models
- inference
- factorization
- bipartite-graphs
stage: advanced
status: draft
---

# Factor Graphs and Inference

## Core Idea
Factor graphs decompose joint distributions into factors (functions over subsets of variables), creating a bipartite graph with variable and factor nodes. This representation unifies Bayesian networks and Markov random fields and makes inference algorithms like sum-product and max-product rules more explicit and modular.
