---
id: autonomous-equations
title: Autonomous Equations and Equilibrium Solutions
domain: mathematics
course: differential-equations
prerequisites:
- id: separable-differential-equations
  type: hard
builds-toward:
- phase-line-analysis
- bifurcation-in-odes
- stability-classification
tags:
- first-order
- qualitative
- equilibrium
stage: formal-systems
status: draft
---

# Autonomous Equations and Equilibrium Solutions

## Core Idea
An autonomous ODE has the form dy/dx = f(y), depending only on y, not on x. Equilibrium solutions occur where f(y) = 0. Autonomous equations are time-independent, making them ideal for studying long-term behavior and stability without explicitly solving.

## Explainer

From separable equations, you know how to solve dy/dx = g(x)h(y) by separating and integrating. An **autonomous equation** is the special case where there is no x on the right-hand side at all: dy/dx = f(y). The rate of change depends only on the current value of y, not on when or where you are. A population growing at a rate proportional to its size, dy/dt = ky, is autonomous. So is the logistic equation dy/dt = ry(1 − y/K). The defining feature is that the behavior of the system is fully determined by where y currently is, not by the value of t.

**Equilibrium solutions** (also called **steady states** or **fixed points**) are constant solutions y(x) = c where f(c) = 0. At these values, the rate of change is zero, so if the system ever reaches an equilibrium, it stays there. To find them, just solve the algebraic equation f(y) = 0. For dy/dt = y(1 − y), the equilibria are y = 0 and y = 1.

The more important question than "what are the equilibria?" is "are they stable?" A **stable equilibrium** (also called a **sink** or attractor) pulls nearby solutions toward it. An **unstable equilibrium** (also called a **source** or repeller) pushes nearby solutions away. You can determine stability without solving the ODE: if f(y) > 0 just below the equilibrium and f(y) < 0 just above it, then solutions are pushed upward from below and downward from above — toward the equilibrium — making it stable. The opposite sign pattern means unstable.

This analysis is the basis for the **phase line**: a number line displaying the equilibria as points, with arrows indicating the sign of f(y) between them. A solution starting anywhere on the phase line follows the arrows in the direction they indicate. The phase line gives you the complete qualitative picture of every solution's long-run behavior without integrating a single equation. This geometric approach to ODEs — understanding the shape of solutions from f(y) alone — is one of the most powerful ideas in the subject, and it extends to higher-dimensional systems in your upcoming work on phase planes and stability classification.
