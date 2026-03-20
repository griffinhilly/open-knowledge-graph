---
id: ecological-succession
title: Ecological Succession
domain: biology
course: ecology-and-evolution
prerequisites:
- id: community-ecology-intro
  type: hard
- id: species-interactions
  type: soft
builds-toward:
- keystone-species
- biodiversity-metrics
tags:
- succession
- pioneer-species
- climax-community
- disturbance
stage: advanced
status: validated
---

# Ecological Succession

## Core Idea
Ecological succession is the directional, predictable change in community composition over time following a disturbance or the colonization of a new substrate. Primary succession begins on bare substrate (e.g., after glacial retreat or volcanic eruption), starting with pioneer species that modify the abiotic environment. Secondary succession occurs where soil and seeds remain after disturbance (e.g., after fire or agricultural abandonment). The intermediate disturbance hypothesis predicts that moderate disturbance frequency maximizes species diversity by preventing competitive exclusion.

## How It's Best Learned
Follow a successional chronosequence — compare sites of different ages after a known disturbance and track community composition changes. Distinguish facilitation, tolerance, and inhibition models of succession. Study Glacier Bay (primary) and old-field succession (secondary) as classical cases.

## Common Misconceptions
- Succession does not always lead to a single, predictable 'climax community' — alternative stable states and ongoing disturbance prevent a fixed endpoint.
- Pioneer species do not 'plan' to be replaced; they simply modify conditions that eventually favor competitors.

## Questions

```yaml
- question: "After a volcanic eruption covers land with bare lava, lichens and mosses begin to colonize the rock. Which type of succession is this, and why?"
  type: multiple-choice
  options:
    - "Secondary succession, because the eruption was a disturbance to a previously occupied landscape"
    - "Primary succession, because colonization begins on bare substrate with no soil or seed bank"
    - "Inhibition succession, because the eruption creates conditions hostile to most species"
    - "Climax succession, because lichens are highly specialized for this environment"
  answer: 1
  explanation: "The defining criterion for primary vs. secondary succession is not whether a disturbance occurred but whether soil and biological legacies (seed bank, organic matter) remain afterward. Fresh lava has neither — organisms are starting from scratch on bare rock. A common error is classifying any post-disturbance sequence as secondary succession; secondary requires that soil and seeds survived the disturbance (as after a fire or field abandonment)."

- question: "Every ecosystem, if left undisturbed long enough, will converge on a single predictable climax community determined entirely by regional climate."
  type: true-false
  answer: false
  explanation: "The classical Clementsian climax community concept has been largely revised. Modern ecology recognizes that alternative stable states can persist indefinitely — different communities can occupy identical climates depending on historical contingency (which species arrived first), legacy effects, and ongoing disturbance regimes. Two identical forest patches can follow different successional trajectories and settle into genuinely different community types. Climate sets broad constraints but does not fully determine a unique endpoint."

- question: "The intermediate disturbance hypothesis predicts that species diversity peaks at moderate disturbance frequency. Explain why diversity declines at both very low and very high disturbance levels."
  type: short-answer
  answer: "At very low disturbance, competitive exclusion proceeds unchecked — dominant species outcompete and eliminate subordinate ones over time. At very high disturbance, most species cannot establish or reproduce between disturbance events, leaving only disturbance-tolerant specialists. Moderate disturbance interrupts competitive exclusion often enough to allow coexistence of many species, while still permitting enough recovery time for non-specialists to persist."
  explanation: "This tests mechanistic understanding rather than pattern recall. The key insight is that disturbance acts differently at each extreme: too little favors competitive dominants; too much favors only stress-tolerant specialists. The middle range creates a diversity-promoting balance between these opposing pressures."
```

## Explainer

From community ecology, you know that species don't just coexist — they compete, facilitate each other, and shift in relative abundance over time. Ecological succession is what happens when you zoom out and watch that process unfold over years, decades, or centuries following a disturbance or the creation of new habitat. It is the directional, somewhat predictable turnover of species assemblages through time.

The most important first distinction is between primary and secondary succession. **Primary succession** starts on bare substrate where no life previously existed and no soil is present — think of the rock left behind as a glacier retreats, or the fresh lava field after an eruption. There is nothing to start with except rock and atmosphere. Pioneer species — typically hardy lichens, mosses, and nitrogen-fixing bacteria — are the first colonizers. They can tolerate the harsh abiotic conditions (extreme temperature swings, no water retention, no nutrients) and, crucially, they begin to modify those conditions: lichens chemically weather rock, organic matter accumulates, soil begins to form. This is facilitation — early species make the environment more hospitable for later arrivals. **Secondary succession** is faster because soil and a seed bank already exist after the disturbance; a burned forest or abandoned agricultural field is not starting from zero.

It is important to understand that pioneer species are not "trying" to be replaced — they simply engineer conditions that eventually favor competitors they cannot resist. As soil depth increases and nutrients accumulate, shrubs can establish. Shrubs shade out the lichens and mosses that cannot grow in low light. Later, trees shade out the shrubs. Each seral stage is outcompeted by the next — not because the pioneers were weak, but because they transformed the environment to favor different species.

The intermediate disturbance hypothesis adds a crucial wrinkle to this picture. It predicts that species diversity is not highest in undisturbed, "mature" communities — it peaks at intermediate disturbance frequencies. With no disturbance, competitive dominants gradually eliminate subordinate species (succession proceeds to a low-diversity dominant state). With very high disturbance, nothing can establish between events. At intermediate levels — periodic fires, storms, gap formation — the community is repeatedly reset in patches, preventing any single dominant from monopolizing all space and resources. This explains why some of the most diverse ecosystems on Earth (tropical forests, coral reefs, grasslands) are characterized by persistent, moderate disturbance.

Finally, abandon the idea that succession reliably ends at a stable "climax community." This concept was appealing in early ecology but has been revised substantially. Ecosystems exist in dynamic equilibrium, driven by ongoing disturbance. Many communities persist in alternative stable states — different species assemblages that are each self-maintaining under the same climate conditions. Which state a community ends up in depends partly on history: which species arrived first, which disturbances occurred, and what legacy effects persist from previous occupants. Succession describes a trajectory, not a guaranteed destination.
