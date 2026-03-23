---
id: thermodynamic-properties-and-equations-of-state
title: Thermodynamic Properties and Equations of State
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: entropy-intro
  type: hard
builds-toward:
- pure-substance-phase-diagrams
tags:
- properties
- state
- equations-of-state
stage: formal-systems
status: draft
---

# Thermodynamic Properties and Equations of State

## Core Idea
Thermodynamic properties (P, T, V, u, h, s) describe the state of matter; intensive properties are independent of mass while extensive properties depend on system size. An equation of state (like PV=RT for ideal gases) relates properties and reduces the number of independent variables needed to specify a system's state. Engineering systems often use simplified equations of state or property tables rather than exact molecular equations.

## How It's Best Learned
For ideal gases, memorize the equation PV=nRT and practice converting between specific and molar forms. For real fluids, learn to navigate property tables (steam tables, refrigerant tables) and understand when ideal gas assumption is reasonable. Recognize that specifying two independent intensive properties (usually T and P or T and v) fully determines all other properties.

## Common Misconceptions
- All six properties (P, T, V, u, h, s) are independent; only two are independent for a pure substance.
- Enthalpy h is only relevant to open systems; it is equally important for understanding closed systems.
- The ideal gas law is always accurate; it fails near saturation and at high pressures.

## Questions

```yaml
- question: "You know that a sample of pure, superheated steam has temperature T = 300°C and pressure P = 1 MPa. How many additional intensive properties (specific volume, specific enthalpy, specific entropy) can be determined from this information alone?"
  type: multiple-choice
  options:
    - "None — each property must be measured independently"
    - "Only specific volume — temperature and pressure don't constrain energy or entropy"
    - "One — you need at least three properties to pin down the full state"
    - "All of them — for a pure simple compressible substance, two independent intensive properties fully determine the state"
  answer: 3
  explanation: "This is the state postulate: for a pure, simple compressible substance (no electrical, magnetic, or surface effects), exactly two independent intensive properties completely determine the thermodynamic state. Every other intensive property is fixed. Knowing T and P for superheated steam locates a unique point in the steam tables, from which v, u, h, and s can all be read directly. The key qualification is 'independent' — during a phase change, T and P are not independent (they move together along the saturation curve), and a third property like quality x is needed."

- question: "A student solving a steam problem wants to find specific enthalpy. She reasons: 'The steam tables are complicated, so I'll just use h = u + Pv with the ideal gas law to get v, then add Pv to u from the table.' The steam is at 2 MPa and 200°C. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Enthalpy is an extensive property, so specific enthalpy cannot be looked up in tables"
    - "At 2 MPa and 200°C, steam is near or in the saturation region where the ideal gas law fails significantly — the steam tables already account for real-gas behavior that the ideal gas law ignores"
    - "The ideal gas law applies only to monatomic gases, not steam"
    - "There is nothing wrong; ideal gas and steam tables give the same answer for steam above 100°C"
  answer: 1
  explanation: "At 2 MPa, the saturation temperature of water is about 212°C, so steam at 200°C and 2 MPa is actually subcooled liquid (or on the saturation boundary) — far from ideal gas conditions. The ideal gas law PV = RT assumes non-interacting point particles, a model that breaks down completely near phase transitions and at elevated pressures. Steam tables are compiled from accurate equations of state (like the IAPWS formulations) and account for real molecular interactions. Using ideal gas in this regime would produce large errors. The steam tables are the correct tool; the ideal gas law is a poor approximation here."

- question: "During a phase change (e.g., water boiling at 100°C and 1 atm), temperature and pressure are independent intensive properties that together uniquely determine all other thermodynamic properties of the two-phase mixture."
  type: true-false
  answer: false
  explanation: "False. This is the key exception to the state postulate as commonly stated. During a phase change, temperature and pressure are not independent — they are linked by the saturation curve (at 1 atm, the boiling point is exactly 100°C; change one and the other changes). A two-phase mixture at these conditions is not fully specified by T and P alone; you also need the quality x (the mass fraction of vapor) to determine v, u, h, and s. Once in the single-phase region (subcooled liquid or superheated vapor), T and P are again independent and two properties suffice."

- question: "Specific enthalpy (h = u + Pv) is an intensive property — its value does not change if you double the amount of substance while keeping temperature and pressure constant."
  type: true-false
  answer: true
  explanation: "True. Specific properties are defined per unit mass (or per mole), making them intensive. If you double the mass of steam at fixed T and P, the total enthalpy H doubles, but the specific enthalpy h = H/m stays the same. This is why steam tables list specific properties: once you know h for the given state, you multiply by mass to get the total. Distinguishing intensive (specific) from extensive (total) properties is essential — you look up intensive properties in tables, then scale by system size."

- question: "What does the state postulate say, and why is it practically useful for engineering thermodynamics calculations?"
  type: short-answer
  answer: "The state postulate says that for a pure, simple compressible substance, two independent intensive properties completely determine the thermodynamic state — every other intensive property is fixed. In practice, this means you only need to know two things (typically T and P, or T and v) to look up or calculate all others (h, u, s, v). This reduces an apparently six-dimensional problem (six common properties) to a two-dimensional lookup. It is what makes steam tables and refrigerant tables work: two inputs locate a unique row, and the remaining columns give you everything else."
  explanation: "Without the state postulate, every thermodynamic problem would require measuring all properties independently for each system — impractical for engineering design. The postulate reflects deep physics: for a simple compressible system, the internal energy is a function of exactly two independent variables (often taken as T and v), and all other properties follow from it through the fundamental relations. This is why specifying two independent properties really does pin down the entire state."
```

## Explainer

From your study of entropy, you've already encountered several thermodynamic properties: temperature T, pressure P, internal energy u, and entropy s. The organizing principle that connects all of them is the **state postulate**: for a pure, simple compressible substance (no electrical, magnetic, or surface effects), specifying two independent intensive properties completely determines the thermodynamic state. Every other property is then fixed. This is not obvious — it is a result, rooted in the structure of the fundamental thermodynamic relations — but it is the rule that makes property calculations tractable.

**Intensive properties** are independent of system size: temperature, pressure, specific volume v (volume per unit mass), specific internal energy u, specific enthalpy h = u + Pv, and specific entropy s. **Extensive properties** scale with mass: total volume V, total internal energy U, total enthalpy H. In engineering calculations, you almost always work with specific (per unit mass) intensive properties and multiply by mass to get totals. This distinction matters practically: if you double the mass of steam in a vessel while keeping T and P the same, h (per unit mass) is unchanged but H (total) doubles.

An **equation of state** is the mathematical relationship that ties the state variables together and reduces the number of independent variables. The ideal gas equation Pv = RT is the simplest: given any two of P, T, and v, the third is determined. This equation derives from treating gas molecules as non-interacting point masses — a model that works well for most gases far from saturation and at moderate pressures. It fails predictably near phase transitions and at high pressures where molecular volume and intermolecular attractions become significant. The van der Waals equation and the Peng-Robinson equation are more accurate for real gases in those regimes.

For water and many refrigerants, no simple equation of state is accurate enough for engineering design. Instead, **property tables** (steam tables, refrigerant tables) provide tabulated values of u, h, s, and v as functions of T and P across subcooled liquid, saturated, and superheated vapor regions. The practical skill is navigation: first identify the phase by comparing the given temperature or pressure to saturation values, then read the appropriate table region, then interpolate between entries if needed. Specifying two independent properties locates a point in the table; the remaining properties are read from that row. The state postulate is why two inputs always suffice — and why memorizing which two properties are given (rather than which six might be listed) is the key to solving any thermodynamic problem efficiently.
