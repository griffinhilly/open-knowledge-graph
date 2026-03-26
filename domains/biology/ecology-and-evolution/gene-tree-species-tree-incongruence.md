---
id: gene-tree-species-tree-incongruence
title: 'Gene Tree and Species Tree Incongruence: Lineage Sorting'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: coalescent-theory
  type: hard
- id: molecular-evolution
  type: hard
- id: phylogenetics-intro
  type: soft
builds-toward:
- speciation
tags:
- gene-tree
- species-tree
- incongruence
- lineage-sorting
stage: formal-systems
status: validated
---

# Gene Tree and Species Tree Incongruence: Lineage Sorting

## Core Idea
Gene trees can differ from species trees because genes take time to coalesce after speciation events. Incomplete lineage sorting (ILS) occurs when ancestral polymorphism persists through speciation; different genes retain different lineages. Rapid speciation exacerbates ILS. The coalescent theory explains the probability of gene-tree incongruence given speciation times and effective population size.

## Questions

```yaml
- question: "You sequence 1,000 genes from three closely related bird species (A, B, C). The species tree places A and B as sister species. You find 420 genes recover (A,B), 310 genes recover (A,C), and 270 genes recover (B,C). How should you interpret this result?"
  type: multiple-choice
  options:
    - "The true species tree is uncertain — you cannot trust any topology when only 42% of genes agree"
    - "The roughly equal frequencies of the two discordant topologies are consistent with incomplete lineage sorting: random ancestral sorting predicts the two alternative discordant trees should occur at approximately equal rates"
    - "The discordant trees indicate hybridization between species A–C and between B–C, because multiple topologies are recovered"
    - "The majority topology (A,B) is the species tree; the discordant trees represent sequencing errors that should be filtered out"
  answer: 1
  explanation: "ILS from random lineage sorting predicts a specific pattern: when discordance occurs, the two alternative discordant topologies (A,C) and (B,C) should appear at roughly equal frequencies, because there is no directional force favoring one over the other — ancestral alleles simply sort randomly. Here (310 vs 270) is roughly equal. Hybridization, by contrast, would produce directional discordance: one alternative topology would be enriched relative to the other because gene flow has a direction. Options A and D misunderstand that discordance under ILS is expected and informative, not erroneous."

- question: "Why does rapid adaptive radiation dramatically increase the probability of gene-tree and species-tree incongruence?"
  type: multiple-choice
  options:
    - "Rapid speciation increases mutation rates, generating more homoplasy that misleads gene tree reconstruction"
    - "Short intervals between successive speciation events leave little time for ancestral lineages to coalesce within each ancestral branch, so ancestral polymorphism persists through multiple speciations"
    - "Rapid speciation always involves hybridization, creating chimeric gene trees that cannot represent either parental species"
    - "Species that radiate rapidly have smaller effective population sizes, reducing the genetic variation needed for incongruence"
  answer: 1
  explanation: "ILS probability depends on the ratio of internodal time to effective population size, measured in coalescent units. In adaptive radiations, the intervals between successive speciation events are very short. There is little time for gene lineages in the ancestral populations to coalesce before the next split happens, so multiple ancient alleles get distributed across the new species and may sort into discordant gene trees. The same problem occurs with large ancestral population sizes, because more variation is present to sort discordantly."

- question: "When a gene tree disagrees with the established species tree, one of the two trees is expected to be wrong — the goal of phylogenomics is to identify and discard the incorrect gene tree."
  type: true-false
  answer: false
  explanation: "This is the central misconception the topic corrects. Gene trees and species trees are tracking different but real histories. A gene tree that disagrees with the species tree is not an error — it accurately reflects the genealogy of those gene copies, which happens to differ from the species branching pattern because of ILS, hybridization, or other processes. The goal of phylogenomics is not to discard discordant gene trees but to use the distribution of gene trees across the genome to estimate the species tree while explicitly accounting for the biological processes that cause discordance."

- question: "The effective population size of an ancestral species is a key factor determining the probability of gene-tree incongruence at any given speciation node in the species tree."
  type: true-false
  answer: true
  explanation: "Large ancestral populations maintain more genetic variation, giving gene lineages more distinct alleles that can be distributed discordantly among daughter species. The coalescent framework formalizes this: the expected time for two gene lineages to coalesce is proportional to 2Ne generations. A large Ne means coalescence takes longer, increasing the chance that lineages remain unsorted at the time of the next speciation event. This is why ILS is more severe in species with historically large populations, and why effective population size estimates are an important component of coalescent-based species tree inference."

- question: "How does gene-tree incongruence from incomplete lineage sorting differ in its statistical signature from incongruence caused by hybridization, and why does this distinction matter?"
  type: short-answer
  answer: "ILS produces random discordance: when a gene tree disagrees with the species tree, the two alternative discordant topologies occur at roughly equal frequencies because lineage sorting is a random process with no directional bias. Hybridization produces directional discordance: one discordant topology is enriched relative to the other because gene flow moves in a specific direction between specific lineages. This distinction matters because it allows researchers to diagnose the process causing discordance. If discordant topologies are roughly symmetric, ILS is the likely explanation. If one discordant topology consistently predominates, hybridization between specific lineages is implicated, which carries very different evolutionary implications."
  explanation: "The statistical signature of ILS versus hybridization is now used routinely in phylogenomics to test whether ancient gene flow occurred in a clade's history. This has produced major revisions in our understanding of, for example, human-Neanderthal-Denisovan relationships and the evolutionary history of many plant and animal groups."
```

