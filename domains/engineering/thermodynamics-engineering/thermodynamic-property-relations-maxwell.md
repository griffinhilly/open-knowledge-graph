---
id: thermodynamic-property-relations-maxwell
title: Maxwell Relations and Thermodynamic Property Derivations
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: second-law-thermodynamics-entropy
  type: hard
- id: differential-equations-intro
  type: hard
tags:
- maxwell-relations
- property-relations
- thermodynamic-identities
stage: formal-systems
status: validated
---

# Maxwell Relations and Thermodynamic Property Derivations

## Core Idea
Maxwell relations are derived from the equality of mixed partial derivatives of thermodynamic potentials (U, H, F, G), linking different properties without direct measurement. For example, (∂S/∂V)_T = (∂P/∂T)_V enables calculation of entropy from P-T-V data. These relations form the theoretical foundation for property tables and reduced-variable equations of state used throughout engineering.

## Questions

```yaml
- question: "An engineer needs to compute how entropy changes with pressure at constant temperature for steam. Entropy cannot be measured directly. Which Maxwell relation makes this calculation possible from measurable PVT data?"
  type: multiple-choice
  options:
    - "(∂T/∂V)_S = −(∂P/∂S)_V — derived from internal energy U(S,V)"
    - "(∂S/∂P)_T = −(∂V/∂T)_P — derived from Gibbs free energy G(T,P)"
    - "(∂S/∂V)_T = (∂P/∂T)_V — derived from Helmholtz free energy A(T,V)"
    - "(∂T/∂P)_S = (∂V/∂S)_P — derived from enthalpy H(S,P)"
  answer: 1
  explanation: "The engineer needs (∂S/∂P)_T — how entropy changes with pressure at constant temperature. This is the Maxwell relation from the Gibbs free energy: dG = −SdT + VdP, so applying the Schwarz symmetry condition to the T and P variables gives (∂S/∂P)_T = −(∂V/∂T)_P. The right-hand side is −1 times the thermal expansion coefficient times the molar volume — both measurable from PVT experiments. Option C gives (∂S/∂V)_T, which answers a different question (entropy vs. volume at constant T). Each Maxwell relation answers a specific question about which pair of variables is involved."

- question: "What is the mathematical origin of Maxwell relations?"
  type: multiple-choice
  options:
    - "They are empirical correlations fit to experimental PVT data for common fluids"
    - "They follow from the Schwarz (Clairaut) theorem: thermodynamic potentials are exact differentials, so their mixed second partial derivatives must be equal regardless of the order of differentiation"
    - "They are approximations derived from the ideal gas law and break down for real substances at high pressure"
    - "They follow from the zeroth law of thermodynamics and the definition of equilibrium temperature"
  answer: 1
  explanation: "Maxwell relations are purely mathematical consequences of the exactness of thermodynamic differentials. For any function Z with exact differential dZ = M dx + N dy, the Schwarz theorem requires (∂M/∂y)_x = (∂N/∂x)_y because ∂²Z/∂x∂y = ∂²Z/∂y∂x. The four Maxwell relations apply this symmetry to U(S,V), H(S,P), A(T,V), and G(T,P) respectively. They are valid for any substance — ideal gas, real gas, liquid, solid — because they rest entirely on mathematics, not on any particular equation of state."

- question: "Maxwell relations allow engineers and scientists to calculate entropy changes from measurements of pressure, volume, and temperature, without ever needing to measure entropy directly."
  type: true-false
  answer: true
  explanation: "This is the practical power of Maxwell relations. Entropy is not accessible to a thermometer or pressure gauge. But (∂S/∂V)_T = (∂P/∂T)_V means that measuring how pressure varies with temperature at constant volume (a PVT experiment) tells you how entropy varies with volume at constant temperature. Combined with specific heat measurements (which give (∂S/∂T) at constant pressure or volume), you can integrate along any path in state space to build a complete entropy surface. This is literally how steam tables and refrigerant property tables are constructed."

- question: "The Maxwell relation (∂S/∂V)_T = (∂P/∂T)_V applies primarily to ideal gases; for real gases and liquids, the relationship between entropy and PVT variables requires a different approach."
  type: true-false
  answer: false
  explanation: "Maxwell relations are substance-independent — they hold for any material in thermodynamic equilibrium, including real gases, liquids, and solids. The relation (∂S/∂V)_T = (∂P/∂T)_V is derived from the exactness of the Helmholtz free energy differential, which holds universally. For an ideal gas, (∂P/∂T)_V = nR/V, giving a simple result. For a van der Waals gas, the same relation with the van der Waals P(T,V) yields a different but equally rigorous entropy expression. Real-fluid property tables (steam, refrigerants) are built by applying Maxwell relations to empirical equations of state that fit real experimental data."

- question: "How are steam tables and refrigerant property tables actually constructed? What role do Maxwell relations play?"
  type: short-answer
  answer: "Steam tables and refrigerant tables list values of entropy, enthalpy, and internal energy that cannot be directly measured with instruments. The construction process uses two types of experimental data: (1) PVT measurements across the fluid's state space, and (2) specific heat (calorimetry) measurements at various conditions. Maxwell relations connect these measurable quantities to the unmeasurable ones. For example, (∂S/∂P)_T = −(∂V/∂T)_P means that measuring the thermal expansion coefficient (how volume changes with temperature at constant pressure) gives how entropy changes with pressure at constant temperature. Starting from a reference state where entropy and enthalpy are defined by convention, engineers integrate along paths in state space using Maxwell relations and specific heat data to build the complete property surfaces tabulated in engineering references."
  explanation: "This question tests whether students can close the loop between the abstract mathematics of Maxwell relations and their engineering significance. The key insight is that property tables are not measured directly — they are computed by applying thermodynamic identities to data that can be measured. A student who says 'Maxwell relations let you compute entropy' but cannot explain the integration procedure or what experimental data feeds in has partial understanding."
```

