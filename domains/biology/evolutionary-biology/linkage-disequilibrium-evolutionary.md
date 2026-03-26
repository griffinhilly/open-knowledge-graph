---
id: linkage-disequilibrium-evolutionary
title: Linkage Disequilibrium and Evolutionary Dynamics
domain: biology
course: evolutionary-biology
prerequisites:
- id: population-genetics-intro
  type: hard
- id: genetic-drift
  type: hard
tags:
- linkage
- recombination
- genetic-association
- haplotype
stage: formal-systems
status: validated
---

# Linkage Disequilibrium and Evolutionary Dynamics

## Core Idea
Linkage disequilibrium (LD) is the non-random association of alleles at different loci, caused by limited recombination, genetic drift, or selection on linked sites. LD decays over time through recombination, but patterns of LD across the genome reveal population history, selection, and recombination rates. LD is fundamental to genome-wide association studies (GWAS).

## Questions

```yaml
- question: "A genome-wide association study identifies a SNP marker strongly associated with Type 2 diabetes risk, but functional studies find no biological effect of that SNP itself. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The GWAS statistical methods produced a false positive, and the association is not real"
    - "The marker SNP is in linkage disequilibrium with a nearby causal variant, so the association is a proxy signal"
    - "The marker SNP has a pleiotropic effect on diabetes through an unknown pathway"
    - "The association is confounded by population stratification in the study sample"
  answer: 1
  explanation: "GWAS exploits LD: a marker SNP that is in strong LD with a causal variant will show strong statistical association with the disease even if the marker itself has no biological function. The causal variant and the marker are inherited together on the same haplotype because recombination has not yet separated them. This is not a false positive — the association is real; the marker is just a proxy. Finding the true causal variant requires fine-mapping the LD block with denser SNP coverage or functional experiments."

- question: "A human population experienced a severe genetic bottleneck 200 generations ago, followed by rapid expansion. Compared to an ancient, large population that has never bottlenecked, this population would be expected to have:"
  type: multiple-choice
  options:
    - "Less linkage disequilibrium, because genetic drift broke up haplotype blocks during the bottleneck"
    - "More linkage disequilibrium across longer chromosomal stretches, because drift created new associations that have had limited time to decay"
    - "The same LD structure, because recombination rates are identical in both populations"
    - "Less genetic variation overall but the same LD structure, since LD depends only on recombination rate"
  answer: 1
  explanation: "A bottleneck creates new LD through genetic drift — random sampling of a small founder population creates chance associations between alleles that may persist for many generations. With 200 generations since the bottleneck, recombination has had limited time to break up these haplotype blocks, especially for closely linked loci. The bottleneck population will have longer LD blocks (reflecting recent history) compared to the ancient population where recombination has been eroding LD over thousands of generations. This is why populations with recent bottlenecks (e.g., isolated island populations) often show extended LD useful for gene mapping."

- question: "Linkage disequilibrium can mainly exist between alleles at loci that are physically located on the same chromosome."
  type: true-false
  answer: false
  explanation: "While physical linkage (proximity on the same chromosome) is the most common cause of LD and produces the most persistent LD, genetic drift in small populations can create LD between alleles at unlinked loci — even loci on different chromosomes. In a small founding population, random sampling can cause alleles at independent loci to co-occur more often than expected by chance. This drift-generated LD typically decays rapidly (halving each generation for unlinked loci), but in very small populations or over short timescales it can be substantial. LD is therefore a property of allele frequency co-distributions, not just physical proximity."

- question: "Over many generations in a large population, linkage disequilibrium between two loci tends to decrease, with tightly linked loci losing LD more slowly than distantly linked ones."
  type: true-false
  answer: true
  explanation: "LD decays at a rate of (1 − r) per generation, where r is the recombination fraction between the two loci. For tightly linked loci (r ≈ 0), LD decays very slowly — nearly intact from generation to generation. For unlinked loci (r = 0.5), LD halves each generation and approaches zero quickly. This differential decay is what makes LD patterns informative: long haplotype blocks indicate either recent origin (not enough generations for recombination to break them) or tight physical linkage, while short blocks indicate ancient, well-mixed populations or high local recombination rates."

- question: "How does the length of linkage disequilibrium blocks across a genome serve as a record of population history, and what does a genome with unusually long LD blocks tell you?"
  type: short-answer
  answer: "LD blocks decay through recombination over generations. Long LD blocks indicate that allele combinations have not had enough time or recombination events to be broken apart — this signature arises after recent events that created new associations: a selective sweep (a beneficial mutation dragging nearby alleles along via genetic hitchhiking), a population bottleneck (random drift creating new associations in a small founder group), or recent admixture (chromosomal segments from one population entering another with their original haplotype structure intact). Short, fragmented LD blocks indicate an ancient, large, well-recombined population. A genome with unusually long LD blocks therefore suggests recent demographic events or strong recent selection."
  explanation: "The relationship between LD block length and evolutionary history is one of the most powerful tools in population genomics. Because the expected rate of LD decay is mathematically predictable from recombination rates, the observed excess of long blocks can be used to date when events occurred — the longer the blocks, the more recent the event. This logic underlies methods for detecting selection sweeps, identifying admixture events, and reconstructing bottleneck history from modern genetic data."
```

## Explainer

From your work in population genetics, you know that allele frequencies change through drift and selection, and that different loci in a genome can behave independently — in theory. **Linkage disequilibrium** (LD) describes the situation where alleles at two different loci are found together on the same chromosome more often (or less often) than you would predict from their individual frequencies alone. If allele A at one locus and allele B at a nearby locus appear together on 60% of chromosomes, but their individual frequencies predict only 40% co-occurrence, those loci are in linkage disequilibrium.

The key force that creates LD is physical proximity on a chromosome. When two loci are close together, recombination rarely separates them, so allele combinations that arise together — whether by mutation, migration, or drift — persist across generations as a block called a **haplotype**. Genetic drift in small populations can also generate LD by chance, even between unlinked loci, because random sampling creates temporary associations. Selection acting on one locus drags nearby alleles along for the ride, a phenomenon called **genetic hitchhiking**, which creates extended regions of LD around beneficial mutations.

The critical insight is that LD is not permanent — it **decays** over time. Each generation of recombination shuffles allele combinations, gradually breaking apart haplotype blocks. The rate of decay depends on the recombination rate between the loci: tightly linked loci lose LD slowly, while distant or unlinked loci reach equilibrium (linkage equilibrium) quickly. This decay is measured by the parameter D, which starts at its maximum value when a new haplotype appears and halves roughly every generation for unlinked loci, or decays at rate (1 − r) per generation where r is the recombination fraction.

This decay property makes LD a powerful tool for reading evolutionary history. Long blocks of LD suggest recent events — a selective sweep, a population bottleneck, or recent admixture — because recombination has not yet had time to break them apart. Short LD blocks indicate ancient, well-recombined populations. In genome-wide association studies (GWAS), researchers exploit LD to find disease-associated variants: if a causal mutation is in LD with a nearby marker SNP, the marker's statistical association with the disease serves as a proxy for the causal variant. Understanding LD structure across the genome is therefore essential for interpreting both evolutionary patterns and the architecture of complex traits.
