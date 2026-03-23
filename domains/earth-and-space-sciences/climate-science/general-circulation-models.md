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
stage: expert
status: draft
---

# General Circulation Models (GCMs) and Climate Simulation

## Core Idea
General circulation models (GCMs) are numerical simulations of the coupled atmosphere-ocean-land system based on primitive equations of fluid dynamics (conservation of momentum, mass, and energy). GCMs discretize the globe into a grid and solve these equations forward in time. Unresolved processes at sub-grid scale (clouds, convection, boundary layers, radiation) are represented via parameterizations, which introduce significant uncertainty. GCMs are the primary tool for climate projection, attribution of observed change, and testing hypothesis about climate feedbacks.

## How It's Best Learned
Run a simplified GCM (e.g., online tools like EdGCM or NCAR CAM) and vary CO₂, solar forcing, or aerosols. Observe changes in temperature distribution, precipitation patterns, and circulation. Analyze the role of parameterizations by toggling them on/off.

## Common Misconceptions
GCMs are not reality, and their predictions depend heavily on parameterization choices. Also, GCM uncertainty does not invalidate projections; ensemble approaches and uncertainty quantification reveal robust signals.

## Questions

```yaml
- question: "A GCM has a horizontal resolution of 100 km per grid cell. An individual tropical convective storm is typically 5–10 km wide. How does the GCM represent the effects of these storms?"
  type: multiple-choice
  options:
    - "The GCM ignores small-scale convection entirely, which is why GCMs cannot simulate tropical precipitation"
    - "The GCM increases its time step in tropical regions to resolve individual storm lifecycles"
    - "The GCM uses a parameterization scheme that estimates the aggregate heating and moistening effects of convection based on grid-cell temperature and humidity"
    - "The GCM uses satellite observations of each storm to nudge the model toward reality at each time step"
  answer: 2
  explanation: "Sub-grid processes that cannot be directly resolved are represented through parameterization — mathematical relationships that estimate aggregate effects from grid-cell-averaged variables. A convective parameterization might trigger 'deep convection' in a grid cell when humidity and instability exceed threshold values, then redistribute heat and moisture vertically according to empirical rules derived from observations or high-resolution simulations. This is not ignorance or error — it is a necessary and deliberate approximation. Parameterization schemes are validated against observations and are a primary focus of ongoing GCM development."

- question: "Two GCMs from different modeling centers are given identical CO₂ forcing scenarios but produce global mean temperature projections that differ by 1.5°C. The most scientifically informative explanation for this discrepancy is:"
  type: multiple-choice
  options:
    - "One model has a coding error that introduces systematic bias in its temperature output"
    - "The models use different physical laws for thermodynamics, making their results incompatible"
    - "The models differ in their cloud and convection parameterization schemes, which affect how much warming the climate system produces for the same forcing"
    - "The models were initialized with different historical CO₂ concentrations, shifting their projections"
  answer: 2
  explanation: "Cloud and convection parameterizations are the dominant source of inter-model spread in climate projections. Clouds are both a major component of Earth's energy budget and highly sensitive to parameterization choices — low clouds cool by reflecting sunlight; high clouds warm by trapping outgoing radiation. Different parameterization schemes produce different amounts and types of cloud cover in response to warming, leading to different effective climate sensitivities. This is not a modeling flaw but a reflection of genuine scientific uncertainty about cloud feedbacks, which is why CMIP coordinates multiple models to map this uncertainty."

- question: "The uncertainty in GCM projections means that scientists cannot reliably determine whether anthropogenic greenhouse gas emissions will cause net warming of the climate system."
  type: true-false
  answer: false
  explanation: "GCM uncertainty primarily concerns the magnitude and regional distribution of projected changes, not the direction. The warming signal from doubled CO₂ (2–5°C equilibrium warming) is robust across virtually all GCMs despite differences in cloud parameterization. This is because the underlying physics — radiative forcing from CO₂ and water vapor feedback amplification — is well constrained. The models disagree about details (how much polar amplification, how precipitation patterns will shift) but consistently agree on net warming. Ensemble methods and model intercomparison (CMIP) are precisely the tools designed to distinguish robust signals from parameterization-dependent uncertainty."

- question: "Running an ensemble of GCM simulations — multiple runs with slightly different initial conditions or parameterization settings — provides more scientific information than relying on a single best-guess simulation."
  type: true-false
  answer: true
  explanation: "A single simulation gives one possible trajectory of the climate system but cannot distinguish between signals that are physically robust and artifacts of specific parameterization choices. An ensemble maps out the range of possible outcomes, letting scientists identify projections that are consistent across many runs (robust signals) versus those that vary widely (uncertain quantities). Ensemble methods also allow estimation of internal climate variability: by running identical forcings with different initial conditions, you can separate the forced response from natural variability. The Coupled Model Intercomparison Project extends this to across-model ensembles, providing the most complete picture of projection uncertainty."

- question: "What is parameterization in a GCM, and why is it a necessary feature of climate models rather than simply a limitation that better computers could eliminate?"
  type: short-answer
  answer: "Parameterization is the representation of sub-grid physical processes — those occurring at scales smaller than the model grid — using simplified mathematical relationships derived from theory, observations, or high-resolution simulations. Processes like individual convective clouds (5–10 km), turbulent boundary-layer eddies (meters), and aerosol-cloud interactions require parameterization in models with 50–100 km grid cells. While finer resolution reduces the need for parameterization, many important processes span multiple orders of magnitude below any computationally feasible global grid resolution. Furthermore, some processes (cloud microphysics, turbulence) involve inherent randomness and non-linearity that cannot be deterministically resolved even with arbitrarily fine grids. Parameterization is therefore a scientifically principled engineering solution, not merely a stopgap."
  explanation: "Understanding that parameterization is a feature rather than a bug is the conceptual key to interpreting GCM uncertainty honestly. The uncertainty is not 'the model is wrong'; it is 'we have quantified our ignorance about sub-grid processes and encoded that uncertainty in the spread of parameterization schemes.' This is progress relative to having no model at all. The skill in using GCMs is distinguishing robust projections (consistent across models with very different parameterizations) from sensitive projections (varying widely across models), using that distinction to guide both scientific conclusions and policy communication."
```

