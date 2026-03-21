---
id: dna-sequence-divergence
title: DNA Sequence Divergence and Phylogenetic Distance
domain: biology
course: evolutionary-biology
prerequisites:
- id: molecular-clock
  type: hard
tags:
- molecular-evolution
- sequence-comparison
- evolutionary-distance
stage: advanced
status: draft
---

# DNA Sequence Divergence and Phylogenetic Distance

## Core Idea
DNA sequences diverge as substitutions accumulate; the number of differences between sequences increases approximately linearly with time under neutral evolution. However, multiple substitutions at the same site and unequal substitution rates among sites require statistical corrections (like Kimura's distance) to accurately estimate evolutionary time. Sequence divergence is the foundation for molecular phylogenetics and dating.

## Questions

```yaml
- question: "Two distantly related species have a p-distance (raw proportion of different sites) of 0.45 at a given gene locus. A researcher concludes that approximately 45% of sites have undergone substitution since their common ancestor. What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "Nothing — the p-distance directly measures the true number of substitutions"
    - "The p-distance overestimates true divergence because sequencing errors inflate the count"
    - "The p-distance underestimates true divergence because multiple hits and back mutations cause some substitutions to go undetected"
    - "The p-distance is only meaningful for protein sequences, not DNA sequences"
  answer: 2
  explanation: "At high divergence levels, many sites will have experienced multiple substitutions (multiple hits) or substituted and then returned to the original base (back mutations). Both events make sites appear unchanged or falsely identical, so the raw count of differences underestimates the true number of substitutions. The p-distance also saturates — as sequences diverge further, it approaches a ceiling (~0.75 for equal-rate models) even as true substitutions continue to accumulate. Statistical corrections like Jukes-Cantor or Kimura's two-parameter model are required to estimate the true evolutionary distance."

- question: "Why does Kimura's two-parameter model generally give more accurate evolutionary distance estimates than the simpler Jukes-Cantor model?"
  type: multiple-choice
  options:
    - "Kimura's model accounts for the fact that transitions (purine-to-purine or pyrimidine-to-pyrimidine changes) occur more frequently than transversions"
    - "Kimura's model uses amino acid sequences rather than nucleotide sequences"
    - "Kimura's model corrects for gene duplication events that inflate apparent sequence differences"
    - "Kimura's model only applies to non-coding regions where mutation rates are higher"
  answer: 0
  explanation: "The Jukes-Cantor model assumes all substitution types (A↔G, A↔C, A↔T, etc.) occur at equal rates. But empirically, transitions (A↔G, purine-to-purine; C↔T, pyrimidine-to-pyrimidine) occur more frequently than transversions (A↔C, A↔T, G↔C, G↔T) — often by a ratio of 2:1 or higher. If you ignore this asymmetry, you incorrectly weight different types of differences, leading to biased distance estimates. Kimura's two-parameter model estimates separate rates for transitions (κ) and transversions, producing better-calibrated distances for most real datasets."

- question: "As two DNA sequences diverge over longer and longer evolutionary time, the observed p-distance continues to increase proportionally with time and never plateaus."
  type: true-false
  answer: false
  explanation: "The p-distance saturates. Because there are only four nucleotide states, sites that have already changed can change again (multiple hits) or revert (back mutations). As divergence increases, an ever-larger fraction of observed differences are erased by subsequent substitutions, while an ever-larger fraction of identical-looking sites are actually sites that changed multiple times and returned to their original state. The p-distance approaches a theoretical maximum near 0.75 (for equal base frequencies and equal rates), after which additional true substitutions produce no increase in observed differences. This is why corrections are necessary for ancient divergences."

- question: "Applying the Jukes-Cantor correction to a p-distance always gives an estimated true distance larger than the raw p-distance value."
  type: true-false
  answer: true
  explanation: "The Jukes-Cantor correction formula d = −(3/4)ln(1 − 4p/3) always produces d ≥ p for valid values of p (0 ≤ p < 0.75). This makes biological sense: the correction inflates the estimate to account for the multiple hits and back mutations that the raw p-distance cannot see. The larger the p-distance, the more the correction diverges from the raw value, because at high divergence levels the probability of undetected multiple hits grows. The correction approaches infinity as p → 0.75, reflecting the complete loss of phylogenetic signal at saturation."

- question: "Explain why the same nucleotide position can appear identical in two distantly related species even though two substitutions have occurred at that site since their common ancestor."
  type: short-answer
  answer: "If the ancestral state at a site is A, and one lineage substitutes A→G independently in both lineages, both modern sequences show G at that site — they look identical, but two substitutions have occurred (one in each lineage). Alternatively, in one lineage a site might change A→G and then later G→A (a back mutation), again appearing identical to the unchanged other lineage despite two events. In both cases, the site contributes zero to the p-distance count, even though it accumulated two substitutions. This is the 'multiple hits' problem, and it causes p-distance to systematically underestimate the true number of substitutions."
  explanation: "The problem worsens with evolutionary distance because the probability of multiple events at the same site increases with time. For closely related sequences it is negligible, but for ancient divergences it can be severe, which is why increasingly complex substitution models — Jukes-Cantor, Kimura, GTR — are necessary for accurate evolutionary inference across deep time."
```

## Explainer

From your study of the molecular clock, you know that neutral mutations accumulate at a roughly constant rate over time, providing a basis for estimating when two lineages diverged. **DNA sequence divergence** is the practical measurement that makes the molecular clock usable: you align homologous sequences from two species, count the differences, and use that count as a proxy for evolutionary time. The concept seems straightforward — more differences mean more time since divergence — but the raw count of observed differences systematically underestimates the true number of substitutions that have occurred, and understanding why is essential to using sequence divergence correctly.

The core problem is **multiple hits**: the same nucleotide position can mutate more than once. Imagine a site that was originally adenine (A) in the common ancestor. In one lineage it mutated to guanine (G), and in the other lineage it also mutated to G independently. When you compare the two modern sequences, that site looks identical — you see G in both — even though two substitutions occurred. Worse, a site might change from A to G and then back to A (**back mutation**), erasing all evidence of change. As sequences diverge further, the probability of multiple hits at the same site increases, which means the observed proportion of different sites (*p-distance*) increasingly underestimates the true evolutionary distance. For closely related sequences this bias is small, but for distant comparisons it can be severe — the observed divergence plateaus and eventually saturates, even as true substitutions continue to accumulate.

To correct for multiple hits, evolutionary biologists use **substitution models** that estimate the true number of substitutions per site from the observed differences. The simplest is the **Jukes-Cantor model**, which assumes all nucleotide substitutions occur at equal rates. It provides a mathematical correction: d = -(3/4) ln(1 - 4p/3), where p is the observed proportion of different sites and d is the estimated true distance. **Kimura's two-parameter model** improves on this by recognizing that transitions (purine-to-purine or pyrimidine-to-pyrimidine changes) occur more frequently than transversions (purine-to-pyrimidine or vice versa), and estimates separate rates for each. More complex models account for unequal base frequencies, rate variation among sites, and other biological realities. Each model makes different assumptions, and choosing an appropriate model for your data is a critical step in any molecular evolutionary analysis.

The practical importance of sequence divergence extends far beyond simply dating splits between species. It is the foundation of **molecular phylogenetics** — distance-based tree-building methods work directly from matrices of pairwise divergence values, and even likelihood-based methods depend on accurate models of sequence change. Divergence values also reveal which parts of the genome evolve fastest and slowest: coding regions accumulate substitutions more slowly than non-coding regions (because many coding changes are deleterious and removed by selection), and synonymous sites (where a nucleotide change does not alter the amino acid) diverge faster than nonsynonymous sites. Comparing these rates is itself a powerful tool for detecting natural selection — a theme you will encounter as you move deeper into molecular evolution.
