---
id: fault-mechanics-rupture-propagation
title: Fault Mechanics and Earthquake Rupture Propagation
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: geologic-structures-folds-faults
  type: soft
- id: earthquakes-and-seismology
  type: soft
builds-toward:
- seismic-wave-velocity-attenuation
tags:
- faults
- rupture
- seismology
stage: formal-systems
status: draft
---

# Fault Mechanics and Earthquake Rupture Propagation

## Core Idea
Faults form when shear stress exceeds friction on existing planes. Earthquake rupture propagates along faults controlled by stress drop, friction, and pore fluid pressure. The depth of seismicity and style of faulting reveal the stress state and mechanical properties of the lithosphere.

## Questions

```yaml
- question: "Following the filling of a large reservoir, seismologists record a significant increase in earthquake frequency and magnitude along a nearby fault that had been quiet for decades. What is the most likely mechanism?"
  type: multiple-choice
  options:
    - "The weight of the reservoir water adds shear stress directly along the fault plane in the direction of potential slip"
    - "Elevated pore fluid pressure from reservoir water reduces the effective normal stress on the fault, lowering the frictional resistance required for shear stress to trigger slip"
    - "Reservoir water lubricates the fault surface, reducing the coefficient of friction to near zero and allowing continuous sliding"
    - "The added mass of water changes the regional stress orientation, reactivating faults that were misaligned with the previous stress field"
  answer: 1
  explanation: "The Mohr-Coulomb failure criterion shows that fault slip occurs when shear stress exceeds (friction coefficient × effective normal stress + cohesion). Pore fluid pressure acts to push the fault surfaces apart, reducing the effective normal stress — not by adding shear stress, but by subtracting from the normal stress that friction acts on. Even a fault very close to failure can be pushed over the threshold by a modest increase in pore pressure, without any increase in shear stress. This is also the mechanism behind injection-induced seismicity from wastewater disposal wells."

- question: "Seismologists determine that earthquakes in a particular region are occurring predominantly on reverse (thrust) faults. What does this reveal about the regional stress state?"
  type: multiple-choice
  options:
    - "The maximum principal stress is vertical — gravity dominates and the crust is subsiding under its own weight"
    - "The crust is being extended — plates are pulling apart, allowing the crust to spread horizontally"
    - "The maximum principal stress is horizontal — tectonic compression dominates and the crust is being shortened"
    - "The faults are creeping aseismically, so the stress state cannot be inferred from fault style"
  answer: 2
  explanation: "Fault style is a direct indicator of which principal stress is largest. Reverse (thrust) faults form when horizontal compression exceeds vertical stress — the maximum principal stress is horizontal, pushing rock horizontally. The faults dip gently and accommodate shortening of the crust. In contrast, normal faults form under extension (maximum stress vertical), and strike-slip faults form when horizontal stresses are both larger or smaller than the vertical but in different horizontal orientations. This is why mapping fault types across a region reveals the tectonic stress regime."

- question: "Fluid injection into deep rock formations (such as from wastewater disposal wells) can trigger earthquakes on nearby faults by increasing pore fluid pressure, which reduces the effective normal stress."
  type: true-false
  answer: true
  explanation: "This is well-documented — injection-induced seismicity is a major concern in areas with high wastewater disposal activity. The mechanism is precisely pore pressure: water injected at depth increases fluid pressure in the pore spaces of rock, effectively reducing the clamping force (normal stress) holding fault surfaces together. This can push a fault that was close to failure over the threshold. Critically, the fault does not need to be stressed by the injection; it simply needs to already be loaded near its failure point, which many ancient faults are. The injection provides the final increment of stress reduction."

- question: "Earthquake rupture propagates outward from the hypocenter at speeds faster than the P-wave velocity of the surrounding rock, which is why strong ground shaking is felt before the rupture front reaches a given location."
  type: true-false
  answer: false
  explanation: "Rupture propagates at approximately 70–90% of the shear wave velocity (Vs) — not faster than P-wave velocity (Vp). Since Vp is always greater than Vs, rupture speed is well below P-wave velocity. Seismic waves (both P and S waves) travel away from the hypocenter at their own characteristic velocities, and P waves arrive at distant stations before rupture could ever propagate there. Ground shaking at a distant location is caused by seismic waves radiated from the hypocenter region, not by the rupture front physically reaching that location — rupture is confined to the fault surface."

- question: "Explain why earthquakes below approximately 15–20 km depth are rare in continental crust, using the concept of the brittle-ductile transition."
  type: short-answer
  answer: "Earthquakes require rocks to fracture and slip rapidly — brittle behavior. In the upper crust, rocks are cold and behave brittlely: when stress accumulates, they eventually fracture rather than flow. With increasing depth, temperature increases due to the geothermal gradient. At approximately 15–20 km depth in continental crust, temperatures reach roughly 300–400°C for common crustal rocks (quartz, feldspar), which is sufficient for crystal-plastic deformation — rocks begin to flow slowly under stress rather than fracturing. This is the brittle-ductile transition. Below it, rocks accommodate stress by ductile creep in shear zones rather than sudden fault slip, so the rapid elastic energy release that constitutes an earthquake cannot occur."
  explanation: "The transition depth varies with rock type, strain rate, and geothermal gradient — it is shallower in hot tectonic environments (like volcanic arcs) and deeper in cold, stable cratons. In oceanic and subducting lithosphere, the colder thermal structure allows earthquakes to depths of hundreds of kilometers (the Wadati-Benioff zone), because the subducting slab carries cold, brittle rock to those depths faster than it can thermally equilibrate with the surrounding mantle."
```