## Explainer

Your prerequisite on the second law established the fundamental thermodynamic relation: dU = TdS − PdV. This tells you that internal energy U is a natural function of entropy S and volume V, with the partial derivatives (∂U/∂S)_V = T and (∂U/∂V)_S = −P. Your calculus prerequisite on differential equations established the **Schwarz (Clairaut) symmetry condition**: for any function f(x, y) with continuous second partial derivatives, ∂²f/∂x∂y = ∂²f/∂y∂x. Thermodynamic potentials are exact differentials, so this symmetry must hold. The **Maxwell relations** are what you get when you apply this symmetry to each of the four thermodynamic potentials.

Starting with U(S, V): the symmetry of mixed partials gives (∂T/∂V)_S = −(∂P/∂S)_V. For the **enthalpy** H = U + PV, the differential is dH = TdS + VdP, so H is natural in (S, P), and the relation is (∂T/∂P)_S = (∂V/∂S)_P. For the **Helmholtz free energy** A = U − TS, the differential is dA = −SdT − PdV, natural in (T, V), giving (∂S/∂V)_T = (∂P/∂T)_V. For the **Gibbs free energy** G = U + PV − TS, the differential is dG = −SdT + VdP, natural in (T, P), giving (∂S/∂P)_T = −(∂V/∂T)_P. These four are the Maxwell relations.

The practical importance is that **entropy is not directly measurable**, but pressure, volume, and temperature are. The Helmholtz relation (∂S/∂V)_T = (∂P/∂T)_V allows you to compute entropy changes from PVT data: measuring how pressure changes with temperature at constant volume gives you how entropy changes with volume at constant temperature. For an ideal gas, (∂P/∂T)_V = nR/V, so (∂S/∂V)_T = nR/V — consistent with what you know. For a real gas described by a van der Waals or Peng-Robinson equation of state, the same procedure yields entropy corrections to the ideal-gas value. This is how steam tables and refrigerant tables are constructed: experimental PVT data and specific heat measurements feed into Maxwell relations and other thermodynamic identities to derive the tabulated entropy, enthalpy, and internal energy values.

More broadly, Maxwell relations are instances of a pattern: whenever you have an exact differential dZ = M dx + N dy, the relation (∂M/∂y)_x = (∂N/∂x)_y holds. This pattern appears throughout thermodynamics — in Gibbs-Duhem relations, in the Clausius-Clapeyron equation, in chemical potential relations — making the mathematical technique as important as any specific relation. Recognizing that a thermodynamic identity follows from the symmetry of mixed partials is a key skill for deriving unfamiliar relations from first principles.
