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
stage: expert
status: validated
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

## Questions

```yaml
- question: "An operator partially closes a valve downstream of a centrifugal pump. What happens to the pump curve, the system curve, and the operating point?"
  type: multiple-choice
  options:
    - "The pump curve shifts upward (pump works harder against the closed valve), system curve unchanged, operating point moves to higher flow and head"
    - "The pump curve is unchanged; the system curve steepens (more friction loss at any Q); the operating point shifts to lower flow and higher head"
    - "The pump curve steepens; the system curve steepens; the operating point moves to higher flow and lower head"
    - "Both curves shift upward proportionally; the operating point remains at the same flow rate but higher head"
  answer: 1
  explanation: "Throttling a valve does NOT change the pump curve — the pump's head-flow characteristic depends on impeller speed and geometry, not on downstream conditions. Closing a valve increases resistance in the system, increasing the coefficient k in H_sys = H_static + kQ². This steepens the system curve (more head required at any given flow rate). The new intersection of the unchanged pump curve with the steeper system curve is at a lower flow rate and higher head. This is a common misconception: operators often think they are 'making the pump work harder,' but they are actually causing it to operate at a different point on its existing curve."

- question: "A pump is drawing water from a reservoir with a suction lift of 5 meters. The operator raises the pump installation height, increasing the suction lift to 8 meters. All else equal, what happens to NPSH_available?"
  type: multiple-choice
  options:
    - "NPSH_available increases because the pump inlet velocity must be higher to draw fluid upward"
    - "NPSH_available is unchanged because NPSH depends only on the fluid's vapor pressure"
    - "NPSH_available decreases because the static pressure at the pump inlet falls as suction lift increases"
    - "NPSH_available decreases only if the fluid temperature also increases"
  answer: 2
  explanation: "NPSH_available = (P_inlet − P_vapor)/(ρg) + V²/(2g). P_inlet = P_atm − ρg·z_suction, where z_suction is the vertical distance the fluid must be lifted. As suction lift increases, P_inlet decreases, so NPSH_available decreases. If NPSH_available falls below NPSH_required (the manufacturer's minimum), cavitation begins: the fluid boils at the impeller inlet, forming vapor bubbles that collapse violently, eroding the impeller. This is why suction lift is strictly limited, and why hot fluids (high vapor pressure) or high altitudes (low atmospheric pressure) further reduce the margin."

- question: "Throttling a control valve downstream of a centrifugal pump changes the pump's operating characteristic curve, shifting its head-flow relationship."
  type: true-false
  answer: false
  explanation: "Throttling a valve changes the SYSTEM curve, not the pump curve. The pump curve is determined by the pump's impeller geometry and rotational speed — it is a physical property of the pump hardware. The system curve describes what the piping network demands. Throttling adds resistance to the system, steepening the system curve (more head required at any given flow). The operating point — the intersection of pump and system curves — moves to lower flow and higher head, but the pump is still operating on the same pump curve. Only changing impeller speed, impeller diameter, or using a different pump can shift the pump curve."

- question: "Two identical centrifugal pumps operating in parallel (with both pumping into the same discharge header) will together deliver approximately twice the flow rate at the same head as a single pump."
  type: true-false
  answer: true
  explanation: "Parallel operation adds the pumps' flows at each head value — the combined pump curve is constructed by doubling the flow at every head. This is correct because each pump still produces the same head (determined by impeller speed and geometry), but both contribute flow. The actual operating point depends on where this doubled-flow curve intersects the system curve, which typically results in somewhat less than double the flow (because higher flow increases system friction losses, moving up the steepened system curve). In series operation, the combined curve is constructed by adding heads at each flow value, which increases head at the same flow — appropriate for high-head, lower-flow applications."

- question: "Explain why you cannot independently choose both the flow rate and the head in a centrifugal pump system once the pump and piping system are fixed. What determines the actual operating condition?"
  type: short-answer
  answer: "The operating point is determined by physics, not choice. The pump curve — the head the pump supplies at each flow rate — is fixed by impeller speed and geometry. The system curve — the head the system demands at each flow rate — is fixed by static head and pipe resistance. The fluid settles at the flow rate where supply exactly equals demand (the intersection). If flow were above the intersection, the system would demand more head than the pump provides and flow would slow; if below, the pump would push harder than needed and flow would speed up. This self-correcting behavior locks the system to the intersection. To change flow, you must change one of the curves — by throttling (steepening system curve), changing pump speed (shifting pump curve), or modifying the piping."
  explanation: "The key insight is that the operating point is an emergent consequence of two physical constraints interacting, not a free parameter. This is why engineers must size pumps carefully: you cannot simply buy a 'bigger' pump to get more flow, because a more powerful pump on the same system curve will move the operating point along the system curve, giving more flow but also more head than needed. Proper pump selection requires matching the pump curve to the system curve so that their intersection falls near the pump's best efficiency point (BEP), where the pump operates most efficiently and reliably."
```

