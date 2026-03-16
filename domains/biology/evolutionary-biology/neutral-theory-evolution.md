---
id: neutral-theory-evolution
title: The Neutral Theory of Molecular Evolution
domain: biology
course: evolutionary-biology
prerequisites:
- id: molecular-evolution
  type: hard
- id: allele-frequency-change
  type: hard
builds-toward:
- molecular-clock
tags:
- neutral-theory
- molecular-evolution
- drift
- synonymous-substitutions
stage: advanced
status: draft
---

# The Neutral Theory of Molecular Evolution

## Core Idea
Kimura's neutral theory proposes that most nucleotide substitutions are random rather than selected, occurring through drift and affecting synonymous sites more than non-synonymous sites. The theory predicts that neutral substitution rates equal mutation rates and that genetic variation should be high due to mutation-drift balance. Evidence includes near-constancy of molecular clock rates and high synonymous divergence.

## How It's Best Learned
Compare synonymous and non-synonymous substitution rates in orthologs across species. Test for signals of selection using Ka/Ks ratios.

## Common Misconceptions
- Neutral theory claims selection is unimportant; it claims most variation and substitutions are neutral, while selection shapes coding changes.
- Neutral sites evolve by drift; neutral sites evolve by mutation-drift balance.

## Explainer

From your study of allele frequency change, you know that genetic drift and natural selection are both forces that shape allele frequencies over time. The default assumption in classical evolutionary biology was that most molecular differences between species reflect adaptive evolution — that selection drove each substitution to fixation because it conferred some advantage. In 1968, Motoo Kimura proposed a radical alternative: the vast majority of evolutionary changes at the molecular level are **selectively neutral**, neither beneficial nor harmful, and they spread through populations by random genetic drift alone.

The core logic rests on a mathematical insight. For a neutral mutation in a diploid population of size *N*, the probability that it eventually reaches fixation is simply 1/(2N) — the same as any single gene copy's frequency at birth. But new neutral mutations arise at a rate of 2Nμ per generation (where μ is the per-gene mutation rate), so the overall rate of neutral substitution equals 2Nμ × 1/(2N) = μ. The population size cancels out entirely. This means the rate at which neutral mutations accumulate between species depends only on the mutation rate, not on population size or ecological circumstances. This prediction became the foundation of the **molecular clock** — the observation that DNA sequences diverge between species at a roughly constant rate per unit time.

The strongest evidence for the neutral theory comes from comparing **synonymous** and **non-synonymous substitution rates**. Synonymous (silent) substitutions change a codon without changing the amino acid, so they are largely invisible to natural selection. Non-synonymous substitutions alter the amino acid and are therefore more likely to be subject to selective pressure. Across nearly all genes and species, synonymous substitutions accumulate much faster than non-synonymous ones. This pattern is exactly what neutral theory predicts: sites free from selective constraint evolve at the mutation rate, while sites under functional constraint evolve more slowly because most changes there are deleterious and get purged by **purifying selection**.

The neutral theory does not claim that natural selection is unimportant — it claims that selection primarily acts as a filter, removing harmful mutations rather than driving the fixation of beneficial ones. Most of the molecular variation you observe within a species (polymorphism) and between species (divergence) reflects the random fixation of neutral variants, not a history of adaptive sweeps. The ratio of non-synonymous to synonymous substitution rates (Ka/Ks or dN/dS) has become a standard tool for detecting selection: a ratio near 1 suggests neutrality, well below 1 suggests purifying selection, and above 1 suggests positive selection driving amino acid changes. The neutral theory thus provides the **null model** against which all claims of molecular adaptation must be tested.
