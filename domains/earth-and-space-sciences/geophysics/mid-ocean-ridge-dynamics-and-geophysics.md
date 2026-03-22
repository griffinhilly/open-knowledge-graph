---
id: mid-ocean-ridge-dynamics-and-geophysics
title: Mid-Ocean Ridge Dynamics and Geophysics
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: mantle-convection-and-dynamics
  type: hard
- id: plate-tectonics
  type: hard
- id: geothermal-gradient-crustal-heat-flow
  type: soft
tags:
- ridge
- spreading
- tectonics
- volcanism
stage: advanced
status: draft
---

# Mid-Ocean Ridge Dynamics and Geophysics

## Core Idea
Mid-ocean ridges are divergent plate boundaries where new oceanic lithosphere forms by upwelling mantle decompression melting. Spreading rate (full rate, 2–20 cm/yr) controls ridge morphology: slow ridges are deep with large scarps; fast ridges are shallow with an axial volcanic high. Seismic imaging reveals the melt distribution and magma chamber structure; heat flow is anomalously high due to young, hot lithosphere; crustal accretion mechanisms (magmatic vs. amagmatic) vary along ridge axis. Magnetic anomalies record reversals and spreading rate changes, providing a precise chronology of ocean floor age.

## Questions

```yaml
- question: "A student explains that mantle melting at mid-ocean ridges happens because rising mantle rock heats up as it approaches the hotter surface. What is wrong with this explanation?"
  type: multiple-choice
  options:
    - "Nothing—rising rock does heat up, and that is the primary driver of melting"
    - "The key driver is pressure decrease, not temperature increase: as mantle rock rises, the melting point drops below the rock's already-hot temperature even though the rock's temperature barely changes"
    - "Mantle rock doesn't actually melt at ridges—pre-existing melt pockets are simply released by the divergence"
    - "Temperature does increase, but only slightly; the main factor is the chemical composition of the mantle changing with depth"
  answer: 1
  explanation: "This is the most common misconception about ridge volcanism. The rising mantle is already close to its melting temperature at depth. As it ascends, the ambient pressure falls, which lowers the rock's melting point. The rock's temperature stays nearly constant (it cools adiabatically at only about 0.3°C/km), but the melting threshold drops below it—so melting begins. This is decompression melting: the cause is a falling melting point, not a rising temperature."

- question: "The Mid-Atlantic Ridge has a deep axial rift valley while the East Pacific Rise has a smooth axial high. What primarily controls this difference in morphology?"
  type: multiple-choice
  options:
    - "The Mid-Atlantic Ridge is older and has subsided more under the weight of accumulated sediment"
    - "Spreading rate: slow ridges have intermittent magma supply so tectonic faulting dominates and creates rift valleys; fast ridges have continuous magma supply that inflates the crust into an axial high"
    - "The Mid-Atlantic Ridge is closer to continental margins, where crustal density pulls the ridge axis down"
    - "Differences in mantle composition beneath the two ridges control melt fraction and therefore ridge height"
  answer: 1
  explanation: "Spreading rate is the single most important variable controlling ridge morphology. At the slow-spreading Mid-Atlantic Ridge (<4 cm/yr full rate), the magma supply is intermittent. Without continuous volcanism to build and inflate the crust, tectonic extension dominates: normal faults develop and throw creates the characteristic deep rift valley. At the fast-spreading East Pacific Rise (>8 cm/yr), a persistent axial magma chamber continuously replenishes the crust, and the inflated magma system lifts the surface into an axial high."

- question: "The symmetric striped pattern of magnetic anomalies on either side of a mid-ocean ridge was produced by geomagnetic polarity reversals recorded in cooling basalt as new oceanic crust formed."
  type: true-false
  answer: true
  explanation: "As basaltic lava erupts at the ridge axis and cools below the Curie temperature, iron-bearing minerals lock in the orientation of the geomagnetic field at that moment. When the field reverses, subsequent eruptions record the new polarity. Because seafloor spreads symmetrically away from the ridge, older crust is farther from the axis, and the stripes on each side are mirror images. This was one of the key lines of evidence for seafloor spreading and today allows reconstruction of plate motions back to the Jurassic."

- question: "During amagmatic spreading at slow ridges, oceanic crust still forms the normal layered sequence of pillow basalts, sheeted dikes, and gabbro—just at reduced thickness due to the lower magma supply."
  type: true-false
  answer: false
  explanation: "In amagmatic spreading, there is essentially no magmatic crust formed at all. Instead, detachment faulting exhumes mantle peridotite directly to the seafloor, producing oceanic core complexes. The normal crustal section (pillow basalts → sheeted dikes → gabbro) is absent. This is not simply thin crust—it is a fundamentally different crustal type, dominated by serpentinized mantle rock rather than basaltic or gabbroic material."

- question: "What is decompression melting, and why does it occur at mid-ocean ridges even though the temperature of the rising mantle barely changes during ascent?"
  type: short-answer
  answer: "Decompression melting occurs when rock melts because the pressure acting on it decreases, lowering its melting point below its current temperature—even without a significant temperature increase. At mid-ocean ridges, diverging plates draw hot mantle rock upward. As this rock rises, the confining pressure drops. The melting point (solidus) of mantle peridotite decreases with pressure, so the ascending rock, which was already near its melting point at depth, crosses its solidus and begins to partially melt—typically generating 15–20% basaltic melt. The temperature change during adiabatic ascent is small (~0.3°C/km), so the temperature barely moves while the melting threshold falls to meet it."
  explanation: "The key is understanding that melting point is pressure-dependent. A common misconception is that the mantle melts because it heats up near the surface, but geothermal gradients in the upper mantle work against this—the surface is cooler. What actually happens is that rising rock maintains its temperature while its melting threshold drops due to decompression, triggering melting without any external heat source."
```

