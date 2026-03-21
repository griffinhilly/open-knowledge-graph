---
id: natural-selection-types-and-examples
title: 'Natural Selection: Types and Contemporary Examples'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: natural-selection
  type: hard
- id: adaptation-and-fitness
  type: soft
- id: heritability-broad-sense-narrow-sense
  type: soft
builds-toward:
- genetic-drift-in-small-populations
- population-genetic-structure-metapopulations
- speciation
tags:
- natural-selection
- directional
- stabilizing
- disruptive
stage: advanced
status: draft
---

# Natural Selection: Types and Contemporary Examples

## Core Idea
Natural selection acts on heritable variation through differential survival and reproduction. Directional selection favors one extreme (larger body size), stabilizing selection removes extremes (maintaining intermediates), and disruptive selection favors extremes (polymorphism). Examples include industrial melanism, antibiotic resistance, and artificial selection in breeding.

## Questions

```yaml
- question: "Human birth weight data show that very small babies have high infant mortality from underdevelopment, and very large babies have high mortality from delivery complications. Intermediate-weight babies have the highest survival. This is a classic example of which type of selection?"
  type: multiple-choice
  options:
    - "Directional selection — survival is highest at one end of the distribution"
    - "Stabilizing selection — selection against both extremes maintains an intermediate optimum"
    - "Disruptive selection — two distinct weight classes are favored over intermediates"
    - "Sexual selection — reproductive success is determined by mate choice rather than survival"
  answer: 1
  explanation: "Stabilizing selection is defined by highest fitness at intermediate trait values with selection against both extremes. The birth weight example fits perfectly: too small (underdevelopment) and too large (delivery complications) are both disadvantaged, while intermediate weights are selectively favored. The population mean doesn't shift, but variance is reduced as the tails of the distribution are culled. This is the most common form of selection in nature — it explains why many traits remain stable for long periods rather than continuously shifting."

- question: "In a bird population, seeds come in only two sizes: very small and very large. Small-beaked birds efficiently crack small seeds, large-beaked birds crack large seeds, but intermediate-beaked birds struggle with both. Over generations, what do you predict will happen to beak size distribution in this population?"
  type: multiple-choice
  options:
    - "The mean beak size will shift toward larger beaks, driven by directional selection"
    - "Beak size variance will decrease as stabilizing selection maintains an intermediate optimum"
    - "Beak size distribution will become bimodal, with both small and large beaks increasing in frequency"
    - "Beak size will not change because the population is already adapted to the food environment"
  answer: 2
  explanation: "This describes disruptive selection: fitness is highest at both extremes and lowest at intermediate trait values. When food availability rewards specialization over generalism, both extreme morphs are favored over intermediates. Over generations, the frequency of intermediate-beaked birds decreases while both small-beaked and large-beaked morphs increase — producing a bimodal distribution. This is the signature outcome of disruptive selection, and it can eventually (especially combined with assortative mating) lead to population divergence and speciation."

- question: "Stabilizing selection shifts the mean of a trait toward a new optimum while reducing phenotypic variance."
  type: true-false
  answer: false
  explanation: "This confuses stabilizing and directional selection. Stabilizing selection maintains the existing mean by removing individuals at both extremes — it reduces variance without shifting the mean. Directional selection is what shifts the mean, by consistently favoring one extreme. Under stabilizing selection, the population 'stays put' at a well-adapted intermediate value. A common implication is that when we observe stable trait means over many generations, stabilizing selection may be the explanation — the trait is already at its fitness optimum."

- question: "A population could simultaneously experience directional selection on one trait (e.g., immune gene variants under pathogen pressure) and stabilizing selection on another trait (e.g., body size near an optimal thermal range) at the same time."
  type: true-false
  answer: true
  explanation: "Selection acts independently on different traits, so multiple selection regimes can operate simultaneously in the same population. Each trait has its own fitness landscape, and the shape of selection on each is determined by the ecological pressures relevant to that trait. Industrial melanism affected wing coloration but not body size; antibiotic resistance affects specific biochemical targets but not pigmentation. Understanding that selection operates trait-by-trait is essential for predicting evolutionary responses to complex, multi-dimensional environments."

- question: "How does disruptive selection differ from directional selection in both mechanism and potential long-term evolutionary consequence?"
  type: short-answer
  answer: "Directional selection favors one extreme of the trait distribution, shifting the population mean toward that extreme over time. Disruptive selection favors both extremes simultaneously while eliminating intermediates, increasing trait variance and potentially creating a bimodal distribution. The long-term consequences differ critically: directional selection produces adaptation toward a new optimum but maintains a unimodal population; disruptive selection can increase polymorphism and, if combined with assortative mating (individuals preferentially mating with similar morphs), can lead to reproductive isolation and ultimately sympatric speciation. Disruptive selection is therefore one of the mechanisms by which a single population can diverge into two distinct lineages without geographic separation."
  explanation: "The African seedcracker finch is a well-documented case: large-billed and small-billed morphs coexist while intermediate birds have significantly lower survival. This illustrates how disruptive selection maintains a polymorphism in a real population. The potential for speciation is what makes disruptive selection evolutionarily consequential despite being the rarest of the three modes."
```

