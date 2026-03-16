---
id: lever-rule
title: The Lever Rule and Phase Fraction Calculation
domain: engineering
course: materials-science
prerequisites:
- id: phase-diagrams-binary
  type: hard
- id: proportions
  type: soft
builds-toward:
- iron-carbon-phase-diagram
- heat-treatment-of-steels
tags:
- lever-rule
- phase-fraction
- composition
- two-phase
stage: formal-systems
status: validated
---

# The Lever Rule and Phase Fraction Calculation

## Core Idea
In a two-phase region of a binary phase diagram, the lever rule quantifies the relative amounts (mass fractions) of each phase present at a given overall composition and temperature. By reading the phase boundary compositions on either side of the overall composition and applying a simple inverse-proportion calculation — like a mechanical lever balanced at the overall composition — engineers can determine how much solid vs. liquid (or two distinct solid phases) is present. This calculation is fundamental to predicting microstructure after solidification or heat treatment.

## How It's Best Learned
Practice on the Pb-Sn eutectic diagram at several temperatures and overall compositions. Verify that the calculated fractions sum to 1 and that limiting cases (at a phase boundary) give 100% of one phase.

## Common Misconceptions
- The lever rule gives mass fractions of phases, not mole fractions of components — students frequently confuse these.
- The rule applies only inside two-phase regions; in single-phase regions the composition of the phase equals the overall composition.

## Explainer

A binary phase diagram tells you which phases are stable at a given temperature and overall composition. From your study of phase diagrams, you know how to read the phase boundaries and identify whether you are in a single-phase region or a two-phase region. What the diagram does not directly tell you is *how much* of each phase is present. That is exactly what the **lever rule** provides: a quantitative statement about the relative amounts of two coexisting phases derived from mass balance.

The physical reasoning is straightforward. Suppose you have a binary alloy of overall composition C₀ that lies in a two-phase (α + β) region at some temperature. Reading the phase diagram at that temperature, you find that the α phase has composition Cα (the left boundary) and the β phase has composition Cβ (the right boundary). The overall composition must be a weighted average of the two phase compositions: C₀ = f_α · Cα + f_β · Cβ, where f_α and f_β are the mass fractions (and f_α + f_β = 1). Solving these two equations gives **f_β = (C₀ − Cα)/(Cβ − Cα)** and **f_α = (Cβ − C₀)/(Cβ − Cα)**. Notice that each fraction is the distance from the overall composition to the *opposite* boundary, divided by the total two-phase field width — exactly like balancing a mechanical lever, with the overall composition as the fulcrum.

The analogy is worth visualizing: draw the two-phase field as a horizontal bar at the relevant temperature, with Cα on the left and Cβ on the right. Place the fulcrum (overall composition C₀) somewhere in the middle. The fraction of β is the length of the left arm (C₀ − Cα) divided by the total bar length (Cβ − Cα); the fraction of α is the right arm (Cβ − C₀) divided by the same total. A composition close to Cβ produces mostly β; a composition close to Cα produces mostly α. At exactly a phase boundary, you get 100% of one phase, which is the correct limiting behavior.

In practice, the lever rule is applied at every temperature during solidification to track how much solid and liquid are present as an alloy cools through a two-phase region. At the liquidus, the alloy is 100% liquid; at the solidus, 100% solid. Between them, the solid fraction increases continuously, and the lever rule tells you the fraction at each temperature. This quantitative picture connects directly to **Scheil solidification** models and to predicting **segregation** — the degree to which the first solid to form differs in composition from the last, which sets the severity of compositional gradients in a cast part. The lever rule is the foundation for all such microstructural predictions from phase diagrams.
