---
id: stress-strain-behavior
title: Stress-Strain Behavior and Elastic Properties
domain: engineering
course: materials-science
prerequisites:
- id: equilibrium-rigid-bodies
  type: hard
- id: free-body-diagrams
  type: soft
- id: static-equilibrium
  type: soft
- id: newtons-second-law
  type: soft
builds-toward:
- mechanical-testing-methods
- plastic-deformation-mechanisms
- fracture-mechanics
- polymer-mechanical-behavior
tags:
- stress
- strain
- youngs-modulus
- elastic
- plastic
stage: formal-systems
status: draft
---

# Stress-Strain Behavior and Elastic Properties

## Core Idea
Engineering stress is force divided by original cross-sectional area; engineering strain is change in length divided by original length. In the elastic regime, stress and strain are linearly proportional via Young's modulus (E = σ/ε), which reflects atomic bond stiffness. Beyond the yield point, permanent plastic deformation occurs. The full stress-strain curve encodes yield strength, ultimate tensile strength, ductility (elongation to fracture), and toughness (area under the curve). These properties are the primary language of structural materials selection.

## How It's Best Learned
Conduct or simulate a tensile test and annotate the resulting curve: elastic region, yield point, strain hardening, necking, and fracture. Compare curves for a brittle ceramic, a ductile metal, and an elastomer to see the full range of material behaviors.

## Common Misconceptions
- True stress and engineering stress diverge significantly after necking begins; engineering stress decreases while true stress continues to rise.
- The elastic modulus reflects interatomic bond strength and is largely unaffected by processing — unlike yield strength, which is highly sensitive to microstructure.
