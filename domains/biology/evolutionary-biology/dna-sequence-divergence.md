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

## Explainer

From your study of the molecular clock, you know that neutral mutations accumulate at a roughly constant rate over time, providing a basis for estimating when two lineages diverged. **DNA sequence divergence** is the practical measurement that makes the molecular clock usable: you align homologous sequences from two species, count the differences, and use that count as a proxy for evolutionary time. The concept seems straightforward — more differences mean more time since divergence — but the raw count of observed differences systematically underestimates the true number of substitutions that have occurred, and understanding why is essential to using sequence divergence correctly.

The core problem is **multiple hits**: the same nucleotide position can mutate more than once. Imagine a site that was originally adenine (A) in the common ancestor. In one lineage it mutated to guanine (G), and in the other lineage it also mutated to G independently. When you compare the two modern sequences, that site looks identical — you see G in both — even though two substitutions occurred. Worse, a site might change from A to G and then back to A (**back mutation**), erasing all evidence of change. As sequences diverge further, the probability of multiple hits at the same site increases, which means the observed proportion of different sites (*p-distance*) increasingly underestimates the true evolutionary distance. For closely related sequences this bias is small, but for distant comparisons it can be severe — the observed divergence plateaus and eventually saturates, even as true substitutions continue to accumulate.

To correct for multiple hits, evolutionary biologists use **substitution models** that estimate the true number of substitutions per site from the observed differences. The simplest is the **Jukes-Cantor model**, which assumes all nucleotide substitutions occur at equal rates. It provides a mathematical correction: d = -(3/4) ln(1 - 4p/3), where p is the observed proportion of different sites and d is the estimated true distance. **Kimura's two-parameter model** improves on this by recognizing that transitions (purine-to-purine or pyrimidine-to-pyrimidine changes) occur more frequently than transversions (purine-to-pyrimidine or vice versa), and estimates separate rates for each. More complex models account for unequal base frequencies, rate variation among sites, and other biological realities. Each model makes different assumptions, and choosing an appropriate model for your data is a critical step in any molecular evolutionary analysis.

The practical importance of sequence divergence extends far beyond simply dating splits between species. It is the foundation of **molecular phylogenetics** — distance-based tree-building methods work directly from matrices of pairwise divergence values, and even likelihood-based methods depend on accurate models of sequence change. Divergence values also reveal which parts of the genome evolve fastest and slowest: coding regions accumulate substitutions more slowly than non-coding regions (because many coding changes are deleterious and removed by selection), and synonymous sites (where a nucleotide change does not alter the amino acid) diverge faster than nonsynonymous sites. Comparing these rates is itself a powerful tool for detecting natural selection — a theme you will encounter as you move deeper into molecular evolution.
