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

## Explainer

From your study of probabilistic graphical models and Bayesian networks, you know that a joint probability distribution over many variables can be factored into smaller, more manageable pieces. A Bayesian network expresses this factorization through conditional probability tables attached to a directed acyclic graph, while a Markov random field uses potential functions on an undirected graph. A **factor graph** is a more explicit representation that makes the factorization structure itself the primary object. It is a bipartite graph with two types of nodes: **variable nodes** (circles, representing random variables) and **factor nodes** (squares, representing functions over subsets of variables). An edge connects a variable node to a factor node if and only if that variable appears in that factor's function.

The advantage of factor graphs over Bayesian networks or Markov random fields is that they make the factorization completely unambiguous. In an undirected graphical model, a clique in the graph might correspond to one factor or to a product of several factors — the graph alone doesn't tell you. A factor graph resolves this ambiguity by giving each factor its own explicit node. For example, if P(a, b, c) = f₁(a, b) × f₂(b, c) × f₃(a, c), the factor graph has three variable nodes (a, b, c) and three factor nodes (f₁, f₂, f₃), with edges showing exactly which variables each factor depends on. Both Bayesian networks and Markov random fields can be converted into factor graphs, making factor graphs a **universal representation** for graphical models.

The real payoff of factor graphs is that they provide a clean substrate for inference algorithms. The **sum-product algorithm** (also called belief propagation) computes marginal distributions by passing messages between variable and factor nodes along the edges of the graph. Each message is a function (or vector) summarizing what one part of the graph "believes" about a variable. Variable-to-factor messages collect incoming information from all other factors connected to that variable; factor-to-variable messages marginalize the factor function over all other variables, weighted by incoming messages. On tree-structured factor graphs, this message passing converges in a single pass (forward then backward) and gives exact marginals. The **max-product algorithm** works identically but replaces summation with maximization, finding the most probable configuration instead of marginals.

When the factor graph has loops (cycles), exact inference via message passing is no longer guaranteed to converge or be correct, but **loopy belief propagation** — running the same message-passing rules iteratively until convergence — often works remarkably well in practice and is the backbone of applications from error-correcting codes (like LDPC and turbo codes) to computer vision. The modularity of factor graphs also makes them natural for building complex models incrementally: you can add new variables and factors without restructuring the entire model. This composability is why factor graphs are the preferred representation in many modern probabilistic programming frameworks and signal processing systems.
