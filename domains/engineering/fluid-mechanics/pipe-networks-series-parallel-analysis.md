---
id: pipe-networks-series-parallel-analysis
title: 'Pipe Network Analysis: Series and Parallel Configurations'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: pipe-flow-network-analysis
  type: hard
- id: bernoullis-equation
  type: hard
- id: continuity-equation-fluid
  type: soft
builds-toward:
- pump-operating-point-curve-matching
tags:
- networks
- systems
- analysis
stage: advanced
status: draft
---

# Pipe Network Analysis: Series and Parallel Configurations

## Core Idea
Complex pipe systems with multiple branches and loops require systematic analysis satisfying pressure continuity and flow conservation at all junctions. The Hardy-Cross method iteratively adjusts flow distributions in each loop until pressure balances. Water distribution networks, heating systems, and industrial piping require this methodology to predict flow rates and pressure losses accurately.

## How It's Best Learned
Set up a looped pipe network model and solve it using Hardy-Cross iteration by hand for a small system (2-3 loops). Then use spreadsheet or software tools to scale to realistic networks and observe convergence. Verify with experimental measurements on constructed networks.

## Explainer

When you studied Bernoulli's equation and the continuity equation, you learned how to analyze a single pipe: given geometry and flow rate, compute pressure drop, or given pressure drop, compute flow rate. Real piping systems — municipal water distribution, HVAC hydronic loops, industrial process plants — are not single pipes. They are networks of interconnected branches that must simultaneously satisfy fluid conservation at every junction. This topic gives you the systematic framework to extend your single-pipe tools to networks of arbitrary complexity.

The governing principles are two conservation laws translated into network language, analogous to Kirchhoff's laws in electrical circuits. **Continuity at each node**: the sum of flows entering any junction equals the sum of flows leaving it — no fluid accumulates. **Pressure consistency in each loop**: if you trace a closed path through the network and sum up all the pressure changes (gains and losses), the total must be zero — pressure is a state variable, so you must return to your starting pressure after a complete loop. In a simple series configuration, the same flow passes through every pipe and the head losses add. In a parallel configuration, the head loss across each branch is equal (both ends share the same junction pressures), and the total flow splits among branches.

Series and parallel networks can be analyzed with simple algebra because there is only one unknown flow distribution consistent with the topology. But most real networks contain **loops** — multiple paths between two nodes — and this creates an underdetermined system: infinitely many flow distributions satisfy continuity at every node, but only one satisfies both continuity and pressure consistency. The **Hardy-Cross method** resolves this by guessing a set of flows that satisfies continuity, then iteratively correcting them until pressure balance is also achieved.

The correction procedure is elegant: for each loop, compute the head loss imbalance ΔH = Σ(h_L) around the loop using the guessed flows. Because head loss scales roughly as Q² (from your prerequisite knowledge of Darcy-Weisbach), a correction flow ΔQ = −ΔH / (2Σ|h_L/Q|) is applied to all pipes in the loop. This correction is derived by linearizing the head-loss function around the current guess. Each pipe that belongs to two loops gets corrections from both. After several rounds of iteration — typically 5–10 for engineering precision — the flow distribution converges to the unique solution satisfying both conservation laws in every element of the network. Modern software automates this, but understanding Hardy-Cross tells you exactly what the solver is doing and why it converges.
