---
id: phylogenetic-inference-methods
title: 'Phylogenetic Inference: Parsimony, Distance, and Maximum Likelihood'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: cladistics-and-systematics
  type: hard
- id: evolutionary-comparative-anatomy
  type: soft
- id: statistical-inference
  type: soft
- id: hypothesis-testing-framework
  type: soft
- id: bayesian-inference-intro
  type: soft
- id: probability-mass-functions
  type: soft
builds-toward:
- molecular-dating-phylogenetic-clocks
- molecular-evolution-phylogenetics
tags:
- phylogenetics
- methods
- inference
- statistics
stage: advanced
status: draft
---

# Phylogenetic Inference: Parsimony, Distance, and Maximum Likelihood

## Core Idea
Phylogenetic trees are reconstructed using methods that make different assumptions: maximum parsimony finds trees requiring fewest changes; distance methods cluster species by overall similarity; maximum likelihood finds the tree most probable under a specified evolutionary model. Each method has strengths and limitations, and disagreement between methods can highlight data limitations. Modern phylogenetics integrates multiple methods and data types for robust inference.

## Explainer

From cladistics and systematics, you know that phylogenetic trees represent hypotheses about evolutionary relationships — branching diagrams showing which species share more recent common ancestors. The challenge is that we cannot directly observe the past: we must *infer* the tree from data available today, whether morphological characters or DNA sequences. Phylogenetic inference methods are the statistical and algorithmic tools that take a matrix of character data and produce the best-supported tree. The three major approaches — parsimony, distance, and likelihood — differ fundamentally in how they define "best."

**Maximum parsimony** operates on a simple principle borrowed from Occam's razor: the best tree is the one requiring the fewest evolutionary changes to explain the observed data. For each possible tree topology, you count how many character-state changes (mutations, morphological transitions) are needed to map the data onto that tree, and you select the tree with the smallest total. Parsimony is intuitive and makes minimal assumptions about the evolutionary process. However, it can be misled when evolution is fast or uneven — a problem called **long-branch attraction**, where distantly related lineages that have evolved rapidly accumulate convergent similarities and get grouped together incorrectly. If you have studied hypothesis testing, you can think of parsimony as choosing the simplest explanation, but simplicity is not always accuracy when the underlying process is complex.

**Distance methods** take a different approach entirely. Instead of examining individual characters, they first collapse the data into a single number for each pair of species: the **evolutionary distance**, typically the fraction of sites that differ between two sequences (corrected for multiple substitutions at the same site). Then they use clustering algorithms — most commonly **neighbor-joining** — to build a tree by progressively grouping the most similar pairs. Distance methods are computationally fast, which matters when you have hundreds or thousands of species, but they discard information by reducing the full character matrix to pairwise distances. Two very different patterns of change can produce the same distance, so some phylogenetic signal is inevitably lost.

**Maximum likelihood** is the most statistically rigorous approach. It requires an explicit model of evolution — for DNA data, this specifies the rates at which each nucleotide substitutes for every other. Given a proposed tree and a model, you calculate the probability that the model would produce the observed data on that tree. The tree with the highest probability (likelihood) is the maximum likelihood estimate. This approach can account for unequal rates across sites, different substitution rates between nucleotide pairs, and variation in evolutionary rate across lineages. If you have encountered Bayesian inference, you will recognize that the Bayesian extension of phylogenetics goes one step further: it combines the likelihood with prior probabilities on tree topologies and model parameters to produce a posterior distribution of trees, often summarized as a consensus tree with support values at each node. Maximum likelihood and Bayesian methods are computationally demanding but generally outperform parsimony and distance methods when the data are complex or the evolutionary signal is weak. In practice, modern phylogenetic studies run multiple methods and look for agreement — nodes supported by all approaches are considered robust, while conflicts flag areas where more data or better models are needed.
