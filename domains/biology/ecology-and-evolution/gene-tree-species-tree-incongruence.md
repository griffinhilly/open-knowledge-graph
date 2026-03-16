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
status: draft
---

# Gene Tree and Species Tree Incongruence: Lineage Sorting

## Core Idea
Gene trees can differ from species trees because genes take time to coalesce after speciation events. Incomplete lineage sorting (ILS) occurs when ancestral polymorphism persists through speciation; different genes retain different lineages. Rapid speciation exacerbates ILS. The coalescent theory explains the probability of gene-tree incongruence given speciation times and effective population size.

## Explainer

From coalescent theory you already know that gene copies within a population trace back to a common ancestor, and that the time to coalescence depends on effective population size. Now consider what happens when a species splits into two — and then splits again before all gene copies within the ancestral population have coalesced. The ancestral species carried genetic variation: multiple alleles at any given locus. When speciation occurs, that variation gets partitioned among daughter species, but the gene lineages themselves are older than the speciation event. If a second split happens quickly, the gene copies may not have had time to sort into lineages that match the new species boundaries.

**Incomplete lineage sorting** (ILS) is the specific outcome where ancestral polymorphism persists through successive speciations, causing the genealogy of a gene to disagree with the branching pattern of species. Imagine three species — A, B, and C — where A and B are sister species. At a particular gene, the copy in species A might be more closely related to the copy in species C than to the copy in species B, simply because the ancestral population harbored both variants and they sorted randomly into the descendent lineages. The gene tree says (A,C) are sisters, but the species tree says (A,B) are sisters. Neither tree is wrong — they are tracking different histories.

The probability of incongruence depends on two factors you can reason about from coalescent principles: the **effective population size** of the ancestral species and the **time between successive speciation events**. Large ancestral populations maintain more variation, giving gene lineages more opportunity to sort discordantly. Short intervals between speciations — as in adaptive radiations — leave less time for lineages to coalesce within each ancestral branch. The ratio of internodal time to population size (measured in coalescent units) determines how likely ILS is at any node in the species tree.

This distinction between gene trees and species trees has profound practical consequences. If you sequence a single gene and build a phylogeny, you might recover the gene tree rather than the species tree, and misinterpret the evolutionary relationships. Modern phylogenomic approaches address this by sequencing many genes and using methods — such as multispecies coalescent models — that explicitly account for ILS. These methods estimate the species tree that best explains the distribution of gene tree topologies across the genome, rather than assuming all genes share the same history.

Recognizing gene-tree incongruence also helps distinguish ILS from other sources of discordance, such as hybridization and horizontal gene transfer. ILS produces a specific statistical signature: the two alternative discordant topologies occur at roughly equal frequencies, because the sorting is random. Hybridization, by contrast, tends to favor one discordant topology over the other, reflecting the direction of gene flow. This distinction makes gene-tree analysis a powerful diagnostic tool for understanding the processes that shaped a clade's history.
