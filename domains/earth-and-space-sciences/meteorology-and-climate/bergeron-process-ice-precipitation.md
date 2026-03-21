---
id: bergeron-process-ice-precipitation
title: Bergeron Process and Ice Crystal Precipitation
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: cloud-condensation-nuclei-activation
  type: hard
- id: latent-heat-and-phase-transitions
  type: hard
builds-toward:
- graupel-and-hail-formation
- precipitation-types-and-processes
tags:
- microphysics
- precipitation
- ice-crystals
stage: advanced
status: draft
---

# Bergeron Process and Ice Crystal Precipitation

## Core Idea
In mixed-phase clouds (containing both liquid droplets and ice crystals), ice crystals grow rapidly at the expense of liquid droplets because the saturation vapor pressure is lower over ice than over water. This Bergeron process is extremely efficient and is the primary precipitation mechanism in mid-latitude and polar clouds. It explains why ice crystals appearing in supercooled clouds trigger rapid precipitation.

## How It's Best Learned
Study the vapor pressure difference between water and ice as a function of temperature; examine mixed-phase cloud radar signatures; observe how seeding clouds with ice nuclei affects precipitation.

## Common Misconceptions
- Thinking the Bergeron process requires liquid water to freeze (ice crystals remain solid; liquid droplets evaporate).
- Believing warm tropical rain always forms by the Bergeron process (warm rain dominates there).

## Questions

```yaml
- question: "A mixed-phase cloud at −15°C contains both supercooled liquid droplets and a small number of ice crystals. The air is at exactly the saturation vapor pressure for liquid water. What happens to the droplets and crystals over the next 15–20 minutes?"
  type: multiple-choice
  options:
    - "Nothing changes — the cloud is in thermodynamic equilibrium since the air is at saturation"
    - "The supercooled droplets gradually freeze as small temperature fluctuations push them below the homogeneous nucleation threshold"
    - "The ice crystals grow by vapor deposition while the liquid droplets evaporate, because air saturated with respect to liquid is supersaturated with respect to ice"
    - "The ice crystals melt and the droplets grow, because temperatures above −20°C favor the liquid phase"
  answer: 2
  explanation: "This is the Bergeron process in action. The key physical fact is that the saturation vapor pressure over ice is lower than over liquid water at the same subfreezing temperature. Air at liquid saturation is therefore supersaturated with respect to ice — vapor deposits onto ice crystals faster than it leaves them. As ice crystals consume vapor, the vapor pressure drops below liquid saturation, forcing droplets to evaporate to restore equilibrium. Mass transfers from liquid to ice via the vapor phase. The droplets do not freeze; they evaporate. This transfer is remarkably fast — a single ice crystal can grow to precipitation size in 15–20 minutes."

- question: "Warm maritime clouds with bases near sea level and tops that barely reach 0°C produce heavy rainfall in tropical regions. Which precipitation mechanism dominates in these clouds, and why?"
  type: multiple-choice
  options:
    - "The Bergeron process, because ice crystals always nucleate at the very top of any cloud that reaches freezing temperature"
    - "Collision-coalescence of liquid droplets, because the cloud lacks the extensive subfreezing layer of coexisting liquid and ice needed for the Bergeron process to operate efficiently"
    - "Both mechanisms operate with equal contribution — the Bergeron process above the freezing level and collision-coalescence below"
    - "Neither mechanism — tropical rain requires strong updrafts to loft droplets high enough to encounter ice"
  answer: 1
  explanation: "The Bergeron process requires a mixed-phase zone where supercooled liquid droplets and ice crystals coexist. Clouds with tops barely at 0°C have little or no such zone. Warm maritime tropical clouds instead produce 'warm rain' entirely through collision-coalescence: large cloud droplets collide with smaller ones, grow, and eventually become heavy enough to fall. This is the dominant precipitation mechanism in the tropics where cloud tops rarely reach deep subfreezing temperatures. Bergeron dominates in mid-latitude and polar clouds where extensive cold layers allow mixed-phase conditions to persist."

- question: "In the Bergeron process, supercooled liquid droplets freeze directly to form ice crystals, which then grow by aggregating with other crystals."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about the Bergeron process. Supercooled liquid droplets do not freeze — they evaporate. The water vapor produced by evaporation is then deposited directly onto existing ice crystals. The entire mass transfer happens through the vapor phase. The ice crystals remain solid throughout; only their size changes as vapor deposits on them. This vapor-phase transfer is what makes the process so efficient: ice crystals grow rapidly without needing to collide with other droplets or crystals."

- question: "Cloud seeding with silver iodide can enhance precipitation from supercooled clouds by introducing artificial ice nuclei that trigger the Bergeron process."
  type: true-false
  answer: true
  explanation: "Silver iodide has a crystal structure similar to ice and is an effective ice nucleus even at temperatures as warm as −4°C. Introducing it into a supercooled cloud creates many ice crystals where few existed before, triggering the vapor pressure imbalance that drives the Bergeron process — ice crystals grow rapidly at the expense of liquid droplets. However, this only works if the cloud contains sufficient supercooled liquid water to begin with. Seeding a cloud that is already glaciated (all ice) or has too little liquid water produces no enhancement."

- question: "Explain why introducing a small number of ice crystals into a supercooled liquid cloud triggers rapid ice crystal growth, without any change in the cloud's temperature."
  type: short-answer
  answer: "The saturation vapor pressure over ice is lower than over liquid water at the same subfreezing temperature. A cloud in equilibrium with its liquid droplets (air at liquid saturation) is therefore supersaturated with respect to ice. When ice crystals are introduced, vapor deposits onto them faster than it leaves, so the crystals grow rapidly. As they consume water vapor, the air pressure drops below liquid saturation, forcing some droplets to evaporate to restore equilibrium. This self-sustaining cycle transfers mass from droplets to ice crystals entirely through the vapor phase — no temperature change is required. The driving force is purely the thermodynamic difference in vapor pressure between the two phases."
  explanation: "The magnitude of the vapor pressure difference between liquid and ice peaks at around −10 to −20°C, which is why the Bergeron process is most efficient in clouds with tops in that temperature range. Below about −40°C, spontaneous homogeneous nucleation freezes all remaining liquid, removing the mixed-phase condition necessary for the process. Above 0°C, there is no ice phase. The Bergeron process therefore operates in a specific temperature window where mixed-phase conditions can be sustained."
```

