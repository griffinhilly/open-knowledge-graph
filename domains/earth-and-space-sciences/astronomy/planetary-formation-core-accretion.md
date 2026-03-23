---
id: planetary-formation-core-accretion
title: 'Planetary Formation I: Core Accretion and Migration'
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: planetary-formation
  type: soft
- id: protoplanetary-disk-structure
  type: soft
builds-toward:
- planetary-formation-disk-instability
- multi-planet-system-architecture
tags:
- planet-formation
- core-accretion
- migration
stage: formal-systems
status: validated
---

# Planetary Formation I: Core Accretion and Migration

## Core Idea
Core accretion is the dominant theory of planetary formation, in which kilometer-sized planetesimals accumulate through collisions to form planetary cores. Planets migrate inward and outward through gravitational interactions with the protoplanetary disk, explaining why giant planets are found at various orbital distances rather than being segregated by their formation distance from the star.

## Questions

```yaml
- question: "Hot Jupiters are gas giant planets found orbiting within 0.1 AU of their stars — well inside the orbit of Mercury. According to core accretion theory with migration, how did they arrive there?"
  type: multiple-choice
  options:
    - "They formed close to their stars from a dense inner disk region where gas and rocky material were both abundant enough for giant planet assembly"
    - "They migrated inward from beyond the snow line, where ice augmented the solid material available for core growth and runaway gas accretion was possible before the disk dissipated"
    - "They are failed stellar companions that condensed directly from gas by gravitational instability without requiring a solid core phase"
    - "They were gravitationally captured from other solar systems during close stellar encounters in young star clusters"
  answer: 1
  explanation: "Hot Jupiters cannot have formed where we find them — the inner disk is too hot for ice to condense, providing insufficient solid material for a large core, and the limited gas there is not enough for runaway gas accretion. Core accretion requires forming beyond the snow line where ice approximately doubles the solid surface density. Once a gas giant formed there, Type II migration (the planet opens a gap in the disk and migrates inward locked to the disk's viscous evolution) carried it inward, sometimes all the way to a very short period orbit. Migration is the critical bridge between where planets form and where we find them."

- question: "The 'meter-size barrier' in core accretion theory describes the challenge that:"
  type: multiple-choice
  options:
    - "Meter-sized boulders are too massive for gas drag to affect, so they stall at that size and cannot grow further"
    - "Objects around a meter across experience aerodynamic drag from disk gas that causes them to spiral inward toward the star faster than they can grow through further collisions"
    - "At meter scales, electrostatic repulsion between silicate surfaces prevents sticking, so collisions become destructive"
    - "Meter-sized rocks are fragmented by tidal forces from the protostar before they can accumulate into larger bodies"
  answer: 1
  explanation: "Objects in the centimeter-to-meter size range experience the worst of both worlds: they are large enough to feel significant aerodynamic drag from the surrounding gas (unlike tiny dust grains that are tightly coupled to the gas), but small enough that this drag is not negligible. The gas orbits slightly slower than Keplerian speed due to pressure support; meter-sized rocks orbit at full Keplerian speed and therefore feel a continuous headwind that saps their angular momentum, causing them to spiral inward. The timescale for a meter-sized rock to fall into the star can be only hundreds of years — far too fast for growth. Streaming instabilities solve this by concentrating particles directly into kilometer-scale planetesimals."

- question: "Gas giant planets require a solid core of approximately 10 Earth masses before they can begin accreting hydrogen and helium from the surrounding disk."
  type: true-false
  answer: true
  explanation: "This is the critical core mass threshold in core accretion theory. Below ~10 Earth masses, a growing core can hold only a thin gaseous envelope — any gas it attracts is in quasi-hydrostatic equilibrium and does not accrete rapidly. At approximately 10 Earth masses, the core's gravitational pull becomes strong enough to overcome the thermal pressure supporting the envelope, triggering runaway gas accretion: gas pours in rapidly, and the planet can grow from a 10 Earth-mass core to hundreds of Earth masses in as little as 100,000 years. The race is to reach this threshold before the protoplanetary disk dissipates (typically within 3–10 million years)."

- question: "According to core accretion theory, the difference between rocky terrestrial planets and gas giants is primarily one of distance from the star — gas giants simply form in a denser part of the inner disk, not through a fundamentally different process."
  type: true-false
  answer: false
  explanation: "Gas giants form beyond the snow line (not closer to the star) and through an additional phase — runaway gas accretion — that has no analog in terrestrial planet formation. The snow line matters because water ice condenses beyond it, roughly doubling the surface density of solid material available for core growth and enabling cores to grow large enough to reach critical mass. Rocky terrestrial planets never reach critical core mass because the inner disk lacks this extra solid material. Gas giants also require runaway gas accretion as a distinct third phase after dust coagulation and core accretion; terrestrial planets form entirely from solid material without this gas-capture step."

- question: "Why is the snow line important in the core accretion model, and what happens to a rocky core once it reaches approximately 10 Earth masses?"
  type: short-answer
  answer: "The snow line is the distance from the star where water ice condenses (roughly 3 AU in our solar system). Beyond it, both silicate rock and water ice are available as solid building blocks, roughly doubling the surface density of solid material compared to the inner disk. This extra material allows rocky cores to grow larger than they could in the ice-free inner disk. When a core reaches approximately 10 Earth masses (the critical core mass), its gravitational attraction becomes sufficient to pull in and retain hydrogen and helium gas from the surrounding disk rather than just holding a thin hydrostatic envelope. At this point, runaway gas accretion begins: the envelope collapses and gas accretes rapidly, potentially growing the planet to Jupiter size within ~100,000 years — well before the disk dissipates."
  explanation: "The snow line acts as a boundary between where terrestrial and gas-giant formation are possible. Interior to it, solid surface densities are too low for cores to reach critical mass. Exterior to it, ice boosts solid density and cores can grow large enough to trigger the gas accretion phase that distinguishes gas giants from rocky planets."
```

