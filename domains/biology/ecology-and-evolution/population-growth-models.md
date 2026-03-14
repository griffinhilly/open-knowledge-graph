---
id: population-growth-models
title: 'Population Growth Models: Exponential and Logistic'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-ecology-intro
  type: hard
- id: exponential-functions-and-graphs
  type: soft
- id: differential-equations-intro-separable
  type: soft
builds-toward:
- carrying-capacity
- population-regulation
- predator-prey-dynamics
tags:
- exponential-growth
- logistic-growth
- intrinsic-rate
- population-dynamics
stage: formal-systems
status: validated
---

# Population Growth Models: Exponential and Logistic

## Core Idea
Exponential growth (dN/dt = rN) models population growth when resources are unlimited, where r is the intrinsic rate of natural increase. Logistic growth (dN/dt = rN(K−N)/K) incorporates carrying capacity K — the maximum sustainable population size given resource constraints. As population size approaches K, growth rate declines due to density-dependent limitations. Real populations rarely exhibit pure logistic growth; oscillations, time lags, and overshooting are common.

## How It's Best Learned
Graph both models and compare J-shaped (exponential) vs. S-shaped (logistic) curves. Solve differential equations at various values of N relative to K. Use bacterial growth or yeast fermentation data as empirical examples before moving to complex wildlife data.

## Common Misconceptions
- Carrying capacity K is not fixed — it changes with environmental conditions.
- Logistic growth does not predict that populations stabilize exactly at K; real populations fluctuate around K.
- A high r does not always mean rapid growth to K — time lags can cause cycles or chaos.
