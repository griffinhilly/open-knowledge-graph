---
id: critical-point-phenomena
title: Critical Point Phenomena
domain: physics
course: thermodynamics
prerequisites:
- id: van-der-waals-equation-of-state
  type: hard
- id: phase-transitions
  type: soft
builds-toward:
- phase-equilibrium-coexistence
tags:
- phase-transitions
- singularities
- supercritical-fluids
stage: formal-systems
status: validated
---

# Critical Point Phenomena

## Core Idea
At the critical point (T_c, P_c), a pure substance exhibits a second-order phase transition where the liquid-vapor distinction vanishes and the density, properties, and fluctuations diverge according to power laws. Above T_c, the substance cannot be liquefied regardless of applied pressure; at T_c, the isotherm has zero slope and inflection point simultaneously. Near the critical point, properties vary dramatically with small changes in conditions, and the distinction between liquid and gas becomes ill-defined, leading to exotic states like supercritical fluids.

## How It's Best Learned
Examine the P-V diagram near the critical point. Observe how the liquid-gas interface disappears above T_c. Study density and property divergences.

## Common Misconceptions
- Thinking all phase transitions are first-order (the critical point is second-order).
- Assuming the critical point is the same for all substances at the same T and P (it is not; it is absolute).
- Confusing supercritical fluids with ordinary gases.

## Questions

```yaml
- question: "A substance is held at temperature T = 1.2 T_c. What happens if you compress it isothermally to very high pressure?"
  type: multiple-choice
  options:
    - "It liquefies once pressure exceeds a critical threshold"
    - "It remains in a single supercritical phase, becoming denser but never crossing a phase boundary"
    - "It undergoes a first-order phase transition to liquid"
    - "It separates into coexisting liquid and gas regions"
  answer: 1
  explanation: "Above T_c, there is no liquid-vapor phase boundary — the substance cannot be liquefied regardless of applied pressure. It becomes increasingly dense and liquid-like, but properties change continuously with no discontinuity. This is the defining feature of the supercritical state. The tempting wrong answer (A) reflects the misconception that high pressure always produces a liquid; that is only true below T_c."

- question: "Critical opalescence — the milky-white appearance of a fluid near its critical point — occurs because:"
  type: multiple-choice
  options:
    - "The substance undergoes a color-producing phase transition"
    - "Density fluctuations at length scales comparable to visible-light wavelengths scatter light strongly"
    - "The refractive index changes abruptly as the two phases begin to merge"
    - "Liquid and gas layers form optical interference patterns"
  answer: 1
  explanation: "Near the critical point, the compressibility diverges and the correlation length ξ grows to macroscopic scales. This means density fluctuations occur on all length scales simultaneously, including those comparable to the wavelength of visible light. These fluctuations scatter light intensely (Rayleigh/Mie scattering), making the fluid appear milky-white. It is a direct signature of the diverging correlation length, not a phase transition color change."

- question: "Above the critical temperature, applying sufficient pressure will typically cause a substance to liquefy."
  type: true-false
  answer: false
  explanation: "This is the defining property of the critical point. Above T_c, there is no phase boundary between liquid and vapor — the two phases have merged into a single supercritical phase. No amount of pressure will cause liquefaction; you can only compress the supercritical fluid continuously. Liquefaction by isothermal compression is only possible below T_c."

- question: "At the critical point on a P-V diagram, the isotherm simultaneously has zero slope and an inflection point."
  type: true-false
  answer: true
  explanation: "This is the mathematical definition of the critical point: (∂P/∂V)_T = 0 (zero slope) and (∂²P/∂V²)_T = 0 (inflection point) are satisfied simultaneously. The first condition means liquid and gas are equally compressible; the second means there is no longer any sense in which one phase is denser than the other. These two conditions together uniquely determine T_c, P_c, and V_c for the van der Waals equation."

- question: "Why can the properties of a supercritical fluid be 'tuned' continuously by adjusting temperature and pressure, while this is not possible for a substance below T_c?"
  type: short-answer
  answer: "Below T_c, liquid and vapor are separated by a first-order phase boundary. Crossing that boundary causes discontinuous jumps in density, enthalpy, and other properties. Above T_c, the phase boundary no longer exists — properties (density, viscosity, diffusivity, solvent power) vary smoothly and continuously with T and P. This is why supercritical CO₂ can be dialed in as a gentle or aggressive solvent simply by adjusting conditions, with no abrupt transitions."
  explanation: "The tunability is a direct consequence of the absence of a phase boundary above T_c. Industrial applications like coffee decaffeination and pharmaceutical extraction exploit exactly this: supercritical CO₂ properties can be finely adjusted without ever crossing a discontinuous phase transition."
```

## Explainer

The van der Waals equation of state (P + a/V²)(V − b) = RT captures the idea that real gases have attractive interactions (the a/V² correction reduces effective pressure) and finite molecular volume (the b correction). On a P-V diagram, this equation predicts a family of isotherms with qualitatively different shapes depending on temperature. Below a certain temperature T_c, the isotherm develops a region with negative slope (∂P/∂V > 0), which is mechanically unstable. The **Maxwell construction** replaces this unphysical portion with a horizontal line at the vapor pressure, representing liquid-vapor coexistence. As temperature increases, the coexistence region shrinks — the gap between liquid and gas molar volumes narrows — until at T_c the two phases have exactly the same density and the distinction between them disappears.

At the **critical point** (T_c, P_c, V_c), the isotherm satisfies two simultaneous conditions: (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0. The first says the isotherm has zero slope — the liquid and gas are equally compressible. The second says it is an inflection point — there is no longer any sense in which one phase is denser than the other. For the van der Waals equation, these conditions give T_c = 8a/27Rb, P_c = a/27b², V_c = 3b, and the dimensionless critical compression factor P_cV_c/(RT_c) = 3/8. The fact that this ratio is a universal constant for van der Waals fluids (regardless of the values of a and b) is the first hint of **universality**: properties near the critical point are, to a surprising degree, independent of molecular details.

Near the critical point, fluctuations in density become enormous. Locally, regions of higher and lower density spontaneously form and dissolve on all length scales simultaneously — a phenomenon called **critical opalescence**, where the fluid scatters light strongly and becomes milky-white. This is because density fluctuations at wavelengths comparable to visible light are thermally excited when the compressibility diverges. The **correlation length** ξ — the spatial range over which density fluctuations are correlated — diverges as T → T_c from above: ξ ∝ |T − T_c|^{−ν}. All other singular properties follow power laws with their own **critical exponents**: the specific heat diverges as |T − T_c|^{−α}, the order parameter (density difference) vanishes as |T − T_c|^β below T_c, and the compressibility diverges as |T − T_c|^{−γ}.

Above T_c, no amount of pressure can liquefy the fluid — you can compress it arbitrarily without crossing a phase boundary. The result is a **supercritical fluid** that has liquid-like densities but gas-like transport properties (high diffusivity, low viscosity). Supercritical CO₂ (T_c = 31°C, P_c = 74 bar) is used industrially as a solvent in coffee decaffeination and pharmaceutical extraction precisely because its properties can be tuned continuously by adjusting temperature and pressure. This tunability is a direct consequence of the absence of a phase boundary — properties change smoothly, not discontinuously, as you vary the conditions above T_c.
