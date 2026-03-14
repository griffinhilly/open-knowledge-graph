---
id: hydraulic-machinery-intro
title: 'Hydraulic Machinery: Pumps and Turbines'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: pipe-system-losses
  type: soft
- id: dimensional-analysis-and-similarity
  type: soft
- id: control-volume-momentum
  type: soft
tags:
- pumps
- turbines
- pump curve
- system curve
- specific speed
- NPSH
stage: formal-systems
status: validated
---
# Hydraulic Machinery: Pumps and Turbines

## Core Idea
Pumps add energy to a fluid; turbines extract it. The operating point of a pump-system combination is found at the intersection of the pump head-flow curve (H-Q curve) and the system curve (which includes static head plus friction losses as a function of Q). Similarity laws (affinity laws) — derived from dimensional analysis — relate pump performance at different speeds: Q∝N, H∝N², Power∝N³. Net Positive Suction Head (NPSH) must be checked to prevent cavitation at the pump inlet.

## How It's Best Learned
Plot a pump H-Q curve and a system curve on the same axes; the intersection is the operating point. Apply affinity laws to determine the effect of changing pump speed. Calculate NPSH available vs. required to identify cavitation risk, adjusting inlet pipe geometry as needed.

## Common Misconceptions
- A pump curve shows head produced at each flow rate, not what the pump delivers to the fluid regardless of the system — the actual operating point depends on both curves.
- Cavitation occurs when local pressure drops below vapor pressure, causing bubble collapse that damages impellers — it is not just 'boiling' but a damaging collapse event.
- Specific speed is a dimensionless (or quasi-dimensional) design parameter that categorizes pump type (centrifugal, mixed-flow, axial); it is evaluated at the best efficiency point, not at arbitrary conditions.
