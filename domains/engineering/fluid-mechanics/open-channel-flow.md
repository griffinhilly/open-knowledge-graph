---
id: open-channel-flow
title: Open Channel Flow
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: reynolds-number
  type: soft
- id: dimensional-analysis-and-similarity
  type: soft
tags:
- open channel
- Manning's equation
- Froude number
- hydraulic jump
- critical flow
stage: formal-systems
status: draft
---

# Open Channel Flow

## Core Idea
Open channel flow has a free surface exposed to atmospheric pressure, making it fundamentally different from pipe flow. The Froude number Fr = V/√(gD) distinguishes subcritical (Fr < 1, disturbances propagate upstream) from supercritical (Fr > 1, disturbances cannot propagate upstream) flow. Manning's equation Q = (1/n)A·R_h^(2/3)·S^(1/2) relates discharge to channel geometry and slope. A hydraulic jump — a standing wave transition from supercritical to subcritical flow — dissipates energy and is analogous to a shock wave in gas dynamics.

## How It's Best Learned
Use specific energy diagrams to visualize how depth and velocity trade off at fixed discharge. Identify critical depth (minimum specific energy for given Q) and compute it for rectangular channels. Observe hydraulic jumps in a flume or kitchen sink to see the abrupt depth increase and energy dissipation.

## Common Misconceptions
- Faster flow (higher velocity) is not always 'supercritical'; the Froude number depends on both velocity and depth — a deep, fast river can be subcritical.
- Manning's n is an empirical roughness coefficient with units; unlike the Darcy-Weisbach approach, Manning's equation is not dimensionally consistent and requires SI or English unit conventions.
- A hydraulic jump always transitions from supercritical to subcritical, never the reverse — flow cannot jump from subcritical to supercritical.
