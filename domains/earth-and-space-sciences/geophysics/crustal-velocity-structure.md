---
id: crustal-velocity-structure
title: Crustal Velocity Structure and Seismic Layering
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earth-interior-structure
  type: hard
- id: seismic-body-waves-p-and-s
  type: hard
builds-toward:
- seismic-tomography-velocity-imaging
tags:
- crust
- velocity
- seismic
- structure
stage: advanced
status: draft
---

# Crustal Velocity Structure and Seismic Layering

## Core Idea
The crust exhibits distinct velocity layers: the weathered layer, sediments, metamorphic basement, and high-velocity lower crust. Seismic velocity is a function of pressure, temperature, mineralogy, and fluid content, varying laterally and with depth.

## Questions

```yaml
- question: "A seismic survey detects a zone with anomalously low P-wave velocity (~2.5 km/s) at a depth where surrounding crystalline basement has velocities of ~6 km/s. Which factor most likely explains this anomaly?"
  type: multiple-choice
  options:
    - "The zone is at higher temperature than surroundings, which slightly reduces seismic velocity"
    - "The zone is water-saturated with high porosity — fluid-filled pores dramatically reduce P-wave velocity relative to solid crystalline rock"
    - "The zone is composed of denser, more mafic minerals with stronger atomic bonds"
    - "The zone is the base of the sedimentary column and has lower pressure, reducing wave velocity"
  answer: 1
  explanation: "While temperature does reduce seismic velocity, it cannot alone account for a drop from 6 km/s to 2.5 km/s. Fluid content has a far more dramatic effect: water-saturated fractures and pores significantly lower the effective bulk modulus of the rock, reducing P-wave velocity sharply. This is why seismic surveys are so powerful for detecting aquifers and hydrocarbon reservoirs — fluid-saturated zones produce distinctive low-velocity anomalies that stand out against the ambient velocity gradient. Denser, more mafic minerals (option C) would increase velocity, not decrease it."

- question: "The Mohorovičić discontinuity (Moho) is defined as:"
  type: multiple-choice
  options:
    - "The depth at which rock temperature first exceeds the solidus, marking the top of the partially molten mantle"
    - "The depth of 35 km below all continental crust, where sedimentary rock grades into crystalline basement"
    - "The seismic velocity discontinuity where P-wave speed jumps from ~6.5–7 km/s to ~8 km/s, marking the compositional boundary between silicate crust and olivine-rich mantle peridotite"
    - "The boundary between the upper crust (granitic) and lower crust (mafic) at which velocity exceeds 6.5 km/s"
  answer: 2
  explanation: "The Moho is defined seismically — by a sharp velocity jump from approximately 6.5–7 km/s in the lower crust to approximately 8 km/s in the upper mantle. This velocity contrast reflects a compositional change: crustal silicates (granite, basalt, gabbro) give way to olivine-rich mantle peridotite, which has higher density and elastic moduli. The Moho is not at a fixed depth (it varies from ~7 km under oceans to ~70 km under thick mountain roots) and does not mark a temperature boundary or an intra-crustal velocity threshold."

- question: "Seismic velocity increases smoothly and monotonically with depth throughout the continental crust because pressure increases continuously downward."
  type: true-false
  answer: false
  explanation: "Velocity generally increases with depth as pressure closes pores and stiffens rock, but the increase is neither smooth nor monotonic. Velocity can decrease locally where fluid-saturated zones or low-velocity sedimentary layers are sandwiched between higher-velocity basement rocks. The four controlling factors — mineralogy, pressure, temperature, and fluid content — interact in complex ways. Temperature increases with depth and tends to decrease velocity, partially opposing the pressure effect. Fluid overpressure in sedimentary basins can maintain high porosity at depth, producing low-velocity zones that deviate from the expected pressure trend."

- question: "Oceanic crust has higher seismic velocities than continental crust at comparable depths because oceanic rocks are denser and more mafic."
  type: true-false
  answer: true
  explanation: "Oceanic crust is composed primarily of basalt and gabbro — mafic (magnesium- and iron-rich) rocks with higher densities and stronger atomic bonding than the felsic (silicon- and aluminum-rich) granitic rocks that dominate the upper continental crust. Higher mineral density combined with greater elastic moduli (stiffer bonds) translates to faster P-wave propagation. Oceanic crust has a relatively simple velocity structure (4–7 km/s) that increases from sediments through basalt to gabbro. Continental crust has a more complex and generally lower velocity profile in its upper portions due to felsic composition and complex tectonic history."

- question: "Why is seismic velocity a more informative diagnostic of crustal properties than depth alone?"
  type: short-answer
  answer: "Because seismic velocity simultaneously encodes mineralogy (rock type), pressure (which closes pores and stiffens rock with depth), temperature (which slightly softens rock), and fluid content (which dramatically lowers P-wave velocity in porous media). Two rock bodies at the same depth can have very different velocities if their composition or fluid saturation differs — a sedimentary layer and metamorphic basement at 5 km depth are distinguishable by velocity. Fluid-saturated zones produce anomalously low velocities that stand out against the ambient gradient, revealing information no depth measurement alone could provide."
  explanation: "This multi-factor sensitivity is why seismic surveys are indispensable in subsurface geology and exploration. Travel-time anomalies can be inverted into three-dimensional velocity models that map rock types, detect fluid-bearing zones, locate the Moho, and image tectonic structures inaccessible to drilling. The velocity-property relationships are also why every large earthquake provides geophysical information: P and S arrivals at global seismic networks continuously sample Earth's velocity structure, allowing progressively refined tomographic images of the crust and mantle over time."
```

