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
stage: formal-systems
status: draft
---

# Supercritical Fluid Properties and Applications

## Core Idea
Above the critical point (T > T_c, P > P_c), fluids are supercritical: no distinct liquid-vapor boundary, but continuous density and thermophysical property changes. Supercritical fluids exhibit high solvent power and are used in extraction (CO₂), sCO₂ power cycles, and advanced cooling systems. Property variations near the critical point are steep, requiring careful calculations and specialized tables.

## Questions

```yaml
- question: "Supercritical CO₂ is used to extract caffeine from coffee beans. After the caffeine dissolves in the sCO₂, how is it recovered without using a secondary liquid solvent?"
  type: multiple-choice
  options:
    - "The temperature is raised above 300°C, causing the caffeine to pyrolyze and precipitate as a solid"
    - "The pressure is reduced, dropping the sCO₂ density so that its solvent power decreases and the caffeine precipitates out"
    - "The sCO₂ is cooled below its boiling point, converting it to liquid CO₂ that is then evaporated"
    - "An aqueous wash is added to the sCO₂ stream, which selectively absorbs the caffeine"
  answer: 1
  explanation: "The key property of supercritical fluids is continuously tunable density. Dispersion-based solvent power scales with density: dense sCO₂ (at high pressure) dissolves nonpolar compounds like caffeine; lower-density sCO₂ (at reduced pressure) does not. Simply reducing pressure decreases the density and causes the dissolved compound to precipitate out — no secondary solvent needed. This is the defining advantage over traditional solvent extraction. Option C describes liquefaction, not a supercritical process. Option D reintroduces the liquid solvent that sCO₂ extraction is designed to avoid."

- question: "Why does an sCO₂ Brayton cycle achieve higher efficiency compared to a conventional gas turbine cycle that uses air as the working fluid?"
  type: multiple-choice
  options:
    - "CO₂ has a higher specific heat than air, so more heat is stored per unit mass"
    - "Supercritical CO₂ is compressed as a dense fluid, dramatically reducing the compressor work relative to compressing a low-density ideal gas"
    - "CO₂ undergoes phase change in the turbine, releasing latent heat that improves the expansion work output"
    - "The critical temperature of CO₂ is low enough to allow heat rejection near ambient conditions"
  answer: 1
  explanation: "Compression work is proportional to the specific volume of the fluid being compressed (W_comp ≈ ∫v dP). A dense supercritical fluid has a much smaller specific volume than a gas at the same pressure, so the compressor work is dramatically reduced. This is the central thermodynamic advantage: the high-side compression occurs in the dense supercritical region, while the turbine expansion can still deliver large work. Option C is incorrect — sCO₂ cycles specifically avoid the two-phase dome, so no phase change (latent heat) occurs. Option D is true but secondary; the primary advantage is reduced compression work."

- question: "Above the critical point, a supercritical fluid exists as a single continuous phase with no distinction between liquid and vapor."
  type: true-false
  answer: true
  explanation: "This is the defining feature of the supercritical state. Below the critical point, liquid and vapor are distinct phases separated by a meniscus and a phase boundary on a P-T diagram. At the critical point, these phases become indistinguishable — the meniscus disappears and all intensive properties converge. Above both T_c and P_c simultaneously, there is no phase transition to cross: the substance varies continuously from liquid-like densities (at high P, low T end of the supercritical region) to gas-like densities (at low P, high T end) without ever crossing a boundary."

- question: "Supercritical fluids have uniform, stable thermophysical properties throughout the supercritical region, which simplifies heat exchanger design compared to subcritical fluids."
  type: true-false
  answer: false
  explanation: "This is the opposite of reality near the pseudocritical line. Properties like specific heat, thermal conductivity, and viscosity vary sharply near the locus of temperatures where heat capacity peaks at each supercritical pressure. Heat transfer correlations developed for subcritical fluids or ideal gases fail badly in this region, and phenomena like heat transfer deterioration can create dangerous hot spots. The engineering challenge of supercritical systems is precisely this property nonlinearity — designers must use specialized tables and carefully track operating conditions relative to the pseudocritical line."

- question: "Why does operating a compressor in the supercritical region — rather than in the gas phase — reduce compression work? Connect this to the thermodynamic definition of compression work."
  type: short-answer
  answer: "For a steady-flow compressor, work input is proportional to ∫v dP, where v is the specific volume of the fluid. A supercritical fluid near its critical point has very high density and therefore very low specific volume compared to an ideal gas at the same pressure. A smaller specific volume means less work is needed per unit of pressure rise. Intuitively: you are squeezing something nearly as incompressible as a liquid rather than a highly compressible gas, so the pressure rises quickly with little volume change and therefore little work. This is exactly analogous to why liquid-phase pumps in a Rankine cycle require far less work than the gas-phase compressors in a Brayton cycle."
  explanation: "This question targets whether students can connect the qualitative claim ('less compression work') to the quantitative mechanism (∫v dP). The analogy to pump vs. compressor in Rankine/Brayton cycles is a useful bridge for students with thermodynamic cycle backgrounds. The key is recognizing that specific volume — not just density — appears directly in the compression work integral."
```

## Explainer

From your study of critical-point behavior, you know that the liquid and vapor phases become indistinguishable at the critical point: density, enthalpy, and all other intensive properties converge to a single value, and the meniscus between liquid and vapor disappears. The supercritical region extends beyond this point — above both T_c and P_c simultaneously — into a domain where the substance exists as a single, continuous phase. There is no phase transition to cross, no latent heat to add or remove, just smooth, continuous property variation from liquid-like densities (when cold and highly compressed) to gas-like densities (when hot and moderately compressed).

The most important property of supercritical fluids is their **continuously tunable density**. Near the critical point, a small change in temperature or pressure produces an enormous change in density. For supercritical CO₂ (T_c = 31.1°C, P_c = 73.8 bar), varying pressure from 80 to 200 bar near 40°C changes the density from roughly 200 to 800 kg/m³ — nearly a fourfold change with no phase transition. This tunable density drives the solvent power: nonpolar compounds dissolve readily in dense sCO₂ because dispersion forces scale with density, but the compounds can be recovered simply by reducing pressure, at which point the sCO₂ density drops and the compound precipitates out. This is the principle behind supercritical CO₂ extraction of caffeine from coffee beans and flavors from hops — no toxic solvent residue, no phase separation equipment.

For engineering cycles, the advantage of working across the critical point is different. A **transcritical CO₂ refrigeration cycle** or an **sCO₂ Brayton power cycle** avoids the two-phase dome entirely on the high-pressure side. In an sCO₂ Brayton cycle, fluid is compressed (as a dense, nearly incompressible supercritical fluid — very low compression work), then heated, then expanded through a turbine. Because the density is so high during compression, the compressor work is dramatically reduced relative to an ideal gas cycle. This is why sCO₂ power cycles promise compact, high-efficiency designs for concentrating solar, nuclear, and waste-heat recovery applications.

The engineering challenge of the supercritical region is the steep property gradients near the **pseudocritical line** — the locus of temperatures at each pressure where specific heat is maximized. Near this line, the specific heat, thermal conductivity, and viscosity all vary sharply. Heat transfer correlations developed for subcritical fluids or ideal gases fail badly here. If a heat exchanger operates near the pseudocritical line, local hot spots can cause dramatic property mismatches between the wall and bulk fluid, disrupting heat transfer (the phenomenon of **heat transfer deterioration** in supercritical flows). Engineers designing supercritical equipment must use specialized property tables and are careful to track whether operating conditions are near this highly nonlinear region.