## Explainer

You already know that protoplanetary disks are rotating structures of gas and dust surrounding young stars, with temperature and composition varying by distance from the star. The **core accretion** model explains how the raw material in these disks assembles into planets through a sequence of stages that span millions of years, starting from microscopic dust grains and ending with worlds the size of Jupiter.

The process begins with **dust coagulation**: micron-sized grains of silicate and ice collide gently in the disk and stick together through electrostatic and surface forces, growing into millimeter- and centimeter-sized aggregates. This early phase is straightforward, but a major theoretical challenge arises at the meter scale — the so-called **meter-size barrier**. Objects around a meter across experience strong aerodynamic drag from the surrounding gas, causing them to spiral inward toward the star on timescales of only a few hundred years, faster than they can grow by further collisions. The leading solution involves **streaming instabilities**, where particles concentrate into dense clumps through collective interactions with the gas, bypassing the problematic size range and jumping directly to kilometer-scale **planetesimals**.

Once planetesimals reach roughly a kilometer across, gravity takes over as the dominant growth mechanism. Larger bodies have stronger gravitational fields, so they sweep up more material than smaller ones — a process called **runaway accretion**. The biggest planetesimals grow fastest, quickly outpacing their neighbors. Eventually, a few dominant bodies — **planetary embryos** — have consumed or scattered most of the nearby material, and growth transitions to **oligarchic accretion**, where a handful of similarly sized embryos compete for the remaining planetesimals in their feeding zones. For rocky planets like Earth, this oligarchic stage produces Mars-sized embryos that later undergo giant impacts over tens of millions of years, gradually assembling into the final terrestrial planets.

Gas giants require an additional step. Beyond the **snow line** — the distance from the star where water ice condenses, roughly 3 AU in our solar system — solid cores can grow larger because ice adds to the available solid material. When a core reaches approximately 10 Earth masses (the **critical core mass**), its gravity becomes strong enough to capture and retain hydrogen and helium gas from the surrounding disk. Gas accretion begins slowly but accelerates dramatically in a process called **runaway gas accretion**, allowing a planet to balloon from a rocky core to a gas giant of hundreds of Earth masses in as little as a hundred thousand years. This must happen before the disk dissipates — typically within 3–10 million years — which sets a tight deadline for giant planet formation.

**Planetary migration** resolves a puzzle that the basic core accretion model cannot: why hot Jupiters orbit closer to their stars than Mercury orbits the Sun, far inside the snow line where they could not have formed. A forming planet exchanges angular momentum with the gas disk through gravitational torques. **Type I migration** affects lower-mass planets embedded in the disk and can move them inward (or occasionally outward) over millions of years. **Type II migration** occurs when a planet grows massive enough to open a gap in the disk; it then migrates locked to the disk's own viscous evolution. Migration explains the wide diversity of observed exoplanet architectures — from hot Jupiters to compact multi-planet systems — as outcomes of the same physical process operating under different disk conditions and timescales.
