---
id: disturbance-ecology-and-succession-dynamics
title: Disturbance Ecology and Succession Dynamics
domain: biology
course: ecology-and-evolution
prerequisites:
- id: community-succession-primary-secondary
  type: hard
- id: ecological-succession
  type: soft
builds-toward:
- ecosystem-stability-resilience-and-tipping-points
tags:
- disturbance
- succession
- community
- dynamics
stage: advanced
status: draft
---

# Disturbance Ecology and Succession Dynamics

## Core Idea
Disturbances (fire, floods, storms, logging) reset community composition and initiate succession. The intermediate disturbance hypothesis suggests maximum diversity at intermediate frequencies—too little and competitors exclude others; too much and only colonizers persist. Succession patterns depend on disturbance intensity, frequency, and extent, and on environment and species traits. Understanding disturbance is critical for predicting responses to human activities and climate change.

## Questions

```yaml
- question: "Fire has been actively suppressed for 70 years in a fire-adapted ponderosa pine forest. Which outcome is most ecologically likely?"
  type: multiple-choice
  options:
    - "The forest reaches a stable climax state with maximum species diversity because disturbance is eliminated"
    - "Fire-adapted species gradually expand their range as competition from fire-intolerant species is reduced"
    - "Fuel accumulates and shade-tolerant species replace fire-adapted species, paradoxically increasing the risk and severity of future fires"
    - "The forest becomes more resilient because species have more time to establish deep root systems without disturbance"
  answer: 2
  explanation: "Fire suppression in fire-adapted ecosystems does not eliminate fire — it delays it while radically changing what burns. Without regular low-intensity burns, leaf litter, dead wood, and shrubs accumulate over decades, creating heavy fuel loads. Meanwhile, shade-tolerant species (which would normally be killed by fire) establish themselves in the understory, replacing fire-adapted species. When fire finally occurs, it burns hotter and more extensively than it would have under a natural fire regime, often killing trees that would have survived low-intensity burns. This is a classic example of how removing a disturbance can create conditions that make future disturbances far more destructive."

- question: "According to the intermediate disturbance hypothesis, which scenario would produce the LOWEST species diversity in a community?"
  type: multiple-choice
  options:
    - "A coral reef experiencing storms every 3-5 years"
    - "A grassland with a fire regime of every 15-20 years"
    - "An intertidal zone that experiences wave disturbance every few days"
    - "A forest with virtually no natural disturbance for centuries"
  answer: 2
  explanation: "The IDH predicts low diversity at both extremes: very high disturbance frequency (only fast-colonizing pioneers can persist) AND very low disturbance frequency (competitive dominants exclude most species as succession proceeds to late stages). A coral reef disturbed every few years sits at an intermediate frequency that typically supports high diversity. A grassland burning every 15-20 years may also be intermediate. An intertidal zone disturbed every few days is very high frequency — only disturbance-tolerant specialists persist. A forest with virtually no disturbance allows a few competitive dominant trees to monopolize light and resources, suppressing most other species — this is the low-frequency extreme that produces low diversity."

- question: "Reducing disturbance frequency in any ecosystem will always increase species diversity by allowing more species to establish and persist."
  type: true-false
  answer: false
  explanation: "This is the intuition that the intermediate disturbance hypothesis directly contradicts. Reducing disturbance frequency from a very high level can increase diversity by allowing more species to persist. But reducing disturbance from an already-intermediate level can *decrease* diversity by allowing competitive dominants to monopolize resources and exclude weaker competitors as succession advances. In fire-adapted grasslands, reducing fire frequency allows woody shrubs and trees to outcompete the diverse prairie species, collapsing diversity. The relationship between disturbance and diversity is hump-shaped, not linear: diversity peaks at intermediate disturbance, not at minimum disturbance."

- question: "Many species in fire-adapted ecosystems have traits — such as thick bark, serotinous cones, and rapid resprouting — that evolved in response to regular fire, not despite it."
  type: true-false
  answer: true
  explanation: "This is a central insight of disturbance ecology: disturbance regimes are not merely something species must survive but are selective forces that shape species' traits over evolutionary time. Longleaf pines have bark several inches thick that insulates their cambium from low-intensity fires. Some Australian Banksia species have serotinous cones that require fire's heat to open and release seeds. Prairie grasses evolved extensive underground root and rhizome systems that allow rapid resprouting after burning. These traits reveal that for these species, fire is part of their adaptive environment — they are not merely tolerating disturbance but are evolutionarily dependent on it."

- question: "Why does the intermediate disturbance hypothesis predict lower species diversity at both very low AND very high disturbance frequencies?"
  type: short-answer
  answer: "At very low disturbance frequencies, succession proceeds to late stages where a few highly competitive dominant species monopolize resources (especially light and space) and outcompete most others — competitive exclusion reduces diversity. At very high disturbance frequencies, the community is constantly reset to early successional stages, and only fast-colonizing, disturbance-tolerant pioneer species can complete their life cycles and persist — all late-successional species are excluded. At intermediate frequencies, a landscape mosaic develops: some patches are recently disturbed with pioneer species, others are in mid-succession, others are approaching late stages. This spatial and temporal heterogeneity allows both early- and late-successional species to coexist regionally, maximizing total diversity."
  explanation: "The IDH is a spatial and temporal argument as much as a successional one. The key mechanism is heterogeneity: intermediate disturbance creates a patchwork of successional ages across the landscape, expanding the diversity of microhabitats that different species can exploit. The two low-diversity extremes are caused by opposite forms of competitive exclusion — dominants in the low-frequency case, pioneers in the high-frequency case."
```

