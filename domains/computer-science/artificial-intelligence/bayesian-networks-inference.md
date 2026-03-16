---
id: bayesian-networks-inference
title: Bayesian Networks and Inference
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: bayes-theorem-and-inference
  type: hard
- id: conditional-probability
  type: hard
- id: bayes-theorem
  type: soft
tags:
- probabilistic-reasoning
- graphical-models
- inference
stage: advanced
status: draft
---

# Bayesian Networks and Inference

## Core Idea
Bayesian networks encode conditional independence as directed acyclic graphs, with nodes representing variables and edges indicating dependencies. Inference computes posterior probabilities of unknown variables given observations. Exact inference uses message passing; approximate methods use sampling.

## Explainer

You already know Bayes' theorem: P(A|B) = P(B|A)P(A)/P(B). This works beautifully for updating a single hypothesis given evidence. But real-world reasoning involves many interrelated variables — a patient's symptoms, test results, medical history, and possible diseases all influence each other. Computing the full joint probability distribution over n binary variables requires 2ⁿ entries, which quickly becomes intractable. **Bayesian networks** solve this by exploiting the fact that most variables are conditionally independent of most other variables, dramatically reducing the number of parameters needed.

A Bayesian network is a **directed acyclic graph (DAG)** where each node represents a random variable and each directed edge represents a direct dependency. The key structural assumption is that each variable is conditionally independent of its non-descendants given its parents. This means that instead of storing the full joint distribution, you only need to store a **conditional probability table (CPT)** for each node given its parents. For example, in a medical diagnosis network, the node "Cough" might depend on "Flu" and "Lung Disease" but be conditionally independent of "Headache" once you know the state of those two diseases. The joint probability of all variables factors as: P(X₁, ..., Xₙ) = ∏ P(Xᵢ | parents(Xᵢ)), which is the chain rule of probability simplified by conditional independence.

**Inference** is the process of computing the posterior probability of some query variables given observed evidence. Suppose you observe that a patient has a cough and fever — what is the probability they have the flu? This requires summing over all possible states of the unobserved variables, weighted by their probabilities. For tree-structured networks, exact inference can be done efficiently using **message passing** (also called belief propagation): each node sends messages to its neighbors summarizing the evidence below it, and these messages propagate through the tree in two passes (leaves-to-root, then root-to-leaves). For more general networks, exact algorithms like **variable elimination** systematically sum out variables in an efficient order, and **junction tree** methods convert the network into a tree structure that supports exact message passing.

When the network is too large or densely connected for exact inference, **approximate methods** become necessary. The most common approach is **Monte Carlo sampling**: generate many random samples from the joint distribution, then estimate posterior probabilities by counting how often the query variables take particular values among samples consistent with the evidence. Variants like **likelihood weighting** and **Gibbs sampling** improve efficiency by focusing samples on configurations compatible with observed evidence rather than wasting samples on unlikely states. The power of Bayesian networks lies in making probabilistic reasoning tractable — they let you answer complex "what if" questions about systems with dozens or hundreds of interacting variables, from medical diagnosis to spam filtering to fault detection in industrial systems.
