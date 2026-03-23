---
id: thermal-conductivity-and-rocks
title: Thermal Conductivity of Rocks
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: geothermal-gradient-crustal-heat-flow
  type: hard
builds-toward:
- thermochronology-and-cooling-ages
tags:
- thermal-properties
- conductivity
- rocks
- minerals
stage: expert
status: validated
---

# Thermal Conductivity of Rocks

## Core Idea
Thermal conductivity k in rocks ranges from ~2 W/(m·K) in poorly consolidated sediments to ~5–6 W/(m·K) in crystalline basement; it decreases with temperature and porosity. Anisotropy in conductivity (higher parallel to foliation) reflects mineral alignment and microstructure. Effective conductivity in layered sequences is a spatial average weighted by layer thickness, and fluid-filled pores greatly reduce effective conductivity compared to dry rock.

## Questions

```yaml
- question: "A sandstone with 25% water-filled porosity is compared to the same sandstone with negligible porosity. Which has higher thermal conductivity?"
  type: multiple-choice
  options:
    - "The water-saturated sandstone — water conducts heat much better than air and fills the pore space"
    - "The low-porosity sandstone — the mineral matrix conducts far better than pore fluids, so more matrix means higher conductivity"
    - "They are equal — porosity changes density but not conductivity"
    - "The water-saturated sandstone — fluid circulation distributes heat more evenly"
  answer: 1
  explanation: "Water has a thermal conductivity of only ~0.6 W/(m·K), while quartz-rich sandstone mineral matrix has k ≈ 4–6 W/(m·K). Adding 25% water-filled pore space therefore dilutes the high-conductivity mineral component with low-conductivity fluid, reducing bulk conductivity significantly — a sandstone with 25% porosity might drop from ~4.5 to ~2.5 W/(m·K). Dry pores (air at ~0.025 W/(m·K)) are even worse. The common misconception is that 'wet rocks conduct heat better,' but this is only true compared to dry porous rock — not compared to the same rock with no porosity."

- question: "Moving from the shallow crust to greater depths at constant heat flow, what generally happens to thermal conductivity of crystalline rocks?"
  type: multiple-choice
  options:
    - "It increases, because higher pressure packs mineral grains together more tightly"
    - "It stays approximately constant, because mineralogy does not change with depth"
    - "It decreases, because higher temperatures increase phonon scattering, reducing the efficiency of heat conduction"
    - "It increases then decreases, peaking at mid-crustal depths where both pressure and temperature effects balance"
  answer: 2
  explanation: "For crystalline rocks, thermal conductivity decreases with increasing temperature, roughly following a 1/T relationship due to increased phonon scattering. This means the deep, hotter crust conducts heat less efficiently than the shallow, cooler crust. At constant heat flow, a lower-conductivity zone must develop a steeper temperature gradient to transmit the same amount of heat — so the geothermal gradient steepens at depth. At very high temperatures (>800°C), radiative heat transfer can increase effective conductivity, but this mainly applies to mantle conditions."

- question: "Water-saturated pore space increases the thermal conductivity of a rock compared to the same rock with no porosity."
  type: true-false
  answer: false
  explanation: "False. Pore space — whether filled with water or air — reduces thermal conductivity below the mineral matrix value because pore fluids conduct heat far less efficiently than most rock-forming minerals. Water (0.6 W/(m·K)) and air (~0.025 W/(m·K)) are both much lower than typical silicate mineral conductivities (2–8 W/(m·K)). The more pore space, the more the bulk conductivity is pulled toward the fluid value and away from the mineral matrix value."

- question: "In a foliated metamorphic rock, heat flows more easily parallel to foliation than perpendicular to it."
  type: true-false
  answer: true
  explanation: "True. Foliation aligns minerals — particularly platy minerals like mica — and creates preferred orientation in the microstructure. Heat flow parallel to foliation encounters a series of conductors in parallel (arithmetic mean, dominated by the highest-conductivity components), while heat flow perpendicular to foliation encounters conductors in series (harmonic mean, dominated by the lowest-conductivity components). This creates thermal anisotropy, with conductivity along foliation sometimes twice the value across it."

- question: "Why does a quartz-rich sandstone have much higher thermal conductivity than a clay-rich shale, even if both are sedimentary rocks at similar depths?"
  type: short-answer
  answer: "Thermal conductivity in rocks is primarily controlled by mineralogy. Quartz has exceptionally high conductivity (~7–8 W/(m·K)), so quartz-dominated sandstone bulk conductivity can reach 4–6 W/(m·K). Clay minerals are poor conductors (~1–1.5 W/(m·K)), so clay-rich shales typically have bulk conductivities below 2 W/(m·K). Shales also tend to have higher porosity filled with low-conductivity fluids. The contrast in mineral conductivity — roughly a factor of 5 between quartz and clay — propagates into a large contrast in bulk rock conductivity."
  explanation: "This tests whether students understand that mineralogy, not rock 'type' or geological age, is the primary control. A geophysicist reading a borehole lithological log can make a reasonable first-pass estimate of the conductivity profile from the mineralogy alone, before any measurements are taken."
```

