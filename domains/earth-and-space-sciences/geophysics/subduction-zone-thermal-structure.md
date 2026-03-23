---
id: subduction-zone-thermal-structure
title: Subduction Zone Thermal Structure and Metamorphism
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: subduction-zone-structure-and-dynamics
  type: hard
- id: conduction-models-crustal-heat
  type: hard
tags:
- subduction
- thermal
- metamorphism
- cold-slab
stage: expert
status: validated
---

# Subduction Zone Thermal Structure and Metamorphism

## Core Idea
Subducting slabs remain cold owing to rapid plate motion. Cold slab interiors inhibit melting; thermal models show geothermal gradients much lower in subduction zones than in the mantle wedge, explaining metamorphic facies and magma generation.

## Questions

```yaml
- question: "A student argues that a subducting oceanic slab should heat up quickly to ambient mantle temperatures (1200–1400°C) because the surrounding asthenosphere is very hot and rock is a reasonably good heat conductor. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — slabs do heat up quickly, which is why earthquakes are limited to shallow depths in subduction zones"
    - "Rock is actually a perfect thermal insulator, so no heat conduction occurs across the slab-mantle boundary"
    - "Plate subduction rates (5–10 cm/yr) are fast enough that the slab moves to depth faster than heat can diffuse inward — advection dominates over conduction, captured by a large thermal Peclet number"
    - "Mantle convection carries cold material downward faster than hot material rises, keeping mantle temperatures near subducting slabs artificially low"
  answer: 2
  explanation: "The key insight is the competition between two timescales: how fast heat diffuses inward (conduction) versus how fast the slab moves to depth (advection). At subduction rates of 5–10 cm/year, the slab descends hundreds of kilometers before heat has time to penetrate more than a few tens of kilometers into the slab interior. The thermal Peclet number — the ratio of advective to conductive heat transport — is large (>>1) for typical subduction parameters, meaning advection wins. The result is a cold slab interior that persists to depths of several hundred kilometers, creating the anomalously low-temperature geothermal gradients unique to subduction zones."

- question: "Volcanic arcs form approximately 100–120 km above the top surface of the subducting slab. What process at this depth triggers arc magmatism?"
  type: multiple-choice
  options:
    - "The slab reaches temperatures high enough to partially melt directly, and this melt rises to form arc volcanoes"
    - "Frictional heating along the subduction fault at 100 km depth melts the overlying mantle wedge directly"
    - "Hydrous minerals in the subducting slab dehydrate at this depth, releasing water that rises into the hot mantle wedge and lowers the peridotite melting point, triggering flux melting"
    - "The weight of 100 km of overriding crust creates enough pressure to squeeze melt upward from the slab"
  answer: 2
  explanation: "Arc magmatism is driven by flux melting, not direct slab melting. The subducting oceanic crust contains hydrous minerals (amphibole, serpentine, chlorite) that are stable only up to certain pressure-temperature conditions. As the slab descends and heats, these minerals break down and release water. This water rises buoyantly into the overlying mantle wedge — which is hot (1200°C+) peridotite. Water dramatically lowers the solidus (melting temperature) of peridotite, causing flux melting at temperatures well below dry peridotite's melting point. The 100–120 km arc-trench gap reflects the depth at which the last major hydrous phases in the slab decompose."

- question: "Blueschist facies metamorphism — characterized by high pressure and low temperature — is uniquely associated with subduction zone settings and is not found at equivalent depths elsewhere in the crust."
  type: true-false
  answer: true
  explanation: "Blueschist facies requires a geothermal gradient far lower than found anywhere in normal continental or oceanic crust — roughly 5–15°C/km, compared to the 25–30°C/km typical of most crustal settings. This extreme cold-geotherm path is only achieved along the top surface of a rapidly subducting slab, where cold oceanic crust is being carried to depth faster than it can heat up. The resulting high-pressure, low-temperature conditions stabilize the blue amphibole glaucophane — the mineral that gives blueschists their characteristic color and their name. Fossilized blueschist belts exposed at the surface are direct records of ancient subduction zones."

- question: "Old, cold, fast-subducting oceanic slabs dehydrate at shallower depths than young, warm, slow-subducting slabs because their lower temperatures keep them cold longer."
  type: true-false
  answer: false
  explanation: "This is the opposite of what occurs. Old, cold, fast-subducting slabs retain their cold cores to much greater depths precisely because they are cold and moving quickly — the large thermal Peclet number keeps the slab interior cold far into the mantle. Their hydrous minerals therefore persist to greater depths before the slab surface heats enough to cause dehydration. Young, warm, slow-subducting slabs have a smaller Peclet number — they heat up more rapidly relative to their descent rate — and therefore dehydrate at shallower depths. This is why the Cascadia subduction zone (young Juan de Fuca plate, slow subduction) shows dehydration signatures at shallower depths than the Japan subduction zone (old Pacific plate, fast subduction)."

- question: "Why do subducting slabs remain cold far into the mantle despite being surrounded by hot asthenosphere? Explain using the concept of the thermal Peclet number."
  type: short-answer
  answer: "The thermal Peclet number (Pe) is the ratio of advective heat transport (governed by plate velocity) to conductive heat transport (governed by thermal diffusivity and length scale). For subduction, Pe = vL/κ, where v is the subduction velocity, L is the relevant length scale (slab thickness), and κ is the thermal diffusivity of rock. For typical subduction parameters (v ~ 5–10 cm/yr, L ~ 50 km, κ ~ 10⁻⁶ m²/s), Pe >> 1, meaning the plate moves to depth far faster than heat can diffuse inward. The slab interior behaves like the center of the frozen metal bar analogy: even as the surface heats up from contact with the hot mantle, the core remains cold because conduction cannot keep pace with the rate of descent. This keeps slab interiors cold to depths of hundreds of kilometers, producing the anomalously cold geothermal gradients that define subduction zone metamorphism."
  explanation: "The Peclet number framework is powerful because it makes the competition between advection and conduction explicit and quantitative. It explains why faster subduction produces colder slabs (higher Pe → less heating), why thicker slabs stay colder longer (larger L), and why different subduction zones worldwide have such different thermal structures despite sharing the same basic geometry."
```

