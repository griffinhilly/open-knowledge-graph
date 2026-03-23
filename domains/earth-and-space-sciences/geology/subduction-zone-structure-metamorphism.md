---
id: subduction-zone-structure-metamorphism
title: Subduction Zone Structure and High-Pressure Metamorphism
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: plate-boundary-types-kinematics
  type: hard
- id: metamorphic-facies-rock-associations
  type: soft
builds-toward:
- continental-collision-orogeny-crustal-thickening
tags:
- subduction
- metamorphism
- plate-tectonics
stage: formal-systems
status: draft
---

# Subduction Zone Structure and High-Pressure Metamorphism

## Core Idea
Subduction zones produce inverted geothermal gradients due to rapid burial of cool oceanic lithosphere. Subducting slabs create diagnostic metamorphic facies (blueschist, eclogite) reflecting high pressure and relatively low temperature. Mineral assemblages in subduction zone metamorphic rocks preserve pressure-temperature-time records of plate descent.

## Questions

```yaml
- question: "Why does subducted oceanic crust form blueschist and eclogite rather than amphibolite or granulite, even at depths where amphibolite is stable in normal continental settings?"
  type: multiple-choice
  options:
    - "Oceanic crust has a basaltic composition that chemically prevents high-temperature minerals from nucleating"
    - "The subducting slab descends faster than the surrounding mantle can heat it, producing anomalously cold temperatures at high pressures"
    - "Blueschist forms at shallower depths before the slab heats up, while eclogite forms at the same depths as amphibolite"
    - "Seawater trapped in oceanic crust acts as a coolant, suppressing temperature regardless of burial depth"
  answer: 1
  explanation: "The critical factor is thermal inertia. Oceanic lithosphere is chilled for millions of years at the seafloor and has low thermal conductivity; it subducts faster than heat can diffuse into it from the surrounding hot mantle. The result is a geothermal gradient that is anomalously cold relative to depth — high pressure from burial, but temperature lagging far behind. Amphibolite and granulite require the high-P AND high-T conditions of a normal geothermal gradient, which simply does not describe the subduction environment. Option 2 inverts the depth relationship: blueschist forms at significant depth, not shallow."

- question: "A geologist finds blueschist outcrops in an ancient, deeply eroded mountain belt with no active subduction today. What is the most defensible interpretation?"
  type: multiple-choice
  options:
    - "A highly energetic magmatic event locally elevated pressure without significantly raising temperature"
    - "These rocks record a past subduction zone in this region — blueschist is diagnostic of subduction P-T conditions"
    - "Blueschist can form in any metamorphic environment when lithostatic pressure is sufficiently high"
    - "The rocks were transported from an active oceanic subduction zone by ancient ocean currents"
  answer: 1
  explanation: "Blueschist requires a combination of high pressure and relatively low temperature that is essentially unique to subduction zones — the inverted geothermal gradient cannot be produced by magmatic events (which raise temperature), regional burial (which follows a normal geotherm), or surface processes. Finding blueschist is therefore treated as diagnostic evidence for past subduction. Its presence in ancient orogenic belts is one of the primary tools geologists use to reconstruct Paleozoic and Mesozoic plate configurations. The rarity of blueschist at the surface (most is dragged to unreturnable depths) makes its preservation especially informative."

- question: "The pressure-temperature path recorded by blueschist minerals shows conditions in the upper-left region of P-T space — high pressure at temperatures far lower than a normal continental geothermal gradient would produce at the same depth."
  type: true-false
  answer: true
  explanation: "This is exactly what makes blueschist diagnostically significant. On a standard P-T diagram, normal continental burial follows a gradient moving toward the lower-right (increasing both P and T with depth), passing through greenschist and amphibolite facies. Blueschist plots in the upper-left — high P, low T — a region inaccessible by normal burial. The P-T-t path reconstructed from mineral assemblages (e.g., glaucophane stability fields) confirms rapid pressure increase with modest temperature increase, consistent with fast descent of cold lithosphere. This is not an approximation; it is the defining P-T signature of subduction."

- question: "Eclogite represents an earlier, shallower stage of subduction metamorphism than blueschist, forming at lower pressures before the slab reaches blueschist depths."
  type: true-false
  answer: false
  explanation: "The relationship is opposite. Eclogite forms at *greater* depths and *higher* pressures than blueschist — roughly above 1.5 GPa (equivalent to ~45 km depth), compared to blueschist's onset around 0.6 GPa. As the slab descends deeper, the blueschist assemblage (dominated by glaucophane) becomes unstable and transforms into eclogite (dominated by garnet and omphacite). Eclogite is a later, deeper product of continued subduction, not an earlier stage. P-T-t paths in subduction rocks often show the blueschist → eclogite transition as a record of continued burial."

- question: "Explain why the geothermal gradient in a subduction zone is described as 'anomalous' or 'inverted,' and what metamorphic consequence this produces."
  type: short-answer
  answer: "In normal crust, both temperature and pressure increase with depth along a predictable geothermal gradient, producing metamorphic sequences from greenschist through amphibolite to granulite. In a subduction zone, the descending slab is cold oceanic lithosphere that has been thermally equilibrated at the seafloor for tens of millions of years. It descends faster than heat can conduct into it from the hot surrounding mantle, so at any given depth, the slab is anomalously cold — pressure increases with depth but temperature lags far behind. This high-P, low-T path stabilizes minerals like glaucophane (blueschist) and eventually garnet + omphacite (eclogite) that never form along normal geothermal gradients."
  explanation: "The 'inverted' label refers to the inversion relative to expectation: you'd expect T and P to both increase with depth, but instead P increases while T does not keep pace. This violation of normal metamorphic sequences is precisely what makes subduction-zone rocks so distinctive and so useful as tectonic indicators. The mineral assemblages that crystallize under these anomalous conditions are barometers and thermometers that lock in the P-T history of the slab's descent."
```

