---
id: sir-compartmental-model
title: SIR Compartmental Models for Infectious Disease
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: basic-reproduction-number
  type: hard
builds-toward:
- seir-model-latency
tags:
- compartmental-models
- sir-model
- modeling
- disease-transmission
stage: advanced
status: draft
---

# SIR Compartmental Models for Infectious Disease

## Core Idea
The SIR model divides a population into Susceptible, Infected, and Recovered compartments and uses differential equations to model transitions. The force of infection (β × I/N) drives susceptible → infected transitions; the recovery rate (γ) drives infected → recovered transitions. SIR models predict epidemic dynamics, peak timing, and final size, forming the basis for control strategy evaluation.
