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

## Questions

```yaml
- question: "In a CMIP6 temperature projection, the spread between different SSP scenario lines widens dramatically after 2050, while before 2030 the lines are nearly indistinguishable. What does this tell us about the sources of uncertainty?"
  type: multiple-choice
  options:
    - "Climate models are reliable only after 2050 when they have enough observational data to calibrate"
    - "Early-century uncertainty is dominated by internal variability and model spread; late-century uncertainty is dominated by which emissions pathway humanity follows"
    - "The models agree perfectly on long-term projections, which is why the scenario lines converge at the end"
    - "Scenario uncertainty is irrelevant because the models all converge on the same warming by 2100"
  answer: 1
  explanation: "This is the key structure of climate projection uncertainty. Before mid-century, natural variability and differences in how models parameterize processes (model uncertainty) dominate the spread. After mid-century, the choice of emissions scenario becomes the largest factor — because that depends on human decisions, not physics. The fan of scenario lines diverging after 2040 visually represents the point where human choices matter more than physical uncertainty we cannot reduce."

- question: "A commentator argues: 'Climate models can't be trusted because different models predict different amounts of warming.' Which response best addresses this claim?"
  type: multiple-choice
  options:
    - "The commentator is correct; model disagreement proves we cannot know anything about future climate"
    - "All models must agree before projections can be used in policy"
    - "Model uncertainty exists about the precise amount of warming, but all models agree on the direction and approximate range; uncertainty is about precision, not whether warming occurs"
    - "Climate models are as accurate as short-range weather forecasts and should be trusted completely"
  answer: 2
  explanation: "Model spread reflects genuine scientific uncertainty about parameterized processes like cloud microphysics — not uncertainty about whether warming will occur. All CMIP6 models agree that continued fossil fuel use causes significant warming; they disagree on the exact sensitivity. This is analogous to multiple doctors agreeing a patient's condition will worsen while disagreeing on the exact timeline. Uncertainty about amount ≠ uncertainty about direction."

- question: "Climate model projections are best understood as conditional statements: if emissions follow a given trajectory, then here is the resulting climate — not as unconditional predictions of what will happen."
  type: true-false
  answer: true
  explanation: "SSP scenarios are explicitly 'what if' storylines paired with radiative forcing levels. No single projection is a prediction of what will happen — each is a conditional outcome contingent on the emissions pathway chosen. This framing is important because it reframes uncertainty productively: rather than 'we don't know what the climate will do,' it becomes 'here are the climate consequences of each policy choice.'"

- question: "Higher-resolution climate models always produce more accurate global temperature projections than lower-resolution models."
  type: true-false
  answer: false
  explanation: "Higher resolution improves representation of regional features and some mesoscale processes, but it does not automatically improve large-scale global temperature projections. Higher-resolution models are computationally expensive, which limits the number of ensemble runs possible, and they can still miss key feedbacks if sub-grid processes are not well parameterized. The quality of parameterization schemes matters more than resolution alone for global-scale projections. This is why the CMIP ensemble includes models across a range of resolutions."

- question: "What is parameterization in climate modeling, and why does it introduce uncertainty even in models that correctly implement the governing equations of physics?"
  type: short-answer
  answer: "Parameterization is the use of simplified statistical representations for physical processes that occur at scales smaller than a model's grid box — individual clouds, turbulent eddies, sea-ice dynamics. Because these processes cannot be resolved directly, they are approximated by rules tuned to observations. Two models can perfectly agree on large-scale fluid dynamics and radiation physics but diverge on how they parameterize cloud microphysics, producing different estimates of climate sensitivity. This disagreement is honest — it reflects genuine scientific uncertainty about processes that are physically real but too small to resolve computationally."
  explanation: "Parameterization is the main source of inter-model spread for climate sensitivity. It is not a flaw in the models — it is an explicit acknowledgment of scale limitations. The uncertainty it introduces is quantified through ensemble modeling: running many parameterization variants reveals the range of plausible outcomes given our current understanding."
```

## Explainer

A **General Circulation Model** (GCM) — now more commonly called an **Earth System Model** (ESM) — is essentially the equations of physics applied to a gridded planet. The model divides the atmosphere and ocean into millions of three-dimensional boxes, typically 50–100 km on a side in the atmosphere and 10–50 km in the ocean, then solves the governing equations of fluid dynamics, thermodynamics, and radiative transfer in each box at every time step. You already understand from your study of climate feedbacks how small changes can amplify — ice-albedo feedback, water vapor feedback, cloud feedback. The model's job is to simulate all of these simultaneously, letting the feedbacks interact rather than analyzing them in isolation. From your study of anthropogenic climate forcing, you know the external push (greenhouse gases, aerosols, land-use change); the model computes the climate system's response.

The core challenge in climate modeling is **parameterization**: processes that occur at scales smaller than a grid box — individual clouds, turbulent eddies, sea-ice leads — must be represented by simplified statistical rules rather than resolved directly. This is where much of the disagreement between models originates. Two models can agree perfectly on the physics of radiation and large-scale circulation but diverge on how they parameterize cloud microphysics, producing different estimates of climate sensitivity. This is not a flaw to be embarrassed about — it is an honest representation of genuine scientific uncertainty about sub-grid processes.

To handle this uncertainty, climate scientists use **ensemble modeling**. There are two kinds: multi-model ensembles (running many different models built by different groups worldwide, as in the CMIP6 project) and perturbed-physics ensembles (running one model many times with slightly different parameter settings or initial conditions). The spread across ensemble members tells you where the models agree (robust signal) and where they diverge (genuine uncertainty). Early in the 21st century, the dominant source of uncertainty is internal variability — the climate system's own chaotic fluctuations. By mid-century, model uncertainty dominates. By late century, **scenario uncertainty** — which emissions pathway humanity actually follows — becomes the largest factor.

The **Shared Socioeconomic Pathways** (SSPs) provide standardized "what if" storylines paired with radiative forcing levels. SSP1-1.9 represents rapid decarbonization and limits warming to about 1.5°C; SSP5-8.5 represents fossil-fuel-intensive development and produces 4–5°C of warming by 2100. These are not predictions — they are conditional projections. The model says: "If emissions follow this trajectory, here is the resulting climate." The value of the projection is not in picking the "right" scenario but in understanding the consequences of each pathway, giving policymakers a map from choices to outcomes. When you see a fan of colored lines diverging after 2040 in a temperature projection, you are looking at this scenario separation — the point where humanity's collective decisions begin to matter more than the physics we cannot control.