## Explainer

From your background in geologic structures, you know that faults are fractures along which rocks have moved, and from seismology, you know that earthquakes are the sudden release of stored elastic energy. Fault mechanics connects these ideas by explaining *how* and *why* faults slip, and how rupture propagates along a fault surface once it begins.

A fault surface is held together by **friction** — the resistance to sliding between the two rock faces in contact. Tectonic forces continuously build up **shear stress** on the fault, but as long as friction exceeds that stress, the fault remains locked and the surrounding rock deforms elastically, storing energy like a compressed spring. This is the interseismic period, and it can last decades to centuries. Failure occurs when shear stress finally overcomes the frictional resistance — a threshold described by the **Mohr-Coulomb failure criterion**, which states that the critical shear stress depends on the normal stress pressing the surfaces together, the coefficient of friction, and the cohesion of the rock. **Pore fluid pressure** plays a critical role: water trapped in rock pores pushes the fault surfaces apart, effectively reducing the normal stress and making slip easier. This is why fluid injection (from wastewater disposal or reservoir impoundment) can trigger earthquakes on faults that were close to failure.

Once slip initiates at a point (the **hypocenter**), rupture propagates outward along the fault surface, and the speed and extent of this propagation determine the earthquake's magnitude and the character of ground shaking. Rupture typically travels at 70–90% of the shear wave velocity of the surrounding rock — roughly 2–3 km/s. As the rupture front advances, it releases the **stress drop**: the difference between the shear stress before and after slip. Not all parts of the fault slip equally; some patches (called **asperities**) are strongly locked and release large stress drops when they finally break, while other sections may creep steadily and radiate little seismic energy. The heterogeneous distribution of friction and stress along a fault surface means that each earthquake has a unique rupture pattern.

The style of faulting — normal, reverse, or strike-slip — reveals the orientation of principal stresses in the lithosphere. **Normal faults** form under extension, where the maximum principal stress is vertical and the crust is being pulled apart. **Reverse (thrust) faults** form under compression, where horizontal stress dominates and crust is being shortened. **Strike-slip faults** accommodate lateral motion where the maximum and minimum horizontal stresses are both larger or smaller than the vertical stress. The depth at which earthquakes occur is limited by the brittle-ductile transition; below about 15–20 km in continental crust, temperatures are high enough that rocks flow rather than fracture, and faults give way to ductile shear zones. The distribution of seismicity on a fault — its depth extent, clustering patterns, and recurrence intervals — encodes the mechanical state of the lithosphere and is the primary observational constraint on fault behavior.
