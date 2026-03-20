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
stage: advanced
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

## Explainer

From your work on pipe system losses, you know that moving fluid through a network requires overcoming two kinds of resistance: static head (the elevation and pressure difference between source and destination) and dynamic head losses (the friction and minor losses that grow with flow rate). Together these define what the *system* demands from a pump at any given flow rate. From your introduction to hydraulic machinery, you have a sense of how a centrifugal pump works — an impeller spins, imparting kinetic energy to the fluid, which is converted to pressure in the volute. The **pump curve** captures that capability: it plots the head H the pump delivers against the volumetric flow rate Q. Centrifugal pump curves are characteristically drooping — high head at low flow, decreasing head as flow increases. This shape reflects the physics: at zero flow, all the impeller energy goes to pressure; as flow increases, friction and incidence losses mount.

The **system curve** is the mirror: it plots the total head the system demands at each flow rate. It has two components. The **static component** is the elevation difference plus any imposed pressure difference between the suction and discharge reservoirs — this is a constant, independent of Q. The **dynamic component** is all the pipe friction, valve, and fitting losses, which grow approximately as Q² (because h_f ∝ V² ∝ Q²). The system curve is therefore a parabola sitting on top of the static head offset: H_sys = H_static + kQ². The steeper the pipes, the more valves, or the narrower the diameter, the steeper k is and the steeper the parabola.

The **operating point** is where these two curves cross. At that intersection, the head the pump supplies exactly equals the head the system demands, and the flow rate settles there by self-regulation. If flow were higher than the operating point, the system would demand more head than the pump provides — flow slows down. If flow were lower, the pump would be pushing harder than needed — flow speeds up. This self-correcting mechanism is elegant, but it means you cannot choose flow rate and head independently once the pump and system are defined. If you close a valve, you steepen the system curve (increase k), shifting the intersection leftward and upward: lower flow, higher head. If you speed up the pump (using a variable-frequency drive), you stretch the pump curve upward, shifting the operating point rightward and upward: higher flow, higher head.

**NPSH** (Net Positive Suction Head) introduces a failure mode that doesn't show up in the H-Q diagram: cavitation. At the pump inlet, pressure must remain above the fluid's vapor pressure; otherwise the fluid boils locally, forming vapor bubbles that collapse violently as they reach higher pressure, eroding the impeller. NPSH_available = (P_inlet - P_vapor)/(ρg) + V_inlet²/(2g) — it is determined entirely by your system's suction piping, elevation, and fluid temperature. NPSH_required is a pump property specified by the manufacturer; it represents the minimum margin needed. The rule is simple: NPSH_A > NPSH_R at all operating conditions. Hot fluids (high vapor pressure), high suction lifts (low inlet pressure), and high flow rates (high velocity → low pressure by Bernoulli) all reduce NPSH_available. Understanding both the H-Q intersection and the NPSH constraint is necessary to properly select, size, and protect a pump in any real system.

