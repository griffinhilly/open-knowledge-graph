---
id: disruptive-selection
title: Disruptive Selection
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
builds-toward:
- sympatric-speciation
- polymorphism-maintenance
tags:
- selection
- adaptive-peaks
stage: advanced
status: draft
---

# Disruptive Selection

## Core Idea
Disruptive (or diversifying) selection favors phenotypic extremes while selecting against intermediates, creating a bimodal distribution. This mechanism can maintain multiple distinct phenotypes and is thought to drive sympatric speciation when coupled with reproductive isolation.

## Questions

```yaml
- question: "A seed-eating bird population lives on an island that has only small and large seeds — very few medium-sized seeds. Over generations, the population's beak-size distribution becomes bimodal, with the middle beak-size class nearly absent. This pattern is most consistent with:"
  type: multiple-choice
  options:
    - "Stabilizing selection, which eliminates extremes and preserves medium phenotypes"
    - "Directional selection, which shifts the entire population toward larger beaks"
    - "Disruptive selection, where medium-beaked birds have lower fitness than both extremes"
    - "Genetic drift, which randomly eliminates intermediate phenotypes from the population"
  answer: 2
  explanation: "Disruptive selection favors both extremes at the expense of intermediates. In this environment, small beaks efficiently handle small seeds and large beaks handle large seeds, but medium beaks are poor at both. The bimodal distribution is the signature of disruptive selection — it is the opposite of stabilizing selection (which produces a unimodal distribution by eliminating extremes) and directional selection (which shifts the whole distribution toward one end)."

- question: "Why is disruptive selection alone often insufficient to produce complete sympatric speciation?"
  type: multiple-choice
  options:
    - "It reduces total genetic diversity, making speciation genetically impossible"
    - "It only occurs in allopatric populations, so cannot drive sympatric speciation by definition"
    - "Random mating continually produces intermediate offspring that are selected against, creating genetic load but preventing the two peaks from fully separating"
    - "Disruptive selection only operates on morphological traits, not on traits that control reproductive isolation"
  answer: 2
  explanation: "If large-peaked individuals mate randomly with small-peaked individuals, recombination in offspring continually regenerates intermediates that are selected against. This genetic load drags against divergence but does not eliminate intermediate genotypes entirely. For speciation to proceed, disruptive selection must be coupled with assortative mating (large with large, small with small), which reduces recombination between the morphs and allows the two peaks to diverge into reproductively isolated lineages."

- question: "Disruptive selection creates a bimodal phenotypic distribution by favoring both extremes while selecting against intermediate phenotypes."
  type: true-false
  answer: true
  explanation: "This is the defining feature of disruptive (diversifying) selection. Where stabilizing selection produces a sharp unimodal distribution by culling extremes, and directional selection shifts the distribution toward one end, disruptive selection pulls in opposite directions simultaneously — both high and low trait values have above-average fitness, while values near the population mean have below-average fitness. The African seed-cracker finch (*Pyrenestes ostrinus*) provides a real-world example."

- question: "Disruptive selection and directional selection are functionally similar because both ultimately favor one end of the phenotypic distribution over the other."
  type: true-false
  answer: false
  explanation: "This conflates two qualitatively different selection modes. Directional selection favors one extreme — the entire distribution shifts toward that end, and the mean changes in one direction. Disruptive selection favors *both* extremes simultaneously while eliminating the middle — the result is divergence, not directional shift. The ecological requirements also differ: directional selection needs one peak on the fitness landscape; disruptive selection requires two fitness peaks with a valley in between, as when resources come in discrete types with a gap in the middle."

- question: "Why does assortative mating amplify the evolutionary consequences of disruptive selection, and what outcome can this coupling potentially produce?"
  type: short-answer
  answer: "Assortative mating — large-phenotype individuals preferring large-phenotype mates — reduces gene flow between the two morphs. Without it, recombination from random mating continually regenerates disadvantaged intermediates. With it, the two phenotypic classes become genetically more isolated from each other over time, allowing their gene pools to diverge. If reproductive isolation becomes strong enough, the result is sympatric speciation: two distinct species arising from a single ancestral population without geographic separation."
  explanation: "The coupling of disruptive selection with assortative mating is one of the leading theoretical mechanisms for sympatric speciation and is theoretically important because it requires no geographic barrier — the ecological and genetic divergence happen within the same habitat. The rarity of disruptive selection in nature is largely a rarity of the ecological conditions that favor intermediates consistently worse than both extremes."
```

## Explainer

From your understanding of natural selection, you know that selection acts on heritable variation in fitness — individuals with traits better suited to their environment leave more offspring, shifting the population's trait distribution over time. You are likely familiar with **directional selection** (favoring one extreme) and **stabilizing selection** (favoring the average). **Disruptive selection** is the third mode: it favors *both* extremes at the expense of intermediates, pulling the population apart rather than pushing it in one direction or squeezing it toward the middle.

Picture a population of seed-eating birds on an island with two types of seeds: very small seeds and very large seeds, but few medium-sized ones. Birds with small beaks efficiently crack small seeds. Birds with large beaks efficiently crack large seeds. But birds with medium beaks are poor at both — too big for the small seeds, too weak for the large ones. In this environment, both extremes have higher fitness than the middle, and selection pushes the beak-size distribution toward a **bimodal shape** with peaks at small and large sizes and a valley in between. The African seed-cracker finch (*Pyrenestes ostrinus*) is a real example: populations show a bimodal distribution of bill sizes corresponding to specialization on hard versus soft seeds, with intermediates being rare.

The evolutionary consequences of disruptive selection depend on what happens to reproduction. If individuals at the two extremes mate randomly with each other, recombination continually produces intermediate offspring that are selected against — a genetic load that limits how far the two peaks can separate. But if **assortative mating** develops — large-beaked birds preferring to mate with other large-beaked birds, and small with small — then the two morphs become reproductively semi-isolated. This coupling of disruptive selection with assortative mating is one of the leading theoretical mechanisms for **sympatric speciation**, where new species arise within a single population without geographic barriers. The process also maintains **polymorphism** — the stable coexistence of multiple distinct phenotypes within a population, which you will encounter as a concept in its own right.

Disruptive selection is rarer and harder to detect than directional or stabilizing selection, because it requires a specific ecological setup where intermediates are disadvantaged. It is most often observed where resources come in discrete types, where different microhabitats within a population's range favor different phenotypes, or where competition is strongest among similar individuals (frequency-dependent selection can create disruptive dynamics). Despite being uncommon, disruptive selection is theoretically important because it provides a mechanism for populations to diversify and potentially split — generating the variation on which further evolution acts.
