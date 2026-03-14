---
id: materials-selection-design
title: Materials Selection for Design
domain: engineering
course: materials-science
prerequisites:
- id: stress-strain-behavior
  type: hard
- id: mechanical-testing-methods
  type: soft
builds-toward: []
tags:
- ashby-charts
- material-indices
- performance-optimization
- multi-objective-selection
- material-property-charts
stage: formal-systems
status: draft
---

# Materials Selection for Design

## Core Idea
Materials selection translates engineering requirements into a rational choice among the thousands of available materials. The methodology developed by Ashby organizes this process into four steps: translation (expressing design requirements as function, objective, constraints, and free variables), screening (eliminating materials that fail hard constraints), ranking (comparing surviving candidates using a material index), and documentation (examining supporting information like cost, availability, and environmental impact). Material indices are performance metrics derived from the design equations — for example, a light stiff beam requires maximizing E^(1/2)/rho (elastic modulus to the half power divided by density), while a light strong beam requires maximizing sigma_y^(2/3)/rho. Ashby charts plot one material property against another (e.g., strength versus density, modulus versus density) on logarithmic axes, allowing the material index to appear as a straight guideline. Materials above the guideline outperform those below it for the specified objective. Multi-objective selection arises when two or more performance metrics conflict — a lightweight design may also need to be cheap, requiring trade-off surfaces (Pareto fronts) to identify non-dominated solutions. This systematic approach prevents the common engineering pitfall of selecting materials based on familiarity rather than performance, and it enables the discovery of unconventional material choices such as using wood or foams where metals have traditionally dominated.

## How It's Best Learned
Derive material indices for several common design scenarios (light stiff panel, light strong tie rod, minimum-cost pressure vessel) to understand how function, objective, and constraints combine into a single ranking criterion. Use Ashby charts (or the CES EduPack software) to identify optimal material classes for each scenario and verify that the chart-based ranking matches the analytical index. Work through a complete case study — such as selecting a material for a bicycle frame or aircraft skin panel — from translation through documentation.

## Common Misconceptions
- The "best" material does not exist in an absolute sense — it depends entirely on the design function, objective, and constraints. Steel is excellent for a bridge but poor for an aircraft wing, and the material index quantifies why.
- Ashby charts do not give a single answer — they identify a shortlist of candidate material families (metals, polymers, ceramics, composites) that must then be narrowed by detailed property data and practical considerations.
- Cost is not a material property but a market variable — materials selection must account for processing cost, not just raw material cost, because a cheap material that requires expensive fabrication may not be economical.
