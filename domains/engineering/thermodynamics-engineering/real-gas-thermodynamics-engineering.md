---
id: real-gas-thermodynamics-engineering
title: Real Gas Thermodynamics and Equations of State
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: thermodynamic-properties-and-equations-of-state
  type: hard
- id: critical-point-behavior-substances
  type: soft
builds-toward:
- compressibility-factor-generalized
tags:
- real-gas
- equation-of-state
- virial
- van-der-waals
- cubic-eos
stage: advanced
status: draft
---

# Real Gas Thermodynamics and Equations of State

## Core Idea
Real gases deviate from ideal behavior due to intermolecular forces and molecular volume. Cubic equations of state (van der Waals, Peng-Robinson, Soave-Redlich-Kwong) predict pressure, temperature, and composition dependence of molar volume. Virial equations express compressibility as a series in density with temperature-dependent coefficients. Accurate thermodynamic properties near the critical point require these models.

## Explainer

You know the ideal gas law PV = nRT and understand that it rests on two assumptions: molecules have no volume, and they exert no forces on each other. At low density and high temperature, these assumptions hold well. But as pressure rises or temperature drops toward the critical point, both assumptions break down and the ideal gas gives increasingly wrong answers. **Real gas thermodynamics** provides the equations needed to correct for these effects.

**Van der Waals** was the first to patch both failures with a physically motivated correction. The **molecular volume** correction replaces V with (V − nb) — the actual free space available for motion is the total volume minus the space occupied by the molecules themselves, where b is the volume excluded per mole. The **intermolecular attraction** correction adds a term −a/V² to the pressure — at high density, attractive forces between nearby molecules reduce the pressure the gas exerts on container walls, as though the molecules "pull back" on each other. The resulting equation (P + a/V²)(V − nb) = RT reduces to the ideal gas at large V and captures qualitative phenomena like the vapor-liquid transition. However, van der Waals is quantitatively poor for engineering calculations. Modern **cubic equations of state** like **Peng-Robinson (PR)** and **Soave-Redlich-Kwong (SRK)** replace van der Waals' simple a/V² with a temperature-dependent attraction term that matches real fluid phase behavior much more accurately, especially near the critical point.

The **virial equation of state** takes a different approach: it expresses the **compressibility factor** Z = PV/nRT as a power series in density, Z = 1 + B/V + C/V² + …, where the **virial coefficients** B, C, … are functions of temperature only. The second virial coefficient B captures two-body interactions; at low to moderate densities, truncating after B gives good accuracy. The virial expansion has rigorous statistical mechanical foundations — each coefficient corresponds to cluster integrals over molecular interactions — making it theoretically transparent, though inconvenient for high-density calculations.

Real gas effects matter most near or above the **critical point**. At the critical point itself, the cubic EOS must satisfy (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0 — two conditions that determine a and b (or their analogues) from the measured critical temperature T_c and critical pressure P_c. This is why you can express any cubic EOS in **reduced variables** (T_r = T/T_c, P_r = P/P_c), leading to the principle of corresponding states: all gases with the same T_r and P_r have approximately the same Z. This principle underlies the **generalized compressibility charts** used in engineering to quickly estimate Z for any gas when precise EOS data is unavailable.
