---
id: population-genetic-structure-metapopulations
title: Population Genetic Structure in Subdivided Populations
domain: biology
course: ecology-and-evolution
prerequisites:
- id: gene-flow-population-structure
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
status: draft
---

# Population Genetic Structure in Subdivided Populations

## Core Idea
When populations are subdivided, genetic variation partitions between and within subpopulations. FST measures genetic differentiation; high FST indicates strong structure and restricted gene flow. Local adaptation can drive differentiation despite gene flow when selection is strong.

## Explainer

You have already learned that metapopulations are networks of subpopulations connected by dispersal, and that gene flow moves alleles between these subpopulations. Now consider what happens to the overall genetic architecture when a species is distributed across such a subdivided landscape. The key insight is that genetic variation does not distribute evenly — it **partitions** between levels, with some variation existing within each subpopulation and some existing as differences between subpopulations.

**FST** (fixation index) is the standard metric for quantifying this partitioning. It measures the proportion of total genetic variation that is due to differences between subpopulations rather than within them. An FST of 0 means all subpopulations have identical allele frequencies — they are genetically interchangeable. An FST of 1 means subpopulations share no genetic variation at all — they are completely differentiated. In practice, most values fall between these extremes. For example, human populations worldwide have an FST of roughly 0.10–0.15, meaning about 85–90% of genetic variation exists within any single population and only 10–15% distinguishes populations from each other. In contrast, island-dwelling land snails with limited dispersal may have FST values above 0.5.

What determines where a species falls on this spectrum? The answer comes from the balance between gene flow and the forces that drive divergence — primarily genetic drift and local selection. From your study of probability distributions, you can appreciate that drift is strongest in small populations, where random sampling of alleles creates large fluctuations between generations. In a metapopulation with small, isolated subpopulations and little migration, drift pushes each subpopulation in a random genetic direction, inflating FST. This is the **Wahlund effect** in action: if you pool individuals from genetically differentiated subpopulations, the combined sample shows a deficit of heterozygotes relative to Hardy-Weinberg expectations, because each subpopulation has drifted toward different allele frequencies.

Gene flow opposes this differentiation. Even very modest migration — on the order of one effective migrant per generation — can prevent drift from driving subpopulations to fixation for different alleles. But when **local selection** is strong, subpopulations can remain differentiated even in the face of substantial gene flow. A classic example is heavy-metal tolerance in grasses growing on mine tailings: plants just meters from non-contaminated soil maintain dramatically different allele frequencies at tolerance loci because selection against non-tolerant genotypes on the contaminated soil is intense enough to overwhelm the homogenizing effect of pollen flow. This tension between gene flow and local selection is a central theme in evolutionary ecology — it determines whether metapopulations act as a single evolutionary unit or as a collection of semi-independent lineages on their own adaptive paths.
