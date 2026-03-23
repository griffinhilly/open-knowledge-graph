---
id: exoplanet-mass-radius-relation
title: Exoplanet Mass-Radius Relations and Interior Composition
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: exoplanet-characterization-spectroscopy
  type: hard
- id: exoplanet-detection-methods
  type: hard
tags:
- exoplanets
- mass-radius
- composition
- interior-structure
stage: expert
status: draft
---

# Exoplanet Mass-Radius Relations and Interior Composition

## Core Idea
The mass-radius relation of exoplanets constrains internal composition, mantle mineralogy, and the presence of volatile-rich envelopes. Terrestrial exoplanets follow a tight sequence; super-Earths and mini-Neptunes show diversity indicating varied compositions (rocky, water-rich, or gas-dominated). Combined with atmospheric characterization, mass-radius measurements infer whether planets are terrestrial, ocean worlds, or mini-Neptunes.

## Questions

```yaml
- question: "A newly discovered planet has 5 Earth masses but a radius of 2.5 Earth radii — much larger than expected for a rocky body of that mass. What does this imply about its composition?"
  type: multiple-choice
  options:
    - "It must have a large iron core, which inflates the radius at high mass"
    - "It contains substantial lower-density material, such as water ice or a hydrogen-helium envelope"
    - "The measurement must be wrong — more massive planets are always denser due to gravitational compression"
    - "It is a rocky super-Earth; the super-Earth range spans 2–5 Earth masses regardless of density"
  answer: 1
  explanation: "Planets that plot above the rocky sequence on the mass-radius diagram are less dense than pure rock and must therefore contain lighter material. More iron would make the planet denser, not less (option A is backwards). Option C confuses the compression effect — rocky planets do get denser with mass, but a planet above the rocky sequence is an outlier in the direction of low density, not high. Option D confuses the mass range label with compositional inference."

- question: "The Fulton gap (radius gap) is a deficit of planets between about 1.5 and 2.0 Earth radii. What process best explains this gap?"
  type: multiple-choice
  options:
    - "Planets cannot form at these sizes due to orbital resonance effects in protoplanetary disks"
    - "The rocky planet sequence predicts no stable configurations at these radii"
    - "Planets with thin hydrogen-helium envelopes lose them to stellar radiation, shrinking to bare rocky cores; those with thick enough envelopes remain puffy mini-Neptunes"
    - "Water worlds at these sizes evaporate their oceans, collapsing to smaller radii over billions of years"
  answer: 2
  explanation: "The gap results from atmospheric mass loss: photoevaporation and core-powered mass loss strip thin hydrogen envelopes from planets close to their host stars. Planets that started with modest envelopes lose them and shrink below ~1.5 R⊕; those with thick envelopes retain them and stay above ~2.0 R⊕. The gap is not a formation artifact (option A) or a theoretical prediction from the rocky sequence (option B). Water loss (option D) is a separate process and does not produce the sharp radius gap observed."

- question: "Two exoplanets have identical masses and identical radii, giving them the same bulk density. They must therefore have the same interior composition."
  type: true-false
  answer: false
  explanation: "This is the degeneracy problem in mass-radius interpretation. Different mixtures of materials — for example, a water-rich planet versus a rocky planet with a thin gas envelope — can produce the same bulk density. Mass and radius constrain average density, but density alone cannot distinguish between multiple compositional models. Breaking this degeneracy requires additional data, typically atmospheric spectroscopy to determine whether a hydrogen-rich envelope or a water-dominated atmosphere is present."

- question: "Determining an exoplanet's bulk density requires both its radius (from transit observations) and its mass (from radial velocity or transit timing variations)."
  type: true-false
  answer: true
  explanation: "Transit observations measure the planet's radius from the fractional dimming of starlight. Radial velocity measurements measure the planet's mass from the gravitational wobble it induces in the star. Density = mass / volume, so both are required. Neither alone is sufficient: a transit gives radius but not mass, and a radial velocity signal gives mass but not radius. When both measurements are available for the same planet, bulk density can be calculated, enabling compositional inferences."

- question: "Explain the degeneracy problem in exoplanet interior modeling. Why can't bulk density alone uniquely determine a planet's composition?"
  type: short-answer
  answer: "Bulk density is a single number — the average of all the materials inside the planet — and multiple combinations of materials can yield the same average. For instance, a planet made mostly of water ice and a planet made of rock plus a thin hydrogen atmosphere can have the same total mass, the same radius, and therefore the same density. Without knowing which layers are present and in what proportions, the interior is underdetermined. Breaking the degeneracy requires additional constraints, such as atmospheric composition from spectroscopy, which can reveal whether a hydrogen envelope or a water-vapor-dominated atmosphere is present."
  explanation: "The degeneracy problem is what makes the mass-radius diagram necessary but not sufficient for compositional inference. It also motivates combining transit spectroscopy (atmospheric chemistry) with mass-radius measurements. The degeneracy is worst in the super-Earth to mini-Neptune range (~1.5–4 R⊕), where rocky, water-rich, and gas-enveloped planets can overlap substantially."
```

