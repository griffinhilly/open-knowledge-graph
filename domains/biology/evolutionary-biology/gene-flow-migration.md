---
id: gene-flow-migration
title: Gene Flow and Population Structure
domain: biology
course: evolutionary-biology
prerequisites:
- id: population-genetics-intro
  type: hard
- id: allele-frequency-change
  type: hard
builds-toward:
- allopatric-speciation
tags:
- gene-flow
- migration
- population-structure
- differentiation
stage: advanced
status: draft
---

# Gene Flow and Population Structure

## Core Idea
Gene flow (migration) introduces alleles from one population into another, homogenizing allele frequencies across populations and reducing genetic differentiation. Even small amounts of gene flow can counteract local adaptation and prevent speciation by swamping local selection. Conversely, restriction of gene flow allows populations to diverge and can lead to reproductive isolation and speciation.

## Explainer

You have already studied allele frequency change and the forces that drive it — selection, drift, mutation. **Gene flow**, also called **migration** in population genetics models, is the fourth force, and it is unique because it acts between populations rather than within them. Where selection and drift reshape a single population's allele frequencies, gene flow connects populations by transferring alleles from one gene pool to another. Understanding gene flow quantitatively allows you to predict whether populations will remain genetically similar or drift apart toward speciation.

The simplest model is the **island model**: imagine a large mainland population sending migrants to a small island population at rate *m* (the fraction of the island population replaced by migrants each generation). If the mainland has allele frequency *p* and the island has frequency *p'*, then after one generation of migration the island's new frequency shifts toward the mainland by an amount proportional to *m* × (*p* − *p'*). This means gene flow acts like a spring pulling the island frequency toward the mainland frequency, and the strength of that pull is directly proportional to the migration rate. Over many generations, even modest migration (a few percent per generation) is enough to make the island nearly genetically identical to the mainland.

The evolutionary significance becomes clear when you consider gene flow's interaction with other forces. Suppose the island environment favors a locally adaptive allele that is rare on the mainland. Selection pushes that allele's frequency up on the island, but gene flow keeps importing the mainland allele, dragging the frequency back down. The outcome depends on the relative strength: if selection is much stronger than gene flow (*s* >> *m*), local adaptation persists despite migration. If gene flow overwhelms selection (*m* >> *s*), the island population cannot maintain its local adaptation and instead mirrors the mainland genetically. This **migration-selection balance** is why populations of the same species can look very different across strong environmental gradients (where selection overcomes gene flow) but very similar across gentle ones (where gene flow homogenizes).

Gene flow's role in speciation is essentially the flip side of its homogenizing power. For two populations to diverge enough to become separate species, gene flow between them must be reduced below the threshold where it can counteract divergence by drift and selection. Geographic barriers accomplish this most obviously — a mountain range or ocean channel physically prevents migration. But gene flow can also be reduced by behavioral changes (different mating calls), temporal isolation (different breeding seasons), or habitat preferences (feeding in different microhabitats), even when populations are geographically close. This is why population geneticists measure gene flow indirectly through **FST** and related statistics: high genetic differentiation between populations implies low historical gene flow, providing evidence for the isolation that precedes speciation.
