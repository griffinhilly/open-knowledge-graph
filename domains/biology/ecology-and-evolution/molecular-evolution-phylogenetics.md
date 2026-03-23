---
id: molecular-evolution-phylogenetics
title: Molecular Evolution and Phylogenetic Inference
domain: biology
course: ecology-and-evolution
prerequisites:
- id: molecular-evolution
  type: hard
- id: phylogenetics-intro
  type: soft
- id: dna-sequence-divergence
  type: soft
builds-toward:
- extinction-rates-phylogenetic-patterns
tags:
- molecular-evolution
- phylogenetics
- molecular-clock
- neutral-theory
stage: formal-systems
status: draft
---

# Molecular Evolution and Phylogenetic Inference

## Core Idea
DNA and protein sequences accumulate mutations over time, allowing inference of evolutionary relationships and divergence times. The molecular clock hypothesis proposes mutations accumulate at relatively constant rates, enabling dating. Phylogenetic methods (parsimony, likelihood, Bayesian) reconstruct evolutionary trees. Most nucleotide evolution is neutral.

## Questions

```yaml
- question: "Researchers compare the rate of nucleotide substitution between humans and chimpanzees for two genes: a metabolic enzyme central to basic cellular function, and a surface antigen that humans evolved to resist in response to a pathogen. The immune antigen gene shows a substitution rate five times higher than the metabolic gene. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "The antigen gene mutates more frequently because immune genes have fewer DNA repair mechanisms"
    - "Both genes evolve under neutral drift, but the antigen gene drifted faster by chance"
    - "The elevated rate in the antigen gene signals positive selection — adaptive changes spread faster than the neutral background clock rate"
    - "The metabolic gene is more conserved because it evolved more recently than the antigen gene"
  answer: 2
  explanation: "Under the neutral theory, most substitutions accumulate at a roughly constant rate — the molecular clock. Genes under strong purifying selection evolve slower than neutral expectation (their mutations are harmful and removed); genes under positive selection evolve faster (beneficial mutations spread rapidly). A substitution rate five times higher than a neutral benchmark is the molecular signature of positive selection — adaptive changes are being fixed faster than chance drift would predict. This is how molecular evolution detects adaptation in the genome without needing to observe organisms in nature."

- question: "What makes the molecular clock a viable tool for dating evolutionary divergences?"
  type: multiple-choice
  options:
    - "All DNA sequences evolve at the same rate, so any gene can be used to measure time"
    - "Neutral mutations accumulate at a roughly constant rate per generation, making the degree of sequence divergence proportional to time since divergence"
    - "The clock is perfectly accurate and requires no calibration from external sources"
    - "Most mutations are beneficial, so they spread at predictable rates governed by natural selection"
  answer: 1
  explanation: "The clock works because most mutations that persist long enough to be compared between species are selectively neutral — they accumulate by drift at a rate proportional to the mutation rate and generation time. This gives a roughly constant baseline substitution rate that can be converted to absolute time once calibrated with a fossils or geological event of known age. The clock is not perfectly constant (rates vary across lineages and genes) but statistical models can account for this variation. Options A and C overstate the clock's precision; option D confuses neutral drift with selection-driven change."

- question: "The neutral theory of molecular evolution implies that natural selection plays no important role in shaping genomes."
  type: true-false
  answer: false
  explanation: "The neutral theory says that the majority of OBSERVED substitutions between species are neutral — they accumulated by drift rather than selection. It does NOT claim that selection is unimportant. Purifying selection continuously removes the vast majority of new mutations (which are deleterious), keeping genomes functional. Positive selection occasionally drives adaptive change. What the neutral theory adds is that after filtering out mutations removed by selection, the ones that persist and spread to fixation are overwhelmingly neutral. Neutrality describes the pattern of differences we observe; selection still governs what doesn't persist."

- question: "The molecular clock can be used to estimate divergence times in lineages that left no fossil record, provided the clock is calibrated using at least one divergence event with a known date."
  type: true-false
  answer: true
  explanation: "This is the practical power of the molecular clock. Once you use a calibration point — a fossil with a known minimum age, or a geological event like the separation of continents that isolated populations — you can convert sequence divergence per site into absolute time. The calibration anchors the rate, and the same rate can then estimate divergence times for any other pair of lineages. Deep-sea bacteria, ancient fungal lineages, and insect radiations that left no fossils can all be dated this way. Calibration quality (the precision and accuracy of the fossil date) propagates directly into uncertainty of the molecular date."

- question: "Why is the fact that most molecular evolution is neutral important for the reliability of the molecular clock?"
  type: short-answer
  answer: "If most molecular evolution were driven by natural selection, rates would vary unpredictably — genes under strong positive selection would accumulate changes rapidly during adaptive episodes, while genes under purifying selection would stall. The resulting rates would be too erratic to function as a clock. Neutral mutations, by contrast, accumulate by drift at a rate primarily determined by the mutation rate and generation time — a relatively constant process. The neutrality of most substitutions is what gives the molecular clock its regularity. Departures from clock-like behavior (genes evolving faster or slower than expected) are diagnostic of selection, which is itself a useful signal."
  explanation: "The clock metaphor works because the tick rate is not set by fitness landscapes (which change) but by the underlying mutation rate (which is relatively stable). Strongly deleterious mutations are weeded out before they can accumulate; strongly beneficial ones are too rare to dominate. The neutral mutations that drift to fixation fill in at a predictable rate, creating the clock signal. This is also why some genes are better molecular clocks than others: highly conserved genes (under strong purifying selection) tick slowly and are good for dating deep divergences; rapidly evolving genes are better for recent splits."
```

