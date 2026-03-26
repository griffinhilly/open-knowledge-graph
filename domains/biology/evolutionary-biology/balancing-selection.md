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
status: validated
---

# Balancing Selection

## Core Idea
Balancing selection maintains multiple alleles in a population by favoring heterozygotes or varying selection across environments. Classic mechanisms include overdominance (heterozygote advantage) and frequency-dependent selection. Balancing selection is crucial for explaining persistent polymorphisms like ABO blood groups.

## Questions

```yaml
- question: "In a malaria-endemic region, HbA/HbS heterozygotes have higher fitness than either HbA/HbA or HbS/HbS homozygotes. As the HbS allele becomes very common in the population, what happens to its fitness advantage?"
  type: multiple-choice
  options:
    - "It increases — more HbS alleles means more heterozygotes, amplifying the advantage"
    - "It stays constant — heterozygote advantage is independent of allele frequency"
    - "It decreases — as HbS becomes common, most HbS alleles end up in HbS/HbS homozygotes (low fitness), eroding the advantage"
    - "The HbS allele rapidly goes to fixation because selection always favors the fitter allele"
  answer: 2
  explanation: "This is the self-stabilizing logic of overdominance. When HbS is rare, nearly every HbS allele is paired with an HbA allele in a heterozygote — high fitness. As HbS becomes common, increasingly many HbS alleles end up in HbS/HbS homozygotes, which suffer from sickle-cell disease. Selection now acts against HbS. The same logic applies symmetrically to HbA: rare HbA alleles enjoy the heterozygote advantage, but common HbA alleles accumulate in lower-fitness HbA/HbA homozygotes. Neither allele can spread to fixation because its fitness declines as it becomes common — producing a stable equilibrium where both persist."

- question: "In a prey species with two color morphs, predators form search images for the most common morph, making it easier to catch. Which type of balancing selection is operating, and what is its predicted outcome?"
  type: multiple-choice
  options:
    - "Overdominance — heterozygotes carrying both color genes have higher survival"
    - "Directional selection — one morph will eventually be favored and reach fixation"
    - "Negative frequency-dependent selection — the rare morph has higher fitness because predators focus on the common one, maintaining both morphs at equilibrium"
    - "Genetic drift — random fluctuations maintain both morphs equally"
  answer: 2
  explanation: "Negative frequency-dependent selection means fitness is negatively correlated with frequency: when your morph is common, predators target you; when it's rare, they overlook you. This creates a self-correcting dynamic. If one morph becomes too common, selection favors the rare alternative, which then increases in frequency until it faces the same disadvantage. The result is a stable equilibrium where both morphs coexist at predictable frequencies — neither can be driven to fixation. This mechanism is thought to maintain MHC diversity in immune systems, where rare alleles confer resistance to pathogens that have evolved to evade common immune responses."

- question: "Natural selection typically reduces genetic variation within a population by spreading the fittest allele and eliminating less fit alternatives."
  type: true-false
  answer: false
  explanation: "Directional selection does reduce variation, but balancing selection is a counterexample that actively maintains it. Under overdominance, neither homozygote is fittest — only the heterozygote — so neither allele can reach fixation. Under negative frequency-dependent selection, rare alleles gain a fitness advantage precisely because they are rare, preventing elimination. The result is that variation is preserved rather than eroded. This is not a trivial exception: many medically and ecologically important polymorphisms (sickle-cell trait, MHC alleles, ABO blood groups) persist in populations because balancing selection maintains them against the erosive forces of drift and directional selection."

- question: "Regions of the genome under balancing selection are expected to show unusually high heterozygosity and an excess of intermediate-frequency alleles compared to neutral regions of the genome."
  type: true-false
  answer: true
  explanation: "These are the molecular signatures of balancing selection. Under neutral evolution, alleles drift toward high or low frequencies, producing a distribution skewed toward rare alleles (Tajima's D ≈ 0 or negative). Balancing selection keeps alleles near intermediate frequencies — the stable equilibria it maintains — producing elevated heterozygosity and a positive Tajima's D. Allelic lineages also persist much longer than expected under drift, giving unusually deep genealogies. The HLA (MHC) loci in humans, for example, show trans-species polymorphisms — alleles shared with other primates for millions of years — a signature impossible under neutral evolution or directional selection."

- question: "Explain why overdominance (heterozygote advantage) produces a stable equilibrium where both alleles persist rather than one allele eventually driving the other to fixation."
  type: short-answer
  answer: "Overdominance creates a fitness landscape where the heterozygote Aa outperforms both homozygotes AA and aa. As a result, each allele has frequency-dependent fitness: when allele A is common, most A-bearing individuals are AA (low fitness), so selection acts against A. When A is rare, most A-bearing individuals are Aa (high fitness), so selection favors A. The same negative frequency dependence applies to allele a. Each allele is favored when rare and disfavored when common, producing a stable equilibrium frequency where both alleles persist indefinitely. At this equilibrium, the marginal fitness of each allele (averaged over all genotypes it appears in) is equal. Any perturbation from this equilibrium is corrected by selection, making it a stable attractor rather than a transient state."
```

## Explainer

From your study of natural selection, you know that selection typically favors one allele over another — the fitter allele spreads while the less fit one is eliminated. From genetic drift, you know that random fluctuations in small populations can also remove alleles. Both forces tend to reduce genetic variation. So here is the puzzle: why do many populations maintain multiple alleles at the same locus for thousands or even millions of years? **Balancing selection** is the answer — a family of selective mechanisms that actively preserve variation rather than eroding it.

The most intuitive mechanism is **overdominance**, or heterozygote advantage. If the heterozygote (Aa) has higher fitness than either homozygote (AA or aa), then neither allele can be driven to fixation. As the A allele becomes common, most A alleles find themselves in AA homozygotes, which are less fit than Aa — so selection pushes back against A's dominance. The same logic applies if a becomes too common. The system reaches a stable equilibrium frequency where both alleles persist indefinitely. The textbook example is sickle-cell anemia in malaria-endemic regions: the HbS allele causes disease in homozygotes (HbS/HbS) but confers malaria resistance in heterozygotes (HbA/HbS), maintaining both alleles in the population at predictable frequencies.

**Frequency-dependent selection** provides a different stabilizing mechanism. In **negative frequency-dependent selection**, rare phenotypes have a fitness advantage precisely because they are rare. Consider a prey species with two color morphs: predators form a search image for the common morph, so the rare morph escapes detection more often. As the rare morph increases in frequency, predators shift attention to it, and the formerly common morph now gains the advantage. The result is an oscillation around an equilibrium where both morphs coexist. This mechanism is thought to maintain variation in immune system genes (MHC loci), where rare alleles confer resistance to pathogens that have evolved to evade common immune responses.

Balancing selection also operates through **spatially or temporally varying selection** — an allele favored in one habitat or season may be disfavored in another, and if individuals move between environments or experience both conditions across their lifetime, neither allele wins outright. The signature of balancing selection in molecular data is distinctive: regions of the genome under balancing selection show elevated heterozygosity, an excess of intermediate-frequency alleles, and unusually deep genealogies where allelic lineages persist far longer than expected under drift alone. Recognizing these signatures helps explain why genetic variation is not merely noise left over from incomplete selection — in many cases, it is actively maintained because diversity itself is adaptive.
