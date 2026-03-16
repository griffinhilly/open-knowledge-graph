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

## Explainer

From your work with probabilistic graphical models, you know that a graphical model encodes a joint probability distribution by making independence assumptions explicit through graph structure. Bayesian networks use directed edges to represent conditional dependencies, which naturally express causal or generative stories: "A causes B, B causes C." But many real-world problems involve dependencies that are symmetric — neighboring pixels in an image influence each other without a clear causal direction, atoms in a crystal lattice interact mutually, and words in a sentence constrain each other bidirectionally. **Markov random fields** (MRFs) handle these situations by using undirected graphs, where an edge between two variables simply means "these two are directly related."

The key structural concept in an MRF is the **clique** — a subset of nodes that are all connected to each other. Instead of specifying conditional probability tables as in Bayesian networks, MRFs define **potential functions** (also called compatibility functions or factors) on cliques. A potential function assigns a non-negative score to each configuration of the variables in a clique, expressing how "compatible" those values are with each other. For example, in an image denoising MRF, a pairwise potential between neighboring pixels might assign a high score when both pixels have similar values and a low score when they differ sharply — encoding the prior belief that natural images are locally smooth. The joint distribution is proportional to the product of all clique potentials, but since potentials are not probabilities, you need a **partition function** Z to normalize everything into a proper distribution.

The Markov property in an MRF takes a spatial rather than temporal form: a variable is conditionally independent of all other variables given its **neighbors** in the graph. This is called the local Markov property, and it is what makes inference tractable — you only need to look at a variable's immediate neighborhood to reason about it. This connects to the Hammersley-Clifford theorem, which states that any distribution satisfying this Markov property with respect to an undirected graph can be factored as a product of potentials on the graph's cliques. The theorem provides the theoretical foundation linking graph structure to factorization.

Computing exact marginal probabilities or finding the most probable configuration in an MRF is generally intractable because the partition function Z requires summing over all possible configurations — exponential in the number of variables. Practical inference relies on approximate methods. **Belief propagation** passes messages between neighboring nodes, iteratively refining local beliefs about each variable's distribution. On tree-structured graphs, belief propagation is exact; on graphs with loops (which most real MRFs have), it becomes **loopy belief propagation**, an approximation that often works well in practice despite lacking formal guarantees. Other approaches include variational methods, which find a tractable distribution close to the true one, and sampling methods like Gibbs sampling, which draw samples from the joint distribution by iterating through variables one at a time, conditioning on neighbors — directly exploiting the local Markov property.
