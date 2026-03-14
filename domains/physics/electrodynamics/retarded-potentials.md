---
id: retarded-potentials
title: Retarded Potentials
domain: physics
course: electrodynamics
prerequisites:
- id: scalar-vector-potentials
  type: hard
- id: lorenz-gauge
  type: hard
- id: greens-functions-pdes
  type: soft
builds-toward:
- lienard-wiechert-potentials
- radiation-accelerating-charges
tags:
- retarded-potentials
- causality
- radiation
stage: advanced
status: draft
---

# Retarded Potentials

## Core Idea
Retarded potentials account for the finite speed of electromagnetic influence by expressing potentials at time t in terms of charge and current distributions at an earlier (retarded) time t' = t - r/c. This naturally encodes causality: fields at a point depend only on sources within the light cone, not on future sources. Retarded potentials form the foundation for understanding radiation and all time-dependent electromagnetic phenomena.
