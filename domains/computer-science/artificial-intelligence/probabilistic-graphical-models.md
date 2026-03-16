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

## Explainer

Consider a medical diagnosis system with 50 binary symptoms and 20 possible diseases. The full joint probability distribution over all 70 variables would require storing 2^70 entries — more than a billion billion values. Yet most symptoms are conditionally independent given the underlying disease: once you know the patient has the flu, whether they have a runny nose tells you nothing new about whether they also have a fever. **Probabilistic graphical models** (PGMs) exploit exactly this kind of conditional independence structure to represent joint distributions compactly. Instead of enumerating every possible combination, a PGM encodes which variables directly influence which others, and the joint distribution factorizes into a product of small local functions.

You already know the most important type of PGM from your study of Bayesian networks. A **directed graphical model** (Bayesian network) uses a directed acyclic graph where each node stores a conditional probability table given only its parents. The joint distribution factorizes as the product of these local conditionals: P(X₁, X₂, ..., Xₙ) = ∏ P(Xᵢ | Parents(Xᵢ)). If each variable has at most k parents and takes d values, storage drops from d^n to n·d^(k+1) — an exponential savings. The graph structure also encodes conditional independence: a variable is conditionally independent of all non-descendants given its parents, which you can read directly from the topology using d-separation.

The second major family is **undirected graphical models** (Markov random fields), where edges have no direction and the distribution factorizes over cliques — fully connected subsets of nodes. Each clique has a **potential function** (a non-negative function of the clique's variables), and the joint distribution is proportional to the product of all clique potentials. Unlike Bayesian networks, the potentials are not probabilities and the distribution requires a normalization constant (the partition function). Undirected models naturally express symmetric relationships — pixels in an image influencing their neighbors, or atoms in a molecule affecting nearby atoms — where there is no natural causal direction.

The power of the PGM framework is that once you express a problem as a graph, generic algorithms handle inference and learning regardless of the specific domain. **Inference** — computing the probability of some variables given observed evidence — uses algorithms like variable elimination, belief propagation, or sampling methods that exploit the graph structure to avoid brute-force summation. The graph tells these algorithms the order in which to combine information, turning an intractable computation into a tractable one. This unifying framework connects Bayesian networks, Markov random fields, hidden Markov models, and many other probabilistic models under a single theoretical roof, where the graph structure is the key that makes reasoning practical.
