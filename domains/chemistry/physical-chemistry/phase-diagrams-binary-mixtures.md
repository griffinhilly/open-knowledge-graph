---
id: phase-diagrams-binary-mixtures
title: Phase Diagrams of Binary Mixtures
domain: chemistry
course: physical-chemistry
prerequisites:
- id: phase-changes-and-diagrams
  type: hard
- id: solution-thermodynamics-activity-models
  type: hard
tags:
- phase-diagrams
- equilibrium
- binary-systems
- azeotropes
stage: advanced
status: validated
---

# Phase Diagrams of Binary Mixtures

## Core Idea
Binary phase diagrams (T-x, P-x) map equilibrium regions (vapor, liquid, solid) and show key features: eutectic points (lowest-melting mixtures), peritectic points, azeotropes (same liquid and vapor composition), and immiscibility regions. These are derived from Gibbs-Duhem relations and activity models. Understanding phase diagrams is essential for distillation, crystallization, and alloy design.

## Questions

```yaml
- question: "A binary liquid mixture forms a maximum-boiling azeotrope (a composition with a higher boiling point than either pure component). What does this imply about the intermolecular interactions in the mixture?"
  type: multiple-choice
  options:
    - "The mixture has weaker interactions than either pure component, reducing vapor pressure and raising boiling point"
    - "The mixture has stronger interactions between unlike molecules than in either pure component, reducing vapor pressure and raising boiling point"
    - "The two components have identical vapor pressures at all compositions"
    - "The mixture violates Raoult's Law by having a higher mole fraction in the vapor than in the liquid"
  answer: 1
  explanation: "A maximum-boiling azeotrope arises from negative deviations from Raoult's Law: A–B interactions are stronger than A–A and B–B interactions. This reduces the escaping tendency (vapor pressure) of both components below the ideal Raoult's Law prediction, lowering the total vapor pressure and raising the boiling point. The ethanol–water system and HCl–water system are examples. Contrast this with a minimum-boiling azeotrope (e.g., ethanol–hexane), where A–B interactions are weaker, vapor pressure is elevated, and boiling point is depressed."

- question: "An azeotropic mixture can be separated into its pure components by standard fractional distillation."
  type: true-false
  answer: false
  explanation: "At the azeotropic composition, the vapor and liquid have identical compositions, so every distillation stage reproduces the azeotrope without enriching either component. The distillate and bottoms converge to the azeotrope, not to pure components. Breaking an azeotrope requires different techniques: pressure-swing distillation (exploits the fact that azeotropic composition shifts with pressure), extractive distillation (adds a third component that alters relative volatility), or membrane separation. This is a critical practical limitation in industrial separations."

- question: "What is the eutectic point in a binary solid-liquid phase diagram, and why is it useful in materials processing?"
  type: short-answer
  answer: "The eutectic point is the unique composition and temperature at which a binary mixture has the lowest possible melting point — at this point, two solid phases are in equilibrium with the liquid simultaneously. Below the eutectic temperature, the entire system is solid; above it, a liquid phase exists. The eutectic mixture melts and solidifies sharply (like a pure compound) rather than over a range, and at a lower temperature than either pure component."
  explanation: "This is useful in materials processing because eutectic compositions can be melted and cast at lower temperatures (saving energy), solidify with a fine microstructure (rapid simultaneous solidification of both phases), and can be designed with specific melting temperatures. Classic applications include lead-tin solder (eutectic at 183°C), aluminum-silicon casting alloys, and pharmaceutical co-crystals designed for precise dissolution behavior."
```

## Explainer

A single-component phase diagram maps the stable phase of a pure substance as a function of temperature and pressure. Binary phase diagrams extend this idea to mixtures of two components, adding composition as a third variable. The result is typically displayed as a T-x diagram (temperature vs. mole fraction at constant pressure) or a P-x diagram (pressure vs. mole fraction at constant temperature). These diagrams encode enormous practical information about how mixtures behave when heated, cooled, or partially vaporized.

In a vapor-liquid T-x diagram for a non-ideal system, the key feature is the two-phase envelope defined by the bubble-point curve (below which all liquid) and the dew-point curve (above which all vapor). At any temperature between these curves, liquid and vapor coexist with compositions given by the endpoints of a horizontal tie line. Raoult's Law predicts ideal behavior; real systems deviate because unlike-molecule interactions (A–B) may be stronger or weaker than like-molecule interactions (A–A, B–B). Stronger A–B interactions suppress vapor pressure below ideal predictions (negative deviation), pushing the bubble-point and dew-point curves upward and potentially creating a maximum-boiling azeotrope. Weaker A–B interactions do the opposite, creating a minimum-boiling azeotrope. At an azeotrope, liquid and vapor compositions are identical — the tie line degenerates to a point — and the mixture cannot be further separated by simple distillation.

In solid-liquid T-x diagrams (relevant for alloys, pharmaceuticals, and salt systems), the most important feature is the eutectic point. For two components that are mutually soluble as liquids but insoluble as solids, cooling any liquid mixture causes one solid to crystallize preferentially, shifting the remaining liquid composition toward the eutectic. At the eutectic temperature, the liquid simultaneously solidifies into two solid phases — a process called eutectic solidification — producing a characteristic fine-grained two-phase microstructure. The eutectic is the thermodynamic minimum of the liquidus curve; no liquid of that composition can exist below it. Systems with peritectic points are more complex: one solid phase partially transforms into a different solid plus liquid on heating, which can trap unequilibrated phases during rapid cooling.

Both diagram types are derived from the same thermodynamic foundation: the Gibbs-Duhem equation constrains how the chemical potentials of components in a mixture must vary together, and activity models (Raoult's Law, Margules, van Laar, NRTL) quantify deviations from ideal behavior. The phase boundaries are located by finding conditions where chemical potentials are equal in coexisting phases — exactly the criterion for thermodynamic equilibrium. Familiarity with binary phase diagrams is essential for distillation column design, alloy selection, crystallization purification, and formulating stable pharmaceutical excipients.