## Explainer

From your study of subduction zone dynamics, you know that oceanic lithosphere descends into the mantle at convergent boundaries. From crustal heat conduction models, you know that temperature distribution in the Earth is governed by the balance between heat sources, conduction, and advection. Subduction zone thermal structure brings these together: the descending slab carries cold oceanic lithosphere into the hot mantle, creating one of the most dramatic thermal contrasts anywhere in the Earth's interior.

The key to understanding why slabs stay cold is the competition between **heat conduction** and **plate velocity**. Heat conducts into the slab from the surrounding hot mantle, but the slab is moving downward faster than heat can diffuse inward. Think of sliding a frozen metal bar through a furnace — if you push it fast enough, the interior remains cold even as the surface heats up. The dimensionless number that captures this competition is the **thermal Peclet number**: the ratio of advective heat transport (plate motion) to conductive heat transport. For typical subduction rates of 5–10 cm/year, the Peclet number is large, meaning advection dominates and the slab interior stays cold to depths of several hundred kilometers.

The thermal structure of a subduction zone is not a simple temperature gradient — it has a distinctive two-dimensional pattern. The slab surface heats up progressively as it descends, reaching temperatures where hydrous minerals in the altered oceanic crust break down and release water. This dehydration produces a sequence of **metamorphic facies** along the slab surface: from zeolite and prehnite-pumpellyite facies at shallow depths, through blueschist facies (the hallmark of high-pressure, low-temperature conditions unique to subduction zones), to eclogite facies at greater depths where all hydrous phases have decomposed. The water released from the slab rises into the hot **mantle wedge** — the triangular region of mantle between the slab surface and the overlying plate — where it lowers the melting point of peridotite, triggering **flux melting**. This is the primary mechanism generating arc magmas, and it explains why volcanic arcs sit about 100–120 km above the slab surface: that is roughly the depth where the slab has heated enough to dehydrate its last major water-bearing minerals.

The thermal structure varies dramatically between subduction zones. Old, cold, fast-subducting slabs (like the Pacific plate beneath Japan) retain their cold cores to great depths and produce narrow, well-defined Wadati-Benioff seismic zones. Young, warm, slow-subducting slabs (like the Juan de Fuca plate beneath Cascadia) heat up more rapidly, dehydrate at shallower depths, and may lose their seismic signature before reaching 100 km depth. These differences have direct consequences for volcanic style, earthquake depth distribution, and the recycling of water and carbon into the deep mantle. Thermal modeling of subduction zones — solving the heat equation with realistic geometries, velocities, and rheologies — is therefore central to understanding why convergent margins behave so differently from one another around the globe.
