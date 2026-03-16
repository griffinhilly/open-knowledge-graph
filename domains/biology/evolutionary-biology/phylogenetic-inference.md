---
id: phylogenetic-inference
title: Phylogenetic Inference Fundamentals
domain: biology
course: evolutionary-biology
prerequisites:
- id: phylogenetics-intro
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- maximum-likelihood-phylogenetics
- bayesian-phylogenetics
- parsimony-phylogenetics
tags:
- phylogenetics
- evolution
- methods
stage: advanced
status: draft
---

# Phylogenetic Inference Fundamentals

## Core Idea
Phylogenetic inference reconstructs evolutionary relationships among organisms using genetic or morphological data. Core approaches (parsimony, likelihood, Bayesian) differ in assumptions and computational costs but share the goal of finding the tree topology and branch lengths best supported by data.

## Explainer

From your introduction to phylogenetics, you understand that evolutionary relationships can be represented as branching trees and that shared derived characters (synapomorphies) provide evidence for grouping organisms. Phylogenetic inference is the set of methods that takes raw data — typically aligned DNA or protein sequences — and determines which tree best explains the observed patterns of similarity and difference. The challenge is that for even modest numbers of species, the number of possible tree topologies is astronomically large (15 possible unrooted trees for 5 taxa, over 34 million for 10), so methods must be both principled and computationally efficient.

**Parsimony** is the most intuitive approach: it prefers the tree that requires the fewest evolutionary changes (substitutions, insertions, deletions) to explain the data. For each candidate tree, you count the minimum number of mutations needed at each site, sum across all sites, and choose the tree with the lowest total. Parsimony is fast and assumption-light, but it has a well-known weakness: when evolution is rapid or uneven across lineages, the method can be misled by **long-branch attraction**, where distantly related but fast-evolving lineages are incorrectly grouped together because they have independently accumulated the same mutations by chance.

**Maximum likelihood** addresses this by incorporating an explicit model of sequence evolution — for example, a model that specifies different rates for transitions versus transversions, or that allows rate variation among sites. For each candidate tree and set of branch lengths, the method calculates the probability of observing the actual sequence data given the model, then searches for the tree and parameters that maximize this probability. Likelihood methods are statistically rigorous and less susceptible to long-branch attraction because the model accounts for the possibility of multiple substitutions at the same site (a phenomenon parsimony ignores). The cost is computational intensity: evaluating the likelihood for each tree requires summing over all possible ancestral states at every internal node.

**Bayesian inference** uses the same likelihood models but adds prior probability distributions on tree topologies, branch lengths, and model parameters. It then applies Bayes' theorem to compute the **posterior probability** of each tree given the data — essentially asking "given what we observed, how probable is this tree?" Bayesian methods use Markov chain Monte Carlo (MCMC) sampling to explore the vast space of possible trees, and the output is not a single best tree but a distribution of trees with associated posterior probabilities. This naturally provides a measure of confidence: if 95% of sampled trees group taxa A and B together, you have strong support for that relationship. Bayesian methods are powerful but require careful assessment of convergence — you must verify that the MCMC chain has run long enough to adequately sample tree space.

In practice, all three methods often agree on well-supported relationships, and disagreements highlight regions of the tree where the data are ambiguous or where model assumptions matter. Modern phylogenetics increasingly combines these methods with techniques like **bootstrapping** (resampling the data to assess support for parsimony or likelihood trees) and model selection criteria to choose the best-fitting evolutionary model. The choice of method depends on the question, the dataset size, and the computational resources available — but understanding the logic of each approach is essential for critically evaluating any published phylogeny.
