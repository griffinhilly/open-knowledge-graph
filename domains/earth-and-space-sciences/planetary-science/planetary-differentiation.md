---
id: planetary-differentiation
title: Planetary Differentiation and Layering
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-interior-dynamics
  type: hard
- id: chemical-equilibrium
  type: soft
- id: gravitation
  type: soft
- id: heat-transfer-conduction-fourier
  type: soft
- id: density-and-buoyancy-fluids
  type: soft
- id: entropy-and-gibbs-free-energy
  type: soft
builds-toward:
- planetary-magnetic-field-generation
- planetary-tectonics-comparative
- meteorites-and-planetary-samples
tags:
- differentiation
- layering
- density
stage: advanced
status: draft
---

# Planetary Differentiation and Layering

## Core Idea
Planetary differentiation is the gravitational separation of materials by density, where dense metals (iron, nickel) sink to form a core and lighter silicates rise to form mantle and crust. This process releases gravitational potential energy that heats the planet and is recorded in meteorite compositions.

## How It's Best Learned
Compare meteorite types (iron, stony-iron, stony) with planetary layering models. Discuss why smaller bodies (asteroids, small moons) show incomplete differentiation while large planets fully differentiate.

## Common Misconceptions
- Differentiation happens instantly at planet formation.
- All asteroids are undifferentiated.
- Core composition is always identical across planets.

## Questions

```yaml
- question: "Which combination of energy sources was primarily responsible for generating the heat that allowed early Earth to differentiate?"
  type: multiple-choice
  options:
    - "Solar radiation absorbed at the surface, which gradually melted the interior over billions of years."
    - "Only long-lived radioactive isotopes like U-238 and Th-232, which have always been the dominant heat source."
    - "Gravitational potential energy released as dense material sank, plus decay of short-lived radioisotopes like Al-26."
    - "Tidal heating from the early Moon, similar to how Io is heated by Jupiter today."
  answer: 2
  explanation: "The early solar system contained abundant short-lived radioisotopes (especially Al-26, with a half-life of ~0.7 Myr) that released enormous heat before decaying away. Simultaneously, the energy released as dense iron sank through lighter silicates — converting gravitational potential energy to heat — provided additional melting. Together, these made wholesale differentiation possible within the first few tens of millions of years."

- question: "All asteroids in the solar system are undifferentiated primitive bodies that preserve the original composition of the solar nebula."
  type: true-false
  answer: false
  explanation: "Several asteroid parent bodies, including the Vesta-family and the parent bodies of iron meteorites, underwent differentiation. Iron meteorites are essentially the exposed cores of destroyed differentiated planetesimals. The existence of differentiated asteroids shows that even relatively small bodies can differentiate if they form early enough to contain sufficient Al-26."

- question: "Why do larger planets differentiate more completely than smaller bodies like asteroids?"
  type: short-answer
  answer: "Larger bodies accumulate more heat from accretion and radioactive decay, and their greater mass provides stronger gravitational driving for density separation. Crucially, they retain heat longer because they have a smaller surface-area-to-volume ratio, keeping the interior molten for millions of years while density sorting occurs. Smaller bodies cool too quickly for complete separation."
  explanation: "The surface-area-to-volume argument is key: a small asteroid radiates heat away faster relative to its volume and freezes solid before iron can fully sink. Large planets stay hot long enough for differentiation to go to completion. This is why small meteorite parent bodies show partial differentiation while Earth, Mars, and the Moon each have a distinct core, mantle, and crust."
```

## Explainer

Imagine dropping a handful of sand and marbles into a jar of honey and watching — over time — the marbles sink and the sand floats upward. Planetary differentiation is exactly this process, played out inside a molten young planet. When a rocky body grows large enough and gets hot enough that its interior melts, gravity takes over: dense materials (iron and nickel) sink toward the center while lighter silicates (the minerals that make up rock) rise toward the surface. The result is the layered structure we observe in Earth and other planets — metallic core, rocky mantle, thin silicate crust.

The critical question is: where did the heat come from? Two sources dominate. First, as the planet grew through accretion — collisions between smaller planetesimals — the kinetic energy of those impacts converted to heat. For a body the size of Earth, this is enormous. Second, the early solar system was laced with short-lived radioactive isotopes, particularly aluminum-26 (Al-26, half-life ~700,000 years), which released intense heat as they decayed. Bodies that formed early enough — while Al-26 was still abundant — received a powerful internal heat source. Add the heat released as dense iron sank (gravitational potential energy converted to thermal energy), and you have a self-reinforcing process: melting allows sinking, and sinking generates more heat.

The evidence for differentiation is literally in our hands. Different types of meteorites correspond to different layers of ancient differentiated bodies that were later shattered by collisions: iron meteorites are the remnants of metallic cores, stony-iron meteorites come from the core-mantle boundary, and stony (chondritic) meteorites represent undifferentiated primitive material that never melted. Comparing these to seismic models of Earth's interior reveals a striking match — Earth's layers are the fully differentiated version of what meteorites sample in fragments.

Not all bodies differentiate equally. Size matters enormously. A large planet retains heat (small surface-area-to-volume ratio), stays molten for millions of years, and differentiates completely. A small asteroid cools rapidly, freezes before separation is complete, and may remain partially or entirely undifferentiated. This is why bodies like Vesta (radius ~260 km) show partial differentiation while tiny asteroids generally do not. Core composition also varies: Mars likely has a sulfur-rich iron core, Earth's is iron-nickel with lighter elements, and Mercury's is disproportionately large — reflecting the different starting compositions and impact histories of each body.
