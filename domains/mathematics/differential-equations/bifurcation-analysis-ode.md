---
id: bifurcation-analysis-ode
title: Bifurcation Analysis in ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: autonomous-equations-phase-lines
  type: hard
- id: implicit-differentiation
  type: soft
builds-toward:
- linearization-nonlinear-systems
tags:
- bifurcation
- parameter-variation
- dynamical-systems
stage: advanced
status: draft
---

# Bifurcation Analysis in ODEs

## Core Idea
Bifurcation occurs when a small change in a parameter causes qualitative changes in solution behavior. Common types include saddle-node (equilibria collide and annihilate), transcritical (equilibria exchange stability), and pitchfork (one stable state splits into two). Bifurcation analysis reveals how systems transition between regimes as parameters vary.

## Explainer

From your work on autonomous equations and phase lines, you know how to classify a fixed point as stable or unstable based on whether the phase line arrows point toward it or away from it. That analysis was done for a given equation. Bifurcation analysis asks a deeper question: what happens to the structure of the phase line — the number and stability of equilibria — as a **parameter** in the equation varies continuously? Sometimes the answer is "nothing changes"; sometimes crossing a critical parameter value causes the entire qualitative picture to reorganize.

The simplest example is the **saddle-node bifurcation**. Consider dx/dt = r + x². The equilibria satisfy r + x² = 0, so x = ±√(−r). When r < 0, two equilibria exist: a stable one at x = −√(−r) and an unstable one at x = +√(−r). As r increases toward zero, these two equilibria approach each other. At r = 0 they collide into a single non-isolated equilibrium at x = 0. For r > 0, there are no real equilibria at all — the phase line is now a single arrow pointing in one direction, and any initial condition flows off to infinity. Two equilibria appeared from nowhere (or vanished), which is the defining signature of a saddle-node bifurcation.

In a **transcritical bifurcation**, two equilibria always exist but exchange stability as the parameter crosses a critical value. The canonical form is dx/dt = rx − x². The equilibria are x = 0 and x = r. When r < 0, x = 0 is stable and x = r (negative) is unstable; when r > 0, x = r is stable and x = 0 is unstable. They swap roles at r = 0 when they coincide. The **pitchfork bifurcation** is the symmetric version: at the critical parameter value, one stable equilibrium splits into two stable ones with an unstable one between them (supercritical pitchfork), or one unstable equilibrium spawns two unstable flankers and a stable center disappears (subcritical). Pitchfork bifurcations arise naturally in systems with left-right symmetry.

The primary tool for visualizing this is the **bifurcation diagram**: plot the parameter r on the horizontal axis and the equilibrium values on the vertical axis. Solid curves indicate stable branches; dashed curves indicate unstable branches. The saddle-node bifurcation looks like a parabola — the two branches meet at a fold point. The transcritical looks like a crossing X. The supercritical pitchfork looks like a pitchfork tine splitting from a single stem. Reading the bifurcation diagram tells you instantly how many equilibria exist for any parameter value, and whether they are stable — information that would require re-drawing the phase line separately for each parameter value otherwise.
