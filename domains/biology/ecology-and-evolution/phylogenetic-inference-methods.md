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
stage: formal-systems
status: validated
---

# Phylogenetic Inference: Parsimony, Distance, and Maximum Likelihood

## Core Idea
Phylogenetic trees are reconstructed using methods that make different assumptions: maximum parsimony finds trees requiring fewest changes; distance methods cluster species by overall similarity; maximum likelihood finds the tree most probable under a specified evolutionary model. Each method has strengths and limitations, and disagreement between methods can highlight data limitations. Modern phylogenetics integrates multiple methods and data types for robust inference.

## Questions

```yaml
- question: "Two rapidly evolving lineages — one from birds, one from lizards — have independently accumulated many convergent mutations in a gene. A maximum parsimony analysis groups them as sister taxa. Why is this result likely an artifact?"
  type: multiple-choice
  options:
    - "Parsimony never makes errors with molecular data — only morphological data misleads it"
    - "Long-branch attraction: parsimony interprets convergently accumulated similarity as shared common ancestry, incorrectly grouping fast-evolving lineages together"
    - "Parsimony correctly identifies them as closely related, because similarity always reflects shared ancestry"
    - "Distance methods would make the same error, confirming the grouping is likely correct"
  answer: 1
  explanation: "Long-branch attraction is a systematic failure mode of maximum parsimony when lineages evolve at very different rates. Rapidly evolving lineages independently accumulate many convergent mutations (homoplasy). Parsimony, which minimizes total changes, interprets shared similarity as evidence of common ancestry — but this similarity is convergent, not inherited from a recent common ancestor. Maximum likelihood methods can correct for this by explicitly modeling substitution probabilities at different rates, detecting that the apparent synapomorphy is more likely due to convergence than to shared ancestry."

- question: "A researcher runs parsimony, neighbor-joining, and maximum likelihood on the same dataset. Parsimony and neighbor-joining agree, but maximum likelihood gives a different tree. What should the researcher conclude?"
  type: multiple-choice
  options:
    - "The maximum likelihood tree is wrong because two independent methods agree against it"
    - "The maximum likelihood tree is certainly correct because it uses the most rigorous statistical model"
    - "The conflict should trigger further investigation — testing model fit, checking for rate variation, or gathering more data — rather than automatically accepting the majority result"
    - "The three trees should be averaged to produce the best consensus estimate"
  answer: 2
  explanation: "Method agreement indicates robustness, but method conflict does not resolve which is correct by counting votes. Parsimony and neighbor-joining can share failure modes — both can be sensitive to rate variation and long-branch attraction — and may go wrong together under conditions that favor those biases. Maximum likelihood under an appropriate model generally outperforms both, but model misspecification can bias it. The correct response to disagreement is investigation: model selection testing, simulation, or gathering more characters. Phylogenetic practice treats method conflict as a signal that the data have limitations requiring further study."

- question: "Distance-based phylogenetic methods cluster species by pairwise evolutionary distances computed from character data, discarding information about which specific character changes occurred."
  type: true-false
  answer: true
  explanation: "This accurately describes both the strength and limitation of distance methods. They collapse the full character matrix into a single pairwise distance for each species pair (typically the fraction of differing sites, corrected for multiple substitutions), then apply clustering algorithms like neighbor-joining. Advantages include computational speed for large datasets. The limitation is information loss: two very different patterns of change can produce identical distances, discarding phylogenetic signal that parsimony and likelihood methods retain by examining individual characters."

- question: "Bayesian phylogenetics produces a single best-supported tree, just like maximum likelihood, and is distinguished primarily by being computationally more efficient."
  type: true-false
  answer: false
  explanation: "Bayesian phylogenetics differs fundamentally from maximum likelihood in both output and computation. Rather than returning a single tree that maximizes the likelihood, Bayesian inference samples from the posterior distribution of trees using MCMC — producing a set of sampled trees summarized as a consensus with posterior probability support values at each node, directly quantifying uncertainty. Maximum likelihood reports bootstrap support, a resampling measure, not a true probability. Computationally, Bayesian methods are typically more demanding than ML, not more efficient."

- question: "Why do modern phylogenetic studies typically run multiple inference methods rather than selecting the 'best' one, and what do they look for in the results?"
  type: short-answer
  answer: "Each method makes different assumptions and has characteristic failure modes: parsimony fails under long-branch attraction and rate variation; distance methods lose information by collapsing characters to pairwise numbers; ML and Bayesian methods can be misled by incorrect substitution models. No single method is universally optimal. By running multiple methods, researchers use convergence as a confidence signal: a node supported by parsimony, distance, and ML/Bayesian methods is considered robustly inferred, because independent approaches with different assumptions reach the same conclusion. Disagreements flag nodes where data are insufficient, rates are heterogeneous, or model assumptions may be violated — guiding decisions about whether to gather more data or refine the analysis."
  explanation: "The multi-method approach applies triangulation: convergence of independent evidence justifies confidence; divergence signals where inference is fragile and further investigation is needed."
```

