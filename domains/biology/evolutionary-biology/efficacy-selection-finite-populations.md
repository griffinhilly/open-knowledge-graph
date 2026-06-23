---
id: efficacy-selection-finite-populations
title: Efficacy of Selection in Finite Populations
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: genetic-drift
  type: hard
- id: effective-population-size
  type: hard
- id: purifying-selection
  type: soft
builds-toward:
- nearly-neutral-evolution
- evolvability
tags:
- selection
- drift
- population-size
- efficacy
stage: advanced
status: validated
---

# Efficacy of Selection in Finite Populations

## Core Idea
Selection efficacy depends on selection coefficient relative to drift. When |s| << 1/(2Ne), drift dominates and selection fails to prevent fixation of deleterious alleles. Critical threshold determines whether selection or drift governs molecular evolution.

## Questions

```yaml
- question: "A mutation reduces fitness by 0.1% (s = −0.001) in a bacterial species with an effective population size of Ne = 10,000,000. What is the expected evolutionary fate of this mutation?"
  type: multiple-choice
  options:
    - "It will drift to fixation because the fitness effect is too small for selection to act on"
    - "Purifying selection will efficiently remove it because 2Ne·|s| = 20,000, far greater than 1"
    - "It will be maintained at intermediate frequency by balancing selection"
    - "Its fate is unpredictable regardless of population size, because drift is always stochastic"
  answer: 1
  explanation: "The threshold for selection to dominate drift is 2Ne·|s| >> 1. Here, 2 × 10,000,000 × 0.001 = 20,000 — vastly greater than 1. Purifying selection will efficiently remove this mutation. In a small population (Ne = 1,000), the same mutation has 2Ne·|s| = 2, close to 1, and drift could easily fix it. The mutation's fate is not inherent to the mutation alone — it depends on the ratio of selection strength to drift intensity, which is a property of the whole mutation-population system."

- question: "A conservation geneticist studying an endangered species (Ne ≈ 500) finds its genome has accumulated many mildly deleterious mutations absent from closely related common species. What explains this pattern?"
  type: multiple-choice
  options:
    - "The endangered species evolved in a harsher environment, inducing higher mutation rates"
    - "Oxidative stress from habitat degradation increases mutation rate in small populations"
    - "In small populations, mildly deleterious mutations have 2Ne·|s| < 1, placing them in the drift-dominated regime where they accumulate as if effectively neutral"
    - "The pattern reflects normal within-species variation that would also be found in large species if carefully examined"
  answer: 2
  explanation: "This is a direct application of the efficacy threshold. In the common species (large Ne), 2Ne·|s| >> 1 for these mutations and purifying selection removes them. In the endangered species (Ne ≈ 500), the same mutations fall below the threshold — 2Ne·|s| < 1 — so drift dominates and they accumulate. The mutations aren't more common because of a higher mutation rate (options A and B) but because selection is too weak relative to drift to purge them. This mutational accumulation is a real conservation concern called genetic erosion or, in extreme cases, mutational meltdown."

- question: "Natural selection is typically more effective than genetic drift at determining allele frequencies, because selection is directional while drift is random."
  type: true-false
  answer: false
  explanation: "Directionality does not guarantee dominance. Whether selection or drift governs allele frequencies depends on the ratio of |s| to 1/(2Ne). In small populations, drift can fix or eliminate alleles regardless of their fitness effects — beneficial alleles can be lost by drift and deleterious ones can fix. A strong directional signal (selection in a large-Ne population) beats random noise (drift). But a weak signal (selection in a small-Ne population) is overwhelmed by noise. 'Directional' means selection consistently pushes in one direction; it does not mean that push is strong enough to overcome drift."

- question: "A mutation with s = −0.0001 is 'effectively neutral' in a population of 1,000 individuals, meaning it behaves evolutionarily like a mutation with s = 0, even though its fitness effect is real."
  type: true-false
  answer: true
  explanation: "When |s| << 1/(2Ne), the fate of an allele is governed by drift rather than selection. For Ne = 1,000 and s = −0.0001: 2Ne·|s| = 0.2, well below 1. Drift will fix or lose this mutation with essentially the same probabilities as a strictly neutral mutation (s = 0). 'Effectively neutral' means the fitness effect is real in principle but too small relative to drift to affect evolutionary outcome. In a bacterial population with Ne = 10⁸, the same mutation would be far from neutral — 2Ne·|s| = 20, strongly selected. The same mutation, entirely different fate."

- question: "Explain why the efficacy of selection is not simply a property of a mutation's fitness effect but depends on the whole mutation-population system. What happens evolutionarily to a mildly deleterious mutation as effective population size decreases?"
  type: short-answer
  answer: "Selection efficacy is determined by the ratio of |s| to 1/(2Ne). The same mutation can be efficiently purged in a large population — where 2Ne·|s| >> 1 and selection dominates drift — yet drift to fixation as if neutral in a small population where 2Ne·|s| << 1. As Ne decreases, the critical threshold 1/(2Ne) rises, and mutations that were previously in the 'selection-dominated' regime enter the 'drift-dominated' regime. A mildly deleterious mutation (s = −0.001) is reliably eliminated in a population of millions but can easily fix in a population of hundreds. The mutation itself hasn't changed; what changed is the competitive balance between the selective force and the random sampling noise of drift."
  explanation: "This insight explains differences in genome architecture across species with different effective population sizes. Large-Ne organisms (bacteria, many invertebrates) have streamlined genomes because purifying selection efficiently removes transposable elements, pseudogenes, and introns. Small-Ne organisms (vertebrates, island species) accumulate genomic 'clutter' because selection is too weak relative to drift to purge it. The nearly neutral theory of molecular evolution, proposed by Tomoko Ohta, formalizes this by showing that the boundary between neutral and selected is set by population size — not by the intrinsic properties of the mutation alone."
```