## Explainer

From your study of exoplanet detection methods, you know that transit observations yield a planet's radius (from how much starlight it blocks) and radial velocity measurements yield its mass (from the gravitational wobble it induces in its star). When you have both measurements for the same planet, you can calculate its **bulk density** — and density is the key that unlocks interior composition. A dense planet must be made primarily of rock and metal; a low-density planet must contain substantial amounts of lighter material like water ice, hydrogen, or helium. The **mass-radius relation** is the systematic pattern that emerges when you plot thousands of exoplanets on a mass-versus-radius diagram.

For purely rocky planets — those made of iron cores and silicate mantles like Earth, Venus, and Mars — physics predicts a tight relationship between mass and radius. As you add mass to a rocky body, gravity compresses the interior, so radius increases more slowly than you might expect. A planet twice Earth's mass is only about 1.25 times Earth's radius if it has the same composition. This **rocky planet sequence** forms a well-defined curve on the mass-radius diagram, and planets that fall on or near it are confidently classified as terrestrial. Planets that plot above this curve — larger than expected for their mass — must contain lower-density material.

The most intriguing region of the mass-radius diagram is the **super-Earth to mini-Neptune transition**, spanning roughly 1.5 to 4 Earth radii and 2 to 20 Earth masses. Here, planets with similar masses can have dramatically different radii, revealing fundamentally different compositions. A planet of 5 Earth masses might be a rocky super-Earth with radius 1.5 R⊕, a **water world** with a deep ocean or high-pressure ice mantle at 2 R⊕, or a **mini-Neptune** with a thick hydrogen-helium envelope at 2.5 R⊕. The mass-radius measurement alone cannot always distinguish between these possibilities — this is the **degeneracy problem**, where different interior structures can produce the same bulk density. Breaking this degeneracy requires atmospheric characterization from spectroscopy, which can reveal whether a planet has a hydrogen-rich envelope, a water-dominated atmosphere, or a thin rocky-planet atmosphere.

A striking observational finding is the **radius gap** (also called the Fulton gap) — a deficit of planets between about 1.5 and 2.0 Earth radii. This gap separates bare rocky super-Earths below from gas-enveloped mini-Neptunes above, and is thought to result from **atmospheric mass loss**: planets that formed with thin hydrogen envelopes lose them to stellar radiation (photoevaporation) or internal heat (core-powered mass loss) if the envelope is not massive enough to resist stripping. Planets that retain their envelopes remain puffy mini-Neptunes; those that lose them shrink to bare rocky cores. The mass-radius relation thus encodes not just present-day composition but the entire history of atmospheric evolution — connecting planet formation, stellar irradiation, and interior physics into a unified picture of planetary diversity.
