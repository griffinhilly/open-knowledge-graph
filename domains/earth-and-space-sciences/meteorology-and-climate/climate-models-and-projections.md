---
id: climate-models-and-projections
title: Climate Models and Future Projections
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: feedback-mechanisms-in-climate
  type: hard
- id: anthropogenic-climate-forcing
  type: hard
- id: global-atmospheric-circulation
  type: soft
tags:
- GCM
- CMIP
- RCP
- SSP
- ensemble
- uncertainty
stage: advanced
status: validated
---

# Climate Models and Future Projections

## Core Idea
General Circulation Models (GCMs), now called Earth System Models, simulate the atmosphere, ocean, land surface, and cryosphere on global grids, solving the governing equations of fluid dynamics, thermodynamics, and radiative transfer. Model uncertainty comes from three sources: initial conditions, internal variability, and scenario uncertainty (how emissions will evolve). Ensemble modeling — running many models or many simulations of one model with slightly perturbed conditions — quantifies this spread. Shared Socioeconomic Pathways (SSPs) provide standardized emissions scenarios from aggressive mitigation (SSP1-1.9) to unmitigated high emissions (SSP5-8.5), producing projected warming of 1.0–5.7°C by 2100 relative to pre-industrial.

## How It's Best Learned
Examine the CMIP6 multi-model ensemble spread for temperature projections: identify how scenario choice separates scenarios after 2040 while early 21st-century uncertainty is dominated by model spread and internal variability. Discuss what 'confidence' means in a probabilistic projection.

## Common Misconceptions
- Climate models are not weather forecasts; they do not predict specific events but project the statistical distribution of climate over decades.
- Model uncertainty does not mean 'we don't know anything' — all models agree on the sign and approximate magnitude of warming; uncertainty is about precision.
- Higher-resolution models are not always better for large-scale projections; they are computationally expensive and may miss key feedbacks if sub-grid processes are not well parameterized.

## Explainer

A **General Circulation Model** (GCM) — now more commonly called an **Earth System Model** (ESM) — is essentially the equations of physics applied to a gridded planet. The model divides the atmosphere and ocean into millions of three-dimensional boxes, typically 50–100 km on a side in the atmosphere and 10–50 km in the ocean, then solves the governing equations of fluid dynamics, thermodynamics, and radiative transfer in each box at every time step. You already understand from your study of climate feedbacks how small changes can amplify — ice-albedo feedback, water vapor feedback, cloud feedback. The model's job is to simulate all of these simultaneously, letting the feedbacks interact rather than analyzing them in isolation. From your study of anthropogenic climate forcing, you know the external push (greenhouse gases, aerosols, land-use change); the model computes the climate system's response.

The core challenge in climate modeling is **parameterization**: processes that occur at scales smaller than a grid box — individual clouds, turbulent eddies, sea-ice leads — must be represented by simplified statistical rules rather than resolved directly. This is where much of the disagreement between models originates. Two models can agree perfectly on the physics of radiation and large-scale circulation but diverge on how they parameterize cloud microphysics, producing different estimates of climate sensitivity. This is not a flaw to be embarrassed about — it is an honest representation of genuine scientific uncertainty about sub-grid processes.

To handle this uncertainty, climate scientists use **ensemble modeling**. There are two kinds: multi-model ensembles (running many different models built by different groups worldwide, as in the CMIP6 project) and perturbed-physics ensembles (running one model many times with slightly different parameter settings or initial conditions). The spread across ensemble members tells you where the models agree (robust signal) and where they diverge (genuine uncertainty). Early in the 21st century, the dominant source of uncertainty is internal variability — the climate system's own chaotic fluctuations. By mid-century, model uncertainty dominates. By late century, **scenario uncertainty** — which emissions pathway humanity actually follows — becomes the largest factor.

The **Shared Socioeconomic Pathways** (SSPs) provide standardized "what if" storylines paired with radiative forcing levels. SSP1-1.9 represents rapid decarbonization and limits warming to about 1.5°C; SSP5-8.5 represents fossil-fuel-intensive development and produces 4–5°C of warming by 2100. These are not predictions — they are conditional projections. The model says: "If emissions follow this trajectory, here is the resulting climate." The value of the projection is not in picking the "right" scenario but in understanding the consequences of each pathway, giving policymakers a map from choices to outcomes. When you see a fan of colored lines diverging after 2040 in a temperature projection, you are looking at this scenario separation — the point where humanity's collective decisions begin to matter more than the physics we cannot control.