## Explainer

From your study of molecular evolution, you know that DNA sequences change over time through mutation, and that most of these changes are selectively neutral — they neither help nor harm the organism. From phylogenetics, you know that shared derived characters can reveal which species are more closely related. Molecular evolution and phylogenetics fuse these ideas: instead of comparing bones or body plans, we compare DNA and protein sequences directly, using the accumulated differences as a record of evolutionary history written in the genome itself.

The central concept is the **molecular clock**. If neutral mutations accumulate at a roughly constant rate per generation, then the number of sequence differences between two species is proportional to the time since they diverged from a common ancestor. Compare the hemoglobin gene in humans and mice: the more substitutions you count, the longer ago those lineages split. Calibrate the clock using a fossil with a known date — say, the oldest primate fossil at 55 million years — and you can estimate divergence times for lineages that left no fossils at all. The clock is not perfectly constant (rates vary across genes, lineages, and time periods), but statistical models can account for this variation, making molecular dating a powerful complement to the fossil record.

**Phylogenetic inference** uses sequence data to reconstruct the branching pattern of evolution — the tree of life. Three major approaches compete. **Parsimony** finds the tree requiring the fewest total mutations, appealing in its simplicity but sometimes misleading when mutation rates vary across branches. **Maximum likelihood** evaluates which tree best explains the observed sequences under an explicit model of how DNA evolves (including different rates for transitions versus transversions, or variation across sites). **Bayesian methods** extend likelihood by incorporating prior information and producing probability distributions over possible trees rather than a single best estimate. All three approaches align sequences, compare them position by position, and search the vast space of possible tree topologies for the one that best fits the data.

A key insight from this field is that most molecular evolution is **neutral** — the majority of substitutions that accumulate between species were invisible to natural selection. This is not a statement that most mutations are unimportant; rather, it means that the mutations which persist long enough to be observed in species comparisons are overwhelmingly ones that had no fitness effect. Strongly deleterious mutations are removed by selection before they can spread, and strongly beneficial ones are rare. The neutral background provides the steady tick of the molecular clock, while departures from neutrality — genes evolving faster or slower than expected — flag regions under positive or purifying selection, revealing where adaptation has left its molecular signature.
