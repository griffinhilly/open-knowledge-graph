---
id: balancing-selection
title: Balancing Selection
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: genetic-drift
  type: soft
builds-toward:
- polymorphism-maintenance
tags:
- selection
- genetic-variation
- equilibrium
stage: advanced
status: draft
---

# Balancing Selection

## Core Idea
Balancing selection maintains multiple alleles in a population by favoring heterozygotes or varying selection across environments. Classic mechanisms include overdominance (heterozygote advantage) and frequency-dependent selection. Balancing selection is crucial for explaining persistent polymorphisms like ABO blood groups.

## Explainer

From your study of natural selection, you know that selection typically favors one allele over another — the fitter allele spreads while the less fit one is eliminated. From genetic drift, you know that random fluctuations in small populations can also remove alleles. Both forces tend to reduce genetic variation. So here is the puzzle: why do many populations maintain multiple alleles at the same locus for thousands or even millions of years? **Balancing selection** is the answer — a family of selective mechanisms that actively preserve variation rather than eroding it.

The most intuitive mechanism is **overdominance**, or heterozygote advantage. If the heterozygote (Aa) has higher fitness than either homozygote (AA or aa), then neither allele can be driven to fixation. As the A allele becomes common, most A alleles find themselves in AA homozygotes, which are less fit than Aa — so selection pushes back against A's dominance. The same logic applies if a becomes too common. The system reaches a stable equilibrium frequency where both alleles persist indefinitely. The textbook example is sickle-cell anemia in malaria-endemic regions: the HbS allele causes disease in homozygotes (HbS/HbS) but confers malaria resistance in heterozygotes (HbA/HbS), maintaining both alleles in the population at predictable frequencies.

**Frequency-dependent selection** provides a different stabilizing mechanism. In **negative frequency-dependent selection**, rare phenotypes have a fitness advantage precisely because they are rare. Consider a prey species with two color morphs: predators form a search image for the common morph, so the rare morph escapes detection more often. As the rare morph increases in frequency, predators shift attention to it, and the formerly common morph now gains the advantage. The result is an oscillation around an equilibrium where both morphs coexist. This mechanism is thought to maintain variation in immune system genes (MHC loci), where rare alleles confer resistance to pathogens that have evolved to evade common immune responses.

Balancing selection also operates through **spatially or temporally varying selection** — an allele favored in one habitat or season may be disfavored in another, and if individuals move between environments or experience both conditions across their lifetime, neither allele wins outright. The signature of balancing selection in molecular data is distinctive: regions of the genome under balancing selection show elevated heterozygosity, an excess of intermediate-frequency alleles, and unusually deep genealogies where allelic lineages persist far longer than expected under drift alone. Recognizing these signatures helps explain why genetic variation is not merely noise left over from incomplete selection — in many cases, it is actively maintained because diversity itself is adaptive.
