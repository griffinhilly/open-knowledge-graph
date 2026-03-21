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

## Questions

```yaml
- question: "A climate model is carefully tuned to match observed global mean temperature, precipitation patterns, and radiation budget for the late 20th century. Why is this tuning insufficient to guarantee accurate regional rainfall projections under doubled CO₂?"
  type: multiple-choice
  options:
    - "Tuning uses noisy data, so the tuned parameters contain observational errors"
    - "Parameterizations are adjusted to reproduce present-day statistics, but the relationships between grid-scale variables and subgrid processes may shift differently under changed forcing"
    - "Regional rainfall is governed by unresolved processes that cannot influence the global-scale tuning targets"
    - "Doubled CO₂ alters the grid spacing of the model, invalidating the tuned parameters"
  answer: 1
  explanation: "Tuning adjusts parameterization parameters to minimize errors against present-day observations. But parameterizations are empirical approximations of subgrid physics, not fundamental laws. Under a warmer, moister atmosphere, the relationships between large-scale variables and subgrid convective behavior may shift in ways the parameterization was not designed to capture. A convection scheme can produce the right global-mean rainfall today through the wrong physical mechanism, which only matters when the climate departs from the conditions it was calibrated against."

- question: "Cloud parameterization is the dominant source of spread in equilibrium climate sensitivity estimates across CMIP models. What is the physical reason this uncertainty is so large?"
  type: multiple-choice
  options:
    - "Clouds are too small to observe accurately, so models depend on unreliable satellite measurements"
    - "Clouds both cool (by reflecting sunlight) and warm (by trapping infrared), and small changes in parameterized cloud properties shift the net feedback from weakly positive to strongly positive"
    - "All CMIP models share the same cloud parameterization code, so a single error amplifies identically across models"
    - "Cloud formation depends on aerosols, which have no physical parameterization and must be prescribed"
  answer: 1
  explanation: "The net cloud feedback is the difference between two large opposing effects: shortwave cooling (clouds reflect incoming solar radiation) and longwave warming (low clouds trap outgoing infrared). The sign and magnitude of the net effect depend on cloud type, altitude, coverage fraction, and optical depth — all quantities that must be parameterized. Small errors in parameterized cloud fraction or altitude can shift the global cloud feedback by several W/m²/K, translating into equilibrium climate sensitivity estimates ranging from below 2°C to above 5°C for doubled CO₂. No other parameterized process has this leverage on the global energy budget."

- question: "A climate parameterization is a physically rigorous representation of a process that simply operates at the grid scale rather than the process scale."
  type: true-false
  answer: false
  explanation: "Parameterizations are informed approximations with tunable parameters, not rigorous physical derivations. A convection scheme might trigger when large-scale instability exceeds a threshold, but the trigger threshold, entrainment rate assumption, and precipitation efficiency are empirically calibrated choices — not derived from first principles. This is why different models using different parameterization approaches can produce significantly different climate responses to the same forcing, and why improving parameterizations is a major research priority distinct from simply increasing resolution."

- question: "The spread across CMIP models in their projections of future global temperature primarily reflects uncertainty in future greenhouse gas emissions scenarios rather than differences in model physics."
  type: true-false
  answer: false
  explanation: "Both sources of uncertainty are large, but climate sensitivity uncertainty — largely driven by cloud and convection parameterization differences — determines how much warming any given emissions pathway produces. At mid-century timescales, inter-model spread from structural parameterization differences is comparable to or larger than scenario uncertainty. The multi-model CMIP ensemble exists specifically to sample this structural uncertainty: each model represents a plausible but different set of assumptions about subgrid physics."

- question: "Why do climate scientists run dozens of different models in coordinated intercomparison projects (CMIP) rather than identifying the single best model and using only that?"
  type: short-answer
  answer: "No single model is demonstrably best across all metrics and all regions — different models perform better on different aspects of climate. More fundamentally, the spread across models sampling different parameterization choices estimates the structural uncertainty that no single model can quantify internally. A single model appears precise but hides the uncertainty from its particular parameterization assumptions. The multi-model ensemble makes this uncertainty explicit and assessable, and it enables identifying robust projections (features appearing across all models) versus uncertain ones (where models disagree)."
  explanation: "This is the same logic as using ensemble weather forecasts rather than trusting one deterministic run. A model can be internally consistent and well-tuned while still being wrong about future climate because its parameterizations assume the wrong physical mechanisms. The multi-model approach acknowledges this limitation and provides a more honest characterization of projection confidence than any single-model run can."
```

## Explainer

From your study of general circulation models, you know that climate models solve the fundamental equations of fluid dynamics and thermodynamics on a three-dimensional grid covering the globe. But here is the problem: many of the most important processes in the climate system happen at scales far smaller than any computationally feasible grid cell. A typical climate model grid cell might be 100 km on a side, yet a thunderstorm is only 10 km across, individual clouds are hundreds of meters, and turbulent eddies in the boundary layer are meters. These **subgrid processes** cannot be ignored — they transport enormous amounts of energy, moisture, and momentum — but they cannot be explicitly simulated at global scales. **Parameterization** is the solution: representing the collective statistical effect of unresolved processes in terms of the large-scale variables that the model does resolve.

Consider **convective parameterization** as a concrete example. A climate model cannot simulate individual thunderstorms, but it needs to know when and where convection occurs, how much rain it produces, and how it redistributes heat and moisture vertically. A convection scheme typically monitors each grid column for instability — when the lower atmosphere becomes warm and moist enough relative to the air above, the parameterization "triggers" and computes a mass flux of rising air, condensation, rainfall, and the resulting warming and drying of the column. The scheme uses relationships derived from observations and high-resolution simulations, but it necessarily involves assumptions: how easily convection triggers, how much air is entrained from the environment, how precipitation efficiency varies. Different models make different choices, which is why two climate models given identical greenhouse gas scenarios can produce different regional rainfall projections.

**Cloud parameterization** is similarly consequential and even more uncertain. Clouds both reflect sunlight (cooling) and trap infrared radiation (warming), and the net effect depends on cloud type, altitude, thickness, and droplet properties — all subgrid details. A parameterization must decide, based on grid-scale humidity and temperature, what fraction of a grid cell is cloudy, what the cloud water content is, and whether the cloud is liquid or ice. Small changes in these assumptions can shift the global cloud feedback from weakly positive to strongly positive, which is why cloud parameterization is the dominant source of spread in **equilibrium climate sensitivity** estimates across models.

The key insight is that parameterizations are not physics in the same sense as the resolved equations — they are **informed approximations** with tunable parameters. Model developers adjust these parameters so that the model's mean climate (global temperature, precipitation patterns, radiation budget) matches observations reasonably well. But tuning to the present climate does not guarantee correct behavior under changed conditions. This is why climate model intercomparison projects (like CMIP) run many models with different parameterization choices: the spread across models provides an estimate of **structural uncertainty** — the uncertainty arising not from imprecise inputs but from our incomplete understanding of how to represent subgrid physics. Advances in computing power are gradually enabling higher-resolution models that explicitly resolve some previously parameterized processes, but full global cloud-resolving simulations remain beyond current capability for century-scale projections.
