---
id: geochemical-cycles-planets
title: Geochemical Cycles and Element Redistribution
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-differentiation
  type: hard
tags:
- geochemistry
- cycles
- element-distribution
stage: expert
status: draft
---

# Geochemical Cycles and Element Redistribution

## Core Idea
Planetary geochemical cycles redistribute elements between core, mantle, crust, atmosphere, and hydrosphere through volcanism, weathering, and outgassing. Incompatible elements preferentially concentrate in the crust; siderophile elements partition into the core. Comparing geochemical cycles across planets reveals how planetary size, composition, and thermal history shape element cycling and atmospheric composition.

## How It's Best Learned
Compare elemental abundances across terrestrial planets. Use partition coefficients to model core-mantle differentiation.

## Common Misconceptions
- Geochemical cycles are independent across planets; they are coupled—volcanic outgassing responds to interior cooling rates.
- Element distributions are static; they change over planetary evolution as cooling rates and outgassing patterns shift.

## Questions

```yaml
- question: "A planet has completely cooled — its interior is no longer hot enough to drive volcanism. Which statement best describes the fate of its geochemical cycles?"
  type: multiple-choice
  options:
    - "Cycles continue uninterrupted via surface weathering alone"
    - "Geochemical cycling effectively halts because volcanism is the primary engine redistributing elements between interior reservoirs and the surface"
    - "Weathering accelerates to compensate for the lost volcanic input, maintaining the same cycling rate"
    - "The crust-to-mantle cycle is unaffected because element partitioning depends on gravity rather than heat"
  answer: 1
  explanation: "Volcanism drives the redistribution of incompatible and volatile elements from the mantle to the crust and atmosphere (outgassing). Once the interior cools and volcanism stops, this primary engine shuts down. Surface weathering can still operate but it cannot return volatiles to the interior without subduction, and it cannot regenerate the volcanic outputs that replenish the atmosphere. Mars is the canonical example: as its interior cooled and volcanism waned, volatile outgassing slowed dramatically and its atmosphere thinned."

- question: "Platinum-group metals (PGMs) are extremely rare in Earth's crust despite being present in the solar system at moderate abundances. What is the primary reason?"
  type: multiple-choice
  options:
    - "PGMs were destroyed by heat during the early solar system before Earth formed"
    - "Being siderophile (iron-loving) elements, they partitioned preferentially into Earth's metallic core during differentiation"
    - "Weathering dissolved them from the crust into the deep ocean billions of years ago"
    - "They are incompatible elements that never concentrated in any single reservoir"
  answer: 1
  explanation: "Siderophile elements have a chemical affinity for metallic iron and preferentially partitioned into the iron core during planetary differentiation. This is why the platinum-group metals — despite being astrophysically present — are depleted in the mantle and crust. The contrast with lithophile elements (which concentrate in the silicate crust) illustrates how chemical affinity, not just abundance, controls where elements end up. The study of siderophile depletion patterns in Earth's mantle is actually one way geochemists infer the conditions of core formation."

- question: "On a planet without plate tectonics, volcanic outgassing transfers volatiles from the mantle to the atmosphere in essentially one direction only."
  type: true-false
  answer: true
  explanation: "On a one-plate planet like Mars or Venus, there is no subduction to return crustal and atmospheric material back into the mantle. Volcanism can still deliver volatiles upward, but without the return path that subduction provides on Earth, the transfer is largely one-directional. Over time, the mantle progressively loses its volatiles to the crust and atmosphere without replenishment — contributing to Mars's declining volcanic activity and atmospheric thinning over geological time."

- question: "Earth's long-term atmospheric CO₂ levels are controlled primarily by the balance between volcanic outgassing and biological photosynthesis, with silicate weathering playing only a minor role."
  type: true-false
  answer: false
  explanation: "Silicate weathering is actually the dominant long-term CO₂ regulator on Earth. Chemical weathering of silicate rocks consumes atmospheric CO₂ and delivers dissolved ions (including Ca²⁺) to the ocean, where they are buried as carbonate sediments — effectively locking up CO₂ for millions of years. This weathering-carbonate cycle is the primary thermostat that has kept Earth's climate habitable over geological time. The comparison with Venus (which lacks liquid water and therefore this weathering feedback) helps explain Venus's runaway CO₂ greenhouse: without weathering to remove it, volcanic CO₂ accumulates indefinitely."

- question: "Why does the presence or absence of plate tectonics fundamentally change the nature of a planet's geochemical cycles? What does subduction make possible that a one-plate planet cannot achieve?"
  type: short-answer
  answer: "Plate tectonics enables bidirectional cycling: subduction carries crustal material, sediments, and volatiles back into the mantle, closing the loop. On a one-plate planet, volcanism can transfer elements from interior to surface/atmosphere, but there is no return pathway. Subduction specifically makes the long-term carbon cycle possible (returning carbonate sediments to the mantle, where CO₂ is eventually re-released via volcanism) and recycles water and other volatiles back into the mantle. Without subduction, the system runs down: the mantle depletes in volatiles, volcanism wanes, and the atmosphere receives no new volcanic input."
  explanation: "This distinction between one-way and cyclic geochemical processes is the key to understanding why Earth's volatile budget has been maintained over 4 billion years while Mars has progressively lost its volatiles. Earth's cycles are driven by the engine of plate tectonics keeping material circulating between the interior and surface; Mars's cycles are more like a leaking bucket."
```

