---
id: magma-melting-pressure-temperature
title: 'Magma Generation: Melting Conditions and Mechanisms'
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: igneous-rocks
  type: hard
- id: plate-tectonics-driving-forces
  type: soft
- id: clausius-clapeyron-equation
  type: soft
- id: phase-diagrams-binary-mixtures
  type: soft
- id: phase-diagrams
  type: hard
- id: thermochemistry-heat-and-energy
  type: soft
builds-toward:
- bowen-fractional-crystallization
- subduction-magmatism
tags:
- magma
- melting
- pressure
- temperature
stage: advanced
status: draft
---

# Magma Generation: Melting Conditions and Mechanisms

## Core Idea
Mantle rock melts through three mechanisms: decompression melting (pressure drop at ridges), addition of volatiles (water in subduction zones), or temperature increase (hotspots). The melting temperature of rock varies with pressure, composition, and water content; understanding these controls explains where and why magma forms.

## How It's Best Learned
Plot melting curves (solidi) on P-T diagrams. Compare mantle adiabat with melting curves to predict melting locations.

## Common Misconceptions
- All melting requires a temperature increase.
- Wet rock melts at higher temperatures than dry rock.
- Magma always forms at extreme temperatures.

## Questions

```yaml
- question: "Volcanism occurs at mid-ocean ridges where plates diverge. No external heat source is supplying extra heat to the mantle at these locations. What drives melting?"
  type: multiple-choice
  options:
    - "Friction between diverging plates generates heat that exceeds the solidus temperature"
    - "Seawater infiltrates spreading center cracks and reacts chemically with the mantle to release heat"
    - "Hot mantle rock rises adiabatically; as pressure drops faster than the rock cools, the actual temperature crosses above the falling solidus"
    - "Radioactive decay in the shallow mantle produces enough heat to melt rock at ridge depths"
  answer: 2
  explanation: "Decompression melting requires no external heat source. Mantle rock is already close to its melting temperature at depth, but enormous pressure keeps it solid by raising the solidus. As plates diverge, hot rock rises adiabatically. The solidus is pressure-dependent: it drops as the rock ascends. The rock's actual temperature decreases slightly during ascent (following the adiabat), but the solidus drops faster — eventually the temperature crosses above it and partial melting begins. This is a pressure effect, not a thermal one."

- question: "Why does water released from a subducting slab trigger melting in the overlying mantle wedge, even though the mantle wedge rock is not unusually hot?"
  type: multiple-choice
  options:
    - "Water reacts exothermically with mantle minerals, heating the wedge above the dry solidus"
    - "Water adds mass to the mantle wedge, increasing pressure and triggering compressional melting"
    - "Water disrupts the silicate crystal lattice and lowers the solidus temperature, so mantle rock at normal temperatures begins to melt"
    - "Water oxidizes iron in the mantle, releasing enough heat to drive melting"
  answer: 2
  explanation: "Water is a flux: it breaks bonds in silicate minerals and lowers the temperature at which rock begins to melt (the solidus) by several hundred degrees. The mantle wedge above a subduction zone is at normal temperatures — it would not melt under dry conditions. When hydrous fluids from the descending slab enter the wedge, the solidus drops below the ambient temperature and partial melting begins without any heating. This flux melting mechanism explains why volcanic arcs (Andes, Cascades) parallel subduction zones globally."

- question: "At mid-ocean ridges, mantle rock can begin to melt as it ascends even without any additional heat being supplied from an external source."
  type: true-false
  answer: true
  explanation: "Decompression melting is driven entirely by the pressure-dependence of the solidus. As mantle rock rises adiabatically, pressure falls and the solidus temperature decreases. If the rock's actual temperature follows an adiabat that crosses above the falling solidus at some depth, melting begins without any heat input. The mid-ocean ridge system — the longest volcanic feature on Earth — produces enormous volumes of basaltic magma entirely through this mechanism."

- question: "Adding water to mantle rock raises its melting temperature, which is why subduction zones produce magma — the water heats the surrounding mantle above its normal melting point."
  type: true-false
  answer: false
  explanation: "Water does the opposite: it lowers the solidus of mantle rock, sometimes by several hundred degrees. Subduction zones produce magma not because the mantle is unusually hot, but because water from the subducted slab makes normally-solid rock melt at lower temperatures. Wet rock has a lower melting temperature than dry rock at the same pressure — one of the most counterintuitive and commonly missed facts in igneous petrology, and the core of the flux melting mechanism."

- question: "Describe the three mechanisms by which mantle rock can melt, and for each, explain what changes on a pressure-temperature diagram to cause melting."
  type: short-answer
  answer: "1) Decompression melting: pressure decreases as rock ascends at a mid-ocean ridge. On a P-T diagram, the system moves to lower pressures; since the solidus slopes upward, this moves the state leftward across the solidus into the melt field — no temperature increase needed. 2) Flux melting: addition of water shifts the solidus itself to lower temperatures at constant pressure. The solidus moves toward the ambient geotherm, intersecting it and triggering melting in the subduction zone mantle wedge. 3) Hotspot melting: an anomalously hot mantle plume raises the rock's actual temperature above the solidus at depth, moving the state upward on the P-T diagram across the solidus."
  explanation: "In all three cases, melting occurs when the geotherm (the actual P-T state of the mantle) crosses above the solidus. The mechanisms differ in which variable shifts: decompression moves the state along the pressure axis, flux melting moves the solidus itself, and hotspot melting moves the state along the temperature axis. Recognizing which variable changes in each tectonic setting is the key to understanding the global distribution of volcanism."
```

