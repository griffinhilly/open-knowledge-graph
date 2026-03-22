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

## Questions

```yaml
- question: "An alloy has an overall composition of 30 wt% B. At a given temperature it falls in the α + liquid two-phase region. The tie line shows the α phase has composition 20 wt% B and the liquid phase has composition 50 wt% B. What is the weight fraction of liquid?"
  type: multiple-choice
  options:
    - "50% — the overall composition is midway between the two endpoints"
    - "33% — calculated as (30 − 20) / (50 − 20)"
    - "67% — the overall composition is closer to the liquid endpoint"
    - "30% — the weight fraction equals the overall composition"
  answer: 1
  explanation: "The lever rule gives the fraction of each phase by mass balance. Fraction of liquid = (x_overall − x_alpha) / (x_liquid − x_alpha) = (30 − 20) / (50 − 20) = 10/30 ≈ 33%. The key insight is that you measure the distance from the overall composition to the *opposite* phase's endpoint. Because the overall composition is only 10 units from the α endpoint but 20 units from the liquid endpoint, less of the liquid is needed to balance the mass — so the fraction of liquid is the smaller number. Option A incorrectly reads the midpoint as 50/50."

- question: "At the eutectic point in a binary system at constant pressure, how many phases coexist simultaneously, and what does this imply about the system's degrees of freedom?"
  type: multiple-choice
  options:
    - "One phase; one degree of freedom (temperature can vary)"
    - "Two phases (liquid + one solid); one degree of freedom"
    - "Three phases (liquid + two solids); zero degrees of freedom — temperature and compositions are all fixed"
    - "Two phases; zero degrees of freedom because composition is fixed at the eutectic"
  answer: 2
  explanation: "At the eutectic point, liquid and both solid phases coexist simultaneously: three phases in a two-component system. Applying the Gibbs phase rule at constant pressure: F = C − P + 1 = 2 − 3 + 1 = 0. Zero degrees of freedom means the eutectic is an invariant point — both the temperature and the compositions of all three phases are fixed. You cannot change temperature or composition while keeping all three phases in equilibrium. This is why the eutectic appears as a single point on the diagram, not a region."

- question: "In a two-phase region of a binary phase diagram, the composition of each phase depends on the overall alloy composition."
  type: true-false
  answer: false
  explanation: "Phase compositions in a two-phase region are determined entirely by the tie line endpoints at that temperature — they do NOT change with overall composition. If you move horizontally across a two-phase region (changing overall composition while holding temperature constant), the tie line stays the same, so the compositions of both phases remain constant. What changes is only the *proportion* (fraction) of each phase, not what each phase is made of. This is one of the most important — and commonly missed — features of phase diagrams."

- question: "The eutectic composition in a binary system melts at a lower temperature than either pure component."
  type: true-false
  answer: true
  explanation: "This is the defining feature of a eutectic: it is the composition with the lowest melting point in the entire system, lower than either pure A or pure B. This happens because mixing lowers the free energy of the liquid phase more than that of the solids, stabilizing the liquid to lower temperatures. Practically, this is why lead-tin solder (near the eutectic) melts at ~183°C while pure lead melts at 327°C and pure tin at 232°C."

- question: "Explain why the lever rule uses the distance to the *opposite* phase's endpoint to calculate the fraction of a given phase — what physical principle underlies this?"
  type: short-answer
  answer: "The lever rule is a mass balance. For the overall composition to equal the weighted sum of the two phase compositions, a phase that is far from the overall composition must be present in a smaller amount, while a phase close to the overall composition must be present in a larger amount. Measuring the distance to the *opposite* endpoint captures how much of that phase must 'pull' the average toward the overall value. It works exactly like a lever or see-saw: the further a phase composition is from the fulcrum (overall composition), the less weight it needs on that side to balance."
  explanation: "If overall = 30%, α = 20%, liquid = 50%, then the liquid must be 'balanced' by enough α to bring the average to 30%. Since liquid (50%) is far above the target and α (20%) is close below, you need less liquid and more α — and the lever rule quantifies this. The formula fraction_liquid = (x_overall − x_α) / (x_liq − x_α) directly expresses this distance-weighting logic."
```

## Explainer

A binary phase diagram is a map of thermodynamic equilibrium: for any combination of temperature and composition in a two-component system, the diagram tells you which phases are present and what their compositions are. The x-axis is composition (from pure component A on the left to pure component B on the right, usually expressed as weight or mole percent of B), and the y-axis is temperature. At any point on the map, you are at equilibrium — meaning the system has had time to reach its lowest free energy configuration. In practice, real materials are often not at equilibrium, but the phase diagram gives the target that any process is driving toward.

The most important skill is reading **phase regions**. A single-phase region (marked α, β, or liquid) means the entire system exists as one phase. A two-phase region contains a mixture of two phases whose compositions are given by the endpoints of the horizontal **tie line** drawn at that temperature. If you are in the α + L (solid plus liquid) region, the solid has the composition at the left end of the tie line and the liquid has the composition at the right end — regardless of where in the region your overall composition falls. The **lever rule** then gives the *fraction* of each phase: the fraction of the left-phase equals the distance from your composition to the right endpoint, divided by the total tie line length. Memorizing the formula is less useful than understanding why: the lever is a mass balance — the further your overall composition is from one phase's composition, the more of the other phase must be present to balance.

**Eutectic** systems are the most commonly encountered two-component diagram. The eutectic point is the unique composition that melts (and solidifies) at the lowest possible temperature — lower than either pure component. At the eutectic temperature, three phases coexist simultaneously (liquid + two solids), and this invariant point has zero degrees of freedom (Gibbs phase rule: F = C − P + 2 = 2 − 3 + 1 = 0 at fixed pressure). Compositions to the left of the eutectic are **hypoeutectic**: on cooling, some primary solid forms first, enriching the remaining liquid toward the eutectic composition, until the eutectic reaction completes. The resulting **microstructure** — how much primary phase versus lamellar eutectic — is directly predicted by the lever rule applied just above the eutectic temperature.

Phase diagrams are the engineer's recipe card for microstructure. The path you take through the diagram during heating and cooling determines what microstructure you get. Slow cooling follows the equilibrium diagram; fast cooling (quenching) can suppress equilibrium transformations and trap high-temperature phases in a metastable state. This is the basis of heat treatment: austenitize steel (take it into the single-phase γ region), then control the cooling rate to get martensite (fast quench), bainite (intermediate), or pearlite (slow cool). Every heat treatment cycle makes sense once you can read the relevant region of the phase diagram and understand what transformations the composition must pass through.