## Explainer

From your study of ecological succession, you understand that communities change over time in a somewhat predictable sequence — pioneer species colonize bare ground, modify conditions, and are gradually replaced by later-arriving species until a relatively stable community develops. **Disturbance ecology** deepens this picture by recognizing that disturbances are not merely destructive interruptions of succession but are integral, recurring features of most ecosystems that actively maintain diversity and shape community structure.

A **disturbance** is any event that disrupts community structure by destroying biomass or altering resource availability — fire, windstorms, floods, volcanic eruptions, tree falls, grazing, or human land clearing. What matters ecologically is not just whether a disturbance occurs, but its **regime**: the characteristic frequency, intensity, spatial extent, and seasonality of disturbances in a given ecosystem. A grassland that burns every 3–5 years has a fundamentally different community than one that burns every 50 years, even if the soil and climate are identical. Many species are adapted to specific disturbance regimes — longleaf pines have thick, fire-resistant bark; some Australian plants require fire to release their seeds; prairie grasses resprout rapidly from underground rhizomes after burning.

The **intermediate disturbance hypothesis (IDH)**, proposed by Joseph Connell, offers an intuitive framework for understanding how disturbance frequency affects diversity. At very low disturbance frequencies, succession proceeds to late stages where a few competitive dominant species monopolize resources and exclude weaker competitors — diversity is low. At very high disturbance frequencies, only fast-colonizing, disturbance-tolerant species can persist — diversity is also low. At intermediate frequencies, a mosaic of successional stages coexists across the landscape: some patches recently disturbed and dominated by pioneers, others in mid-succession with a mix of species, and others approaching late-successional dominance. This spatial and temporal heterogeneity allows both early- and late-successional species to persist regionally, maximizing diversity. While the IDH is an idealization — real ecosystems show more complex patterns — it captures a genuine and widely observed phenomenon.

The interaction between disturbance and succession has profound practical implications. Fire suppression in fire-adapted ecosystems (like western North American forests) allows fuel to accumulate and shade-tolerant species to replace fire-adapted ones, paradoxically increasing the severity of fires when they eventually occur. Climate change is altering disturbance regimes worldwide — more intense hurricanes, longer fire seasons, shifting flood patterns — and communities adapted to historical regimes may not persist under novel ones. Effective conservation and land management therefore require understanding not just which species are present, but what disturbance regime maintains them.
