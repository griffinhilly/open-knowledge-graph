---
id: earthquakes-and-seismology
title: Earthquakes and Seismology
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: tectonic-boundaries
  type: hard
- id: geologic-structures-folds-faults
  type: soft
builds-toward:
- seismic-waves
- earth-interior-structure
tags:
- earthquakes
- seismology
- focus
- epicenter
- magnitude
- fault-rupture
stage: formal-systems
status: validated
---

# Earthquakes and Seismology

## Core Idea
Earthquakes result from the sudden release of elastic strain energy accumulated along faults when shear stress exceeds frictional strength, a process described by the elastic rebound theory. The hypocenter (focus) is the point of rupture initiation at depth; the epicenter is its surface projection. Earthquake magnitude—measured on the moment magnitude scale (Mw)—is logarithmic: each unit increase corresponds to roughly 32 times more energy released. Shallow (< 70 km) earthquakes occur at all plate boundaries; intermediate (70–300 km) and deep (300–700 km) earthquakes occur only in subducting slabs where the cold, brittle lithosphere has not yet equilibrated to ambient mantle temperatures. The global seismograph network constrains fault geometry, stress drop, and rupture propagation within minutes of a major event.

## How It's Best Learned
Plotting the depth distribution of earthquakes along a cross-section perpendicular to a subduction zone reveals the Wadati-Benioff zone—the inclined slab of seismicity—which makes the geometry of subduction concrete. Comparing seismograms from near and far stations to understand how wave travel time changes with distance introduces the inverse problem central to seismology.

## Common Misconceptions
- The Richter scale and moment magnitude scale are not the same; scientists today use Mw almost exclusively, while Richter (ML) is a local magnitude valid only for southern California.
- A 'big one' is not building up in a linear way; earthquake recurrence is stochastic, and the timing of future ruptures cannot be precisely predicted.
- Deeper earthquakes are not more destructive; shallow earthquakes near population centers cause far more damage because seismic energy attenuates with distance.

## Questions

```yaml
- question: "A deep earthquake at 500 km depth in a subduction zone registers Mw 7.5. A shallow earthquake at 15 km depth registers Mw 6.5. Assuming both occur the same distance from a city, which is likely more destructive?"
  type: multiple-choice
  options:
    - "The deep Mw 7.5 earthquake, because it releases roughly 32 times more energy"
    - "The shallow Mw 6.5 earthquake, because seismic energy is concentrated near the surface and attenuates less before reaching the city"
    - "They cause equal damage because the magnitude difference exactly compensates for the depth difference"
    - "Deep earthquakes are always more destructive because they rupture larger fault areas"
  answer: 1
  explanation: "Depth matters enormously for destructiveness. A shallow earthquake concentrates its energy near the surface, producing intense ground shaking in a smaller area. A deep earthquake at 500 km disperses its energy through a much larger rock volume before reaching the surface, resulting in weaker shaking at any given point. The Mw 6.5 shallow earthquake can easily cause more local destruction than a Mw 7.5 deep earthquake, despite releasing ~32 times less energy total. This is the common misconception: bigger magnitude does not automatically mean more destruction."

- question: "Why do earthquakes with depths greater than 300 km occur only in subduction zones and nowhere else?"
  type: multiple-choice
  options:
    - "Subduction zones are the only locations with sufficient tectonic stress to generate large earthquakes"
    - "Only the geometry of subduction zones creates faults that extend to such depths"
    - "The subducting slab remains cold and brittle enough to fracture at those depths, while surrounding mantle rock deforms plastically"
    - "Deep earthquakes occur globally but seismographs can only detect them at subduction zones"
  answer: 2
  explanation: "Rock fractures (producing earthquakes) only when it is cold and brittle. At great depths, the surrounding mantle is hot enough to deform plastically rather than fracture. The subducting oceanic slab, however, descends faster than it can equilibrate to ambient mantle temperatures — it remains anomalously cold and therefore brittle down to about 700 km depth. Below that, even the slab has heated enough to deform plastically, and earthquakes cease. This inclined zone of seismicity — the Wadati-Benioff zone — directly images the geometry of the subducting plate."

- question: "A magnitude 8 earthquake releases approximately twice the energy of a magnitude 7 earthquake."
  type: true-false
  answer: false
  explanation: "The moment magnitude scale is logarithmic in a specific way: each whole-number increase corresponds to roughly 32 times more energy released (and 10 times the ground motion amplitude). So a magnitude 8 earthquake releases about 32 times more energy than a magnitude 7, and about 1,000 times more than a magnitude 6. This nonlinearity is why great earthquakes (Mw 8–9) release a vastly disproportionate share of total seismic energy compared to the thousands of smaller earthquakes that occur daily."

- question: "Shallow earthquakes near populated areas are typically more destructive than deep earthquakes of equal magnitude."
  type: true-false
  answer: true
  explanation: "Seismic energy attenuates (weakens) as it travels through rock. A shallow earthquake at 10 km depth delivers its energy to the surface over a short path, concentrating shaking in a small area at high intensity. A deep earthquake at 400 km spreads the same energy through a vastly larger volume of rock before reaching the surface, resulting in weaker but more widespread shaking. For a given magnitude, proximity of the hypocenter to the surface is one of the strongest predictors of localized destruction."

- question: "Explain the elastic rebound theory of earthquake generation, and why the hypocenter and epicenter are located at different points."
  type: short-answer
  answer: "The elastic rebound theory holds that tectonic plates move continuously, but friction locks fault surfaces together, causing rocks on either side to slowly deform elastically as strain energy accumulates — like bending a ruler. When accumulated stress exceeds the fault's frictional strength, the rocks snap back to their unstrained configuration, releasing the stored energy as seismic waves. The hypocenter (focus) is the underground point where this rupture initiates; the epicenter is the point on Earth's surface directly above it. They differ because faults are inclined planes at depth, not vertical walls reaching the surface."
  explanation: "This distinction matters for hazard assessment: the epicenter is easy to report on a map, but the hypocenter depth determines how energy is distributed. A magnitude 7 hypocenter at 10 km is far more dangerous to surface structures than one at 200 km. The elastic rebound model also explains aftershocks: after the main rupture, the fault has adjusted its geometry and the surrounding rock continues to settle into new stress configurations, producing smaller subsequent fractures."
```

