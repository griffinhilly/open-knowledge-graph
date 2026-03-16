---
id: steady-state-analysis-growth
title: Steady-State Analysis in Growth Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: eigenvalues-eigenvectors
  type: hard
- id: systems-of-linear-equations
  type: hard
builds-toward:
- golden-rule-capital-accumulation
tags:
- equilibrium-analysis
- long-run-growth
- dynamics
stage: advanced
status: draft
---

# Steady-State Analysis in Growth Models

## Core Idea
A steady state in growth models is a balanced-growth path where all variables grow at constant rates and capital-to-labor ratios remain constant. Analyzing steady-state properties reveals long-run equilibrium capital stocks, consumption levels, and growth rates that determine welfare. Stability analysis around the steady state shows whether economies converge to equilibrium or diverge after disturbances, providing crucial insights into long-run economic behavior.

## Explainer

In a growth model like the Solow model, the economy accumulates capital over time: workers save part of their income, and that saving becomes new machines, buildings, and equipment. But capital also depreciates — it wears out. The **steady state** is the point where these two forces exactly balance: new investment replaces depreciated capital, and the capital-per-worker ratio stops changing. Think of it like filling a bathtub with a slow leak — the steady state is the water level where inflow equals outflow. Once you reach it, the water level holds constant even though water keeps flowing in and draining out.

To find the steady state mathematically, you set the change in the capital-per-worker ratio to zero and solve the resulting equation. In the Solow model, this means solving sf(k) = (n + δ)k, where s is the savings rate, f(k) is per-capita output, n is population growth, and δ is the depreciation rate. The solution k* gives you the long-run capital stock, and from it you can derive steady-state output, consumption, and investment. The power of this approach is that it collapses a dynamic system — one that evolves over time — into a single algebraic problem about where the system eventually rests.

But finding the steady state is only half the question. You also need to know whether the economy actually converges to it after a shock, and this is where your background in **eigenvalues** and **systems of linear equations** becomes essential. To analyze stability, you linearize the dynamic system around the steady state — essentially taking a first-order Taylor approximation — and examine the eigenvalues of the resulting Jacobian matrix. If all eigenvalues have negative real parts, the steady state is **stable**: small perturbations decay over time and the economy returns to equilibrium. If any eigenvalue has a positive real part, the system is unstable in that direction, meaning some shocks push the economy permanently away from the steady state.

In richer models like the Ramsey-Cass-Koopmans model, the steady state involves two variables (capital and consumption), and the linearized system produces a 2×2 matrix with two eigenvalues. The typical result is one negative and one positive eigenvalue, creating a **saddle-point stability**: there is exactly one path — the **saddle path** — along which the economy converges to the steady state. All other paths eventually diverge. This is why forward-looking agents must "jump" to the saddle path immediately after a shock; any other initial consumption choice leads to an economically impossible outcome (zero consumption or infinite capital). The eigenvalue structure thus determines not just whether the economy converges, but how it converges and what the transition dynamics look like along the way.
