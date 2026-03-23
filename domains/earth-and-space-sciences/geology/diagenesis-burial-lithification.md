---
id: diagenesis-burial-lithification
title: Diagenesis and the Lithification of Sediments
domain: earth-and-space-sciences
course: geology
prerequisites:
- id: sedimentary-rocks
  type: soft
- id: crustal-heat-flow-and-geotherms
  type: soft
builds-toward:
- metamorphic-grade-pressure-temperature-paths
tags:
- diagenesis
- lithification
- cementation
stage: formal-systems
status: draft
---

# Diagenesis and the Lithification of Sediments

## Core Idea
Diagenesis involves physical (compaction, pressure-solution) and chemical (cementation, precipitation, dissolution) processes occurring at low temperature and pressure during sediment burial. These processes transform unconsolidated sediment into solid rock and control porosity/permeability evolution, important for fluid flow and diagenetic mineral formation.

## Questions

```yaml
- question: "A reservoir engineer finds that a sandstone at 2 km depth has much lower porosity than a similar sandstone at 500 m depth in the same basin. Which diagenetic processes most likely explain this difference?"
  type: multiple-choice
  options:
    - "Metamorphic recrystallization at depth destroyed the pore spaces"
    - "Compaction from overlying sediment weight and cementation by minerals precipitated from pore fluids progressively reduced porosity with burial"
    - "Weathering of quartz grains at depth generated clay minerals that filled pore spaces"
    - "Increased temperature at depth caused sand grains to melt and fuse together"
  answer: 1
  explanation: "Diagenetic compaction and cementation progressively reduce porosity with burial depth. Compaction squeezes grains together and expels pore water; pressure solution allows grains to interpenetrate. Cementation fills remaining pores with precipitated minerals like calcite, quartz, or iron oxides. Metamorphic temperatures (~200–300°C) are not typically reached at 2 km under normal geothermal gradients, and weathering occurs at the surface, not at depth."

- question: "Pressure solution is a diagenetic process that occurs because:"
  type: multiple-choice
  options:
    - "Hot fluids dissolve grains uniformly throughout the rock volume"
    - "Minerals dissolve preferentially at grain-to-grain contacts where stress is concentrated, allowing grains to interpenetrate and reducing porosity"
    - "Elevated temperature causes silica to migrate upward and reprecipitate near the surface"
    - "Acidic pore fluids attack grain surfaces evenly, shrinking all grains simultaneously"
  answer: 1
  explanation: "At grain contacts, stress concentrations lower the chemical potential of the solid, making dissolution thermodynamically favorable at those specific points — even at temperatures where dissolution would not otherwise occur. The dissolved material moves away in solution, and grains physically interpenetrate, creating sutured contacts in sandstones and stylolites in carbonates. This is distinct from cementation, which adds material; pressure solution removes it from stressed locations."

- question: "Early cementation in a sandstone can preserve higher porosity compared to a sandstone that received no early cement during burial."
  type: true-false
  answer: true
  explanation: "Counterintuitively, early cementation can protect porosity by creating a rigid grain framework that resists mechanical compaction during deeper burial. Without early cement, grains rotate, fracture, and compact progressively under increasing overburden, destroying pore space. A cemented framework transmits stress through grain-cement contacts rather than collapsing pores. This early-cementation preservation effect is critical for predicting reservoir quality."

- question: "Diagenesis and metamorphism differ primarily in the types of minerals they produce, not in the temperatures and pressures at which they occur."
  type: true-false
  answer: false
  explanation: "The defining distinction is temperature and pressure, not just mineralogy. Diagenesis occurs from surface conditions to roughly 200–300°C and a few kilometers depth. Metamorphism begins where diagenesis ends, at higher temperatures and pressures that produce fundamentally different mineral assemblages (garnet, kyanite, sillimanite). The different mineral products follow from the different physical conditions."

- question: "How does diagenesis control the economic potential of a sedimentary rock as an oil or groundwater reservoir?"
  type: short-answer
  answer: "Diagenesis controls porosity (the fraction of rock volume that is pore space, determining how much fluid can be stored) and permeability (how easily fluid flows through connected pores, determining extractability). Compaction and cementation reduce both properties; dissolution can create secondary porosity. A rock may store fluids but be uneconomic if permeability is too low to allow extraction at viable rates."
  explanation: "Two sandstones with identical depositional histories can have radically different reservoir qualities if their diagenetic paths diverged — one early-cemented (rigid framework, preserved porosity), the other deeply compacted (porosity destroyed). Predicting these differences from burial history is a central task in petroleum geology and hydrogeology."
```

## Explainer

From your study of sedimentary rocks, you know that sediment begins as loose, unconsolidated material — sand grains on a beach, mud on a lake bottom, shell fragments on a reef. But the sedimentary rocks we find in outcrops and drill cores are hard and cohesive. **Diagenesis** is the collection of processes that bridges this gap, transforming soft sediment into solid rock without reaching the temperatures and pressures that define metamorphism. Think of diagenesis as everything that happens to sediment after deposition but before metamorphism — a low-temperature, low-pressure domain roughly spanning surface conditions to about 200–300°C and a few kilometers of burial depth.

The first and most intuitive process is **compaction**. As sediment accumulates, the weight of overlying layers squeezes out pore water and rearranges grains into a tighter packing. Mud is especially susceptible — freshly deposited clay-rich sediment can be 60–80% water by volume, but after a few hundred meters of burial, compaction may reduce porosity to 20–30%. Sand, with its rigid grains, compacts less but still loses porosity as grains rotate and fracture at points of contact. A related process is **pressure solution**: at grain contacts where stress is concentrated, minerals dissolve preferentially, allowing grains to interpenetrate and further reducing pore space. You can sometimes see the evidence as sutured grain contacts in thin section.

The chemical counterpart is **cementation** — the precipitation of new minerals in the pore spaces between grains. The most common cements are calcite, silica (quartz overgrowths), and iron oxides. Dissolved minerals are carried through the sediment by pore fluids, and when conditions change — temperature rises, pH shifts, or the fluid becomes supersaturated — minerals precipitate on grain surfaces, binding the grains together. Cementation is what gives sandstone its hardness and limestone its density. The type of cement records the chemistry of the pore fluids during burial, making it a valuable clue to burial history.

Why does diagenesis matter beyond simply making rock? Because it controls **porosity and permeability** — the two properties that determine whether a rock can store and transmit fluids. Oil reservoirs, groundwater aquifers, and geothermal systems all depend on pore space that survived or was created during diagenesis. Early cementation can preserve porosity by creating a rigid framework that resists later compaction, while late-stage cementation can destroy it entirely. Dissolution can create secondary porosity — for instance, acidic fluids dissolving carbonate cement to reopen pore space. Understanding the diagenetic history of a sedimentary sequence is therefore essential for predicting where fluids will be found underground, how they will flow, and what resources a formation might hold.
