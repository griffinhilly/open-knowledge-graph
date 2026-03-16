---
id: molecular-evolution-rates
title: Molecular Clock and Evolutionary Rate Variation
domain: biology
course: evolutionary-biology
prerequisites:
- id: molecular-clock-hypothesis
  type: hard
- id: substitution-rates
  type: hard
- id: neutral-theory-molecular
  type: hard
- id: probability-axioms-and-rules
  type: soft
- id: statistics-probability
  type: soft
builds-toward:
- genealogical-methods-phylogenetics
tags:
- molecular-clock
- evolution-rate
- substitution
- time
stage: advanced
status: draft
---

# Molecular Clock and Evolutionary Rate Variation

## Core Idea
Rates of molecular evolution vary among sites (constrained sites evolve slowly), genes (different functions have different constraints), and lineages (generation time, population size affect rates). Understanding rate variation is essential for accurate molecular dating and phylogenetic inference.

## Explainer

From your study of the molecular clock hypothesis and substitution rates, you know the basic idea: neutral mutations accumulate at a roughly steady rate, so the number of differences between two sequences can estimate how long ago they diverged. But "roughly steady" hides important complexity. In practice, the rate of molecular evolution is not a single universal constant — it varies at three distinct levels, and understanding each is essential for using molecular data to date evolutionary events accurately.

The first level is **among-site rate variation**. Within a single protein, some amino acid positions are buried in the hydrophobic core and are critical for folding, while others sit on the surface and tolerate substitution. A mutation that disrupts protein folding is eliminated by purifying selection regardless of how often it arises, so these constrained sites accumulate almost no substitutions over millions of years. Surface residues, by contrast, may evolve rapidly. This is why the neutral theory — your prerequisite — predicts that the substitution rate equals the neutral mutation rate: sites under strong constraint have a low neutral mutation rate (most mutations there are deleterious), while unconstrained sites have a high one. Statistically, among-site rate variation is often modeled with a **gamma distribution**, which captures the observation that most sites evolve slowly and a few evolve very fast.

The second level is **among-gene rate variation**. Histone genes, which encode proteins that package DNA and must interact precisely with every gene in the genome, evolve extremely slowly — histone H4 differs by only two amino acids between peas and cows. Fibrinopeptides, which are clipped off during blood clotting and have minimal functional constraints, evolve roughly 500 times faster. The principle is the same as among-site variation but applied at a broader scale: genes under stronger functional constraint have lower neutral mutation rates and therefore lower substitution rates. This is why molecular dating studies must calibrate rates gene by gene rather than applying a single universal clock.

The third level is **among-lineage rate variation**. Even for the same gene, substitution rates can differ between species. Rodents evolve faster than primates at most loci, partly because rodents have shorter **generation times** — more DNA replications per year means more replication errors per year. Population size also matters: in small populations, slightly deleterious mutations can fix by genetic drift (recall that drift overwhelms selection when the selection coefficient *s* is much less than 1/2N_e), inflating the observed substitution rate above the strictly neutral rate. These lineage effects mean that a simple molecular clock — one rate fits all branches — often fails, and modern phylogenetic methods use **relaxed clock models** that allow each branch of the tree to have its own rate, constrained by a statistical distribution.

Putting these three sources of variation together, the molecular clock is better understood as an approximate and calibration-dependent tool rather than a precise metronome. Accurate molecular dating requires choosing appropriate genes, modeling among-site rate variation, calibrating with fossil or biogeographic evidence, and accounting for lineage-specific rate shifts. When these factors are handled carefully, molecular dates often agree well with the fossil record — but when they are ignored, estimated divergence times can be off by tens of millions of years.
