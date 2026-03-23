---
id: saturation-and-remanence-in-rocks
title: Saturation Magnetization and Natural Remanent Magnetization
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: paleomagnetism-and-reversals
  type: hard
builds-toward:
- secondary-magnetization-alteration
tags:
- rock-magnetism
- remanence
- saturation
stage: expert
status: validated
---

# Saturation Magnetization and Natural Remanent Magnetization

## Core Idea
Magnetic minerals acquire natural remanent magnetization (NRM) during cooling through the Curie temperature (thermoremanent magnetization) or during deposition and diagenesis (depositional remanence). The strength of NRM depends on paleomagnetic field strength at the time of remanence acquisition and is independent of the current ambient field. Saturation magnetization indicates the maximum magnetization possible for a given mineral.

## Questions

```yaml
- question: "A geologist measures the NRM of a basalt sample and finds it points toward what is now magnetic south — opposite the current geomagnetic field direction at the sampling site. What is the most geologically meaningful interpretation?"
  type: multiple-choice
  options:
    - "The sample's magnetic minerals were physically rotated after collection, reversing the measured direction"
    - "The NRM measurement is erroneous because remanent magnetization should always align with the current field"
    - "The basalt cooled and acquired its TRM during a period when Earth's geomagnetic polarity was reversed"
    - "The basalt was struck by lightning, which can randomly orient NRM in any direction"
  answer: 2
  explanation: "TRM is locked in at the time of cooling through the Curie temperature and records the ambient field direction at that moment — not the current field. A reversed NRM indicates the geomagnetic field had opposite polarity when the basalt erupted. This is the principle behind magnetostratigraphy: the rock is a fossil compass, not a live one. Lightning can cause spurious magnetization, but that is not the primary paleomagnetic interpretation."

- question: "Which statement correctly distinguishes saturation magnetization from natural remanent magnetization (NRM)?"
  type: multiple-choice
  options:
    - "Saturation magnetization is measured in the field during sampling; NRM is only measurable in the laboratory"
    - "Saturation magnetization is the intrinsic upper limit for a given mineral composition; NRM is the magnetization actually acquired under ancient field conditions"
    - "NRM can exceed saturation magnetization if the paleomagnetic field was stronger than the modern field"
    - "Both saturation magnetization and NRM depend on the strength of the current ambient magnetic field"
  answer: 1
  explanation: "Saturation magnetization is an intrinsic mineral property — the maximum magnetization when all magnetic domains are forcibly aligned — and is independent of field history. NRM is the magnetization a rock actually acquired and retained under paleomagnetic conditions, which is always a fraction of saturation. NRM cannot exceed saturation magnetization; that is the physical upper bound set by the mineral's composition."

- question: "The intensity of thermoremanent magnetization (TRM) acquired by a cooling lava flow is proportional to the strength of the ambient geomagnetic field at the time of cooling."
  type: true-false
  answer: true
  explanation: "TRM intensity scales with the ambient field strength during cooling through the Curie temperature. This is the physical basis of paleointensity studies: by comparing TRM intensity to laboratory-induced magnetization, researchers can estimate how strong Earth's field was at the time the rock formed. The direction of TRM records field direction; the intensity records field strength."

- question: "A rock's natural remanent magnetization gradually updates over geological time to reflect changes in the ambient magnetic field, functioning as a continuously adjusting compass."
  type: true-false
  answer: false
  explanation: "NRM is locked in at the time of acquisition — when the rock cools through the Curie temperature (TRM), when sediment is deposited and cemented (DRM), or when new minerals grow (CRM). Once acquired, NRM persists essentially unchanged for billions of years unless the rock is reheated above the Curie temperature or undergoes chemical alteration. This permanence is what makes NRM a useful record of ancient fields."

- question: "What makes thermoremanent magnetization (TRM) the most stable form of NRM, and under what conditions can it be destroyed or reset?"
  type: short-answer
  answer: "TRM forms as magnetic minerals cool through the Curie temperature and their crystal structures physically lock magnetic domain walls in place. At ambient temperatures, thermal energy is insufficient to move domain walls, so the magnetization is stable over billions of years. TRM can be destroyed or reset by: (1) reheating above the Curie temperature, allowing domains to re-randomize and then reacquire a magnetization aligned with whatever field is present during re-cooling; or (2) chemical alteration that converts the original magnetic mineral into a new phase, which acquires its own chemical remanent magnetization (CRM) recording a younger field."
  explanation: "The contrast between TRM stability and the instability of depositional or chemical remanence explains why igneous rocks are often preferred for paleomagnetic studies — TRM is acquired quickly during cooling and locked in firmly, minimizing the risk of acquiring secondary magnetizations that obscure the primary record."
```

## Explainer

From your study of paleomagnetism, you know that rocks can carry a memory of ancient magnetic fields. But how exactly does a rock become magnetized, and what controls how strong that magnetization is? The answers lie in the behavior of **magnetic minerals** — primarily magnetite, hematite, and their solid-solution relatives — and the physical processes that lock magnetic signals into the rock record.

Every ferromagnetic or ferrimagnetic mineral has a characteristic **Curie temperature** above which thermal energy overwhelms the magnetic ordering of atoms, and the mineral becomes paramagnetic (essentially non-magnetic in the paleomagnetic sense). For magnetite, this temperature is about 580°C; for hematite, about 675°C. When a lava flow cools and its magnetic minerals drop below the Curie temperature, the minerals acquire a magnetization aligned with the ambient geomagnetic field. This is **thermoremanent magnetization (TRM)**, and it is the strongest and most stable form of natural remanent magnetization. The key insight is that once acquired, TRM is locked in by the crystal structure of the mineral — it persists for billions of years unless the rock is reheated above the Curie temperature or chemically altered. The intensity of TRM is proportional to the strength of the ambient field at the time of cooling, which is why paleointensity studies can estimate how strong Earth's field was millions of years ago.

Sedimentary rocks acquire remanence through a different mechanism. As sediment settles through water, magnetic grains — tiny crystals of magnetite or hematite — physically rotate to align with the ambient field before being locked into place by compaction and cementation. This **depositional remanent magnetization (DRM)** is typically weaker than TRM because not all grains align perfectly and because post-depositional compaction can disturb the original orientation. A related process, **chemical remanent magnetization (CRM)**, occurs when new magnetic minerals grow during diagenesis or low-grade metamorphism; these minerals acquire a magnetization reflecting the field at the time of their growth, not the time of original deposition. Together, TRM, DRM, and CRM constitute the **natural remanent magnetization (NRM)** that paleomagnetic studies seek to measure and interpret.

**Saturation magnetization** is a different but related concept. It describes the maximum magnetization a mineral can achieve when every magnetic domain is aligned in the same direction — the state reached when an external field strong enough to overcome all internal resistance is applied. Saturation magnetization is an intrinsic property of the mineral (about 480 kA/m for pure magnetite at room temperature) and does not depend on the rock's history. It matters in practice because it sets the upper limit on how strong a rock's remanence can be and because comparing measured NRM to saturation magnetization reveals what fraction of the mineral's magnetic capacity was utilized — a ratio that carries information about the paleomagnetic field strength, grain size, and domain state of the magnetic carriers.
