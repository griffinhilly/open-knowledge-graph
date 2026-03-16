---
id: heat-capacity-constant-volume-pressure
title: Heat Capacity at Constant Volume and Pressure
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: enthalpy-definition-and-significance
  type: hard
tags:
- heat-capacity
- thermodynamic-properties
- specific-heat
stage: formal-systems
status: draft
---

# Heat Capacity at Constant Volume and Pressure

## Core Idea
Heat capacity is the amount of heat required to raise temperature by one unit. At constant volume (Cv), all heat goes into internal energy: Q_v = nCvΔT. At constant pressure (Cp), heat also does flow work: Q_p = nCpΔT. These are different for the same substance and relate through the gas constant.

## Explainer

From the first law of thermodynamics, ΔU = Q − W: the internal energy changes by the heat added minus the work done by the system. When you heat a gas, where does the energy go? The answer depends on whether the gas is free to expand — and this is the essential distinction between Cv and Cp.

At **constant volume**, the container walls prevent expansion, so no PdV work is done (W = 0). All the heat goes directly into internal energy: Q_v = ΔU = nCv ΔT. The **molar heat capacity at constant volume**, Cv, is defined precisely by this: Cv = (1/n)(∂U/∂T)_V. For a monatomic ideal gas, the only internal energy is translational kinetic energy — 3/2 RT per mole from the equipartition theorem — so Cv = 3R/2 ≈ 12.5 J/(mol·K). The temperature rise is entirely due to faster molecular motion; no energy is "wasted" on expansion.

At **constant pressure**, the gas expands as it warms. For an ideal gas, ΔV = nRΔT/P, so the system does work W = PΔV = nRΔT on its surroundings. To achieve the same temperature rise as in the constant-volume case, you must supply that extra work on top of the internal energy increase: Q_p = ΔU + W = nCv ΔT + nR ΔT = n(Cv + R) ΔT. This gives **Cp = Cv + R** — the **Mayer relation**. From your study of enthalpy H = U + PV, this has an elegant interpretation: at constant pressure, Q = ΔH = nCp ΔT, so Cp = (1/n)(∂H/∂T)_P. Enthalpy is the natural thermodynamic potential for constant-pressure processes precisely because it already includes the PV work term.

The **ratio γ = Cp/Cv** = (Cv + R)/Cv has wide physical significance. For a monatomic ideal gas, γ = 5/3. For diatomic gases like N₂ and O₂ at room temperature, the two rotational degrees of freedom contribute, making Cv = 5R/2 and γ = 7/5. At higher temperatures, vibrational modes activate, raising Cv further and driving γ toward 1. The physical content is this: a gas with more internal degrees of freedom absorbs heat more "efficiently" — temperature rises more slowly because the energy distributes among more modes. Measuring Cv or Cp thus probes the internal structure of a molecule, and the temperature-dependence of γ charts which molecular degrees of freedom become thermally accessible at each temperature.
