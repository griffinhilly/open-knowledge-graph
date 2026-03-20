---
id: binary-phase-diagrams-equilibrium
title: Binary Phase Diagrams and Equilibrium
domain: engineering
course: materials-science
prerequisites:
- id: phase-equilibrium-thermodynamics-materials
  type: hard
- id: phase-diagrams-binary-mixtures
  type: hard
builds-toward:
- heat-treatment-steel-processing
tags:
- phase-diagram
- eutectic
- solid-solution
- miscibility-gap
- lever-rule
stage: advanced
status: draft
---

# Binary Phase Diagrams and Equilibrium

## Core Idea
Binary phase diagrams (composition vs. temperature at constant pressure) map equilibrium phases as a function of composition and temperature. Key features include solid solutions (single phase), two-phase regions, and invariant points (eutectic, peritectic, congruent melting). The lever rule relates phase compositions and fractions at equilibrium. Phase diagrams are essential tools for predicting microstructure and designing heat treatment paths to achieve desired properties.

## Explainer

A binary phase diagram is a map of thermodynamic equilibrium: for any combination of temperature and composition in a two-component system, the diagram tells you which phases are present and what their compositions are. The x-axis is composition (from pure component A on the left to pure component B on the right, usually expressed as weight or mole percent of B), and the y-axis is temperature. At any point on the map, you are at equilibrium — meaning the system has had time to reach its lowest free energy configuration. In practice, real materials are often not at equilibrium, but the phase diagram gives the target that any process is driving toward.

The most important skill is reading **phase regions**. A single-phase region (marked α, β, or liquid) means the entire system exists as one phase. A two-phase region contains a mixture of two phases whose compositions are given by the endpoints of the horizontal **tie line** drawn at that temperature. If you are in the α + L (solid plus liquid) region, the solid has the composition at the left end of the tie line and the liquid has the composition at the right end — regardless of where in the region your overall composition falls. The **lever rule** then gives the *fraction* of each phase: the fraction of the left-phase equals the distance from your composition to the right endpoint, divided by the total tie line length. Memorizing the formula is less useful than understanding why: the lever is a mass balance — the further your overall composition is from one phase's composition, the more of the other phase must be present to balance.

**Eutectic** systems are the most commonly encountered two-component diagram. The eutectic point is the unique composition that melts (and solidifies) at the lowest possible temperature — lower than either pure component. At the eutectic temperature, three phases coexist simultaneously (liquid + two solids), and this invariant point has zero degrees of freedom (Gibbs phase rule: F = C − P + 2 = 2 − 3 + 1 = 0 at fixed pressure). Compositions to the left of the eutectic are **hypoeutectic**: on cooling, some primary solid forms first, enriching the remaining liquid toward the eutectic composition, until the eutectic reaction completes. The resulting **microstructure** — how much primary phase versus lamellar eutectic — is directly predicted by the lever rule applied just above the eutectic temperature.

Phase diagrams are the engineer's recipe card for microstructure. The path you take through the diagram during heating and cooling determines what microstructure you get. Slow cooling follows the equilibrium diagram; fast cooling (quenching) can suppress equilibrium transformations and trap high-temperature phases in a metastable state. This is the basis of heat treatment: austenitize steel (take it into the single-phase γ region), then control the cooling rate to get martensite (fast quench), bainite (intermediate), or pearlite (slow cool). Every heat treatment cycle makes sense once you can read the relevant region of the phase diagram and understand what transformations the composition must pass through.