## Explainer

From your study of igneous rocks, you know that magma is molten rock that cools to form crystalline or glassy solids. From phase diagrams, you know that whether a substance is solid or liquid depends on both temperature and pressure. The crucial insight for understanding magma generation is that the **solidus** — the boundary between fully solid and partially molten rock on a pressure-temperature diagram — is not a fixed temperature. It shifts depending on pressure and composition, and this shift is what allows rock to melt without necessarily getting hotter.

The mantle is almost entirely solid, yet magma forms in several tectonic settings. The most voluminous mechanism is **decompression melting**, which occurs at mid-ocean ridges. As tectonic plates diverge, hot mantle rock rises to fill the gap. This rock is already close to its melting temperature at depth, but it stays solid because the enormous pressure at depth raises the solidus. As the rock ascends, pressure drops faster than the rock cools, and at some point the rock's actual temperature crosses above the falling solidus — partial melting begins. No external heat source is needed; the rock melts simply because it has risen to a depth where the pressure is low enough. If you recall the Clausius-Clapeyron equation from thermodynamics, the same principle applies: the slope of the solid-liquid boundary on a P-T diagram means that reducing pressure at constant temperature can cross the phase boundary into the liquid field.

The second mechanism is **flux melting**, dominant at subduction zones. When oceanic lithosphere descends into the mantle, it carries water locked in hydrated minerals like serpentine and amphibole. As the slab heats up at depth, these minerals break down and release water into the overlying mantle wedge. Water is a powerful **flux**: it disrupts the silicate crystal lattice and dramatically lowers the solidus — by several hundred degrees in some cases. The mantle wedge rock, which would otherwise be too cool to melt, partially melts because the addition of water has moved the solidus down below the ambient temperature. This is why volcanic arcs (like the Andes or the Cascades) sit directly above subduction zones — the water released from the descending slab triggers melting in a narrow zone above it.

The third mechanism is **hot-spot melting**, where an anomalously hot plume of mantle material rises from deep within the Earth — possibly from the core-mantle boundary. Unlike decompression melting at ridges, which taps mantle at roughly normal temperatures, plume material is genuinely hotter than its surroundings (by perhaps 100–300°C). This excess temperature means it crosses the solidus at greater depth and produces larger volumes of melt. Hawaii and Iceland are the classic examples: both sit atop mantle plumes and produce prolific volcanism far from any plate boundary. In all three mechanisms, the key to understanding where and why magma forms is the relationship between the mantle's actual temperature profile (the **geotherm**) and the pressure-dependent solidus — melting happens wherever the geotherm crosses above the solidus.
