---
id: community-stability-resistance-resilience
title: 'Community Stability: Resistance and Resilience'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: community-ecology-intro
  type: hard
- id: ecological-succession
  type: soft
builds-toward:
- restoration-ecology-principles
- climate-change-ecology
tags:
- stability
- resistance
- resilience
- disturbance
stage: formal-systems
status: validated
---

# Community Stability: Resistance and Resilience

## Core Idea
Resistance is a community's ability to withstand disturbance without changing composition. Resilience is its ability to recover after disturbance. Diversity often increases both properties, though the relationship is complex. Stability trades off with productivity—highly productive systems are often less resistant to disturbance.

## Questions

```yaml
- question: "An old-growth temperate forest has remained essentially unchanged in species composition for centuries. After clear-cutting, the site has not recovered its original composition after 200 years. What does this pattern reveal about the forest's stability properties?"
  type: multiple-choice
  options:
    - "The forest has high resistance and high resilience — centuries of stability followed by eventual recovery"
    - "The forest has low resistance and low resilience — it failed to resist disturbance and cannot recover"
    - "The forest has high resistance but low resilience — it withstood minor disturbances for centuries but recovers very slowly after major clearing"
    - "The forest has low resistance but high resilience — its slow recovery proves it resists disturbance more than it recovers"
  answer: 2
  explanation: "Resistance is the ability to remain unchanged *during* disturbance; resilience is the ability to *recover after* disturbance. The centuries of compositional stability under natural stressors demonstrate high resistance. But the 200+ year recovery timeline after clear-cutting reveals extremely low resilience. This combination — high resistance, low resilience — is a key insight: the two properties are distinct and can trade off. It also has conservation implications: once a highly resistant ecosystem is overcome, restoration may take generations."

- question: "A diverse grassland maintains relatively stable biomass production across several drought years, while an adjacent species-poor grassland crashes. According to the insurance hypothesis, what mechanism explains the diverse grassland's stability?"
  type: multiple-choice
  options:
    - "More species means more total photosynthetic capacity, which offsets drought losses through sheer abundance"
    - "Diverse communities have more predators, which prevent herbivore outbreaks that would amplify drought stress"
    - "Functional redundancy allows drought-tolerant species to compensate when drought-sensitive species decline, maintaining overall community function"
    - "Species-rich communities have deeper root networks on average, giving them better access to groundwater during drought"
  answer: 2
  explanation: "The insurance hypothesis holds that diversity buffers against environmental variability because different species respond differently to the same stressor. When drought causes drought-sensitive species to decline, drought-tolerant species with similar ecological roles expand and maintain overall ecosystem function. This functional redundancy — multiple species performing similar roles — is the mechanism, not raw abundance (A), predator effects (B), or average root depth (D). The analogy is insurance: you don't benefit most of the time, but when something goes wrong, backup capacity prevents collapse."

- question: "A community can have high resistance to disturbance but low resilience after disturbance — these two properties are independent enough to trade off within the same ecosystem."
  type: true-false
  answer: true
  explanation: "Resistance and resilience are distinct properties that measure different aspects of stability. Old-growth forests exemplify high resistance (centuries of compositional stability under chronic stress) combined with low resilience (extremely slow recovery if major disturbance eliminates the community). Grasslands often show the opposite: easily disturbed by fire but recovering within a few years. This independence is ecologically important because you cannot infer resilience from resistance or vice versa — conservation strategies must assess each property separately."

- question: "Highly productive ecosystems are generally more stable than less productive ones because greater biomass provides a larger buffer against disturbance losses."
  type: true-false
  answer: false
  explanation: "High productivity does not confer stability and can actually reduce it. A monoculture cornfield is among the most productive agricultural ecosystems but is catastrophically vulnerable to a single pathogen or weather event because it lacks the functional redundancy and diversity that buffer diverse communities. Highly productive systems are often species-poor and optimized for performance in one condition, not robustness across varied conditions. The diversity-stability relationship — not the productivity-stability relationship — is the reliable empirical pattern."

- question: "Explain the difference between resistance and resilience, and describe why understanding both properties matters for conservation decisions."
  type: short-answer
  answer: "Resistance is a community's ability to remain unchanged during a disturbance — to absorb stress without shifting in composition or function. Resilience is its ability to return to its original state after disturbance has altered it. They matter independently for conservation because they suggest different management strategies: a highly resistant ecosystem rewards protection (prevent disturbance from reaching the threshold that overcomes resistance), while a highly resilient ecosystem is more forgiving and rewards restoration investment. An ecosystem with low resistance and low resilience needs both urgent protection of intact areas and pessimistic forecasts for restoration."
  explanation: "The two properties can trade off (old-growth forests: high resistance, low resilience; grasslands: low resistance, high resilience), so 'is this ecosystem stable?' is an incomplete question. Conservation ecologists must ask: stable in which sense, and against what disturbances? This framing also helps predict responses to climate change — a resistant ecosystem may persist for decades under gradually intensifying stress, then collapse suddenly with little capacity to recover, demanding intervention before the threshold is reached."
```

## Explainer

From your study of community ecology and ecological succession, you know that communities are not static — they change in response to disturbance and over time. But some communities absorb shocks while others collapse. The concepts of **resistance** and **resilience** provide a framework for understanding these differences. Resistance is the ability to remain essentially unchanged during a disturbance — a resistant forest barely shifts in species composition during a drought. Resilience is the ability to bounce back afterward — a resilient grassland recovers its original species mix within a few years of a fire. A community can be high in one property and low in the other: old-growth forests are often highly resistant (stable for centuries) but poorly resilient (if cleared, they take hundreds of years to recover), while grasslands may be easily disturbed but snap back rapidly.

The relationship between **diversity and stability** has been debated since the 1950s, but a large body of experimental evidence — particularly David Tilman's long-term grassland experiments at Cedar Creek — shows that more diverse communities tend to be both more resistant and more resilient. The mechanism is often called the **insurance hypothesis**: in a species-rich community, if one species declines during a drought, other species with different drought tolerances can compensate, maintaining overall community function. In a species-poor community, losing one of only a few species can cause the whole system to crash. Functional redundancy — multiple species performing similar ecological roles — provides a buffer against environmental variability.

However, the diversity-stability relationship is not a simple rule. **Highly productive systems** can be surprisingly fragile. A monoculture cornfield is enormously productive but collapses entirely under the wrong pest or weather event. Conversely, species-poor but highly adapted communities — like desert scrublands — can be remarkably resistant to the specific stresses they evolved under, yet devastatingly slow to recover from novel disturbances like grazing or development. The type of disturbance matters too: a community resistant to fire may not be resistant to flooding.

These concepts have direct conservation and management implications. When ecologists assess a threatened ecosystem, they ask not just "how many species are here?" but "how will this community respond to climate change, invasive species, or land-use change?" A community with high resistance buys time — it persists under pressure, giving managers a window to intervene. A community with high resilience is more forgiving — it can recover from management mistakes. Understanding which property a given ecosystem possesses, and why, guides decisions about where to invest limited conservation resources and whether to prioritize protection (leveraging resistance) or restoration (leveraging resilience).
