---
id: pump-system-curves
title: Pump and System Curves
domain: engineering
course: fluid-mechanics
prerequisites:
- id: hydraulic-machinery-intro
  type: hard
- id: pipe-system-losses
  type: hard
tags:
- pump curve
- system curve
- operating point
- NPSH
- pump selection
- cavitation
stage: formal-systems
status: draft
---
# Pump and System Curves

## Core Idea
A centrifugal pump's performance is described by its characteristic curve: head H vs. flow rate Q, typically showing head decreasing as flow rate increases. The system curve represents the total head the pump must overcome — the sum of static lift (elevation change plus pressure difference) and friction losses, where the friction component grows approximately as Q² (since h_f ∝ V² ∝ Q²). The operating point is the intersection of the pump curve and system curve, where the head supplied by the pump exactly matches the head required by the system. If the system changes (e.g., a valve closes, increasing friction losses), the system curve shifts up and the operating point moves to lower Q and higher H. Net Positive Suction Head (NPSH) ensures the pump inlet pressure stays above the fluid's vapor pressure to prevent cavitation: NPSH_available (determined by the system) must exceed NPSH_required (specified by the manufacturer) at all operating conditions.

## How It's Best Learned
Plot a pump curve and a system curve on the same H-Q axes and identify the operating point. Then modify the system — add pipe length, close a valve, raise the discharge tank — and re-plot the system curve to see how the operating point shifts. Calculate NPSH_available for a pump drawing from a reservoir at various elevations and temperatures, and compare against NPSH_required to determine the maximum allowable suction lift. Analyze what happens when two identical pumps operate in series (heads add at same Q) vs. parallel (flows add at same H).

## Common Misconceptions
- The operating point is not where the pump "wants" to run — it is dictated by the intersection of the pump and system curves. Throttling a valve does not change the pump curve; it steepens the system curve and moves the operating point.
- NPSH_available decreasing below NPSH_required does not immediately destroy the pump. It causes cavitation — vapor bubble formation and collapse — which initially reduces performance (head and flow drop) and over time causes erosion damage to impeller surfaces.
- Running a pump at shut-off (zero flow, maximum head) or at run-out (maximum flow, near-zero head) are both damaging. At shut-off, all energy goes to heating the fluid; at run-out, NPSH margin vanishes and structural loads increase. Pumps should operate near their best efficiency point (BEP).