## Explainer

At a convergent plate boundary — a concept you already know from plate kinematics — one lithospheric plate dives beneath another and descends into the mantle. What makes subduction zones geologically distinctive is the thermal paradox they create. The subducting slab is cold oceanic lithosphere, chilled at the seafloor for tens of millions of years, and it plunges downward faster than the surrounding mantle can heat it. The result is an **inverted geothermal gradient**: instead of temperature rising steadily with depth (the normal continental pattern), the slab interior remains anomalously cool even as it reaches depths where surrounding mantle rock is far hotter. This thermal disequilibrium is the engine behind the unusual metamorphic rocks found in subduction settings.

Under normal continental conditions, increasing depth means both increasing pressure and increasing temperature, producing familiar metamorphic sequences like greenschist to amphibolite facies. In a subduction zone, however, pressure increases rapidly with depth while temperature lags behind. This combination of **high pressure and relatively low temperature** stabilizes mineral assemblages that rarely form elsewhere. The signature rock is **blueschist**, named for the blue amphibole glaucophane that forms when basaltic oceanic crust is metamorphosed at pressures above roughly 0.6 GPa but temperatures below about 500°C. At even greater depths — beyond 1.5 GPa — the assemblage transforms into **eclogite**, a dense rock dominated by garnet and omphacite (a sodium-rich pyroxene). If you have studied metamorphic facies, you can place blueschist and eclogite on a pressure-temperature diagram and see how they occupy the upper-left quadrant: high pressure, low temperature, far from the normal geothermal gradient.

These metamorphic rocks are more than curiosities — they are recorders of the subduction process. Each mineral assemblage is stable only within a specific pressure-temperature window, so identifying the minerals in a subduction-zone rock tells you the depth and temperature conditions it experienced. By mapping the sequence of mineral assemblages and combining them with radiometric ages, geologists reconstruct **pressure-temperature-time (P-T-t) paths** that trace the trajectory of the slab as it descended. A classic P-T-t path for a blueschist shows rapid burial to high pressure at low temperature (the down-going leg), sometimes followed by heating and decompression as the rock is exhumed back toward the surface by tectonic processes like corner flow in the mantle wedge or buoyancy-driven return.

The survival of blueschist and eclogite at the surface is itself remarkable. These minerals are unstable at low pressures, and most subducted material never returns. The rocks we find in mountain belts — often in narrow, fault-bounded slivers called **mélange zones** — represent rare fragments that were scraped off the slab or squeezed back up along the subduction channel before they could be dragged to unreturnable depths. Their presence in an ancient mountain belt is diagnostic evidence that a subduction zone once operated there, making them essential markers for reconstructing past plate configurations.
