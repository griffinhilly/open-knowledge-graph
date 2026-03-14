---
id: markov-random-fields
title: Markov Random Fields
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: probabilistic-graphical-models
  type: hard
- id: hidden-markov-models
  type: soft
builds-toward:
- factor-graphs-inference
tags:
- graphical-models
- undirected-graphs
- inference
- cliques
stage: advanced
status: draft
---

# Markov Random Fields

## Core Idea
Markov random fields (undirected graphical models) represent joint distributions using potential functions on cliques, where a variable's conditional distribution depends only on its neighbors. They are symmetric in dependencies (unlike directed Bayesian networks) and are natural for image processing, spatial modeling, and problems without clear causality.

## How It's Best Learned
Implement inference in a simple MRF for image denoising or texture synthesis using belief propagation.
