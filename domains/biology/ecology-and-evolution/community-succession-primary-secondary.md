---
id: community-succession-primary-secondary
title: 'Community Succession: Primary and Secondary'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: ecological-succession
  type: hard
- id: species-interactions
  type: soft
builds-toward:
- community-stability-resistance-resilience
- restoration-ecology-principles
tags:
- succession
- primary
- secondary
- pioneer-species
- climax-community
stage: formal-systems
status: validated
---

# Community Succession: Primary and Secondary

## Core Idea
Primary succession begins on bare rock or newly formed substrate where no soil exists (volcanic islands, glacial retreats). Secondary succession follows disturbance in established communities with intact soil (fire, logging). Early successional stages are dominated by pioneer species with high dispersal; later stages have higher diversity and longer-lived species.

## Questions

```yaml
- question: "A forest fire burns through an established forest, leaving bare but intact mineral soil. Separately, a volcanic eruption creates a new lava field with no soil. Which comparison correctly describes the succession that follows in each site?"
  type: multiple-choice
  options:
    - "Both sites undergo identical primary succession because both start with bare substrate after a destructive event"
    - "The burned forest undergoes secondary succession — soil, seed bank, and fungal networks are intact — and recovers much faster; the lava field undergoes primary succession starting with no soil and progresses over centuries"
    - "The burned forest undergoes primary succession because fire destroys all biological material including soil"
    - "The lava field undergoes secondary succession because lava rock contains abundant mineral nutrients for pioneer plants"
  answer: 1
  explanation: "The key distinction is whether soil is present when succession begins. Fire is typically a surface disturbance — it burns the vegetation and organic litter but leaves the mineral soil, its seed bank, fungal networks, and nutrient reserves intact. Secondary succession begins with these advantages and recovers in decades. The lava field has none of this: no soil, no seed bank, no organic matter. Primary succession must build the soil itself, starting with lichens and cyanobacteria that colonize bare rock, and may take centuries before supporting forest. The mechanism of disturbance (fire vs. volcanic) matters less than what it leaves behind."

- question: "In a primary succession study, lichens colonize bare rock, die, and contribute organic matter that enables mosses to establish. The mosses then outcompete and displace the lichens. Which successional mechanism does this illustrate?"
  type: multiple-choice
  options:
    - "Inhibition — later species actively suppress the pioneer species to prevent re-establishment"
    - "Tolerance — the mosses simply outcompete the lichens without depending on any modifications the lichens made"
    - "Facilitation — the pioneer species modify the environment in ways that allow later species to establish, even at the cost of their own eventual displacement"
    - "Primary succession cannot involve competitive exclusion between successional stages"
  answer: 2
  explanation: "Facilitation is the model in which early colonizers make the environment less suitable for themselves and more suitable for later arrivals. The lichens break down rock, add organic material, and create the thin soil that mosses require — then find themselves displaced by the very conditions they created. This is a recurring pattern in primary succession: pioneers are rarely the 'winners' in the long run; they are the builders who make subsequent stages possible. Inhibition (option A) would mean the pioneer actively prevents later species from establishing, which is the opposite of what happened here."

- question: "The primary reason secondary succession proceeds faster than primary succession on bare rock is that secondary succession sites receive more rainfall and sunlight due to the absence of a forest canopy."
  type: true-false
  answer: false
  explanation: "The speed advantage of secondary succession has nothing to do with abiotic differences in rainfall or sunlight. The key advantage is pre-existing soil: intact mineral soil containing organic matter, a seed bank of dormant seeds from the pre-disturbance community, living fungal networks (mycorrhizae) that accelerate plant establishment, and stored nutrients. These biological and chemical resources compress the recovery timeline from centuries to decades. Primary succession on bare rock lacks all of these — it must build soil from nothing, which is the slow step."

- question: "In modern ecology, the 'climax community' concept is best understood as a dynamic steady state subject to ongoing disturbance at varying scales, rather than a fixed endpoint that every successional sequence inevitably reaches."
  type: true-false
  answer: true
  explanation: "The classic climax concept — a single stable endpoint determined by regional climate — has been substantially revised. Modern ecologists recognize that disturbances occur at many scales and frequencies: a 'climax' forest experiences constant small-scale gaps from falling trees, periodic fires, insect outbreaks, and infrequent catastrophic events. Each disturbance initiates local succession. The landscape at any moment is a mosaic of patches at different successional stages. Rather than a static endpoint, 'climax' is better understood as the most frequently observed state under a given disturbance regime — a dynamic equilibrium, not a permanent destination."

- question: "What is facilitation in ecological succession, and why does it explain why pioneer species are eventually replaced by later-successional species even when the pioneers initially dominated?"
  type: short-answer
  answer: "Facilitation is the process by which early-successional species modify the environment in ways that make it more hospitable for later-successional species, even though those modifications eventually disadvantage the pioneers themselves. Lichens break down rock and create thin soil that mosses need. Nitrogen-fixing species like alder enrich soil that supports more diverse plants. Shade-tolerant seedlings establish under the canopy created by sun-loving pioneers. In each case, the pioneer species is engineering its own competitive displacement: the habitat it creates suits its successors better than itself. This is why succession tends to proceed in a somewhat predictable direction — each stage prepares the ground for the next."
  explanation: "Facilitation is not the only mechanism: inhibition occurs when early species actively resist replacement, and tolerance describes cases where later species simply outcompete earlier ones without depending on their modifications. Real successions often involve all three mechanisms operating simultaneously in different parts of the community. But facilitation is the mechanism most directly responsible for the characteristic replacement of pioneer species — those adapted to harsh initial conditions — by later-successional species adapted to the more developed conditions the pioneers help create."
```

