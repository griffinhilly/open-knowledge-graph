---
id: planetary-accretion-chronology
title: Planetary Accretion Chronology and Radiometric Age Constraints
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: radiometric-dating
  type: hard
- id: meteorites-and-planetary-samples
  type: hard
- id: planetary-formation
  type: soft
builds-toward:
- thermal-evolution-terrestrial-planets
tags:
- chronology
- accretion
- radiometric-dating
- early-solar-system
stage: advanced
status: draft
---

# Planetary Accretion Chronology and Radiometric Age Constraints

## Core Idea
Radiometric dating of meteorites and lunar samples constrains planetary accretion timescales to typically 1–10 million years. Isotopic anomalies reveal the sequence and timing of accretion events, fractionation between inner and outer solar system material, and the presence of short-lived radioactive isotopes that influenced early planetary heating.

## Questions

```yaml
- question: "Two asteroids form from the same nebular material: Asteroid A accretes 0.5 million years after CAI formation; Asteroid B accretes 5 million years after CAI formation. Both are the same size and initial composition. What outcome does short-lived radionuclide theory predict?"
  type: multiple-choice
  options:
    - "Both differentiate, since they formed from the same initial material with the same isotopic composition"
    - "Asteroid A melts and differentiates; Asteroid B remains a cold, undifferentiated body"
    - "Asteroid B differentiates more because it had more time to accumulate heat"
    - "Neither differentiates, since heating requires sustained stress over geological time"
  answer: 1
  explanation: "Al-26 has a half-life of ~717,000 years. After 5 million years (~7 half-lives), it has decayed to about 0.8% of its initial value — far too little to melt a planetesimal. The key insight is that accretion timing determines thermal fate: form early while Al-26 is live and you melt and differentiate; form just a few million years later and you remain a cold rubble pile. Option A is the classic misconception — same initial composition does not mean same heating if accretion timing differs."

- question: "Al-26 has completely decayed from the solar system. How do scientists use it to date early planetesimal formation?"
  type: multiple-choice
  options:
    - "By measuring the ratio of Al-26 to stable Al-27 in ancient meteorite samples"
    - "By measuring excess Mg-26 (the stable decay product) locked in early-formed minerals, relative to reference standards — more excess means earlier formation when Al-26 was more abundant"
    - "By calculating how much Al-26 should have been present at solar system formation using nucleosynthesis models alone"
    - "Al-26 cannot be used for dating since it is undetectable; only long-lived systems like U-Pb are used"
  answer: 1
  explanation: "Since Al-26 (half-life ~717,000 yr) has been gone for over 4 billion years, it cannot be measured directly. Instead, its former presence is recorded as excess Mg-26 locked into minerals when they crystallized. More Mg-26 excess means Al-26 was more abundant at the time of formation — i.e., earlier formation relative to CAIs. This is the principle of short-lived radionuclide chronometry: measure the daughter, infer the parent's former abundance, determine relative age."

- question: "Al-26 serves a dual role in planetary accretion chronology: it acts both as a precise chronometer and as a physical heat engine driving differentiation in early-accreting planetesimals."
  type: true-false
  answer: true
  explanation: "Exactly. As a chronometer, Al-26's decay to Mg-26 records when minerals formed relative to CAIs (time zero). As a physical driver, its radioactive decay deposited enough heat in early-accreting planetesimals to melt their interiors and drive metal-silicate differentiation. The same short half-life (~717,000 yr) that makes it a precise chronometer also concentrates its energy release in the brief window of early solar system history, making it the dominant heat source only for bodies that accreted early."

- question: "The former presence of short-lived radionuclides like Al-26 in early solar system materials is confirmed by detecting trace amounts of these isotopes still present in modern meteorites."
  type: true-false
  answer: false
  explanation: "Al-26 (half-life ~717,000 yr) and other short-lived radionuclides have been completely absent for billions of years — their concentrations in modern samples are zero and undetectable. Their former presence is inferred indirectly from excesses of their stable daughter products (e.g., Mg-26 for Al-26 decay) that were locked into minerals at the time of crystallization. This indirect inference is what makes short-lived radionuclide chronometry both powerful and technically demanding."

- question: "Why does the timing of accretion — when a planetesimal formed relative to CAIs — determine whether it differentiated, even if all early solar system bodies began with the same bulk composition?"
  type: short-answer
  answer: "Al-26 (half-life ~717,000 yr) was the primary heat source for early planetesimals, but it decays rapidly. A body accreting 0.5 million years after CAIs retains nearly full Al-26 abundance and heats enough to melt and differentiate into a metallic core and silicate mantle. A body accreting 4–5 million years later retains only a few percent of the initial Al-26, producing insufficient heat to melt. Since all solar system solids started with the same initial Al-26/Al-27 ratio, timing — not composition — determines how much Al-26 survived to provide heat. This is why the meteorite record preserves both differentiated iron meteorites (from early-accreting bodies) and undifferentiated chondrites (from late-accreting bodies) from what was originally the same reservoir of material."
  explanation: "The fundamental point is that radioactive heating is time-gated: the isotope decays on the same timescale as accretion. This is also why the same isotope serves as both the clock and the engine — the precision of Al-26 as a chronometer comes from the same rapid decay that makes it a heating engine only for early-forming bodies."
```

## Explainer

You already know that radiometric dating uses the predictable decay of parent isotopes into daughter products to measure absolute ages, and that meteorites and lunar samples preserve material from the earliest solar system. Planetary accretion chronology applies these tools to answer a deceptively simple question: how fast did the planets come together, and in what order? The answer turns out to be surprisingly precise — and surprisingly fast.

The key technique is **short-lived radionuclide chronometry**. Isotopes like aluminum-26 (half-life ~717,000 years) and hafnium-182 (half-life ~8.9 million years) were present when the solar system formed but have long since decayed to undetectable levels. Their former presence is recorded as excesses of their daughter products (magnesium-26 and tungsten-182, respectively) locked into minerals that crystallized early. By measuring how much daughter excess a sample contains relative to a reference, you can determine when that mineral formed relative to the oldest solar system solids — **calcium-aluminum-rich inclusions** (CAIs), which date to 4.567 billion years ago and serve as "time zero."

Using these clocks, the chronology becomes remarkably clear. CAIs formed first. Chondrules (the rounded grains in chondrite meteorites) formed within the next 1–3 million years. Iron meteorite parent bodies — small planetesimals that melted and differentiated — accreted and separated their metal cores within just 1–2 million years of CAI formation, meaning planet-building began almost immediately. Mars-sized embryos likely assembled within 5–10 million years. Earth's final assembly, including the Moon-forming giant impact, is constrained by hafnium-tungsten systematics to roughly 30–100 million years after solar system formation — slow by comparison, but still geologically instantaneous.

The chronological picture also reveals that **short-lived radioactive isotopes were not just clocks but engines**. Aluminum-26 was abundant enough in early planetesimals to melt their interiors through radioactive heating, driving differentiation (separation of metal cores from silicate mantles) even in bodies only tens of kilometers across. This means the timing of accretion directly controlled a body's thermal fate: accrete early while aluminum-26 is still live, and you melt and differentiate; accrete a few million years later, and you remain a cold, undifferentiated rubble pile. The meteorite record preserves both outcomes, giving us a physical archive of how accretion timing shaped planetary structure from the very beginning.