## Explainer

You have already encountered climate models at a conceptual level and understand that they project future climate based on physical laws and emission scenarios. A **general circulation model** (GCM) is the most comprehensive type of climate model — a numerical simulation that solves the fundamental equations of fluid dynamics and thermodynamics for the atmosphere and ocean on a three-dimensional grid covering the entire globe. Your background in partial differential equations and numerical methods is directly applicable here: GCMs are, at their core, massive PDE solvers.

The equations at the heart of a GCM are the **primitive equations** — a simplified form of the Navier-Stokes equations adapted for a thin fluid layer on a rotating sphere. These include conservation of momentum (Newton's second law applied to air and water parcels, including Coriolis and pressure gradient forces), conservation of mass (the continuity equation), the thermodynamic energy equation (tracking heating from radiation, latent heat, and conduction), and an equation of state linking temperature, pressure, and density. The model divides the atmosphere into a grid of cells — typically 50–100 km on a side horizontally and 30–60 vertical layers — and steps forward in time increments of minutes to hours, computing how each cell's temperature, pressure, humidity, and wind evolve based on its current state and interactions with neighboring cells.

The fundamental challenge of GCMs is **parameterization**: many of the most important physical processes occur at scales smaller than the grid. A single grid cell 100 km across might contain dozens of individual convective thunderstorms, each only a few kilometers wide, along with turbulent boundary layer eddies, cloud microphysics, and radiative interactions with aerosol particles. These sub-grid processes cannot be resolved directly — instead, their aggregate effects are represented by simplified mathematical relationships called **parameterization schemes**. For example, a convective parameterization might trigger "convection" in a grid cell when its humidity and instability exceed certain thresholds, redistributing heat and moisture vertically according to empirical rules. Cloud parameterizations estimate fractional cloud cover and optical properties based on grid-cell humidity and temperature. These parameterizations are the largest source of uncertainty in GCMs and the primary reason different models can produce different projections from the same emission scenario.

Despite this uncertainty, GCMs produce robust results by exploiting **ensemble methods** and **model intercomparison**. Rather than relying on a single simulation, climate scientists run ensembles — multiple simulations with slightly different initial conditions or parameterization settings — to map out the range of possible outcomes. The **Coupled Model Intercomparison Project** (CMIP) coordinates dozens of modeling centers worldwide to run standardized experiments, allowing researchers to identify projections that are consistent across independent models (and therefore more trustworthy) versus those that diverge (indicating genuine scientific uncertainty). The result that doubled CO₂ produces 2–5°C of equilibrium warming, for instance, is robust across virtually all GCMs despite their differences in cloud parameterization — because the underlying physics of radiative forcing and water vapor feedback is well constrained.

GCMs have been validated against the historical climate record, paleoclimate data, and natural experiments like volcanic eruptions (which inject aerosols and allow testing of the model's radiative response). They successfully reproduce observed patterns including the latitude structure of warming, stratospheric cooling alongside tropospheric warming, polar amplification, and the spatial pattern of precipitation change. This track record of **hindcasting** — correctly simulating past climate when given past forcings — provides the foundation for trusting their forward projections, while honest accounting of parameterization uncertainty keeps those projections from being mistaken for precise predictions.
