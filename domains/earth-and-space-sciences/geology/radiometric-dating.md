---
id: radiometric-dating
title: Radiometric Dating
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: geological-time-scale
  type: hard
- id: half-life-decay-law
  type: hard
- id: nuclear-chemistry
  type: soft
- id: radioactive-decay
  type: hard
- id: exponential-growth-and-decay
  type: hard
- id: exponential-decay
  type: soft
- id: alpha-decay-emission
  type: hard
- id: exponential-decay-growth
  type: hard
builds-toward:
- fossils-and-paleontology
tags:
- radiometric-dating
- radiocarbon
- uranium-lead
- isotopes
- geochronology
- half-life
stage: abstract-reasoning
status: validated
---
# Radiometric Dating

## Core Idea
Radiometric dating uses the known, constant decay rates of radioactive isotopes to calculate the age of minerals and rocks by measuring the ratio of parent to daughter isotopes. Different isotope systems are suited to different time ranges and materials: carbon-14 (half-life ~5,730 years) dates organic material up to ~50,000 years old; potassium-40/argon-40 dates volcanic minerals millions to billions of years old; uranium-lead dating of zircon crystals can yield ages close to 4 billion years. The method requires a closed system assumption—that no parent or daughter isotopes were added or lost after mineral crystallization—which is tested using concordia diagrams (for U-Pb) or isochron plots. Radiometric dating calibrates the geological time scale and has provided overwhelming evidence that Earth is 4.54 billion years old.

## How It's Best Learned
Working through a decay calculation (given a measured parent/daughter ratio and a known half-life, solve for age) connects the physics of radioactive decay directly to the geological application. Understanding why carbon-14 is useless for dating dinosaur bones (too old by ~60 million years, essentially no C-14 remains) reinforces the importance of choosing the appropriate isotope system for the time range of interest.

## Common Misconceptions
- Radiometric dating does not assume that decay rates have been constant without evidence; rates are measured in controlled laboratory conditions and are governed by nuclear physics that does not depend on external conditions.
- Different dating methods give consistent ages when applied to the same rocks (concordance), which validates the approach.
- Radiocarbon dating cannot date rocks; it dates carbon-bearing organic material, because rocks do not incorporate atmospheric carbon-14.

## Questions

```yaml
- question: "A geologist wants to determine the age of a volcanic ash layer believed to be approximately 500 million years old. Which isotope system is most appropriate?"
  type: multiple-choice
  options:
    - "Carbon-14 / Nitrogen-14 (half-life ~5,730 years)"
    - "Uranium-238 / Lead-206 (half-life ~4.47 billion years)"
    - "Hydrogen-3 / Helium-3 (half-life ~12.3 years)"
    - "Carbon-12 / Carbon-13 (stable isotopes, no decay)"
  answer: 1
  explanation: "The half-life of the isotope system must be comparable to the age being measured. After ~10 half-lives, a parent isotope is effectively undetectable. Carbon-14's half-life of 5,730 years makes it useless for anything older than ~50,000 years. Uranium-238's half-life of ~4.47 billion years is appropriate for hundreds of millions of years. Carbon-12 and -13 are stable and cannot be used for dating at all."

- question: "Radiometric dating relies on the assumption that radioactive decay rates were much faster in Earth's early history and that scientists apply a correction factor to account for this."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Radioactive decay rates are governed by nuclear physics (the weak and strong nuclear forces) and are independent of temperature, pressure, chemical environment, or electromagnetic fields. Rates are measured precisely in laboratories under controlled conditions. They have been verified to be constant across geological contexts — and multiple independent dating methods applied to the same rocks give consistent ages, which validates the assumption of constant rates."

- question: "A sample of wood from an ancient campfire gives a carbon-14 activity that is one-quarter of what a living tree shows today. Approximately how old is the wood?"
  type: short-answer
  answer: "Approximately 11,460 years (two half-lives of carbon-14)."
  explanation: "Each half-life reduces the C-14 to half its previous amount. After one half-life (~5,730 years), the activity is 1/2 of modern. After two half-lives (~11,460 years), it is 1/4 of modern. The formula is: age = (half-life / ln 2) × ln(N₀/N), but the 'one-quarter remaining = two half-lives' reasoning is a direct application of the exponential decay law from prerequisite knowledge."
```

## Explainer

You already know from your prerequisites that radioactive isotopes decay at a constant, predictable rate described by the half-life: the time it takes for exactly half of a sample to decay from the parent isotope to a stable daughter product. Radiometric dating turns this into a clock. If you measure the ratio of parent to daughter atoms in a mineral, and you know the half-life, you can calculate how long ago that mineral formed — because the only way daughter atoms are present is through radioactive decay of the parent since the mineral crystallized.

The key starting condition is the crystallization event. When a mineral like zircon or feldspar forms from molten rock, it incorporates certain elements based on its crystal chemistry — for example, zircon accepts uranium but strongly rejects lead. This means that at time zero, the mineral contains essentially pure parent isotope (uranium) and no daughter (lead). From that moment, uranium decays to lead at a known rate. When a geologist measures the U/Pb ratio today, the amount of lead is the accumulated "clock reading" since crystallization.

Different decay systems are calibrated for different time ranges. **Carbon-14** (half-life ~5,730 years) dates organic materials up to ~50,000 years old — it works because living organisms continuously exchange carbon with the atmosphere, fixing carbon-14 until death, after which no new C-14 enters and the existing C-14 decays. After ~10 half-lives, the remaining C-14 is below detection limits, which is why carbon dating is useless for dinosaur bones (66+ million years old). For ancient rocks, geologists use **potassium-40/argon-40** (half-life ~1.25 billion years) or **uranium-238/lead-206** (half-life ~4.47 billion years), which have yielded consistent ages for the oldest terrestrial zircons at ~4.4 billion years.

The method's validity rests on the **closed system assumption**: no parent or daughter isotopes entered or left the mineral after crystallization. Geologists test this using concordia diagrams (for U-Pb systems) or isochron plots, which reveal whether a sample has remained closed or has been disturbed by later heating or fluid activity. When multiple dating methods agree on the same age for the same rock — called **concordance** — this provides strong validation of both the method and the closed system assumption. The consistent picture from thousands of such measurements across all continents is that Earth is 4.54 billion years old.
