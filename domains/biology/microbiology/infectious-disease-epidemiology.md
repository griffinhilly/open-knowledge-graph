---
id: infectious-disease-epidemiology
title: Infectious Disease Epidemiology
domain: biology
course: microbiology
prerequisites:
- id: host-pathogen-interactions
  type: hard
- id: population-ecology-intro
  type: soft
- id: population-growth-models
  type: soft
- id: antibiotic-resistance-mechanisms
  type: soft
builds-toward:
- emerging-infectious-diseases
tags:
- R0
- herd immunity
- SIR model
- transmission
- endemic
- epidemic
- pandemic
- incubation period
stage: abstract-reasoning
status: validated
---
# Infectious Disease Epidemiology

## Core Idea
Infectious disease epidemiology quantifies how diseases spread through populations using mathematical and statistical tools. The basic reproduction number R₀ — the average number of secondary infections from one case in a fully susceptible population — determines whether an outbreak grows (R₀ > 1) or dies out (R₀ < 1). Herd immunity is achieved when a sufficient fraction of the population is immune to reduce effective R below 1, protecting even non-immune individuals. Transmission routes (respiratory, contact, fecal-oral, vector-borne, vertical) determine control strategies. The SIR (Susceptible-Infected-Recovered) compartmental model provides the mathematical foundation for predicting epidemic curve shape and final outbreak size.

## How It's Best Learned
Calculate R₀ and the derived herd immunity threshold (1 − 1/R₀) for diseases with contrasting values — measles (R₀ ≈ 15, threshold ≈ 93%), influenza (R₀ ≈ 1.3, threshold ≈ 23%). Plotting SIR model outputs while varying R₀ shows how a small increase in transmissibility produces a disproportionately larger epidemic.

## Common Misconceptions
- R₀ is not a fixed biological property of a pathogen — it varies with population density, contact patterns, behavior, and prior immunity levels.
- Herd immunity protects immunocompromised individuals who cannot receive live vaccines — it is not merely statistical protection for the majority.
- High case fatality rate does not make a disease a better epidemic candidate; high transmissibility (even with low fatality) drives far larger outbreaks.
