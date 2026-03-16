---
id: parsimony-phylogenetics
title: Parsimony in Phylogenetic Reconstruction
domain: biology
course: evolutionary-biology
prerequisites:
- id: phylogenetic-inference
  type: hard
tags:
- phylogenetics
- methods
- evolution
stage: advanced
status: draft
---

# Parsimony in Phylogenetic Reconstruction

## Core Idea
Parsimony phylogenetics selects the tree requiring the fewest evolutionary steps (mutations) to explain sequence differences. While simple and computationally fast, parsimony can be misled by homoplasy and unequal substitution rates. It remains useful for morphological data and as a null hypothesis for phylogenetic inference.

## Explainer

From phylogenetic inference, you already know that the goal is to reconstruct the branching pattern of evolutionary relationships from observed data — typically DNA sequences or morphological characters. **Maximum parsimony** offers the simplest criterion for choosing among possible trees: pick the tree that requires the fewest total evolutionary changes. The logic follows Occam's razor — all else being equal, the simplest explanation is preferred. If tree A requires 47 mutations to explain the observed sequences and tree B requires 52, parsimony selects tree A.

Here is how it works in practice. Suppose you have four species and have aligned a stretch of their DNA. At each position in the alignment, you ask: which nucleotide changes are required on each candidate tree to produce the observed pattern? A site where species A and B share a "G" while C and D share a "T" is **informative** — it favors the tree grouping A with B over alternatives. Sites where all species share the same nucleotide, or where only one species differs, do not distinguish between trees and are called uninformative under parsimony. You tally the minimum number of changes required at every informative site across all candidate trees, and the tree with the lowest total score wins.

The appeal of parsimony is its transparency and computational speed. You do not need to specify a model of sequence evolution — no assumptions about substitution rates, transition/transversion ratios, or base frequencies. This makes it particularly well-suited for **morphological data**, where realistic evolutionary models are hard to define. How do you model the rate at which a fin becomes a limb? Parsimony sidesteps the question and simply counts changes.

However, parsimony has a well-known weakness called **long branch attraction**. When two lineages evolve rapidly (accumulating many changes along long branches), chance alone will produce some identical mutations in both lineages — a phenomenon called **homoplasy**. Parsimony interprets these convergent changes as evidence of shared ancestry, incorrectly grouping the two fast-evolving lineages together. This problem is especially severe when substitution rates are unequal across the tree. Model-based methods like maximum likelihood and Bayesian inference account for the probability of multiple substitutions at the same site and are more robust to this artifact. For this reason, parsimony is often used today as a starting point or sanity check rather than as the final word in phylogenetic analysis — a baseline that more sophisticated methods can be compared against.
