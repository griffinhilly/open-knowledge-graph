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

## Explainer

From your study of factor graphs, you know that a joint probability distribution can be represented as a bipartite graph with variable nodes and factor nodes, where each factor encodes a local relationship between a subset of variables. The inference problem is to compute the marginal probability of each variable — that is, to sum out all other variables from the joint distribution. Doing this by brute force is exponential in the number of variables. **Belief propagation** (BP) solves this efficiently by breaking the global computation into local message-passing steps.

The algorithm works by sending **messages** along edges of the factor graph. There are two types. A message from a variable node x to a factor node f summarizes what x "believes" about its own state based on all factors *except* f. A message from a factor node f to a variable node x summarizes what f "thinks" x should be, given the local function and all messages from f's other neighboring variables. Each message is a function over the states of the receiving variable — think of it as an unnormalized probability vector. The **belief** at each variable node is the product of all incoming messages, normalized to sum to one. This gives the estimated marginal distribution.

On **tree-structured** factor graphs (graphs with no cycles), belief propagation is exact and terminates in a number of steps equal to the diameter of the tree. The reason is elegant: in a tree, every path between two nodes is unique, so messages carry independent information. You can think of it as a generalization of the forward-backward algorithm for hidden Markov models or the elimination algorithm for Bayesian networks — both are special cases of BP on tree-shaped graphs. The sum-product variant computes marginals; the closely related **max-product** (or min-sum in log space) variant computes the most probable configuration, analogous to the Viterbi algorithm.

When the factor graph has cycles — the **loopy** case — messages are no longer independent, because information can circulate around loops and be counted multiple times. Nevertheless, **loopy belief propagation** often works remarkably well in practice. The algorithm simply runs the same update rules iteratively until messages converge (or a maximum number of iterations is reached). It is the core inference engine behind turbo codes, LDPC codes in modern communication systems, and stereo vision algorithms in computer vision. Convergence is not guaranteed in general, and when it does converge, the marginals are approximate. Techniques like message damping (averaging new messages with old ones) and careful scheduling (updating messages in a strategic order rather than all at once) improve reliability. Understanding when and why loopy BP fails — for instance, on graphs with short, tight cycles — is an active area of research that connects to variational inference and the Bethe free energy approximation.
