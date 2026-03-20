---
id: three-point-crosses-chromosome-interference
title: Three-Point Crosses and Chromosome Interference
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: genetic-mapping-recombination-frequency
  type: hard
- id: dihybrid-crosses
  type: soft
builds-toward:
- linkage-disequilibrium-evolutionary
tags:
- genetic-mapping
- three-point-cross
- interference
- linkage
stage: advanced
status: draft
---

# Three-Point Crosses and Chromosome Interference

## Core Idea
Three-point crosses involve three linked loci and reveal non-independence of crossovers: crossovers are not randomly distributed. Interference is the reduction in probability of a second crossover near a first crossover; coefficient of coincidence measures observed vs. expected double crossovers. This reveals the physical basis of recombination.

## How It's Best Learned
Analyze a three-point testcross progeny: identify parental, single-crossover, and double-crossover classes. Calculate map distances between adjacent genes, then predict frequencies and detect interference. Compare with data to understand the mechanics of crossing over.

## Common Misconceptions
- Assuming crossovers occur independently; interference shows they are not independent.
- Not recognizing that interference can vary along the chromosome and be sex-specific.
- Thinking double-crossover classes are the most frequent when they are the rarest class, allowing easy identification.

## Explainer

You already know from genetic mapping that recombination frequency between two loci estimates the genetic distance between them, and that linked genes produce fewer recombinant offspring than expected under independent assortment. A **three-point cross** extends this logic by tracking three linked genes simultaneously, and it reveals something two-point crosses cannot: crossovers along a chromosome are not independent events. A crossover in one interval changes the probability of a crossover occurring nearby.

The experimental setup is straightforward. You cross an organism heterozygous at three linked loci (ABC/abc) to a homozygous recessive tester (abc/abc), then classify every offspring by its combination of phenotypes. With three genes, there are eight possible phenotype classes that fall into four categories: **parentals** (the two most frequent classes, matching the original chromosome arrangements), **single crossovers in interval I** (recombination between genes A and B), **single crossovers in interval II** (recombination between genes B and C), and **double crossovers** (recombination in both intervals simultaneously). The double crossover class is always the rarest, and this is your entry point for analysis — comparing the two rarest classes to the parentals immediately tells you which gene is in the middle, because a double crossover reverses only the middle gene's allele relative to the parentals.

Once you have identified gene order and counted each class, you calculate map distances for each interval by summing all crossover events in that interval (singles plus doubles) and dividing by total offspring. The critical insight comes next: if crossovers in interval I and interval II were truly independent, the expected frequency of double crossovers would simply be the product of the two single-crossover frequencies. But when you compare expected doubles to observed doubles, you almost always find fewer doubles than predicted. This deficit is **interference** — a physical phenomenon in which the occurrence of one crossover suppresses additional crossovers nearby.

Interference is quantified through the **coefficient of coincidence** (c.o.c.), defined as observed double crossovers divided by expected double crossovers. **Interference** itself equals 1 minus the coefficient of coincidence. A coefficient of coincidence of 0.4 means you observed only 40% of the expected doubles, giving interference of 0.6 — a 60% reduction. Complete interference (interference = 1) means no double crossovers occur at all; no interference (interference = 0) means crossovers are fully independent. This is not just a statistical curiosity — it reflects the physical mechanics of recombination, where the protein machinery involved in one crossover event physically inhibits formation of another crossover within a certain chromosomal distance.
