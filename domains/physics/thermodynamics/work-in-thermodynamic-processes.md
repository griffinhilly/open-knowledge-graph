---
id: work-in-thermodynamic-processes
title: Work in Thermodynamic Processes
domain: physics
course: thermodynamics
prerequisites:
- id: ideal-gas-law
  type: hard
- id: work-and-energy
  type: hard
- id: work-as-integral
  type: soft
- id: definite-integral-definition
  type: soft
builds-toward:
- first-law-of-thermodynamics
- thermodynamic-processes
tags:
- thermodynamic-work
- PV-work
- expansion
- compression
- area-under-PV-curve
stage: formal-systems
status: validated
---

# Work in Thermodynamic Processes

## Core Idea
In thermodynamics, work done by a gas expanding against an external pressure is W = ∫P dV. For a process on a PV diagram, work equals the area under the P-V curve. Work is positive when a gas expands (does work on surroundings) and negative when compressed (surroundings do work on the gas). The work done in a cyclic process — traversing a closed loop on a PV diagram — equals the enclosed area, and its sign depends on whether the loop is traversed clockwise (net positive work out) or counterclockwise.

## How It's Best Learned
Calculate work graphically from PV diagrams before applying formulas. Compare work done along different paths between the same two states — this path-dependence is fundamental and distinguishes work and heat from state functions like internal energy.

## Common Misconceptions
- Work in thermodynamics is not simply force times distance — it is pressure times change in volume.
- Work is path-dependent: different processes connecting the same initial and final states generally do different amounts of work.
- Sign conventions vary by text; always establish whether W is work done BY the gas or ON the gas.

## Explainer

You already know work in mechanics: force applied over a distance. In thermodynamics, the same idea applies to gases, but the "force" is pressure and the "distance" is volume change. When a gas expands and pushes a piston outward, it exerts pressure P over an area A, moving the piston a small distance dx. Force times distance gives P·A·dx = P·dV. Summing over the entire expansion gives W = ∫P dV — the **PV work** formula. This is not a new concept; it is force-times-distance expressed in terms of fluid variables.

The **PV diagram** is the key visual tool. Plot pressure on the y-axis and volume on the x-axis, and any thermodynamic process becomes a path drawn on that plane. The work done by the gas along any path equals the area under the curve — literally the geometric area between the curve and the V-axis. An isobaric (constant-pressure) process is a horizontal line; its area is a simple rectangle, W = PΔV. A more complex process traces a curved path, and you compute the area by integration. The sign rule is intuitive: when volume increases (gas expands), work is positive — the gas pushes outward and does work on its surroundings. When volume decreases (compression), work is negative — the surroundings do work on the gas.

Here is where path-dependence becomes crucial. Your prerequisite knowledge of integrals tells you that ∫P dV depends on how P varies with V along the entire path, not just the endpoints. Two processes starting at the same state (P₁, V₁) and ending at the same state (P₂, V₂) but following different curves in between will trace different areas — and therefore do different amounts of work. This makes work a **path function**, not a state function. Internal energy is a state function (it depends only on where you are); work is not. This distinction is the conceptual heart of the First Law, which you'll encounter next.

Cyclic processes — closed loops on the PV diagram — are especially important for understanding heat engines. When the system traverses a clockwise loop, the area enclosed equals net work output: the gas does more work expanding (bottom of loop, lower pressure) than the surroundings do compressing it (top of loop, higher pressure). A counterclockwise loop means net work is done on the gas — this is a refrigerator cycle. The enclosed area, regardless of direction, is the magnitude of the net work. Memorizing the clockwise = positive convention is less important than understanding why: the expanding path has a larger area under it than the compressing return path when the loop runs clockwise.
