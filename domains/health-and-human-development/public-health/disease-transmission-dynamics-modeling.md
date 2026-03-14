---
id: disease-transmission-dynamics-modeling
title: Disease Transmission Dynamics and Mathematical Modeling
domain: health-and-human-development
course: public-health
prerequisites:
- id: epidemic-curve-analysis
  type: hard
- id: force-of-infection
  type: soft
builds-toward:
- pandemic-preparedness-and-response-planning
- communicable-disease-control-strategy-selection
tags:
- epidemiology
- modeling
- disease-transmission
stage: abstract-reasoning
status: draft
---

# Disease Transmission Dynamics and Mathematical Modeling

## Core Idea
Mathematical models of disease transmission quantify how infections spread through populations using compartmental structures (SIR: susceptible, infected, recovered). Transmission rate, recovery rate, and contact patterns determine epidemic growth. These models predict epidemic trajectory, estimate basic reproduction number (R₀), and evaluate the impact of interventions like vaccination and isolation.

## How It's Best Learned
Start with simple SIR models by hand, then use R or Python to simulate scenarios. Compare predictions to real outbreak data (e.g., COVID-19, influenza) to see how well models perform.

## Common Misconceptions
- Models predict the future exactly; they represent simplified reality and are most useful for comparing intervention scenarios.
- R₀ is fixed for a disease; it depends on contact patterns, transmission probability, and recovery rate, which vary by setting and population.