## Explainer

From coalescent theory you already know that gene copies within a population trace back to a common ancestor, and that the time to coalescence depends on effective population size. Now consider what happens when a species splits into two — and then splits again before all gene copies within the ancestral population have coalesced. The ancestral species carried genetic variation: multiple alleles at any given locus. When speciation occurs, that variation gets partitioned among daughter species, but the gene lineages themselves are older than the speciation event. If a second split happens quickly, the gene copies may not have had time to sort into lineages that match the new species boundaries.

**Incomplete lineage sorting** (ILS) is the specific outcome where ancestral polymorphism persists through successive speciations, causing the genealogy of a gene to disagree with the branching pattern of species. Imagine three species — A, B, and C — where A and B are sister species. At a particular gene, the copy in species A might be more closely related to the copy in species C than to the copy in species B, simply because the ancestral population harbored both variants and they sorted randomly into the descendent lineages. The gene tree says (A,C) are sisters, but the species tree says (A,B) are sisters. Neither tree is wrong — they are tracking different histories.

The probability of incongruence depends on two factors you can reason about from coalescent principles: the **effective population size** of the ancestral species and the **time between successive speciation events**. Large ancestral populations maintain more variation, giving gene lineages more opportunity to sort discordantly. Short intervals between speciations — as in adaptive radiations — leave less time for lineages to coalesce within each ancestral branch. The ratio of internodal time to population size (measured in coalescent units) determines how likely ILS is at any node in the species tree.

This distinction between gene trees and species trees has profound practical consequences. If you sequence a single gene and build a phylogeny, you might recover the gene tree rather than the species tree, and misinterpret the evolutionary relationships. Modern phylogenomic approaches address this by sequencing many genes and using methods — such as multispecies coalescent models — that explicitly account for ILS. These methods estimate the species tree that best explains the distribution of gene tree topologies across the genome, rather than assuming all genes share the same history.

Recognizing gene-tree incongruence also helps distinguish ILS from other sources of discordance, such as hybridization and horizontal gene transfer. ILS produces a specific statistical signature: the two alternative discordant topologies occur at roughly equal frequencies, because the sorting is random. Hybridization, by contrast, tends to favor one discordant topology over the other, reflecting the direction of gene flow. This distinction makes gene-tree analysis a powerful diagnostic tool for understanding the processes that shaped a clade's history.
