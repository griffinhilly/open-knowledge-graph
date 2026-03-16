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
- id: partial-differential-equations-intro
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

## Explainer

From your study of general circulation models, you know that climate models solve the fundamental equations of fluid dynamics and thermodynamics on a three-dimensional grid covering the globe. But here is the problem: many of the most important processes in the climate system happen at scales far smaller than any computationally feasible grid cell. A typical climate model grid cell might be 100 km on a side, yet a thunderstorm is only 10 km across, individual clouds are hundreds of meters, and turbulent eddies in the boundary layer are meters. These **subgrid processes** cannot be ignored — they transport enormous amounts of energy, moisture, and momentum — but they cannot be explicitly simulated at global scales. **Parameterization** is the solution: representing the collective statistical effect of unresolved processes in terms of the large-scale variables that the model does resolve.

Consider **convective parameterization** as a concrete example. A climate model cannot simulate individual thunderstorms, but it needs to know when and where convection occurs, how much rain it produces, and how it redistributes heat and moisture vertically. A convection scheme typically monitors each grid column for instability — when the lower atmosphere becomes warm and moist enough relative to the air above, the parameterization "triggers" and computes a mass flux of rising air, condensation, rainfall, and the resulting warming and drying of the column. The scheme uses relationships derived from observations and high-resolution simulations, but it necessarily involves assumptions: how easily convection triggers, how much air is entrained from the environment, how precipitation efficiency varies. Different models make different choices, which is why two climate models given identical greenhouse gas scenarios can produce different regional rainfall projections.

**Cloud parameterization** is similarly consequential and even more uncertain. Clouds both reflect sunlight (cooling) and trap infrared radiation (warming), and the net effect depends on cloud type, altitude, thickness, and droplet properties — all subgrid details. A parameterization must decide, based on grid-scale humidity and temperature, what fraction of a grid cell is cloudy, what the cloud water content is, and whether the cloud is liquid or ice. Small changes in these assumptions can shift the global cloud feedback from weakly positive to strongly positive, which is why cloud parameterization is the dominant source of spread in **equilibrium climate sensitivity** estimates across models.

The key insight is that parameterizations are not physics in the same sense as the resolved equations — they are **informed approximations** with tunable parameters. Model developers adjust these parameters so that the model's mean climate (global temperature, precipitation patterns, radiation budget) matches observations reasonably well. But tuning to the present climate does not guarantee correct behavior under changed conditions. This is why climate model intercomparison projects (like CMIP) run many models with different parameterization choices: the spread across models provides an estimate of **structural uncertainty** — the uncertainty arising not from imprecise inputs but from our incomplete understanding of how to represent subgrid physics. Advances in computing power are gradually enabling higher-resolution models that explicitly resolve some previously parameterized processes, but full global cloud-resolving simulations remain beyond current capability for century-scale projections.
