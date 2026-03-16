---
id: phase-diagrams-binary
title: Binary Phase Diagrams
domain: engineering
course: materials-science
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: entropy-and-gibbs-free-energy
  type: hard
- id: phase-diagrams
  type: soft
- id: phase-transitions
  type: soft
- id: phase-equilibrium-thermodynamics-materials
  type: soft
- id: phase-diagrams-binary-mixtures
  type: soft
builds-toward:
- lever-rule
- iron-carbon-phase-diagram
tags:
- phase-diagram
- binary-alloy
- liquidus
- solidus
- eutectic
stage: formal-systems
status: validated
---

# Binary Phase Diagrams

## Core Idea
A binary phase diagram maps the equilibrium phases present for all compositions and temperatures of a two-component system. Key features include the liquidus (above which the system is fully liquid), solidus (below which it is fully solid), and special invariant points such as the eutectic (a single liquid transforming simultaneously into two solids). Reading a phase diagram for a given alloy composition and temperature reveals which phases exist, their compositions, and — via the lever rule — their relative amounts. Phase diagrams are the roadmap for heat treatment and solidification processing.

## How It's Best Learned
Start with the isomorphous (fully soluble) Cu-Ni system to practice reading single- and two-phase regions, then progress to the eutectic Pb-Sn system. Draw cooling curves for different compositions to connect diagram features to solidification behavior.

## Common Misconceptions
- Phase diagrams represent equilibrium — real solidification can deviate significantly due to incomplete diffusion, producing cored (compositionally graded) microstructures.
- The eutectic composition is not necessarily 50/50; it is defined by thermodynamics and varies by system.

## Questions

```yaml
- question: "On a binary eutectic phase diagram, an alloy of composition X is cooled to a temperature where the liquidus and solidus lines bracket it in a two-phase (liquid + solid) region. What does the lever rule tell you?"
  type: multiple-choice
  options: ["The total composition of each phase present", "The relative amounts (mass fractions) of the two phases present", "The temperature at which solidification will complete", "Whether the microstructure is proeutectoid or hypereutectoid"]
  answer: 1
  explanation: "The lever rule uses the distances between the alloy composition and the two phase-boundary compositions at a given temperature to compute the fraction of each phase. It does not give phase compositions (those are read directly from the diagram boundaries) nor transformation temperatures."

- question: "A binary phase diagram always represents the equilibrium state, so real alloys cooled at normal rates will match it exactly."
  type: true-false
  answer: false
  explanation: "Phase diagrams show equilibrium, which requires infinitely slow cooling so diffusion can fully homogenize each phase. At practical cooling rates, diffusion is incomplete, producing cored (compositionally graded) microstructures whose compositions deviate from equilibrium predictions."

- question: "What distinguishes the eutectic point on a binary phase diagram from other points in the two-phase liquid+solid region?"
  type: short-answer
  answer: "The eutectic point is an invariant point — a unique composition and temperature at which a single liquid phase transforms simultaneously into two distinct solid phases. No other composition melts or solidifies at a single fixed temperature; instead, they pass through a temperature range with coexisting liquid and solid."
  explanation: "At the eutectic, the Gibbs phase rule gives zero degrees of freedom (for a binary system at fixed pressure): F = C − P + 1 = 2 − 3 + 1 = 0. This means composition and temperature are both fixed, so the transformation occurs at one sharp temperature — the eutectic temperature."
```

## Explainer

A binary phase diagram is a map of a two-component system: one axis is temperature, the other is composition (often expressed as weight percent or mole fraction of one component), and each region of the map tells you which phases are present at equilibrium. You read it like a topographic map — the boundary lines are where phase transitions occur, and the regions between them describe stable coexistence.

The most important lines are the **liquidus** (above it, everything is liquid) and the **solidus** (below it, everything is solid). Between them is a two-phase region where liquid and solid coexist. For a given alloy composition and temperature that falls in this region, you can immediately read off two things from the diagram: the *compositions* of each phase (where a horizontal tie-line meets each boundary) and the *amounts* of each phase (from the lever rule). The lever rule is mechanical intuition applied to composition: the fraction of one phase equals how far the overall composition is from that phase's boundary, divided by the total span between the two boundaries.

The **eutectic point** is the most distinctive feature of many binary diagrams. It is the one composition that melts at the lowest possible temperature for the system, and at that temperature a single liquid transforms into two solid phases simultaneously. The Pb-Sn eutectic (used in solder) is the classic example: at 61.9% Sn and 183 °C, liquid transforms directly into alternating lamellae of Sn-rich and Pb-rich solid. Compositions richer or leaner in Sn pass through a mushy two-phase region during cooling rather than transforming at a sharp temperature.

The critical caveat for all phase diagrams is that they describe **equilibrium** — what you get if you cool infinitely slowly, giving every atom time to diffuse to its equilibrium position. Real cooling rates are finite, which means diffusion is often incomplete. The result is **coring**: the first solid to form is enriched in the higher-melting component, while later-solidifying layers are leaner, creating a composition gradient within each grain. The actual microstructure can differ substantially from what the diagram would predict. Homogenization heat treatments exist precisely to drive real alloys back toward equilibrium by allowing solid-state diffusion to proceed.