## Explainer

From your study of cloud condensation nuclei and latent heat, you know that water vapor in the atmosphere condenses onto tiny particles to form cloud droplets, and that phase changes release or absorb energy. The Bergeron process builds on a subtle but powerful consequence of these ideas: ice and liquid water coexisting in the same cloud creates a vapor pressure imbalance that drives rapid ice crystal growth and is responsible for most precipitation outside the tropics.

The key physical fact is that **saturation vapor pressure over ice is lower than over liquid water** at the same subfreezing temperature. Imagine a cloud between about −10°C and −20°C containing both supercooled liquid droplets and a few ice crystals. The air may be saturated with respect to liquid water — meaning the droplets are in equilibrium with their surroundings — but that same air is actually supersaturated with respect to the ice surface. Water vapor molecules deposit onto the ice crystals faster than they sublimate away, so the ice crystals grow. As vapor is consumed by the growing crystals, the air dips below liquid saturation, causing the liquid droplets to evaporate to restore equilibrium. The net effect is a transfer of mass from liquid droplets to ice crystals, with the vapor phase acting as an intermediary. The liquid droplets shrink and disappear; the ice crystals fatten.

This process is remarkably efficient. A single ice crystal in a field of supercooled droplets can grow to precipitation size in about 15–20 minutes — far faster than droplets could grow by collision-coalescence alone in such clouds. The resulting ice crystals may aggregate into snowflakes as they fall, or melt into raindrops if they pass through a warm layer below. In mid-latitude weather systems, where cloud tops routinely reach temperatures cold enough for mixed-phase conditions, the Bergeron process is the dominant precipitation mechanism.

Understanding when the Bergeron process is active versus when warm-rain collision-coalescence dominates depends on cloud temperature structure. Tropical maritime clouds with warm bases and tops that barely reach freezing produce rain almost entirely through droplet collisions. Mid-latitude and polar clouds, with extensive subfreezing layers, rely heavily on ice-phase growth. Cloud seeding exploits the Bergeron process directly: introducing artificial ice nuclei (like silver iodide) into a supercooled cloud creates more ice crystals, triggering the vapor pressure imbalance and enhancing precipitation — though only if the cloud already contains sufficient supercooled liquid water for the transfer to occur.
