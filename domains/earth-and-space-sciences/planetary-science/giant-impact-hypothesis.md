---
id: giant-impact-hypothesis
title: Giant Impact Hypothesis and Lunar Formation
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-differentiation
  type: hard
- id: impact-cratering-mechanics
  type: soft
- id: collision-analysis-applications
  type: soft
- id: conservation-of-momentum
  type: soft
builds-toward:
- tidal-orbital-evolution-long-term
- thermal-evolution-terrestrial-planets
tags:
- moon
- giant-impact
- early-solar-system
- angular-momentum
stage: expert
status: draft
---

# Giant Impact Hypothesis and Lunar Formation

## Core Idea
The Moon likely formed from a giant collision between the proto-Earth and a Mars-sized body around 4.5 Ga. This impact explains the Moon's mass, orbital parameters, and the Earth-Moon system's high angular momentum. Isotopic similarities between the Moon and Earth support this origin rather than Earth capture or co-accretion.

## Questions

```yaml
- question: "Why does the giant impact hypothesis predict that the Moon has very little iron, despite forming from a collision between two iron-containing bodies?"
  type: multiple-choice
  options:
    - "The impactor Theia was iron-poor to begin with, unlike rocky planets with differentiated iron cores"
    - "The iron cores of both Theia and proto-Earth merged into the resulting Earth; the ejected debris came predominantly from the silicate mantles"
    - "Iron is too dense to be ejected into orbit during any planetary collision and dispersed into space instead"
    - "The Moon's iron was lost over time through volcanic outgassing during the early lunar period"
  answer: 1
  explanation: "Both proto-Earth and Theia had already differentiated — iron cores surrounded by silicate mantles — before the collision. During the impact, the dense metallic cores merged and were retained by the proto-Earth rather than being launched into orbit. The high-velocity ejecta that formed the Moon-forming disk came predominantly from the silicate mantles of both bodies. This explains the Moon's iron depletion (~1–2% of mass vs. Earth's ~32%) without invoking any special chemistry in Theia."

- question: "A planetary scientist discovers a moon of a distant exoplanet with oxygen isotope ratios identical to the planet, only ~2% iron content by mass, and the planet-moon system has anomalously high total angular momentum. Which formation model does this combination of evidence most strongly support?"
  type: multiple-choice
  options:
    - "Co-accretion: moon and planet formed side by side from the same protoplanetary disk material"
    - "Capture: the planet gravitationally snared a passing body from another region of the solar system"
    - "Giant impact: a large body struck the planet, ejecting iron-poor mantle material into orbit"
    - "Fission: the planet's rapid early rotation flung off a portion of its outer layers"
  answer: 2
  explanation: "The combination of clues is diagnostic. Identical oxygen isotopes rules out capture (a foreign body would have a distinct isotopic signature). Iron depletion points to mantle-dominated ejecta — exactly what the giant impact predicts, since cores merge rather than launching into orbit. High angular momentum is naturally explained by a glancing impact transferring momentum. Co-accretion could produce similar isotopes but doesn't naturally explain iron depletion or high angular momentum. Fission requires implausibly fast initial rotation. Only the giant impact simultaneously accounts for all three observations."

- question: "The giant impact hypothesis predicts that lunar rocks should have oxygen isotope ratios similar to meteorites from the outer solar system, since Theia likely originated beyond the snow line before drifting inward."
  type: true-false
  answer: false
  explanation: "False. The giant impact hypothesis actually predicts near-identical oxygen isotope ratios between Earth and the Moon — which is precisely what Apollo samples confirmed. Oxygen isotopes vary measurably between different bodies in the solar system; Mars, asteroid parent bodies, and Earth each have distinct signatures. The hypothesis succeeds partly because models where Theia's material thoroughly mixes with Earth's mantle before the debris disk condenses naturally produce isotopic homogeneity. Similarity to outer-solar-system meteorites would actually contradict the hypothesis."

- question: "In the giant impact scenario, the Moon-forming debris disk is composed primarily of material from the silicate mantles of both colliding bodies, because dense metallic cores merge rather than being ejected into orbit."
  type: true-false
  answer: true
  explanation: "True. By 4.5 Ga, both proto-Earth and Theia had differentiated into iron cores and silicate mantles. During the collision, the iron cores — being much denser — merged gravitationally into the resulting Earth rather than being launched into orbit. The material with sufficient velocity to escape into a circumplanetary disk was predominantly the less-dense silicate mantle material. This prediction matches observation: the Moon's iron core is only ~1–2% of its mass, compared to ~32% for Earth."

- question: "What evidence from Apollo lunar samples most directly distinguishes the giant impact hypothesis from the capture hypothesis, and why does that evidence favor giant impact?"
  type: short-answer
  answer: "Apollo samples show lunar rocks have oxygen isotope ratios virtually identical to Earth rocks. The capture hypothesis predicts a body from another region of the solar system would carry a distinct oxygen isotope signature — different bodies in the solar system have measurably different ratios (Mars, asteroid parent bodies, and Earth all differ). Identical lunar and terrestrial ratios indicate the Moon formed from material already in Earth's orbital region, consistent with giant impact and inconsistent with capture of a foreign body."
  explanation: "Oxygen isotopes act as a geochemical address: where in the solar system material condensed determines its isotopic ratio. If the Moon had been captured, it should look isotopically foreign. Instead it looks like Earth. This also eliminates most simple co-accretion scenarios unless the disk was thoroughly mixed. The isotopic evidence combined with the Moon's iron depletion and the system's high angular momentum creates a constraint set that only the giant impact model satisfies simultaneously."
```

