---
id: critical-point-and-supercritical-fluids
title: Critical Point and Supercritical Fluids
domain: physics
course: thermodynamics
prerequisites:
- id: clausius-clapeyron-equation
  type: hard
- id: phase-diagrams
  type: soft
- id: phase-diagrams-thermodynamics
  type: soft
- id: critical-point-phenomena
  type: soft
tags:
- critical-point
- phase-diagram
- supercritical
stage: expert
status: validated
---
# Critical Point and Supercritical Fluids

## Core Idea
The critical point is the endpoint of the liquid-vapor boundary on a phase diagram (T_c, P_c). Above the critical temperature, liquid and gas become indistinguishable (supercritical fluid). The critical point is characterized by (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0.

## Questions

```yaml
- question: "A sealed container of water is heated well above T_c = 374°C while the pressure is kept above P_c = 218 atm. As it continues to heat, which of the following correctly describes what happens to the liquid-gas distinction?"
  type: multiple-choice
  options:
    - "The liquid evaporates completely into steam — a normal phase transition occurs"
    - "The distinction between liquid and gas disappears — the system is supercritical, and no phase boundary is crossed regardless of further pressure or temperature changes"
    - "The water remains liquid indefinitely because high pressure prevents evaporation"
    - "A new type of phase boundary appears above T_c separating supercritical fluid from gas"
  answer: 1
  explanation: "Above T_c and P_c, the liquid-vapor phase boundary no longer exists — it terminated at the critical point. There is no phase transition to speak of; the substance is a supercritical fluid whose properties vary continuously. You can heat it, cool it, compress it, or expand it without ever crossing a phase boundary (as long as you stay above T_c). The fundamental insight is that 'liquid' and 'gas' are not distinct phases above the critical temperature — they are the same fluid."

- question: "Critical opalescence — the milky appearance of a fluid near its critical point — occurs because:"
  type: multiple-choice
  options:
    - "The fluid changes color as liquid and gas mix in equal proportions near the critical point"
    - "Density fluctuations grow to length scales comparable to visible light wavelengths, causing strong scattering, because compressibility diverges and fluctuations occur at all scales simultaneously"
    - "The critical point marks a chemical reaction that produces light-scattering byproducts"
    - "Supercritical fluids are inherently opaque because they have both liquid and gas properties"
  answer: 1
  explanation: "Near T_c, the compressibility (∂V/∂P)_T diverges — it costs almost no energy to rearrange matter between liquid-like and gas-like density. This means density fluctuations grow spontaneously to macroscopic length scales, comparable to the wavelength of visible light (~400–700 nm). Light scatters off these fluctuations, making the fluid appear milky or opaque. This is a physical signature of scale-free fluctuations — at the critical point, there is no preferred length scale, so fluctuations exist at all scales simultaneously."

- question: "Above the critical temperature, it is possible to continuously convert a substance from a liquid-like state to a gas-like state without crossing any phase boundary."
  type: true-false
  answer: true
  explanation: "This is the defining property of the critical point's location on the phase diagram. The liquid-vapor boundary is a line that terminates at the critical point — above T_c, that boundary no longer exists. By increasing temperature above T_c while adjusting pressure, a substance can be taken continuously from high-density (liquid-like) to low-density (gas-like) states. There is no discontinuous jump in properties, no latent heat, and no phase boundary crossed. This 'going around the critical point' is what makes supercritical fluids possible."

- question: "A supercritical fluid is simply a gas that has been compressed to high pressure — it behaves like an ordinary gas and can be described by the ideal gas law with corrections."
  type: true-false
  answer: false
  explanation: "Supercritical fluids are qualitatively different from ordinary gases. They combine liquid-like densities (making them effective solvents) with gas-like transport properties (diffusivity and viscosity comparable to gases, allowing penetration into porous materials). This combination — not available in either the liquid or gas phase — is what makes supercritical CO₂ industrially valuable for extraction and decaffeination. The ideal gas law fails severely at liquid-like densities. A supercritical fluid is a distinct thermodynamic state, not merely a compressed gas."

- question: "Explain why, approaching the critical point from below, the density difference between the liquid and vapor phases shrinks to zero, and what happens to the P-V isotherm at exactly the critical temperature."
  type: short-answer
  answer: "As temperature increases along the liquid-vapor coexistence curve, the liquid expands (thermal expansion reduces its density) while the vapor is compressed (increasing pressure raises vapor density). These two densities converge and meet at T_c, where they become equal — there is no longer any density difference distinguishing the two phases. At T_c, the P-V isotherm develops a horizontal inflection point: (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0 simultaneously. The normally steep, monotonically decreasing isotherm flattens to a horizontal tangent at the critical volume V_c, reflecting the diverging compressibility — an infinitesimal pressure change produces a large volume change at this unique point."
  explanation: "The two mathematical conditions (first and second derivatives both zero) uniquely identify the critical point in the van der Waals model. Below T_c, isotherms have an unphysical region where (∂P/∂V)_T > 0, which resolves into a two-phase coexistence region via the Maxwell construction. Above T_c, isotherms are monotone with no phase separation. At T_c exactly, the boundary between these two behaviors is the inflection-point isotherm."
```

## Explainer

From phase diagrams and the Clausius-Clapeyron equation, you know that the liquid-vapor boundary is a curve in the P-T plane along which both phases coexist in equilibrium. If you follow this boundary upward — increasing both temperature and pressure — what happens? The density of the vapor increases (it becomes more compressed), while the density of the liquid decreases (thermal expansion). At some point, the two densities must converge. The **critical point** (T_c, P_c) is exactly where they meet: above this temperature, there is no longer a meaningful distinction between liquid and gas.

The mathematical signature of the critical point is that the P-V isotherm develops an inflection point with zero slope: (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0 simultaneously. On the van der Waals equation, these two conditions uniquely determine T_c = 8a/27Rb and P_c = a/27b², giving the critical point in terms of the intermolecular interaction parameters a and b. Below T_c, isotherms have a "swaybacked" region where the van der Waals equation predicts (∂P/∂V)_T > 0 — a mechanically unstable region that resolves into the coexisting liquid and vapor phases via the Maxwell construction. Above T_c, isotherms are monotonically decreasing and no phase separation occurs.

A **supercritical fluid** exists above T_c and P_c. Because liquid and gas become indistinguishable at the critical point, you can continuously transform liquid into gas above T_c without ever crossing a phase boundary — by going around the critical point. A supercritical fluid shares properties of both phases: it has the density of a liquid but the diffusivity and viscosity of a gas, making it an excellent solvent and transport medium. Supercritical CO₂ (T_c = 304 K, P_c = 73 atm) is industrially important for decaffeination, pharmaceutical extraction, and dry cleaning precisely because it has liquid-like solvating power with gas-like penetration into porous materials.

Near the critical point, something physically dramatic occurs: **critical opalescence**. Density fluctuations grow over length scales comparable to the wavelength of visible light, scattering it strongly and making the fluid appear milky. This is a signature that the system has no preferred length scale — fluctuations occur at all scales simultaneously. The compressibility (∂V/∂P)_T diverges as T → T_c because the usual resistance to compression vanishes: at the critical point, it costs almost no energy to rearrange matter between liquid-like and gas-like density. These diverging fluctuations near the critical point are the entry point to the much deeper subject of critical phenomena and universal scaling.
