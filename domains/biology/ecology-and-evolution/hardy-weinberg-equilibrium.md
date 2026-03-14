---
id: hardy-weinberg-equilibrium
title: Hardy-Weinberg Equilibrium
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-genetics-intro
  type: hard
- id: mendelian-genetics
  type: hard
- id: gene-flow
  type: soft
- id: genetic-drift
  type: soft
- id: simple-probability
  type: soft
- id: solving-quadratics-by-factoring
  type: soft
builds-toward:
- speciation
- molecular-evolution
tags:
- population-genetics
- allele-frequency
- null-model
- evolution
stage: formal-systems
status: validated
---

# Hardy-Weinberg Equilibrium

## Core Idea
Hardy-Weinberg equilibrium predicts that allele and genotype frequencies remain constant across generations in a large, randomly mating population with no selection, mutation, migration, or drift. Given allele frequencies p and q (p + q = 1), genotype frequencies are p², 2pq, and q². This null model is a baseline — deviations from it signal that evolutionary forces are acting. It is used to infer allele frequencies from genotype data and vice versa.

## How It's Best Learned
Practice calculating expected genotype frequencies from observed allele frequencies, then compare to observed genotypes to test for equilibrium. Work through violations — a population under directional selection will show systematic departures from HWE predictions.

## Common Misconceptions
- Hardy-Weinberg equilibrium does not mean evolution is impossible — it describes what happens when evolution is absent.
- The equation p² + 2pq + q² = 1 applies to diploid, sexually reproducing organisms under specific conditions.
- A population in HWE is not 'frozen' — phenotypes can vary; it is allele frequencies that are stable.