## Explainer

The Moon is anomalous. It is far too large relative to its host planet — about 1/81 of Earth's mass — to be a typical captured asteroid, and its orbital properties and composition pose puzzles that simpler formation models cannot resolve. Your understanding of planetary differentiation tells you that by the time of the hypothesized impact (~4.5 billion years ago), the proto-Earth had already separated into an iron core and a silicate mantle. The Moon, strikingly, has a tiny iron core — only about 1–2% of its mass compared to Earth's ~32%. Any formation model must explain this iron depletion, along with the Moon's bulk composition, the angular momentum of the Earth-Moon system, and the near-identical oxygen isotope ratios between Earth and lunar samples.

The **giant impact hypothesis** proposes that a Mars-sized body — often called **Theia** — struck the proto-Earth in a glancing collision at roughly 4.5 Ga. Your knowledge of conservation of momentum helps here: a glancing impact transfers enormous angular momentum to the system, explaining why the Earth-Moon system has an unusually high total angular momentum. The collision was energetic enough to partially vaporize both bodies, ejecting a disk of superheated silicate debris into orbit around the proto-Earth. This debris disk, drawn predominantly from the mantles of both Theia and the proto-Earth (since dense iron cores would have merged rather than being launched into orbit), then accreted to form the Moon. This neatly explains why the Moon is iron-poor: the disk material was mostly silicate mantle, not metallic core.

The strongest evidence favoring the giant impact over competing hypotheses — co-accretion (Earth and Moon forming side by side from the same material) and capture (Earth gravitationally snaring a passing body) — comes from **isotopic geochemistry**. Oxygen isotopes vary measurably between different bodies in the solar system: Mars, meteorite parent bodies, and Earth each have distinct oxygen isotope signatures. Yet lunar samples returned by the Apollo missions have oxygen isotope ratios virtually identical to Earth's. Co-accretion could potentially explain this similarity, but it fails to account for the Moon's iron depletion and the system's angular momentum. Capture would predict a distinctly different isotopic signature. The giant impact, particularly in models where the impactor's material thoroughly mixes with Earth's mantle before the Moon-forming disk condenses, naturally produces isotopic homogeneity.

Modern computational simulations using **smoothed particle hydrodynamics** (SPH) have refined the hypothesis significantly. Early models required Theia to strike at a specific angle and velocity, and they tended to produce a Moon composed mostly of Theia's material — which would predict isotopic differences from Earth, not similarities. More recent models explore scenarios including a higher-energy impact that completely vaporizes both bodies into a mixed "synestia" (a donut-shaped cloud of rock vapor), or a smaller, faster impactor. These variants better reproduce the observed isotopic similarity by ensuring thorough mixing. The giant impact hypothesis remains the leading model for lunar origin, but the details of the impact geometry and the physics of disk-to-Moon accretion are still active areas of research.