## Explainer

From cladistics and systematics, you know that phylogenetic trees represent hypotheses about evolutionary relationships — branching diagrams showing which species share more recent common ancestors. The challenge is that we cannot directly observe the past: we must *infer* the tree from data available today, whether morphological characters or DNA sequences. Phylogenetic inference methods are the statistical and algorithmic tools that take a matrix of character data and produce the best-supported tree. The three major approaches — parsimony, distance, and likelihood — differ fundamentally in how they define "best."

**Maximum parsimony** operates on a simple principle borrowed from Occam's razor: the best tree is the one requiring the fewest evolutionary changes to explain the observed data. For each possible tree topology, you count how many character-state changes (mutations, morphological transitions) are needed to map the data onto that tree, and you select the tree with the smallest total. Parsimony is intuitive and makes minimal assumptions about the evolutionary process. However, it can be misled when evolution is fast or uneven — a problem called **long-branch attraction**, where distantly related lineages that have evolved rapidly accumulate convergent similarities and get grouped together incorrectly. If you have studied hypothesis testing, you can think of parsimony as choosing the simplest explanation, but simplicity is not always accuracy when the underlying process is complex.

**Distance methods** take a different approach entirely. Instead of examining individual characters, they first collapse the data into a single number for each pair of species: the **evolutionary distance**, typically the fraction of sites that differ between two sequences (corrected for multiple substitutions at the same site). Then they use clustering algorithms — most commonly **neighbor-joining** — to build a tree by progressively grouping the most similar pairs. Distance methods are computationally fast, which matters when you have hundreds or thousands of species, but they discard information by reducing the full character matrix to pairwise distances. Two very different patterns of change can produce the same distance, so some phylogenetic signal is inevitably lost.

**Maximum likelihood** is the most statistically rigorous approach. It requires an explicit model of evolution — for DNA data, this specifies the rates at which each nucleotide substitutes for every other. Given a proposed tree and a model, you calculate the probability that the model would produce the observed data on that tree. The tree with the highest probability (likelihood) is the maximum likelihood estimate. This approach can account for unequal rates across sites, different substitution rates between nucleotide pairs, and variation in evolutionary rate across lineages. If you have encountered Bayesian inference, you will recognize that the Bayesian extension of phylogenetics goes one step further: it combines the likelihood with prior probabilities on tree topologies and model parameters to produce a posterior distribution of trees, often summarized as a consensus tree with support values at each node. Maximum likelihood and Bayesian methods are computationally demanding but generally outperform parsimony and distance methods when the data are complex or the evolutionary signal is weak. In practice, modern phylogenetic studies run multiple methods and look for agreement — nodes supported by all approaches are considered robust, while conflicts flag areas where more data or better models are needed.
