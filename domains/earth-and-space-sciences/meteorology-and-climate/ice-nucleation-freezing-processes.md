---
id: ice-nucleation-freezing-processes
title: Ice Nucleation and Freezing Processes in Clouds
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: cloud-condensation-nuclei-activation
  type: hard
- id: precipitation-types-and-processes
  type: soft
builds-toward:
- bergeron-process-ice-precipitation
tags:
- ice
- nucleation
- freezing
- cloud-microphysics
stage: formal-systems
status: validated
---

# Ice Nucleation and Freezing Processes in Clouds

## Core Idea
Ice nuclei (mineral dust, bacteria, pollution particles) catalyze freezing of supercooled droplets (liquid below 0°C), enabling ice crystal formation. Freezing temperatures range from −5°C to −40°C depending on ice nuclei type, with heterogeneous nucleation on particles dominating over homogeneous freezing in clouds. Ice formation initiates the Bergeron process, key to precipitation in mid-latitude clouds and colder regions.

## How It's Best Learned
Study cloud chamber experiments showing ice nucleation at different temperatures. Examine relationships between cloud temperature and ice fraction.

## Questions

```yaml
- question: "A cloud at −15°C is observed to contain only liquid water droplets with no detectable ice. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "At −15°C, water cannot exist as a liquid; the observation must be an instrument error"
    - "The cloud lacks effective ice nucleating particles, so supercooled liquid droplets persist despite temperatures well below 0°C"
    - "The cloud is too warm for ice formation; ice only forms below −40°C in all circumstances"
    - "The droplets are too large to be nucleated by available particles"
  answer: 1
  explanation: "Supercooling is common in clouds. Without effective ice nucleating particles (INPs), pure water droplets can remain liquid down to about −40°C. At −15°C, ice formation requires heterogeneous nucleation on mineral dust or similar INPs. In their absence, the surface-energy barrier prevents spontaneous homogeneous nucleation at that temperature. All-liquid clouds at −15°C are physically possible and well-documented in nature."

- question: "In a mixed-phase cloud between −10°C and −40°C, why do ice crystals grow preferentially at the expense of supercooled liquid droplets?"
  type: multiple-choice
  options:
    - "Ice crystals are larger and physically sweep up liquid droplets through collision"
    - "Ice crystals are warmer than liquid droplets, creating a vapor pressure gradient"
    - "The saturation vapor pressure over ice is lower than over liquid water at the same temperature, so vapor flows from droplets to ice"
    - "Ice crystals produce surface tension forces that compress neighboring droplets"
  answer: 2
  explanation: "This is the Bergeron process. At the same sub-zero temperature, the saturation vapor pressure over a liquid surface is higher than over an ice surface. Vapor in the cloud is supersaturated with respect to ice but subsaturated with respect to liquid. Vapor therefore diffuses from liquid droplets (where it is in excess) to ice crystals (where it is deficient), depositing as ice while the droplets shrink. This vapor-pressure differential, not collision, drives rapid ice crystal growth."

- question: "Supercooled liquid water — water that remains liquid below 0°C — can exist in clouds under natural atmospheric conditions."
  type: true-false
  answer: true
  explanation: "Supercooling is a well-documented atmospheric phenomenon. Without ice nucleating particles, the surface-energy barrier to forming an ice crystal lattice prevents freezing at temperatures only slightly below 0°C. Pure water droplets can persist as liquid down to approximately −40°C (the homogeneous nucleation temperature). Clouds in the −10°C to −40°C range routinely contain a mixture of supercooled liquid droplets and ice crystals — the mixed-phase zone central to mid-latitude precipitation."

- question: "All aerosol particles in the atmosphere are approximately equally effective at nucleating ice at a given temperature."
  type: true-false
  answer: false
  explanation: "Ice nucleating efficiency varies enormously among particle types. Certain biological particles (e.g., Pseudomonas syringae bacteria) can nucleate ice near −2°C, while mineral dust (clay minerals like kaolinite and feldspar) operates between −10°C and −20°C, and many common aerosols (sea salt, sulfate) are poor INPs requiring temperatures below −25°C. Effectiveness depends on how closely the particle's crystal surface matches ice's lattice structure. Most atmospheric aerosols are poor INPs."

- question: "Why can't the Bergeron process operate in an all-liquid cloud, and what role does ice nucleation play in enabling it?"
  type: short-answer
  answer: "The Bergeron process relies on the vapor pressure difference between supercooled liquid and ice at the same temperature — vapor flows from liquid to ice, growing ice crystals rapidly. If no ice crystals are present (all-liquid cloud), there is no vapor pressure differential to drive this transfer. Ice nucleation, triggered by INPs, creates the initial ice crystals that then exploit the vapor pressure gradient to grow at the expense of surrounding liquid droplets. Without INPs in the −10°C to −40°C range, mid-latitude precipitation via the Bergeron process cannot occur."
  explanation: "Ice nucleation is not merely a microphysical detail but a gate that controls whether precipitation forms at all. An all-liquid cloud at −15°C would need droplets to grow large enough to collide and coalesce (the warm-rain process), which is much slower. The Bergeron process is far more efficient precisely because the vapor pressure differential drives rapid ice crystal growth — but this only works once ice is present, which requires nucleation by suitable particles."
```

## Explainer

From your study of cloud condensation nuclei, you know that liquid cloud droplets need particles to form on. Ice formation in clouds faces an even higher barrier. Water does not freeze at 0°C in the atmosphere — in fact, cloud droplets routinely remain liquid at temperatures well below freezing, a state called **supercooling**. Pure water droplets can persist as liquid down to about −40°C before freezing spontaneously. The reason is that forming an ice crystal requires water molecules to arrange themselves into an ordered lattice, and the energy cost of creating the surface of a tiny ice embryo is enormous relative to the energy gained from freezing at temperatures only slightly below 0°C. This is the same surface-energy barrier you encountered with liquid droplet formation, but it is even more severe for ice.

**Ice nucleating particles** (INPs) solve this problem the same way CCN solve the condensation problem — by providing a surface that lowers the energy barrier. Certain particles with crystal structures resembling ice, particularly mineral dust (especially clay minerals like kaolinite and feldspar), some biological particles (certain bacteria like *Pseudomonas syringae*), and volcanic ash, can template ice formation at much warmer temperatures than homogeneous freezing. This process is called **heterogeneous nucleation**, and it can occur through several mechanisms: **deposition nucleation** (vapor deposits directly as ice on the particle), **immersion freezing** (a particle already inside a supercooled droplet triggers freezing), **contact freezing** (a particle collides with a supercooled droplet's surface and initiates freezing), and **condensation freezing** (water condenses on the particle and immediately freezes).

The temperature at which freezing occurs depends on the type of INP. The most effective biological INPs can nucleate ice near −2°C, while typical mineral dust operates between −10°C and −20°C, and less effective particles require temperatures below −25°C. This is critically important because the **mixed-phase zone** of a cloud — the layer between about −10°C and −40°C where both supercooled liquid droplets and ice crystals coexist — is where most mid-latitude precipitation originates. Ice crystals in this zone grow rapidly at the expense of surrounding liquid droplets through the Bergeron process, because the saturation vapor pressure over ice is lower than over liquid water at the same temperature. The ice crystals quickly gain mass, aggregate into snowflakes, and fall — melting into rain if they pass through warm air below. Without ice nucleation, clouds in the −10°C to −40°C range would remain entirely liquid, drastically altering global precipitation patterns. Understanding which particles nucleate ice, at what temperatures, and through which mechanisms is therefore essential to both weather prediction and climate modeling.