## Explainer

From your study of planetary differentiation, you know that early in a terrestrial planet's history, heat from accretion and radioactive decay melts the interior, allowing dense metallic iron to sink toward the center and lighter silicates to float upward. This one-time separation creates the fundamental layered structure — core, mantle, crust — but it is not the end of the story. **Geochemical cycles** are the ongoing processes that continue to redistribute elements between these reservoirs over the lifetime of a planet, and comparing these cycles across worlds reveals how planetary size and thermal history control a planet's chemical evolution.

The key concept is **element partitioning**: different elements have chemical affinities that cause them to preferentially concentrate in certain reservoirs. **Siderophile** elements (iron-loving, such as nickel, cobalt, and the platinum-group metals) partition strongly into the metallic core during differentiation and are therefore depleted in the crust and mantle. **Lithophile** elements (rock-loving, such as potassium, uranium, and the rare earth elements) prefer silicate phases and concentrate in the crust. **Incompatible** elements — those whose ionic radius or charge makes them poor fits in common mantle minerals — are progressively extracted from the mantle into the crust with each episode of partial melting and volcanism. Over billions of years, this one-way transfer enriches the crust in elements like potassium, thorium, and uranium while depleting the mantle.

**Volcanism** is the primary engine driving geochemical cycles on terrestrial planets. When mantle rock partially melts, the resulting magma carries incompatible and volatile elements upward, delivering them to the crust and atmosphere through eruptions and **outgassing**. On Earth, this volcanic output is balanced by **subduction**, which returns crustal and sedimentary material back into the mantle, creating a true cycle. On one-plate planets like Mars and Venus, there is no subduction, so the transfer is largely one-directional: the mantle progressively loses its volatile and incompatible elements to the crust and atmosphere without significant return. This difference has profound consequences — Mars's mantle is thought to have become substantially depleted in water and other volatiles over time, contributing to the decline of volcanic activity and the thinning of its atmosphere.

**Weathering** adds another dimension on planets with atmospheres and hydrospheres. On Earth, chemical weathering of silicate rocks consumes atmospheric CO₂ and delivers dissolved ions to the ocean, where they are eventually buried as carbonate sediments — closing the long-term **carbon cycle** and regulating climate over millions of years. Venus, despite its dense CO₂ atmosphere, lacks liquid water and therefore lacks this weathering feedback, which may partly explain its runaway greenhouse state. Comparing geochemical cycles across the terrestrial planets — Earth's active, bidirectional cycling versus Mars's diminishing one-way degassing versus Venus's atmosphere-dominated system — demonstrates that a planet's size (which controls how long the interior stays hot enough for volcanism), its distance from the Sun (which governs surface temperature and the stability of liquid water), and its tectonic style collectively determine how elements are distributed and how atmospheres evolve over geological time.
