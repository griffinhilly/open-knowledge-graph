---
id: phylogenetic-tree-construction
title: Phylogenetic Tree Construction
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: multiple-sequence-alignment
  type: hard
- id: molecular-evolution
  type: hard
- id: pairwise-sequence-alignment
  type: soft
- id: probability-density-functions
  type: soft
builds-toward:
- comparative-genomics
- population-genomics
tags:
- phylogenetics
- neighbor-joining
- maximum-likelihood
- Bayesian
- bootstrap
- tree-topology
stage: advanced
status: validated
---
# Phylogenetic Tree Construction

## Core Idea
Phylogenetic trees depict evolutionary relationships among sequences or species, inferred from aligned molecular data. Distance-based methods (neighbor-joining) cluster sequences by pairwise distances. Character-based methods (maximum parsimony, maximum likelihood, Bayesian inference) evaluate alternative tree topologies against the alignment data. Maximum likelihood finds the tree that makes the observed data most probable given a model of sequence evolution. Bootstrap values and Bayesian posterior probabilities assess statistical support for each branch. Tree construction requires choosing an appropriate substitution model and rooting strategy.

## How It's Best Learned
Build a neighbor-joining tree and a maximum likelihood tree from the same MSA of 10-15 orthologous sequences. Compare the topologies and bootstrap support values. Experiment with different substitution models (JC69 vs. GTR) and observe how model choice affects branch lengths and topology.

## Common Misconceptions
- A phylogenetic tree does not show which species evolved from which — it shows patterns of shared ancestry and relative divergence.
- High bootstrap support (e.g., 95%) does not mean the branch is certainly correct; it means the data consistently support that grouping when resampled.

## Questions

```yaml
- question: "What does a bootstrap value of 85 on an internal branch of a phylogenetic tree indicate?"
  type: multiple-choice
  options: ["85% of the sequences support that branch", "In 85% of bootstrap replicates (resampled alignment columns), that branch was recovered", "The branch has an 85% probability of being correct", "85% of the nucleotide sites are informative for that branch"]
  answer: 1
  explanation: "Bootstrapping resamples columns of the multiple sequence alignment with replacement to create many pseudo-replicate datasets (typically 100-1,000). A tree is built from each replicate, and the bootstrap value reports the percentage of replicates in which a given branch appeared. A value of 85 means 85% of resampled datasets recovered that grouping. It measures the sensitivity of the grouping to data perturbation, not the probability of correctness in an absolute sense."

- question: "Neighbor-joining and maximum likelihood always produce identical tree topologies for the same dataset."
  type: true-false
  answer: false
  explanation: "Neighbor-joining is a fast distance-based method that uses a greedy algorithm to build a single tree from pairwise distances. Maximum likelihood evaluates many possible topologies and selects the one with the highest probability of producing the observed data under a specified substitution model. They can produce different topologies because NJ reduces the data to pairwise distances (losing information), uses a greedy strategy (which may not find the global optimum), and does not explicitly model the substitution process. ML is generally considered more accurate but is much more computationally expensive."

- question: "Why is the choice of substitution model important when constructing a maximum likelihood phylogenetic tree?"
  type: short-answer
  answer: "The substitution model specifies the rates and probabilities of different nucleotide or amino acid changes. A model that is too simple (like JC69, which assumes all substitutions are equally likely) will underestimate the true amount of sequence divergence, especially between distantly related sequences, because it fails to account for multiple substitutions at the same site. A more parameter-rich model (like GTR, which allows different rates for each substitution type and unequal base frequencies) better captures real evolutionary dynamics but requires more data to estimate its parameters reliably. The wrong model can systematically distort branch lengths and even change the tree topology."
  explanation: "Model selection is typically done using information criteria (AIC, BIC) or likelihood ratio tests. Tools like ModelTest-NG and jModelTest automate this by fitting many models to the data and selecting the best-fitting one. The selected model is then used for the full ML tree search."
```

## Explainer

Phylogenetic trees are the primary tool for representing evolutionary relationships, and molecular sequence data has become the dominant source of information for building them. Given a multiple sequence alignment, the question is: what tree topology (branching pattern) and branch lengths best explain the observed pattern of similarities and differences? Different methods answer this question in fundamentally different ways.

**Distance-based methods** convert the MSA into a matrix of pairwise evolutionary distances (corrected for multiple substitutions at the same site), then build a tree that approximates those distances. Neighbor-joining (NJ) is the most widely used distance method: it iteratively joins the pair of sequences that minimizes the total branch length of the tree, adjusting for the average distance to all other sequences. NJ is fast (O(n^3) for n sequences) and produces reasonable trees, making it useful for quick exploratory analyses and very large datasets. But it reduces the full alignment to pairwise distances, losing information about which specific sites support which groupings.

**Maximum likelihood (ML)** takes a fundamentally different approach. It considers the alignment column by column, calculates the probability of each observed column pattern for every possible tree topology under a specified model of sequence evolution, and multiplies these probabilities across all columns to get the likelihood of the entire dataset given each tree. The tree with the highest total likelihood is selected. This approach uses all the information in the alignment and explicitly models the evolutionary process, but it requires searching an enormous space of possible topologies (which grows super-exponentially with the number of sequences). Software like RAxML and IQ-TREE use heuristic search strategies to navigate this space efficiently.

**Bayesian inference** (implemented in MrBayes and BEAST) extends ML by incorporating prior probabilities on tree topologies, branch lengths, and model parameters, using Markov chain Monte Carlo (MCMC) sampling to explore the posterior distribution. Rather than returning a single best tree, Bayesian methods return a distribution of trees weighted by their posterior probability, naturally providing measures of uncertainty. Bayesian posterior probabilities on branches tend to be higher than bootstrap values for the same data, and interpreting them correctly requires understanding MCMC convergence diagnostics.

Regardless of method, the resulting tree must be evaluated critically. **Bootstrap analysis** for ML/NJ and **posterior probabilities** for Bayesian trees indicate how strongly the data support each branch. An unrooted tree shows relative relationships but not the direction of evolution; rooting (typically with an outgroup) is needed to infer ancestor-descendant relationships. And the tree reflects the history of the sequences analyzed, which may not match the species tree if gene duplication, horizontal transfer, or incomplete lineage sorting has occurred.