## Explainer

From your study of ecological succession, you understand the general principle: communities change over time in a somewhat predictable sequence after a disturbance. The distinction between **primary** and **secondary succession** comes down to one critical factor — whether soil is present when the process begins. This seemingly simple difference has profound consequences for the speed, trajectory, and participants in the successional sequence.

**Primary succession** starts from scratch — literally. Think of a newly cooled lava flow, a retreating glacier exposing bare rock, or a newly formed volcanic island. There is no soil, no seed bank, no organic matter. The first colonizers must be organisms that can survive on bare mineral surfaces: **lichens** (symbioses of fungi and photosynthetic algae or cyanobacteria) that can dissolve rock and begin soil formation, and **cyanobacteria** that fix nitrogen from the atmosphere. These pioneers are slow-growing but spectacularly tough. As they live, die, and decompose, they create thin layers of organic material that mix with weathered rock particles to form primitive soil. Mosses follow, then small herbaceous plants whose roots further break down rock and add organic matter. Over decades to centuries, the soil deepens enough to support shrubs and eventually trees. Primary succession on glacial moraines in Alaska, for example, progresses from bare till to alder thickets to spruce forest over roughly 200 years.

**Secondary succession** begins with a major advantage: the soil is already there. After a forest fire, a logged clearcut, or an abandoned farm field, the mineral soil, its seed bank, fungal networks, and nutrient reserves remain intact. Pioneer species in secondary succession are fast-growing, sun-loving plants — grasses, wildflowers, and early-successional trees like birch or aspen — that can rapidly exploit the open conditions. Because they don't need to build soil from nothing, the process is dramatically faster. An abandoned agricultural field in the eastern United States can progress from weedy annuals to a young forest in 50–100 years, compared to the centuries or millennia that primary succession on bare rock requires.

In both types, the general trajectory follows a pattern shaped by species interactions you already know. Early colonizers modify the environment — adding nutrients, creating shade, altering soil chemistry — in ways that often make conditions less favorable for themselves and more favorable for later arrivals. This **facilitation** model explains why pioneer species are eventually replaced: they create the very conditions that allow their competitors to establish. However, succession does not always follow a single deterministic path. **Inhibition** occurs when early species resist displacement, and **tolerance** describes cases where later species simply outcompete earlier ones without depending on their modifications. The endpoint — sometimes called a **climax community** — is the relatively stable assemblage that persists until the next major disturbance resets the clock. Modern ecologists view climax less as a fixed destination and more as a dynamic steady state, always subject to disruption at some scale.
