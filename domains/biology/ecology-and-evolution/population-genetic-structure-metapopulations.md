---
id: population-genetic-structure-metapopulations
title: Population Genetic Structure in Subdivided Populations
domain: biology
course: ecology-and-evolution
prerequisites:
- id: gene-flow-migration
  type: hard
- id: metapopulation-dynamics-connectivity
  type: hard
- id: probability-distributions
  type: soft
builds-toward:
- speciation
- conservation-genetics-effective-size
tags:
- population-structure
- fst
- wahlund-effect
- local-adaptation
stage: formal-systems
status: validated
---

# Population Genetic Structure in Subdivided Populations

## Core Idea
When populations are subdivided, genetic variation partitions between and within subpopulations. FST measures genetic differentiation; high FST indicates strong structure and restricted gene flow. Local adaptation can drive differentiation despite gene flow when selection is strong.

## Questions

```yaml
- question: "Two small island lizard populations have been isolated from each other for thousands of generations with no migration. Their FST for neutral genetic markers is 0.60. A researcher claims this high FST is clear evidence of local adaptation to different environments. What is the most important problem with this interpretation?"
  type: multiple-choice
  options:
    - "FST of 0.60 is not high enough to indicate significant differentiation between populations"
    - "FST cannot be computed for island populations — it only applies to mainland metapopulations"
    - "High FST at neutral markers can arise from genetic drift alone in small, isolated populations with no adaptive divergence — selection is not needed to explain this result"
    - "The researcher should have used FST values above 1.0 to detect local adaptation"
  answer: 2
  explanation: "This is the central interpretive trap in population genetics. FST measures genetic differentiation, not adaptation. In small isolated populations, random genetic drift will cause allele frequencies to diverge over generations at neutral loci — loci that have nothing to do with local environmental differences. To infer local adaptation, you need evidence that differentiation at specific loci exceeds what drift alone would predict (FST outlier tests), or direct evidence of differential fitness. High FST is a starting point for investigating adaptation, not evidence of it."

- question: "Human populations worldwide have an FST of approximately 0.10–0.15. What is the correct interpretation of this value?"
  type: multiple-choice
  options:
    - "About 85–90% of human genetic variation exists within any single population; only 10–15% reflects differences between populations"
    - "Human populations are 85–90% genetically identical to each other at the sequence level"
    - "Only 10–15% of human genes vary at all across the species"
    - "Human populations on the same continent are as genetically differentiated as those on different continents"
  answer: 0
  explanation: "FST = 0.10–0.15 means that 10–15% of total human genetic variation is partitioned between populations (between-group differences), while 85–90% exists within any single population (within-group variation). Two randomly chosen individuals from the same population differ almost as much genetically as two individuals from different continents. This result — first clearly articulated by Lewontin — has profound implications: most human genetic diversity is shared across all populations, and 'racial' categories capture only a small fraction of overall genetic variation."

- question: "Even very modest migration — roughly one effective migrant per generation between subpopulations — can prevent genetic drift from driving those subpopulations to fixation for completely different alleles."
  type: true-false
  answer: true
  explanation: "This is one of the most important quantitative results in population genetics, derived from Wright's island model. One migrant per generation sounds trivially small, but it is sufficient to introduce new alleles and prevent the complete drift-driven divergence (FST → 1) that would occur in total isolation. The formula FST ≈ 1/(1 + 4Nem) captures this: even Nem = 1 gives FST ≈ 0.20, representing substantial but not complete differentiation. This result explains why many geographically distributed species maintain considerable genetic cohesion despite limited dispersal."

- question: "Pooling individuals from two genetically differentiated subpopulations into a single sample will produce an excess of heterozygotes compared to Hardy-Weinberg expectations."
  type: true-false
  answer: false
  explanation: "This is the Wahlund effect, and it works in the opposite direction: pooling differentiated subpopulations produces a *deficit* of heterozygotes, not an excess. Here is the intuition: if subpopulation A has drifted toward allele frequency p₁ and subpopulation B toward p₂, each subpopulation has fewer heterozygotes than a single large panmictic population with the same overall allele frequency. Pooling doesn't increase heterozygosity — it reveals that the population was never one randomly mating unit to begin with. A heterozygote deficit in a sample is therefore a diagnostic signal of hidden population structure."

- question: "Explain why strong local selection can maintain genetic differentiation (high FST) at selected loci even when there is substantial gene flow between subpopulations."
  type: short-answer
  answer: "Gene flow introduces alleles from other subpopulations and is the primary force homogenizing allele frequencies across a metapopulation. Under normal circumstances, even moderate migration rapidly erodes differentiation. However, when selection against immigrants (or against locally maladapted alleles) is strong, each migrant allele that reaches a new subpopulation is selectively removed before it can spread — natural selection acts as a filter on the genetic material that gene flow introduces. The heavy-metal tolerance example illustrates this: non-tolerant alleles arriving via pollen flow onto contaminated mine tailings are immediately disadvantaged; tolerant alleles persist. This creates a locally adapted allele frequency pattern that is maintained generation after generation despite ongoing migration. The critical condition is that selection (measured by the selection coefficient s) must substantially exceed the migration rate m; when s >> m, local adaptation persists and FST at the selected loci remains high even though neutral loci nearby may be more homogenized."
  explanation: "This balance between gene flow and local selection is why metapopulations can simultaneously be genetically connected (low FST at neutral loci) and locally adapted (high FST at selected loci). Genome scans for adaptation exploit exactly this contrast — loci showing anomalously high FST relative to neutral expectations are candidate adaptive loci."
```

