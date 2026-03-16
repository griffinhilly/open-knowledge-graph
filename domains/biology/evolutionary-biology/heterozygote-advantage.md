---
id: heterozygote-advantage
title: Heterozygote Advantage and Overdominance
domain: biology
course: evolutionary-biology
prerequisites:
- id: adaptation-and-fitness
  type: hard
- id: dominance-and-recessiveness
  type: hard
- id: balancing-selection
  type: soft
builds-toward:
- balancing-selection
- population-genetics-intro
tags:
- selection
- polymorphism
- allele-frequency
- fitness
stage: advanced
status: draft
---

# Heterozygote Advantage and Overdominance

## Core Idea
Heterozygotes possess higher fitness than both homozygotes, maintaining genetic polymorphism at stable intermediate allele frequencies. Classic example: sickle-cell trait confers malaria resistance without severe anemia cost in heterozygotes.

## Explainer

From adaptation and fitness, you know that natural selection increases the frequency of alleles that confer higher reproductive success. From dominance and recessiveness, you know that diploid organisms carry two copies of each gene and that the phenotypic expression of alleles depends on their dominance relationships. Heterozygote advantage — also called **overdominance** — arises when the heterozygous genotype (one copy of each allele, Aa) has *higher fitness* than either homozygote (AA or aa). This creates a situation where selection cannot drive either allele to fixation, because as one allele becomes common, the other becomes rare and increasingly appears in the high-fitness heterozygous state.

The sickle-cell example makes the logic concrete. The hemoglobin S allele (HbS), when homozygous (HbS/HbS), causes severe sickle-cell anemia — a devastating condition that sharply reduces fitness. The normal allele (HbA), when homozygous (HbA/HbA), produces healthy red blood cells but offers no special resistance to malaria. The heterozygote (HbA/HbS) gets the best of both worlds: enough normal hemoglobin to avoid serious anemia, but enough altered hemoglobin to create an inhospitable environment for *Plasmodium falciparum* parasites inside red blood cells. In malaria-endemic regions of sub-Saharan Africa, the heterozygote survives both threats better than either homozygote. The result is **balancing selection** that maintains both alleles in the population at a stable equilibrium frequency.

The equilibrium frequency is predictable from the relative fitness values. If we define the fitness of AA as 1 - s (reduced by malaria susceptibility), Aa as 1 (highest), and aa as 1 - t (reduced by sickle-cell disease), then the equilibrium frequency of the HbS allele is q̂ = s / (s + t). The allele cannot disappear because when it is rare, nearly all copies exist in heterozygotes where they are positively selected; it cannot go to fixation because when it is common, too many homozygous aa individuals are produced and removed by selection. This **frequency-dependent dynamic** is self-correcting — any perturbation from equilibrium is automatically corrected by selection, making the polymorphism stable rather than transient.

Beyond sickle cell, heterozygote advantage has been proposed for several other systems: cystic fibrosis heterozygotes may have had increased resistance to cholera or typhoid; MHC heterozygotes present a broader array of pathogen peptides to the immune system, improving pathogen recognition. However, unambiguous cases of overdominance are rarer than once thought — many apparent examples turn out to involve other forms of balancing selection (frequency-dependent selection, spatially varying selection) rather than true overdominance. The concept remains important because it provides the clearest mechanism by which natural selection *actively maintains* genetic variation, countering the common misconception that selection always reduces variation by driving alleles to fixation or loss.
