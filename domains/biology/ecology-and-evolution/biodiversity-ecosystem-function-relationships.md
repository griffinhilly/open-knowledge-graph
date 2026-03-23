---
id: biodiversity-ecosystem-function-relationships
title: Biodiversity and Ecosystem Function Relationships
domain: biology
course: ecology-and-evolution
prerequisites:
- id: biodiversity-and-conservation
  type: hard
- id: ecosystem-structure-and-function
  type: soft
builds-toward:
- ecosystem-services
tags:
- biodiversity
- ecosystem-function
- productivity
- stability
stage: formal-systems
status: draft
---

# Biodiversity and Ecosystem Function Relationships

## Core Idea
Biodiversity affects ecosystem functions including productivity, nutrient cycling, stability, and disturbance resistance. Mechanisms include complementarity (different species use resources differently) and selection effects (communities differ in species composition). Relationships between diversity and function are often nonlinear: adding species increases function until redundancy appears. Whether biodiversity-function relationships represent strong ecosystem services depends on environmental context and mechanisms operating.

## Questions

```yaml
- question: "A grassland experiment compares monocultures to an 8-species mixture. The mixture produces more total biomass than the average monoculture — but also more than the single best-performing species grown alone. This result most directly supports:"
  type: multiple-choice
  options:
    - "The selection effect — the mixture contains the most productive species, which drives high yields"
    - "Complementarity — species use different resources so the community exploits the environment more completely than any single species could"
    - "Functional redundancy — many species contribute equally to productivity, diluting variance"
    - "The portfolio effect — diverse communities are more stable, and stability itself produces higher average yields"
  answer: 1
  explanation: "The selection effect predicts the mixture performs *as well as* the best monoculture (because it samples from a larger pool), not *better than* it. When the mixture outperforms even the best monoculture, this 'overyielding' is the signature of complementarity: species are occupying different resource niches (root depths, light levels, nutrient preferences) and the community collectively exploits more of the total resource pool than any single species alone can access."

- question: "A prairie ecosystem with 30 plant species experiences a severe drought. Several grass species decline sharply in cover. Compared to a 5-species pasture under the same drought, the most likely outcome in the diverse community is:"
  type: multiple-choice
  options:
    - "Greater collapse, because more species are present to be harmed by the drought"
    - "Identical decline, because drought affects all plants regardless of community composition"
    - "More stable total biomass, because drought-tolerant species compensate for declining drought-sensitive species"
    - "More rapid collapse, because competition among species is disrupted under stress"
  answer: 2
  explanation: "This is the portfolio effect: a diverse community contains species with different drought tolerances, phenologies, and root strategies. When drought-sensitive species decline, drought-tolerant ones compensate, maintaining total ecosystem function. A species-poor community or monoculture has no such insurance — if its dominant species is drought-sensitive, total productivity collapses. Biodiversity stabilizes ecosystem function precisely because different species respond differently to the same environmental perturbation."

- question: "The relationship between species richness and ecosystem productivity is linear — each species added to an ecosystem contributes equally to total function."
  type: true-false
  answer: false
  explanation: "The relationship is typically saturating, not linear. The first few species added to a barren system each make large contributions by filling distinct ecological roles. As more species accumulate, new additions increasingly overlap functionally with those already present, and each additional species contributes diminishing marginal function. This pattern of diminishing returns reflects functional redundancy — extra species provide insurance (stability over time) rather than immediate proportional productivity gains. The curve rises steeply, then levels off."

- question: "Diverse ecosystems tend to be more resistant to invasion by non-native species than species-poor ecosystems."
  type: true-false
  answer: true
  explanation: "One mechanism for invasion resistance in diverse communities is more complete resource use: complementarity among resident species means available light, water, and nutrients are more thoroughly exploited, leaving fewer unfilled ecological niches for invaders to colonize. Species-poor systems and monocultures leave more unused resources, creating openings for invaders. This is one of the practical ecosystem services of biodiversity with direct implications for restoration ecology and sustainable agriculture."

- question: "What is the 'portfolio effect,' and how does it explain why biodiversity promotes ecosystem stability over time?"
  type: short-answer
  answer: "The portfolio effect is the ecological analog of financial diversification: just as a diversified investment portfolio is less volatile than any single stock (because different assets respond differently to market conditions), a diverse community is more stable than a monoculture because different species respond differently to environmental perturbations. When drought, disease, or temperature extremes reduce some species, others with different tolerances compensate, and total ecosystem function remains relatively stable. A monoculture's fate is tied entirely to one species under all conditions — there is no compensatory mechanism."
  explanation: "The analogy to financial portfolios is mathematically precise: the variance of a sum of imperfectly correlated variables is less than the sum of their individual variances. Because species do not all respond identically to environmental variation, total community biomass or productivity fluctuates less than any individual species' abundance — provided sufficient diversity is maintained."
```

## Explainer

From your study of biodiversity and conservation, you understand that species richness varies across ecosystems and is under threat from human activities. But a deeper question arises: does biodiversity actually *matter* for how ecosystems work? The field of **biodiversity-ecosystem function (BEF) research** addresses this directly, and the answer, supported by hundreds of experiments over the past three decades, is a clear yes — but the mechanisms and magnitude are more nuanced than a simple "more species equals better."

The two primary mechanisms linking diversity to ecosystem function are **complementarity** and the **selection effect** (sometimes called the sampling effect). Complementarity occurs when different species use resources in different ways — different root depths, different light requirements, different nutrient preferences — so that a diverse community exploits the total resource pool more completely than any single species could alone. Imagine a grassland with ten plant species: some have deep roots accessing groundwater, others have shallow roots capturing rainfall, some fix nitrogen, others are efficient phosphorus scavengers. Together, they capture more total resources and produce more biomass than a monoculture of any one species. The selection effect, by contrast, is a statistical phenomenon: a more diverse community is more likely to contain a particularly productive or dominant species simply because you are sampling from a larger pool. Both mechanisms operate simultaneously in most natural systems.

The relationship between diversity and function is typically **saturating** — a curve that rises steeply at first as species are added, then levels off. The first few species added to a barren system each make a large contribution because they fill distinct roles. But as more species accumulate, new additions increasingly overlap with species already present, and each additional species contributes less marginal function. This pattern of diminishing returns has led some to argue that ecosystems contain **functional redundancy** — that many species are "insurance" that only become important when conditions change. And that insurance function is real: diverse communities tend to be more **stable** over time because when one species declines due to drought or disease, others compensate. This is the **portfolio effect**, analogous to how diversifying financial investments reduces risk.

Whether these BEF relationships translate into strong arguments for conservation depends on context. In controlled experiments using simplified grassland plots, the diversity-productivity relationship is robust and reproducible. In complex natural ecosystems with hundreds of species, environmental variation, and historical contingency, the signal is harder to isolate — but meta-analyses consistently show that biodiversity loss reduces ecosystem productivity, nutrient retention, and resistance to invasion. The practical implication is that biodiversity is not merely an aesthetic or ethical concern; it is a functional component of ecosystems that underpins the services — clean water, carbon storage, pollination, disease regulation — on which human societies depend.
