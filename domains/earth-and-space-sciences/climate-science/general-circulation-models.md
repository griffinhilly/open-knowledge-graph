---
id: general-circulation-models
title: General Circulation Models (GCMs) and Climate Simulation
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: climate-models-and-projections
  type: hard
- id: differential-equations-intro
  type: soft
- id: convection-natural-and-forced
  type: soft
- id: thermodynamic-processes
  type: soft
- id: numerical-methods
  type: hard
- id: partial-differential-equations
  type: hard
- id: partial-differential-equations-intro
  type: hard
builds-toward:
- climate-projections-modeling
- climate-sensitivity-radiative-feedbacks
tags:
- model
- gcm
- simulation
- parameterization
- numerical
stage: advanced
status: draft
---

# General Circulation Models (GCMs) and Climate Simulation

## Core Idea
General circulation models (GCMs) are numerical simulations of the coupled atmosphere-ocean-land system based on primitive equations of fluid dynamics (conservation of momentum, mass, and energy). GCMs discretize the globe into a grid and solve these equations forward in time. Unresolved processes at sub-grid scale (clouds, convection, boundary layers, radiation) are represented via parameterizations, which introduce significant uncertainty. GCMs are the primary tool for climate projection, attribution of observed change, and testing hypothesis about climate feedbacks.

## How It's Best Learned
Run a simplified GCM (e.g., online tools like EdGCM or NCAR CAM) and vary CO₂, solar forcing, or aerosols. Observe changes in temperature distribution, precipitation patterns, and circulation. Analyze the role of parameterizations by toggling them on/off.

## Common Misconceptions
GCMs are not reality, and their predictions depend heavily on parameterization choices. Also, GCM uncertainty does not invalidate projections; ensemble approaches and uncertainty quantification reveal robust signals.

## Explainer

You have already encountered climate models at a conceptual level and understand that they project future climate based on physical laws and emission scenarios. A **general circulation model** (GCM) is the most comprehensive type of climate model — a numerical simulation that solves the fundamental equations of fluid dynamics and thermodynamics for the atmosphere and ocean on a three-dimensional grid covering the entire globe. Your background in partial differential equations and numerical methods is directly applicable here: GCMs are, at their core, massive PDE solvers.

The equations at the heart of a GCM are the **primitive equations** — a simplified form of the Navier-Stokes equations adapted for a thin fluid layer on a rotating sphere. These include conservation of momentum (Newton's second law applied to air and water parcels, including Coriolis and pressure gradient forces), conservation of mass (the continuity equation), the thermodynamic energy equation (tracking heating from radiation, latent heat, and conduction), and an equation of state linking temperature, pressure, and density. The model divides the atmosphere into a grid of cells — typically 50–100 km on a side horizontally and 30–60 vertical layers — and steps forward in time increments of minutes to hours, computing how each cell's temperature, pressure, humidity, and wind evolve based on its current state and interactions with neighboring cells.

The fundamental challenge of GCMs is **parameterization**: many of the most important physical processes occur at scales smaller than the grid. A single grid cell 100 km across might contain dozens of individual convective thunderstorms, each only a few kilometers wide, along with turbulent boundary layer eddies, cloud microphysics, and radiative interactions with aerosol particles. These sub-grid processes cannot be resolved directly — instead, their aggregate effects are represented by simplified mathematical relationships called **parameterization schemes**. For example, a convective parameterization might trigger "convection" in a grid cell when its humidity and instability exceed certain thresholds, redistributing heat and moisture vertically according to empirical rules. Cloud parameterizations estimate fractional cloud cover and optical properties based on grid-cell humidity and temperature. These parameterizations are the largest source of uncertainty in GCMs and the primary reason different models can produce different projections from the same emission scenario.

Despite this uncertainty, GCMs produce robust results by exploiting **ensemble methods** and **model intercomparison**. Rather than relying on a single simulation, climate scientists run ensembles — multiple simulations with slightly different initial conditions or parameterization settings — to map out the range of possible outcomes. The **Coupled Model Intercomparison Project** (CMIP) coordinates dozens of modeling centers worldwide to run standardized experiments, allowing researchers to identify projections that are consistent across independent models (and therefore more trustworthy) versus those that diverge (indicating genuine scientific uncertainty). The result that doubled CO₂ produces 2–5°C of equilibrium warming, for instance, is robust across virtually all GCMs despite their differences in cloud parameterization — because the underlying physics of radiative forcing and water vapor feedback is well constrained.

GCMs have been validated against the historical climate record, paleoclimate data, and natural experiments like volcanic eruptions (which inject aerosols and allow testing of the model's radiative response). They successfully reproduce observed patterns including the latitude structure of warming, stratospheric cooling alongside tropospheric warming, polar amplification, and the spatial pattern of precipitation change. This track record of **hindcasting** — correctly simulating past climate when given past forcings — provides the foundation for trusting their forward projections, while honest accounting of parameterization uncertainty keeps those projections from being mistaken for precise predictions.