## Explainer

From your work on pipe system losses, you know that moving fluid through a network requires overcoming two kinds of resistance: static head (the elevation and pressure difference between source and destination) and dynamic head losses (the friction and minor losses that grow with flow rate). Together these define what the *system* demands from a pump at any given flow rate. From your introduction to hydraulic machinery, you have a sense of how a centrifugal pump works — an impeller spins, imparting kinetic energy to the fluid, which is converted to pressure in the volute. The **pump curve** captures that capability: it plots the head H the pump delivers against the volumetric flow rate Q. Centrifugal pump curves are characteristically drooping — high head at low flow, decreasing head as flow increases. This shape reflects the physics: at zero flow, all the impeller energy goes to pressure; as flow increases, friction and incidence losses mount.

The **system curve** is the mirror: it plots the total head the system demands at each flow rate. It has two components. The **static component** is the elevation difference plus any imposed pressure difference between the suction and discharge reservoirs — this is a constant, independent of Q. The **dynamic component** is all the pipe friction, valve, and fitting losses, which grow approximately as Q² (because h_f ∝ V² ∝ Q²). The system curve is therefore a parabola sitting on top of the static head offset: H_sys = H_static + kQ². The steeper the pipes, the more valves, or the narrower the diameter, the steeper k is and the steeper the parabola.

The **operating point** is where these two curves cross. At that intersection, the head the pump supplies exactly equals the head the system demands, and the flow rate settles there by self-regulation. If flow were higher than the operating point, the system would demand more head than the pump provides — flow slows down. If flow were lower, the pump would be pushing harder than needed — flow speeds up. This self-correcting mechanism is elegant, but it means you cannot choose flow rate and head independently once the pump and system are defined. If you close a valve, you steepen the system curve (increase k), shifting the intersection leftward and upward: lower flow, higher head. If you speed up the pump (using a variable-frequency drive), you stretch the pump curve upward, shifting the operating point rightward and upward: higher flow, higher head.

**NPSH** (Net Positive Suction Head) introduces a failure mode that doesn't show up in the H-Q diagram: cavitation. At the pump inlet, pressure must remain above the fluid's vapor pressure; otherwise the fluid boils locally, forming vapor bubbles that collapse violently as they reach higher pressure, eroding the impeller. NPSH_available = (P_inlet - P_vapor)/(ρg) + V_inlet²/(2g) — it is determined entirely by your system's suction piping, elevation, and fluid temperature. NPSH_required is a pump property specified by the manufacturer; it represents the minimum margin needed. The rule is simple: NPSH_A > NPSH_R at all operating conditions. Hot fluids (high vapor pressure), high suction lifts (low inlet pressure), and high flow rates (high velocity → low pressure by Bernoulli) all reduce NPSH_available. Understanding both the H-Q intersection and the NPSH constraint is necessary to properly select, size, and protect a pump in any real system.

