---
id: slightly-deleterious-mutations
title: Slightly Deleterious Mutations and Mutational Load
domain: biology
course: evolutionary-biology
prerequisites:
- id: mutation-selection-balance
  type: hard
- id: genetic-drift
  type: hard
- id: population-genetics-intro
  type: soft
- id: nearly-neutral-evolution
  type: hard
builds-toward:
  - efficacy-selection-finite-populations
tags:
- mutation
- deleterious
- load
- genome-evolution
stage: advanced
status: validated
---
# Slightly Deleterious Mutations and Mutational Load

## Core Idea
Mildly deleterious mutations accumulate in small populations because drift overwhelms weak purifying selection. This reduces population fitness (mutational load) and becomes critical in conservation biology and speciation.

## Questions

```yaml
- question: "A mutation has a selection coefficient of s = 0.00005. Population A has an effective size of Nₑ = 5,000 and Population B has Nₑ = 500,000. What is the most accurate statement about this mutation in the two populations?"
  type: multiple-choice
  options:
    - "The mutation is equally deleterious in both populations because the selection coefficient is a fixed property of the allele"
    - "The mutation is effectively neutral in Population A (drift dominates) but subject to efficient purifying selection in Population B"
    - "The mutation will fix faster in Population B because larger populations have more individuals to carry it"
    - "The mutation will be eliminated in Population A because small populations have stronger selection pressure per individual"
  answer: 1
  explanation: "The key threshold is whether s is much larger or much smaller than 1/(2Nₑ). For Population A (Nₑ = 5,000), 1/(2Nₑ) = 0.0001, which is larger than s = 0.00005 — so drift overwhelms selection and the mutation behaves essentially as neutral. For Population B (Nₑ = 500,000), 1/(2Nₑ) = 0.000001, which is far smaller than s — so selection efficiently detects and removes the mutation. Crucially, the mutation itself hasn't changed; what changed is the population's ability to 'see' it. This is the defining insight of the nearly neutral framework: the fate of a mutation depends on both its intrinsic effect and the population context."

- question: "According to Ohta's nearly neutral theory, what pattern would you expect in the rate of amino acid substitution when comparing lineages with large versus small effective population sizes?"
  type: multiple-choice
  options:
    - "Higher substitution rates in large-population lineages, because more mutations occur per generation in larger populations"
    - "Equal substitution rates in all lineages, because most amino acid substitutions are strictly neutral"
    - "Higher substitution rates in small-population lineages, because slightly deleterious mutations behave as neutral and fix more readily"
    - "Higher substitution rates in large-population lineages, because stronger selection drives adaptive fixation of beneficial mutations"
  answer: 2
  explanation: "Ohta's nearly neutral theory predicts that slightly deleterious mutations — those with s ≈ 1/(2Nₑ) — will behave as neutral in small populations and be purged in large ones. This means more slightly deleterious amino acid changes should fix in small-Nₑ lineages (because they slip past selection), producing higher substitution rates. This prediction contrasts with Kimura's strictly neutral theory (which predicts equal rates across all population sizes) and with adaptive evolution (which predicts higher rates in large populations where beneficial mutations are more common). Empirical comparisons across taxa have confirmed that substitution rates are indeed higher in lineages inferred to have smaller effective population sizes."

- question: "The same mutation can be efficiently removed by purifying selection in a large population but drift to fixation in a small population."
  type: true-false
  answer: true
  explanation: "This is the central insight of the slightly deleterious mutation framework. Whether a mutation is 'visible' to selection depends on the ratio of its selection coefficient (s) to the power of drift (1/2Nₑ). The mutation's intrinsic fitness effect is fixed, but its evolutionary fate depends on population context. In a population of millions, selection can reliably detect fitness differences of 0.001%; in a population of hundreds, such differences are swamped by random sampling noise. This means the same genome change can be adaptive, neutral, or deleterious in different population contexts — a key insight for comparing molecular evolution across taxa."

- question: "Whether a mutation counts as 'slightly deleterious' is a fixed property of the mutation's biochemical effect on the organism, independent of population size."
  type: true-false
  answer: false
  explanation: "This is the core misconception that slightly deleterious mutation theory corrects. 'Slightly deleterious' is not a fixed label for certain mutations — it describes mutations whose population-genetic behavior sits in the zone where drift and selection compete. The same mutation with s = 0.0001 is effectively neutral (behaves as nearly neutral) in a population of Nₑ = 1,000 but is subject to efficient purifying selection in a population of Nₑ = 1,000,000. The boundary is 1/(2Nₑ), which varies with population size. This is why endangered species with small populations accumulate genetic damage that large populations of the same species would clear efficiently."

- question: "Explain the concept of mutational meltdown and describe why it creates a self-reinforcing cycle."
  type: short-answer
  answer: "Mutational meltdown is a process in which slightly deleterious mutations accumulate in a small population, reducing mean fitness, which further reduces population size (through increased mortality or reduced reproduction), which in turn reduces Nₑ even further. A smaller Nₑ means that even weaker selection coefficients fall below the drift threshold, allowing still more slightly deleterious mutations to fix. Each round of fitness reduction accelerates the next: the population becomes smaller, the genetic filter becomes coarser, more mutations accumulate, fitness drops further. Without intervention, this feedback loop can drive the population to extinction even in a stable environment."
  explanation: "Mutational meltdown illustrates why slightly deleterious mutations are not merely a theoretical curiosity — they have direct conservation implications. The key is the feedback: fitness reduction → population size reduction → weaker selection → more mutation accumulation → further fitness reduction. This is why conservation genetics prioritizes maintaining adequate effective population size: once a population enters the meltdown trajectory, recovery is difficult even if external threats are removed. Students who understand the cycle understand why Ne management is not just about inbreeding depression but also about long-term genomic health."
```

