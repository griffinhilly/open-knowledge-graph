---
id: effective-recombination-rate
title: Effective Recombination Rate and Linked Selection
domain: biology
course: evolutionary-biology
prerequisites:
- id: recombination-evolution
  type: hard
- id: efficacy-selection-finite-populations
  type: hard
- id: linkage-disequilibrium-evolutionary
  type: hard
builds-toward:
- molecular-evolution-rates
tags:
- recombination
- linked-selection
- efficacy
- evolution
stage: advanced
status: validated
---

# Effective Recombination Rate and Linked Selection

## Core Idea
The effective recombination rate experienced by a locus depends on local recombination and linkage to other sites under selection. Even modest recombination is reduced effective when linked to many selected sites, reducing efficacy of selection genome-wide.

## Questions

```yaml
- question: "A neutral mutation arises near a centromere, a region with very low physical recombination rates and many neighboring sites under purifying selection. Compared to a neutral mutation in a high-recombination gene-poor region, what pattern would you expect for this centromere-proximal mutation?"
  type: multiple-choice
  options:
    - "Higher genetic diversity and more efficient positive selection, because purifying selection on neighbors removes competing alleles"
    - "Lower genetic diversity, stronger linkage disequilibrium, and reduced efficacy of selection on any weakly beneficial variants it sits near"
    - "Similar diversity levels, because physical recombination rate is what determines evolutionary outcomes"
    - "Higher diversity, because background selection continuously generates new neutral variation in the region"
  answer: 1
  explanation: "Low-recombination regions near centromeres experience strong linked selection — both background selection (purifying selection on deleterious mutations drags down linked neutral variants) and selective sweeps (beneficial mutations carry nearby neutral variants to fixation, reducing diversity). Both effects reduce effective population size for neutral loci in the region. Smaller effective population size means genetic drift is stronger, weakly beneficial mutations are less efficiently selected, and linkage disequilibrium persists longer. The signature: lower diversity, higher LD, and accumulation of mildly deleterious mutations — exactly the pattern observed empirically near centromeres across species."

- question: "A selective sweep occurs when a strongly beneficial mutation rapidly rises to fixation. How does this event affect the effective recombination rate at nearby loci?"
  type: multiple-choice
  options:
    - "It increases effective recombination by creating new recombination opportunities as the swept haplotype spreads"
    - "It has no effect on effective recombination because the physical crossover rate is unchanged"
    - "It reduces effective recombination because the sweep generates strong linkage disequilibrium that persists until recombination gradually dismantles it"
    - "It reduces effective recombination only in high-recombination regions, where sweeps are more common"
  answer: 2
  explanation: "A selective sweep drives a specific haplotype to very high frequency very quickly, eliminating most of the pre-existing diversity in the region and creating a long block of linkage disequilibrium. Even though physical recombination continues at the normal rate, crossovers must now occur within a nearly monomorphic region where everyone carries the same haplotype — so they cannot generate new allelic combinations. The effective recombination rate is low because the raw material for recombinant diversity has been eliminated. In regions where sweeps are frequent, new LD is being generated faster than recombination can dismantle it, chronically suppressing effective recombination."

- question: "Regions of the genome with low physical recombination rates tend to show lower genetic diversity and higher linkage disequilibrium than high-recombination regions, across species from Drosophila to humans."
  type: true-false
  answer: true
  explanation: "This is one of the best-established patterns in population genomics. The correlation between recombination rate and genetic diversity was first documented in Drosophila and later confirmed across many species. It confirms that effective recombination rate — not just physical recombination — governs how efficiently selection operates. Low-recombination regions experience stronger linked selection (both background selection and hitchhiking), which reduces the effective population size for neutral loci, lowers diversity, and sustains extended LD blocks. Y chromosomes, which have essentially no recombination, represent the extreme case: they accumulate deleterious mutations and lose diversity at dramatic rates."

- question: "A locus with a high physical recombination rate will always experience efficient selection and maintain high genetic diversity, regardless of its genomic context."
  type: true-false
  answer: false
  explanation: "Physical recombination rate is only part of the story. A locus embedded in a dense cluster of selected sites will experience linked selection even if crossovers occur frequently, because selection on neighbors continuously regenerates linkage disequilibrium faster than recombination breaks it down. The *effective* recombination rate — the rate at which recombination successfully decouples the focal locus from neighboring selected variation — is the relevant quantity. If the density of selected sites is high enough, even a locus with a high physical recombination rate can behave as if it were in a low-recombination environment, showing reduced diversity and less efficient selection."

- question: "Why is the effective recombination rate often much lower than the physical recombination rate, and what are the consequences for selection efficacy?"
  type: short-answer
  answer: "Physical recombination rate measures the frequency of crossovers between two positions during meiosis. But a crossover is only evolutionarily effective if it separates alleles in linkage disequilibrium. When neighboring sites are under selection — either purifying (removing deleterious mutations) or positive (driving beneficial ones to fixation) — selection on those neighbors continuously regenerates associations between alleles at the focal locus and its neighborhood. Background selection and selective sweeps both create new LD faster than recombination can break it down. The focal locus therefore behaves as if recombination were much rarer. Consequences: drift becomes stronger (smaller effective population size), weakly beneficial mutations are less efficiently selected, and deleterious mutations accumulate rather than being removed."
  explanation: "This is the central insight of the topic: effective recombination rate is determined jointly by the local physical crossover rate AND the density and strength of selection at linked sites. Genome architecture — where recombination hotspots and coldspots fall relative to gene density and selected sites — therefore shapes how efficiently selection operates across the genome. This explains why Y chromosomes, chromosomal inversions, and centromere-proximal regions all show signs of reduced selection efficacy: they are not just physically low-recombination; they are also dense with linked selected sites."
```

