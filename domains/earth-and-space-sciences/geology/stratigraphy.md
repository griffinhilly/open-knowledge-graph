---
id: stratigraphy
title: Stratigraphy and Stratigraphic Principles
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: sedimentary-rocks
  type: hard
- id: geological-time-scale
  type: hard
builds-toward:
- fossils-and-paleontology
- radiometric-dating
tags:
- stratigraphy
- superposition
- correlation
- unconformity
- steno
- sequence-stratigraphy
stage: formal-systems
status: validated
---

# Stratigraphy and Stratigraphic Principles

## Core Idea
Stratigraphy is the study of rock layers (strata) and their spatial and temporal relationships, governed by Steno's principles: superposition (younger beds overlie older), original horizontality (beds are deposited flat), and lateral continuity (beds extend laterally until they thin or terminate). Unconformities—surfaces of missing time where erosion removed strata or deposition ceased—record gaps in the geological record and are classified as angular unconformities, disconformities, or nonconformities. Correlation matches rock units across separated outcrops using lithological similarity, key beds (volcanic ash layers, impact ejecta), or fossil content; radiometric ages anchor correlations absolutely. Sequence stratigraphy relates stratigraphic packages to relative sea-level cycles, predicting rock architecture in sedimentary basins.

## How It's Best Learned
Interpreting a stratigraphic column diagram—identifying the oldest and youngest units, locating unconformities, and determining the relative sequence of events—directly applies all four of Steno's principles. Cross-correlating two widely separated columns using index fossils or a distinctive volcanic ash layer demonstrates how stratigraphy builds a regional picture from local outcrops.

## Common Misconceptions
- Superposition applies only to undisturbed sequences; overturned folds or thrust sheets can place older rocks on top of younger ones.
- An angular unconformity records tilting and erosion, not simply a period of non-deposition; it implies an entire cycle of deformation, uplift, and erosion before re-burial.
- Correlation does not mean rocks in two locations are identical; it means they were deposited at approximately the same time, even if their lithologies differ due to different depositional environments.

## Questions

```yaml
- question: "A geologist observes that older rock layers appear above younger ones in an undisturbed-looking outcrop. Which explanation is most consistent with Steno's principles?"
  type: multiple-choice
  options:
    - "The principle of superposition is incorrect and does not apply universally"
    - "The sequence has been overturned or displaced by tectonic folding or thrust faulting"
    - "The younger rocks sank through the older ones due to density differences after deposition"
    - "An unconformity placed the older rocks directly on top of the younger ones"
  answer: 1
  explanation: "Superposition holds only for undisturbed sequences. Tectonic forces can overturn folds or move older rocks on top of younger ones via thrust faults, creating an apparent violation of superposition that is actually consistent with it — because the sequence was disrupted after deposition. Recognizing this exception is crucial: when superposition seems violated, the diagnosis is structural deformation, not a failure of the principle."

- question: "An angular unconformity separates flat-lying sandstone above from tilted shale below. What sequence of geological events does this surface record?"
  type: multiple-choice
  options:
    - "A period of non-deposition followed by resumed sedimentation with a slight tectonic tilt"
    - "Simultaneous deposition of both layers in different environments that were later juxtaposed"
    - "Deposition of shale, followed by tilting through deformation, uplift, erosion, and finally deposition of overlying sandstone"
    - "A volcanic intrusion that tilted the shale, then cooled and eroded before sandstone accumulated"
  answer: 2
  explanation: "An angular unconformity requires a complete geological cycle: the lower beds must have been deposited, then tilted or folded by tectonic deformation, then uplifted to the surface where erosion truncated them, and finally buried by a new episode of sedimentation. This is fundamentally different from a simple gap in deposition (a disconformity). The angular relationship between lower and upper beds is the direct evidence of the deformation-erosion cycle."

- question: "Biostratigraphic correlation works because rocks of the same age have the same lithology — similar rock types indicate similar age."
  type: true-false
  answer: false
  explanation: "This is a common and consequential misconception. Biostratigraphic correlation matches time intervals using index fossils — it explicitly does NOT require matching rock types. Two outcrops 500 km apart might contain the same ammonite species in completely different lithologies (one a limestone, the other a shale) because the same time interval can produce different sediment types in different depositional environments. Lithostratigraphic correlation uses rock type similarity, but this is unreliable over long distances precisely because environment varies."

- question: "The law of superposition applies only to undisturbed sequences; structural deformation can place older rocks above younger ones."
  type: true-false
  answer: true
  explanation: "This is a critical qualification of Steno's principle. In overturned folds or along thrust faults, older rocks can be physically emplaced on top of younger ones. Geologists detect these situations by examining sedimentary structures (graded bedding, cross-bedding, ripple marks) that reveal which way was originally 'up,' and by mapping the structural geometry of the area. The principle is not wrong — the sequence was deformed after deposition."

- question: "How do index fossils enable correlation of rock layers across widely separated outcrops, even when the rock types at those locations are completely different?"
  type: short-answer
  answer: "Index fossils are species that were geographically widespread, ecologically abundant, and geologically short-lived — they existed for a narrow time interval before going extinct. Because they lived everywhere and for only a short time, their presence in a rock layer constrains when that layer was deposited regardless of its lithology. If two outcrops both contain the same index fossil, those layers formed at approximately the same time, even if one is limestone and the other is shale — different depositional environments producing different rocks during the same time interval."
  explanation: "The power of biostratigraphy is that organisms spread across many environments simultaneously, so their fossils serve as time markers that cut across lithological differences. This is why paleontology and stratigraphy developed together: fossils provide the temporal index that lithology alone cannot."
```

