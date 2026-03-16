---
id: genealogical-methods-phylogenetics
title: Genealogical and Coalescent Methods in Phylogenetics
domain: biology
course: evolutionary-biology
prerequisites:
- id: coalescent-theory
  type: hard
- id: phylogenetic-inference
  type: hard
- id: population-genetics-intro
  type: soft
builds-toward:
- molecular-evolution-rates
- bayesian-phylogenetics
tags:
- coalescent
- phylogenetics
- genealogy
- population-history
stage: advanced
status: draft
---

# Genealogical and Coalescent Methods in Phylogenetics

## Core Idea
Genealogical methods use genetic data to infer population history and evolutionary relationships by modeling how lineages coalesce backward in time. Enables estimation of divergence times, migration rates, demographic changes, and time to most recent common ancestor.

## Explainer

You have studied coalescent theory, which models how gene copies in a sample trace back to a common ancestor when you look backward in time. You have also studied phylogenetic inference, which reconstructs evolutionary trees from sequence data. Genealogical methods in phylogenetics bring these two frameworks together, using coalescent models as the statistical engine for phylogenetic analysis — particularly at the boundary between population genetics and species-level phylogenetics, where traditional tree-building methods begin to break down.

Traditional phylogenetic methods assume that a single tree describes the history of the sequences being analyzed. This assumption works well for distantly related species, where the species history and gene history are effectively identical. But for recently diverged species or populations within a species, different genes often have different genealogies due to incomplete lineage sorting, recombination, and gene flow. **Coalescent-based phylogenetic methods** address this by explicitly modeling the genealogical process within populations. Instead of forcing all genes onto one tree, these methods estimate the population-level parameters — effective population size, divergence times, migration rates — that generated the observed distribution of gene trees.

The practical workflow involves sampling multiple unlinked genetic loci from individuals across populations or species. Each locus has its own genealogy shaped by the stochastic coalescent process. The methods then ask: given a proposed demographic history (population sizes, split times, migration rates), what is the probability of observing these particular gene genealogies? By evaluating many possible demographic scenarios, typically through **Bayesian inference** using Markov chain Monte Carlo (MCMC) sampling, the methods identify the demographic model that best explains the data. The output includes not just a species tree but also estimates of ancestral population sizes and divergence times with credible intervals — quantities that are invisible to traditional phylogenetic approaches.

These methods are especially powerful for answering questions at the interface of microevolution and macroevolution. Did two species diverge with or without ongoing gene flow? How large was the ancestral population before a speciation event? When did populations split, and did they exchange migrants afterward? Has a population expanded or contracted in the recent past? By grounding phylogenetic inference in an explicit population-genetic model, genealogical methods convert sequence data into a remarkably detailed portrait of evolutionary history — one that captures not just the branching order of lineages but the demographic processes that shaped them.
