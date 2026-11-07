---
id: borehole-geophysics-well-logging
title: Borehole Geophysics and Well Logging
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: sedimentary-rocks
  type: hard
- id: seismic-velocity-density-relationships
  type: soft
- id: electrical-resistivity-tomography
  type: soft
- id: fluid-flow-porous-media
  type: soft
- id: near-surface-geophysics-methods
  type: soft
builds-toward: []
tags:
- well-logging
- petrophysics
- porosity
- archie-law
- gamma-ray-log
- resistivity-log
stage: advanced
status: validated
---

# Borehole Geophysics and Well Logging

## Core Idea
Well logging records the physical properties of rocks along a borehole by lowering instruments into the hole and measuring continuously with depth. Common logs measure natural gamma radiation, electrical resistivity, bulk density, neutron response, and sound speed. Interpreted together, they reveal rock type, porosity, and the fluid in the pores, such as salt water, fresh water, oil, or gas. Logs also tie rock layers between wells and link surface seismic data to real rock properties at depth.

## How It's Best Learned
Work with a real or sample log display, reading the tracks side by side, and mark shale and sand beds from the gamma ray curve first. Then compute porosity from a density reading and water saturation from resistivity using Archie's law, and check whether the answers agree with the other logs. Compare logs from two nearby wells to correlate the same beds and see how they thicken or thin.

## Common Misconceptions
- A high resistivity reading always means oil or gas. (Fresh water and low-porosity rocks such as dense limestone or crystalline rock also give high resistivity, so resistivity must be read with porosity and lithology logs.)
- The gamma ray log measures how dense a rock is. (It measures natural radioactivity from potassium, uranium, and thorium, which is usually highest in clay-rich shales.)
- Logs measure porosity directly. (Density, neutron, and sonic tools measure physical responses that are converted to porosity using assumed values for the rock matrix and fluid.)

## Questions

```yaml
- question: "On a gamma ray log, a sandstone bed reads low and the shale above it reads high. Why?"
  type: multiple-choice
  options:
    - "Shale is denser than sandstone"
    - "Shale contains more clay minerals and potassium-bearing minerals, which carry more of the naturally radioactive elements potassium, thorium, and uranium"
    - "Sandstone is saturated with oil, which blocks gamma rays"
    - "Gamma rays travel faster through shale"
  answer: 1
  explanation: "The gamma ray tool counts natural radiation from potassium-40 and the uranium and thorium decay series. Clay minerals hold these elements, so shales usually read high, while clean quartz sandstone and pure carbonates read low."

- question: "A sandstone has a matrix density of 2.65 g/cm³, the pore fluid has a density of 1.00 g/cm³, and the density log reads 2.32 g/cm³. What is the porosity?"
  type: short-answer
  answer: "Porosity = (2.65 − 2.32) ÷ (2.65 − 1.00) = 0.33 ÷ 1.65 = 0.20, or 20 percent."
  explanation: "The bulk density is a mix of solid grains and fluid in proportion to porosity. Solving the mixing equation for porosity gives this standard density-porosity formula."

- question: "Using Archie's law with a = 1, m = 2, and n = 2, a formation has porosity 0.20, formation water resistivity 0.05 ohm-m, and measured resistivity 10 ohm-m. What is the water saturation?"
  type: multiple-choice
  options:
    - "About 12 percent"
    - "About 35 percent"
    - "About 65 percent"
    - "About 100 percent"
  answer: 1
  explanation: "Archie's law gives Sw² = (a × Rw) ÷ (φ^m × Rt) = 0.05 ÷ (0.04 × 10) = 0.125, so Sw ≈ 0.35. About 35 percent of the pore space holds water, and the rest, about 65 percent, holds hydrocarbons."

- question: "Sonic and density logs from a well can be combined to build a synthetic seismogram, which helps match reflections in surface seismic data to specific rock layers."
  type: true-false
  answer: true
  explanation: "Sonic velocity times density gives acoustic impedance. Changes in impedance between layers produce reflections, so a reflection series built from logs can be compared with the seismic section at the well."
```

## Explainer
Surface geophysical surveys image the subsurface from above, but their resolution falls with depth. A borehole lets you put instruments right next to the rock. **Well logging** does this. A tool called a sonde is lowered on a cable, called a wireline, and measurements are recorded as it is pulled up. The result is a set of curves plotted against depth. The first electrical log was run in 1927 in Pechelbronn, France, by a team working for Conrad and Marcel Schlumberger.

Each log answers a different question.

The **gamma ray log** measures natural radioactivity from potassium, uranium, and thorium. Clay minerals hold these elements, so shales usually read high and clean sandstones and limestones read low. Geologists use it first to separate shale from reservoir rock.

**Porosity logs** estimate how much of the rock is pore space. The **density log** sends gamma rays into the rock and counts those scattered back, which depends on electron density and so on bulk density. With known grain and fluid densities, porosity follows from a simple mixing equation. The **neutron log** responds mainly to hydrogen, which sits mostly in pore fluids. The **sonic log** measures how fast sound travels; sound moves more slowly in more porous rock.

**Resistivity logs** show what fills the pores. Rock grains such as quartz conduct very little electricity, so current flows through the pore water. Salty water conducts well, while oil and gas do not. In 1942, the Shell engineer Gus Archie published an empirical relation that links resistivity, porosity, and the resistivity of the formation water to water saturation. If a porous sandstone shows high resistivity, its pores are likely filled partly with hydrocarbons.

The logs are strongest together. A gas-bearing sand often shows a low gamma ray reading, high resistivity, and a "crossover" in which density porosity reads high while neutron porosity reads low, because gas holds little hydrogen. Matching patterns between nearby wells lets geologists **correlate** beds across a field.

Logs also connect geology to seismic data. Multiplying sonic velocity by density gives acoustic impedance, which controls seismic reflections. A synthetic seismogram built from logs ties each reflection to a known rock layer. Beyond oil and gas, well logs are used to locate aquifers, assess geothermal resources, and check rock for storing carbon dioxide underground.
