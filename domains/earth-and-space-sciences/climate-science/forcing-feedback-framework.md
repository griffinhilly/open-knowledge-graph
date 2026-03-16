---
id: forcing-feedback-framework
title: Forcing-Feedback Framework in Climate
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: climate-sensitivity-radiative-feedbacks
  type: hard
- id: energy-balance-models
  type: hard
- id: surface-energy-balance
  type: hard
- id: radiative-transfer-atmospheric
  type: soft
builds-toward:
- climate-tipping-points
- climate-model-evaluation
tags:
- feedback
- forcing
- climate-sensitivity
- stability
stage: advanced
status: draft
---

# Forcing-Feedback Framework in Climate

## Core Idea
The forcing-feedback framework separates climate responses into radiative forcings (external perturbations) and feedbacks (self-amplifying or self-limiting responses). Climate sensitivity is determined by the ratio of forcing to net feedback; positive feedbacks amplify warming while negative feedbacks damp it. This framework quantifies how ice-albedo, cloud, water-vapor, and lapse-rate feedbacks control the climate response to increased greenhouse gases.

## Explainer

From your study of energy balance models and climate sensitivity, you already understand that the Earth system responds to changes in its radiation budget. The **forcing-feedback framework** provides the mathematical structure for separating the cause of a climate change (the forcing) from the processes that amplify or dampen it (the feedbacks). This separation is not merely conceptual — it is the foundation for quantifying climate sensitivity and comparing the effects of different perturbations.

A **radiative forcing** is an externally imposed change to the Earth's energy balance: doubling CO₂ reduces outgoing longwave radiation by about 3.7 W/m², volcanic aerosols reflect sunlight and reduce incoming shortwave radiation, changes in solar output alter the energy input. In each case, the forcing creates an energy imbalance — the planet absorbs more energy than it emits (positive forcing) or emits more than it absorbs (negative forcing). If no feedbacks existed, the system would simply warm or cool until the Planck response — increased thermal emission from a warmer surface — restored balance. This **no-feedback response** would give about 1.1°C of warming per doubling of CO₂. But feedbacks exist, and they are what make climate sensitivity uncertain and interesting.

A **feedback** is a process internal to the climate system that responds to the initial temperature change and either amplifies or dampens it. The **water vapor feedback** is the strongest positive feedback: warmer air holds more water vapor (Clausius-Clapeyron), water vapor is a greenhouse gas, so more water vapor traps more heat, causing further warming. The **ice-albedo feedback** is another positive feedback: warming melts reflective ice and snow, exposing darker ocean or land that absorbs more sunlight. The **lapse rate feedback** is typically negative: in the tropics, warming is amplified at upper levels, increasing emission to space more than surface warming alone would predict. The **cloud feedback** remains the most uncertain — low clouds that increase would cool the planet, but thinning or rising clouds would warm it. Mathematically, feedbacks are expressed as a feedback parameter (λ, in W/m²/K), and the equilibrium temperature change is ΔT = F / (λ₀ − Σλᵢ), where F is the forcing, λ₀ is the Planck response, and the λᵢ are individual feedback parameters. When the sum of positive feedbacks approaches λ₀, climate sensitivity becomes very large — the system is approaching a **runaway** state.

The power of this framework is that it allows scientists to decompose the total climate response into individually understandable pieces. Each feedback can be estimated from observations, paleoclimate data, or models, and their contributions compared. For example, paleoclimate evidence from the Last Glacial Maximum constrains the net feedback parameter because we know both the forcing (lower CO₂, ice-sheet albedo) and the response (4-7°C cooling). The framework also reveals why uncertainty in cloud feedback dominates uncertainty in climate sensitivity: clouds contribute the largest range of plausible feedback values. Understanding forcing-feedback decomposition is essential for interpreting climate projections, because it tells you not just how much warming to expect, but *why* — and where the remaining scientific uncertainty lies.