## Explainer

You already understand mutation-selection balance: in large populations, selection efficiently removes deleterious alleles, maintaining them at low equilibrium frequencies. And from genetic drift, you know that random sampling effects are strongest in small populations. **Slightly deleterious mutations** sit at the intersection of these two forces, in a regime where neither dominates cleanly. These are mutations with small negative fitness effects — a selection coefficient (s) so tiny that drift can overpower selection in finite populations.

The critical threshold is the relationship between selection strength and population size. When the selection coefficient s is much larger than 1/(2Nₑ), where Nₑ is the effective population size, selection "sees" the mutation and can remove it efficiently. But when s is on the order of 1/(2Nₑ) or smaller, the mutation behaves almost as if it were neutral — drift pushes it up and down in frequency, and it may fix purely by chance despite being harmful. In a population of 10,000, a mutation with s = 0.00005 is effectively invisible to selection. In a population of 1,000,000, that same mutation is efficiently purged. The mutation hasn't changed; the population's ability to detect it has.

This has profound consequences. **Mutational load** — the cumulative fitness reduction caused by segregating deleterious alleles — builds up faster in small populations because their "filter" for weak selection is coarser. Imagine a quality control inspector examining widgets on an assembly line: a careful inspector (large population) catches tiny defects, while a rushed one (small population) misses them. Over time, the rushed inspector lets through many subtly flawed products. For real organisms, this means small populations gradually accumulate genetic damage that large populations would have eliminated.

The implications extend across biology. In conservation, endangered species with small population sizes face a **mutational meltdown** risk: as slightly deleterious mutations accumulate, fitness drops, which further reduces population size, which allows even more deleterious mutations to drift to fixation — a vicious cycle. In molecular evolution, the observation that most amino acid substitutions between species are slightly deleterious (not strictly neutral) led Tomoko Ohta to propose the **nearly neutral theory**, refining Kimura's original neutral model. The key prediction is that substitution rates for slightly deleterious mutations should be higher in lineages with smaller effective population sizes — a pattern confirmed across many taxonomic comparisons.
