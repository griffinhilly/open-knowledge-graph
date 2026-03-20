---
id: molecular-dating-phylogenetic-clocks
title: Molecular Clocks and Phylogenetic Dating
domain: biology
course: ecology-and-evolution
prerequisites:
- id: molecular-clock-hypothesis
  type: hard
- id: phylogenetic-inference-methods
  type: hard
- id: exponential-growth-and-decay
  type: soft
- id: statistics-rigorous
  type: soft
- id: exponential-distribution-theory
  type: soft
builds-toward:
- molecular-evolution-rates
tags:
- molecular-clock
- dating
- evolution
- phylogenetics
stage: advanced
status: draft
---

# Molecular Clocks and Phylogenetic Dating

## Core Idea
The molecular clock hypothesis assumes substitutions accumulate at relatively constant rates in DNA or proteins, allowing divergence time estimation. Rates vary among genes, lineages, and sites; relaxed clock models accommodate this variation. By calibrating molecular clocks with fossil dates, we estimate divergence times for groups lacking good fossils and test whether molecular predictions match paleontological dates.

## Explainer

You already know from the molecular clock hypothesis that DNA and protein sequences accumulate substitutions over time, and from phylogenetic inference that we can reconstruct the branching relationships among species. **Molecular dating** combines these two ideas: if we know the rate at which substitutions accumulate and the number of substitutions separating two lineages, we can estimate when those lineages diverged. The logic is analogous to estimating how long ago two travelers parted by measuring how far apart they are now and knowing their walking speed.

The simplest version assumes a **strict clock** — a single, constant substitution rate across all lineages. Under this model, the number of differences between two sequences is directly proportional to the time since their common ancestor. But real molecular evolution is messier. Substitution rates vary across genes (mitochondrial DNA evolves faster than many nuclear genes), across lineages (rodents evolve faster than whales), and across sites within a gene (functionally constrained sites evolve slowly). A strict clock applied blindly to such data will produce misleading dates, which is why modern phylogenetics uses **relaxed clock models** that allow rates to vary among branches while still estimating divergence times.

The critical step that anchors molecular dates to real time is **calibration**. Sequence differences alone tell you relative divergence — lineage A and B are twice as divergent as lineage C and D — but not absolute time. To convert relative divergence into years, you need at least one point where you independently know the age. Fossil first appearances are the most common calibration points: if the oldest fossil of a group dates to 65 million years ago, that provides a minimum age for the node where that group originated. Calibration fossils are set as constraints (usually minimum ages, since the true divergence must predate the first fossil), and the statistical framework distributes rate estimates across the tree to make all calibrated nodes consistent.

The power of molecular dating is that it lets us estimate divergence times for groups with poor or nonexistent fossil records — fungi, many invertebrate lineages, viruses — by borrowing calibration information from better-preserved relatives. It also serves as an independent check on paleontological dates. When molecular and fossil estimates agree, our confidence in both increases; when they disagree, it signals either rate variation we have not accounted for, fossil gaps, or calibration problems. This interplay between molecular and paleontological evidence is one of the most productive feedback loops in modern evolutionary biology.