## Explainer

You understand natural selection as a deterministic force that increases the frequency of beneficial alleles and removes deleterious ones. You also understand genetic drift as a stochastic force that causes random fluctuations in allele frequencies, especially in small populations. The question at the heart of this topic is: **when does selection actually work?** In an idealized infinite population, even the tiniest fitness difference would eventually be resolved by selection. But real populations are finite, and drift introduces noise that can swamp weak selective signals.

The critical insight is a threshold relationship between the **selection coefficient** (s) and the **effective population size** (Ne). When the absolute value of s is much greater than 1/(2Ne), selection dominates: beneficial alleles are very likely to increase in frequency, and deleterious alleles are very likely to be removed. The population is large enough that drift cannot overpower the fitness difference. But when |s| is much less than 1/(2Ne), drift dominates: the allele's fate is determined almost entirely by chance, regardless of whether it is beneficial or deleterious. The mutation is effectively **neutral** from evolution's perspective, even if it has a real, measurable effect on fitness. The boundary region where |s| ≈ 1/(2Ne) is where the contest between selection and drift is most uncertain.

A concrete example makes this tangible. Consider a mutation that reduces fitness by 0.01% (s = -0.0001). In a population with Ne = 1,000,000, the quantity 2Ne·s = 200, far greater than 1 — selection efficiently purges this mutation. But in a population with Ne = 1,000, 2Ne·s = 0.2, much less than 1 — drift dominates, and this mildly deleterious mutation can easily drift to fixation as if it were neutral. The same mutation, with the same fitness effect, has completely different evolutionary fates depending on population size. This is why small populations accumulate slightly deleterious mutations — a process called **genetic deterioration** or mutational meltdown in extreme cases.

This threshold has profound implications for molecular evolution. Most mutations in protein-coding genes are mildly deleterious, with selection coefficients in the range where population size determines their fate. In large populations (many bacteria, some insects), purifying selection is efficient and genomes stay lean. In small populations (many vertebrates, island species, endangered populations), weakly deleterious mutations accumulate because drift shields them from selection. This framework also explains why species with small effective population sizes tend to have larger genomes with more noncoding DNA, more pseudogenes, and more transposable elements — the genomic "junk" persists because selection is too weak relative to drift to remove it. The efficacy of selection is thus not a fixed property of a mutation but an emergent property of the mutation-population system.
