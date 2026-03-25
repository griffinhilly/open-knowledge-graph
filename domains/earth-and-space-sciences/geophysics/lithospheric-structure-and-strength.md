---
id: lithospheric-structure-and-strength
title: Lithospheric Structure and Strength
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: rock-rheology-elastic-plastic-deformation
  type: hard
- id: plate-tectonics
  type: hard
builds-toward:
- subduction-zone-structure-and-dynamics
tags:
- lithosphere
- strength
- plate-tectonics
- structure
stage: advanced
status: validated
---

# Lithospheric Structure and Strength

## Core Idea
The lithosphere is the strong, relatively cold outer layer of the Earth (crust + uppermost mantle) overlying the weaker asthenosphere. Strength profiles, computed from laboratory rheology and geotherms, show elastic thickness and integrated strength varying with age, temperature, and composition; young, hot lithosphere is weak and thick, old, cold lithosphere is strong. The seismogenic zone's depth distribution reflects the brittle-ductile transition; total lithospheric strength governs stress accumulation at plate boundaries and controls the style of tectonics (extension, compression, strike-slip).

## Questions

```yaml
- question: "A seamount forms on young oceanic lithosphere near a mid-ocean ridge, and another seamount of equal mass forms on old oceanic lithosphere far from the ridge. Which seamount will cause greater lithospheric flexure (bending)?  "
  type: multiple-choice
  options:
    - "The seamount on old lithosphere, because old lithosphere is weaker and more easily bent"
    - "The seamount on young lithosphere, because young lithosphere is thinner and more easily bent"
    - "Both will flex equally, because flexure depends only on the load mass, not on lithospheric age"
    - "The seamount on young lithosphere, because hot rocks are more buoyant and respond more dramatically to loading"
  answer: 1
  explanation: "Young oceanic lithosphere near a mid-ocean ridge is hot, thin, and has a small elastic thickness (Te). A small Te means the plate is mechanically weak and bends significantly under topographic loads. Old, cold oceanic lithosphere has a large Te because more of the plate is below the brittle-ductile transition temperature, contributing to its rigidity. The same load on old lithosphere produces much less flexure. This is why the Hawaiian chain shows progressively stronger subsidence signatures on older lithosphere as the Pacific Plate moves northwest over the hot spot."

- question: "In the yield strength envelope (strength vs. depth diagram) for continental lithosphere, what controls the transition from increasing strength to decreasing strength as depth increases?"
  type: multiple-choice
  options:
    - "The transition from sedimentary to metamorphic rock types"
    - "The change from brittle frictional failure (governed by confining pressure) to ductile creep (governed by temperature)"
    - "The Moho discontinuity, where crustal composition changes to mantle composition"
    - "The increase in grain size with depth, which causes rocks to become more ductile"
  answer: 1
  explanation: "In the shallow crust, rock strength increases with depth because brittle frictional failure is governed by Byerlee's law: strength scales with confining pressure (which increases with depth). But temperature also increases with depth (the geotherm), and once temperature is high enough to activate ductile creep in the dominant mineral phases (quartz at ~300°C, feldspar at ~400°C, olivine at ~600–700°C), strength plummets exponentially with further temperature increase. The depth of peak strength is the brittle-ductile transition — a thermal boundary, not a compositional one."

- question: "Old, cold oceanic lithosphere is mechanically stronger and stiffer than young, hot oceanic lithosphere near a mid-ocean ridge."
  type: true-false
  answer: true
  explanation: "Lithospheric strength is controlled primarily by temperature: the cooler the rock, the deeper the brittle-ductile transition and the greater the integrated strength. Old oceanic lithosphere has been cooling since it formed at the ridge — its geotherm is lower, the seismogenic zone extends deeper, and its elastic thickness is larger. Young lithosphere at the ridge crest is nearly at asthenospheric temperatures and has very little mechanical strength. This is why subducting old oceanic slabs can transmit stresses over large distances and generate deep seismicity, while young slabs buckle and deform."

- question: "Earthquakes can occur throughout the full thickness of the lithosphere, including in the ductile lower portion."
  type: true-false
  answer: false
  explanation: "Earthquakes require brittle failure — sudden shear fracture or frictional sliding on faults. This only occurs in the brittle portion of the yield strength envelope, which corresponds to the seismogenic zone. In the ductile portion (deeper, hotter rocks), deformation occurs by creep — slow, continuous flow that releases strain gradually without generating seismic waves. The seismogenic depth limit corresponds closely to the brittle-ductile transition temperature for the dominant mineral. In most continental crust this is the upper 15–20 km; deeper earthquakes occur in the strong upper mantle beneath some old cratons."

- question: "Why does the yield strength envelope for continental lithosphere sometimes show a 'jelly sandwich' pattern — strong upper crust, weak lower crust, and strong upper mantle?"
  type: short-answer
  answer: "Continental crust is rich in quartz and feldspar, which become ductile at lower temperatures (~300–400°C) than olivine (~600–700°C). The lower crust reaches quartz/feldspar ductile temperatures while the uppermost mantle is still cool enough to remain brittle and strong. This temperature contrast between the weak lower crust and the strong olivine-rich upper mantle creates a strength minimum sandwiched between two stronger layers."
  explanation: "The key is that lithospheric strength depends on both temperature (the geotherm) and mineralogy (which mineral is deforming). In oceanic lithosphere, olivine dominates from the surface down, so there is one main brittle-ductile transition. Continental crust has a compositional boundary at the Moho: felsic minerals (quartz, feldspar) in the crust have lower ductile transition temperatures than mafic minerals (olivine) in the mantle. So the lower crust goes ductile before the upper mantle does, creating the 'jelly' weak layer between two 'bread' strong layers."
```

