---
id: focal-depth-classification-seismotectonics
title: Focal Depth Classification and Seismotectonics
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earthquake-location-and-hypocenter
  type: hard
- id: plate-tectonics
  type: soft
builds-toward:
- subduction-zone-seismic-structure
tags:
- seismic
- focal-depth
- subduction
- seismotectonics
stage: advanced
status: draft
---

# Focal Depth Classification and Seismotectonics

## Core Idea
Earthquakes are classified as shallow (<70 km), intermediate (70–300 km), or deep (>300 km) based on focal depth. Shallow earthquakes occur at all plate boundaries; intermediate and deep earthquakes occur primarily in subduction zones where cold, sinking lithosphere remains brittle at depths where surface rocks would deform plastically. Focal depth patterns reveal lithospheric structure and plate convergence geometry.

## Questions

```yaml
- question: "Seismologists detect an earthquake at 450 km depth beneath a region with no active surface fault directly above it. What is the most likely tectonic explanation?"
  type: multiple-choice
  options:
    - "The depth determination is wrong — deep earthquakes cannot occur without a surface fault directly above"
    - "The earthquake occurs within a subducting oceanic slab descending from a distant trench, which remains cold and brittle at that depth"
    - "High confining pressure at 450 km compresses rocks until they fracture, regardless of temperature"
    - "The earthquake originates at the boundary between the lower mantle and the outer core"
  answer: 1
  explanation: "Intermediate and deep earthquakes occur almost exclusively in subducting slabs. The slab descends at an angle from a trench and may extend far from the trench laterally at depth. A 450 km depth earthquake can easily be hundreds of kilometers horizontally from the surface trench. The key is not location above a surface fault but rather the presence of cold brittle lithosphere — which only exists at those depths inside a subducting slab. Option C is incorrect: pressure alone does not cause brittle fracture in hot rock; temperature is the key variable."

- question: "Why do deep-focus earthquakes (300–700 km depth) occur in subduction zones but not in the ambient mantle at the same depth?"
  type: multiple-choice
  options:
    - "The subducting slab moves laterally, creating shear stress that the surrounding stationary mantle doesn't experience"
    - "High hydrostatic pressure in subduction zones directly exceeds the fracture threshold regardless of temperature"
    - "The subducting slab is much colder than the surrounding mantle at the same depth, preserving brittle behavior or enabling dehydration embrittlement"
    - "Subducting slabs contain mafic minerals that are inherently more brittle than peridotite mantle at high pressure"
  answer: 2
  explanation: "This is the key insight. At depths greater than ~300 km, the ambient mantle is hot enough that rocks deform plastically — ductile flow dominates over brittle fracture. The subducting slab, however, is cold oceanic lithosphere that sinks faster than heat can conduct inward. This thermal anomaly — the slab remaining hundreds of degrees colder than surrounding mantle — preserves the conditions for brittle failure (or dehydration embrittlement, where water released from hydrated minerals triggers sudden fracture). Without this thermal anomaly, no earthquake mechanism would operate at those depths."

- question: "Shallow earthquakes (less than 70 km depth) occur at all types of plate boundaries, while deep earthquakes occur almost exclusively at subduction zones."
  type: true-false
  answer: true
  explanation: "Shallow earthquakes occur wherever brittle rock fractures under stress — at transform faults (like the San Andreas), at spreading ridges (oceanic divergent boundaries), and at subduction zones. They are by far the most common type and cause the most damage because they are close to the surface. Deep earthquakes require the specific condition of cold brittle material at great depth, which only subducting oceanic lithosphere provides. Transform faults and spreading ridges involve lithosphere that is either too thin or too warm to sustain seismicity at depth."

- question: "The Wadati-Benioff zone is an inclined seismic band that steepens progressively as the subducting slab heats up and becomes more ductile."
  type: true-false
  answer: false
  explanation: "The Wadati-Benioff zone traces the geometry of the descending slab as it dips into the mantle — its angle and extent reflect the slab's descent geometry, not a thermal steepening. Earthquakes cease at the base of the Wadati-Benioff zone (~700 km) when the slab has finally warmed enough to deform plastically (or mineral phase changes absorb the strain), but this termination is not a 'steepening.' Different subduction zones have dramatically different dip angles (steep under Marianas, shallow under parts of South America), reflecting the age and speed of subduction, not a thermal progression."

- question: "Explain why deep-focus earthquakes (>300 km) can occur within subducting slabs but not in the surrounding mantle at the same depth."
  type: short-answer
  answer: "At depths greater than 300 km, the ambient mantle is hot enough that rocks flow plastically — the pressure-temperature conditions favor ductile deformation rather than elastic fracture. Earthquakes require brittle failure: rock must store elastic energy and then snap suddenly. The subducting oceanic slab, however, is old and cold when it begins to descend, and it sinks faster than heat can diffuse inward from the surrounding mantle. This creates a persistent thermal anomaly: the slab remains hundreds of degrees cooler than the surrounding mantle at the same depth. That temperature difference preserves the conditions for brittle failure, or enables dehydration embrittlement — where minerals in the subducting slab release water at specific pressure-temperature conditions, reducing effective stress and triggering sudden fracture. Without this temperature contrast, deep-focus seismicity would be impossible."
```

## Explainer

From your work on earthquake location and hypocenter determination, you know that seismologists can pinpoint not just where an earthquake occurs on the surface but how deep within the Earth it originates. That depth — the **focal depth** — turns out to be one of the most informative measurements in seismology, because it reveals which tectonic process is generating the earthquake.

**Shallow earthquakes** occur at depths less than 70 km. These are by far the most common and occur at every type of plate boundary: transform faults, spreading ridges, and subduction zones alike. They happen within the brittle upper lithosphere, where rocks respond to stress by fracturing — the same brittle failure mechanism you would expect from your understanding of plate tectonics. Most destructive earthquakes are shallow, because the energy release is close to the surface.

**Intermediate-depth earthquakes** (70–300 km) and **deep earthquakes** (300–700 km) are far more restricted in their geography. They occur almost exclusively in **subduction zones**, where one tectonic plate descends beneath another. This is initially puzzling: at those depths, the surrounding mantle is hot enough that rocks should flow plastically rather than snap. The key insight is that the subducting slab is old, cold oceanic lithosphere. It sinks faster than it can warm up, remaining hundreds of degrees cooler than the surrounding mantle at the same depth. This thermal anomaly preserves brittle behavior — or enables alternative failure mechanisms like dehydration embrittlement, where minerals in the slab release water at specific pressure-temperature conditions, triggering sudden fracture.

The spatial pattern of these deep earthquakes is strikingly systematic. In the 1930s and 1940s, Hugo Benioff and Kiyoo Wadati independently noticed that earthquake foci in subduction zones define an inclined plane dipping from the trench into the mantle — now called the **Wadati-Benioff zone**. The angle and extent of this seismic zone maps the geometry of the descending slab. Steeply dipping slabs (like beneath the Mariana Trench) produce earthquakes down to nearly 700 km, while shallowly dipping slabs (like beneath parts of South America) spread their seismicity over a wider horizontal area. Below about 700 km, earthquakes cease entirely — the slab has either warmed enough to deform plastically, or it has reached the transition zone where mineral phase changes absorb the strain. Focal depth classification thus transforms earthquake catalogs into three-dimensional maps of lithospheric structure.
