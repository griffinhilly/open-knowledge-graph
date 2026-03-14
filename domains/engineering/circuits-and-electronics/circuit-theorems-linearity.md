---
id: circuit-theorems-linearity
title: Linearity, Superposition, and Scaling
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: node-voltage-systematic-solution
  type: soft
- id: mesh-current-systematic-solution
  type: soft
- id: ohms-law-and-conductance
  type: hard
builds-toward:
- thevenin-circuit-equivalent
- norton-circuit-equivalent
tags:
- linearity
- superposition
- homogeneity
- additivity
stage: formal-systems
status: draft
---

# Linearity, Superposition, and Scaling

## Core Idea
Linear circuits satisfy superposition: response to multiple sources equals the sum of individual responses. Linearity requires homogeneity (scaling input scales output) and additivity (sum of inputs produces sum of outputs). These properties hold for circuits with R, L, C, and independent sources, enabling efficient analysis and design techniques.