## Explainer

From mantle convection and plate tectonics, you understand that Earth's interior heat drives convective flow and that plates diverge at spreading centers. Mid-ocean ridges are where this process becomes directly observable in geophysical data — they are the factories where oceanic lithosphere is manufactured, and their behavior reveals fundamental connections between mantle dynamics, volcanism, and crustal formation.

The engine of a mid-ocean ridge is **decompression melting**. As plates diverge, hot mantle rock rises to fill the gap. This rock is already close to its melting temperature at depth, and as it ascends, the pressure decreases while the temperature barely changes. Since the melting point of rock decreases with pressure, the rising mantle crosses its solidus and begins to partially melt — typically producing 15–20% melt from a peridotite source. This basaltic melt is less dense than the surrounding solid, so it migrates upward through porous flow and focused conduits, eventually erupting at the ridge axis or crystallizing in a shallow **axial magma chamber** (AMC). The resulting oceanic crust has a characteristic layered structure: pillow basalts on top, sheeted dikes below, and gabbro (slowly cooled melt) at the base.

**Spreading rate** is the single most important variable controlling ridge character. Fast-spreading ridges like the East Pacific Rise (full rate >8 cm/yr) have a robust, continuous magma supply. The AMC is a persistent, narrow melt lens detectable as a strong seismic reflector, and the ridge crest is marked by a smooth axial high — the surface expression of the inflated magma system beneath. Slow-spreading ridges like the Mid-Atlantic Ridge (<4 cm/yr) receive less melt. The magma supply is intermittent, so the AMC is transient or absent. Without continuous volcanism to build the crust, tectonic extension dominates: deep rift valleys form, bounded by large normal faults with throws of hundreds of meters. In some segments, spreading is **amagmatic** — mantle peridotite is exhumed directly to the seafloor by detachment faulting, producing oceanic core complexes without a normal crustal section at all.

Geophysical observations illuminate these processes from multiple angles. **Heat flow** measurements show values several times the global average near the ridge axis, reflecting the proximity of hot mantle and the cooling of newly formed lithosphere — though hydrothermal circulation through young, permeable crust complicates the signal by redistributing heat laterally. **Seismic surveys** image the AMC reflector, map crustal thickness variations along the ridge, and detect regions of partial melt in the underlying mantle. **Magnetic anomaly** stripes, created as cooling basalt locks in the polarity of the geomagnetic field at the time of eruption, provide a tape-recorder record of spreading history. The symmetric pattern of normal and reversed polarity stripes on either side of the ridge was one of the key pieces of evidence for seafloor spreading itself, and today these anomalies are used to reconstruct plate motions with precision back to the Jurassic.
