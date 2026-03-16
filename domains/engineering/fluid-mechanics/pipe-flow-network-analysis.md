---
id: pipe-flow-network-analysis
title: Pipe Flow Network Analysis and System Design
domain: engineering
course: fluid-mechanics
prerequisites:
- id: pipe-system-losses
  type: hard
- id: friction-factor-darcy-weisbach-equation
  type: soft
tags:
- pipe-flow
- systems
- design
stage: formal-systems
status: draft
---

# Pipe Flow Network Analysis and System Design

## Core Idea
Complex piping systems are analyzed using energy balance equations combined with continuity at junctions and compatibility of pressure drops. For series pipes, head losses add; for parallel pipes, pressure drops are equal. Pump operation is determined by matching the system curve (pressure drop vs. flow rate) with the pump curve, and valve sizing controls flow distribution.

## How It's Best Learned
Analyze and solve actual piping system problems using energy balance spreadsheets. Plot both pump curves and system curves together to find operating point, and observe how changes in pipe diameter or length shift the system curve.

## Common Misconceptions
- Adding a parallel pipe always increases total flow by a constant amount (flow increase depends on system resistance; lower resistance systems see smaller percentage increase).
- Pump efficiency is independent of operating point (pump efficiency varies significantly with flow rate; operation at design point maximizes efficiency).

## Explainer

A single pipe carrying fluid from one point to another obeys the Darcy-Weisbach equation you already know: the head loss h_L = f (L/D)(V²/2g) depends on pipe geometry and flow velocity. A **pipe network** extends this to interconnected systems — branching distribution mains, building HVAC loops, irrigation grids — where multiple pipes share fluid and energy. Two governing laws apply at every junction: **continuity** (what flows in must flow out, ΣQ = 0) and **energy compatibility** (the head loss between any two nodes is the same regardless of which path you take). These are the pipe-flow analogues of Kirchhoff's current and voltage laws.

The two limiting cases are series and parallel configurations. In a **series** arrangement, the same flow rate Q passes through every pipe, and head losses simply add: h_total = h_L1 + h_L2 + ···. This means a long thin pipe and a short fat pipe in series impose their head loss penalties consecutively — the bottleneck controls. In a **parallel** arrangement, the total flow splits among branches, but each branch sees the same pressure drop: h_L1 = h_L2 = ···. Flow distributes itself so that every branch dissipates identical head per unit of the path. Pipes with lower resistance (larger diameter or shorter length) carry more flow; pipes with higher resistance carry less. Solving for the split requires iterating or solving simultaneous equations.

A **pump** in the system is characterized by its **pump curve** — a manufacturer-supplied plot of head added (H_pump) versus flow rate Q, which typically shows head decreasing as flow increases. The piping system has its own **system curve** — head required versus flow, which increases with Q because friction losses scale as Q² through Darcy-Weisbach. The **operating point** is the intersection of these two curves: the unique Q at which the pump supplies exactly the head the system demands. Shifting the system curve by adding pipe length, closing a valve, or adding a parallel branch moves the operating point along the pump curve, changing both the delivered flow and the pump efficiency. Real pump selection requires ensuring the operating point falls near the pump's best efficiency point (BEP).

For complex networks with multiple loops and sources, Hardy-Cross iteration is the classical method: guess flow in each pipe, check if head loss around each loop closes to zero (loop equation), and apply corrections proportional to the imbalance until convergence. Modern engineers use software for this, but the underlying equations are the same. The key habit is always checking units and signs: head losses are positive in the direction of assumed flow, and sign errors in loop equations are the most common source of wrong answers.
