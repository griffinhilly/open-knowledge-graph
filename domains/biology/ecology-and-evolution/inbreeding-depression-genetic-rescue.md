---
id: inbreeding-depression-genetic-rescue
title: Inbreeding Depression and Genetic Rescue Mechanisms
domain: biology
course: ecology-and-evolution
prerequisites:
- id: inbreeding-consequences
  type: hard
- id: population-bottleneck-drift-inbreeding
  type: hard
- id: effective-population-size
  type: soft
- id: sampling-distributions
  type: soft
builds-toward:
- conservation-genetics-effective-size
tags:
- inbreeding-depression
- genetic-load
- purging
- genetic-rescue
stage: formal-systems
status: draft
---

# Inbreeding Depression and Genetic Rescue Mechanisms

## Core Idea
Inbreeding depression is reduced fitness in inbred individuals due to increased homozygosity of deleterious recessive alleles. Purging—selection against deleterious recessive mutations—can reduce inbreeding depression over time. Genetic rescue through immigration introduces new alleles and restores heterozygosity. Conservation programs must balance genetic rescue against swamping of local adaptations.

## Explainer

You already know from studying inbreeding consequences that mating between relatives increases homozygosity across the genome. **Inbreeding depression** is the fitness cost of that increased homozygosity. The mechanism is straightforward: every population carries deleterious recessive alleles at low frequency — mutations that are harmful when homozygous but masked when heterozygous. In a large, outbreeding population, most individuals carry these alleles in heterozygous form, so the damage stays hidden. When relatives mate, the probability of inheriting the same deleterious allele from both parents rises sharply. The result is offspring that are homozygous at more loci, exposing recessive diseases, reduced fertility, weakened immune function, and lower survival. This is why small, isolated populations — the kind you studied in population bottlenecks and drift — suffer disproportionately: drift removes alleles randomly, and the remaining individuals are increasingly related to one another.

A natural question follows: if inbreeding exposes deleterious recessives, can selection remove them? This process is called **purging**. When deleterious alleles become homozygous and reduce fitness, natural selection acts more efficiently against them than it could when they were hidden in heterozygotes. Over multiple generations of moderate inbreeding, purging can reduce the frequency of strongly deleterious recessives and partially alleviate inbreeding depression. However, purging is unreliable — it works best against alleles of large effect and fails against the many mildly deleterious alleles that collectively drag down fitness. Populations that crash to very small sizes often lose too much genetic variation through drift before purging can operate effectively, creating an "extinction vortex" where small size leads to inbreeding, which reduces fitness, which further shrinks the population.

**Genetic rescue** is the introduction of unrelated individuals (immigrants) into an inbred population to restore heterozygosity and mask deleterious recessives. Even a small number of immigrants can have dramatic effects. The classic example is the Florida panther: by the 1990s, fewer than 30 individuals remained, showing kinked tails, heart defects, and poor sperm quality — hallmarks of inbreeding depression. Eight female Texas pumas were introduced in 1995, and within a generation the population tripled and the physical abnormalities largely disappeared. The immigrant alleles restored heterozygosity at thousands of loci simultaneously.

The challenge in conservation genetics is that genetic rescue is not without risk. If the immigrant population is adapted to very different environmental conditions, introducing their alleles can disrupt locally adapted gene combinations — a phenomenon called **outbreeding depression**. A population of desert-adapted fish rescued with individuals from a cold-water population might produce hybrid offspring poorly suited to either environment. Conservation biologists must therefore evaluate the genetic distance between donor and recipient populations, the severity of inbreeding depression, and the degree of local adaptation before recommending genetic rescue. The effective population size concept you studied helps quantify how urgently rescue is needed: populations with very low effective size are losing heterozygosity rapidly and face the greatest risk of inbreeding depression overwhelming their capacity to persist.
