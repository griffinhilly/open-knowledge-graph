---
id: neutral-theory-molecular
title: Neutral Theory of Molecular Evolution
domain: biology
course: evolutionary-biology
prerequisites:
- id: molecular-evolution
  type: hard
- id: population-genetics-intro
  type: hard
builds-toward:
- molecular-clock-hypothesis
- synonymous-nonsynonymous-substitutions
tags:
- molecular-evolution
- neutral-evolution
- population-genetics
stage: advanced
status: validated
---

# Neutral Theory of Molecular Evolution

## Core Idea
Kimura's neutral theory proposes that most molecular sequence variation and substitutions are neutral and evolve primarily by genetic drift rather than natural selection. The theory predicts that substitution rates depend only on mutation rates and that nucleotide diversity is determined by population size and mutation rate (μ = 4Neμ).

## Questions

```yaml
- question: "A small island population and a large continental population of the same species are isolated from each other for 10,000 generations and accumulate mutations at the same rate μ. If neutral theory is correct, how should the number of neutral substitutions fixed in each population compare?"
  type: multiple-choice
  options:
    - "The large population fixes more substitutions because it has more individuals generating mutations"
    - "The small population fixes more substitutions because drift is stronger in small populations"
    - "Both populations fix approximately the same number of neutral substitutions, because the substitution rate equals the mutation rate regardless of population size"
    - "No neutral substitutions are fixed in either population because selection eliminates all neutral mutations"
  answer: 2
  explanation: "This is the neutral theory's most counterintuitive result. A small population has fewer mutations entering per generation but each one has a higher fixation probability (1/2Ne). A large population has more mutations but lower fixation probability per mutation. These two effects cancel exactly: 2Neμ × 1/(2Ne) = μ. The neutral substitution rate equals the mutation rate, independent of Ne. Option B is the intuitive-but-wrong answer — drift is stronger in small populations, but this only speeds fixation relative to the number of mutations, not relative to time."

- question: "A gene's rate of synonymous substitutions (mutations that do not change the amino acid) is much higher than its rate of nonsynonymous substitutions (mutations that change the amino acid). What does neutral theory predict this means?"
  type: multiple-choice
  options:
    - "Synonymous sites are more mutation-prone because they are in exposed regions of the chromosome"
    - "Nonsynonymous sites are evolving faster than neutral expectation, suggesting positive selection"
    - "Nonsynonymous substitutions are being constrained by purifying selection, so most amino acid-changing mutations are eliminated before fixation"
    - "Both types of sites are evolving neutrally but synonymous mutations are more common in the genome"
  answer: 2
  explanation: "Neutral theory predicts that synonymous mutations (usually silent at the protein level) should behave approximately neutrally and fix at the mutation rate. Nonsynonymous mutations that change amino acids are more likely to affect protein function — most will be deleterious and removed by purifying selection. The ratio of nonsynonymous to synonymous substitution rates (dN/dS) below 1 is therefore the signature of purifying selection constraining protein evolution. This is one of neutral theory's most powerful empirical applications."

- question: "According to the neutral theory, most observable nucleotide variation within a species is the result of selectively neutral mutations drifting in the population rather than being maintained by natural selection."
  type: true-false
  answer: true
  explanation: "Kimura's neutral theory holds that the majority of within-species polymorphism (nucleotide diversity) is composed of neutral or near-neutral variants drifting toward fixation or loss. The predicted nucleotide diversity θ = 4Neμ links observable variation directly to population size and mutation rate under this neutral assumption. Variants under strong positive or balancing selection exist but are rare relative to the neutral background."

- question: "The neutral theory of molecular evolution claims that natural selection is unimportant for the evolution of organisms, arguing that most phenotypic change is driven by genetic drift."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about neutral theory. Kimura explicitly stated that the theory makes no claim about phenotypic or organismal evolution — natural selection remains the primary mechanism shaping adaptations, organismal design, and phenotypic evolution. The neutral theory applies specifically to the molecular level: most of the variation you observe in DNA sequences is neutral and spreads by drift. The theory is agnostic about, not contradictory to, the role of selection in shaping the visible features of organisms."

- question: "Why is the neutral theory described as a 'null model' for molecular evolution, and how is it used to detect natural selection from sequence data?"
  type: short-answer
  answer: "The neutral theory specifies what molecular evolution should look like in the absence of selection: substitution rate equals mutation rate, diversity equals 4Neμ, and dN/dS equals approximately 1. This neutral expectation is the baseline against which real data is compared. When a gene evolves faster than the neutral rate (elevated dN/dS, excess nonsynonymous substitutions), this is evidence of positive selection accelerating change. When it evolves slower (dN/dS << 1), purifying selection is constraining it. Without the neutral null, you have no way to know what 'too fast' or 'too slow' means — any observed rate would be uninterpretable."
  explanation: "The analogy to Hardy-Weinberg equilibrium is instructive: both are null models that specify what to expect under the simplest assumptions (no selection, no drift, etc.). Deviations from the null are the signal of interest. Neutral theory turned molecular sequence data from description into hypothesis testing."
```

## Explainer

From your study of molecular evolution and population genetics, you understand that mutations arise constantly and that genetic drift causes random fluctuations in allele frequencies — fluctuations that are strongest in small populations. Motoo Kimura's **neutral theory of molecular evolution**, proposed in 1968, builds on these foundations with a surprising claim: the vast majority of mutations that become fixed in a population's DNA are not beneficial. They are selectively **neutral** — neither helping nor harming the organism — and they spread through populations by drift alone.

The mathematical elegance of the neutral theory comes from a key derivation. In a diploid population of effective size Ne, a new neutral mutation has a fixation probability of 1/(2Ne). Since there are 2Ne gene copies in the population and each mutates at rate μ per generation, the total number of new neutral mutations entering the population per generation is 2Ne × μ. Multiply the input rate by the fixation probability: 2Neμ × 1/(2Ne) = μ. The **substitution rate for neutral mutations equals the mutation rate**, regardless of population size. This is a profound result — it means the molecular clock ticks at a rate determined only by mutation, not by how large or small the population is.

The neutral theory does not claim that natural selection is unimportant for organismal evolution — it absolutely is. Rather, it claims that at the molecular level, most of the variation you observe (polymorphism within species) and most of the divergence you measure (substitutions between species) involves mutations with negligible fitness effects. Strongly deleterious mutations are removed by purifying selection and never contribute to divergence. Strongly beneficial mutations do fix by positive selection, but they are rare. The great middle ground — slightly deleterious to truly neutral mutations — dominates the molecular landscape.

The neutral theory provides a **null model** for molecular evolution, much like Hardy-Weinberg equilibrium provides a null model for population genetics. When you observe that a gene evolves faster or slower than the neutral prediction, that deviation is informative: faster substitution suggests positive selection driving change, while slower substitution reveals purifying selection constraining the sequence. Without the neutral baseline, you would have no framework for detecting selection from sequence data. The theory also predicts that nucleotide diversity within a population (θ) should equal 4Neμ, linking observable genetic variation directly to population size and mutation rate — a relationship that remains central to modern population genomics.