## Explainer

From your study of the geothermal gradient and crustal heat flow, you know that heat flows outward through the Earth's crust and that the temperature increase with depth depends on both the heat flux and the rock's ability to conduct that heat. **Thermal conductivity** (k) is the material property that governs this ability — it quantifies how many watts of heat pass through a one-meter cube of rock for each degree of temperature difference across it, measured in W/(m·K). Understanding how k varies across rock types, conditions, and structures is essential for converting heat flow measurements into temperature profiles and for modeling thermal evolution of the crust.

The thermal conductivity of a rock is primarily controlled by its **mineralogy**. Quartz has exceptionally high conductivity (~7–8 W/(m·K)), so quartz-rich rocks like quartzite and clean sandstone are among the best thermal conductors in the crust (k ≈ 4–6 W/(m·K)). Feldspars and micas conduct less well (~2–2.5 W/(m·K)), making granites and gneisses moderate conductors. Clay minerals are poor conductors (~1–1.5 W/(m·K)), which is why shales and mudstones have low bulk conductivity. At the low end, poorly consolidated sediments and volcanic tuffs can have k below 1.5 W/(m·K). This mineralogical control means that a simple lithological log of a borehole can provide a reasonable first estimate of the conductivity profile.

**Porosity** and **pore fluids** introduce a second major control. Water has a thermal conductivity of only about 0.6 W/(m·K) and air is even worse (~0.025 W/(m·K)), so pore space filled with fluid or gas dramatically reduces the effective conductivity below the mineral matrix value. A sandstone with 25% porosity filled with water might have k ≈ 2.5 W/(m·K) compared to ~4.5 W/(m·K) for the same sandstone with negligible porosity. The geometric mixing model matters too: the **harmonic mean** (appropriate for heat flow perpendicular to layering) weights low-conductivity components heavily, while the **arithmetic mean** (for flow parallel to layering) is dominated by high-conductivity components. This creates thermal **anisotropy** in foliated or layered rocks — heat flows more easily along foliation than across it, sometimes by a factor of two or more.

Temperature itself affects thermal conductivity. For most crystalline rocks, k **decreases** with increasing temperature, roughly following a 1/T relationship at moderate temperatures (300–800 K) due to increased phonon scattering. This means the deep crust conducts heat less efficiently than the shallow crust, causing the geothermal gradient to steepen at depth even if heat flow is constant. At very high temperatures (above ~800°C), radiative heat transfer through partially transparent minerals begins to increase the effective conductivity again, though this is mainly relevant for mantle conditions. For sedimentary rocks, compaction with burial reduces porosity, which tends to increase conductivity, partially offsetting the temperature effect. These competing controls — mineralogy, porosity, fluid content, temperature, and fabric — make thermal conductivity one of the more variable and difficult-to-predict physical properties in geophysics, but also one of the most diagnostic for characterizing subsurface thermal regimes.
