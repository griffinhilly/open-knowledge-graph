---
id: autonomous-equations-phase-lines
title: Autonomous Equations and Phase Lines
domain: mathematics
course: differential-equations
prerequisites:
- id: existence-uniqueness-ode
  type: hard
- id: first-derivative-test
  type: hard
builds-toward:
- bifurcation-analysis-ode
- stability-classification
tags:
- autonomous
- phase-line
- qualitative-analysis
stage: formal-systems
status: draft
---

# Autonomous Equations and Phase Lines

## Core Idea
An autonomous ODE dy/dx = f(y) has no explicit x-dependence. Solutions can be analyzed qualitatively using a phase line: equilibria (where f(y) = 0) divide the line into regions where solutions flow toward stable equilibria (sinks) or away from unstable ones (sources). This geometric approach provides deep understanding without solving the equation explicitly.

## Explainer

An **autonomous ODE** is a differential equation of the form dy/dt = f(y) where the right-hand side depends only on y, not on t. The absence of explicit time dependence is the key feature: the rate of change of y is determined entirely by the current value of y, not by when you're observing it. Population models, cooling laws, and many physical equilibria take this form. Because the equation doesn't depend on t, you can analyze its qualitative behavior without finding a single explicit formula for y(t).

The starting point is finding **equilibrium solutions**: values y* where f(y*) = 0. At these values, dy/dt = 0, so the solution is constant — the system sits still. But equilibria tell you more than just where the system pauses. From your work with the first derivative test, you know that the sign of a function tells you whether a quantity is increasing or decreasing. Here, f(y) plays that role: wherever f(y) > 0, solutions are increasing (y is climbing); wherever f(y) < 0, solutions are decreasing (y is falling).

The **phase line** is a one-dimensional diagram that captures this information. Mark the equilibria on a vertical line representing y-values. Between consecutive equilibria, f(y) has constant sign, so draw arrows pointing up (f > 0) or down (f < 0). These arrows show the direction solutions flow. An equilibrium is a **sink** (stable) if arrows on both sides point toward it — any solution that starts nearby will be attracted to it over time. It is a **source** (unstable) if arrows point away — nearby solutions diverge from it. A **node** has arrows pointing in from one side and out from the other (semi-stable).

This analysis gives a complete qualitative picture without solving the ODE: you know where solutions end up, which starting values lead to which behaviors, and how sensitive the long-run outcome is to initial conditions. The existence-uniqueness theorem you studied guarantees that solution curves starting at different initial conditions cannot cross each other, which is what makes the phase-line picture logically consistent. Each initial value y₀ determines exactly one solution trajectory, and the arrows on the phase line tell you exactly where that trajectory goes as t → ∞.
