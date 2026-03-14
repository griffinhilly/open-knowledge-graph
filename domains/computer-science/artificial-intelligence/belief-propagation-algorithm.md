---
id: belief-propagation-algorithm
title: Belief Propagation Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: factor-graphs-inference
  type: hard
- id: dynamic-programming-intro
  type: soft
tags:
- inference
- message-passing
- factor-graphs
- loopy-belief-propagation
stage: advanced
status: draft
---

# Belief Propagation Algorithm

## Core Idea
Belief propagation iteratively passes messages between variables and factors in a factor graph to compute marginal probabilities and max-marginals. It is exact on tree-structured graphs and an effective approximation on loopy graphs; the algorithm's convergence and quality depend on the graph structure and message scheduling.

## How It's Best Learned
Implement sum-product belief propagation on a factor graph and trace message updates to understand how beliefs propagate through the network.