## Explainer

You already understand the core logic of natural selection: individuals vary, some variants survive and reproduce better, and if those variants are heritable, the population changes over generations. What this topic adds is the recognition that selection does not always push a trait in one direction. The *shape* of selection — how fitness relates to the trait distribution — determines whether a population shifts its mean, narrows its spread, or splits into distinct forms.

**Directional selection** is the most intuitive type: one extreme of a trait distribution has higher fitness, so the population mean shifts toward that extreme over generations. The classic example is industrial melanism in peppered moths. Before industrial pollution darkened tree bark in 19th-century England, light-colored moths were camouflaged against lichen-covered trees, and dark moths were conspicuous to predators. As soot blackened the trees, dark moths gained a survival advantage, and the population shifted from predominantly light to predominantly dark within decades. Antibiotic resistance in bacteria follows the same logic: in the presence of an antibiotic, resistant bacteria survive and sensitive ones die, directionally shifting the population toward resistance. The key signature of directional selection is a change in the trait mean with relatively little change in trait variance.

**Stabilizing selection** is the most common form in nature, though the least dramatic to observe. Here, individuals with intermediate trait values have the highest fitness, and both extremes are disfavored. Human birth weight is a textbook example: babies that are too small face survival challenges, while babies that are too large face delivery complications. The result is strong selection maintaining an intermediate optimum. Stabilizing selection reduces phenotypic variance without shifting the mean — it narrows the bell curve. From your understanding of heritability, you can see why this creates an apparent paradox: if selection keeps removing variation, why does heritable variation persist? The answer involves mutation-selection balance and the contributions of many loci, each with small effects.

**Disruptive selection** is the rarest and most evolutionarily consequential type. Here, both extremes have higher fitness than intermediates, favoring a bimodal trait distribution. Consider a bird population feeding on seeds: if seeds come in two sizes (large and small), birds with beaks specialized for either size do better than birds with intermediate beaks suited to neither. Over time, disruptive selection can increase phenotypic variance and, if combined with assortative mating, lead to population divergence and potentially speciation. African seedcracker finches, where large-billed and small-billed morphs coexist while intermediate-billed birds have lower survival, provide a well-documented natural example.

These three modes are not mutually exclusive or permanent. A population may experience stabilizing selection on birth weight, directional selection on immune gene frequencies in response to a new pathogen, and disruptive selection on beak morphology — all simultaneously on different traits. The mode can also shift over time: an environmental change can convert long-standing stabilizing selection into directional selection, as when climate warming favors earlier breeding dates in migratory birds. Recognizing which type of selection is operating, and on which traits, is the foundation for understanding how populations respond to environmental change and how genetic drift in small populations can override even strong selection.
