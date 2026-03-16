---
id: supercritical-fluid-properties
title: Supercritical Fluid Properties and Applications
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: critical-point-behavior-substances
  type: hard
- id: thermodynamic-property-equations-engineering
  type: soft
builds-toward:
- transcritical-and-supercritical-cycles
tags:
- supercritical
- critical-point
- properties
- applications
stage: advanced
status: draft
---

# Supercritical Fluid Properties and Applications

## Core Idea
Above the critical point (T > T_c, P > P_c), fluids are supercritical: no distinct liquid-vapor boundary, but continuous density and thermophysical property changes. Supercritical fluids exhibit high solvent power and are used in extraction (CO₂), sCO₂ power cycles, and advanced cooling systems. Property variations near the critical point are steep, requiring careful calculations and specialized tables.

## Explainer

From your study of critical-point behavior, you know that the liquid and vapor phases become indistinguishable at the critical point: density, enthalpy, and all other intensive properties converge to a single value, and the meniscus between liquid and vapor disappears. The supercritical region extends beyond this point — above both T_c and P_c simultaneously — into a domain where the substance exists as a single, continuous phase. There is no phase transition to cross, no latent heat to add or remove, just smooth, continuous property variation from liquid-like densities (when cold and highly compressed) to gas-like densities (when hot and moderately compressed).

The most important property of supercritical fluids is their **continuously tunable density**. Near the critical point, a small change in temperature or pressure produces an enormous change in density. For supercritical CO₂ (T_c = 31.1°C, P_c = 73.8 bar), varying pressure from 80 to 200 bar near 40°C changes the density from roughly 200 to 800 kg/m³ — nearly a fourfold change with no phase transition. This tunable density drives the solvent power: nonpolar compounds dissolve readily in dense sCO₂ because dispersion forces scale with density, but the compounds can be recovered simply by reducing pressure, at which point the sCO₂ density drops and the compound precipitates out. This is the principle behind supercritical CO₂ extraction of caffeine from coffee beans and flavors from hops — no toxic solvent residue, no phase separation equipment.

For engineering cycles, the advantage of working across the critical point is different. A **transcritical CO₂ refrigeration cycle** or an **sCO₂ Brayton power cycle** avoids the two-phase dome entirely on the high-pressure side. In an sCO₂ Brayton cycle, fluid is compressed (as a dense, nearly incompressible supercritical fluid — very low compression work), then heated, then expanded through a turbine. Because the density is so high during compression, the compressor work is dramatically reduced relative to an ideal gas cycle. This is why sCO₂ power cycles promise compact, high-efficiency designs for concentrating solar, nuclear, and waste-heat recovery applications.

The engineering challenge of the supercritical region is the steep property gradients near the **pseudocritical line** — the locus of temperatures at each pressure where specific heat is maximized. Near this line, the specific heat, thermal conductivity, and viscosity all vary sharply. Heat transfer correlations developed for subcritical fluids or ideal gases fail badly here. If a heat exchanger operates near the pseudocritical line, local hot spots can cause dramatic property mismatches between the wall and bulk fluid, disrupting heat transfer (the phenomenon of **heat transfer deterioration** in supercritical flows). Engineers designing supercritical equipment must use specialized property tables and are careful to track whether operating conditions are near this highly nonlinear region.