## Explainer

You have already learned that metapopulations are networks of subpopulations connected by dispersal, and that gene flow moves alleles between these subpopulations. Now consider what happens to the overall genetic architecture when a species is distributed across such a subdivided landscape. The key insight is that genetic variation does not distribute evenly — it **partitions** between levels, with some variation existing within each subpopulation and some existing as differences between subpopulations.

**FST** (fixation index) is the standard metric for quantifying this partitioning. It measures the proportion of total genetic variation that is due to differences between subpopulations rather than within them. An FST of 0 means all subpopulations have identical allele frequencies — they are genetically interchangeable. An FST of 1 means subpopulations share no genetic variation at all — they are completely differentiated. In practice, most values fall between these extremes. For example, human populations worldwide have an FST of roughly 0.10–0.15, meaning about 85–90% of genetic variation exists within any single population and only 10–15% distinguishes populations from each other. In contrast, island-dwelling land snails with limited dispersal may have FST values above 0.5.

What determines where a species falls on this spectrum? The answer comes from the balance between gene flow and the forces that drive divergence — primarily genetic drift and local selection. From your study of probability distributions, you can appreciate that drift is strongest in small populations, where random sampling of alleles creates large fluctuations between generations. In a metapopulation with small, isolated subpopulations and little migration, drift pushes each subpopulation in a random genetic direction, inflating FST. This is the **Wahlund effect** in action: if you pool individuals from genetically differentiated subpopulations, the combined sample shows a deficit of heterozygotes relative to Hardy-Weinberg expectations, because each subpopulation has drifted toward different allele frequencies.

Gene flow opposes this differentiation. Even very modest migration — on the order of one effective migrant per generation — can prevent drift from driving subpopulations to fixation for different alleles. But when **local selection** is strong, subpopulations can remain differentiated even in the face of substantial gene flow. A classic example is heavy-metal tolerance in grasses growing on mine tailings: plants just meters from non-contaminated soil maintain dramatically different allele frequencies at tolerance loci because selection against non-tolerant genotypes on the contaminated soil is intense enough to overwhelm the homogenizing effect of pollen flow. This tension between gene flow and local selection is a central theme in evolutionary ecology — it determines whether metapopulations act as a single evolutionary unit or as a collection of semi-independent lineages on their own adaptive paths.