## Explainer

You already know that the Earth's interior is divided into crust, mantle, and core, and that P-waves and S-waves travel at different speeds depending on the material they pass through. Crustal velocity structure zooms in on the outermost layer — the crust — and reveals that it is not a uniform slab but a stack of distinct layers, each with its own seismic velocity signature.

The shallowest layer is the **weathered zone**, where rocks are fractured, porous, and often saturated with water. Seismic velocities here are low — sometimes below 1 km/s — because waves slow down in loose, unconsolidated material. Below this sits the **sedimentary layer**, with velocities typically between 2 and 4 km/s depending on compaction and lithology. Sandstones, shales, and limestones each produce characteristic velocity ranges. Deeper still lies the **crystalline basement** — metamorphic and igneous rocks with velocities of 5.5 to 6.5 km/s. The **lower crust** reaches velocities of 6.5 to 7.2 km/s, composed of denser, more mafic rocks formed under higher pressures. The transition from crust to mantle — the **Mohorovičić discontinuity** (Moho) — is marked by a sharp velocity jump to about 8 km/s as composition shifts from crustal silicates to olivine-rich mantle peridotite.

What controls these velocity differences? Four factors interact. **Mineralogy** is primary: denser minerals with stronger atomic bonds transmit waves faster. **Pressure** increases with depth, compressing pore spaces and stiffening the rock matrix, which raises velocity. **Temperature** works in the opposite direction — hotter rocks are slightly softer and slower. **Fluid content** has a dramatic effect: water-filled fractures and pores slow P-waves significantly and can attenuate S-waves entirely if connected pore spaces contain free fluid. This is why seismic velocity is such a powerful diagnostic tool — it encodes information about rock type, depth, porosity, and fluid saturation simultaneously.

Crustal velocity structure also varies laterally. Oceanic crust is thin (5–7 km), with a simple layered structure of sediments over basalt over gabbro. Continental crust is thick (25–70 km), heterogeneous, and has a more complex velocity profile reflecting billions of years of tectonic reworking. Understanding these velocity variations is foundational for seismic tomography, where travel-time anomalies are inverted to build three-dimensional images of Earth's interior.
