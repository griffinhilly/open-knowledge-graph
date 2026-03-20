---
id: seawater-properties
title: Physical and Chemical Properties of Seawater
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: solution-concentration
  type: hard
- id: intermolecular-forces
  type: soft
- id: colligative-properties
  type: soft
- id: ionic-bonding
  type: soft
- id: specific-heat-capacity
  type: soft
builds-toward:
- ocean-layering-and-stratification
- thermohaline-circulation
- ocean-chemistry-and-nutrients
tags:
- salinity
- density
- seawater
- temperature
- pressure
stage: advanced
status: validated
---

# Physical and Chemical Properties of Seawater

## Core Idea
Seawater is a complex solution with an average salinity of about 35 parts per thousand (ppt), dominated by sodium chloride but containing many dissolved ions. Its density depends on three variables: temperature (higher temperature lowers density), salinity (higher salinity raises density), and pressure (higher pressure raises density). These properties govern how water masses stratify and circulate globally. Seawater also has a higher heat capacity than freshwater and freezes at approximately −1.8°C.

## How It's Best Learned
Work through density calculations for water parcels with different T-S combinations using T-S diagrams. Observe how adding salt depresses freezing point and raises density, connecting to colligative properties from chemistry.

## Common Misconceptions
- Seawater is not uniformly saline — polar regions are fresher due to ice melt and precipitation; tropics are saltier due to high evaporation.
- Pressure effects on density are significant only at great depths; surface density is primarily governed by temperature and salinity.

## Questions

```yaml
- question: "Two water parcels have the same salinity. Parcel A is at 5°C and Parcel B is at 20°C. Which is denser, and why?"
  type: multiple-choice
  options:
    - "Parcel B, because warmer water expands and contains more dissolved gas"
    - "Parcel A, because lower temperature causes molecules to move more slowly and pack together more tightly"
    - "They are equal, because salinity is the only variable that affects density"
    - "Parcel B, because warm water evaporates less and retains more mass"
  answer: 1
  explanation: "Temperature and density are inversely related in seawater: as temperature rises, water expands (molecules move faster and occupy more volume), reducing density. Parcel A at 5°C is denser than Parcel B at 20°C. Salinity also affects density, but with both parcels at the same salinity, temperature is the deciding variable."

- question: "The ocean is uniformly saline at about 35 ppt everywhere at the surface."
  type: true-false
  answer: false
  explanation: "Surface salinity varies significantly by region. In tropical regions, high solar radiation drives intense evaporation, concentrating salts and raising salinity above 36 ppt. In polar regions, sea ice melt and high precipitation dilute surface waters, lowering salinity to around 30–33 ppt or less. River outflows near coasts also produce locally fresher water. The 35 ppt figure is an approximate global average, not a uniform value."

- question: "Seawater freezes at approximately −1.8°C rather than 0°C. What property of seawater explains this, and what happens to the salt when seawater does freeze?"
  type: short-answer
  answer: "Dissolved salts lower the freezing point of seawater via freezing point depression (a colligative property). When seawater freezes, the ice crystal lattice excludes most dissolved ions, so sea ice is nearly fresh water and the remaining liquid becomes saltier and denser."
  explanation: "Freezing point depression is a colligative property: solutes disrupt the formation of the ordered ice crystal lattice, requiring a lower temperature to freeze. Because ions are excluded from the solid lattice as seawater freezes, the rejected brine sinks into surrounding seawater, increasing its salinity and density — a key driver of deep water formation in polar regions."
```

## Explainer

Seawater is not simply salty water — it is a complex solution of dissolved ions, gases, and organic matter with physical properties that differ meaningfully from pure freshwater. The average salinity of the open ocean is about 35 parts per thousand (ppt), meaning roughly 35 grams of dissolved salts per kilogram of seawater. The dominant ions are sodium and chloride (table salt), but seawater also contains magnesium, sulfate, calcium, potassium, and many trace elements. Importantly, the ratio of major ions remains nearly constant across the ocean even as total salinity varies — this is known as the rule of constant proportions.

The most consequential physical property of seawater is its density, and density is controlled by three variables: temperature, salinity, and pressure. Temperature and density are inversely related: warmer water is less dense because thermal energy causes molecules to spread apart. Salinity and density are directly related: dissolved ions add mass without proportionally increasing volume. Pressure effects are significant only at depth (thousands of meters) and can largely be ignored at the surface. This means that in the surface ocean, the density of a water parcel is almost entirely determined by its temperature and salinity — summarized on a T-S diagram that oceanographers use to identify and track distinct water masses.

Two properties set seawater apart from freshwater in climatically important ways. First, seawater has a high specific heat capacity — it can absorb and store large amounts of heat without a large temperature change. This is why the ocean acts as a thermal buffer for Earth's climate, absorbing excess heat during warming periods and releasing it slowly. Second, seawater freezes at about −1.8°C rather than 0°C because dissolved salts depress the freezing point (a colligative property you may recognize from chemistry). When seawater does freeze, the ice crystal lattice expels most dissolved ions, producing nearly fresh sea ice and leaving behind a saltier, denser brine that sinks — a process central to deep ocean circulation.

A key misconception to correct: surface salinity is not uniform. The tropics have higher salinity because intense evaporation concentrates dissolved ions, while polar regions have lower salinity due to ice melt and net precipitation exceeding evaporation. This spatial variation in salinity — alongside temperature differences — creates the density contrasts that drive the large-scale circulation patterns you will study next in thermohaline circulation.