## Explainer

From rock rheology, you know that rocks can deform in fundamentally different ways depending on temperature, pressure, and strain rate: brittle fracture at low temperatures, ductile flow at high temperatures. From plate tectonics, you know that the Earth's surface is divided into rigid plates that move relative to one another. The lithosphere is where these ideas converge — it is defined not by composition alone but by mechanical behavior. The lithosphere is the portion of the Earth that is strong enough to behave rigidly over geological timescales, and its structure determines how plates respond to forces.

The **yield strength envelope** (or "Christmas tree" diagram) is the central tool for understanding lithospheric strength. It plots the maximum stress a rock can sustain before failing, as a function of depth. In the shallow crust, failure is brittle — governed by Byerlee's law, where frictional strength increases linearly with depth (and confining pressure). Below a certain depth, temperature becomes high enough that rocks deform by ductile creep instead of fracturing. Creep strength decreases exponentially with temperature, so the strength drops off rapidly once temperatures exceed about 300–400°C for crustal minerals and 600–700°C for olivine in the mantle. The result is a profile that is strong near the surface, weak in the middle-to-lower crust, potentially strong again in the uppermost mantle (for continental lithosphere), and then weak in the asthenosphere.

The **elastic thickness** (Te) of the lithosphere — a measure of how stiff a plate is when loaded — is directly related to this strength profile. A plate with a thick, cold, strong lithosphere (like old oceanic lithosphere or an ancient craton) has a large Te and can support topographic loads without much flexure. Young, hot lithosphere (like that near a mid-ocean ridge) has a small Te and flexes easily under loading. This is why oceanic lithosphere stiffens as it ages and cools: the brittle-ductile transition deepens, and more of the plate contributes to its rigidity. Continental lithosphere is more complex because the quartz-rich crust is weaker than the olivine-rich mantle, sometimes producing a "jelly sandwich" strength profile with a weak lower crust separating two strong layers.

These strength variations have direct tectonic consequences. The depth extent of the seismogenic zone — where earthquakes nucleate — corresponds to the brittle portion of the strength envelope. In oceanic lithosphere, earthquakes occur down to about 30–40 km; in continents, they are typically confined to the upper 15–20 km of crust, with deeper events possible in the strong upper mantle beneath cratons. The total integrated strength of the lithosphere determines whether a plate boundary accommodates deformation through narrow faults (strong lithosphere) or broad distributed zones (weak lithosphere), and whether continental collision produces narrow mountain belts or wide plateaus. Every tectonic style — rifting, subduction, collision — is ultimately controlled by where the lithosphere is strong, where it is weak, and how those properties change with depth and temperature.