## Explainer

You already understand that Earth's lithosphere is divided into tectonic plates that move relative to one another at boundaries — divergent, convergent, and transform. Where plates interact, friction locks their edges together even as the plates continue to move, building up **elastic strain energy** in the rock over decades to centuries. Think of slowly bending a wooden stick: it stores energy as it flexes until it snaps. This is the **elastic rebound theory** proposed by H.F. Reid after the 1906 San Francisco earthquake: rocks on either side of a locked fault gradually deform, and when accumulated stress exceeds the frictional strength of the fault, they snap back to their undeformed shape, releasing energy as seismic waves.

The point underground where the rock first breaks is the **hypocenter** (or focus); the point on the surface directly above it is the **epicenter**. The distinction matters because earthquake depth dramatically affects the damage pattern. A shallow earthquake at 10 km depth concentrates its energy near the surface, producing intense shaking in a small area. A deep earthquake at 600 km depth spreads its energy over a much larger volume, producing weaker shaking at any single point. Earthquake size is quantified by the **moment magnitude scale (Mw)**, which measures the total energy released based on the area of the fault that ruptured, the amount of slip, and the rigidity of the rock. The scale is logarithmic: a magnitude 7 earthquake releases about 32 times more energy than a magnitude 6, and about 1,000 times more than a magnitude 5. This is why the jump from a moderate earthquake to a great earthquake is not incremental — it is explosive.

The global distribution of earthquakes is not random; it traces plate boundaries with remarkable precision. Shallow earthquakes occur at all three boundary types: at divergent boundaries where plates rift apart, at transform boundaries where plates grind past each other, and at convergent boundaries where plates collide. But intermediate and deep earthquakes occur only at **subduction zones**, where cold, dense oceanic lithosphere plunges into the mantle. The subducting slab remains brittle enough to fracture down to about 700 km depth, producing an inclined plane of seismicity called the **Wadati-Benioff zone**. Below that depth, the slab has heated enough to deform plastically rather than fracturing, and earthquakes cease. Mapping these earthquake depths in cross-section reveals the geometry of the subducting plate — its angle, its extent, and where it may be tearing or bending — making seismology one of the most powerful tools for imaging Earth's interior structure.
