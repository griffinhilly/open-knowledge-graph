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
stage: formal-systems
status: validated
---

# Phylogenetic Inference Fundamentals

## Core Idea
Phylogenetic inference reconstructs evolutionary relationships among organisms using genetic or morphological data. Core approaches (parsimony, likelihood, Bayesian) differ in assumptions and computational costs but share the goal of finding the tree topology and branch lengths best supported by data.

## Questions

```yaml
- question: "A parsimony analysis groups two distantly related lineages together, but molecular clock data suggests they diverged very early and evolved rapidly. What artifact likely caused this error?"
  type: multiple-choice
  options:
    - "The parsimony tree was rooted incorrectly, reversing the direction of evolution"
    - "Long-branch attraction: the two lineages independently accumulated the same mutations by chance, making them resemble each other"
    - "Insufficient taxon sampling caused the algorithm to undercount substitutions in both lineages"
    - "The parsimony model assigned too high a cost to transversions relative to transitions"
  answer: 1
  explanation: "Long-branch attraction is the characteristic failure mode of parsimony when lineages evolve rapidly. On a long branch, multiple substitutions can occur at the same site — including reversals and parallel changes. Two fast-evolving lineages can independently converge on the same nucleotide at many positions, making parsimony group them together as apparent 'relatives' even if they are not. Parsimony cannot account for this because it counts the minimum number of changes, ignoring the possibility of multiple hits at the same site."

- question: "Why is maximum likelihood less susceptible to long-branch attraction than parsimony?"
  type: multiple-choice
  options:
    - "Maximum likelihood searches a larger number of tree topologies and therefore finds the globally optimal solution"
    - "The evolutionary model explicitly accounts for the probability of multiple substitutions occurring at the same site"
    - "Maximum likelihood assigns lower weight to fast-evolving lineages, reducing their influence on tree topology"
    - "It uses bootstrapping to filter out long-branch taxa before constructing the tree"
  answer: 1
  explanation: "Maximum likelihood calculates the probability of the observed data given each tree and a substitution model. Models like GTR+Γ explicitly allow for the possibility that multiple substitutions have occurred at a single site (including reversals and parallel changes) — a phenomenon parsimony simply ignores by counting only the minimum changes. By modeling the full stochastic process, ML can recognize that two long-branch taxa sharing a character state are more likely doing so by convergence than by shared ancestry."

- question: "Bayesian phylogenetic inference produces a single best tree, just like maximum likelihood, but uses prior probability distributions over model parameters."
  type: true-false
  answer: false
  explanation: "Bayesian inference produces a distribution over trees, not a single tree. MCMC sampling explores tree space and the output is a posterior probability distribution across many possible topologies. The proportion of sampled trees supporting a given grouping (clade) is its posterior probability — a natural measure of confidence. This is fundamentally different from maximum likelihood, which returns the single tree that maximizes the probability of the observed data."

- question: "The parsimony criterion for tree selection makes no assumptions about the underlying model of sequence evolution."
  type: true-false
  answer: true
  explanation: "Parsimony is model-free in the sense that it does not specify substitution rates, transition/transversion biases, or rate variation among sites — it simply counts the minimum number of mutations required. This is both a strength (no incorrect model assumptions) and a weakness (it implicitly assumes that all changes are equally likely and that multiple substitutions at the same site are negligible — an assumption violated when evolution is rapid). Being assumption-light is not the same as being assumption-free."

- question: "Why is the sheer number of possible tree topologies a fundamental challenge for phylogenetic inference, and how do computational methods address it?"
  type: short-answer
  answer: "The number of possible unrooted tree topologies grows super-exponentially with the number of taxa: 3 trees for 4 taxa, 15 for 5, over 34 million for 10, and astronomically more for hundreds of taxa. Exhaustive evaluation of every topology is computationally impossible beyond a handful of taxa. Methods address this by using heuristic search algorithms (hill-climbing, branch swapping, simulated annealing) that explore promising regions of tree space without evaluating all possibilities, and Bayesian methods use MCMC to sample proportionally from the posterior distribution of trees."
  explanation: "The combinatorial explosion of tree space is why phylogenetics is computationally expensive and why exact algorithms are limited to small datasets. Practically, this means that for large datasets, methods are not guaranteed to find the globally optimal tree — they find the best tree among those explored. This is why multiple search strategies, adequate MCMC run lengths, and convergence diagnostics are important in practice."
```

## Explainer

From your introduction to phylogenetics, you understand that evolutionary relationships can be represented as branching trees and that shared derived characters (synapomorphies) provide evidence for grouping organisms. Phylogenetic inference is the set of methods that takes raw data — typically aligned DNA or protein sequences — and determines which tree best explains the observed patterns of similarity and difference. The challenge is that for even modest numbers of species, the number of possible tree topologies is astronomically large (15 possible unrooted trees for 5 taxa, over 34 million for 10), so methods must be both principled and computationally efficient.

**Parsimony** is the most intuitive approach: it prefers the tree that requires the fewest evolutionary changes (substitutions, insertions, deletions) to explain the data. For each candidate tree, you count the minimum number of mutations needed at each site, sum across all sites, and choose the tree with the lowest total. Parsimony is fast and assumption-light, but it has a well-known weakness: when evolution is rapid or uneven across lineages, the method can be misled by **long-branch attraction**, where distantly related but fast-evolving lineages are incorrectly grouped together because they have independently accumulated the same mutations by chance.

**Maximum likelihood** addresses this by incorporating an explicit model of sequence evolution — for example, a model that specifies different rates for transitions versus transversions, or that allows rate variation among sites. For each candidate tree and set of branch lengths, the method calculates the probability of observing the actual sequence data given the model, then searches for the tree and parameters that maximize this probability. Likelihood methods are statistically rigorous and less susceptible to long-branch attraction because the model accounts for the possibility of multiple substitutions at the same site (a phenomenon parsimony ignores). The cost is computational intensity: evaluating the likelihood for each tree requires summing over all possible ancestral states at every internal node.

**Bayesian inference** uses the same likelihood models but adds prior probability distributions on tree topologies, branch lengths, and model parameters. It then applies Bayes' theorem to compute the **posterior probability** of each tree given the data — essentially asking "given what we observed, how probable is this tree?" Bayesian methods use Markov chain Monte Carlo (MCMC) sampling to explore the vast space of possible trees, and the output is not a single best tree but a distribution of trees with associated posterior probabilities. This naturally provides a measure of confidence: if 95% of sampled trees group taxa A and B together, you have strong support for that relationship. Bayesian methods are powerful but require careful assessment of convergence — you must verify that the MCMC chain has run long enough to adequately sample tree space.

In practice, all three methods often agree on well-supported relationships, and disagreements highlight regions of the tree where the data are ambiguous or where model assumptions matter. Modern phylogenetics increasingly combines these methods with techniques like **bootstrapping** (resampling the data to assess support for parsimony or likelihood trees) and model selection criteria to choose the best-fitting evolutionary model. The choice of method depends on the question, the dataset size, and the computational resources available — but understanding the logic of each approach is essential for critically evaluating any published phylogeny.
