---
id: pump-operating-point-curve-matching
title: 'Pump Operating Point: Curve Matching and System Selection'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: pump-system-curves
  type: hard
- id: pump-system-matching-operating-point
  type: hard
- id: bernoullis-equation
  type: soft
builds-toward:
- pump-affinity-laws-and-similarity
- cavitation-sigma-number-prediction
tags:
- pump
- operating-point
- system-curve
stage: formal-systems
status: draft
---

# Pump Operating Point: Curve Matching and System Selection

## Core Idea
A pump's performance curve (head H versus flow rate Q) intersects the system curve (total head = static head + friction head) at the operating point. This intersection determines actual flow rate, efficiency, and power consumption. Off-design operation (cavitation at inlet, surge in compressors, recirculation) occurs outside favorable ranges. Proper matching ensures safe, efficient operation and prevents damage from cavitation or vibration.

## How It's Best Learned
Plot pump characteristic curves from manufacturer data and draw system curves for different configurations (different pipe lengths, fittings, discharge elevations). Observe where they intersect and predict flow rate. Verify experimentally or adjust system design to achieve desired flow.
