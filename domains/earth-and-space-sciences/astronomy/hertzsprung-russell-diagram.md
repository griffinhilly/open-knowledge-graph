---
id: hertzsprung-russell-diagram
title: The Hertzsprung-Russell Diagram
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: stellar-spectral-classification
  type: hard
- id: stellar-properties-luminosity-temperature
  type: hard
- id: blackbody-radiation
  type: soft
- id: logarithms-intro
  type: soft
builds-toward:
- stellar-nucleosynthesis
- stellar-evolution-main-sequence-to-giant
- stellar-end-states
tags:
- HR-diagram
- main-sequence
- giant-branch
- white-dwarfs
- supergiants
- mass-luminosity-relation
stage: advanced
status: validated
---

# The Hertzsprung-Russell Diagram

## Core Idea
The Hertzsprung-Russell diagram plots stellar luminosity (y-axis) against surface temperature or spectral type (x-axis, with hot stars on the left). Most stars occupy the main sequence — a diagonal band from hot luminous blue stars to cool dim red dwarfs — where hydrogen fusion powers them in hydrostatic equilibrium. Giant and supergiant branches extend to the upper right; white dwarfs cluster at the lower left. A star's position encodes its mass, age, and evolutionary stage. The main sequence is fundamentally a mass sequence: massive stars are hotter and more luminous, with lifetimes scaling roughly inversely with mass squared.

## How It's Best Learned
Plot a sample of real stars on an HR diagram and identify the main sequence, giant branch, and white dwarf region. Trace evolutionary tracks for stars of different masses to understand what happens as they exhaust their hydrogen fuel.

## Common Misconceptions
- Stars do not travel along the main sequence as they age — a star maintains roughly the same position until core hydrogen is exhausted, then rapidly evolves to the giant branch.
- The x-axis is reversed relative to normal convention: temperature decreases from left to right.

## Questions

```yaml
- question: "A Sun-like star has been on the main sequence for about 4 billion years. How has its position on the HR diagram changed during this time?"
  type: multiple-choice
  options:
    - "It has slowly moved from the lower right toward the upper left as it converted hydrogen to helium and became hotter"
    - "It has remained at roughly the same position, determined by its birth mass, and will stay there until core hydrogen is exhausted"
    - "It has moved upward and rightward as it aged, gradually becoming a red giant over billions of years"
    - "It has moved leftward as its luminosity decreased due to fuel consumption"
  answer: 1
  explanation: "Stars do not travel along the main sequence as they age. A star's position on the main sequence is set by its birth mass and remains nearly fixed for most of its life while hydrogen fusion proceeds in the core. A Sun-like star spends about 10 billion years essentially stationary on the main sequence. Only when core hydrogen is nearly exhausted does the star evolve rapidly off the main sequence — expanding to become a red giant (moving to the upper right of the HR diagram). The common misconception that stars 'drift' along the main sequence confuses the population sequence (mass ordering) with an evolutionary track."

- question: "Two main-sequence stars are observed: Star A is at the upper left of the HR diagram, and Star B is at the lower right. Which statement best summarizes their relationship?"
  type: multiple-choice
  options:
    - "Star A is older and has evolved further along the main sequence than Star B"
    - "Star A is more massive, hotter, more luminous, and shorter-lived than Star B"
    - "Star A has more hydrogen fuel remaining because its greater luminosity is powered by more efficient fusion"
    - "Star B must be a white dwarf because it is cooler and less luminous"
  answer: 1
  explanation: "The main sequence is a mass sequence: more massive stars are hotter, more luminous, and larger, placing them at the upper left. But their greater luminosity comes at a steep cost — they burn through their hydrogen fuel much faster. A star 10× the Sun's mass is roughly 10,000× more luminous but lives only about 10 million years, vs the Sun's 10 billion. Star B (lower right) is a low-mass, cool, dim red dwarf that may survive for hundreds of billions of years. Position on the main sequence correlates with mass and lifetime, not age or evolutionary stage."

- question: "As a Sun-like star ages on the main sequence, it gradually slides leftward and upward, becoming hotter and more luminous over time."
  type: true-false
  answer: false
  explanation: "Stars do not 'slide' along the main sequence. A star maintains approximately the same position for the duration of its main-sequence lifetime, with only a slight and gradual increase in luminosity (the Sun has brightened about 30% since formation, a small displacement on the logarithmic scale). The main sequence is a mass sequence — each position on it corresponds to a star of a given mass during the hydrogen-burning phase — not a timeline that a single star traverses. The dramatic HR diagram evolution happens when the star *leaves* the main sequence: expanding rightward and upward to the giant branch, then eventually to white dwarf, neutron star, or supernova."

- question: "A red giant star can be far more luminous than a main-sequence star despite having a much lower surface temperature, because its enormous physical radius compensates in the luminosity formula L = 4πR²σT⁴."
  type: true-false
  answer: true
  explanation: "This is exactly correct and explains an otherwise paradoxical feature of the HR diagram. Red giants appear in the upper right — high luminosity, low temperature — which seems contradictory until you remember that L = 4πR²σT⁴. A red giant may have a surface temperature of ~4,000 K (much cooler than the Sun's ~5,800 K), but its radius may be 100 times the Sun's. The R² term dominates: (100)² = 10,000 × the Sun's surface area, more than compensating for the lower T⁴. Giant and supergiant stars are genuinely enormous physical objects, not merely hot ones."

- question: "Why is the main sequence described as a 'mass sequence' rather than an 'age sequence,' and what determines where on the main sequence a star will spend its life?"
  type: short-answer
  answer: "A star's position on the main sequence is determined almost entirely by its birth mass. More massive stars have more gravitational pressure, requiring higher core temperatures and fusion rates to maintain hydrostatic equilibrium, making them hotter and dramatically more luminous. The mass-luminosity relation (L ∝ M^~3.5–4) means a small increase in mass produces a large increase in luminosity. Every star of a given mass settles onto essentially the same main-sequence position regardless of when it formed — a 1 solar-mass star born today plots in the same place as one born 8 billion years ago. Age matters only insofar as it determines how much core hydrogen has been consumed, but the star won't visibly leave its main-sequence position until that fuel is nearly exhausted."
  explanation: "This is why plotting the HR diagram of a star cluster is so powerful: all stars in the cluster formed at the same time, so the point where stars have begun leaving the main sequence (the 'main sequence turnoff') directly reveals the cluster's age. Stars above the turnoff have already evolved off the main sequence; stars below it are still burning hydrogen. The main sequence is thus a mass sequence in cross-section but reveals age structure when you identify the turnoff."
```

