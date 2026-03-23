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
status: validated
---

# Parsimony in Phylogenetic Reconstruction

## Core Idea
Parsimony phylogenetics selects the tree requiring the fewest evolutionary steps (mutations) to explain sequence differences. While simple and computationally fast, parsimony can be misled by homoplasy and unequal substitution rates. It remains useful for morphological data and as a null hypothesis for phylogenetic inference.

## Questions

```yaml
- question: "Two distantly related lineages have each accumulated many substitutions along long branches. By chance, 15 sites in their sequences show identical nucleotides arising from independent mutations. A parsimony analysis groups these two lineages as sisters. What problem is this, and what causes it?"
  type: multiple-choice
  options:
    - "Saturation: too many substitutions destroy phylogenetic signal, causing random groupings"
    - "Long branch attraction: parsimony misinterprets convergent homoplastic changes as evidence of shared ancestry, pulling long branches together incorrectly"
    - "Polytomy collapse: parsimony cannot resolve rapidly evolving lineages and defaults to incorrect groupings"
    - "Molecular clock violation: unequal rates cause the parsimony score to be miscalculated"
  answer: 1
  explanation: "Long branch attraction is parsimony's most important and systematic failure mode. When two lineages evolve rapidly (long branches), chance produces identical mutations in both — homoplasy. Parsimony treats these convergent similarities as evidence of shared ancestry (shared derived characters), grouping the two fast-evolving lineages together even when they are not closely related. The key word is 'systematic': this is not random noise but a biased error that parsimony can commit with high confidence, producing a confidently wrong tree. Model-based methods account for the probability of multiple hits at the same site and are more robust to this artifact."

- question: "For which type of data is maximum parsimony most defensible as a phylogenetic method, and why?"
  type: multiple-choice
  options:
    - "DNA sequences with high substitution rates, because parsimony is fastest when many characters are informative"
    - "Sequences from rapidly radiating clades, because parsimony handles polytomies better than model-based methods"
    - "Morphological characters, because defining realistic substitution models for the evolution of anatomical structures is extremely difficult"
    - "Ancient DNA, because parsimony does not assume a molecular clock and handles missing data well"
  answer: 2
  explanation: "Parsimony's biggest liability — requiring no model — is also its biggest asset for morphological data. For DNA, realistic substitution models (GTR, HKY, etc.) have been well-developed and validated; using them substantially improves inference. But how do you model the rate at which a fin becomes a limb, or the number of independent times eyes have evolved? Realistic morphological models are hard to define, and the parameter estimation involved can be unreliable. Parsimony sidesteps this by simply counting minimum changes, which is more defensible when model specification is genuinely uncertain."

- question: "Maximum parsimony can recover a confidently incorrect phylogenetic tree — not just an uncertain one — when long branches are present in the data."
  type: true-false
  answer: true
  explanation: "This is the critical point that separates long branch attraction from ordinary statistical noise. When two long branches accumulate many homoplastic changes that parsimony misinterprets as synapomorphies, the method does not produce a polytomy or low bootstrap support — it produces a strongly supported, but wrong, grouping. Bootstrap resampling the same data over and over simply confirms the same erroneous pattern. This is why long branch attraction is so dangerous: the method can be maximally confident about an incorrect topology, giving no warning signal that something is wrong."

- question: "Parsimony is the preferred method for large genomic datasets because it requires no assumptions about the evolutionary process, making it the most objective approach to phylogenetic inference."
  type: true-false
  answer: false
  explanation: "While parsimony does not require specification of a substitution model, it implicitly assumes that the most parsimonious explanation is the most likely — which is itself an assumption that breaks down when substitution rates are unequal across lineages. For large genomic datasets, model-based methods (maximum likelihood, Bayesian inference) are generally preferred because they can account for rate variation, multiple substitutions at the same site, and other biological realities that parsimony ignores. Parsimony's speed advantage has also diminished as computational resources have grown. Today it is most useful as a baseline or for morphological data."

- question: "Explain how maximum parsimony's core principle — choosing the tree requiring the fewest changes — can lead to a confidently incorrect phylogeny when lineages evolve at very different rates."
  type: short-answer
  answer: "When two lineages evolve rapidly, each accumulates many substitutions independently. At some sites, by chance, both lineages acquire the same nucleotide through convergent evolution (homoplasy). Parsimony interprets these shared but independently derived characters as evidence of common ancestry — shared derived characters (synapomorphies) — and therefore groups the two fast-evolving lineages together. Because the number of homoplastic shared characters can be large on long branches, parsimony may treat them as strong evidence for incorrect grouping. The method has no mechanism to distinguish shared ancestry from coincidental convergence when multiple substitutions occur at the same site."
  explanation: "Model-based methods solve this by using substitution models that estimate the probability of multiple hits at the same site. A position where G appears in two distantly related taxa is assigned a probability that accounts for multiple changes through the same site — recognizing that apparent similarity may reflect independent paths through the same nucleotide state. Parsimony's 'one change = one event' assumption fails whenever the same site changes more than once."
```

## Explainer

From phylogenetic inference, you already know that the goal is to reconstruct the branching pattern of evolutionary relationships from observed data — typically DNA sequences or morphological characters. **Maximum parsimony** offers the simplest criterion for choosing among possible trees: pick the tree that requires the fewest total evolutionary changes. The logic follows Occam's razor — all else being equal, the simplest explanation is preferred. If tree A requires 47 mutations to explain the observed sequences and tree B requires 52, parsimony selects tree A.

Here is how it works in practice. Suppose you have four species and have aligned a stretch of their DNA. At each position in the alignment, you ask: which nucleotide changes are required on each candidate tree to produce the observed pattern? A site where species A and B share a "G" while C and D share a "T" is **informative** — it favors the tree grouping A with B over alternatives. Sites where all species share the same nucleotide, or where only one species differs, do not distinguish between trees and are called uninformative under parsimony. You tally the minimum number of changes required at every informative site across all candidate trees, and the tree with the lowest total score wins.

The appeal of parsimony is its transparency and computational speed. You do not need to specify a model of sequence evolution — no assumptions about substitution rates, transition/transversion ratios, or base frequencies. This makes it particularly well-suited for **morphological data**, where realistic evolutionary models are hard to define. How do you model the rate at which a fin becomes a limb? Parsimony sidesteps the question and simply counts changes.

However, parsimony has a well-known weakness called **long branch attraction**. When two lineages evolve rapidly (accumulating many changes along long branches), chance alone will produce some identical mutations in both lineages — a phenomenon called **homoplasy**. Parsimony interprets these convergent changes as evidence of shared ancestry, incorrectly grouping the two fast-evolving lineages together. This problem is especially severe when substitution rates are unequal across the tree. Model-based methods like maximum likelihood and Bayesian inference account for the probability of multiple substitutions at the same site and are more robust to this artifact. For this reason, parsimony is often used today as a starting point or sanity check rather than as the final word in phylogenetic analysis — a baseline that more sophisticated methods can be compared against.
