---
id: meteorites-and-planetary-samples
title: Meteorites as Planetary Samples
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: asteroids-composition-and-properties
  type: soft
- id: comets-structure-and-composition
  type: soft
- id: radiometric-dating
  type: hard
- id: planetary-differentiation
  type: soft
tags:
- meteorites
- samples
- dating
stage: expert
status: validated
---

# Meteorites as Planetary Samples

## Core Idea
Meteorites are solid fragments from planets, asteroids, moons, and comets that reach planetary surfaces; their mineralogy, isotope ratios (U-Pb, Ar-Ar), and noble-gas contents reveal accretion ages, parent-body thermal histories, and impact events. Meteorite groups (chondrites, achondrites, irons) sample distinct solar system bodies and processes.

## Questions

```yaml
- question: "Why does the bulk elemental composition of chondrite meteorites closely match that of the Sun (excluding volatile gases)?"
  type: multiple-choice
  options:
    - "Chondrites formed from material ejected by the Sun during early solar activity and retain its composition"
    - "Chondrites come from parent bodies that never underwent melting or differentiation, preserving the original solar nebula composition"
    - "Chondrites formed last in the solar system after heavier elements had settled, concentrating the same elements as the Sun's photosphere"
    - "The match is coincidental; chondrites are too old to have a compositional relationship with the current Sun"
  answer: 1
  explanation: "Chondrites are primitive — their parent bodies never became hot enough to melt and differentiate into layers. Because differentiation is the process that separates iron from silicates and concentrates certain elements in different reservoirs, undifferentiated bodies preserve the original mix of condensed solids from the solar nebula. That primordial mix reflects the solar composition (the source of all the material), minus gases like hydrogen and helium that escaped. This is why chondrites serve as the baseline 'solar' composition for planetary science."

- question: "A researcher finds a meteorite composed almost entirely of iron-nickel metal with trace silicate inclusions. Which process does this meteorite most likely sample?"
  type: multiple-choice
  options:
    - "A primitive undifferentiated body, because iron and nickel are the most abundant nebular condensates"
    - "A comet's rocky interior, which is enriched in heavy metals by cosmic ray processing"
    - "A differentiated body's metallic core, where iron-nickel separated from lighter silicates during large-scale melting"
    - "A fragment of the early Sun's convection zone, expelled during a flare event"
  answer: 2
  explanation: "Iron meteorites are fragments of the metallic cores of differentiated parent bodies — asteroids large enough to generate internal heat (from radioactive decay or impacts), causing global melting and gravitational separation of dense iron-nickel from lighter silicates. This makes iron meteorites the only direct samples we have of material equivalent to Earth's own inaccessible metallic core. Primitive undifferentiated bodies (chondrites) have mixed silicates and metal throughout, not nearly pure iron-nickel."

- question: "Meteorites are valuable to planetary scientists primarily because they provide direct samples of currently active asteroids and comets, supplementing spacecraft missions."
  type: true-false
  answer: false
  explanation: "Meteorites are valuable because they preserve a record of the EARLY solar system — not because they represent the present-day state of parent bodies. Most meteorite parent bodies became geologically inactive billions of years ago, preserving primordial compositions and structures that Earth's own rocks (continuously recycled by plate tectonics and weathering) destroyed long ago. The antiquity and primitive nature of meteorites is the key, not any connection to currently active bodies."

- question: "Calcium-aluminum-rich inclusions (CAIs) in chondrites have been U-Pb dated to approximately 4.567 billion years, making them the oldest known solid material to have formed in the solar system."
  type: true-false
  answer: true
  explanation: "CAIs are high-temperature condensates that crystallized directly from the cooling solar nebula. Their uranium-lead ages of 4.567 Ga define the age of the solar system itself — the moment when solid material first formed from the presolar gas and dust cloud. All other solar system chronology (planet formation, core differentiation, late heavy bombardment) is measured relative to this benchmark. No other material of solar system origin has been dated to an earlier age."

- question: "Explain why Earth's own rocks cannot provide the same information about early solar system history that meteorites can."
  type: short-answer
  answer: "Earth is geologically active: plate tectonics continuously recycles crustal rocks into the mantle, and weathering destroys surface materials. The oldest Earth rocks are only about 4.0 billion years old, and the oldest mineral grains (zircons) reach about 4.4 billion years — leaving the first 150+ million years of Earth history unsampled. More importantly, Earth differentiated early, mixing and destroying the primitive solar nebula composition. Meteorite parent bodies — mostly small asteroids — formed in the first few million years, then became geologically inactive and have preserved their primordial compositions ever since, recording the solar system's first solid materials, the timing of differentiation events, and impact histories that Earth has completely erased."
  explanation: "This contrast between dynamic Earth and static small bodies is fundamental to planetary science. It explains why we study meteorites despite having abundant Earth rocks: the very processes that make Earth habitable (plate tectonics, volcanism, weathering) also destroy the ancient record. The asteroid belt acts as a museum of the early solar system, with meteorites as its exhibits."
```

## Explainer

Most of what we know about the earliest history of the solar system comes not from telescopes or spacecraft, but from rocks that fall to Earth. **Meteorites** are fragments of asteroids, moons, and even other planets that survive passage through the atmosphere and land on the surface. Because many of these parent bodies formed in the first few million years of the solar system and have remained geologically dead ever since, meteorites preserve a chemical and isotopic record that Earth's own rocks — constantly recycled by plate tectonics and weathering — long ago destroyed.

The classification of meteorites into major groups directly reflects the degree of processing their parent bodies underwent. **Chondrites**, the most primitive group, contain millimeter-scale spherules called chondrules that crystallized from molten droplets in the solar nebula. They have never been melted or differentiated into layers, so their bulk composition closely matches that of the Sun (minus volatile gases). **Achondrites**, by contrast, come from bodies large enough that internal heating caused melting and differentiation — they resemble terrestrial igneous rocks and include samples knocked off the surfaces of Mars and the Moon by giant impacts. **Iron meteorites** are fragments of the metallic cores of differentiated bodies, directly sampling material equivalent to Earth's inaccessible core.

The radiometric dating techniques you studied earlier are the primary tool for extracting age information from these samples. Uranium-lead dating of calcium-aluminum-rich inclusions (CAIs) in chondrites yields ages of 4.567 billion years — the benchmark age of the solar system itself. Argon-argon dating reveals when a sample last cooled through a critical temperature, recording impact events or thermal metamorphism on the parent body. Together, these chronometers let scientists reconstruct a timeline of accretion, differentiation, and bombardment that no single planetary body preserves on its own.

Noble gases trapped in meteorites add another dimension. Because noble gases are chemically inert, they are retained in mineral lattices and record exposure to cosmic rays during the meteorite's journey through space, the composition of the early solar wind, and even the atmospheric composition of Mars (trapped in shock-melted glass in Martian meteorites). Each meteorite is thus a multi-layered archive: its mineralogy records the parent body's geology, its isotopes record its age and thermal history, and its trapped gases record its journey and environment. Collectively, meteorites give us a ground-truth sample library for the solar system that complements the remote observations from asteroid and comet studies.
