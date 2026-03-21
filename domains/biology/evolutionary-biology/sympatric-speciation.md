---
id: sympatric-speciation
title: Sympatric Speciation
domain: biology
course: evolutionary-biology
prerequisites:
- id: speciation
  type: hard
- id: disruptive-selection
  type: soft
tags:
- speciation
- reproductive-isolation
- sympatry
stage: advanced
status: draft
---

# Sympatric Speciation

## Core Idea
Sympatric speciation involves reproductive isolation evolving without geographic barriers, requiring strong disruptive selection and assortative mating. Polyploidy causes instant reproductive isolation in plants. Cichlid fish in lakes provide compelling examples of sympatric diversification through sexual selection and ecological specialization.

## Questions

```yaml
- question: "Why does sympatric speciation typically require both disruptive selection AND assortative mating, rather than either mechanism alone?"
  type: multiple-choice
  options:
    - "Disruptive selection alone creates two species if given enough generations — assortative mating only speeds the process"
    - "Assortative mating alone produces reproductive isolation without any need for selection on phenotype"
    - "Disruptive selection creates fitness differences between extreme phenotypes; assortative mating prevents gene flow from blending them back — both are required to maintain divergence"
    - "Neither mechanism contributes to reproductive isolation; geographic barriers remain necessary for any speciation event"
  answer: 2
  explanation: "Gene flow is the key obstacle in sympatric speciation. Disruptive selection alone creates extreme phenotypes but does not prevent them from mating with intermediate individuals, so offspring revert toward the mean each generation. Assortative mating alone creates non-random mating patterns but without selection, there is no fitness difference driving divergence. Together, disruptive selection creates and maintains extreme phenotypes while assortative mating restricts interbreeding between those phenotypes — the two mechanisms reinforce each other to overcome gene flow's homogenizing effect."

- question: "A tetraploid plant (4n) arises spontaneously from a diploid (2n) ancestor. A student argues it is not yet a new species because 'one mutation cannot speciate a population.' Which response best addresses this?"
  type: multiple-choice
  options:
    - "The student is correct — reproductive isolation requires many generations of divergence, not a single chromosomal change"
    - "The student is incorrect — crosses between the tetraploid and diploid produce triploid offspring that are typically sterile, so reproductive isolation is immediate and complete"
    - "The student is correct — species status also requires geographic separation from the ancestor"
    - "The student is incorrect — the tetraploid is already a different species simply because it occupies a different ecological niche"
  answer: 1
  explanation: "Polyploidy creates instant reproductive isolation: the tetraploid (4n) crossed with the diploid (2n) produces triploid (3n) offspring. Triploids cannot undergo normal meiosis because chromosomes lack matching partners for synapsis, so they are typically sterile — just like mules from horse-donkey crosses. A single whole-genome duplication event therefore creates a new reproductively isolated lineage in one generation, making polyploidy the fastest known speciation mechanism. It accounts for 30-80% of flowering plant species diversity."

- question: "Polyploidy is considered the fastest known speciation mechanism because it can produce complete reproductive isolation in a single generation."
  type: true-false
  answer: true
  explanation: "A new polyploid individual is immediately reproductively isolated from its diploid ancestors. Crosses between tetraploid (4n) and diploid (2n) parents produce sterile triploid (3n) offspring, just as crosses between horse and donkey produce the sterile mule. No gradual accumulation of differences over generations is required — the chromosomal change itself constitutes a reproductive barrier. This contrasts sharply with allopatric speciation, which typically requires thousands to millions of years of geographic isolation."

- question: "In sympatric speciation, gene flow between diverging groups is irrelevant because they occupy the same habitat and will naturally accumulate genetic differences through random mutation over time."
  type: true-false
  answer: false
  explanation: "Gene flow is precisely what makes sympatric speciation difficult and rare compared to allopatric speciation. When individuals share the same habitat, they can freely interbreed, and random mutations that arise in one subgroup are quickly diluted and lost through mating with the broader population. Without some force (disruptive selection + assortative mating) that restricts interbreeding between diverging subgroups, gene flow continuously blends genetic differences back together. Mutation alone, at typical rates, cannot outpace gene flow's homogenizing effect."

- question: "Why is sympatric speciation considered harder to explain than allopatric speciation, and what is the key condition that makes it possible?"
  type: short-answer
  answer: "In allopatric speciation, a geographic barrier physically prevents gene flow, so populations can diverge freely through selection, drift, and mutation. In sympatric speciation, all individuals occupy the same habitat and can interbreed, meaning gene flow continuously blends away any divergence. The key condition making sympatric speciation possible is strong disruptive selection (favoring individuals at phenotypic extremes over the middle) combined with assortative mating (individuals preferentially mating with phenotypically similar partners). Together these forces create and maintain divergence that overrides gene flow. Polyploidy bypasses this problem entirely by creating instant chromosomal incompatibility."
  explanation: "The cichlid example illustrates the difficulty: Lake Victoria is small and lacks the geographic barriers that would enable easy allopatric speciation, yet over 500 species evolved from a common ancestor in ~15,000 years. Sexual selection on male coloration provided the assortative mating component; ecological specialization on different food sources provided the disruptive selection. The speed and scale of this radiation is extraordinary precisely because the underlying conditions were unusually strong."
```

## Explainer

From your study of speciation, you know that new species arise when populations become reproductively isolated and diverge genetically. The most intuitive mechanism is allopatric speciation, where a geographic barrier — a mountain range, a river, an ocean — physically separates populations and prevents gene flow. **Sympatric speciation** asks a harder question: can a single population, living in the same place with no physical barriers, split into two reproductively isolated species? The answer is yes, but the conditions are demanding.

The fundamental problem is **gene flow**. When individuals in a population can freely interbreed, any genetic divergence between subgroups gets blended away each generation. For sympatric speciation to work, something must counteract this homogenizing force. The two main mechanisms are **disruptive selection** and **assortative mating**, and they typically must act together. Disruptive selection favors individuals at the extremes of a trait distribution over those in the middle — for example, birds with very large or very small beaks might feed more efficiently on different seed sizes than birds with medium beaks. If individuals also preferentially mate with others who share their extreme phenotype (assortative mating), the population can begin to split into two non-interbreeding groups even without any geographic separation.

The clearest and most dramatic mechanism of sympatric speciation is **polyploidy** in plants — a whole-genome duplication that creates an individual with twice the normal chromosome number. A tetraploid plant (4n) is immediately reproductively isolated from its diploid (2n) ancestors because crosses between them produce triploid (3n) offspring that are usually sterile, just as a mule (horse × donkey cross) is sterile due to mismatched chromosome numbers. Polyploidy can generate a new species in a single generation, making it the fastest known speciation mechanism. It is remarkably common in plants: estimates suggest that 30-80% of flowering plant species have polyploid origins.

The cichlid fishes of the African Great Lakes provide the most celebrated animal examples. In Lake Victoria alone, over 500 species evolved from a common ancestor in perhaps 15,000 years — far too many species in too small and uniform a lake for geographic isolation to explain. Instead, **sexual selection** on male coloration combined with **ecological specialization** on different food sources appears to have driven divergence. Females prefer males of particular colors, creating assortative mating, while competition for resources drives ecological divergence. The lesson of sympatric speciation is that reproductive isolation does not require mountains or oceans — it requires that selection and mating preferences be strong enough to overcome the blending power of gene flow within a shared habitat.
