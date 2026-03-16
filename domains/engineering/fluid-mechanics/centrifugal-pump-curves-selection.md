---
id: centrifugal-pump-curves-selection
title: Centrifugal Pump Performance Curves and System Selection
domain: engineering
course: fluid-mechanics
prerequisites:
- id: mechanical-energy-balance-pump-turbine
  type: hard
builds-toward:
- pump-system-matching-operating-point
tags:
- pumps
- performance
- head-capacity
stage: formal-systems
status: draft
---

# Centrifugal Pump Performance Curves and System Selection

## Core Idea
Pump manufacturers provide head-capacity curves (H vs. Q), efficiency curves, and power curves for specific pump models at rated speed. A pump operates at the intersection of its characteristic curve with the system resistance curve. Understanding pump curves enables prediction of operating flow rate and head, efficiency, and power consumption under different system conditions.

## Explainer

From the mechanical energy balance, you know that a pump adds head to a fluid and that the energy equation governs what head is required to move fluid from one point to another. A real pump cannot deliver arbitrary combinations of head and flow — its performance is characterized by a **head-capacity curve** (H–Q curve), which shows how much head the pump produces at each possible flow rate.

The H–Q curve has a characteristic shape: maximum head at zero flow (the **shutoff head**) and falling head as flow increases. This makes physical sense — the impeller is most effective at lifting fluid when nothing is flowing and progressively less effective as flow rate demands more energy to move fluid through the passages. Along with the H–Q curve, the manufacturer provides efficiency and **brake horsepower** (BHP) curves. The efficiency curve peaks at the **best efficiency point (BEP)** — the design condition where the pump converts shaft power to hydraulic energy most effectively. Operating far from BEP causes recirculation, vibration, and accelerated wear, which is why selecting a pump with the BEP near your design flow rate matters for reliability as much as for energy cost.

The **system curve** is the other half of the picture. The mechanical energy balance tells you that the head required to push flow through a piping system increases with flow rate — typically as H_system = H_static + R·Q², where H_static is the elevation and pressure difference to overcome and the R·Q² term captures friction and minor losses (which scale approximately with the square of velocity, hence Q²). Plotting the system curve and pump H–Q curve together on the same axes, the **operating point** is their intersection — the only combination of H and Q where both the pump and the system are simultaneously satisfied.

Pump selection means choosing a pump whose H–Q curve intersects the system curve at or near the BEP for the desired design flow rate. If the system needs 500 GPM at 80 ft of head, you need a pump whose curve passes through that point at good efficiency. If you need more flow than one pump can provide, pumps in **parallel** add their flow rates at the same head — the combined H–Q curve is the horizontal sum of the individual curves. If you need more head than one pump can provide, pumps in **series** add heads at the same flow rate — the combined curve is the vertical sum. In both cases, the combined curve intersects the system curve at the new operating point, which you read off to find the actual delivered flow and head.
