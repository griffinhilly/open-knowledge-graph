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

## Explainer

A pump does not deliver a fixed flow rate — it delivers whatever flow the system will accept given the head the pump provides. This is a mutual constraint, and understanding it requires thinking about two distinct curves that exist simultaneously. The **pump characteristic curve** (or pump curve) comes from the manufacturer: it plots the head H the pump adds to the fluid as a function of flow rate Q. At zero flow (shutoff), the pump delivers maximum head; as flow increases, head drops. This shape comes from the impeller geometry and rotational speed. The **system curve** comes from the piping and elevation: it plots the total head required to push flow through the system at various flow rates. It has two parts — a static component (elevation difference, regardless of flow) and a dynamic component (friction losses that grow roughly as Q²). The system curve always curves upward.

The **operating point** is where these two curves intersect. At that intersection, the head the pump provides exactly equals the head the system demands — the system and pump are in equilibrium. If the pump tried to deliver more head, the flow rate would be more than the system needs, and flow would increase until balance is restored; if less head, flow would decrease. This self-correcting mechanism makes the intersection uniquely stable. From Bernoulli's equation — your prerequisite — you can write the system curve explicitly: H_system = Δz + (f·L/D + ΣK)·V²/2g, where Δz is static head and the friction term scales with V² ∝ Q². Superimposing this on the pump curve gives the operating point directly.

Matching pump to system requires choosing or modifying curves so that the operating point falls near the pump's **best efficiency point** (BEP). The BEP is the flow rate where the pump converts shaft power to fluid energy most efficiently; operating far from it wastes energy and accelerates wear. If the operating point is too far to the left (low flow), the pump may experience recirculation at the inlet — flow reverses near the impeller eye, causing noise and vibration. Too far to the right, and **cavitation** becomes a risk: the local pressure at the inlet drops below vapor pressure, forming vapor bubbles that collapse violently on the impeller. You can shift the operating point without changing the pump by altering the system curve — adding pipe resistance (throttle valve) steepens the curve and moves the operating point left; removing resistance moves it right.

System engineers often need to achieve a specific design flow rate. The process is: (1) compute the system curve from pipe geometry and elevation, (2) obtain pump curves for candidate pumps, (3) find the intersection and check it falls near BEP, and (4) if not, adjust pipe sizing or select a different pump. Multiple pumps in series add their head curves (useful for high-head, low-flow applications); pumps in parallel add their flow curves (useful for high-flow, modest-head applications). In each case the same graphical intersection method applies — the combined pump curve intersects the single system curve to give the new operating point.
