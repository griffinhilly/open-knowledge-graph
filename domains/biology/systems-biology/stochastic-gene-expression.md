---
id: stochastic-gene-expression
title: Stochastic Gene Expression
domain: biology
course: systems-biology
prerequisites:
- id: ode-models-in-biology
  type: hard
- id: gene-expression-overview
  type: hard
- id: probability-distributions
  type: soft
builds-toward:
- synthetic-gene-circuits
- cell-cycle-modeling
tags:
- gene-expression-noise
- stochastic-modeling
- Gillespie-algorithm
- intrinsic-noise
- extrinsic-noise
stage: expert
status: validated
---
# Stochastic Gene Expression

## Core Idea
Gene expression is inherently stochastic: transcription and translation are probabilistic events involving small numbers of molecules (often fewer than 10 mRNA copies per gene per cell), producing random fluctuations in protein levels even among genetically identical cells in the same environment. This noise is decomposed into intrinsic noise (randomness in the biochemical reactions of a specific gene) and extrinsic noise (cell-to-cell variation in shared cellular machinery like ribosomes and polymerases). Stochastic modeling using the chemical master equation or Gillespie algorithm captures these fluctuations, revealing that noise is not merely an imperfection but a functional feature exploited by cells for bet-hedging, probabilistic differentiation, and phenotypic diversity.

## Questions

```yaml
- question: "Two copies of the same gene (labeled with different fluorescent proteins) are measured simultaneously in single cells. One copy is green, the other red. If the green and red signals are uncorrelated across cells, what does this indicate about the dominant source of noise?"
  type: multiple-choice
  options:
    - "Extrinsic noise dominates, because shared cellular factors affect both copies equally"
    - "Intrinsic noise dominates, because the independent fluctuations in each gene copy's transcription are not coordinated"
    - "There is no noise — the measurements are simply inaccurate"
    - "The genes are on different chromosomes, which eliminates noise"
  answer: 1
  explanation: "This is the classic dual-reporter experiment by Elowitz et al. (2002). If noise were purely extrinsic (variations in ribosomes, polymerase, growth rate), both copies would fluctuate together — when the cell has more ribosomes, both green and red expression increase. Correlated fluctuations = extrinsic noise. Uncorrelated fluctuations (one copy high while the other is low in the same cell) can only arise from randomness intrinsic to each copy's individual transcription and translation events. The relative contribution of intrinsic vs. extrinsic noise depends on expression level and gene characteristics."

- question: "Stochastic gene expression noise is always detrimental to cell function and is minimized by natural selection."
  type: true-false
  answer: false
  explanation: "While some gene circuits (like those controlling essential metabolic enzymes) have evolved to minimize noise through negative feedback and high copy numbers, noise is functionally beneficial in many contexts. Bacterial persistence — where a small fraction of cells stochastically enters a dormant state resistant to antibiotics — is a bet-hedging strategy that relies on gene expression noise. Probabilistic cell fate decisions in the immune system and in stem cell differentiation also exploit noise to generate phenotypic diversity from genetically identical populations. Natural selection shapes noise levels to match functional requirements."

- question: "Why does the Gillespie algorithm, rather than deterministic ODEs, become necessary for modeling gene expression in single cells?"
  type: short-answer
  answer: "ODEs describe average behavior over large populations but assume continuous concentrations — valid when molecule numbers are large. In single cells, key molecular species exist in very small numbers (often 1-10 mRNA molecules per gene, a few transcription factor molecules at a promoter). At these copy numbers, the discrete, probabilistic nature of individual reaction events (one mRNA molecule being made, one being degraded) produces significant fluctuations around the ODE solution. The Gillespie algorithm simulates each individual reaction event as a stochastic process, correctly capturing the probability distributions of molecular species over time rather than just the mean."
  explanation: "The Gillespie algorithm (also called the stochastic simulation algorithm, SSA) is exact for well-mixed chemical systems: it samples the time to the next reaction and which reaction occurs from the appropriate probability distributions. For gene expression with low mRNA copy numbers, Gillespie simulations produce the characteristic bursty, noisy expression patterns seen in single-cell experiments — behavior that is entirely invisible to ODE models, which only describe population averages."
```

## Explainer

Classical molecular biology and traditional ODE models treat gene expression as a deterministic process: given the concentration of transcription factors and the state of signaling pathways, each gene produces a predictable amount of mRNA and protein. This deterministic view works well for describing population averages — the mean expression level across millions of cells. But single-cell measurements, enabled by fluorescent reporters and single-molecule imaging, revealed a startling reality: genetically identical cells in the same environment express the same gene at wildly different levels. This cell-to-cell variability is not measurement error — it is **gene expression noise**, an inherent consequence of the molecular mechanics of transcription and translation.

The physical basis of noise is the **small-number problem**. A typical bacterial gene produces a few mRNA molecules at a time, each of which is translated into a burst of proteins before being degraded. With so few molecules, the law of large numbers does not apply — statistical fluctuations are a large fraction of the mean. Transcription itself is bursty: a gene's promoter switches stochastically between active and inactive states, producing intermittent bursts of mRNA separated by silent periods. The combination of burst frequency, burst size, and mRNA/protein lifetimes determines the noise level (typically quantified as the coefficient of variation, CV = standard deviation / mean).

Noise is decomposed into two components using the **dual-reporter technique** pioneered by Elowitz et al. (2002). Two identical copies of a gene (distinguishable by fluorescent color) are placed in the same cell. **Intrinsic noise** produces uncorrelated fluctuations between the two copies (one is high while the other is low), arising from the stochastic biochemistry of each copy's individual transcription and translation. **Extrinsic noise** produces correlated fluctuations (both copies are simultaneously high or low), arising from cell-to-cell variation in shared resources — ribosome abundance, polymerase levels, cell size, growth rate. In practice, both components contribute, with their relative importance depending on expression level and cellular context.

Far from being a nuisance, noise has been co-opted by evolution for functional purposes. **Bet-hedging** in bacteria (persisters that survive antibiotics through stochastic dormancy), **probabilistic differentiation** in developing organisms (stochastic commitment to alternative cell fates), and **phenotypic diversification** in clonal populations all exploit gene expression noise. Computational models using the Gillespie algorithm or the chemical master equation quantify how network architecture shapes noise — negative feedback reduces it, positive feedback amplifies it, and specific circuit designs (like the toggle switch) convert continuous noise into discrete, stable cell states. Understanding noise is essential for designing reliable synthetic gene circuits and for explaining how genetically identical cells produce the phenotypic diversity required for tissue development and stress adaptation.