## Explainer

From your study of recombination in evolution and linkage disequilibrium, you know that recombination breaks apart associations between alleles at different loci, allowing natural selection to act on each variant more independently. The **effective recombination rate** is the rate at which recombination actually succeeds in decoupling a focal locus from its genomic neighborhood — and it is often much lower than the raw, physical recombination rate would suggest.

The physical recombination rate tells you how often crossovers occur between two positions on a chromosome during meiosis. But a crossover only matters evolutionarily if it separates alleles that are in linkage disequilibrium — alleles whose association affects their joint fate under selection. If a neutral mutation sits in a genomic region where many neighboring sites are under selection (either positive or purifying), selection on those neighbors drags the neutral variant along for the ride. This **linked selection** effect means that even though crossovers may be occurring at the normal physical rate, the focal locus behaves as if recombination were much rarer, because selection at linked sites keeps regenerating the associations that recombination tries to break down.

Two specific forms of linked selection drive this reduction. **Background selection** occurs when purifying selection continuously removes deleterious mutations and, with them, any neutral variants that happen to sit on the same haplotype. This reduces the effective population size experienced by neutral loci in low-recombination regions, which from your understanding of selection efficacy in finite populations means that drift becomes stronger and selection on weakly beneficial mutations becomes less effective. **Selective sweeps** occur when a strongly beneficial mutation rises to fixation, carrying with it a swath of linked neutral variation — a "hitchhiking" event that locally eliminates diversity and linkage disequilibrium. In regions where sweeps occur frequently, the effective recombination rate drops because new associations are constantly being created and driven to fixation faster than recombination can dismantle them.

The practical consequences are visible across genomes. Regions of low recombination — near centromeres, on sex chromosomes, or in chromosomal inversions — consistently show lower genetic diversity, higher linkage disequilibrium, and a greater accumulation of slightly deleterious mutations than high-recombination regions. This pattern, observed across species from *Drosophila* to humans, confirms that effective recombination rate, not just physical recombination rate, determines how efficiently selection can operate. For evolutionary biology, this means that genome architecture — where recombination hotspots and coldspots fall — shapes the distribution of adaptive and deleterious variation, influencing everything from the rate of molecular evolution to the long-term fate of non-recombining genomic regions like Y chromosomes.
