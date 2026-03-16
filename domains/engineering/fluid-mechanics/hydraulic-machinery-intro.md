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

## Explainer

Bernoulli's equation tells you that energy per unit weight of fluid — called **head** — can be expressed as a sum of pressure head, velocity head, and elevation head. A pump's job is to add head to the flow; a turbine's job is to extract it. The **H-Q curve** (pump characteristic curve) shows how much head a centrifugal pump delivers at each flow rate: at zero flow, head is maximum (the shutoff head); as flow increases, head decreases because more energy is lost overcoming internal flow velocities. This inverse relationship is the fundamental shape of every centrifugal pump curve.

The **system curve** represents what the system demands: it is the sum of static head (the fixed elevation difference the pump must overcome regardless of flow) and dynamic head losses (pipe friction, fittings, valves — all of which scale approximately as Q²). The system curve always starts at the static head value and rises parabolically. Where these two curves intersect is the **operating point** — the one flow rate and head at which supply exactly meets demand. If you increase flow demand (open a valve), the system curve flattens, the operating point shifts right, and the pump delivers more flow at lower head. This graphical intersection method is the core tool for pump-system design.

The **affinity laws**, derived from dimensional analysis and similarity, are among the most useful rules in fluid machinery. When you change pump speed from N₁ to N₂: flow scales as Q ∝ N, head scales as H ∝ N², and power scales as P ∝ N³. The cubic relationship between power and speed is why variable-speed drives save so much energy — reducing pump speed by 20% reduces power consumption by nearly 50%. The same laws apply to geometrically similar pumps of different sizes (scaled by diameter), making them invaluable for selecting among a family of impeller sizes.

**Net Positive Suction Head (NPSH)** connects directly to cavitation. NPSH_available is the absolute pressure at the pump inlet expressed as head, minus the vapor pressure head of the liquid — it tells you how much pressure margin exists before cavitation. NPSH_required is specified by the pump manufacturer based on testing; it represents the margin the pump needs to avoid internal cavitation. The design rule is simply NPSH_available > NPSH_required with some safety factor. NPSH_available decreases when the pump is positioned high above the liquid source, when suction pipe losses are large, when liquid temperature is high (increasing vapor pressure), or when operating at high altitude. Every pump installation must verify this inequality before commissioning.
