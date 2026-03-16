---
id: maximum-likelihood-phylogenetics
title: Maximum Likelihood Phylogenetics
domain: biology
course: evolutionary-biology
prerequisites:
- id: phylogenetic-inference
  type: hard
- id: probability-axioms
  type: hard
builds-toward:
- bayesian-phylogenetics
tags:
- phylogenetics
- statistics
- methods
stage: advanced
status: draft
---

# Maximum Likelihood Phylogenetics

## Core Idea
Maximum likelihood phylogenetics finds the tree and evolutionary model that maximize the probability of observing the data. ML accounts for multiple substitutions per site and provides branch length estimates and statistical support values. Likelihood framework allows model comparison and hypothesis testing about evolutionary processes.

## Explainer

From your work on phylogenetic inference, you know that the goal is to reconstruct the branching history of species or sequences from observed data — typically aligned DNA or protein sequences. The challenge is that many different trees could explain the same data. **Maximum likelihood (ML) phylogenetics** provides a principled statistical framework for choosing among them: it selects the tree that makes the observed sequence alignment most probable under a given model of evolution.

The core logic draws directly on probability theory. For any candidate tree topology with specific branch lengths, you can calculate the probability of observing each column in a sequence alignment. At a single site, this means summing over all possible ancestral states at every internal node, weighted by the substitution probabilities along each branch. Those substitution probabilities come from the **evolutionary model** — a matrix describing how likely each nucleotide is to change into another over a given amount of evolutionary time. Simple models like Jukes-Cantor assume all substitutions are equally likely; more complex models like GTR (General Time Reversible) allow different rates for each type of change and unequal base frequencies. The total likelihood of the tree is the product of these per-site probabilities across all columns in the alignment.

Finding the ML tree is computationally demanding because the number of possible tree topologies grows super-exponentially with the number of taxa. For even 20 sequences, exhaustive search is impossible. In practice, ML programs like RAxML and IQ-TREE use **heuristic search strategies** — starting from a reasonable initial tree and then rearranging branches (using operations like nearest-neighbor interchange or subtree pruning and regrafting) to find trees with higher likelihood. Branch lengths and model parameters are optimized numerically at each step. The result is the tree and parameter combination that achieves the highest likelihood found during the search, though there is no guarantee it is the global optimum.

One of the great strengths of the likelihood framework is that it naturally supports **statistical assessment**. Bootstrap support values, obtained by resampling alignment columns and re-estimating trees, measure how consistently a particular branching pattern appears. Likelihood ratio tests allow formal comparison of nested evolutionary models — for example, testing whether allowing rate variation among sites significantly improves the fit. This capacity for model selection and hypothesis testing is what distinguishes ML from simpler methods like parsimony, and it sets the stage for Bayesian phylogenetics, which extends the likelihood framework by incorporating prior distributions over trees and parameters.
