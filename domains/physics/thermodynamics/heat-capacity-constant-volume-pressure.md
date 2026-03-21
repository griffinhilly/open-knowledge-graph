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

## Questions

```yaml
- question: "You heat 1 mole of an ideal monatomic gas by 10 K at constant volume, then separately heat a second mole of the same gas by 10 K at constant pressure. Which process requires more heat input?"
  type: multiple-choice
  options:
    - "They require the same heat — the temperature rise is identical, so the energy added must be equal"
    - "Constant pressure requires more heat — additional energy must be supplied to do PdV expansion work"
    - "Constant volume requires more heat — confining the gas causes more internal collisions, needing more energy"
    - "Constant pressure requires more heat — higher pressure means more molecular resistance to heating"
  answer: 1
  explanation: "At constant volume, no expansion occurs (W = 0), so all heat goes into internal energy: Q_V = nCᵥΔT. At constant pressure, the gas expands as it warms, doing work W = PΔV = nRΔT on its surroundings. To achieve the same ΔT, you must supply that extra work on top of the internal energy increase: Q_P = nCᵥΔT + nRΔT = nCₚΔT. Since Cₚ = Cᵥ + R > Cᵥ, the constant-pressure process always requires more heat for the same temperature rise. The extra heat doesn't go into the gas — it goes into the surroundings as expansion work."

- question: "The Mayer relation Cₚ = Cᵥ + R holds for ideal gases. What does the R term physically represent?"
  type: multiple-choice
  options:
    - "The extra heat needed to overcome intermolecular attractions as the gas expands"
    - "The work per mole done by the gas expanding against constant pressure as temperature rises by 1 K"
    - "The additional rotational kinetic energy that activates specifically at constant pressure"
    - "The energy lost to friction between gas molecules during the expansion process"
  answer: 1
  explanation: "For an ideal gas at constant pressure, when temperature rises by ΔT, the gas expands by ΔV = nRΔT/P. The work done by the gas is W = PΔV = nRΔT. Per mole per kelvin, this is R ≈ 8.314 J/(mol·K). This is exactly the difference Cₚ − Cᵥ = R. The gas molecules themselves have the same kinetic energy as in the constant-volume case (since ΔU = nCᵥΔT is the same), but extra energy equal to nRΔT was needed to push back the atmosphere. There are no intermolecular attractions in an ideal gas (option A is wrong)."

- question: "For all ideal gases, Cₚ > Cᵥ, and the ratio γ = Cₚ/Cᵥ approaches 1 as the number of thermally active degrees of freedom increases."
  type: true-false
  answer: true
  explanation: "Both claims are correct. Cₚ = Cᵥ + R always, so Cₚ is always larger. The ratio γ = Cₚ/Cᵥ = (Cᵥ + R)/Cᵥ = 1 + R/Cᵥ. As more degrees of freedom activate (translation, rotation, vibration), Cᵥ grows while R stays constant, so R/Cᵥ shrinks and γ → 1. Monatomic: Cᵥ = 3R/2, γ = 5/3 ≈ 1.67. Diatomic at room temperature: Cᵥ = 5R/2, γ = 7/5 = 1.40. At high temperature with vibration active: Cᵥ = 7R/2, γ = 9/7 ≈ 1.29."

- question: "For an ideal gas heated at constant volume, the heat added equals the change in enthalpy ΔH."
  type: true-false
  answer: false
  explanation: "At constant volume, Q = ΔU = nCᵥΔT. It is constant pressure, not constant volume, where Q equals the change in enthalpy: Q_P = ΔH = nCₚΔT. This is precisely why enthalpy was defined as H = U + PV — it is the natural thermodynamic potential for constant-pressure processes because ΔH automatically accounts for both the internal energy change and the PV work. At constant volume, enthalpy changes by ΔH = ΔU + VΔP = nCᵥΔT + nRΔT = nCₚΔT, which is not equal to Q_V."

- question: "Explain why Cₚ is always greater than Cᵥ for an ideal gas, and what the difference Cₚ − Cᵥ = R represents physically."
  type: short-answer
  answer: "At constant volume, all the heat supplied goes into increasing the internal energy (kinetic energy of the molecules), so Cᵥ = (1/n)(ΔU/ΔT). At constant pressure, the gas must not only increase its internal energy by the same amount but also expand and do work on the surroundings. By the first law, Q_P = ΔU + W = nCᵥΔT + PΔV. For an ideal gas, PΔV = nRΔT, so Q_P = n(Cᵥ + R)ΔT, giving Cₚ = Cᵥ + R. The R represents the mechanical work done by one mole of ideal gas expanding against constant external pressure when heated by 1 K — energy that leaves the gas as work rather than staying as internal energy."
  explanation: "This also explains why Cₚ is the relevant heat capacity for most laboratory and industrial processes, which occur at (approximately) constant atmospheric pressure rather than constant volume. Measuring Q at constant pressure and dividing by nΔT gives Cₚ directly — and Cᵥ can be recovered via the Mayer relation. The elegance of the Mayer relation is that it connects a purely mechanical quantity (R, from PV = nRT) to measured thermal properties (Cᵥ and Cₚ)."
```

## Explainer

From the first law of thermodynamics, ΔU = Q − W: the internal energy changes by the heat added minus the work done by the system. When you heat a gas, where does the energy go? The answer depends on whether the gas is free to expand — and this is the essential distinction between Cv and Cp.

At **constant volume**, the container walls prevent expansion, so no PdV work is done (W = 0). All the heat goes directly into internal energy: Q_v = ΔU = nCv ΔT. The **molar heat capacity at constant volume**, Cv, is defined precisely by this: Cv = (1/n)(∂U/∂T)_V. For a monatomic ideal gas, the only internal energy is translational kinetic energy — 3/2 RT per mole from the equipartition theorem — so Cv = 3R/2 ≈ 12.5 J/(mol·K). The temperature rise is entirely due to faster molecular motion; no energy is "wasted" on expansion.

At **constant pressure**, the gas expands as it warms. For an ideal gas, ΔV = nRΔT/P, so the system does work W = PΔV = nRΔT on its surroundings. To achieve the same temperature rise as in the constant-volume case, you must supply that extra work on top of the internal energy increase: Q_p = ΔU + W = nCv ΔT + nR ΔT = n(Cv + R) ΔT. This gives **Cp = Cv + R** — the **Mayer relation**. From your study of enthalpy H = U + PV, this has an elegant interpretation: at constant pressure, Q = ΔH = nCp ΔT, so Cp = (1/n)(∂H/∂T)_P. Enthalpy is the natural thermodynamic potential for constant-pressure processes precisely because it already includes the PV work term.

The **ratio γ = Cp/Cv** = (Cv + R)/Cv has wide physical significance. For a monatomic ideal gas, γ = 5/3. For diatomic gases like N₂ and O₂ at room temperature, the two rotational degrees of freedom contribute, making Cv = 5R/2 and γ = 7/5. At higher temperatures, vibrational modes activate, raising Cv further and driving γ toward 1. The physical content is this: a gas with more internal degrees of freedom absorbs heat more "efficiently" — temperature rises more slowly because the energy distributes among more modes. Measuring Cv or Cp thus probes the internal structure of a molecule, and the temperature-dependence of γ charts which molecular degrees of freedom become thermally accessible at each temperature.
