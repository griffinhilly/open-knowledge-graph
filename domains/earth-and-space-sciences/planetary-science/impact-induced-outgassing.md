---
id: impact-induced-outgassing
title: Impact-Induced Outgassing and Atmospheric Loss
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: impact-cratering-mechanics
  type: hard
- id: volatile-inventory-and-escape-evolution
  type: soft
- id: late-heavy-bombardment
  type: soft
builds-toward:
- thermal-evolution-terrestrial-planets
- habitable-zone-boundaries-constraints
tags:
- impacts
- outgassing
- atmospheric-loss
- bombardment
stage: expert
status: validated
---
# Impact-Induced Outgassing and Atmospheric Loss

## Core Idea
Giant impacts deposit enormous energy into planetary surfaces and atmospheres, causing rapid vaporization of volatiles and atmospheric erosion. The cumulative effect of early bombardment can strip primordial atmospheres (especially from small bodies), deliver volatiles from planetesimals, and fundamentally alter atmospheric composition and planetary habitability.

## Questions

```yaml
- question: "A planet is struck by thousands of small asteroids over millions of years versus one giant impactor delivering the same total kinetic energy. How do the atmospheric outcomes likely differ?"
  type: multiple-choice
  options:
    - "Both scenarios deliver the same net volatiles because total kinetic energy is identical"
    - "The giant impact strips more atmosphere; many small impacts are net volatile contributors"
    - "Many small impacts strip more atmosphere because cumulative shock waves penetrate deeper"
    - "Giant impacts always add more volatiles because large impactors contain more water ice"
  answer: 1
  explanation: "The key insight is that atmospheric erosion requires an impactor large enough to accelerate overlying atmosphere to escape velocity — small impacts deliver volatiles without achieving this threshold. Many small impacts therefore tend to be net atmospheric contributors. A single giant impact, concentrating enormous energy, can blast the entire atmospheric column into space. The same total energy distributed among many small events has very different consequences than concentrated in one catastrophic event."

- question: "Earth's current atmosphere is described as a 'secondary atmosphere.' What does this imply about the Moon-forming impact?"
  type: multiple-choice
  options:
    - "The Moon-forming impact delivered Earth's initial hydrogen and nitrogen from the impactor"
    - "The Moon-forming impact stripped Earth's primordial atmosphere, requiring a complete rebuild from volcanic outgassing and later impacts"
    - "The Moon-forming impact was too small to affect Earth's atmosphere significantly"
    - "Earth's secondary atmosphere formed because the primary atmosphere slowly leaked into space via thermal escape"
  answer: 1
  explanation: "A 'secondary atmosphere' is one rebuilt after the original was lost — the term implies the primary atmosphere was stripped. The Moon-forming impact was so energetic it reset Earth's atmospheric composition entirely, removing the primordial hydrogen-rich atmosphere. Earth's current atmosphere accumulated subsequently through volcanic outgassing and volatile delivery from later, smaller impactors. This is direct evidence that giant impacts can be catastrophic atmospheric erasers, not just contributors."

- question: "Mars lost much of its early atmosphere to impacts while Earth retained most of its inventory because Mars is less massive."
  type: true-false
  answer: true
  explanation: "This is correct. For a given impact energy, smaller planets with weaker gravity have a lower escape velocity, so impacts can accelerate atmospheric gas to escape velocity more easily. Mars's lower escape velocity means a larger fraction of its atmosphere was lost per impact event. Earth's stronger gravity made atmospheric retention more favorable under the same bombardment conditions."

- question: "Because comets and carbonaceous asteroids are volatile-rich, all large cometary impacts are net contributors to a planet's atmosphere."
  type: true-false
  answer: false
  explanation: "This is false. While comets and carbonaceous asteroids do carry substantial volatiles (comets are roughly half water ice), a sufficiently large impact can erode far more atmosphere than it delivers. The delivered volatile mass and the eroded atmospheric mass scale differently with impactor energy. Very large impacts can be net destroyers of atmosphere even when the impactor is volatile-rich. The balance depends on impact energy, impactor composition, planet size, and impact angle."

- question: "Why is Earth's current atmosphere called a 'secondary atmosphere,' and what does that tell us about the net atmospheric effect of the early bombardment history?"
  type: short-answer
  answer: "Earth's atmosphere is 'secondary' because the Moon-forming giant impact stripped its original primordial atmosphere. The current atmosphere was rebuilt from volcanic outgassing and volatile delivery from subsequent smaller impactors. This implies that early bombardment had mixed effects: many smaller impactors delivered volatiles that built the secondary atmosphere, but at least one giant impact caused catastrophic atmospheric loss."
  explanation: "The distinction matters for planetary habitability: a planet that retains its primordial atmosphere has a different chemical history than one that was reset by a giant impact. For Earth, this reset may have actually been beneficial by removing a hydrogen-dominated reducing atmosphere and enabling the buildup of a nitrogen-oxygen-carbon dioxide secondary atmosphere more conducive to complex chemistry and eventual life."
```

## Explainer

From your study of impact cratering mechanics, you know that hypervelocity collisions release enormous kinetic energy, generating shock waves that melt and vaporize rock. From volatile inventories and atmospheric escape, you understand that planets hold reservoirs of gases and ices that can be gained or lost over time. **Impact-induced outgassing** connects these ideas: when large objects strike a planet, the energy released is so extreme that it does not merely excavate a crater — it can fundamentally restructure the planet's atmosphere by simultaneously releasing trapped volatiles and blasting existing atmosphere into space.

The physics operates through two competing processes. First, the **outgassing effect**: impact energy vaporizes volatile-bearing minerals in both the impactor and the target surface, releasing gases like H₂O, CO₂, CO, SO₂, and reduced species like H₂ and CH₄ into the atmosphere. The impactor itself may be volatile-rich — comets are roughly half water ice, and carbonaceous asteroids contain significant water and carbon locked in hydrated minerals. A single large impact can deliver and release more gas in seconds than a volcano produces in thousands of years. During the Late Heavy Bombardment roughly 3.9 billion years ago, the cumulative volatile delivery from countless impacts may have contributed substantially to Earth's early ocean and atmosphere.

Second, the **atmospheric erosion effect**: the expanding vapor plume and shock wave from a sufficiently large impact can accelerate overlying atmosphere to escape velocity, permanently removing it from the planet. For a given impact energy, smaller planets with weaker gravity lose proportionally more atmosphere — this is why Mars, with its lower escape velocity, may have lost much of its early atmosphere to impacts, while Earth retained most of its inventory. The balance between volatile delivery (adding atmosphere) and atmospheric erosion (removing it) depends on the impactor's size, velocity, and angle of incidence. Oblique impacts are less efficient at eroding atmosphere because more energy is directed laterally rather than upward through the atmospheric column.

The net effect of bombardment on a planet's atmosphere depends on the size distribution of impactors. Many small impacts tend to be net contributors of volatiles, because they deliver material without generating enough energy to erode the existing atmosphere significantly. A few very large impacts, however, can be catastrophic — the Moon-forming impact likely stripped Earth of its primordial hydrogen-rich atmosphere entirely, resetting its atmospheric composition. The atmosphere we live in today is largely a **secondary atmosphere**, rebuilt from volcanic outgassing and later impact delivery after that catastrophic loss. Understanding this interplay between delivery and erosion is essential for reconstructing the atmospheric histories of all terrestrial planets and for assessing whether rocky exoplanets in other systems could have retained atmospheres capable of supporting surface liquid water.
