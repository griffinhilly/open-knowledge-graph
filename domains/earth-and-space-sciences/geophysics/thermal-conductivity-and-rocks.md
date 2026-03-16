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
stage: advanced
status: draft
---

# Thermal Conductivity of Rocks

## Core Idea
Thermal conductivity k in rocks ranges from ~2 W/(m·K) in poorly consolidated sediments to ~5–6 W/(m·K) in crystalline basement; it decreases with temperature and porosity. Anisotropy in conductivity (higher parallel to foliation) reflects mineral alignment and microstructure. Effective conductivity in layered sequences is a spatial average weighted by layer thickness, and fluid-filled pores greatly reduce effective conductivity compared to dry rock.

## Explainer

From your study of the geothermal gradient and crustal heat flow, you know that heat flows outward through the Earth's crust and that the temperature increase with depth depends on both the heat flux and the rock's ability to conduct that heat. **Thermal conductivity** (k) is the material property that governs this ability — it quantifies how many watts of heat pass through a one-meter cube of rock for each degree of temperature difference across it, measured in W/(m·K). Understanding how k varies across rock types, conditions, and structures is essential for converting heat flow measurements into temperature profiles and for modeling thermal evolution of the crust.

The thermal conductivity of a rock is primarily controlled by its **mineralogy**. Quartz has exceptionally high conductivity (~7–8 W/(m·K)), so quartz-rich rocks like quartzite and clean sandstone are among the best thermal conductors in the crust (k ≈ 4–6 W/(m·K)). Feldspars and micas conduct less well (~2–2.5 W/(m·K)), making granites and gneisses moderate conductors. Clay minerals are poor conductors (~1–1.5 W/(m·K)), which is why shales and mudstones have low bulk conductivity. At the low end, poorly consolidated sediments and volcanic tuffs can have k below 1.5 W/(m·K). This mineralogical control means that a simple lithological log of a borehole can provide a reasonable first estimate of the conductivity profile.

**Porosity** and **pore fluids** introduce a second major control. Water has a thermal conductivity of only about 0.6 W/(m·K) and air is even worse (~0.025 W/(m·K)), so pore space filled with fluid or gas dramatically reduces the effective conductivity below the mineral matrix value. A sandstone with 25% porosity filled with water might have k ≈ 2.5 W/(m·K) compared to ~4.5 W/(m·K) for the same sandstone with negligible porosity. The geometric mixing model matters too: the **harmonic mean** (appropriate for heat flow perpendicular to layering) weights low-conductivity components heavily, while the **arithmetic mean** (for flow parallel to layering) is dominated by high-conductivity components. This creates thermal **anisotropy** in foliated or layered rocks — heat flows more easily along foliation than across it, sometimes by a factor of two or more.

Temperature itself affects thermal conductivity. For most crystalline rocks, k **decreases** with increasing temperature, roughly following a 1/T relationship at moderate temperatures (300–800 K) due to increased phonon scattering. This means the deep crust conducts heat less efficiently than the shallow crust, causing the geothermal gradient to steepen at depth even if heat flow is constant. At very high temperatures (above ~800°C), radiative heat transfer through partially transparent minerals begins to increase the effective conductivity again, though this is mainly relevant for mantle conditions. For sedimentary rocks, compaction with burial reduces porosity, which tends to increase conductivity, partially offsetting the temperature effect. These competing controls — mineralogy, porosity, fluid content, temperature, and fabric — make thermal conductivity one of the more variable and difficult-to-predict physical properties in geophysics, but also one of the most diagnostic for characterizing subsurface thermal regimes.
