---
id: climate-model-parameterization
title: Climate Model Parameterization of Subgrid Processes
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: general-circulation-models
  type: hard
- id: cloud-formation-and-types
  type: hard
- id: radiative-transfer-atmospheric
  type: soft
builds-toward:
- climate-model-evaluation
- climate-models-and-projections
tags:
- parameterization
- subgrid
- convection
- cloud-microphysics
- model-development
stage: advanced
status: draft
---

# Climate Model Parameterization of Subgrid Processes

## Core Idea
Climate models coarsen physics onto grid cells typically 50–200 km on a side, so subgrid processes (convection, cloud microphysics, turbulence) must be parameterized rather than explicitly computed. Parameterizations relate unresolved processes to resolved grid-scale variables, introducing assumptions and uncertainty. Convection and cloud parameterizations are major sources of climate model uncertainty; improving them is a priority for reducing climate projection uncertainty.

## How It's Best Learned
Study the structure of a convection parameterization (e.g., mass-flux formulation) and how it relates rainfall to large-scale vertical motion. Compare parameterized versus explicit convection in high-resolution simulations. Examine how parameter choices affect model-mean climate and feedbacks.

## Common Misconceptions
- Assuming parameterizations are fixed; they are tuned to match observations and vary between models. - Overlooking that parameterized processes are inherently uncertain; structural uncertainty in parameterizations is often larger than structural uncertainty in resolved processes.
