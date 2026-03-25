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
- id: markov-random-fields
  type: soft
builds-toward:
- belief-propagation-algorithm
tags:
- graphical-models
- inference
- factorization
- bipartite-graphs
stage: advanced
status: validated
---
# Factor Graphs and Inference

## Core Idea
Factor graphs decompose joint distributions into factors (functions over subsets of variables), creating a bipartite graph with variable and factor nodes. This representation unifies Bayesian networks and Markov random fields and makes inference algorithms like sum-product and max-product rules more explicit and modular.

## Questions

```yaml
- question: "A Markov random field has a clique of three variables {A, B, C} with a single joint potential ψ(A,B,C). How does this appear in a factor graph?"
  type: multiple-choice
  options:
    - "As a triangle of three variable nodes with edges between them — the same structure as the MRF clique"
    - "As one factor node connected by edges to three variable nodes (A, B, C)"
    - "As three separate factor nodes, one per variable, each connected to the others"
    - "As a single variable node labeled ABC representing the joint state"
  answer: 1
  explanation: "In a factor graph, every factor gets its own explicit square node. A single potential ψ(A,B,C) becomes one factor node connected to all three variable nodes — a star pattern, not a triangle. This explicitness is the key advantage: an MRF clique might contain one factor or many factors, and the graph topology alone doesn't tell you which. Factor graphs resolve this by making each factor a visible node."

- question: "On a tree-structured factor graph, what does the sum-product algorithm guarantee?"
  type: multiple-choice
  options:
    - "Approximate marginals that converge after enough iterations"
    - "Exact joint distribution over all variables in the graph"
    - "Exact marginal distributions for all variables, computed in a single forward-backward message-passing pass"
    - "The most probable assignment of all variables via dynamic programming"
  answer: 2
  explanation: "On trees (no cycles), the sum-product algorithm computes exact marginals in a single pass: messages flow from leaves inward, then back outward, and each variable's marginal is the product of all incoming messages. There is no approximation and no iteration needed. The max-product algorithm does the analogous computation for the most probable configuration. Loops are the source of the exactness problem — on loopy graphs, belief propagation is approximate."

- question: "Loopy belief propagation on a factor graph with cycles always fails to converge and cannot produce useful results."
  type: true-false
  answer: false
  explanation: "False. While loopy belief propagation is not guaranteed to converge or give exact marginals, in practice it often converges and produces excellent approximate results. It is the backbone of modern error-correcting codes (LDPC, turbo codes) and computer vision algorithms. The lack of a convergence guarantee is a theoretical limitation, not a practical one in many important applications."

- question: "A factor graph can represent any distribution expressible as either a Bayesian network or a Markov random field."
  type: true-false
  answer: true
  explanation: "True. Factor graphs are a universal representation for graphical models. Any Bayesian network (directed, with CPTs) and any Markov random field (undirected, with potential functions) can be converted to a factor graph by creating one factor node for each conditional probability table or potential function. This universality is what makes factor graphs the preferred representation for unifying inference algorithms across model types."

- question: "What ambiguity in Markov random field representations do factor graphs resolve, and how do they resolve it?"
  type: short-answer
  answer: "In a Markov random field, a clique in the undirected graph could correspond to a single factor over all variables in the clique, or to a product of several smaller factors — the graph topology alone cannot distinguish these cases. Factor graphs resolve this by giving each factor its own explicit node in a bipartite graph. If P(a,b,c) = f₁(a,b) × f₂(b,c), the factor graph has two factor nodes (f₁, f₂), not one — making the factorization completely unambiguous."
  explanation: "This disambiguation matters for inference efficiency. If a clique factor actually decomposes into smaller subfactors, the message-passing algorithm can exploit that decomposition to reduce computation. Treating it as a single large factor when smaller factors exist wastes computation. Factor graphs make the true factorization explicit, so inference algorithms can always operate at the finest granularity available."
```

## Explainer

From your study of probabilistic graphical models and Bayesian networks, you know that a joint probability distribution over many variables can be factored into smaller, more manageable pieces. A Bayesian network expresses this factorization through conditional probability tables attached to a directed acyclic graph, while a Markov random field uses potential functions on an undirected graph. A **factor graph** is a more explicit representation that makes the factorization structure itself the primary object. It is a bipartite graph with two types of nodes: **variable nodes** (circles, representing random variables) and **factor nodes** (squares, representing functions over subsets of variables). An edge connects a variable node to a factor node if and only if that variable appears in that factor's function.

The advantage of factor graphs over Bayesian networks or Markov random fields is that they make the factorization completely unambiguous. In an undirected graphical model, a clique in the graph might correspond to one factor or to a product of several factors — the graph alone doesn't tell you. A factor graph resolves this ambiguity by giving each factor its own explicit node. For example, if P(a, b, c) = f₁(a, b) × f₂(b, c) × f₃(a, c), the factor graph has three variable nodes (a, b, c) and three factor nodes (f₁, f₂, f₃), with edges showing exactly which variables each factor depends on. Both Bayesian networks and Markov random fields can be converted into factor graphs, making factor graphs a **universal representation** for graphical models.

The real payoff of factor graphs is that they provide a clean substrate for inference algorithms. The **sum-product algorithm** (also called belief propagation) computes marginal distributions by passing messages between variable and factor nodes along the edges of the graph. Each message is a function (or vector) summarizing what one part of the graph "believes" about a variable. Variable-to-factor messages collect incoming information from all other factors connected to that variable; factor-to-variable messages marginalize the factor function over all other variables, weighted by incoming messages. On tree-structured factor graphs, this message passing converges in a single pass (forward then backward) and gives exact marginals. The **max-product algorithm** works identically but replaces summation with maximization, finding the most probable configuration instead of marginals.

When the factor graph has loops (cycles), exact inference via message passing is no longer guaranteed to converge or be correct, but **loopy belief propagation** — running the same message-passing rules iteratively until convergence — often works remarkably well in practice and is the backbone of applications from error-correcting codes (like LDPC and turbo codes) to computer vision. The modularity of factor graphs also makes them natural for building complex models incrementally: you can add new variables and factors without restructuring the entire model. This composability is why factor graphs are the preferred representation in many modern probabilistic programming frameworks and signal processing systems.