## Explainer

From your study of sedimentary rocks, you know that sediments accumulate in layers, and from the geological time scale, you know that Earth's history spans billions of years divided into named intervals. Stratigraphy is the discipline that connects these ideas: it provides the principles for reading the order, age, and meaning of rock layers — turning exposed cliff faces and drill cores into a narrative of Earth history.

The foundational rules come from **Nicolas Steno** (17th century) and remain the starting point for any stratigraphic analysis. The **law of superposition** states that in an undisturbed sequence, each layer is younger than the one below it and older than the one above — a principle so intuitive it seems trivial, yet it provides the basic logic for relative dating. **Original horizontality** holds that sedimentary layers are deposited in approximately horizontal sheets; if you find tilted or folded strata, something has deformed them after deposition. **Lateral continuity** states that layers originally extend in all directions until they thin out at the basin edge or grade into a different sediment type. Together, these principles let you reconstruct the original geometry of a sedimentary sequence even when erosion, faulting, or folding has disrupted it.

**Unconformities** are the most important features in stratigraphy because they represent missing time — intervals when deposition ceased or when previously deposited rock was eroded away. An **angular unconformity** is dramatic: tilted or folded layers are truncated by erosion and then overlain by flat-lying younger strata, recording an entire cycle of deposition, deformation, uplift, and erosion before burial resumed. A **disconformity** is subtler: the layers above and below are parallel, but a time gap (recognizable from missing fossils or a weathered surface) separates them. A **nonconformity** separates sedimentary rocks from underlying igneous or metamorphic rocks, indicating that deep crystalline basement was once exposed at the surface. Recognizing unconformities is critical because the geological record is more gap than record — at any given location, more time is represented by missing strata than by preserved strata.

**Correlation** is the practice of matching rock units across separated outcrops to build a regional or global picture. **Lithostratigraphic correlation** matches similar rock types (a distinctive red sandstone, a thick limestone), but this is unreliable over long distances because the same environment can produce different rocks in different places. **Biostratigraphic correlation** uses **index fossils** — species that were widespread, abundant, and short-lived — to match time intervals. If two outcrops 500 km apart both contain the same ammonite species, those layers are approximately the same age regardless of rock type. **Chronostratigraphic correlation** anchors the relative sequence to absolute time using radiometric dates from volcanic ash layers or other datable materials. **Sequence stratigraphy** adds another dimension by relating packages of strata to cycles of relative sea-level change: during transgression (rising sea level), fine-grained sediments blanket the shelf; during regression (falling sea level), coarser sediments prograde seaward. These predictable patterns allow geologists to reconstruct basin architecture and even predict the location of petroleum reservoirs from stratigraphic principles alone.
