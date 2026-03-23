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
status: validated
---

# Probabilistic Graphical Models

## Core Idea
Probabilistic graphical models represent joint probability distributions compactly using graph structure where nodes are variables and edges encode conditional independence. This enables efficient representation and inference when the joint distribution would be exponentially large; directed acyclic graphs represent Bayesian networks while undirected graphs represent Markov random fields.

## Questions

```yaml
- question: "A Bayesian network models 20 binary variables, where each variable has at most 3 parents. Compared to storing the full joint distribution, how does the network's storage requirement compare?"
  type: multiple-choice
  options:
    - "Roughly the same, because the network must still implicitly represent all 2^20 possible variable combinations"
    - "Exponentially smaller, because each variable's conditional probability table depends only on its parents, not all other variables"
    - "Slightly smaller, because the network removes redundant variables that are fully determined by others"
    - "Larger, because storing the graph structure plus all conditional tables requires more space than a flat lookup table"
  answer: 1
  explanation: "The full joint distribution over 20 binary variables requires 2^20 ≈ 1 million entries. With at most 3 parents, each variable's CPT has at most 2^3 = 8 rows × 2 columns = 16 entries, and there are 20 variables, for roughly 320 entries total. The savings come from conditional independence: once you know a variable's parents, knowing other variables adds no information about it. The factorization P(X₁,...,X₂₀) = ∏ P(Xᵢ | Parents(Xᵢ)) decomposes the exponentially large joint into a product of small local tables — this exponential savings in representation is the central reason PGMs are computationally tractable."

- question: "In a Bayesian network, variable X directly causes variable Y (X → Y). A new observation is made for variable Z, a distant descendant of Y. How does observing Z affect our beliefs about X?"
  type: multiple-choice
  options:
    - "Observing Z does not change beliefs about X because the causal arrow points away from X, not toward it"
    - "Observing Z updates beliefs about Y, and this change propagates up the causal chain to update beliefs about X"
    - "Observing Z makes X and Y conditionally independent, because Z screens off Y from X"
    - "Observing Z increases uncertainty about X because the downstream observation introduces conflicting information"
  answer: 1
  explanation: "In Bayesian networks, belief propagation flows in both directions, regardless of the direction of causal arrows. Observing Z tells us something about Y's likely value (since Z is caused by Y), and knowing more about Y tells us something about X's likely value (since X causes Y). This 'explaining away' or 'backward inference' is the core of Bayesian reasoning — causes and effects update each other bidirectionally. Option A is the classic misconception: thinking causal arrows block inference from going 'backward.' In probability, causation tells you the model structure; inference flows wherever the evidence leads."

- question: "The joint probability distribution in a Bayesian network factorizes as the product of each variable's conditional probability given its parents alone — this is what makes the network a compact representation."
  type: true-false
  answer: true
  explanation: "This factorization P(X₁,...,Xₙ) = ∏ P(Xᵢ | Parents(Xᵢ)) is the defining property of a Bayesian network. It is valid precisely because the graph encodes conditional independence: each variable is independent of its non-descendants given its parents. Without this independence structure, the factorization would not hold and you would need the full joint distribution. The graph structure is therefore not just a visualization — it is a formal assertion about which conditional independencies hold in the domain, and the factorization is the direct computational payoff of those assertions."

- question: "Adding more edges to a Bayesian network generally makes inference more efficient, because more connections allow information to flow more directly between related variables."
  type: true-false
  answer: false
  explanation: "More edges mean more conditional dependencies and fewer conditional independencies. Each additional edge can enlarge the parent sets of variables, increasing the size of their conditional probability tables exponentially (a variable with k parents has a CPT of size 2^k for binary variables). It also complicates the factorization: the joint distribution can be broken into fewer, larger local terms rather than many small ones. Efficient inference algorithms like variable elimination and belief propagation exploit sparsity — the fact that most variables are independent of most others. A densely connected graph is harder to reason about, not easier."

- question: "Why do probabilistic graphical models represent joint distributions much more compactly than explicitly enumerating all combinations, and what role does the graph structure play in enabling this?"
  type: short-answer
  answer: "The joint distribution over n variables takes exponential space to enumerate explicitly. A PGM represents the distribution compactly by encoding conditional independence relationships in the graph: each variable depends only on its neighbors (parents in a directed graph, clique members in an undirected graph), not on all other variables. The joint distribution factorizes into a product of small local terms, one per variable (or clique), each involving only a small subset of variables. The graph structure specifies exactly which variables each local term involves, making the factorization possible and turning an exponential representation problem into a polynomial one."
  explanation: "The key insight is that the graph is not just a picture of the model — it is a formal specification of conditional independencies, and those independencies are what enable the factorization. Without the independence structure, no compact representation is possible. Understanding this connection — graph topology → conditional independence → factorization → tractable representation and inference — is the conceptual core of PGMs."
```

## Explainer

Consider a medical diagnosis system with 50 binary symptoms and 20 possible diseases. The full joint probability distribution over all 70 variables would require storing 2^70 entries — more than a billion billion values. Yet most symptoms are conditionally independent given the underlying disease: once you know the patient has the flu, whether they have a runny nose tells you nothing new about whether they also have a fever. **Probabilistic graphical models** (PGMs) exploit exactly this kind of conditional independence structure to represent joint distributions compactly. Instead of enumerating every possible combination, a PGM encodes which variables directly influence which others, and the joint distribution factorizes into a product of small local functions.

You already know the most important type of PGM from your study of Bayesian networks. A **directed graphical model** (Bayesian network) uses a directed acyclic graph where each node stores a conditional probability table given only its parents. The joint distribution factorizes as the product of these local conditionals: P(X₁, X₂, ..., Xₙ) = ∏ P(Xᵢ | Parents(Xᵢ)). If each variable has at most k parents and takes d values, storage drops from d^n to n·d^(k+1) — an exponential savings. The graph structure also encodes conditional independence: a variable is conditionally independent of all non-descendants given its parents, which you can read directly from the topology using d-separation.

The second major family is **undirected graphical models** (Markov random fields), where edges have no direction and the distribution factorizes over cliques — fully connected subsets of nodes. Each clique has a **potential function** (a non-negative function of the clique's variables), and the joint distribution is proportional to the product of all clique potentials. Unlike Bayesian networks, the potentials are not probabilities and the distribution requires a normalization constant (the partition function). Undirected models naturally express symmetric relationships — pixels in an image influencing their neighbors, or atoms in a molecule affecting nearby atoms — where there is no natural causal direction.

The power of the PGM framework is that once you express a problem as a graph, generic algorithms handle inference and learning regardless of the specific domain. **Inference** — computing the probability of some variables given observed evidence — uses algorithms like variable elimination, belief propagation, or sampling methods that exploit the graph structure to avoid brute-force summation. The graph tells these algorithms the order in which to combine information, turning an intractable computation into a tractable one. This unifying framework connects Bayesian networks, Markov random fields, hidden Markov models, and many other probabilistic models under a single theoretical roof, where the graph structure is the key that makes reasoning practical.
