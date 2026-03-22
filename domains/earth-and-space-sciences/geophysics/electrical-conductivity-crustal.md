---
id: electrical-conductivity-crustal
title: Electrical Properties of Crustal Materials
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earth-interior-structure
  type: hard
- id: rock-rheology-elastic-plastic-deformation
  type: soft
builds-toward:
- electromagnetic-induction-methods
- magnetotelluric-methods-em-induction
tags:
- electrical
- conductivity
- rocks
- minerals
stage: advanced
status: draft
---

# Electrical Properties of Crustal Materials

## Core Idea
Crustal electrical conductivity varies with mineralogy, temperature, fluid content, and pressure. Mafic rocks are more conductive than felsic rocks; water-saturated rocks are much more conductive than dry rock. Conductivity increases steeply with temperature in the lower crust.

## Questions

```yaml
- question: "A magnetotelluric survey images a high-conductivity anomaly at 10 km depth beneath a tectonically stable, cold continental shield. What is the most likely cause?"
  type: multiple-choice
  options:
    - "Partial melting of the crust at that depth"
    - "Interconnected saline fluids in pore spaces or fractures"
    - "High-temperature thermally activated charge carriers in silicate minerals"
    - "A layer of mafic rock with abundant metallic minerals"
  answer: 1
  explanation: "In a cold, tectonically stable shield region, temperatures at 10 km are far too low for partial melting or thermally activated conduction in silicate minerals (which requires 300–400°C minimum). While mafic rock is more conductive than felsic rock, the contrast is modest compared to the orders-of-magnitude drop caused by interconnected saline fluid. Fluids are the dominant control on upper-crustal conductivity — even small amounts of interconnected aqueous solution dramatically reduce resistivity through ionic conduction. Melt and thermal effects dominate only in magmatically active or deep-crustal settings."

- question: "Dry granite at the surface has resistivity of ~10,000 ohm-meters. Adding a small amount of interconnected saline fluid reduces this by a factor of 100 or more. What is the primary mechanism?"
  type: multiple-choice
  options:
    - "Water molecules lubricate grain boundaries, allowing electronic conduction between metallic minerals"
    - "Dissolved ions in the fluid carry charge efficiently through ionic conduction"
    - "The fluid increases temperature locally, thermally activating charge carriers in the silicate minerals"
    - "The fluid causes chemical reactions that convert insulating silicates into more conductive oxides"
  answer: 1
  explanation: "The dominant mechanism is ionic conduction: dissolved salts dissociate into ions (Na⁺, Cl⁻, etc.) that migrate under an applied electric field, carrying charge far more efficiently than the electron-hopping pathways available in dry silicate minerals. Water molecules themselves do not conduct electrons well — the key is the dissolved ions. The 'connectivity' of the fluid matters enormously: isolated pockets of fluid have little effect, but a connected network of fluid-filled fractures creates continuous ionic pathways that drastically reduce bulk resistivity."

- question: "In the upper crust, the single most important factor controlling bulk electrical conductivity is usually rock composition — specifically, whether the rocks are mafic or felsic."
  type: true-false
  answer: false
  explanation: "Composition matters, but it is secondary to fluid content in the upper crust. Even a small amount of interconnected saline fluid can reduce resistivity by orders of magnitude — far more than the difference between mafic and felsic mineralogy. The Explainer explicitly states that fluid content and connectivity is 'usually the single most important factor controlling upper-crustal conductivity.' Mafic vs. felsic composition becomes more relevant when rocks are dry, but in natural settings, fluids dominate the signal."

- question: "Electrical conductivity of crustal rocks generally increases with depth, partly because rising temperature thermally activates charge carriers in silicate minerals."
  type: true-false
  answer: true
  explanation: "This is correct for the deeper crust. Above ~300–400°C, silicate minerals begin to conduct through thermally activated charge carriers, and conductivity increases exponentially with temperature. In the lower crust at 600–800°C, even dry rocks become moderately conductive, and the presence of partial melt amplifies this further. The upper crust is dominated by fluid effects; the lower crust is dominated by temperature. Both mechanisms cause conductivity to increase with depth, but for different reasons."

- question: "Why does even a small amount of interconnected saline fluid reduce rock resistivity so dramatically compared to dry rock?"
  type: short-answer
  answer: "Dry silicate minerals are electrical insulators — the only conduction pathways are through rare metallic or semiconducting minerals. Saline fluid provides dissolved ions that migrate freely under an electric field (ionic conduction), creating a highly efficient conduction pathway through pore spaces and fractures. The key is connectivity: an interconnected fluid network provides a continuous low-resistance path through the rock, while isolated fluid pockets have little effect."
  explanation: "This contrast — many orders of magnitude in resistivity — is what makes electromagnetic geophysical methods so powerful. A tiny fraction of interconnected brine (a few percent by volume) can dominate the bulk conductivity of a rock that is otherwise >99% insulating silicate minerals. This is why upper-crustal conductivity anomalies are so often interpreted as fluid pathways: fluids are the most electrically efficient material that commonly exists in the crust, and even trace connectivity produces a dramatic signal."
```

## Explainer

From your understanding of Earth's interior structure, you know that the crust is composed of diverse rock types arranged in layers. What electrical conductivity adds is a way to "see" the state of those rocks — not just their composition, but whether they contain fluids, how hot they are, and whether they are partially melting. **Electrical conductivity** (the inverse of resistivity) measures how easily electric current flows through a material, and in crustal rocks it varies over many orders of magnitude depending on conditions.

In dry, crystalline rocks at the surface, conductivity is extremely low because most rock-forming silicate minerals are electrical insulators. Current flow in these rocks happens primarily through **electronic conduction** in metallic or semiconducting minerals like magnetite, graphite, or sulfides. A granite with no metallic minerals might have a resistivity of 10,000 ohm-meters or more. But introduce even a small amount of interconnected saline fluid into the pore spaces and fractures, and resistivity can drop by a factor of 100 or more. This happens because dissolved ions in the fluid carry charge efficiently — a mechanism called **ionic conduction**. This is why the single most important factor controlling upper-crustal conductivity is usually the presence and connectivity of aqueous fluids.

Temperature is the dominant control in the deeper crust. As you descend and temperatures rise above roughly 300–400°C, the conductivity of silicate minerals themselves begins to increase exponentially through thermally activated charge carriers. By the time you reach lower-crustal temperatures of 600–800°C, even dry rocks become moderately conductive. The presence of partial melt amplifies this effect dramatically, because silicate melts are far more conductive than solid minerals. This is why electromagnetic methods can detect magma chambers and zones of partial melting beneath volcanoes and rift zones.

Composition also matters in predictable ways. **Mafic rocks** (basalt, gabbro) tend to be more conductive than **felsic rocks** (granite, rhyolite) because mafic minerals contain more iron and have higher intrinsic conductivity. Graphite films along grain boundaries, even in trace amounts, can create anomalously high conductivity because graphite is an excellent electronic conductor and tends to form interconnected networks along shear zones. Some of the most conductive features ever mapped in the crust — conductivity anomalies in ancient suture zones — are attributed to thin graphite films deposited during past subduction of carbon-rich sediments.

Understanding these controls is essential for interpreting geophysical surveys. When a magnetotelluric or resistivity survey reveals a high-conductivity anomaly at depth, the question becomes: is it fluids, partial melt, graphite, or simply hot rock? Answering that question requires combining the electrical data with knowledge of the local geology, temperature structure, and tectonic setting — turning a measurement of how easily current flows into a window on the physical state of the deep crust.
