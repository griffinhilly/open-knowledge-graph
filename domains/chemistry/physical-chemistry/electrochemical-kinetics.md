---
id: electrochemical-kinetics
title: 'Electrochemical Kinetics: Butler-Volmer Theory'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: electrochemical-cells
  type: hard
- id: transition-state-theory
  type: soft
- id: arrhenius-equation
  type: soft
- id: electric-potential
  type: soft
- id: electric-current-and-resistance
  type: soft
- id: exponential-functions-and-graphs
  type: soft
tags:
- Butler-Volmer
- overpotential
- exchange-current
- Tafel-equation
- charge-transfer
- Marcus-theory
stage: advanced
status: draft
---

# Electrochemical Kinetics: Butler-Volmer Theory

## Core Idea
Electrochemical kinetics describes how electron-transfer rates at electrode-electrolyte interfaces depend on electrode potential. The Butler-Volmer equation i = i₀[exp(αFη/RT) − exp(−(1−α)Fη/RT)] relates current density i to overpotential η = E − E_eq, where i₀ is the exchange current density and α is the transfer coefficient (typically 0.5). At large overpotentials, the Butler-Volmer equation simplifies to the Tafel equation: η = a + b·log(i). Marcus theory provides a quantum-mechanical foundation, relating the rate constant to the reorganization energy λ and the driving force ΔG°, predicting the 'inverted region' where rate decreases for very exergonic reactions.

## How It's Best Learned
Plot Butler-Volmer curves for different i₀ values and observe how exchange current density determines reversibility. Construct a Tafel plot from real polarization data and extract the Tafel slope (b = 2.303RT/αF) to determine α.

## Common Misconceptions
- Thinking a large overpotential always increases the rate indefinitely — at extreme overpotentials, mass transport limits the current.
- Confusing transfer coefficient α with a symmetry factor; α = 0.5 only for a symmetric energy barrier.
