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

## Questions

```yaml
- question: "You are modeling whether neighboring pixels in a photograph should have similar colors. Which representation is most natural, and why?"
  type: multiple-choice
  options:
    - "A Bayesian network, because pixel A causes pixel B to have a similar color"
    - "A Markov random field, because the dependency between neighbors is symmetric — neither pixel causes the other"
    - "A hidden Markov model, because pixels form a sequence across rows"
    - "A naive Bayes classifier, because each pixel's color is conditionally independent of all others"
  answer: 1
  explanation: "Pixel dependencies in an image are symmetric: pixel A's value influences pixel B's, and B's influences A's equally — there is no causal direction. Bayesian networks require directed edges and encode causal stories ('A causes B'), which is unnatural here. MRFs use undirected edges that simply state 'these two are directly related,' exactly capturing the bidirectional smoothness prior. HMMs model sequential dependencies along a chain, not a 2D spatial grid. Naive Bayes assumes complete independence, which is the opposite of what we want."

- question: "In a Markov random field, what is the role of the partition function Z?"
  type: multiple-choice
  options:
    - "It counts the number of cliques in the graph"
    - "It normalizes the product of potential functions so the result is a valid probability distribution summing to 1"
    - "It stores the marginal probability of each variable"
    - "It measures how much the graph structure deviates from a tree"
  answer: 1
  explanation: "Potential functions assign non-negative scores to clique configurations but are not themselves probabilities — their product can be any positive number. The partition function Z is the sum of these products over all possible configurations of all variables; dividing by Z normalizes the distribution so it sums (or integrates) to 1, making it a valid probability distribution. Computing Z exactly is the main reason inference is intractable: it requires summing over an exponential number of configurations."

- question: "In a Markov random field, a variable is conditionally independent of all non-neighboring variables given the values of its immediate neighbors."
  type: true-false
  answer: true
  explanation: "This is the defining local Markov property of an MRF. Given all of a variable's neighbors, knowing the values of variables further away in the graph adds no information about the variable's distribution. This property is what makes local inference algorithms like Gibbs sampling practical: to sample a new value for a variable, you only need to look at its neighborhood, not the entire graph. The Hammersley-Clifford theorem proves this Markov property is equivalent to the clique-factorization structure of the joint distribution."

- question: "Potential functions in an MRF are probability distributions — each potential function must be non-negative and sum to 1 over its clique's configurations."
  type: true-false
  answer: false
  explanation: "Potential functions are not probability distributions and have no normalization requirement. They are arbitrary non-negative functions that encode compatibility (how 'good' a particular assignment of values to a clique is) — they can take any positive real value. The full joint distribution is proportional to the product of all potential functions, and the partition function Z provides the global normalization. Confusing potentials with probabilities is a common source of confusion when first working with MRFs."

- question: "Why is exact inference in a Markov random field generally intractable, and what structural property of the graph enables exact inference in special cases?"
  type: short-answer
  answer: "Exact inference requires computing marginal probabilities, which involves the partition function Z — the sum of the unnormalized joint distribution over all possible configurations of all variables. With n binary variables, this sum has 2^n terms, making it exponential in the number of variables. Exact inference is tractable only when the graph is a tree (or can be converted to one via junction tree methods), because trees have no loops, allowing messages to propagate exactly from leaves to root without double-counting. Belief propagation is exact on trees and becomes approximate (loopy belief propagation) on graphs with cycles."
  explanation: "The hardness of inference in MRFs is one of the central challenges of probabilistic graphical models. The exponential partition function is the culprit: even evaluating the probability of a single configuration requires knowing Z, which is a sum over all configurations. Trees are the exception because their acyclic structure allows a dynamic programming decomposition that computes marginals in polynomial time. Most real problems involve graphs with loops (images, protein contact maps, spatial grids), where approximate methods — belief propagation, variational inference, MCMC — are essential."
```

## Explainer

From your work with probabilistic graphical models, you know that a graphical model encodes a joint probability distribution by making independence assumptions explicit through graph structure. Bayesian networks use directed edges to represent conditional dependencies, which naturally express causal or generative stories: "A causes B, B causes C." But many real-world problems involve dependencies that are symmetric — neighboring pixels in an image influence each other without a clear causal direction, atoms in a crystal lattice interact mutually, and words in a sentence constrain each other bidirectionally. **Markov random fields** (MRFs) handle these situations by using undirected graphs, where an edge between two variables simply means "these two are directly related."

The key structural concept in an MRF is the **clique** — a subset of nodes that are all connected to each other. Instead of specifying conditional probability tables as in Bayesian networks, MRFs define **potential functions** (also called compatibility functions or factors) on cliques. A potential function assigns a non-negative score to each configuration of the variables in a clique, expressing how "compatible" those values are with each other. For example, in an image denoising MRF, a pairwise potential between neighboring pixels might assign a high score when both pixels have similar values and a low score when they differ sharply — encoding the prior belief that natural images are locally smooth. The joint distribution is proportional to the product of all clique potentials, but since potentials are not probabilities, you need a **partition function** Z to normalize everything into a proper distribution.

The Markov property in an MRF takes a spatial rather than temporal form: a variable is conditionally independent of all other variables given its **neighbors** in the graph. This is called the local Markov property, and it is what makes inference tractable — you only need to look at a variable's immediate neighborhood to reason about it. This connects to the Hammersley-Clifford theorem, which states that any distribution satisfying this Markov property with respect to an undirected graph can be factored as a product of potentials on the graph's cliques. The theorem provides the theoretical foundation linking graph structure to factorization.

Computing exact marginal probabilities or finding the most probable configuration in an MRF is generally intractable because the partition function Z requires summing over all possible configurations — exponential in the number of variables. Practical inference relies on approximate methods. **Belief propagation** passes messages between neighboring nodes, iteratively refining local beliefs about each variable's distribution. On tree-structured graphs, belief propagation is exact; on graphs with loops (which most real MRFs have), it becomes **loopy belief propagation**, an approximation that often works well in practice despite lacking formal guarantees. Other approaches include variational methods, which find a tractable distribution close to the true one, and sampling methods like Gibbs sampling, which draw samples from the joint distribution by iterating through variables one at a time, conditioning on neighbors — directly exploiting the local Markov property.
