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

## Questions

```yaml
- question: "Researcher A builds an ML tree using Jukes-Cantor (log-likelihood = −10,500). Researcher B uses GTR+Γ on the same alignment (log-likelihood = −9,800). What is the most appropriate interpretation?"
  type: multiple-choice
  options:
    - "Researcher A's tree is more reliable because Jukes-Cantor is more conservative and avoids overfitting"
    - "The two likelihoods cannot be meaningfully compared because different substitution models were used"
    - "GTR+Γ fits the data better; a likelihood ratio test or information criterion can assess whether the improvement justifies the additional parameters"
    - "Researcher B's tree is always preferable because more parameters always improve likelihood"
  answer: 2
  explanation: "Higher log-likelihood means the model assigns greater probability to the observed data, which is evidence of better fit. GTR+Γ allows different substitution rates and rate variation across sites — capturing real features of molecular evolution that Jukes-Cantor ignores. Model comparison tests (likelihood ratio test for nested models, AIC/BIC for non-nested) formalize whether the improvement is statistically justified. The correct approach is model selection, not blanket preference for simpler or more complex models."

- question: "Why do ML phylogenetic programs like RAxML use heuristic search strategies rather than evaluating every possible tree topology?"
  type: multiple-choice
  options:
    - "Heuristic methods are provably more accurate than exhaustive search for biological data"
    - "The number of possible unrooted tree topologies grows super-exponentially with the number of taxa, making exhaustive search computationally infeasible even for modest datasets"
    - "ML likelihood calculations can only be performed for trees with branch lengths below a certain threshold"
    - "Exhaustive search does not allow simultaneous optimization of branch lengths"
  answer: 1
  explanation: "For N taxa, the number of distinct unrooted tree topologies is (2N−5)!! — a super-exponential function. For 20 sequences, this exceeds 10²⁰ trees; for 50 sequences, the number is astronomically larger. Evaluating every tree is impossible. Heuristics like nearest-neighbor interchange (NNI) and subtree pruning-regrafting (SPR) start from an initial tree and improve it incrementally, but they cannot guarantee finding the global ML optimum."

- question: "In ML phylogenetics, the likelihood of a tree at a single alignment site is calculated by summing over all possible ancestral nucleotide states at internal nodes, weighted by the substitution probabilities defined by the evolutionary model."
  type: true-false
  answer: true
  explanation: "This is the Felsenstein pruning algorithm. At each internal node, you cannot observe the ancestral sequence directly, so you must average over all possible ancestral states. Each path through the tree — assigning specific nucleotides to all internal nodes — has a probability determined by the substitution model's rate matrix and the branch lengths. Summing these probabilities over all possible ancestral assignments gives the marginal likelihood of observing the tip nucleotides at that site, given the tree and model."

- question: "The ML tree returned by phylogenetic software is guaranteed to be the tree with the highest possible likelihood across all possible topologies for the given alignment."
  type: true-false
  answer: false
  explanation: "There is no guarantee. Heuristic search explores only a fraction of tree space, moving from tree to tree by local rearrangements. It can get trapped in local optima — regions where no simple branch swap improves the likelihood, even though a better tree exists elsewhere in tree space. The returned tree has the highest likelihood found during the search, not the highest possible. This is why researchers often run multiple searches from different starting trees."

- question: "What role does the substitution model play in ML phylogenetics, and why does using a more realistic model typically produce a higher likelihood even without changing the tree topology?"
  type: short-answer
  answer: "The substitution model defines a matrix of probabilities for each nucleotide changing into another over a given branch length. It is used to calculate the probability of observing the actual sequence data at the tips, given the tree and branch lengths. A more realistic model (e.g., GTR allows unequal rates for all six substitution types; Γ allows rate variation across sites) better matches the true patterns of molecular evolution. Because the model more accurately predicts the data-generating process, it assigns higher probability to the observed alignment — producing a higher likelihood — even with the same tree topology. The improvement comes from a better statistical description of how sequences evolve, not from a different evolutionary history."
  explanation: "This is why model selection is a critical step in ML phylogenetics. An underfitting model (e.g., treating all substitutions as equally likely when they are not) systematically mispredicts data patterns, reducing the likelihood. Choosing a well-fitting model improves both the likelihood and the accuracy of the inferred tree."
```

## Explainer

From your work on phylogenetic inference, you know that the goal is to reconstruct the branching history of species or sequences from observed data — typically aligned DNA or protein sequences. The challenge is that many different trees could explain the same data. **Maximum likelihood (ML) phylogenetics** provides a principled statistical framework for choosing among them: it selects the tree that makes the observed sequence alignment most probable under a given model of evolution.

The core logic draws directly on probability theory. For any candidate tree topology with specific branch lengths, you can calculate the probability of observing each column in a sequence alignment. At a single site, this means summing over all possible ancestral states at every internal node, weighted by the substitution probabilities along each branch. Those substitution probabilities come from the **evolutionary model** — a matrix describing how likely each nucleotide is to change into another over a given amount of evolutionary time. Simple models like Jukes-Cantor assume all substitutions are equally likely; more complex models like GTR (General Time Reversible) allow different rates for each type of change and unequal base frequencies. The total likelihood of the tree is the product of these per-site probabilities across all columns in the alignment.

Finding the ML tree is computationally demanding because the number of possible tree topologies grows super-exponentially with the number of taxa. For even 20 sequences, exhaustive search is impossible. In practice, ML programs like RAxML and IQ-TREE use **heuristic search strategies** — starting from a reasonable initial tree and then rearranging branches (using operations like nearest-neighbor interchange or subtree pruning and regrafting) to find trees with higher likelihood. Branch lengths and model parameters are optimized numerically at each step. The result is the tree and parameter combination that achieves the highest likelihood found during the search, though there is no guarantee it is the global optimum.

One of the great strengths of the likelihood framework is that it naturally supports **statistical assessment**. Bootstrap support values, obtained by resampling alignment columns and re-estimating trees, measure how consistently a particular branching pattern appears. Likelihood ratio tests allow formal comparison of nested evolutionary models — for example, testing whether allowing rate variation among sites significantly improves the fit. This capacity for model selection and hypothesis testing is what distinguishes ML from simpler methods like parsimony, and it sets the stage for Bayesian phylogenetics, which extends the likelihood framework by incorporating prior distributions over trees and parameters.
