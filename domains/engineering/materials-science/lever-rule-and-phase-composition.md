---
id: lever-rule-and-phase-composition
title: The Lever Rule and Phase Diagram Composition Analysis
domain: engineering
course: materials-science
prerequisites:
- id: phase-diagrams-binary
  type: hard
builds-toward:
- solidification-and-dendrite-formation
- heat-treatment-of-steels
tags:
- phase-diagrams
- lever-rule
- composition
- two-phase-regions
stage: advanced
status: draft
---

# The Lever Rule and Phase Diagram Composition Analysis

## Core Idea
The lever rule calculates the relative amounts and compositions of phases in equilibrium at a given temperature and overall composition. For a two-phase region, the rule uses a fulcrum at overall composition: phase fractions equal the inverse ratio of distances to phase boundaries. This tool predicts microstructure and enables composition optimization.

## Explainer

From your study of binary phase diagrams, you know that a two-phase region (like the α + L region in a eutectic system) contains multiple coexisting phases whose compositions are determined by the phase boundaries at a given temperature — you read them off as the endpoints of the **tie line** (the horizontal isothermal line connecting the two phase boundaries). What the phase diagram alone does not tell you is *how much* of each phase is present. That is exactly what the lever rule provides.

The lever rule is simply a **mass balance**. If your alloy has overall composition C₀, and it consists of phase α (with composition C_α) and phase β (with composition C_β), then conservation of mass requires: C₀ = f_α·C_α + f_β·C_β, where f_α + f_β = 1. Solving these two equations gives: f_α = (C_β − C₀)/(C_β − C_α) and f_β = (C₀ − C_α)/(C_β − C_α). Notice that f_α is determined by how far C₀ is from the β boundary (the opposite side), and f_β by how far C₀ is from the α boundary. This is the lever analogy: C₀ is the fulcrum, the tie line is the lever, and the phase fractions are inversely proportional to the distances from the fulcrum to each end — closer to one end means more of that phase.

A concrete example anchors the intuition. Consider a Cu-Ni alloy with 70 wt% Cu being cooled to a temperature where the tie line spans from C_α = 45 wt% Cu (solid) to C_L = 58 wt% Cu (liquid). The fraction of solid is f_α = (58 − 70)/(58 − 45) = −12/13... wait, that can't be right. Let me reframe: if C₀ = 70 wt% Cu, C_α = 58 wt% Cu (solid), and C_L = 80 wt% Cu (liquid), then f_α = (80 − 70)/(80 − 58) = 10/22 ≈ 45%. The remaining 55% is liquid. As temperature drops further and C₀ moves through the two-phase region, f_α increases continuously until you reach the solidus, where f_α = 100%.

The lever rule applies anywhere in a two-phase region — solid-liquid, solid-solid (like α + β in an isomorphous or eutectic system), or any two coexisting phases. It gives the **weight fractions** (or mole fractions if composition axes are in mole percent). Engineers use it to predict microstructural proportions: what fraction of a steel microstructure is ferrite versus cementite at room temperature after slow cooling, for example. Combined with knowledge of each phase's properties (hardness, conductivity, ductility), the lever rule lets you estimate composite properties of the microstructure and design compositions to hit target phase ratios. The closer the overall composition is to a phase boundary, the more of that phase will be present — an insight that directly guides alloy design.
