---
id: age-structured-epidemiological-models
title: Age-Structured Epidemiological Models
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: sir-compartmental-model
  type: hard
- id: disease-frequency-measures
  type: soft
- id: population-age-structure-life-history
  type: hard
- id: population-growth-models
  type: hard
builds-toward:
- force-of-infection
tags:
- transmission-dynamics
- age-specific-rates
- vaccination-strategy
stage: advanced
status: draft
---

# Age-Structured Epidemiological Models

## Core Idea
Age structure is crucial in epidemiology because contact patterns, susceptibility, transmissibility, and outcomes vary substantially by age. Age-structured models partition the population into age strata and allow differential transmission rates and transitions between strata, producing more realistic predictions than homogeneous-mixing models. Age-specific force of infection and next-generation matrices capture how transmission flows between age groups. These models are essential for evaluating childhood disease burden and vaccination strategy optimization.

## How It's Best Learned
Build and simulate an age-structured SIR or SEIR model for an infectious disease; compare predictions to a homogeneous-mixing model and real outbreak data.

## Common Misconceptions
Age structure matters mainly for childhood diseases (it affects transmission patterns for all infectious diseases). Random mixing between age groups is a reasonable assumption.