## Explainer

The **Hertzsprung-Russell (HR) diagram** is the most important single plot in stellar astronomy. It takes two observable stellar properties — surface temperature (or equivalently spectral type, which you studied as a prerequisite) and luminosity — and plots one against the other for a population of stars. The result is not a random scatter but a highly structured pattern that reveals the physics of stellar structure and evolution. The convention is historically rooted: temperature *decreases* from left to right (hot blue stars on the left, cool red stars on the right), and luminosity increases upward on a logarithmic scale spanning many orders of magnitude.

The dominant feature is the **main sequence**, a diagonal band running from the upper left (hot, luminous blue stars) to the lower right (cool, dim red dwarfs). About 90% of all stars fall on this band at any given time, because the main sequence represents the longest-lived phase of stellar evolution: hydrogen fusion in the core. From your study of blackbody radiation, you know that a star's luminosity depends on both its surface temperature and its size (L = 4πR²σT⁴). Stars on the main sequence obey a tight **mass-luminosity relation**: more massive stars are hotter, larger, and dramatically more luminous. A star ten times the Sun's mass is roughly ten thousand times more luminous — but burns through its hydrogen fuel proportionally faster, living millions rather than billions of years. The main sequence is fundamentally a mass sequence, ordered from the most massive stars at the top left to the least massive at the bottom right.

Away from the main sequence, two other populations stand out. In the upper right corner sit the **giants and supergiants** — stars that are cool (red or orange) yet enormously luminous. They can be so luminous despite their low surface temperature only because they are physically enormous: a red giant might be 100 times the Sun's radius. These are evolved stars that have exhausted the hydrogen in their cores and expanded as hydrogen shell burning or helium core burning drives their envelopes outward. In the lower left sit the **white dwarfs** — stars that are hot yet very faint. They are faint because they are tiny, roughly Earth-sized, despite having masses comparable to the Sun. White dwarfs are stellar remnants: the exposed cores of stars that have shed their outer layers, slowly cooling with no fusion energy source.

A star does not slide along the main sequence as it ages. Instead, it sits at roughly one position on the main sequence (determined by its birth mass) for most of its life, then evolves *off* the main sequence when core hydrogen is exhausted — moving rightward and upward to the giant branch, and eventually leftward to the white dwarf region (for lower-mass stars) or exploding as a supernova (for the most massive). Tracing these **evolutionary tracks** on the HR diagram is how astronomers predict and interpret the life cycles of stars, connecting the snapshot of a stellar population to the underlying physics of nuclear fusion, gravitational contraction, and mass loss.
